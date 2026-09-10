"""Stage 1 only: inventory, path proposal, limited link baseline, verified ZIP.

Run from the repository root. Never moves or rewrites source research files.
Outputs are a snapshot; reruns use a fresh backup name and refresh JSON reports.
"""
from pathlib import Path
import collections
import datetime
import hashlib
import json
import os
import posixpath
import re
import subprocess
import zipfile
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
D = 'directions/ceramic-corrosion/'
EXCLUDED = {'.git', '.migration-backups'}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def write_json(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT).decode('utf-8').strip()

def classify(p):
    if p.startswith(('raw/', 'wiki/', 'synthesis/')):
        note = '按文件归属迁移；仅派生知识页/管理记录可修复链接，原件内容保持字节一致'
        if p.startswith('raw/zotero_imports/田志林/'):
            note += '；历史collection快照单独保留，不与田老师清单合并'
        if p.startswith('raw/notes/') and p.endswith('.md'):
            note += '；原始笔记不改写内部旧链接，使用路径映射溯源'
        return 'direction', 'move', D + p, [], note
    if p in {'log.md', 'inbox.md', 'index.md', 'memory/error_log.md', 'memory/decision_log.md'}:
        return 'mixed', 'split-history', D + p, [p], '完整历史/研究内容归方向；根文件重建公共入口或公共新增记录，按引用语境选目标'
    splits = {
        'memory/project_profile.md': (D+'memory/project_profile.md', ['memory/user_profile.md', D+'memory/reading_rules.md']),
        'memory/context_policy.md': ('memory/context_policy.md', [D+'memory/current_context.md', D+'docs/context-history-pre-migration.md']),
        'memory/tag_taxonomy.md': ('memory/tag_taxonomy.md', [D+'memory/tag_taxonomy.md']),
        'memory/term_aliases.md': ('memory/term_aliases.md', [D+'memory/term_aliases.md']),
        'agents/pdf_read_agent.md': ('agents/pdf_read_agent.md', [D+'memory/reading_rules.md']),
    }
    if p in splits:
        main, extra = splits[p]
        return 'mixed', 'split-sections', main, extra, '按section-routing.md逐段拆分，不对一对多映射做全局字符串替换'
    if p == 'memory/ceramic_corrosion_reading_rules.md':
        return 'direction', 'merge-sections', D+'memory/reading_rules.md', [], '完整保留组内外和作者规则，合并来自profile及阅读流程的CMAS检查'
    if p.startswith('docs/') and (p.startswith('docs/scopus-screening-') or Path(p).name in {
        'collection-candidates-2026-09-08.md', 'progress-and-background-2026-09-09.md',
        'rules-improvement-plan.md', 'system-audit-2026-09-05.md'}):
        return 'direction-history', 'move', D+p, [], '完整保存含研究内容的报告历史，更新实际导航，不把历史状态作为当前指令'
    if p.startswith(('.obsidian/', '.vscode/')):
        return 'global-local-config', 'retain-review', p, [], '设置保留根目录；涉及wiki/raw路径的过滤、workspace引用在阶段2定向修订'
    return 'global', 'retain-review', p, [], '保留根级职责；公共文档中研究输出路径在阶段2改成所选方向，LICENSE/工具文件无须改写'

tracked = set(subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode('utf-8').split('\0'))
paths = []
for current, dirs, names in os.walk(ROOT, followlinks=False):
    base = Path(current)
    dirs[:] = sorted(d for d in dirs if d not in EXCLUDED and base/d != OUT)
    for d in dirs:
        if (base/d).is_symlink() or (base/d).stat().st_file_attributes & 0x400:
            raise RuntimeError('Reparse directory requires manual review: '+str(base/d))
    for name in sorted(names):
        file = base/name
        if file.is_symlink():
            raise RuntimeError('Symlink requires manual review: '+str(file))
        paths.append(file.relative_to(ROOT).as_posix())
paths.sort()
ignored_process = subprocess.run(['git','check-ignore','--stdin','-z'], input=('\0'.join(paths)+'\0').encode('utf-8'), cwd=ROOT, stdout=subprocess.PIPE, check=False)
if ignored_process.returncode not in (0,1):
    raise RuntimeError('git check-ignore failed')
ignored = set(ignored_process.stdout.decode('utf-8').split('\0'))
content = {p:(ROOT/p).read_bytes() for p in paths}
rows = []
for p in paths:
    scope, action, target, extra, note = classify(p)
    rows.append(dict(source=p, scope=scope, action=action, target=target, additional_targets=extra,
                     note=note, bytes=len(content[p]), sha256=digest(content[p]),
                     tracked=p in tracked, ignored=p in ignored))
targets = collections.defaultdict(list)
for row in rows:
    targets[row['target'].casefold()].append(row['source'])
collisions = {k:v for k,v in targets.items() if len(v)>1}
occupied = [r['target'] for r in rows if r['target'] != r['source'] and (ROOT/r['target']).exists()]
if collisions or occupied:
    raise RuntimeError(f'Unexpected primary target collision: {collisions}, {occupied}')

