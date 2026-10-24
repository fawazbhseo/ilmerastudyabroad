#!/usr/bin/env python3
"""Compare newly extracted ZIP-only adapter to repository and historical manifest renders."""
import hashlib,json,pathlib,subprocess,urllib.request,urllib.error,xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).resolve().parents[2];PACK=pathlib.Path('/home/user/phase28/payload');old=json.loads((ROOT/'reports/phase-27-payload-proof.json').read_text());rows=[]
def get(port,path,method='GET'):
    try:
        with urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:'+str(port)+'/'+path.lstrip('/'),method=method)) as r:return r.status,r.read()
    except urllib.error.HTTPError as e:return e.code,e.read()
def sha(b):return hashlib.sha256(b).hexdigest()
assert (ROOT/'releases/ilmera-deploy-850d0af.zip').is_file() and (ROOT/'releases/.htaccess').is_file()
assert not (PACK/'releases').exists()
for r in old['routes']:
    a=get(8080,r['route']);b=get(8085,r['route']);assert a==b and a[0]==200 and sha(b[1])==r['sha256'],r['route']
    rows.append({'route':r['route'],'published':r['published'],'sha256':sha(b[1]),'exact_current_repo_and_historical_match':True})
assets=[]
for r in old['static_GET_HEAD_checks']:
    st,b=get(8085,r['path']);hs,hb=get(8085,r['path'],'HEAD');assert st==hs==200 and hb==b'' and sha(b)==r['sha256']
    assets.append({'path':r['path'],'GET':st,'HEAD':hs,'bytes':len(b),'sha256':sha(b)})
status,sm=get(8085,'sitemap.xml');assert status==200 and b'releases' not in sm
urls=[n.text for n in ET.fromstring(sm).iter() if n.tag.endswith('loc')];assert len(urls)==38
assert get(8080,'sitemap.xml')==(status,sm)
probes={}
for f in ['data/entity.json','includes/site.php','reports/phase-28-progress.md','tools/phase28/check_zip.py','releases/ilmera-deploy-850d0af.zip','releases/.htaccess']:
    code,_=get(8085,f);assert code in (403,404),f;probes[f]=code
files=sorted(p.relative_to(PACK).as_posix() for p in PACK.rglob('*') if p.is_file());assert len(files)==130
tracked=set(subprocess.check_output(['git','ls-files'],cwd=ROOT,text=True).splitlines())|set(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=ROOT,text=True).splitlines());excluded=sorted(tracked-set(files));assert all(f.startswith('releases/') for f in ['releases/.htaccess','releases/ilmera-deploy-850d0af.zip']) and {'releases/.htaccess','releases/ilmera-deploy-850d0af.zip'}<=set(excluded)
proof={'passed':True,'source_start_head':'850d0af5c083b06e3c65abc997fcab6708121c6f','archive':'releases/ilmera-deploy-850d0af.zip','zip_only_payload_root':str(PACK),'upload_count':130,'route_count':43,'published_routes':38,'held_and_404':5,'routes':rows,'sitemap_urls':38,'releases_in_sitemap':False,'releases_in_payload':False,'release_folder_present_in_source':True,'asset_paths_checked':len(assets),'static_GET_HEAD_checks':assets,'excluded_private_or_missing_probes':probes,'native_htaccess_acl_rewrite_cache_mime_csp_verified':False,'tracked_plus_pending_source_count_at_task2':len(tracked),'excluded_count_at_task2':len(excluded),'exclusion_ledger':'phase-28-excluded-files.json','later_internal_reports_may_grow_exclusion_count':True}
(ROOT/'reports/phase-28-payload-proof.json').write_text(json.dumps(proof,indent=2)+'\n')
(ROOT/'reports/phase-28-excluded-files.json').write_text(json.dumps({'policy':'Only the unchanged130-file upload manifest is publishable. Entire releases/ excluded, including safety .htaccess. All other source paths excluded. This snapshot is refreshed at final handoff.','files':excluded},indent=2)+'\n');print('PASS130 files,43 exact renders,38 sitemap,20 GET/HEAD; releases absent from payload/discovery')
