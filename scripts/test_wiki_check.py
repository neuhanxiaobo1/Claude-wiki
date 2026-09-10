"""Synthetic fixtures only; does not edit the real vault."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.dont_write_bytecode = True
from wiki_check import Checker, REQUIRED


class WikiCheckTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for rel in ('AGENTS.md', 'index.md', 'memory/hard_memory.md', 'memory/user_profile.md'):
            self.write(rel, '# Public entry\n')
        self.entries = []
        for ident in ('alpha', 'beta'):
            base = 'directions/' + ident
            self.entries.append(dict(id=ident, name=ident, path=base, status='active', last_used=None))
            for rel in REQUIRED:
                self.write(base + '/' + rel, '# Entry\n')
        self.registry()

    def write(self, rel, content):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')

    def registry(self):
        self.write('memory/direction_registry.yaml', json.dumps(dict(schema_version=1, directions=self.entries)))

    def paper(self, name='Paper', body='', metadata=''):
        rel = 'directions/alpha/wiki/papers/' + name + '.md'
        self.write(rel, '---\ndirection_id: alpha\ntype: paper\ntitle: Fixture\nsource: local fixture\n'
                       'status: processed\nreview_status: draft\ntags: [paper]\n' + metadata + '---\n# Fixture\n' + body)
        return rel

    def run_check(self, mode='direction', direction='alpha'):
        return Checker(self.root, mode, direction).run()

    def codes(self, result):
        return {x['code'] for x in result['findings']}

    def test_valid_page(self):
        self.paper(body='### E1\nResult.\n[[#E1]]\n')
        self.assertEqual(self.run_check()['errors'], 0)

    def test_duplicate_yaml_key(self):
        self.paper(metadata='type: topic\n')
        self.assertIn('yaml_invalid', self.codes(self.run_check()))

    def test_bad_yaml(self):
        self.paper(metadata='broken: [\n')
        self.assertIn('yaml_invalid', self.codes(self.run_check()))

    def test_nonmapping_frontmatter(self):
        self.write('directions/alpha/wiki/papers/P.md', '---\n- not-a-map\n---\n')
        self.assertIn('yaml_invalid', self.codes(self.run_check()))

    def test_wrong_direction_and_type(self):
        self.write('directions/alpha/wiki/papers/P.md', '---\ndirection_id: beta\ntype: topic\n---\n')
        self.assertTrue({'direction_mismatch', 'page_type_mismatch'} <= self.codes(self.run_check()))

    def test_missing_metadata_not_upgraded(self):
        rel = self.paper()
        content = (self.root / rel).read_text().replace('review_status: draft\n', '').replace('source: local fixture\n', '')
        self.write(rel, content)
        self.assertTrue({'metadata_missing', 'paper_identity_pending'} <= self.codes(self.run_check()))
        self.assertEqual((self.root / rel).read_text(), content)

    def test_missing_heading_and_file(self):
        self.paper(body='[[#Absent]]\n[[directions/alpha/wiki/papers/Missing]]\n')
        self.assertTrue({'anchor_missing', 'link_missing'} <= self.codes(self.run_check()))

    def test_legacy_heading_alias_and_block(self):
        self.paper(body='### E1 - Original label\nEvidence. ^evidence-1\n'
                   '[[#E1 - Original label|E1]]\n[[#^evidence-1]]\n')
        self.assertEqual(self.run_check()['errors'], 0)

    def test_legacy_prefix_does_not_resolve(self):
        self.paper(body='### E1 - Original label\n[[#E1]]\n')
        self.assertIn('anchor_missing', self.codes(self.run_check()))

    def test_external_suffix_detected(self):
        self.paper(body='[[directions/alpha/wiki/papers/Paper]]#E1\n')
        self.assertIn('evidence_suffix_outside_link', self.codes(self.run_check()))

    def test_duplicate_heading(self):
        self.paper(body='### E1\nA\n### E1\nB\n[[#E1]]\n')
        self.assertIn('anchor_ambiguous', self.codes(self.run_check()))

    def test_short_link_ambiguity(self):
        self.paper(body='[[Shared]]\n')
        self.write('directions/alpha/wiki/topics/Shared.md', '# Topic\n')
        self.write('directions/alpha/wiki/methods/Shared.md', '# Method\n')
        self.assertIn('link_ambiguous', self.codes(self.run_check()))

    def test_code_and_template_exemptions(self):
        self.paper(body='`[[Missing]]`\n~~~md\n[[Missing]]\n~~~\n<!-- [[Missing]] -->\n')
        self.write('templates/paper.md', '---\ndirection_id: "{{direction_id}}"\n---\n[[D/wiki/papers/Paper#E1]]\n')
        self.assertEqual(self.run_check('all')['errors'], 0)

    def test_real_placeholder_is_error(self):
        self.paper(body='[[D/wiki/papers/Paper]]\n')
        self.assertIn('unexpanded_link', self.codes(self.run_check()))

    def test_public_does_not_read_research(self):
        self.paper(metadata='broken: [\n')
        self.assertNotIn('yaml_invalid', self.codes(self.run_check('public')))

    def test_cross_direction_anchor_not_read(self):
        self.paper(body='[[directions/beta/wiki/papers/P#E1]]\n')
        self.write('directions/beta/wiki/papers/P.md', '---\nbroken: [\n---\n')
        result = self.run_check()
        self.assertIn('anchor_not_checked', self.codes(result))
        self.assertNotIn('yaml_invalid', self.codes(result))

    def test_raw_never_parsed(self):
        self.paper(body='[[directions/alpha/raw/papers/Original#E1]]\n')
        self.write('directions/alpha/raw/papers/Original.md', '---\nbroken: [\n---\n')
        self.assertNotIn('yaml_invalid', self.codes(self.run_check('all')))

    def test_markdown_file_and_anchor_scope(self):
        self.paper(body='[same](Paper.md)\n[heading](Paper.md#fixture)\n[web](https://example.invalid/)\n')
        result = self.run_check()
        self.assertEqual(result['errors'], 0)
        self.assertIn('anchor_not_checked', self.codes(result))

    def test_registry_duplicates(self):
        self.entries.append(self.entries[0].copy())
        self.registry()
        self.assertIn('direction_duplicate', self.codes(self.run_check()))

    def test_registry_escape(self):
        self.entries[0]['path'] = '../outside'
        self.registry()
        self.assertIn('direction_path_invalid', self.codes(self.run_check()))

    def test_registry_wrong_schema(self):
        self.write('memory/direction_registry.yaml', 'schema_version: true\ndirections: []\n')
        self.assertIn('registry_schema', self.codes(self.run_check()))

    def test_wrong_page_state(self):
        rel = self.paper()
        self.write(rel, (self.root / rel).read_text().replace('review_status: draft', 'review_status: partial'))
        self.assertIn('review_status_invalid', self.codes(self.run_check()))

    def test_symlink_not_followed(self):
        link = self.root / 'directions/alpha/wiki/topics'
        link.parent.mkdir(parents=True, exist_ok=True)
        try:
            link.symlink_to(self.root / 'directions/beta', target_is_directory=True)
        except OSError:
            self.skipTest('Symlink creation unavailable on this OS/account.')
        self.assertIn('scan_path_skipped', self.codes(self.run_check()))

    def test_checker_writes_nothing(self):
        self.paper()
        hashes = lambda: {p.relative_to(self.root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in self.root.rglob('*') if p.is_file()}
        before = hashes()
        self.run_check('all')
        self.assertEqual(before, hashes())

    def test_cli_requires_scope(self):
        result = subprocess.run([sys.executable, '-B', str(Path(__file__).with_name('wiki_check.py')),
                                 '--root', str(self.root)], capture_output=True)
        self.assertEqual(result.returncode, 2)

    def test_dotted_note_name(self):
        self.paper(name='Version2.0', body='[[directions/alpha/wiki/papers/Version2.0]]\n')
        self.assertEqual(self.run_check()['errors'], 0)

    def test_root_and_direction_short_link(self):
        self.write('index.md', '# Root index\n')
        self.paper(body='[[index]]\n')
        self.assertIn('link_ambiguous', self.codes(self.run_check()))

    def test_hidden_root_file_not_read(self):
        self.write('.private.md', '---\nbroken: [\n---\n')
        self.assertNotIn('yaml_invalid', self.codes(self.run_check('public')))

    def test_external_path_never_opened(self):
        self.paper(body='[external](../../../../../../outside.md)\n')
        self.assertIn('link_path_not_checked', self.codes(self.run_check()))

    def test_reparse_guard_unit(self):
        path = self.root / 'directions/alpha'
        original = Path.lstat
        class Reparse:
            st_mode = 0
            st_file_attributes = 1024
        def fake_lstat(p):
            return Reparse() if p == path else original(p)
        with patch.object(Path, 'lstat', fake_lstat):
            self.assertFalse(Checker(self.root, 'public').guarded(path / 'index.md'))

    def test_missing_public_entry(self):
        (self.root / 'AGENTS.md').unlink()
        self.assertIn('public_file_missing', self.codes(self.run_check()))

    def test_partial_unregistered_direction(self):
        self.write('directions/partial/index.md', '# Partial\n')
        self.assertIn('unregistered_direction', self.codes(self.run_check('public')))

    def test_relative_markdown_before_root_fallback(self):
        self.write('scripts/run.py', '# Fixture\n')
        self.write('docs/structure-check.md', '[tool](../scripts/run.py)\n')
        result = self.run_check('public')
        self.assertEqual(result['errors'], 0)
        self.assertNotIn('link_path_not_checked', self.codes(result))

    def test_note_before_same_named_directory(self):
        (self.root / 'Note').mkdir()
        self.write('Note.md', '# Note\n')
        self.write('index.md', '[[Note]]\n')
        result = self.run_check('public')
        self.assertNotIn('link_ambiguous', self.codes(result))


if __name__ == '__main__':
    unittest.main()
