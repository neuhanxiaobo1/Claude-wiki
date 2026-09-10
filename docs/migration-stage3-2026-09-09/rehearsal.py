"""File-layout rehearsal only, not an agent execution sandbox or dialogue test.
All fake pages stay below ignored .migration-backups; real research is read-only.
"""
from pathlib import Path
import datetime, hashlib, json, re
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
real_files=[p for p in (ROOT/'directions').rglob('*') if p.is_file()]
before={p.relative_to(ROOT).as_posix():sha(p) for p in real_files}
registry=(ROOT/'memory/direction_registry.yaml').read_bytes()
fixture=ROOT/'.migration-backups'/('stage3-rehearsal-'+datetime.datetime.now().strftime('%Y%m%dT%H%M%S'))
fixture.mkdir(parents=True,exist_ok=False)
template=(ROOT/'templates/paper.md').read_text(encoding='utf-8')
spec=(ROOT/'templates/direction.md').read_text(encoding='utf-8')
assert 'current_context' in spec and 'reading_rules' in spec
results=[]
for ident in ['case-a','case-b']:
    d=fixture/'directions'/ident
    for rel in ['memory','raw/papers','raw/notes','raw/assets','raw/zotero_imports','wiki/papers','wiki/authors','wiki/topics','wiki/methods','wiki/datasets','wiki/metrics','wiki/claims','wiki/gaps','wiki/reviews','synthesis','docs']:
        (d/rel).mkdir(parents=True,exist_ok=True)
    contents={
      'AGENTS.md':f'# Fixture {ident}\nDirection: {ident}\n沿用通用规则，无领域扩展；仅本方向可写。\n',
      'memory/project_profile.md':f'# {ident}\n范围：虚构结构验收样例，不是真实课题。\n核心问题：待确认。\n',
      'memory/current_context.md':'尚未开展真实研究。\n',
      'memory/tag_taxonomy.md':'沿用公共标准，本方向领域词条暂无。\n',
      'memory/term_aliases.md':'沿用公共标准，本方向术语暂无。\n',
      'memory/error_log.md':'# Fixture error log\n', 'memory/decision_log.md':'# Fixture decision log\n',
      'index.md':f'# {ident} fixture index\n','log.md':'# Fixture log\n','inbox.md':'暂无。\n'}
    for rel,s in contents.items(): (d/rel).write_text(s,encoding='utf-8')
    paper=template.replace('{{direction_id}}',ident).replace('{{title}}','Shared fixture paper')
    paper=paper.replace('doi: 待确认','doi: null\nsource_identity: fixture-only-shared-source')
    (d/'wiki/papers/Shared.md').write_text(paper,encoding='utf-8')
    (d/'wiki/methods/Common Method.md').write_text(f'# Common Method\nFixture interpretation: {ident}\n',encoding='utf-8')
    combined='\n'.join(contents.values())+paper
    assert not re.search('CMAS|Tian|田老师|ceramic-corrosion',combined)
    assert f'direction_id: "{ident}"' in paper and '{{direction_id}}' not in paper
results.append({'case':'new-direction-neutral-skeleton','result':'passed','scope':'explicit fixture creation from template checklist; not a production generator'})
a=fixture/'directions/case-a'; b=fixture/'directions/case-b'
assert (a/'wiki/methods/Common Method.md').read_bytes() != (b/'wiki/methods/Common Method.md').read_bytes()
assert (a/'wiki/papers/Shared.md').exists() and (b/'wiki/papers/Shared.md').exists()
results.append({'case':'same-name-method-and-same-source-pages','result':'passed','scope':'distinct full paths; no automatic merge; common origin retained'})
before_a={p.relative_to(a).as_posix():sha(p) for p in a.rglob('*') if p.is_file()}
before_b={p.relative_to(b).as_posix():sha(p) for p in b.rglob('*') if p.is_file()}
source='directions/case-a/wiki/methods/Common Method'
borrow=f'# Borrowing fixture\nSource: [[{source}]]\nVersion: fixture-v1\nOriginal conditions: synthetic fixture only\nBorrowed part: outline only\nAssessment: AI推断，尚未验证\nNot independent evidence: same original source\n'
(b/'wiki/methods/Borrowed.md').write_text(borrow,encoding='utf-8')
(b/'log.md').write_text('# Fixture log\nBorrowed outline in case-b only.\n',encoding='utf-8')
assert (fixture/(source+'.md')).is_file()
assert all(sha(a/p)==h for p,h in before_a.items())
changed=[p for p,h in before_b.items() if sha(b/p)!=h]
assert changed==['log.md']
results.append({'case':'cross-direction-borrow-and-local-log','result':'passed','scope':'case-b adds its own assessment and log; every case-a byte unchanged'})
session_one={'direction':'case-a'}; session_two={'direction':'case-b'}
session_one['direction']='case-b'
assert session_two['direction']=='case-b'
session_two['direction']='case-a'
assert session_one['direction']=='case-b'
results.append({'case':'independent-session-data-model','result':'passed','scope':'desktop model only; actual assistant session binding is a rule, not code-enforced'})
assert before=={p.relative_to(ROOT).as_posix():sha(p) for p in real_files}
assert (ROOT/'memory/direction_registry.yaml').read_bytes()==registry
assert [p.name for p in (ROOT/'directions').iterdir() if p.is_dir()]==['ceramic-corrosion']
results.append({'case':'real-library-and-registry-unchanged','result':'passed','scope':f'{len(real_files)} real direction files verified; no fake registered direction'})
output={'fixture':fixture.relative_to(ROOT).as_posix(),'checks':results,'real_files_verified':len(real_files),
        'limitations':['Fixture operations performed explicitly by this script; this is not OS access control','No new independent agent conversation or Obsidian UI executed','No scientific claims or real paper ingestion tested','Temporary pages retain paper template placeholders because they are fixtures, not completed cards']}
(OUT/'rehearsal-results.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(output,ensure_ascii=False,indent=2))
