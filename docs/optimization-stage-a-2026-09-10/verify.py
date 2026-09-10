"""Focused stage-A regression checks; not a general lint or Obsidian UI test.

Usage: python docs/optimization-stage-a-2026-09-10/verify.py --baseline <snapshot-dir>
The snapshot directory must contain baseline.json and files/. Reads only; JSON to stdout.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('--baseline', required=True)
args = parser.parse_args()
snapshot = Path(args.baseline).resolve()
baseline = json.loads((snapshot / 'baseline.json').read_text(encoding='utf-8'))
results = []


def read(rel):
    return (ROOT / rel).read_text(encoding='utf-8-sig')


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    results.append(name)


profile = 'directions/ceramic-corrosion/memory/project_profile.md'
direction_files = {p.relative_to(ROOT).as_posix() for p in (ROOT / 'directions').rglob('*') if p.is_file()}
check('direction_members_unchanged', direction_files == {p for p in baseline if p.startswith('directions/')})
check('direction_bytes_unchanged_except_profile', all(
    hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() == baseline[rel]
    for rel in direction_files if rel != profile))
check('registry_unchanged', hashlib.sha256((ROOT / 'memory/direction_registry.yaml').read_bytes()).hexdigest()
      == baseline['memory/direction_registry.yaml'])

agents = list((ROOT / 'agents').glob('*.md'))
templates = list((ROOT / 'templates').glob('*.md'))
check('no_external_evidence_suffix_in_active_examples', all(
    not re.search(r'\]\]#E\d+', p.read_text(encoding='utf-8-sig')) for p in agents + templates))
references = [(p, x) for p in agents + templates
              for x in re.findall(r'\[\[D/wiki/papers/Paper#E1\]\]', p.read_text(encoding='utf-8-sig'))]
check('six_corrected_example_references', len(references) == 6)

# Only full-path Wikilinks to exact ATX headings; no aliases, blocks, embeds,
# duplicate-heading disambiguation or desktop rendering is implemented here.
fixture_path = 'directions/fixture-a/wiki/papers/Paper'
paper = read('templates/paper.md').replace('{{direction_id}}', 'fixture-a').replace('{{title}}', 'Fixture')
fixture = {fixture_path: paper, 'directions/fixture-a/wiki/papers/Legacy': '### E1 - Original label\n\nEvidence text.\n'}


def resolves(link):
    match = re.fullmatch(r'\[\[([^\[\]#|]+)#([^\[\]#|]+)\]\]', link)
    if not match or match[1] not in fixture:
        return False
    headings = re.findall(r'^#{1,6}\s+(.+?)\s*$', fixture[match[1]], re.M)
    return match[2] in headings


check('new_template_heading_exists', resolves('[[' + fixture_path + '#E1]]'))
check('external_suffix_rejected', not resolves('[[' + fixture_path + ']]#E1'))
check('missing_evidence_rejected', not resolves('[[' + fixture_path + '#E9]]'))
check('wrong_direction_target_rejected', not resolves('[[directions/fixture-b/wiki/papers/Paper#E1]]'))
check('legacy_exact_heading_retained', resolves('[[directions/fixture-a/wiki/papers/Legacy#E1 - Original label]]'))
check('legacy_prefix_is_not_exact_heading', not resolves('[[directions/fixture-a/wiki/papers/Legacy#E1]]'))
check('all_six_examples_resolve_after_expansion', all(
    resolves(link.replace('D/', 'directions/fixture-a/')) for _, link in references))

# Check the example table has separate fields without treating a page state
# or a valid link as evidence of scientific support.
synthesis = read('agents/synthesis_agent.md')
check('separate_page_state_and_evidence_scope',
      'Source page review_status | Evidence verification scope' in synthesis
      and 'checked / partial / needs-review' not in synthesis)
for p in templates:
    match = re.search(r'^review_status:\s*(\S+)', p.read_text(encoding='utf-8-sig'), re.M)
    if match:
        check('template_stays_draft:' + p.name, match[1] == 'draft')

# Original scientific requirements remain verbatim; only definitions were added.
old_hard = (snapshot / 'files/memory/hard_memory.md').read_text(encoding='utf-8-sig')
new_hard = read('memory/hard_memory.md')
old_evidence = old_hard.split('## Evidence Rules\n', 1)[1].split('## Maintenance Rules', 1)[0]
check('original_evidence_paragraphs_preserved', all(
    paragraph in new_hard for paragraph in re.split(r'\n\s*\n', old_evidence.strip())))
check('all_agents_keep_root_and_evidence_entry', all(
    'AGENTS.md' in p.read_text(encoding='utf-8-sig')
    and 'memory/hard_memory.md' in p.read_text(encoding='utf-8-sig') for p in agents))

baseline_agent_chars = sum(len((snapshot / 'files' / p.relative_to(ROOT)).read_text(encoding='utf-8-sig')) for p in agents)
current_agent_chars = sum(len(p.read_text(encoding='utf-8-sig')) for p in agents)
print(json.dumps({
    'checks_passed': len(results), 'checks': results,
    'direction_files_compared': len(direction_files) - 1,
    'allowed_direction_change': profile,
    'agent_chars_before': baseline_agent_chars, 'agent_chars_after': current_agent_chars,
    'limits': ['Exact ATX heading fixture checks only; not a general link parser',
               'No Obsidian UI or independent agent session executed',
               'No scientific evidence or full-library links rechecked',
               'Text size change is not measured runtime or token savings']
}, indent=2))
