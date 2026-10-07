"""Read-only stage checks; writes validation snapshots only beside this file."""
from pathlib import Path
import hashlib,io,json,os,re,subprocess,sys
from urllib.parse import unquote
import openpyxl

HERE=Path(__file__).resolve().parent;D=HERE.parents[1];ROOT=D.parents[1]
sys.path.insert(0,str(D/'scripts/review_bc'))
from workbook_io import BOOK,rows
def run(args):
 return subprocess.run(args,cwd=ROOT,capture_output=True,encoding='utf-8',env={**os.environ,'PYTHONIOENCODING':'utf-8'})
def save(name,data):
 (HERE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def gitbytes(path):
 r=subprocess.run(['git','show','HEAD:'+path],cwd=ROOT,capture_output=True)
 if r.returncode:raise RuntimeError('Cannot read published '+path)
 return r.stdout

reports={};errors=[]
for name,args in [
 ('workbook-validation.json',[sys.executable,'-B',str(D/'scripts/review_bc/validate_workbook.py')]),
 ('contract-checks.json',[sys.executable,'-B',str(D/'scripts/review_bc/check_contract.py')]),
 ('structure-validation.json',[sys.executable,'-B','scripts/wiki_check.py','--direction',D.name])]:
 r=run(args)
 try:data=json.loads(r.stdout)
 except json.JSONDecodeError:raise RuntimeError(r.stderr or r.stdout)
 save(name,data);reports[name]={'exit_code':r.returncode}
 if r.returncode:errors.append(name+' failed')

base=(D/'raw/bc-stage7-2026-09-30/before.xlsx').read_bytes()
before=openpyxl.load_workbook(io.BytesIO(base));after=openpyxl.load_workbook(BOOK)
change=json.loads((HERE/'workbook-change.json').read_text(encoding='utf-8'))
if hashlib.sha256(base).hexdigest()!=change['before_sha256']:errors.append('Stage baseline differs from change manifest')
if hashlib.sha256(BOOK.read_bytes()).hexdigest()!=change['after_sha256']:errors.append('Workbook differs from change manifest')
if hashlib.sha256((D/'raw/bc-stage7-2026-09-30/before.xlsx').read_bytes()).hexdigest()!=change['before_sha256']:errors.append('Local baseline differs')
diffs={};counts={}
allowed_followup=set();allowed_synth=set(change['updated_syntheses'])
for sheet,key in [('Paper_Index','Paper_ID'),('Evidence_Records','Evidence_ID'),('Synthesis_Map','Synthesis_ID')]:
 old=rows(before[sheet]);new={r[key]:r for r in rows(after[sheet])};counts[sheet]=len(new);differences=[]
 for record in old:
  for field,value in record.items():
   if new.get(record[key],{}).get(field)!=value:
    allowed=(sheet=='Evidence_Records' and record[key] in allowed_followup and field in ['Verification_Scope','Check_Reason']) or (sheet=='Synthesis_Map' and record[key] in allowed_synth)
    differences.append({'id':record[key],'field':field,'allowed':allowed})
    if not allowed:errors.append('Unexpected old cell change: '+str(differences[-1]))
 diffs[sheet]={'old_records':len(old),'differences':differences}
if counts!={'Paper_Index':21,'Evidence_Records':113,'Synthesis_Map':9}:errors.append('Counts mismatch')

sources=json.loads((HERE/'sources.json').read_text(encoding='utf-8'))
prior_sources=json.loads((HERE.parent/'bc-stage3-2026-09-26/sources.json').read_text(encoding='utf-8'))
prior_sources+=json.loads((HERE.parent/'bc-stage4-2026-09-28/sources.json').read_text(encoding='utf-8'))
expected_legacy={s['legacy_page']+'.md' for s in prior_sources}
prior_change=json.loads((HERE.parent/'bc-stage6-2026-09-29/workbook-change.json').read_text(encoding='utf-8'))
if change['before_sha256']!=prior_change['after_sha256']:errors.append('Stage continuity mismatch')
screened=sources
screen_checks=[]
for s in screened:
 for kind in [k for k in ['pdf','md','manifest','identity'] if k+'_sha256' in s]:
  path=Path(s[kind]);same=path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest()==s[kind+'_sha256']
  screen_checks.append({'screen_id':s['Paper_ID'],'kind':kind,'unchanged':same})
  if not same:errors.append('Screened source changed: '+s['Paper_ID']+'/'+kind)
papers=run(['git','ls-files','--',D.relative_to(ROOT).as_posix()+'/wiki/papers/*.md']).stdout.splitlines()
changed=[];anchor_before=0;anchor_after=0
for p in papers:
 old=gitbytes(p).decode('utf-8').replace('\r\n','\n');new=(ROOT/p).read_text(encoding='utf-8')
 if old!=new:changed.append(p)
 a=re.findall(r'^### E\d+.*$',old,re.M);b=re.findall(r'^### E\d+.*$',new,re.M)
 anchor_before+=len(a);anchor_after+=len(b)
 if a!=b:errors.append('Changed E anchors: '+p)
if set(changed)!=expected_legacy:errors.append('Unexpected legacy page modification set')
if len(papers)!=27 or anchor_before!=108 or anchor_after!=108:errors.append('Legacy counts mismatch')

manifest=json.loads((D/'raw/zotero_imports/literature-PI5UBPW7/manifest.json').read_text(encoding='utf-8'))
if [r['number'] for r in manifest['items']]!=list(range(1,19)):errors.append('Import numbering mismatch')
if len({r['doi'].lower() for r in manifest['items']})!=18:errors.append('Import duplicate DOI')
index={r['Paper_ID']:r for r in rows(after['Paper_Index'])}
for s in sources:
 folder='literature-PI5UBPW7'
 selected_manifest=json.loads((D/'raw/zotero_imports'/folder/'manifest.json').read_text(encoding='utf-8'))
 m=next(x for x in selected_manifest['items'] if x.get('zotero_item_key',x.get('item_key'))==s['item_key'])
 if (m['Paper_ID'],m['doi'],m['zotero_item_key'])!=(s['Paper_ID'],s['doi'],s['item_key']):errors.append('Manifest mapping mismatch')
 if index[s['Paper_ID']]['DOI']!=s['doi']:errors.append('Workbook DOI mismatch')

status=run(['git','status','--porcelain=v1','--untracked-files=all']);paths=[line[3:] for line in status.stdout.splitlines()]
isolated=all(p.startswith(D.relative_to(ROOT).as_posix()+'/') for p in paths)
if not isolated:errors.append('Change outside direction')
diff=run(['git','diff','--check'])
if diff.returncode:errors.append('Diff whitespace failure')
link_files=[ROOT/p for p in paths if p.endswith('.md') and (ROOT/p).is_file()]
link_files.extend(D/'raw/zotero_imports'/folder/'import_plan.md' for folder in ['literature-PI5UBPW7','wave-transparent-composites-BSQRX4DM'])
missing=[];targets=0;planned={HERE/'delivery-validation.json'}
for p in link_files:
 t=re.sub(r'```.*?```','',p.read_text(encoding='utf-8'),flags=re.S)
 for match in re.finditer(r'\[\[([^\]\n]+)\]\]',t):
  target=match.group(1).split('|',1)[0].split('#',1)[0]
  if not target:continue
  path=ROOT/target
  if not path.suffix:path=path.with_suffix('.md')
  targets+=1
  if not path.exists():missing.append({'file':str(p.relative_to(ROOT)),'target':target})
 for match in re.finditer(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)',t):
  target=unquote(match.group(1).strip('<>')).split('#',1)[0]
  if not target or re.match(r'^[a-zA-Z]+:',target):continue
  path=(p.parent/target).resolve();targets+=1
  if not path.exists() and path not in planned:missing.append({'file':str(p.relative_to(ROOT)),'target':target})
if missing:errors.append('Missing local links')
workspace=sorted(p.name for p in (D/'synthesis/review_BC').iterdir() if p.is_file())
if workspace!=['BC_review_evidence.xlsx','BC_synthesis_notes.md','source_check_log.md']:errors.append('Unexpected workspace files')
for p in (D/'raw/bc-stage7-2026-09-30').glob('_*.py'):errors.append('One-time writer remains: '+p.name)

result={'direction_id':D.name,'checked':'2026-09-30','published_base':run(['git','rev-parse','HEAD']).stdout.strip(),
 'workbook_sha256':hashlib.sha256(BOOK.read_bytes()).hexdigest(),'reports':reports,'counts':counts,
 'previous_stage_record_changes':diffs,'screened_source_checks':screen_checks,'legacy_paper_count':len(papers),'legacy_evidence_anchors_before_after':[anchor_before,anchor_after],
 'changed_legacy_papers':changed,'import_version':manifest['version'],'import_items':len(manifest['items']),
 'source_ids':[s['Paper_ID'] for s in sources],'local_link_check':{'files':len(link_files),'targets':targets,'missing':missing,'anchor_slugs_checked':False},
 'review_workspace_files':workspace,'all_git_changes_within_direction':isolated,'diff_check_exit_code':diff.returncode,
 'git_read_warnings':sorted(set(status.stderr.strip().splitlines())),'uploaded':False,
 'scientific_correctness_automatically_verified':False,'errors':errors}
save('delivery-validation.json',result)
print(json.dumps({'reports':reports,'counts':counts,'legacy_E_anchors':[anchor_before,anchor_after],'link_targets':targets,'errors':errors},ensure_ascii=False,indent=2))
sys.exit(bool(errors))
