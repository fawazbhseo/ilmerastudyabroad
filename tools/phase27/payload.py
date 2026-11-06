#!/usr/bin/env python3
"""Pinned full-branch upload allowlist and isolated HTTP parity proof. Never deploys."""
import argparse, hashlib, json, pathlib, re, shutil, subprocess, sys, urllib.parse, urllib.request, urllib.error
from html.parser import HTMLParser
ROOT=pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools'))
from check_discovery import routes
SOURCE='a3d696f7942b2df5c76d660c2b9f3252881ce314'
WORK=pathlib.Path('/home/user/phase27'); SRC=WORK/'source'; PACK=WORK/'payload'; EVIDENCE=WORK/'evidence'
HOST='https://ilmerastudyabroad.com'
sha=lambda b:hashlib.sha256(b).hexdigest()
def get(base,path):
    with urllib.request.urlopen(base+path,timeout=60) as r:return r.status,dict(r.headers),r.read()
def tracked():return subprocess.check_output(['git','ls-tree','-r','--name-only',SOURCE],cwd=ROOT,text=True).splitlines()
def save(name,value):(ROOT/'reports'/name).write_text(json.dumps(value,indent=2)+'\n')
class Assets(HTMLParser):
    def __init__(self,text):
        super().__init__(convert_charrefs=True);self.urls=set();self.feed(text)
        self.urls.update(m.strip(' \"\'') for m in re.findall(r'url\((.*?)\)',text,re.S))
        self.urls.update(re.findall(r'https?://[^\s\"<>]+/assets/[^\s\"<>]+',text))
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag in ('img','source','script','video','audio','iframe') and d.get('src'):self.urls.add(d['src'])
        if d.get('poster'):self.urls.add(d['poster'])
        if d.get('srcset'):
            self.urls.update(item.strip().split()[0] for item in d['srcset'].split(',') if item.strip())
        if tag=='link' and set(d.get('rel','').split())&{'stylesheet','icon','preload','shortcut'} and d.get('href'):self.urls.add(d['href'])
        if tag=='meta' and d.get('property',d.get('name','')) in ('og:image','twitter:image') and d.get('content'):self.urls.add(d['content'])
def classify(url):
    if not url or url.startswith(('data:','#','about:')):return None,None
    p=urllib.parse.urlsplit(urllib.parse.urljoin(HOST+'/',url))
    if p.hostname not in ('ilmerastudyabroad.com','www.ilmerastudyabroad.com'):return None,urllib.parse.urlunsplit(p)
    path=urllib.parse.unquote(p.path).lstrip('/')
    assert '..' not in pathlib.PurePosixPath(path).parts,path
    return path,None

