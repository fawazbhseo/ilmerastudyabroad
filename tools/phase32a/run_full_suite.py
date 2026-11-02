#!/usr/bin/env python3
"""Run the final Phase32a verification suite once, serially, without resume."""
from __future__ import annotations
import datetime,hashlib,json,os,pathlib,subprocess,sys,time,urllib.error,urllib.request,xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=ROOT/'reports/phase-32a-full-suite-run-01.json'
EVIDENCE=pathlib.Path(os.environ.get('PHASE32A_SUITE_EVIDENCE','/home/user/phase32a-runtime/phase32a-full-suite-run01'))
RENDER_DIR=pathlib.Path(os.environ.get('PHASE32A_SUITE_RENDER_DIR','/home/user/phase32a-runtime/phase32a-current-after-fallback-full/render-before'))
BASE=os.environ.get('PHASE31_BASE_URL','http://127.0.0.1:8094')
RUNTIME=os.environ.get('PHASE32_RUNTIME','/home/user/phase32a-runtime/node_modules')
PHP_WASM=os.environ.get('PHP_WASM_CLI',str(pathlib.Path(RUNTIME)/'.bin/php-wasm-cli'))

def sha(b):return hashlib.sha256(b).hexdigest()
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()
def save(report):OUT.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def record(report,name,status,started,duration,details=None):
 row={'name':name,'status':status,'started_at':started,'duration_seconds':round(duration,2)}
 if details:row.update(details)
 report['checks'].append(row);save(report);print(f"{status} {name}",flush=True)
def run_command(report,name,cmd,env,timeout=900,expected_json=None):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.time();log=EVIDENCE/(name.lower().replace(' ','-').replace('/','-')+'.log')
 try:
  p=subprocess.run(cmd,cwd=ROOT,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=timeout)
  output=p.stdout or '';log.write_text(output,encoding='utf-8');details={'command':cmd,'exit_code':p.returncode,'log':str(log),'tail':output[-1600:]}
  status='PASS' if p.returncode==0 else 'FAIL'
  if expected_json and p.returncode==0:
   try:
    data=json.loads(pathlib.Path(expected_json).read_text(encoding='utf-8'))
    if not data.get('passed',data.get('status') in {'PASS','PASS_BASELINE_RELATIVE'}):status='FAIL';details['validation_error']='Output JSON did not report pass'
    details['output_json']=str(expected_json)
   except Exception as e:status='FAIL';details['validation_error']=str(e)
  record(report,name,status,start,time.time()-t,details);return status
 except subprocess.TimeoutExpired as e:
  output=(e.stdout or b'').decode('utf-8','replace') if isinstance(e.stdout,bytes) else (e.stdout or '')
  log.write_text(output+'\nTIMEOUT after '+str(timeout)+' seconds\n',encoding='utf-8')
  record(report,name,'FAIL',start,time.time()-t,{'command':cmd,'timeout_seconds':timeout,'log':str(log),'tail':output[-1600:]});return 'FAIL'
def check_render_inputs(report):
 name='43-route current render and content inputs';start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.time();details={};status='PASS'
 try:
  idx_path=RENDER_DIR/'routes.json';idx=json.loads(idx_path.read_text(encoding='utf-8'));routes=idx.get('routes',[]);by={x['url']:x for x in routes}
  current=git('rev-parse','HEAD');source=idx.get('source_head')
  if len(by)!=43 or any(r.get('status')!=200 for r in routes):raise ValueError('Current render index is not 43/43 HTTP 200')
  if subprocess.run(['git','merge-base','--is-ancestor',source,current],cwd=ROOT).returncode:raise ValueError('Render source not ancestor of suite HEAD')
  changed=subprocess.run(['git','diff','--quiet',source,current,'--','*.php','assets','includes','blog','destinations','places'],cwd=ROOT)
  if changed.returncode:raise ValueError('Runtime source changed after final render')
  fetched=0
  for route,row in by.items():
   with urllib.request.urlopen(BASE+route,timeout=20) as res:
    body=res.read()
    if res.status!=200 or len(body)!=row['bytes'] or sha(body)!=sha((RENDER_DIR/row['evidence']).read_bytes()):raise ValueError(f'HTTP/body mismatch {route}')
    fetched+=1
  cmp=json.loads((ROOT/'reports/phase-32a-43-route-content-comparison.json').read_text(encoding='utf-8'))
  if not cmp.get('passed') or cmp.get('route_count')!=43 or cmp.get('route_invariant_failures')!=0:raise ValueError('43-route text/link/image/JSON-LD comparison is not PASS')
  details={'render_source_head':source,'suite_head':current,'routes':len(by),'http_200':fetched,'runtime_unchanged':True,'render_index_sha256':sha(idx_path.read_bytes()),'content_comparison_report':'reports/phase-32a-43-route-content-comparison.json','protected_content_failures':0}
 except Exception as e:status='FAIL';details={'error':str(e)}
 record(report,name,status,start,time.time()-t,details);return status
