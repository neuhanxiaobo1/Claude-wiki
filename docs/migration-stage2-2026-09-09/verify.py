"""Structural migration audit for execution.json preview or --live workspace.
Does not judge scientific evidence or emulate Obsidian UI.
"""
from pathlib import Path
import collections, hashlib, json, re, sys, zipfile
from urllib.parse import unquote
import posixpath
import yaml

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
record=json.loads((OUT/'execution.json').read_text(encoding='utf-8'))
live='--live' in sys.argv
with zipfile.ZipFile(ROOT/record['backup']) as z: old={p:z.read(p) for p in z.namelist()}
with zipfile.ZipFile(ROOT/record['preview']) as z: planned={p:z.read(p) for p in z.namelist()}
files={p:b for p,b in old.items() if p not in record['retired']}
files.update(planned)
for p in (ROOT/'docs').rglob('*'):
    if p.is_file(): files[p.relative_to(ROOT).as_posix()]=p.read_bytes()
if live:
    update_file=OUT/'post-migration-updates.json'
    updates=json.loads(update_file.read_text(encoding='utf-8')) if update_file.exists() else {}
    locked={r['source'] for r in record.get('locked_legacy_copies',[])}
    assert all(not (ROOT/p).exists() or p in locked and (ROOT/p).read_bytes()==old[p] for p in record['retired'])
    assert all((ROOT/p).read_bytes()==b or p in updates and hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==updates[p]['sha256'] for p,b in planned.items()), 'Unrecorded output drift'
    assert all((ROOT/p).read_bytes()==b for p,b in old.items() if p not in record['retired'] and p not in planned), 'Unrelated source drift'
    files={p:(ROOT/p).read_bytes() for p in files if (ROOT/p).is_file()}
lookup={p.casefold():p for p in files}
mapping=record['mapping']
errors=[]; notes=[]; links=[]; counts=collections.Counter(); yaml_count=0
for p in record['protected_raw']:
    assert files[mapping[p]]==old[p],p
for p in record['scientific_pages']:
    s=files[mapping[p]].decode('utf-8-sig').replace('\r\n','\n')
    original=old[p].decode('utf-8-sig').replace('\r\n','\n')
    assert s.startswith('---\n')
    meta=yaml.safe_load(s.split('---\n',2)[1])
    assert meta['direction_id']=='ceramic-corrosion'
    if original.startswith('---\n'):
        previous=yaml.safe_load(original.split('---\n',2)[1])
        for key in ('status','review_status','type','assessment','confidence','novelty_status'):
            assert meta.get(key)==previous.get(key),(p,key)
    # Reverse only known path expansions; direction_id is the only metadata addition.
    restored=s.replace('direction_id: ceramic-corrosion\n','',1)
    if not original.startswith('---\n'): restored=restored.removeprefix('---\n---\n\n')
    reverse={v:k for k,v in mapping.items() if k!=v}
    for prefix in ('wiki/','raw/','synthesis/'): reverse['directions/ceramic-corrosion/'+prefix]=prefix
    # Headerless paths in wikilinks also need the stem mapping.
    reverse.update({v.removesuffix('.md'):k.removesuffix('.md') for k,v in mapping.items() if k!=v and k.endswith('.md')})
    pattern='|'.join(re.escape(k) for k in sorted(reverse,key=len,reverse=True))
    restored=re.sub(pattern,lambda m:reverse[m.group(0)],restored)
    if restored!=original: errors.append({'kind':'scientific-nonmechanical-diff','source':p})

