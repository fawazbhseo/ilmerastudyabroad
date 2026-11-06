"""Freeze both arms before measurement, then use identical HTTP delivery."""
from pathlib import Path
import json,urllib.request,hashlib,subprocess
R=Path(__file__).resolve().parents[2];P=Path('/home/user/phase25c-evidence');P.mkdir(exist_ok=True)
routes=['/','/services','/contact','/about','/study-in-germany','/study-in-italy','/study-in-gcc','/study-abroad-counselling-mysuru','/study-abroad-counselling-bengaluru','/blog/how-to-choose-study-abroad-consultant-karnataka','/blog/documents-needed-to-study-abroad-from-india','/blog/','/privacy-policy','/all-pages']
old=json.loads((R/'reports/phase-25-baseline-renders.json').read_text())['routes'];refs=json.loads((P/'stage1-references.json').read_text())['routes'];data={};manifest=[]
for route in routes:
 a=(refs if route in refs else old)[route]['html'];b=urllib.request.urlopen('http://127.0.0.1:8080'+route).read().decode();data[route]={'A':a,'B':b};manifest.append({'route':route,'A_source':'Stage1 3f0e141' if route in refs else 'immutable Phase24b captured HTML','A_sha256':hashlib.sha256(a.encode()).hexdigest(),'B_sha256':hashlib.sha256(b.encode()).hexdigest(),'identical_control':a==b if route in refs else None})
(P/'fixtures.json').write_text(json.dumps(data));(R/'reports/phase-25c-ab-fixtures.json').write_text(json.dumps({'routes':manifest,'delivery':'Both frozen HTML arms served by same Node fixture server at identical origin/path, with identical static asset/CDN mirror handling. Not native hosting.'},indent=2)+'\n')
print('Frozen',len(data),'routes including all4 controls')
