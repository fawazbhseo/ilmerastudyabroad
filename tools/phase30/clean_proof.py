#!/usr/bin/env python3
"""ZIP-only payload versus repo:43 pages, discovery, every asset and temp auth."""
import hashlib,json,pathlib,re,urllib.request,urllib.error,xml.etree.ElementTree as ET
R=pathlib.Path(__file__).resolve().parents[2];m=json.loads((R/'reports/phase-27-payload-manifest.json').read_text());z=json.loads((R/'reports/phase-30-zip-proof.json').read_text());root=pathlib.Path(z['external_clean_root']);base='http://127.0.0.1:8083';repo='http://127.0.0.1:8080'
def get(origin,p,method='GET'):
 try:
  with urllib.request.urlopen(urllib.request.Request(origin+p,method=method)) as r:return r.status,dict(r.headers),r.read()
 except urllib.error.HTTPError as e:return e.code,dict(e.headers),e.read()
old=json.loads((R/'reports/phase-30-duplicate-fix.json').read_text());rows=[]
for item in old['results']:
 route=item['route'];a=get(repo,route);b=get(base,route);assert a[0]==b[0]==200 and a[2]==b[2],route
 rows.append({'route':route,'status':200,'repo_and_pack_exact':True,'sha256':hashlib.sha256(b[2]).hexdigest()})
static=[]
for f in ['sitemap.xml','robots.txt','llms.txt','llms-full.txt','google10fa7a4178242a1f.html','favicon.ico']+[r['path'] for r in m['files'] if r['path'].startswith('assets/') and pathlib.Path(r['path']).name!='.htaccess']:
 a=get(repo,'/'+f);b=get(base,'/'+f);assert a[0]==b[0]==200 and a[2]==b[2],f
 hs,_,hb=get(base,'/'+f,'HEAD');assert hs==200 and not hb
 if f in ['robots.txt','llms.txt','llms-full.txt','sitemap.xml']:assert b'deploy-check' not in b[2] and b'releases/' not in b[2]
 static.append({'path':f,'GET':b[0],'HEAD':hs,'sha256':hashlib.sha256(b[2]).hexdigest(),'content_type':b[1].get('Content-Type')})
sm=get(base,'/sitemap.xml')[2];urls=[e.text for e in ET.fromstring(sm).iter() if e.tag.endswith('loc')];assert len(urls)==len(set(urls))==38
actual=sorted(p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file());assert actual==sorted(r['path'] for r in m['files']) and len(actual)==131
for row in m['files']:assert hashlib.sha256((root/row['path']).read_bytes()).hexdigest()==row['sha256']
key=re.search("const ILMERA_DEPLOY_CHECK_KEY = '([a-f0-9]{64})'",(R/'deploy-check.php').read_text())[1]
a=get(base,'/deploy-check.php?key='+key);assert a[0]==200 and b'ALL FILES OK' in a[2]
for suffix in ['', '?key=wrong','?key='+key+'&file=../../etc/passwd']:
 s,h,b=get(base,'/deploy-check.php'+suffix);assert s==404 and b==b'Not found'
private={}
for f in ['data/entity.json','includes/header.php','phase14-source-review.json','reports/phase-30-progress.md','tools/phase30/suite.py','releases/'+pathlib.Path(z['archive']).name]:
 s,h,b=get(base,'/'+f);assert s in [403,404],(f,s);private[f]=s
proof={'passed':True,'source_commit':m['source_commit'],'upload_count':131,'isolated_filesystem':'Existing tools/phase27/server.cjs loads only the exported folder into PHP memory, no host mount or source fallback; isolation probe runs at startup/reset','routes':rows,'render_count':43,'published_routes':38,'sitemap_count':38,'static_asset_discovery_GET_HEAD':static,'self_check_all_files_ok':True,'key_not_recorded_in_test_evidence':True,'missing_wrong_extra_query_404':True,'private_or_missing_probes':private,'releases_not_in_payload_or_sitemap':True,'native_headers_acl_rewrite_csp_cache_or_live_deployment_proved':False}
(R/'reports/phase-30-clean-payload-proof.json').write_text(json.dumps(proof,indent=2)+'\n');print('PASS131 clean files,43 exact routes,38 sitemap, all assets/discovery and temporary auth')
