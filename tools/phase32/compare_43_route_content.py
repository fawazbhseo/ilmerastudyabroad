#!/usr/bin/env python3
"""Compare frozen A and B renders for all protected 43-route content invariants."""
from __future__ import annotations
import gzip, hashlib, html.parser, json, os, pathlib, re, sys, xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parents[2]
A_INDEX=ROOT/'reports/phase-32-before-render-index.json'
A_ARCHIVE=ROOT/'reports/phase-32-before-renders.json.gz'
A_SITEMAP=ROOT/'reports/phase-32-before-sitemap.xml'
B_DIR=pathlib.Path(os.environ.get('PHASE32_B_RENDER_DIR','/home/user/phase32-runtime/phase32-b-4e709ed/render-before'))
B_INDEX=B_DIR/'routes.json'
B_SITEMAP=B_DIR.parent/'sitemap.xml'
OUT=pathlib.Path(os.environ.get('PHASE32_CONTENT_COMPARE_OUT',str(ROOT/'reports/phase-32-43-route-content-comparison.json')))
SUMMARY=pathlib.Path(os.environ.get('PHASE32_CONTENT_COMPARE_MD',str(ROOT/'reports/phase-32-43-route-content-comparison.md')))
A_COMMIT='796879d7b3d5ca0fa1e398562e937e9f364a5f62'
B_COMMIT='4e709ed0cc6ec4e2b2a60d7d914765ae170634a0'
SHA=lambda b:hashlib.sha256(b).hexdigest()
NORM=lambda s:re.sub(r'\s+',' ',s or '').strip()