reference_paths = paths + [p.relative_to(ROOT).as_posix() for p in OUT.rglob('*') if p.is_file()]
lookup = {p.casefold():p for p in reference_paths}
def resolve(source, target, kind):
    target = unquote(target.strip().strip('<>')).replace('\\','/')
    page, _, anchor = target.partition('#')
    if re.match(r'^[A-Za-z]:/', page) or page.startswith('//'):
        return 'external-local-unchecked', [], anchor
    if re.match(r'^[a-zA-Z][\w+.-]*:', page):
        return 'external-uri-unchecked', [], anchor
    if not page:
        return 'same-file', [source], anchor
    if kind == 'markdown':
        candidates = [posixpath.normpath(posixpath.join(posixpath.dirname(source),page))]
    else:
        candidates = [posixpath.normpath(page.lstrip('/')),posixpath.normpath(posixpath.join(posixpath.dirname(source),page))]
    found = set()
    for c in candidates:
        for v in (c,c+'.md'):
            if v.casefold() in lookup:
                found.add(lookup[v.casefold()])
    if not found and kind == 'wiki' and '/' not in page:
        found = {p for p in reference_paths if Path(p).name.casefold() == page.casefold() or Path(p).stem.casefold() == page.casefold()}
    if len(found) > 1:
        return 'ambiguous', sorted(found), anchor
    if found:
        return 'resolved-file', sorted(found), anchor
    for c in candidates:
        path = (ROOT/c).resolve()
        if path.is_relative_to(ROOT) and path.is_dir():
            return 'directory', [c], anchor
    return 'unresolved', [], anchor

links, path_mentions = [], []
for p in paths:
    if not p.endswith(('.md','.json','.yaml','.yml','.csv','.bat')):
        continue
    try:
        source = content[p].decode('utf-8-sig')
    except UnicodeDecodeError:
        continue
    fence = False
    for line_no, line in enumerate(source.splitlines(),1):
        if re.match(r'^\s*(`{3,}|~{3,})',line):
            fence = not fence
            continue
        for match in re.finditer(r'!?\[\[([^\]\n]+)\]\]',line):
            target = match.group(1).split('|',1)[0]
            status, found, anchor = resolve(p,target,'wiki')
            links.append(dict(source=p,line=line_no,kind='wiki',target=target,status=status,resolved=found,anchor=anchor,
                              context='fenced-example' if fence else 'template' if p.startswith('templates/') else 'inline-code' if line[:match.start()].count('`')%2 else 'body',
                              trailing_evidence=bool(re.match(r'#E\d+',line[match.end():]))))
        # Common inline links, including <paths with spaces>; nested destination parentheses unsupported.
        for match in re.finditer(r'(?<!!)\[(?!\[)([^\]\n]+)\]\((<[^>]+>|[^)\s]+)(?:\s+"[^"]*")?\)',line):
            target = match.group(2).strip('<>')
            status, found, anchor = resolve(p,target,'markdown')
            links.append(dict(source=p,line=line_no,kind='markdown',target=target,status=status,resolved=found,anchor=anchor,
                              context='fenced-example' if fence else 'template' if p.startswith('templates/') else 'body'))
        # Image inline links are collected separately.
        for match in re.finditer(r'!\[[^\]\n]*\]\((<[^>]+>|[^)\s]+)\)',line):
            target=match.group(1).strip('<>')
            status, found, anchor=resolve(p,target,'markdown')
            links.append(dict(source=p,line=line_no,kind='image',target=target,status=status,resolved=found,anchor=anchor,context='fenced-example' if fence else 'body'))
        if re.search(r'(?:raw/|wiki/|synthesis/|memory/|docs/|[A-Za-z]:[/\\])',line):
            path_mentions.append(dict(source=p,line=line_no,text=line))

timestamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
backup_dir = ROOT/'.migration-backups'
backup_dir.mkdir(exist_ok=True)
backup = backup_dir/f'pre-direction-migration-{timestamp}.zip'
with zipfile.ZipFile(backup,'x',zipfile.ZIP_DEFLATED) as z:
    for p in paths:
        z.writestr(p,content[p])
with zipfile.ZipFile(backup) as z:
    assert sorted(z.namelist()) == paths
    assert z.testzip() is None
    for row in rows:
        assert digest(z.read(row['source'])) == row['sha256']
        assert digest((ROOT/row['source']).read_bytes()) == row['sha256'], 'Source changed during snapshot'

stats = collections.Counter(r['status'] for r in links)
types = collections.Counter()
for p in paths:
    if p.startswith('wiki/') and p.endswith('.md'):
        types[p.split('/')[1]] += 1
summary = dict(created_utc=timestamp, head=git('rev-parse','HEAD'), git_status=git('status','--short'),
    snapshot_scope='All workspace files except .git, .migration-backups and this stage report directory; no external Zotero/MinerU files',
    files=len(rows), bytes=sum(r['bytes'] for r in rows), tracked=sum(r['tracked'] for r in rows), ignored=sum(r['ignored'] for r in rows),
    raw_files=sum(r['source'].startswith('raw/') for r in rows), raw_pdf_files=sum(r['source'].startswith('raw/') and r['source'].endswith('.pdf') for r in rows),
    wiki_markdown_counts=dict(types), link_counts=dict(stats), links=len(links), path_mentions=len(path_mentions),
    target_collisions=collisions, occupied_targets=occupied,
    backup=backup.relative_to(ROOT).as_posix(), backup_sha256=digest(backup.read_bytes()), backup_verified_files=len(rows),
    source_drift_during_snapshot=[],
    backup_note='ZIP readback hashes verified; same-disk local rollback copy, not disaster recovery; stage artifacts are excluded and kept alongside this report',
    limitations=['Links: common inline Markdown/wiki syntax only; fenced examples, templates, inline-code annotated',
                 'Heading/block anchors recorded but not validated; trailing #E recorded, not assumed clickable',
                 'No HTTP requests or external local file access; no scientific evidence re-review',
                 'Markdown reference-style links, HTML links, complex nested parentheses and Dataview not parsed; path-mentions.json retained for manual review'])
write_json('inventory.json',rows)
write_json('links-baseline.json',links)
write_json('path-mentions.json',path_mentions)
write_json('summary.json',summary)
write_json('raw-hashes.json',[r for r in rows if r['source'].startswith('raw/')])
print(json.dumps(summary,ensure_ascii=False,indent=2))
