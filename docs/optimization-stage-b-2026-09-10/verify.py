"""Read-only stage-B compatibility checks, not a general lint or scientific review.
Usage: python docs/optimization-stage-b-2026-09-10/verify.py --baseline <snapshot-dir>
Requires PyYAML already available in the current environment.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('--baseline', required=True)
args = parser.parse_args()
snapshot = Path(args.baseline).resolve()
results = []


def text(rel, before=False):
    return ((snapshot / 'files' if before else ROOT) / rel).read_text(encoding='utf-8-sig')


def check(name, ok):
    if not ok:
        raise AssertionError(name)
    results.append(name)


def section(content, number):
    return re.search(r'(?ms)^## ' + str(number) + r'\. .*?(?=^## |\Z)', content).group(0)


protected = json.loads((snapshot / 'protected-hashes.json').read_text(encoding='utf-8'))
members = {p.relative_to(ROOT).as_posix() for p in (ROOT / 'directions').rglob('*') if p.is_file()}
check('direction_members_unchanged', members == {p for p in protected if p.startswith('directions/')})
check('directions_and_registry_byte_identical', all(
    hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() == digest for rel, digest in protected.items()))
check('hard_memory_byte_identical', (ROOT / 'memory/hard_memory.md').read_bytes()
      == (snapshot / 'files/memory/hard_memory.md').read_bytes())
for number in [1, 2, 3, 4, 5, 6, 8]:
    check('root_protected_section_' + str(number), section(text('AGENTS.md'), number)
          == section(text('AGENTS.md', True), number))
for number in [2, 3, 4, 5, 8]:
    check('reader_source_coverage_evidence_section_' + str(number),
          section(text('agents/pdf_read_agent.md'), number)
          == section(text('agents/pdf_read_agent.md', True), number))

paper = text('templates/paper.md')
old_paper = text('templates/paper.md', True)
fm = lambda s: yaml.safe_load(s.split('---', 2)[1])
check('paper_metadata_schema_and_defaults_preserved', fm(paper) == fm(old_paper))
headings = re.findall(r'^## (.+)$', paper, re.M)
check('downstream_entry_headings_preserved', all(x in headings for x in [
    'Study Design', 'Key Evidence', 'Conclusions for Reuse', 'Downstream Review']))
check('finding_inside_reuse_section', bool(re.search(
    r'(?s)## Conclusions for Reuse\n(?:(?!\n## ).)*### Finding 1', paper)))
check('stable_e1_heading_preserved', bool(re.search(r'^### E1$', paper, re.M)))
check('no_second_fillable_evidence_card', not re.search(
    r'^### E\d+|^- (?:Claim|Evidence IDs|Source locator):', text('templates/pdf_ingestion_template.md'), re.M))
check('standalone_duplicate_output_sections_removed', all(x not in headings for x in [
    'Takeaway', 'Findings and Interpretation', 'Notes for Review Writing', 'Linked Pages', 'Maintenance']))

bundle = ['templates/paper.md', 'templates/pdf_ingestion_template.md', 'agents/pdf_read_agent.md']
metrics = {rel: {'chars_before': len(text(rel, True)), 'chars_after': len(text(rel)),
                 'lines_before': len(text(rel, True).splitlines()),
                 'lines_after': len(text(rel).splitlines())} for rel in bundle}
print(json.dumps({'checks_passed': len(results), 'checks': results,
    'direction_files_compared': len(members), 'metrics': metrics,
    'bundle_chars_before': sum(v['chars_before'] for v in metrics.values()),
    'bundle_chars_after': sum(v['chars_after'] for v in metrics.values()),
    'limitations': ['No actual paper reading or user dialogue executed',
        'No proof of scientific accuracy or runtime savings',
        'Recording triggers reviewed as rules, not enforced by runtime code']}, indent=2))
