"""Exact isolated allowlist. Three root review journals are runtime inputs, not optional exports."""
from pathlib import Path
import json,hashlib,shutil,sys,urllib.request,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[2];C=Path('/home/user/phase26/candidate');P=Path('/home/user/phase26/payload');routes=json.loads(Path('/home/user/phase26/evidence/routes.json').read_text());mode=sys.argv[1]
if mode=='build':
 assert not P.exists(),'Do not mix a previous folder with a clean proof'
 files={i['file'] for i in routes.values()}|{'.htaccess','sitemap.php','sitemap.xml','robots.txt','llms.txt','llms-full.txt','favicon.ico','google10fa7a4178242a1f.html','phase14-source-review.json','phase14-location-review.json','phase14-article-review.json'}
 for folder in ['includes','data','destinations','places']:
  files|={str(p.relative_to(C)) for p in (C/folder).rglob('*') if p.is_file() and (p.suffix=='.php' or p.name=='.htaccess' or folder=='data' and p.suffix=='.json')}
 files|={str(p.relative_to(C)) for p in (C/'assets').rglob('*') if p.is_file() and p.suffix.lower() not in ['.md','.json','.csv','.pyc'] and '__pycache__' not in p.parts}
 for f in sorted(files):p=P/f;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(C/f,p)
 assert all(not p.is_symlink() for p in P.rglob('*'))
 rows=[{'path':f,'bytes':(P/f).stat().st_size,'sha256':hashlib.sha256((P/f).read_bytes()).hexdigest()} for f in sorted(files)]
 manifest={'source':'isolated164d6de plus reports/phase-26-team-only.patch, NOT a release branch','files':rows,'runtime_json_exceptions':['phase14-source-review.json','phase14-location-review.json','phase14-article-review.json']+sorted(f for f in files if f.startswith('data/') and f.endswith('.json')),'runtime_denied_folders':['data/','includes/','destinations/','places/'],'clean_folder':'/home/user/phase26/payload','no_symlinks':True}
 (R/'reports/phase-26-payload-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print('Clean allowlist copied',len(rows),'files')
elif mode=='check':
 manifest=json.loads((R/'reports/phase-26-payload-manifest.json').read_text());actual={str(p.relative_to(P)) for p in P.rglob('*') if p.is_file()};assert actual=={r['path'] for r in manifest['files']}
 for row in manifest['files']:assert hashlib.sha256((P/row['path']).read_bytes()).hexdigest()==row['sha256']
 results=[]
 for route,info in routes.items():
  before=urllib.request.urlopen('http://127.0.0.1:8080'+route).read();after=urllib.request.urlopen('http://127.0.0.1:8083'+route).read();assert before==after,(route,'Clean payload output differs, runtime dependency missing');results.append({'route':route,'published':info['status']=='published' and route!='/404','sha256':hashlib.sha256(after).hexdigest(),'exact_candidate_match':True})
 assets=[r['path'] for r in manifest['files'] if r['path'].startswith('assets/') or r['path']=='favicon.ico']
 for f in ['sitemap.xml','robots.txt','llms.txt','llms-full.txt','google10fa7a4178242a1f.html']+assets:
  body=urllib.request.urlopen('http://127.0.0.1:8083/'+f).read();assert body==(P/f).read_bytes(),f
 n=len(ET.fromstring(urllib.request.urlopen('http://127.0.0.1:8083/sitemap.xml').read()).findall('.//{*}loc'));assert n==38
 denied=[]
 for f in manifest['runtime_json_exceptions']+['data/proof.php','includes/posts.php','destinations/germany.php','places/mysuru.php']:
  try:urllib.request.urlopen('http://127.0.0.1:8083/'+f);raise AssertionError('Private input exposed '+f)
  except urllib.error.HTTPError as e:assert e.code in [403,404];denied.append({'path':f,'local_status':e.code})
 result={'passed':True,'published_routes':sum(r['published'] for r in results),'all_route_count':len(results),'routes':results,'sitemap_urls':n,'asset_count':len(assets),'all_asset_bytes_match':True,'payload_files':len(manifest['files']),'denied_runtime_probes':denied,'no_symlink_or_source_fallback':True,'native_apache':False,'local_adapter_only':True,'limits':'Fresh PHP instance rooted at clean payload, no candidate symlinks; application files resolve within payload. PHP engine/libraries remain external test infrastructure. HTACCESS manually mirrored, NOT executed. No actual contact submission or native/live proof.'}
 (R/'reports/phase-26-payload-checks.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS isolated payload:',len(results),'routes/38 published,',len(assets),'assets,38 sitemap URLs')
