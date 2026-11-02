#!/usr/bin/env python3
"""Freeze Phase32a's six-route A/B HTML and verify protected content before the lab."""
from __future__ import annotations
import hashlib,importlib.util,json,os,pathlib,subprocess,sys,tarfile
ROOT=pathlib.Path(__file__).resolve().parents[2]
TAR=ROOT/'reports/phase-31-task4-ab-fixtures.tar.gz'
A_MANIFEST=ROOT/'reports/phase-31-task4-ab-fixtures.json'
B_DIR=pathlib.Path(os.environ.get('PHASE32A_B_RENDER_DIR','/home/user/phase32a-runtime/phase32a-current-b/render-before'))
EVIDENCE=pathlib.Path(os.environ.get('PHASE32A_AB_EVIDENCE','/home/user/phase32a-runtime/phase32a-ab-run01'))
OUT_FIXTURE=EVIDENCE/'fixtures.json'
OUT_SELECTED=EVIDENCE/'selected.json'
OUT_MANIFEST=ROOT/'reports/phase-32a-six-route-fixtures.json'
OUT_MD=ROOT/'reports/phase-32a-six-route-fixtures.md'
A_SOURCE='7d1bb9ec0522bcbc7953262920fafb50bf04ab72'
ROUTES=['/study-in-germany','/study-abroad-counselling-mysuru','/blog/how-to-choose-study-abroad-consultant-karnataka','/blog/','/services','/contact']
CONTROLS={'/services','/contact'}
SHA=lambda data:hashlib.sha256(data).hexdigest()

def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()
def digest_html(value:str):return SHA(value.encode('utf-8'))

