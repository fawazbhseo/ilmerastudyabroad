#!/usr/bin/env python3
"""Reproduce approved whole-square derivatives. Requires Pillow 13.0.0 for byte checks.

Default: verify only. --write creates/updates the two authorized derivatives,
never the original. No crop, retouching, metadata import or site-text edits.
"""
import argparse,hashlib,io,json,pathlib,subprocess
from PIL import Image
ROOT=pathlib.Path(__file__).resolve().parents[2]
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--write',action='store_true');a=p.parse_args()
original=ROOT/'assets/images/fawazbh.webp';before=original.read_bytes()
assert before==subprocess.check_output(['git','show','9157825:assets/images/fawazbh.webp'],cwd=ROOT),'Original portrait changed'
rows=[]
with Image.open(io.BytesIO(before)) as image:
 assert image.format=='PNG' and image.size==(1254,1254)
 for width in [384,192]:
  out=ROOT/f'assets/images/fawazbh-{width}.webp';buffer=io.BytesIO()
  image.resize((width,width),Image.Resampling.LANCZOS).save(buffer,format='WEBP',quality=82,method=6)
  encoded=buffer.getvalue()
  assert len(encoded)<60000 and encoded[:4]==b'RIFF' and encoded[8:12]==b'WEBP'
  if a.write:out.write_bytes(encoded)
  assert out.read_bytes()==encoded,'Derivative not reproducible with the documented encoder'
  with Image.open(out) as check:assert check.format=='WEBP' and check.size==(width,width)
  rows.append({'path':out.relative_to(ROOT).as_posix(),'bytes':len(encoded),'format':'WEBP','dimensions':[width,width]})
assert original.read_bytes()==before,'Original was modified'
print(json.dumps({'status':'PASS','original_bytes':len(before),'original_sha256':hashlib.sha256(before).hexdigest(),'derivatives':rows,'operation':'whole-square LANCZOS resize, WebP quality 82 method 6; no crop or retouching'}))