def check_sitemap(report):
 name='Sitemap exactness and 38 unique URLs';start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.time();details={};status='PASS'
 try:
  old=(ROOT/'reports/phase-32-before-sitemap.xml').read_bytes();new=RENDER_DIR.parent.joinpath('sitemap.xml').read_bytes();root=ET.fromstring(new);urls=[x.text or '' for x in root.iter() if x.tag.endswith('loc')]
  if old!=new or len(urls)!=38 or len(set(urls))!=38:raise ValueError('Sitemap bytes or 38-URL inventory differs')
  details={'A_sha256':sha(old),'B_sha256':sha(new),'byte_identical':True,'url_count':len(urls),'unique_urls':len(set(urls))}
 except Exception as e:status='FAIL';details={'error':str(e)}
 record(report,name,status,start,time.time()-t,details);return status
def check_structured_data(report):
 name='All-43-route structured data parity';start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.time();details={};status='PASS'
 try:
  data=json.loads((ROOT/'reports/phase-32a-43-route-content-comparison.json').read_text(encoding='utf-8'));rows=data['rows']
  if len(rows)!=43 or not data.get('passed') or any(not row['protected_invariants'].get('json_ld') for row in rows):raise ValueError('JSON-LD parity failed or route coverage incomplete')
  details={'routes':43,'json_ld_mismatches':0,'source_report':'reports/phase-32a-43-route-content-comparison.json'}
 except Exception as e:status='FAIL';details={'error':str(e)}
 record(report,name,status,start,time.time()-t,details);return status
