"""Read-only checks, with batch validation reports written only beside this script."""
from pathlib import Path
import hashlib,io,json,os,re,subprocess,sys
from urllib.parse import unquote
import openpyxl

HERE=Path(__file__).resolve().parent
D=HERE.parents[1]
ROOT=D.parents[1]
sys.path.insert(0,str(D/'scripts/review_bc'))
from workbook_io import BOOK,rows

def run(args):
    return subprocess.run(args,cwd=ROOT,capture_output=True,encoding='utf-8',
        env={**os.environ,'PYTHONIOENCODING':'utf-8'})
def save(name,data):
    (HERE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def gitbytes(path):
    result=subprocess.run(['git','show','HEAD:'+path],cwd=ROOT,capture_output=True)
    if result.returncode:raise RuntimeError('Cannot read published file '+path)
    return result.stdout

reports={}
for filename,args in [
 ('workbook-validation.json',[sys.executable,'-B',str(D/'scripts/review_bc/validate_workbook.py')]),
 ('contract-checks.json',[sys.executable,'-B',str(D/'scripts/review_bc/check_contract.py')]),
 ('structure-validation.json',[sys.executable,'-B','scripts/wiki_check.py','--direction',D.name])]:
    result=run(args)
    try:data=json.loads(result.stdout)
    except json.JSONDecodeError:raise RuntimeError(result.stderr or result.stdout)
    save(filename,data);reports[filename]={'exit_code':result.returncode}
    if result.returncode:print(json.dumps(data,ensure_ascii=False));raise SystemExit(result.returncode)

errors=[]
before=openpyxl.load_workbook(io.BytesIO(gitbytes(BOOK.relative_to(ROOT).as_posix())))
after=openpyxl.load_workbook(BOOK)
preserved={}
for sheet,key in [('Paper_Index','Paper_ID'),('Evidence_Records','Evidence_ID'),('Synthesis_Map','Synthesis_ID')]:
    old=rows(before[sheet]);new={r[key]:r for r in rows(after[sheet])}
    differences=[]
    for record in old:
        for field,value in record.items():
            if new.get(record[key],{}).get(field)!=value:differences.append([record[key],field])
    preserved[sheet]={'published_records':len(old),'differences':differences}
    if differences:errors.append('Published record changed: '+sheet)

legacy=run(['git','ls-files','--',D.relative_to(ROOT).as_posix()+'/wiki/papers/*.md'])
papers=legacy.stdout.splitlines()
changed=[]
for p in papers:
    previous=gitbytes(p).decode('utf-8').replace('\r\n','\n')
    if (ROOT/p).read_text(encoding='utf-8')!=previous:changed.append(p)
if changed:errors.append('Legacy paper changed')

manifest=json.loads((D/'raw/zotero_imports/literature-PI5UBPW7/manifest.json').read_text(encoding='utf-8'))
sources=json.loads((HERE/'sources.json').read_text(encoding='utf-8'))
index={r['Paper_ID']:r for r in rows(after['Paper_Index'])}
if [r['number'] for r in manifest['items']]!=list(range(1,16)):errors.append('Import numbering mismatch')
for row,source in zip(manifest['items'][-5:],sources):
    if row['doi']!=source['doi'] or index[row['Paper_ID']]['DOI']!=source['doi']:errors.append('Manifest identity mismatch')
if len({r['doi'].lower() for r in manifest['items']})!=15:errors.append('Duplicate DOI in import manifest')

status=run(['git','status','--porcelain=v1','--untracked-files=all'])
paths=[line[3:] for line in status.stdout.splitlines()]
if any(not p.startswith(D.relative_to(ROOT).as_posix()+'/') for p in paths):errors.append('Change outside direction')
diff=run(['git','diff','--check'])
if diff.returncode:errors.append('git diff --check failed')

# Root checker excludes rules and dated docs. Verify simple links in affected
# Markdown separately; this checks file existence, not renderer anchor slugs.
link_files=[ROOT/p for p in paths if p.endswith('.md') and (ROOT/p).is_file()]
link_files += [D/'raw/zotero_imports/literature-PI5UBPW7/import_plan.md']
missing=[];targets=0
planned={HERE/'delivery-validation.json'}
for p in link_files:
    text=p.read_text(encoding='utf-8')
    text=re.sub(r'```.*?```','',text,flags=re.S)
    for match in re.finditer(r'\[\[([^\]\n]+)\]\]',text):
        target=match.group(1).split('|',1)[0].split('#',1)[0]
        if not target:continue
        path=ROOT/target
        if not path.suffix:path=path.with_suffix('.md')
        targets+=1
        if not path.exists():missing.append({'file':p.relative_to(ROOT).as_posix(),'target':target})
    for match in re.finditer(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)',text):
        target=unquote(match.group(1).strip('<>')).split('#',1)[0]
        if not target or re.match(r'^[a-zA-Z]+:',target):continue
        path=(p.parent/target).resolve();targets+=1
        if not path.exists() and path not in planned:missing.append({'file':p.relative_to(ROOT).as_posix(),'target':target})
if missing:errors.append('Missing local link targets')

workspace=sorted(p.name for p in (D/'synthesis/review_BC').iterdir() if p.is_file())
expected=['BC_review_evidence.xlsx','BC_synthesis_notes.md','source_check_log.md']
if workspace!=expected:errors.append('Unexpected review workspace files')
if list((D/'synthesis/review_BC').glob('*.pending.xlsx')):errors.append('Pending workbook remains')
for name in ['_ingest.py','_synthesize.py','_upgrade.py','_handoff.py']:
    if (D/'raw/bc-batch2-2026-09-25'/name).exists():errors.append('One-time writer remains: '+name)

report={'direction_id':D.name,'checked':'2026-09-25','workbook_sha256':hashlib.sha256(BOOK.read_bytes()).hexdigest(),
 'published_base':run(['git','rev-parse','HEAD']).stdout.strip(),'reports':reports,
 'published_records_preserved':preserved,'legacy_paper_count':len(papers),'changed_legacy_papers':changed,
 'import_version':manifest['version'],'import_items':len(manifest['items']),
 'new_paper_ids':[s['Paper_ID'] for s in sources],
 'local_link_check':{'files':len(link_files),'targets':targets,'missing':missing,'anchor_slugs_checked':False},
 'review_workspace_files':workspace,'all_git_changes_within_direction':not any(not p.startswith(D.relative_to(ROOT).as_posix()+'/') for p in paths),
 'diff_check_exit_code':diff.returncode,'git_read_warnings':sorted(set(status.stderr.strip().splitlines())),
 'uploaded':False,'scientific_correctness_automatically_verified':False,
 'limitations':['Raw and external attachments are not Git backups.','Source hashes validate identity/integrity, not scientific truth.','Per-row unresolved evidence remains restricted.'],
 'errors':errors}
save('delivery-validation.json',report)
print(json.dumps({'reports':reports,'published_records_preserved':preserved,'legacy_papers':len(papers),'local_links_checked':targets,'errors':errors},ensure_ascii=False,indent=2))
sys.exit(bool(errors))
