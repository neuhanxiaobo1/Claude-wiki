"""Read-only validation of the authoritative B/C workbook and every registered paper source."""
from pathlib import Path
from collections import Counter
import json,re,hashlib,subprocess,sys
import openpyxl
from workbook_io import BOOK,HERE,D,rows,validate,digest,splitids

def run():
    wb=openpyxl.load_workbook(BOOK);errors,data=validate(wb)
    root=D.parents[1]
    sources=[]
    for paper in data['Paper_Index']:
        path=(root/str(paper.get('Source_Manifest',''))).resolve()
        if not path.is_relative_to(D.resolve()) or not path.is_file():continue
        entries=json.loads(path.read_text(encoding='utf-8'))
        matches=[s for s in entries if s.get('Paper_ID')==paper['Paper_ID']]
        if len(matches)!=1:errors.append(paper['Paper_ID']+': missing/duplicate source entry');continue
        s=matches[0];sources.append(s)
        if str(s['doi']).strip().lower()!=str(paper['DOI']).strip().lower():errors.append(paper['Paper_ID']+': source DOI mismatch')
        if s['item_key']!=str(paper['Zotero_Item_Key']).split(':')[-1]:errors.append(paper['Paper_ID']+': source item mismatch')
    source_checks=[]
    for s in sources:
        for kind in [k for k in ['pdf','md','manifest','identity'] if k+'_sha256' in s]:
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
      'manual_verification_scope':'Per-record Verification_Scope and corresponding batch report; not whole-paper approval.'}

if __name__=='__main__':
    result=run();print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(bool(result['errors']))