def resolve(p,t,kind):
    t=unquote(t.strip().strip('<>')).replace('\\','/')
    base,_,anchor=t.partition('#')
    if re.match(r'^[A-Za-z][\w+.-]*:',base) or base.startswith('//'): return 'external',[],anchor
    if not base: return 'same-file',[p],anchor
    opts=[base] if kind=='wiki' else [posixpath.normpath(posixpath.join(posixpath.dirname(p),base))]
    found=set()
    for opt in opts:
        for candidate in (opt,opt+'.md'):
            if candidate.casefold() in lookup: found.add(lookup[candidate.casefold()])
    if not found and kind=='wiki' and '/' not in base:
        found={n for n in files if n.endswith('.md') and (Path(n).name.casefold()==base.casefold() or Path(n).stem.casefold()==base.casefold())}
    return ('resolved' if len(found)==1 else 'ambiguous' if found else 'unresolved'),sorted(found),anchor

for p,data in sorted(files.items()):
    if not p.endswith('.md') or p.startswith(('docs/migration-stage1-','docs/migration-stage2-')): continue
    s=data.decode('utf-8-sig').replace('\r\n','\n')
    if s.startswith('---\n'):
        try: yaml.safe_load(s.split('---\n',2)[1]); yaml_count+=1
        except Exception as e: errors.append({'kind':'yaml','source':p,'error':str(e)})
    if p.startswith('directions/ceramic-corrosion/wiki/'): counts[p.split('/')[3]]+=1
    fence=False
    for no,line in enumerate(s.splitlines(),1):
        if re.match(r'^\s*(`{3,}|~{3,})',line): fence=not fence; continue
        if fence or p.startswith('templates/'): continue
        matches=[('wiki',m.group(1).split('|',1)[0]) for m in re.finditer(r'\[\[([^\]\n]+)\]\]',line)]
        matches += [('markdown',m.group(1)) for m in re.finditer(r'(?<!!)\[(?!\[)[^\]\n]+\]\((<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\)',line)]
        for kind,target in matches:
            status,found,anchor=resolve(p,target,kind)
            item={'source':p,'line':no,'target':target,'status':status,'resolved':found,'anchor':anchor}
            links.append(item)
            if status in ('unresolved','ambiguous'):
                if p.startswith('agents/') and ('/Paper' in target or '/Claim' in target): item['exception']='task-template-example';notes.append(item)
                elif p.startswith('directions/ceramic-corrosion/raw/'):
                    item['exception']='protected-original-link-use-mapping';notes.append(item)
                else: errors.append(item)

before=old['memory/hard_memory.md'].decode('utf-8-sig').replace('\r\n','\n')
after=files['memory/hard_memory.md'].decode('utf-8-sig').replace('\r\n','\n')
assert before.split('## Evidence Rules',1)[1].split('## Maintenance Rules',1)[0]==after.split('## Evidence Rules',1)[1].split('## Maintenance Rules',1)[0]
assert not re.search(r'CMAS|Tian|田老师|陶瓷', files['agents/pdf_read_agent.md'].decode('utf-8'))
registry=yaml.safe_load(files['memory/direction_registry.yaml'])
assert registry['directions'][0]['id']=='ceramic-corrosion' and len(registry['directions'])==1
for p,data in files.items():
    if p.endswith('.json') and not p.startswith('docs/migration-stage'): json.loads(data)
result={'mode':'live' if live else 'preview','errors':errors,'exceptions':notes,'parsed_markdown_frontmatter':yaml_count,
    'protected_raw_verified':len(record['protected_raw']),'scientific_pages_verified':len(record['scientific_pages']),
    'wiki_markdown_counts':dict(counts),'evidence_rules_unchanged':True,'cmasspecial_removed_from_common_reader':True,
    'links_checked':len(links),'link_status_counts':dict(collections.Counter(l['status'] for l in links)),
    'limitations':['Common inline Markdown/wiki syntax only; fenced/template examples excluded','Heading/block anchors recorded, not all validated; outside-]] E# not treated as clickable','External files and web URLs not accessed; Obsidian UI not run','Stage1/2 historical reports and their embedded source paths excluded from active link audit']}
(OUT/('verification-live.json' if live else 'verification-preview.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
sys.exit(bool(errors))