def run_php_lint(report,env):
 name='PHP-WASM lint all tracked PHP';start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.time();files=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().split('\0');files=sorted(x for x in files if x.endswith('.php'))
 failures=[]
 for rel in files:
  p=subprocess.run([PHP_WASM,'-l',str(ROOT/rel)],cwd=ROOT,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  if p.returncode or 'No syntax errors detected' not in p.stdout:failures.append({'file':rel,'output':p.stdout[-500:]})
 (EVIDENCE/'php-lint.json').write_text(json.dumps({'file_count':len(files),'failures':failures},indent=2)+'\n',encoding='utf-8')
 status='PASS' if not failures else 'FAIL';record(report,name,status,start,time.time()-t,{'php_files':len(files),'failures':failures[:20],'full_results':str(EVIDENCE/'php-lint.json'),'runtime':'PHP 8.5.8 WASM CLI via @php-wasm/cli 3.1.50'});return status

def main():
 if OUT.exists():raise SystemExit(f'Refusing to repeat or resume the one full suite: {OUT} already exists')
 EVIDENCE.mkdir(parents=True,exist_ok=False)
 started=datetime.datetime.now(datetime.timezone.utc).isoformat();start=time.time();head=git('rev-parse','HEAD')
 report={'phase':'32a','task':'one_final_full_verification_suite','status':'RUNNING','started_at':started,'suite_head':head,'local_only':True,'live_or_production_claim':False,'no_resume_or_second_run':True,'evidence_directory_external':str(EVIDENCE),'requested_cases':{'normal_browser_matrix':258,'reduced_motion_representatives':48,'normal_scroll_widths':[360,768,1280],'axe_templates':['destination','place','article','blog-index','legal','utility']},'checks':[]}
 save(report)
 env=dict(os.environ,NODE_PATH='/home/user/phase32a-runtime/node_modules',PHASE32_RUNTIME=RUNTIME,PHASE31_RUNTIME=RUNTIME,PHASE31_EVIDENCE='/home/user/phase32a-runtime/phase32a-current-after-fallback-full',PHASE31_RENDER_DIR=str(RENDER_DIR),PHASE31_BASE_URL=BASE,PHASE32A_SUITE_EVIDENCE=str(EVIDENCE),PHASE32A_SUITE_RENDER_DIR=str(RENDER_DIR),PHASE32A_PALETTE_OUT=str(EVIDENCE/'palette.json'),PHASE32A_AXE_OUT=str(EVIDENCE/'axe.json'))
 try:
  check_render_inputs(report);run_php_lint(report,env)
  run_command(report,'Static discovery tests',[sys.executable,'tools/test_discovery.py'],env)
  run_command(report,'Strict wording tests',[sys.executable,'tools/test_wording.py'],env)
  run_command(report,'Citations tests',[sys.executable,'tools/test_citations.py'],env)
  run_command(report,'Italy claims tests',[sys.executable,'tools/test_italy_claims.py'],env)
  run_command(report,'LLM directory tests',[sys.executable,'tools/test_llm_directory.py'],env)
  run_command(report,'LLM policy tests',[sys.executable,'tools/test_llm_policy.py'],env)
  run_command(report,'Content presence tests',[sys.executable,'tools/test_presence.py'],env)
  run_command(report,'Duplicate answer tests',[sys.executable,'tools/test_duplicate_answers.py'],env)
  run_command(report,'Team biography policy tests',[sys.executable,'tools/test_team_bio_policy.py'],env)
  run_command(report,'Public exposure tests',[sys.executable,'tools/test_public_exposure.py'],env)
  run_command(report,'Rendered discovery routes',[sys.executable,'tools/check_discovery.py','--base-url',BASE],env,timeout=900)
  run_command(report,'Rendered publication wording review',[sys.executable,'tools/check_publication_review.py','--base-url',BASE],env,timeout=900)
  run_command(report,'Rendered Italy claim policy',[sys.executable,'tools/check_italy_claims.py','--base-url',BASE],env,timeout=900)
  run_command(report,'Rendered Phase19 policy',[sys.executable,'tools/check_phase19.py','--base-url',BASE],env,timeout=900)
  run_command(report,'Technical SEO and sitemap routes',[sys.executable,'tools/check_technical_seo.py','--base-url',BASE],env,timeout=900)
  run_command(report,'Phase20 content inventory',[sys.executable,'tools/check_phase20.py','--base-url',BASE],env,timeout=900)
  check_sitemap(report);check_structured_data(report)
  run_command(report,'Final palette and fallback scope',['node','tools/phase32a/palette_check.cjs'],env,timeout=900,expected_json=EVIDENCE/'palette.json')
  run_command(report,'258-case browser matrix and no-overflow',['node','tools/phase31/browser-suite.cjs','--out',str(EVIDENCE/'browser-matrix.json'),'--require-visible'],env,timeout=10800)
  browser_status=report['checks'][-1]['status']
  if browser_status=='PASS':
   try:
    browser=json.loads((EVIDENCE/'browser-matrix.json').read_text())
    if browser.get('normal_cases')!=258 or browser.get('total_cases')!=306 or any(c['scroll_width']>c['width']+1 for c in browser['cases']):raise ValueError('Browser matrix count/overflow validation failed')
    report['checks'][-1]['normal_cases']=browser['normal_cases'];report['checks'][-1]['reduced_motion_cases']=browser['reduced_motion_cases'];report['checks'][-1]['total_cases']=browser['total_cases'];report['checks'][-1]['horizontal_overflow_cases']=sum(c['scroll_width']>c['width']+1 for c in browser['cases']);save(report)
   except Exception as e:
    report['checks'][-1]['status']='FAIL';report['checks'][-1]['validation_error']=str(e);save(report)
  run_command(report,'Axe representative pages, one per template',['node','tools/phase32a/axe_template_check.cjs'],env,timeout=1800,expected_json=EVIDENCE/'axe.json')
  run_command(report,'Git whitespace',['git','-c','core.whitespace=cr-at-eol','diff','--check'],env)
 except Exception as e:
  report['runner_error']=str(e);save(report)
 report['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat();report['suite_seconds']=round(time.time()-start,2);report['completed_checks']=len(report['checks']);report['failed_checks']=[c['name'] for c in report['checks'] if c['status']!='PASS'];report['status']='PASS' if not report['runner_error'] and not report['failed_checks'] and len(report['checks'])==24 else 'FAIL';report['complete_no_skip_or_resume']=True;save(report)
 print(f"PHASE32A FINAL SUITE {report['status']}: {report['completed_checks']} checks, failed={len(report['failed_checks'])}, {report['suite_seconds']}s",flush=True)
 if report['failed_checks'] or report.get('runner_error'):sys.exit(1)
if __name__=='__main__':main()
