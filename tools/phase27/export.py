#!/usr/bin/env python3
"""Offline, hash-checked export into a NEW folder. No network or deployment action."""
import argparse,hashlib,json,pathlib,subprocess,zipfile
ROOT=pathlib.Path(__file__).resolve().parents[2]
p=argparse.ArgumentParser();p.add_argument('--out',type=pathlib.Path,required=True);p.add_argument('--zip',type=pathlib.Path);a=p.parse_args()
m=json.loads((ROOT/'reports/phase-27-payload-manifest.json').read_text())
assert not a.out.exists(),'Destination must be a new temporary folder, never an existing live folder'
a.out.mkdir(parents=True)
for row in m['files']:
    f=row['path'];assert not pathlib.PurePosixPath(f).is_absolute() and '..' not in pathlib.PurePosixPath(f).parts
    body=subprocess.check_output(['git','show',m['source_commit']+':'+f],cwd=ROOT)
    assert len(body)==row['bytes'] and hashlib.sha256(body).hexdigest()==row['sha256'],f
    target=a.out/f;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(body)
if a.zip:
    assert not a.zip.exists(),'Refuse to overwrite an existing artifact'
    with zipfile.ZipFile(a.zip,'x',compression=zipfile.ZIP_DEFLATED) as z:
        for row in m['files']:z.write(a.out/row['path'],row['path'])
print('Exported',len(m['files']),'exact files from',m['source_commit'],'to',a.out)
