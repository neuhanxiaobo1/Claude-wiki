"""Read-only validation of the direction's authoritative B/C workbook and pilot sources."""
from pathlib import Path
from collections import Counter
import json,re,hashlib,subprocess,sys
import openpyxl
from workbook_io import BOOK,HERE,rows,validate,digest,splitids

def run():
    wb=openpyxl.load_workbook(BOOK);errors,data=validate(wb)
    D=HERE.parents[1];root=D.parents[1]
    sources=json.loads((D/'docs/bc-pilot-2026-09-25/sources.json').read_text(encoding='utf-8'))
    source_checks=[]
    for s in sources:
        for kind in ['pdf','md']:
            p=Path(s[kind]);same=p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==s[kind+'_sha256']
            source_checks.append({'paper':s['Paper_ID'],'kind':kind,'unchanged':same})
            if not same:errors.append(s['Paper_ID']+': source missing/changed '+kind)
    pp=data['Paper_Index'];ee=data['Evidence_Records'];ss=data['Synthesis_Map']
    doi=[str(p['DOI']).strip().lower().removeprefix('https://doi.org/') for p in pp if p.get('DOI')]
    if len(doi)!=len(set(doi)):errors.append('duplicate DOI')
    for p in pp:
        if not p.get('B_Use') or not p.get('C_Use') or not p.get('Verification_Scope'):errors.append(p['Paper_ID']+': missing role/scope')
    for e in ee:
        for ref in splitids(e.get('Legacy_Evidence_Ref')):
            page,anchor=ref.split('#',1);path=root/(page+'.md')
            if not path.is_file() or not re.search(r'^### '+re.escape(anchor)+r'\s*$',path.read_text(encoding='utf-8'),re.M):errors.append(e['Evidence_ID']+': invalid legacy ref '+ref)
    b={p['Paper_ID'] for p in pp if p['B_Use']=='Core'};c={p['Paper_ID'] for p in pp if p['C_Use']=='Core'}
    pages=list((D/'wiki/papers').glob('*.md'))
    legacy_count=sum(len(re.findall(r'^### E\d+\s*$',p.read_text(encoding='utf-8'),re.M)) for p in pages)
    book_relative=BOOK.relative_to(root).as_posix()
    eligible=subprocess.run(['git','ls-files','--others','--exclude-standard','--',book_relative],cwd=root,capture_output=True,text=True).stdout.strip()==book_relative
    tracked=bool(subprocess.run(['git','ls-files','--',book_relative],cwd=root,capture_output=True,text=True).stdout.strip())
    if not(eligible or tracked):errors.append('Production workbook is ignored or not discoverable by git')
    return {'workbook_sha256':digest(),'counts':{k:len(v) for k,v in data.items()},'B_core':sorted(b),'C_core':sorted(c),'core_intersection':sorted(b&c),'primary_track':dict(Counter(p['Primary_Track'] for p in pp)),
      'evidence_per_paper':dict(Counter(e['Paper_ID'] for e in ee)),
      'evidence_type':dict(Counter(e['Evidence_Type'] for e in ee)),
      'directness':dict(Counter(e['Evidence_Directness'] for e in ee)),
      'verification_status':dict(Counter(e['Verification_Status'] for e in ee)),
      'needs_check_evidence':[e['Evidence_ID'] for e in ee if e['Needs_Check']=='Yes'],
      'pairing_status':dict(Counter(e['Pairing_Status'] for e in ee)),
      'synthesis_readiness':dict(Counter(s['Readiness'] for s in ss)),
      'unmapped_new_extracts':[e['Evidence_ID'] for e in ee if e.get('Legacy_Evidence_Ref')=='NA'],
      'legacy_paper_count':len(pages),'legacy_evidence_count':legacy_count,
      'sources':source_checks,'git_eligible':eligible or tracked,'git_already_tracked':tracked,
      'errors':errors,'machine_scientific_evidence_checked':False,
      'manual_verification_scope':'Per-record Verification_Scope and docs/bc-pilot-2026-09-25/report.md; not whole-paper approval.'}

if __name__=='__main__':
    result=run();print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(bool(result['errors']))
