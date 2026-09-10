"""Read-only, explicitly scoped ResearchWiki structural checks. JSON to stdout.

No network, auto-fix, content generation, Git mutation or report file writing.
See docs/structure-check.md for syntax coverage and exit codes.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
import os
from pathlib import Path
import re
import stat
import sys
from urllib.parse import unquote

sys.dont_write_bytecode = True
try:
    import yaml
except ImportError:
    yaml = None

ID = re.compile(r'^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$')
TYPE = dict(papers='paper', authors='author', topics='topic', methods='method',
            datasets='dataset', metrics='metric', claims='claim', gaps='gap', reviews='review')
REQUIRED = ('AGENTS.md', 'index.md', 'log.md', 'inbox.md', 'memory/project_profile.md',
            'memory/current_context.md', 'memory/tag_taxonomy.md', 'memory/term_aliases.md',
            'memory/error_log.md', 'memory/decision_log.md')
LIMITS = [
    'Structure only: no scientific evidence, source availability, tag semantics or DOI deduplication review.',
    'No raw, external files, hidden directories, symlinks/junctions or historical report/log contents scanned.',
    'Wikilinks: scoped file targets, aliases, exact ATX headings and block ID existence; not desktop rendering.',
    'Markdown: simple inline local file targets only; anchors and complex/reference-style syntax not validated.',
    'Fenced code, inline code and HTML comments excluded; explicit template placeholders are not real pages.',
    'No write protection for other programs, backup creation, restore or concurrent-write locking is provided.',
]


if yaml:
    class UniqueLoader(yaml.SafeLoader):
        pass

    def unique_mapping(loader, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if key in result:
                raise yaml.constructor.ConstructorError(None, None, 'duplicate key: ' + str(key), key_node.start_mark)
            result[key] = loader.construct_object(value_node, deep=deep)
        return result

    UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def visible(text):
    """Mask excluded syntax while preserving line numbers. Not a Markdown renderer."""
    text = re.sub(r'<!--[\s\S]*?-->', lambda m: re.sub(r'[^\n]', ' ', m[0]), text)
    out, fence = [], None
    for line in text.splitlines(keepends=True):
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence):
                fence = None
            out.append(re.sub(r'[^\n]', ' ', line))
        elif marker:
            fence = marker[1]
            out.append(re.sub(r'[^\n]', ' ', line))
        else:
            out.append(re.sub(r'(`+)([^`]*?)\1', lambda m: ' ' * len(m[0]), line))
    return ''.join(out)


class Checker:
    def __init__(self, root, mode, direction=None):
        self.root = Path(root).resolve()
        self.mode, self.direction = mode, direction
        self.findings, self.cache, self.selected, self.registry = [], {}, set(), {}
        self.link_count = 0

    def add(self, level, code, path, message, line=None):
        item = dict(level=level, code=code, path=str(path), message=message)
        if line is not None:
            item['line'] = line
        self.findings.append(item)

    def guarded(self, path):
        """Reject escapes and reparse points before reading any contents."""
        path = Path(os.path.abspath(path))
        try:
            parts = path.relative_to(self.root).parts
        except ValueError:
            return False
        cursor = self.root
        for part in parts:
            cursor /= part
            try:
                info = cursor.lstat()
            except FileNotFoundError:
                continue
            if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & 1024:
                return False
        return True

    def read(self, rel):
        if rel in self.cache:
            return self.cache[rel]
        path = self.root / rel
        if not self.guarded(path):
            self.add('error', 'unsafe_path', rel, 'Path escapes root or uses a symlink/junction.')
            return None
        try:
            data = path.read_text(encoding='utf-8-sig')
        except (OSError, UnicodeError) as exc:
            self.add('error', 'read_failed', rel, type(exc).__name__)
            return None
        self.cache[rel] = data
        return data

    def parse(self, value, rel):
        try:
            data = yaml.load(value, Loader=UniqueLoader)
            if not isinstance(data, dict):
                raise ValueError('Expected a YAML mapping.')
            return data
        except (yaml.YAMLError, ValueError, TypeError, RecursionError) as exc:
            mark = getattr(exc, 'problem_mark', None)
            self.add('error', 'yaml_invalid', rel, str(exc).splitlines()[0], mark.line + 1 if mark else None)
            return None

    def load_registry(self):
        for required in ('AGENTS.md', 'index.md', 'memory/hard_memory.md', 'memory/user_profile.md'):
            candidate = self.root / required
            if not self.guarded(candidate) or not candidate.is_file():
                self.add('error', 'public_file_missing', required, 'Missing or unsafe public entry file.')
        rel = 'memory/direction_registry.yaml'
        text = self.read(rel)
        data = self.parse(text, rel) if text is not None else None
        if data is None:
            return
        if type(data.get('schema_version')) is not int or data['schema_version'] != 1 or not isinstance(data.get('directions'), list):
            self.add('error', 'registry_schema', rel, 'Expected schema_version 1 and directions list.')
            return
        names = set()
        for entry in data['directions']:
            if not isinstance(entry, dict):
                self.add('error', 'registry_entry', rel, 'Each direction must be a mapping.')
                continue
            ident, name, path = entry.get('id'), entry.get('name'), entry.get('path')
            if not isinstance(ident, str) or not ID.fullmatch(ident):
                self.add('error', 'direction_id_invalid', rel, 'Invalid stable direction ID.')
                continue
            if ident in self.registry:
                self.add('error', 'direction_duplicate', rel, ident)
                continue
            if not isinstance(name, str) or not name.strip() or name in names:
                self.add('error', 'direction_name_invalid', rel, ident + ': missing or duplicate name.')
            names.add(name if isinstance(name, str) else '')
            if path != 'directions/' + ident or not self.guarded(self.root / path):
                self.add('error', 'direction_path_invalid', rel, ident + ': path must equal directions/<id>, without reparse points.')
                continue
            self.registry[ident] = path
            for required in REQUIRED:
                candidate = self.root / path / required
                if not self.guarded(candidate) or not candidate.is_file():
                    self.add('error', 'direction_file_missing', path + '/' + required, 'Missing or unsafe direction entry file.')
        parent = self.root / 'directions'
        if self.guarded(parent) and parent.is_dir():
            for child in sorted(parent.iterdir()):
                if not child.name.startswith('.') and child.is_dir() and child.name not in self.registry:
                    self.add('warning', 'unregistered_direction', 'directions/' + child.name,
                             'Directory not registered; inspect partial creation before resuming.')

    def walk(self, rel):
        base = self.root / rel
        if not self.guarded(base):
            self.add('error', 'unsafe_path', rel, 'Unsafe scan directory.')
            return
        for parent, dirs, files in os.walk(base, followlinks=False):
            keep = []
            for name in sorted(dirs):
                path = Path(parent) / name
                if name.startswith('.'):
                    continue
                if not self.guarded(path):
                    self.add('warning', 'scan_path_skipped', path.relative_to(self.root).as_posix(), 'Symlink/junction skipped.')
                else:
                    keep.append(name)
            dirs[:] = keep
            for name in sorted(files):
                if name.endswith('.md') and not name.startswith('.'):
                    yield (Path(parent) / name).relative_to(self.root).as_posix()

    def select(self):
        if self.mode in ('public', 'all'):
            self.selected.update(p.name for p in self.root.glob('*.md') if p.name != 'log.md' and not p.name.startswith('.'))
            for folder in ('agents', 'templates', 'shared'):
                self.selected.update(self.walk(folder))
            self.selected.update('memory/' + p.name for p in (self.root / 'memory').glob('*.md')
                                 if p.name not in ('error_log.md', 'decision_log.md'))
            # User guides only: dated architecture reports and plans are historical inputs.
            self.selected.update('docs/' + name for name in ('direction-workflow.md', 'structure-check.md',
                'recovery-and-backup.md', 'privacy-and-gitignore.md', 'zotero-workflow.md', 'obsidian-setup.md', 'initialization.md')
                if (self.root / 'docs' / name).exists())
        chosen = list(self.registry) if self.mode == 'all' else [self.direction] if self.mode == 'direction' else []
        for ident in chosen:
            if ident not in self.registry:
                self.add('error', 'direction_unknown', 'memory/direction_registry.yaml', str(ident))
                continue
            base = self.registry[ident]
            self.selected.update(base + '/' + name for name in ('AGENTS.md', 'index.md', 'inbox.md'))
            self.selected.update(base + '/memory/' + p.name for p in (self.root / base / 'memory').glob('*.md')
                                 if p.name not in ('error_log.md', 'decision_log.md'))
            for folder in ('wiki', 'synthesis'):
                self.selected.update(self.walk(base + '/' + folder))

    def metadata(self, rel, text):
        parts = rel.split('/')
        knowledge = len(parts) > 3 and parts[0] == 'directions' and parts[2] in ('wiki', 'synthesis')
        match = re.match(r'\A---\s*\n([\s\S]*?)\n---(?:\n|$)', text)
        if not match:
            if text.startswith('---\n') or text.startswith('---\r\n'):
                self.add('error', 'frontmatter_unclosed', rel, 'Missing closing delimiter.')
            elif knowledge:
                self.add('warning', 'frontmatter_missing', rel, 'Legacy page: inspect before migration.')
            return
        data = self.parse(match[1], rel)
        if data is None or rel.startswith('templates/'):
            return
        state = data.get('review_status')
        if state is not None and state not in ('draft', 'checked', 'needs-review'):
            self.add('error', 'review_status_invalid', rel, 'Page review_status must be draft/checked/needs-review.')
        if 'tags' in data and (not isinstance(data['tags'], list) or any(not isinstance(x, str) for x in data['tags'])):
            self.add('warning', 'tags_type', rel, 'Expected a list of tag strings.')
        if not knowledge:
            return
        if data.get('direction_id') != parts[1]:
            self.add('error', 'direction_mismatch', rel, 'direction_id does not match directory.')
        expected = TYPE.get(parts[3]) if parts[2] == 'wiki' else None
        if expected and data.get('type') != expected:
            self.add('error', 'page_type_mismatch', rel, 'Expected type: ' + expected)
        if expected:
            for key in ('status', 'tags', 'review_status'):
                if key not in data:
                    self.add('warning', 'metadata_missing', rel, key + ' missing; do not infer checked.')
        if expected == 'paper':
            for key in ('title', 'source'):
                value = data.get(key)
                if not isinstance(value, str) or not value.strip() or value in ('待确认', '待核查'):
                    self.add('warning', 'paper_identity_pending', rel, key + ' missing or unresolved.')

    def anchor(self, source, dest, anchor, line, markdown=False):
        if dest not in self.selected or Path(dest).suffix.lower() != '.md':
            self.add('warning', 'anchor_not_checked', source, dest + ': outside content scope.', line)
            return
        if markdown or '#' in anchor:
            self.add('warning', 'anchor_not_checked', source, 'Markdown/nested heading anchor requires manual check: ' + anchor, line)
            return
        content = self.read(dest)
        if content is None:
            return
        content = visible(content)
        if anchor.startswith('^'):
            hits = len(re.findall(r'\^' + re.escape(anchor[1:]) + r'\s*$', content, re.M)) if re.fullmatch(r'\^[A-Za-z0-9-]+', anchor) else 0
        else:
            hits = sum(h.rstrip().rstrip('#').rstrip() == anchor for h in re.findall(r'^ {0,3}#{1,6}\s+(.+)$', content, re.M))
        if hits == 0:
            self.add('error', 'anchor_missing', source, dest + '#' + anchor, line)
        elif hits > 1:
            self.add('warning', 'anchor_ambiguous', source, dest + '#' + anchor, line)

    def link(self, rel, target, line, markdown=False):
        target = unquote(target.replace('\\|', '|').split('|', 1)[0].strip().strip('<>'))
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('//'):
            return  # No network or absolute external source access.
        self.link_count += 1
        knowledge = re.match(r'^directions/[^/]+/(wiki|synthesis)/', rel)
        if '{{' in target or '<' in target or target.startswith('D/'):
            if knowledge:
                self.add('error', 'unexpanded_link', rel, target, line)
            return
        name, sep, anchor = target.partition('#')
        candidates = []
        if not name:
            candidates = [self.root / rel]
        elif not markdown and '/' not in name:
            candidates = [self.root / p for p in self.selected if Path(p).name in (name, name + '.md')]
            candidates.append(self.root / name)
        else:
            candidates = [self.root / name]
            if markdown:
                candidates.insert(0, (self.root / rel).parent / name)
        existing = []
        for candidate in candidates:
            candidate = Path(os.path.abspath(candidate))
            if not self.guarded(candidate):
                self.add('warning', 'link_path_not_checked', rel, 'Outside root or symlink/junction: ' + name, line)
                return
            note = candidate.with_name(candidate.name + '.md')
            options = [candidate] if candidate.suffix.lower() == '.md' else [candidate, note] if candidate.suffix else [note, candidate]
            for path in options:
                if not self.guarded(path):
                    self.add('warning', 'link_path_not_checked', rel, 'Symlink/junction target: ' + name, line)
                    return
                if path.exists():
                    if path not in existing:
                        existing.append(path)
                    break
            if markdown and existing:
                break  # Relative Markdown destination takes precedence over vault-root fallback.
        if len(existing) > 1:
            self.add('warning', 'link_ambiguous', rel, target, line)
        elif not existing:
            self.add('error', 'link_missing', rel, target, line)
        elif sep:
            if existing[0].is_dir():
                self.add('warning', 'anchor_not_checked', rel, 'Directory anchor: ' + target, line)
            else:
                self.anchor(rel, existing[0].relative_to(self.root).as_posix(), anchor, line, markdown)

    def links(self, rel, content):
        body = visible(content)
        for match in re.finditer(r'\[\[([^\]\n]+)\]\](#E\d+)?', body):
            line = body.count('\n', 0, match.start()) + 1
            if match[2]:
                self.add('warning', 'evidence_suffix_outside_link', rel, match[0], line)
            self.link(rel, match[1], line)
        # Deliberately limited to simple inline destinations, including angle-wrapped spaces.
        for match in re.finditer(r'(?<!!)\[[^\[\]\n]*\]\((<[^>\n]+>|[^()\s]+)\)', body):
            self.link(rel, match[1], body.count('\n', 0, match.start()) + 1, markdown=True)

    def run(self):
        if yaml is None:
            raise RuntimeError('PyYAML is required; see scripts/requirements.txt. Nothing was installed.')
        self.load_registry()
        self.select()
        for rel in sorted(self.selected):
            content = self.read(rel)
            if content is not None:
                self.metadata(rel, content)
                self.links(rel, content)
        counts = Counter(x['level'] for x in self.findings)
        return dict(mode=self.mode, direction=self.direction, selected_files=len(self.selected),
                    read_files=len(self.cache), links_seen=self.link_count,
                    errors=counts['error'], warnings=counts['warning'], findings=self.findings,
                    limitations=LIMITS, scientific_evidence_checked=False)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument('--public', action='store_true')
    scope.add_argument('--direction')
    scope.add_argument('--all-directions', action='store_true')
    args = parser.parse_args(argv)
    mode = 'public' if args.public else 'direction' if args.direction is not None else 'all'
    try:
        result = Checker(args.root, mode, args.direction).run()
    except (RuntimeError, OSError) as exc:
        print(json.dumps({'execution_error': str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result['errors'] else 0


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    raise SystemExit(main())
