#!/usr/bin/env python3
"""Compare every current local PHP render with the immutable Phase31 pre-fix HTML."""
from __future__ import annotations
import gzip,hashlib,json,os,pathlib,subprocess,sys
from bs4 import BeautifulSoup
from source_policy import verify_task2_spacing_scope
ROOT=pathlib.Path(__file__).resolve().parents[2]
ARCHIVE=ROOT/'reports/phase-31-before-renders.json.gz'
EVIDENCE=pathlib.Path(os.environ.get('PHASE31_EVIDENCE','/home/user/phase31'))
RENDER=pathlib.Path(os.environ.get('PHASE31_RENDER_DIR',str(EVIDENCE/'render-after')))
COMPARISON_OUT=pathlib.Path(os.environ.get('PHASE31_COMPARISON_OUT',str(ROOT/'reports/phase-31-render-comparison.json')))

def runtime_paths_changed(source_head,current_head):
    if subprocess.run(['git','merge-base','--is-ancestor',source_head,current_head],cwd=ROOT).returncode:raise SystemExit('Render source is not an ancestor of verification HEAD')
    names=subprocess.check_output(['git','diff','--name-only',source_head,current_head],cwd=ROOT,text=True).splitlines()
    roots={'index.php','services.php','about.php','contact.php','404.php','all-pages.php','privacy-policy.php','terms.php','robots.txt','sitemap.xml','llms.txt','llms-full.txt','favicon.ico','deploy-check.php'}
    return [p for p in names if pathlib.PurePosixPath(p).parts[0] in {'assets','data','includes','destinations','places','blog'} or p in roots or pathlib.PurePosixPath(p).name=='.htaccess' or (len(pathlib.PurePosixPath(p).parts)==1 and p.endswith('.php'))]

def html_signature(raw):
    soup=BeautifulSoup(raw,'html.parser')
    for e in soup.select('script,style,noscript'):e.decompose()
    text=' '.join(soup.get_text(' ',strip=True).split())
    headings=[(e.name,' '.join(e.get_text(' ',strip=True).split())) for e in soup.select('h1,h2,h3,h4,h5,h6')]
    original=BeautifulSoup(raw,'html.parser')
    title=' '.join((original.title.get_text(' ',strip=True) if original.title else '').split())
    metadata=[sorted((k,tuple(v) if isinstance(v,list) else v) for k,v in e.attrs.items()) for e in original.select('meta')]
    links=[]
    for a in BeautifulSoup(raw,'html.parser').select('a'):
        links.append({'attributes':sorted((k,tuple(v) if isinstance(v,list) else v) for k,v in a.attrs.items()),'text':' '.join(a.get_text(' ',strip=True).split())})
    images=[]
    for img in BeautifulSoup(raw,'html.parser').select('img'):
        images.append(sorted((k,tuple(v) if isinstance(v,list) else v) for k,v in img.attrs.items()))
    data=[]
    faq=[]
    for sc in original.select('script[type="application/ld+json"]'):
        try:data.append(json.loads(sc.get_text()))
        except Exception as e:raise AssertionError(f'Invalid JSON-LD: {e}')
    for box in original.select('details.il-faq,.faq-item'):
        faq.append({'class':box.get('class',[]),'text':' '.join(box.get_text(' ',strip=True).split()),'summary':(' '.join(box.select_one('summary').get_text(' ',strip=True).split()) if box.select_one('summary') else None)})
    canon=[(x.get('rel'),x.get('href')) for x in original.select('link[rel="canonical"]')]
    robots=[x.get('content') for x in original.select('meta[name="robots"]')]
    return {'text':text,'title':title,'metadata':metadata,'headings':headings,'links':links,'images':images,'json_ld':data,'faq':faq,'canonical':canon,'robots':robots}

def main():
    if not ARCHIVE.exists():raise SystemExit('Missing immutable pre-fix render archive')
    with gzip.open(ARCHIVE,'rb') as f:baseline=json.loads(f.read())
    if len(baseline['routes'])!=43:raise SystemExit('Baseline must contain 43 rendered routes')
    route_index=RENDER/'routes.json'
    if not route_index.exists():route_index=EVIDENCE/'routes.json'
    index=json.loads(route_index.read_text())
    current_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    approved_visual_files=verify_task2_spacing_scope(baseline['source_head'],current_head)
    render_source=index.get('source_head')
    runtime_changes=runtime_paths_changed(render_source,current_head)
    if runtime_changes:raise SystemExit(f'Current route render is stale for runtime source: {runtime_changes}')
    current={x['url']:x for x in index['routes']}
    baseline_status={x['route']:x['http_status'] for x in baseline.get('route_inventory',[])}
    if set(baseline_status)!=set(baseline['routes']):raise SystemExit('Baseline status inventory missing or incomplete')
    if set(current)!=set(baseline['routes']):raise SystemExit('Route inventory changed')
    rows=[]
    for route in sorted(baseline['routes']):
        old=baseline['routes'][route]['html'];entry=current[route];new=(RENDER/entry['evidence']).read_text(encoding='utf-8')
        a=html_signature(old);b=html_signature(new)
        changed=[k for k in a if a[k]!=b[k]]
        if changed:raise AssertionError(f'{route} changed content invariants: {changed}')
        if entry['status']!=baseline_status[route]:raise AssertionError(f'{route} HTTP status changed: {baseline_status[route]} -> {entry["status"]}')
        rows.append({'route':route,'http_status':entry['status'],'source_file':entry['file'],'render_bytes':entry['bytes'],'render_sha256':hashlib.sha256(new.encode()).hexdigest(),'text_title_metadata_headings_faq_links_images_jsonld_canonical_robots_status_exact':True})
    expected_sitemap_count=38
    sitemap=EVIDENCE/'sitemap.xml';baseline_sitemap=ROOT/'reports/phase-31-before-sitemap.xml'
    if not sitemap.exists() or not baseline_sitemap.exists():raise SystemExit('Missing pre-fix or current sitemap snapshot')
    sitemap_bytes=sitemap.read_bytes();baseline_sitemap_bytes=baseline_sitemap.read_bytes()
    if sitemap_bytes!=baseline_sitemap_bytes:raise AssertionError('Sitemap bytes changed')
    from xml.etree import ElementTree as ET
    root=ET.fromstring(sitemap_bytes);urls=[e.text for e in root.iter() if e.tag.endswith('loc')]
    if len(urls)!=expected_sitemap_count or len(set(urls))!=expected_sitemap_count:raise AssertionError(f'Sitemap entry count changed: {len(urls)}')
    out={'passed':True,'routes':len(rows),'source_head':index['source_head'],'baseline_source_head':baseline['source_head'],'approved_visual_source_files':approved_visual_files,'authorized_visual_source_scope_passed':True,'content_invariants':['all visible/document text and order','title and all meta attributes','headings in order','visible/custom FAQ text','all link hrefs and attributes/multiplicity/order','all img src/alt/dimensions/loading/srcset and attributes','JSON-LD graphs','canonicals','robots directives','HTTP statuses','sitemap exact bytes and 38 entries'],'rows':rows,'sitemap_entries':expected_sitemap_count,'sitemap_sha256':hashlib.sha256(sitemap_bytes).hexdigest(),'live_or_native_hosting':False}
    COMPARISON_OUT.parent.mkdir(parents=True,exist_ok=True)
    COMPARISON_OUT.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
    print(f"PASS exact pre-fix text/title/meta/headings/FAQ/links/images/JSON-LD/canonical/robots/status/sitemap: {len(rows)} routes")
if __name__=='__main__':main()
