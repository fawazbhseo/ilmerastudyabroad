#!/usr/bin/env python3
"""Compare current Phase32a rendered protected content against the frozen pre-phase A render."""
from __future__ import annotations
import gzip,hashlib,importlib.util,json,os,pathlib,subprocess,sys,xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).resolve().parents[2]
A_INDEX=ROOT/'reports/phase-32-before-render-index.json'
A_ARCHIVE=ROOT/'reports/phase-32-before-renders.json.gz'
A_SITEMAP=ROOT/'reports/phase-32-before-sitemap.xml'
B_DIR=pathlib.Path(os.environ.get('PHASE32A_B_RENDER_DIR','/home/user/phase32a-runtime/phase32a-final-render/render-before'))
B_INDEX=B_DIR/'routes.json';B_SITEMAP=B_DIR.parent/'sitemap.xml'
OUT=ROOT/'reports/phase-32a-43-route-content-comparison.json'
SUMMARY=ROOT/'reports/phase-32a-43-route-content-comparison.md'
A_COMMIT='796879d7b3d5ca0fa1e398562e937e9f364a5f62'
EXPECTED_ARCHIVE_SHA='2b20187771f9117a16099754e4f579f6eb3f6f752b8c11a8ec25d255785b9dee'
SHA=lambda b:hashlib.sha256(b).hexdigest()