class InvariantParser(html.parser.HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True);self.in_head=False;self.skip=[];self.title_parts=[];self.title_depth=0;self.meta=[];self.canonical=[];self.anchors=[];self.anchor=None;self.headings=[];self.heading=None;self.images=[];self.image_sources=[];self.json_scripts=[];self.json_script=None;self.body_text=[]
 def handle_starttag(self,tag,attrs):
  attrs={k:(v if v is not None else '') for k,v in attrs}
  if tag=='head':self.in_head=True
  if tag=='meta':self.meta.append(sorted(attrs.items()))
  if tag=='link' and 'canonical' in (attrs.get('rel','').lower().split()):self.canonical.append(sorted(attrs.items()))
  if tag=='title':self.title_depth+=1
  if re.fullmatch(r'h[1-6]',tag):self.heading={'level':tag,'id':attrs.get('id',''),'aria_label':attrs.get('aria-label',''),'parts':[]}
  if tag=='a':self.anchor={'attrs':sorted((k,v) for k,v in attrs.items() if k not in {'class','style'}),'parts':[]}
  if tag=='img':self.images.append(sorted(attrs.items()))
  if tag=='source' and any(k in attrs for k in ('src','srcset','sizes','type','media')):self.image_sources.append(sorted(attrs.items()))
  if tag=='script':
   script_type=attrs.get('type','').lower().split(';',1)[0].strip()
   self.skip.append('script')
   if script_type=='application/ld+json':self.json_script=[]
  elif tag=='style':self.skip.append('style')
 def handle_endtag(self,tag):
  if tag=='head':self.in_head=False
  if tag=='title' and self.title_depth:self.title_depth-=1
  if re.fullmatch(r'h[1-6]',tag) and self.heading is not None:
   self.headings.append({'level':self.heading['level'],'id':self.heading['id'],'aria_label':self.heading['aria_label'],'text':NORM(' '.join(self.heading['parts']))});self.heading=None
  if tag=='a' and self.anchor is not None:
   self.anchors.append({'attrs':self.anchor['attrs'],'text':NORM(' '.join(self.anchor['parts']))});self.anchor=None
  if tag=='script' and self.skip and self.skip[-1]=='script':
   self.skip.pop()
   if self.json_script is not None:
    raw=''.join(self.json_script).strip()
    try:self.json_scripts.append(json.loads(raw))
    except Exception:self.json_scripts.append({'__invalid_json_ld__':raw})
    self.json_script=None
  elif tag=='style' and self.skip and self.skip[-1]=='style':self.skip.pop()
 def handle_data(self,data):
  if self.title_depth:self.title_parts.append(data)
  if self.heading is not None:self.heading['parts'].append(data)
  if self.anchor is not None:self.anchor['parts'].append(data)
  if self.skip:
   if self.json_script is not None:self.json_script.append(data)
   return
  if not self.in_head:self.body_text.append(data)
 def result(self):
  text=NORM(' '.join(self.body_text))
  meta_sorted=sorted(self.meta)
  robots=sorted(attrs for attrs in self.meta if dict(attrs).get('name','').lower() in {'robots','googlebot','bingbot'})
  jsonld=json.loads(json.dumps(self.json_scripts,sort_keys=True,ensure_ascii=False))
  return {'text':text,'text_sha256':SHA(text.encode()),'text_chars':len(text),'title':NORM(' '.join(self.title_parts)),'headings':self.headings,'meta':meta_sorted,'robots':robots,'canonical':sorted(self.canonical),'anchors':self.anchors,'images':self.images,'picture_sources':self.image_sources,'json_ld':jsonld,'json_ld_sha256':SHA(json.dumps(jsonld,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode())}

def extract(raw:bytes):
 p=InvariantParser();p.feed(raw.decode('utf-8',errors='strict'));p.close();return p.result()

def compare(a,b):
 keys=['text','title','headings','meta','robots','canonical','anchors','images','picture_sources','json_ld']
 return {k:a[k]==b[k] for k in keys}

def main():
 if OUT.exists() or SUMMARY.exists():raise SystemExit('Refusing to overwrite a content-comparison output')
 aidx=json.loads(A_INDEX.read_text(encoding='utf-8'));a_bytes=A_ARCHIVE.read_bytes()
 if aidx.get('source_commit')!=A_COMMIT or aidx.get('route_count')!=43 or aidx.get('render_archive_sha256')!=SHA(a_bytes):raise SystemExit('Frozen A render index/archive identity check failed')
 with gzip.open(A_ARCHIVE,'rt',encoding='utf-8') as f:a_archive=json.load(f)
 if a_archive.get('source_commit')!=A_COMMIT or len(a_archive.get('routes',{}))!=43:raise SystemExit('Frozen A render archive is not the exact 43-route baseline')
 bidx=json.loads(B_INDEX.read_text(encoding='utf-8'))
 if bidx.get('source_head')!=B_COMMIT or len(bidx.get('routes',[]))!=43:raise SystemExit(f'Frozen B render identity/count failed: {bidx.get("source_head")}')
 b_rows={r['url']:r for r in bidx['routes']};a_routes=a_archive['routes']
 if set(b_rows)!=set(a_routes):raise SystemExit('A/B route inventories differ')
 rows=[];all_pass=True
 for route in sorted(a_routes):
  ar=a_routes[route];br=b_rows[route]
  if ar.get('status')!=200 or br.get('status')!=200:raise SystemExit(f'Expected HTTP 200 for all frozen renders: {route} A={ar.get("status")} B={br.get("status")}')
  araw=ar['html'].encode('utf-8');braw=(B_DIR/br['evidence']).read_bytes()
  if len(araw)!=ar['bytes'] or SHA(araw)!=ar['sha256'] or len(braw)!=br['bytes']:raise SystemExit(f'HTML byte/hash integrity failure: {route}')
  ai,bi=extract(araw),extract(braw);checks=compare(ai,bi);passed=all(checks.values());all_pass=all_pass and passed
  failed=[k for k,v in checks.items() if not v]
  rows.append({'route':route,'A_status':ar['status'],'B_status':br['status'],'A_bytes':len(araw),'B_bytes':len(braw),'A_sha256':SHA(araw),'B_sha256':SHA(braw),'html_byte_identical':araw==braw,'protected_invariants':checks,'failed_invariants':failed,'A_visible_text_chars':ai['text_chars'],'B_visible_text_chars':bi['text_chars'],'A_title':ai['title'],'B_title':bi['title'],'A_h1':[h['text'] for h in ai['headings'] if h['level']=='h1'],'B_h1':[h['text'] for h in bi['headings'] if h['level']=='h1'],'A_anchors':len(ai['anchors']),'B_anchors':len(bi['anchors']),'A_images':len(ai['images']),'B_images':len(bi['images'])})
 a_sm=A_SITEMAP.read_bytes();b_sm=B_SITEMAP.read_bytes()
 try:urls=[n.text or '' for n in ET.fromstring(b_sm).iter() if n.tag.endswith('loc')]
 except Exception as e:raise SystemExit(f'B sitemap XML invalid: {e}')
 sitemap_same=a_sm==b_sm and len(urls)==38 and len(set(urls))==38
 if not sitemap_same:all_pass=False
 result={'phase':32,'task':'43_route_rendered_content_comparison','generated_at':__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),'A_source_commit':A_COMMIT,'A_rendered_at_head':aidx.get('rendered_at_head'),'B_source_commit':B_COMMIT,'B_render_index':str(B_INDEX),'A_render_archive_sha256':SHA(a_bytes),'route_count':len(rows),'http_200_routes':sum(r['A_status']==200 and r['B_status']==200 for r in rows),'protected_invariants':['normalized rendered body text and order','title','heading levels/order/text/IDs','all meta attributes','robots directives','canonical links','anchor semantic attributes, visible text, order and multiplicity','all img attributes','picture source attributes','all JSON-LD graphs'],'route_invariant_failures':sum(bool(r['failed_invariants']) for r in rows),'html_byte_identical_routes':sum(r['html_byte_identical'] for r in rows),'sitemap':{'A_sha256':SHA(a_sm),'B_sha256':SHA(b_sm),'byte_identical':a_sm==b_sm,'B_url_count':len(urls),'B_unique_url_count':len(set(urls)),'passed':sitemap_same},'passed':all_pass,'local_only':True,'production_or_native_host_verified':False,'rows':rows}
 OUT.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 summary=['# Phase32 43-route rendered-content comparison','','## Method','',f"Frozen A HTML: source `{A_COMMIT}`, archive SHA-256 `{SHA(a_bytes)}`. Frozen B HTML: source `{B_COMMIT}` in `{B_DIR}`. Both contain the identical 43-route inventory and returned HTTP 200. The comparison is local-only; it is not native hosting or production evidence.",'','## Protected invariants','',f"Result: **{'PASS' if all_pass else 'FAIL'}**. {len(rows)} routes, {sum(r['html_byte_identical'] for r in rows)} byte-identical HTML responses. The comparison checks normalized rendered body text/order, title, headings, meta, robots, canonical, anchor semantics/text/order/multiplicity, image and picture-source attributes, and parsed JSON-LD graphs.",'', '| Route | A/B HTML bytes | A/B visible text chars | Anchors | Images | HTML bytes identical | Content invariants |','|---|---:|---:|---:|---:|---|---|']
 for r in rows:summary.append(f"| `{r['route']}` | {r['A_bytes']}/{r['B_bytes']} | {r['A_visible_text_chars']}/{r['B_visible_text_chars']} | {r['A_anchors']}/{r['B_anchors']} | {r['A_images']}/{r['B_images']} | {'yes' if r['html_byte_identical'] else 'no'} | {'PASS' if not r['failed_invariants'] else 'FAIL: '+', '.join(r['failed_invariants'])} |")
 summary+=['',f"Sitemap bytes identical: **{sitemap_same}**; B contains {len(urls)} unique URLs. Full per-route hashes/checks: `{OUT.relative_to(ROOT).as_posix()}`.",'','## Limits','','This validates only the protected rendered content in these two frozen local source snapshots. It does not assert HTML byte identity where layout/resource markup legitimately differs, measure live routes or prove native-host rewrite, ACL or cache behavior.']
 SUMMARY.write_text('\n'.join(summary)+'\n',encoding='utf-8')
 print(json.dumps({'passed':all_pass,'routes':len(rows),'http_200':result['http_200_routes'],'route_invariant_failures':result['route_invariant_failures'],'html_byte_identical':result['html_byte_identical_routes'],'sitemap':result['sitemap'],'json':str(OUT),'markdown':str(SUMMARY)},indent=2))
 if not all_pass:sys.exit(1)
if __name__=='__main__':main()
