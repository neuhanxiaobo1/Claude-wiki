"""Read-only external source access; local identity records and PDF renders only."""
from pathlib import Path
import json,hashlib,yaml,fitz,re,sys
D=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
NAMES=['Cao-2013-SiNOf-BN-High-Temperature','Cao-2022-Si3N4f-SiNO-Composites','Li-2023-BN-SiON-Double-Interphase','Meng-2023-PIP-Heating-Rate-Si3N4','Liu-2024-Porous-Si3N4']
CACHES=['11856','12803','12789','11867','10110']
def records():
    result=[]
    for i,(name,c) in enumerate(zip(NAMES,CACHES),1):
        page=D/'wiki/papers'/f'{name}.md';content=page.read_text(encoding='utf-8');meta=yaml.safe_load(content.split('---')[1]);cache=Path(r'D:\shuju\zotero1\llm-for-zotero-mineru')/c
        manifest=json.loads((cache/'manifest.json').read_text(encoding='utf-8'))
        identity=json.loads((cache/'_llm_source.json').read_text(encoding='utf-8'))
        assert identity['parentItemKey']==meta['zotero_item_key'] and identity['attachmentKey']==meta['zotero_attachment_key']
        pdf=meta['source'] if i<5 else re.search(r'原PDF：`([^`]+)`',content).group(1)
        r={'Paper_ID':f'P{i:04d}','page':f'directions/wave-transparent-composites/wiki/papers/{name}.md','doi':meta['doi'],'title':meta['title'],'year':meta['year'],'item_key':meta['zotero_item_key'],'attachment_key':meta['zotero_attachment_key'],'pdf':pdf,'md':str(cache/'full.md'),'manifest':str(cache/'manifest.json')}
        for label,path in [('pdf',Path(pdf)),('md',cache/'full.md'),('legacy',page)]:r[label+'_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
        with fitz.open(pdf) as doc:r['pdf_pages']=len(doc)
        r['manifest_sections']=[s.get('heading') for s in manifest.get('sections',[])]
        r['figure_blocks']=len(manifest.get('figureBlocks',[]));result.append(r)
    return result
if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='identity':
        data=records();(HERE/'sources.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
        print(json.dumps(data,ensure_ascii=False,indent=2))
    else:
        data=json.loads((HERE/'sources.json').read_text(encoding='utf-8'));r=data[int(sys.argv[2])-1]
        if mode=='md':
            t=Path(r['md']).read_text(encoding='utf-8');t=re.split(r'(?im)^#*\s*References\s*$',t)[0]
            print(t)
        elif mode=='pdf':
            with fitz.open(r['pdf']) as doc:
                for num in map(int,sys.argv[3:]):print(f'PDF PAGE {num}\n'+doc[num-1].get_text())
        elif mode=='render':
            out=D/'raw/bc-pilot-2026-09-25';out.mkdir(exist_ok=True)
            with fitz.open(r['pdf']) as doc:
                for num in map(int,sys.argv[3:]):
                    target=out/f'{r["Paper_ID"]}-p{num}.png';doc[num-1].get_pixmap(matrix=fitz.Matrix(1.6,1.6)).save(target);print(target)