def main():
 for p in [OUT_FIXTURE,OUT_SELECTED,OUT_MANIFEST,OUT_MD]:
  if p.exists():raise SystemExit(f'Refusing to overwrite existing frozen fixture output: {p}')
 if not TAR.is_file() or not A_MANIFEST.is_file():raise SystemExit('Required frozen Task4 A fixture archive or manifest is missing')
 a_manifest=json.loads(A_MANIFEST.read_text(encoding='utf-8'))
 if a_manifest.get('A_source_commit')!=A_SOURCE:raise SystemExit('Task4 fixture manifest is not frozen at A=7d1bb9e')
 if a_manifest.get('fixture_json_sha256')!=SHA(tarfile.open(TAR,'r:gz').extractfile('fixtures.json').read()):raise SystemExit('Task4 fixture tar payload does not match its committed hash')
 with tarfile.open(TAR,'r:gz') as archive:a_fixtures=json.loads(archive.extractfile('fixtures.json').read().decode('utf-8'))
 a_rows={row['route']:row for row in a_manifest['routes']}
 b_index_path=B_DIR/'routes.json'
 if not b_index_path.is_file():raise SystemExit(f'Missing current-B render index: {b_index_path}')
 b_index_bytes=b_index_path.read_bytes();b_index=json.loads(b_index_bytes)
 b_rendered_head=b_index.get('source_head')
 if len(b_index.get('routes',[]))!=43:raise SystemExit('Current B capture must contain all 43 frozen routes')
 current_head=git('rev-parse','HEAD')
 if subprocess.run(['git','merge-base','--is-ancestor',b_rendered_head,current_head],cwd=ROOT).returncode!=0:raise SystemExit(f'B render source {b_rendered_head} is not an ancestor of current HEAD {current_head}')
 runtime_diff=subprocess.run(['git','diff','--quiet',b_rendered_head,current_head,'--','*.php','assets','includes','blog','destinations','places'],cwd=ROOT)
 if runtime_diff.returncode!=0:raise SystemExit('Runtime source changed after B render capture; rerender before freezing')
 b_rows={row['url']:row for row in b_index['routes']}
 if set(ROUTES)-set(a_fixtures) or set(ROUTES)-set(b_rows):raise SystemExit('Missing a requested route in A or B captures')
 spec=importlib.util.spec_from_file_location('phase32_compare',ROOT/'tools/phase32/compare_43_route_content.py')
 comparator=importlib.util.module_from_spec(spec);sys.modules[spec.name]=comparator;spec.loader.exec_module(comparator)
 fixtures={};rows=[]
 for route in ROUTES:
  a_html=a_fixtures[route].get('A');b_row=b_rows[route];a_row=a_rows[route]
  if not isinstance(a_html,str) or b_row.get('status')!=200 or a_row.get('http_status_A')!=200:raise SystemExit(f'Expected valid A/B HTTP 200 fixture for {route}')
  a_bytes=a_html.encode('utf-8');b_file=B_DIR/b_row['evidence'];b_bytes=b_file.read_bytes();b_html=b_bytes.decode('utf-8',errors='strict')
  if len(a_bytes)!=a_row['A_html_bytes'] or SHA(a_bytes)!=a_row['A_html_sha256']:raise SystemExit(f'A Task4 HTML integrity mismatch for {route}')
  if len(b_bytes)!=b_row['bytes']:raise SystemExit(f'B rendered HTML size mismatch for {route}')
  ai,bi=comparator.extract(a_bytes),comparator.extract(b_bytes);checks=comparator.compare(ai,bi)
  if not all(checks.values()):raise SystemExit(f'Protected content changed on {route}: {[key for key,value in checks.items() if not value]}')
  fixtures[route]={'A':a_html,'B':b_html}
  rows.append({'route':route,'role':'reference control, existing pushed B differs' if route in CONTROLS else 'still target','A_http_status':a_row['http_status_A'],'B_http_status':b_row['status'],'A_html_bytes':len(a_bytes),'B_html_bytes':len(b_bytes),'A_html_sha256':SHA(a_bytes),'B_html_sha256':SHA(b_bytes),'html_byte_identical':a_bytes==b_bytes,'protected_content_checks':checks,'A_visible_text_chars':ai['text_chars'],'B_visible_text_chars':bi['text_chars'],'A_anchor_count':len(ai['anchors']),'B_anchor_count':len(bi['anchors']),'A_image_count':len(ai['images']),'B_image_count':len(bi['images'])})
 fixture_bytes=(json.dumps(fixtures,ensure_ascii=False,separators=(',',':'))+'\n').encode('utf-8')
 b_source_paths=subprocess.check_output(['git','diff','--name-only',A_SOURCE,b_rendered_head,'--','*.php','assets','includes','blog','destinations','places'],cwd=ROOT,text=True).splitlines()
 evidence={'phase':'32a','task':'six_route_frozen_ab_fixture','freeze_status':'PASS','A_source_commit':A_SOURCE,'A_fixture_source':'reports/phase-31-task4-ab-fixtures.tar.gz','A_fixture_archive_sha256':SHA(TAR.read_bytes()),'A_fixture_json_sha256':a_manifest['fixture_json_sha256'],'B_rendered_source_head':b_rendered_head,'B_current_head_at_freeze':current_head,'B_runtime_equal_current_head':True,'B_runtime_files_changed_after_capture':b_source_paths,'B_render_index_path_external':str(b_index_path),'B_render_index_sha256':SHA(b_index_bytes),'fixture_path_external':str(OUT_FIXTURE),'fixture_json_sha256':SHA(fixture_bytes),'fixture_json_bytes':len(fixture_bytes),'route_count':len(ROUTES),'routes':rows,'protected_content_invariant_set':list(rows[0]['protected_content_checks']),'content_invariant_failures':0,'byte_identical_routes':sum(row['html_byte_identical'] for row in rows),'reference_control_note':'Services and Contact HTML are compared to the Task4 A snapshot, but B includes already-pushed shared Phase32 presentation changes. They are measurement controls, not byte-identical no-op controls. Phase32a makes no new reference-page change.','local_only':True,'live_or_native_host_verified':False}
 OUT_FIXTURE.parent.mkdir(parents=True,exist_ok=True);OUT_FIXTURE.write_bytes(fixture_bytes);OUT_SELECTED.write_text(json.dumps({'route':ROUTES[0],'variant':'A'},separators=(',',':'))+'\n',encoding='utf-8')
 OUT_MANIFEST.write_text(json.dumps(evidence,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 md=['# Phase32a six-route frozen fixture','',f"Status: **PASS**. A source `{A_SOURCE}`; B render source `{b_rendered_head}`; B runtime tree matches current HEAD `{current_head}`. Fixture SHA-256 `{SHA(fixture_bytes)}` ({len(fixture_bytes)} bytes), stored externally at `{OUT_FIXTURE}`.",'','| Route | Role | A/B HTML bytes | A/B text chars | Anchors | Images | Protected content | HTML bytes identical |','|---|---|---:|---:|---:|---:|---|---|']
 for row in rows:md.append(f"| `{row['route']}` | {row['role']} | {row['A_html_bytes']}/{row['B_html_bytes']} | {row['A_visible_text_chars']}/{row['B_visible_text_chars']} | {row['A_anchor_count']}/{row['B_anchor_count']} | {row['A_image_count']}/{row['B_image_count']} | PASS | {'yes' if row['html_byte_identical'] else 'no'} |")
 md+=['','Content check covers normalized body text/order, title, headings, meta, robots, canonical, semantic anchor attributes/text/order, image and picture-source attributes, and parsed JSON-LD. All six pass with no content invariant failures.','',evidence['reference_control_note'],'','This fixture is local-only. The Task2 A/B measurement has not started; no sample is included in this file.']
 OUT_MD.write_text('\n'.join(md)+'\n',encoding='utf-8')
 print(json.dumps({'status':'PASS','routes':len(rows),'fixture_sha256':SHA(fixture_bytes),'fixture_bytes':len(fixture_bytes),'B_rendered_source':b_rendered_head,'B_current_head':current_head,'content_invariant_failures':0,'byte_identical_routes':evidence['byte_identical_routes'],'manifest':str(OUT_MANIFEST),'summary':str(OUT_MD),'fixture_external':str(OUT_FIXTURE)},indent=2))
if __name__=='__main__':main()