def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()
def main():
 if OUT.exists() or SUMMARY.exists():raise SystemExit('Refusing to overwrite Phase32a 43-route comparison output')
 for p in [A_INDEX,A_ARCHIVE,A_SITEMAP,B_INDEX,B_SITEMAP]:
  if not p.is_file():raise SystemExit(f'Missing frozen or current render input: {p}')
 aidx=json.loads(A_INDEX.read_text(encoding='utf-8'));archive_bytes=A_ARCHIVE.read_bytes()
 if aidx.get('source_commit')!=A_COMMIT or aidx.get('route_count')!=43 or aidx.get('render_archive_sha256')!=SHA(archive_bytes) or SHA(archive_bytes)!=EXPECTED_ARCHIVE_SHA:raise SystemExit('Pre-phase A render index/archive identity check failed')
 with gzip.open(A_ARCHIVE,'rt',encoding='utf-8') as f:a_archive=json.load(f)
 if a_archive.get('source_commit')!=A_COMMIT or len(a_archive.get('routes',{}))!=43:raise SystemExit('Pre-phase A render archive is not the exact 43-route baseline')
 b_index_bytes=B_INDEX.read_bytes();bidx=json.loads(b_index_bytes);b_commit=bidx.get('source_head')
 if len(bidx.get('routes',[]))!=43:raise SystemExit(f'Current B inventory has {len(bidx.get("routes",[]))} routes, expected 43')
 current_head=git('rev-parse','HEAD')
 if subprocess.run(['git','merge-base','--is-ancestor',b_commit,current_head],cwd=ROOT).returncode!=0:raise SystemExit('Current render source is not an ancestor of current HEAD')
 runtime_diff=subprocess.run(['git','diff','--quiet',b_commit,current_head,'--','*.php','assets','includes','blog','destinations','places'],cwd=ROOT)
 if runtime_diff.returncode!=0:raise SystemExit('Runtime source changed after the current B renders; rerender')
 config=subprocess.check_output(['git','show',f'{b_commit}:includes/visual-config.php'],cwd=ROOT,text=True)
 if "define('ILMERA_SCENES_ENABLED', true)" not in config or "['place','article']" not in config:raise SystemExit('Current B source does not contain the measured palette fallback and global scene switch')
 b_rows={r['url']:r for r in bidx['routes']};a_routes=a_archive['routes']
 if set(b_rows)!=set(a_routes):raise SystemExit('Pre-phase and current B route inventories differ')
 spec=importlib.util.spec_from_file_location('phase32a_invariant_comparator',ROOT/'tools/phase32/compare_43_route_content.py')
 mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
 rows=[];all_pass=True
 for route in sorted(a_routes):
  ar=a_routes[route];br=b_rows[route]
  if ar.get('status')!=200 or br.get('status')!=200:raise SystemExit(f'Expected HTTP 200 for all frozen renders: {route} A={ar.get("status")} B={br.get("status")}')
  araw=ar['html'].encode('utf-8');braw=(B_DIR/br['evidence']).read_bytes()
  if len(araw)!=ar['bytes'] or SHA(araw)!=ar['sha256'] or len(braw)!=br['bytes']:raise SystemExit(f'HTML byte/hash integrity failure: {route}')
  ai,bi=mod.extract(araw),mod.extract(braw);checks=mod.compare(ai,bi);passed=all(checks.values());all_pass=all_pass and passed
  failed=[k for k,v in checks.items() if not v]
  rows.append({'route':route,'A_status':ar['status'],'B_status':br['status'],'A_bytes':len(araw),'B_bytes':len(braw),'A_sha256':SHA(araw),'B_sha256':SHA(braw),'html_byte_identical':araw==braw,'protected_invariants':checks,'failed_invariants':failed,'A_visible_text_chars':ai['text_chars'],'B_visible_text_chars':bi['text_chars'],'A_title':ai['title'],'B_title':bi['title'],'A_h1':[h['text'] for h in ai['headings'] if h['level']=='h1'],'B_h1':[h['text'] for h in bi['headings'] if h['level']=='h1'],'A_anchors':len(ai['anchors']),'B_anchors':len(bi['anchors']),'A_images':len(ai['images']),'B_images':len(bi['images'])})
 a_sm=A_SITEMAP.read_bytes();b_sm=B_SITEMAP.read_bytes()
 try:urls=[n.text or '' for n in ET.fromstring(b_sm).iter() if n.tag.endswith('loc')]
 except Exception as e:raise SystemExit(f'Current B sitemap XML invalid: {e}')
 sitemap_same=a_sm==b_sm and len(urls)==38 and len(set(urls))==38
 if not sitemap_same:all_pass=False
 result={'phase':'32a','task':'43_route_rendered_content_comparison','generated_at':__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),'A_source_commit':A_COMMIT,'A_rendered_at_head':aidx.get('rendered_at_head'),'A_render_archive_sha256':SHA(archive_bytes),'B_rendered_source_head':b_commit,'B_current_head_at_compare':current_head,'B_runtime_unchanged_since_render':True,'B_render_index_sha256':SHA(b_index_bytes),'route_count':len(rows),'http_200_routes':sum(r['A_status']==200 and r['B_status']==200 for r in rows),'protected_invariants':['normalized rendered body text and order','title','heading levels/order/text/IDs','all meta attributes','robots directives','canonical links','anchor semantic attributes, visible text, order and multiplicity','all img attributes','picture source attributes','all JSON-LD graphs'],'route_invariant_failures':sum(bool(r['failed_invariants']) for r in rows),'html_byte_identical_routes':sum(r['html_byte_identical'] for r in rows),'sitemap':{'A_sha256':SHA(a_sm),'B_sha256':SHA(b_sm),'byte_identical':a_sm==b_sm,'B_url_count':len(urls),'B_unique_url_count':len(set(urls)),'passed':sitemap_same},'palette_fallback':{'place':True,'article':True,'ILMERA_SCENES_ENABLED':True},'passed':all_pass,'local_only':True,'production_or_native_host_verified':False,'rows':rows}
 OUT.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 summary=['# Phase32a 43-route rendered-content comparison','','## Method','',f"Frozen A HTML is from pre-phase source `{A_COMMIT}`, archive SHA-256 `{SHA(archive_bytes)}`. Current B source snapshot is `{b_commit}`; it contains the `place`/`article` palette fallback while retaining `ILMERA_SCENES_ENABLED=true`. The comparison is local-only, not native-host or production evidence.",'','## Protected invariants','',f"Result: **{'PASS' if all_pass else 'FAIL'}**. {len(rows)} routes, {sum(r['A_status']==200 and r['B_status']==200 for r in rows)} A/B HTTP 200 responses, {sum(r['html_byte_identical'] for r in rows)} byte-identical HTML responses. Checks cover normalized rendered body text/order, title, headings, meta, robots, canonical, anchor semantics/text/order/multiplicity, image and picture-source attributes, and parsed JSON-LD graphs.",'','| Route | A/B HTML bytes | A/B visible text chars | Anchors | Images | HTML bytes identical | Content invariants |','|---|---:|---:|---:|---:|---|---|']
 for r in rows:summary.append(f"| `{r['route']}` | {r['A_bytes']}/{r['B_bytes']} | {r['A_visible_text_chars']}/{r['B_visible_text_chars']} | {r['A_anchors']}/{r['B_anchors']} | {r['A_images']}/{r['B_images']} | {'yes' if r['html_byte_identical'] else 'no'} | {'PASS' if not r['failed_invariants'] else 'FAIL: '+', '.join(r['failed_invariants'])} |")
 summary+=['',f"Sitemap byte identity: **{sitemap_same}**; current B contains {len(urls)} unique URLs. Full per-route hashes/checks are in `{OUT.relative_to(ROOT).as_posix()}`.",'','## Limits','','This validates protected rendered content for the two frozen local source snapshots. It does not require HTML byte identity when visual/resource markup differs. It does not measure live routes or prove native-host rewrite, access-control or cache behavior.']
 SUMMARY.write_text('\n'.join(summary)+'\n',encoding='utf-8')
 print(json.dumps({'passed':all_pass,'routes':len(rows),'http_200':result['http_200_routes'],'route_invariant_failures':result['route_invariant_failures'],'html_byte_identical':result['html_byte_identical_routes'],'sitemap':result['sitemap'],'json':str(OUT),'markdown':str(SUMMARY)},indent=2))
 if not all_pass:sys.exit(1)
if __name__=='__main__':main()
