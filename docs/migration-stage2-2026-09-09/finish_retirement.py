"""Resume an interrupted retirement from the validated stage2 preview.
Only touches enumerated old file paths; locked originals are reported and retained.
"""
from pathlib import Path
import json, zipfile, hashlib
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
record=json.loads((OUT/'execution.json').read_text(encoding='utf-8'))
with zipfile.ZipFile(ROOT/record['backup']) as z: old={p:z.read(p) for p in z.namelist()}
with zipfile.ZipFile(ROOT/record['preview']) as z: planned={p:z.read(p) for p in z.namelist()}
update_file=OUT/'post-migration-updates.json'
updates=json.loads(update_file.read_text(encoding='utf-8')) if update_file.exists() else {}
for p,b in planned.items():
    assert (ROOT/p).read_bytes()==b or p in updates and hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==updates[p]['sha256'], 'Unrecorded output change: '+p
locked=[]
for p in record['retired']:
    source=(ROOT/p).resolve()
    assert source.is_relative_to(ROOT) and source!=ROOT
    if not source.exists(): continue
    assert source.is_file() and source.read_bytes()==old[p], 'Old file changed: '+p
    assert (ROOT/record['mapping'][p]).is_file()
    try: source.unlink()
    except PermissionError as e: locked.append({'source':p,'target':record['mapping'][p],'error':str(e)})
for prefix in ('raw','wiki','synthesis'):
    parent=(ROOT/prefix).resolve(); assert parent.parent==ROOT
    if parent.exists():
        for d in sorted((x for x in parent.rglob('*') if x.is_dir()),key=lambda x:len(x.parts),reverse=True):
            assert d.resolve().is_relative_to(parent)
            if not any(d.iterdir()): d.rmdir()
        if not any(parent.iterdir()): parent.rmdir()
record['mode']='apply-recovered'
record['locked_legacy_copies']=locked
record['status']='applied-with-locked-legacy-copy' if locked else 'applied-and-output-hashes-verified'
(OUT/'execution.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':record['status'],'retired_count':len(record['retired'])-len(locked),'locked_legacy_copies':locked},ensure_ascii=False))
