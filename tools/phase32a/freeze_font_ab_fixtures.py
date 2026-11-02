#!/usr/bin/env python3
"""Freeze a current-font versus swap/no-visibility-gate candidate for two routes."""
from __future__ import annotations
import hashlib,importlib.util,json,os,pathlib,subprocess,sys
ROOT=pathlib.Path(__file__).resolve().parents[2]
EVIDENCE=pathlib.Path(os.environ.get('PHASE32A_FONT_EVIDENCE','/home/user/phase32a-runtime/phase32a-font-ab-run01'))
RENDER_DIR=pathlib.Path(os.environ.get('PHASE32A_FALLBACK_RENDER_DIR','/home/user/phase32a-runtime/phase32a-after-fallback'))
FIXTURE=EVIDENCE/'fixtures.json';SELECTED=EVIDENCE/'selected.json'
OUT_JSON=ROOT/'reports/phase-32a-font-ab-run-01-fixtures.json'
OUT_MD=ROOT/'reports/phase-32a-font-ab-run-01-fixtures.md'
ROUTES=['/study-abroad-counselling-mysuru','/blog/how-to-choose-study-abroad-consultant-karnataka']
FILENAMES={'/study-abroad-counselling-mysuru':'mysuru.html','/blog/how-to-choose-study-abroad-consultant-karnataka':'article.html'}
GATE='.p25-font-pending body.p25{visibility:hidden;}'
SHA=lambda b:hashlib.sha256(b).hexdigest()
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()
def transform(html:str,route:str):
 start=html.find('<style id="ilmera-visual-system">')
 if start<0:raise SystemExit(f'Missing inline visual-system stylesheet: {route}')
 end=html.find('</style>',start)
 if end<0:raise SystemExit(f'Unclosed inline visual-system stylesheet: {route}')
 end+=len('</style>');block=html[start:end];count=block.count('font-display:block');gate_count=block.count(GATE)
 if count!=7 or gate_count!=1:raise SystemExit(f'Unexpected candidate source shape for {route}: block_faces={count}, visibility_gate={gate_count}')
 changed=block.replace('font-display:block','font-display:swap')
 if changed.count('font-display:swap')!=7:raise SystemExit(f'Candidate did not change exactly seven font-display declarations: {route}')
 changed=changed.replace(GATE,'')
 return html[:start]+changed+html[end:],count,gate_count

def main():
 for p in [FIXTURE,SELECTED,OUT_JSON,OUT_MD]:
  if p.exists():raise SystemExit(f'Refusing to overwrite existing font fixture output: {p}')
 source_commit=git('log','-1','--format=%H','--','includes/visual-config.php')
 current_head=git('rev-parse','HEAD')
 changed=subprocess.run(['git','diff','--quiet',source_commit,current_head,'--','*.php','assets','includes','blog','destinations','places'],cwd=ROOT)
 if changed.returncode!=0:raise SystemExit('Site runtime changed after the fallback render; refresh before freezing font fixtures')
 fixture={};rows=[]
 spec=importlib.util.spec_from_file_location('phase32a_compare',ROOT/'tools/phase32/compare_43_route_content.py')
 cmp=importlib.util.module_from_spec(spec);sys.modules[spec.name]=cmp;spec.loader.exec_module(cmp)
 for route in ROUTES:
  src=RENDER_DIR/FILENAMES[route]
  if not src.is_file():raise SystemExit(f'Missing post-fallback PHP-WASM render: {src}')
  a_bytes=src.read_bytes();a=a_bytes.decode('utf-8',errors='strict');b,face_count,gate_count=transform(a,route);checks=cmp.compare(cmp.extract(a_bytes),cmp.extract(b.encode('utf-8')))
  if not all(checks.values()):raise SystemExit(f'Font candidate changes protected content on {route}: {[k for k,v in checks.items() if not v]}')
  fixture[route]={'A':a,'B':b}
  rows.append({'route':route,'A_html_bytes':len(a_bytes),'B_html_bytes':len(b.encode('utf-8')),'A_html_sha256':SHA(a_bytes),'B_candidate_html_sha256':SHA(b.encode('utf-8')),'font_display_declarations_changed':face_count,'body_visibility_gate_rules_removed':gate_count,'preload_links_unchanged':True,'font_files_weights_families_unchanged':True,'protected_content_checks':checks})
 fixture_bytes=(json.dumps(fixture,ensure_ascii=False,separators=(',',':'))+'\n').encode('utf-8')
 EVIDENCE.mkdir(parents=True,exist_ok=True);FIXTURE.write_bytes(fixture_bytes);SELECTED.write_text(json.dumps({'route':ROUTES[0],'variant':'A'},separators=(',',':'))+'\n',encoding='utf-8')
 meta={'phase':'32a','task':'fresh_font_candidate_ab_fixture','status':'PASS','A_policy':'Current post-fallback font policy: seven local faces font-display:block, two preloads, body visibility gate','A_source_commit':source_commit,'fixture_freeze_head':current_head,'runtime_unchanged_since_render':True,'B_policy':'Candidate only: seven webfont declarations changed to font-display:swap and the single .p25-font-pending body visibility rule removed. Font families, file URLs, weights, preloads, text, images, scripts and markup otherwise preserved.','routes':rows,'route_count':len(ROUTES),'sample_plan':'Seven A and seven B Lighthouse samples per route, alternating pair order; fresh Chromium per sample, serial, no retries.','fixture_json_path_external':str(FIXTURE),'fixture_json_bytes':len(fixture_bytes),'fixture_json_sha256':SHA(fixture_bytes),'content_invariant_failures':0,'local_only':True,'live_or_field_verified':False,'analysis_performed':False}
 OUT_JSON.write_text(json.dumps(meta,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 md=['# Phase32a fresh font candidate fixture','',f"Status: **PASS**. Current font-policy source `{source_commit}`; fixture-freeze HEAD `{current_head}`. The runtime tree did not change after the post-fallback render.",'',f"Fixture SHA-256 `{SHA(fixture_bytes)}` ({len(fixture_bytes)} bytes), stored externally at `{FIXTURE}`.",'','| Route | A/B bytes | Display declarations changed | Visibility gate removed | Preloads/families/weights unchanged | Protected content |','|---|---:|---:|---:|---|---|']
 for row in rows:md.append(f"| `{row['route']}` | {row['A_html_bytes']}/{row['B_html_bytes']} | {row['font_display_declarations_changed']} | {row['body_visibility_gate_rules_removed']} | yes | PASS |")
 md+=['','A is the current post-fallback page. B is a candidate-only HTML transform; no font source, preload or production setting has changed. It swaps `font-display` and removes the body-visibility gate. All protected content comparisons pass.','',meta['sample_plan'],'','This is a local fixture only. No browser measurement or metric analysis has run yet.']
 OUT_MD.write_text('\n'.join(md)+'\n',encoding='utf-8')
 print(json.dumps({'status':'PASS','fixture_sha256':SHA(fixture_bytes),'fixture_bytes':len(fixture_bytes),'source_commit':source_commit,'routes':len(rows),'manifest':str(OUT_JSON),'summary':str(OUT_MD),'fixture_external':str(FIXTURE)},indent=2))
if __name__=='__main__':main()