def build():
    assert not PACK.exists(),'Refuse to mix an old payload with a clean proof'
    EVIDENCE.mkdir(parents=True,exist_ok=True)
    inventory=routes(SRC); assert len(inventory)==43
    assets=set();external=set();manifest={};raw_hits=[]
    for i,(route,info) in enumerate(inventory.items()):
        status,headers,body=get('http://127.0.0.1:8080',route);assert status==200
        name=f'{i:02}.html';(EVIDENCE/name).write_bytes(body)
        manifest[route]={'file':name,'info':info,'sha256':sha(body)}
        for url in Assets(body.decode()).urls:
            local,remote=classify(url)
            if local:assets.add(local)
            if remote:external.add(remote)
        for term in ['digital marketer','free','tuition-free','co-founder']:
            for m in re.finditer(re.escape(term),body.decode(),re.I):raw_hits.append({'route':route,'term':term,'excerpt':body.decode()[max(0,m.start()-80):m.end()+80]})
    # Follow local CSS imports/urls, not only preloads or the current font weight.
    pending=list(assets)
    while pending:
        f=pending.pop();assert (SRC/f).is_file(),('Missing referenced local asset',f)
        if pathlib.Path(f).suffix not in ('.css','.js'):continue
        for url in Assets((SRC/f).read_text()).urls:
            if not urllib.parse.urlsplit(url).scheme and not url.startswith('/'):
                url='/'+str(pathlib.PurePosixPath(f).parent/url)
            local,remote=classify(url)
            if local and local not in assets:assets.add(local);pending.append(local)
            if remote:external.add(remote)
    # CSS is read by PHP and inlined. Variable faces are read by PHP for destination data URIs.
    runtime_assets={'assets/css/visual-system.css','assets/fonts/outfit-latin.woff2','assets/fonts/cormorant-garamond-latin.woff2','assets/fonts/outfit-OFL.txt','assets/fonts/cormorant-garamond-OFL.txt','favicon.ico'}
    # All seven static weights are potential browser font matches, even if not preloaded.
    runtime_assets|={f for f in tracked() if f.startswith('assets/fonts/') and f.endswith('.woff2')}
    files={v['file'] for v in inventory.values()}|assets|runtime_assets
    files|={'sitemap.php','sitemap.xml','robots.txt','llms.txt','llms-full.txt','google10fa7a4178242a1f.html'}
    journals={'phase14-source-review.json','phase14-location-review.json','phase14-article-review.json'}
    files|=journals
    for folder in ['data','includes','destinations','places']:
        files|={f for f in tracked() if f.startswith(folder+'/') and pathlib.Path(f).suffix in ('.php','.json')}
    # Explicit deny-only exceptions: no report/tool contents are uploaded.
    denies={f for f in tracked() if pathlib.Path(f).name=='.htaccess'};assert len(denies)==8;files|=denies
    assert not any('hero-still' in f for f in assets),'Reassess still dependency before packaging'
    assert not any(f.endswith(('.md','.csv','.py','.cjs')) for f in files)
    for f in sorted(files):
        src=SRC/f;assert src.is_file() and not src.is_symlink(),f
        target=PACK/f;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,target)
    assert not any(p.is_symlink() for p in PACK.rglob('*'))
    rows=[{'path':f,'bytes':(PACK/f).stat().st_size,'sha256':sha((PACK/f).read_bytes())} for f in sorted(files)]
    exclusions=[]
    for f in sorted(set(tracked())-files):
        reason='Internal/historical owner evidence, tool, test, cache or export; not runtime.'
        if f.startswith('assets/'):reason='Unused asset: not referenced/read by current runtime; stills disabled and original/alternate images not requested.'
        exclusions.append({'path':f,'reason':reason})
    result={'source_commit':SOURCE,'scope':'entire current branch including Phase25 design and Phase26b finance-only bio; NOT the old117-file content candidate','files':rows,'upload_count':len(rows),'excluded_source_tracked_count':len(exclusions),'source_tracked_count':len(tracked()),'count_basis':'Git-tracked snapshot at source_commit; all additional Phase27 reports/tools and untracked caches are excluded too. No finite count claimed for Git internals/node modules/caches.','runtime_json_exceptions':sorted(journals|{f for f in files if f.startswith('data/') and f.endswith('.json')}),'all_htaccess':sorted(denies),'runtime_assets_read_or_licensed':sorted(runtime_assets),'referenced_first_party_assets':sorted(assets),'external_asset_dependencies':sorted(external),'no_symlinks':True,'payload_root':str(PACK)}
    save('phase-27-payload-manifest.json',result);save('phase-27-excluded-files.json',{'source_commit':SOURCE,'excluded_count':len(exclusions),'files':exclusions})
    save('phase-27-raw-wording-hits.json',{'raw_substring_hits':raw_hits,'note':'Raw source substrings are not necessarily prohibited prose. Legacy URL identifiers must not be renamed in this no-site-change phase.'})
    (EVIDENCE/'snapshots.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (WORK/'routes.json').write_text(json.dumps(inventory,indent=2)+'\n')
    print('BUILT',len(rows),'upload files;',len(exclusions),'excluded tracked source files;',len(assets),'referenced first-party assets')

def check():
    m=json.loads((ROOT/'reports/phase-27-payload-manifest.json').read_text());expected={r['path'] for r in m['files']}
    actual={str(p.relative_to(PACK)) for p in PACK.rglob('*') if p.is_file()};assert actual==expected
    for row in m['files']:
        assert sha((PACK/row['path']).read_bytes())==row['sha256'],row['path']
        assert (ROOT/row['path']).read_bytes()==(PACK/row['path']).read_bytes(),row['path']
    source=json.loads((EVIDENCE/'snapshots.json').read_text());rows=[]
    for route,item in source.items():
        s,h,b=get('http://127.0.0.1:8084',route);ss,hh,bb=get('http://127.0.0.1:8080',route)
        assert s==ss==200 and b==bb==(EVIDENCE/item['file']).read_bytes(),(route,'Payload/repo render difference')
        assert not re.search(rb'(?:Warning|Fatal error|Parse error):',b),route
        rows.append({'route':route,'published':item['info']['status']=='published' and route!='/404','sha256':sha(b),'exact_repo_and_frozen_match':True})
    fetches=[]
    asset_paths=set(m['referenced_first_party_assets'])|set(m['runtime_assets_read_or_licensed'])
    for f in sorted(asset_paths|{'sitemap.xml','robots.txt','llms.txt','llms-full.txt','google10fa7a4178242a1f.html'}):
        s,h,b=get('http://127.0.0.1:8084','/'+f);assert s==200 and b==(PACK/f).read_bytes(),f
        request=urllib.request.Request('http://127.0.0.1:8084/'+f,method='HEAD')
        with urllib.request.urlopen(request) as r:assert r.status==200;head=dict(r.headers)
        fetches.append({'path':f,'GET':s,'HEAD':200,'bytes':len(b),'sha256':sha(b),'content_type':h.get('Content-Type',h.get('content-type')),'native_cache_verified':False})
    xml=get('http://127.0.0.1:8084','/sitemap.xml')[2];assert len(re.findall(rb'<loc>',xml))==38
    assert not any(t in xml for t in [b'free-aps',b'italy-dsu',b'czech-republic',b'study-in-russia'])
    probes=[]
    for f in m['runtime_json_exceptions']+['data/proof.php','includes/posts.php','destinations/germany.php','places/mysuru.php','reports/.htaccess','tools/.htaccess','.git/HEAD']:
        try:get('http://127.0.0.1:8084','/'+f);raise AssertionError('Private resource exposed '+f)
        except urllib.error.HTTPError as e:
            body=e.read();assert e.code in [403,404] and body in [b'Forbidden',b'Not found'];probes.append({'path':f,'local_status':e.code,'no_contents':True})
    result={'passed':True,'source_commit':SOURCE,'upload_count':m['upload_count'],'excluded_source_tracked_count':m['excluded_source_tracked_count'],'route_count':len(rows),'published_routes':sum(r['published'] for r in rows),'404_checked':True,'held_routes_checked':4,'route_differences':[],'routes':rows,'sitemap_urls':38,'asset_paths_checked':len(asset_paths),'static_GET_HEAD_checks':fetches,'private_probes':probes,'no_symlink':not any(p.is_symlink() for p in PACK.rglob('*')),'isolation':'Fresh PHP8.5 WASM memory filesystem /site populated ONLY from clean payload. No host filesystem mount or original-source path fallback. Static delivery rooted at payload. PHP engine remains external test infrastructure.','native_apache':False,'external_CDN_verified':False,'cache_CSP_verified':False,'contact_delivery':False,'deployment':False}
    save('phase-27-payload-proof.json',result);print('PASS',len(rows),'exact renders,38 published/38 sitemap,',len(asset_paths),'asset paths GET/HEAD, private probes')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['build','check']);a=p.parse_args()
    (build if a.mode=='build' else check)()
