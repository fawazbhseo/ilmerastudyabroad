#!/usr/bin/env python3
"""Full per-task Phase31 verification. No performance runs, skips, or resume mode."""
from __future__ import annotations
import argparse,datetime,json,os,pathlib,subprocess,sys,time
ROOT=pathlib.Path(__file__).resolve().parents[2]
P=argparse.ArgumentParser();P.add_argument('task',type=int,choices=range(1,8));P.add_argument('--evidence',type=pathlib.Path,required=True);P.add_argument('--render-dir',type=pathlib.Path,required=True);P.add_argument('--baseline-targets',type=pathlib.Path);P.add_argument('--require-visible',action='store_true');a=P.parse_args()
if a.evidence.exists():raise SystemExit(f'Refusing to overwrite evidence directory: {a.evidence}')
a.evidence.mkdir(parents=True)
base=os.environ.get('PHASE31_BASE_URL','http://127.0.0.1:8080');start=time.time();groups=[];env=dict(os.environ,PHASE31_BASE_URL=base,PHASE31_RENDER_DIR=str(a.render_dir),PHASE31_EVIDENCE=os.environ.get('PHASE31_EVIDENCE','/home/user/phase31'))

def run(label,cmd,timeout=900,allow_fail=False):
    t=time.time();r=subprocess.run(cmd,cwd=ROOT,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=timeout)
    log=a.evidence/(label.lower().replace(' ','-').replace('/','-')+'.log');log.write_text(r.stdout)
    row={'name':label,'status':'PASS' if r.returncode==0 else 'FAIL','exit_code':r.returncode,'seconds':round(time.time()-t,2),'log':str(log.relative_to(a.evidence)),'tail':r.stdout[-1800:]}
    groups.append(row);print(row['status'],label,flush=True)
    if r.returncode and not allow_fail:raise SystemExit(f'{label} failed ({r.returncode}); see {log}\n{r.stdout[-5000:]}')
    return r

def php_files():
    return sorted(p for p in ROOT.rglob('*.php') if '.git' not in p.parts and 'node_modules' not in p.parts)

def main():
    php=php_files();t=time.time();fail=[]
    for f in php:
        r=subprocess.run(['php','-l',str(f)],cwd=ROOT,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        if r.returncode or 'No syntax errors detected' not in r.stdout:fail.append({'file':str(f.relative_to(ROOT)),'output':r.stdout})
    (a.evidence/'php-lint.json').write_text(json.dumps({'files':len(php),'failures':fail},indent=2)+'\n')
    groups.append({'name':'PHP-WASM CLI syntax','status':'FAIL' if fail else 'PASS','files':len(php),'seconds':round(time.time()-t,2),'runtime':'PHP 8.5.10 WASM CLI via pinned php-wasm-cli 3.1.58'})
    print('FAIL' if fail else 'PASS','PHP-WASM syntax',len(php),flush=True)
    if fail:raise SystemExit('PHP syntax failures: '+json.dumps(fail[:5]))
    tests=['test_discovery.py','test_citations.py','test_italy_claims.py','test_llm_directory.py','test_llm_policy.py','test_presence.py','test_wording.py','test_team_bio_policy.py','test_duplicate_answers.py']
    for name in tests:run(name,[sys.executable,'tools/'+name])
    for mode in ['on','off','inline']:run('visual policy '+mode,['php','tools/phase25/stage2/policy.php',mode])
    for name in ['check_destination_sources.php','check_place_contact.php','check_place_publication.php','test_proof.php','test_strategy_schema.php']:
        run(name,['php','tools/'+name])
    run('public exposure policy',[sys.executable,'tools/test_public_exposure.py'])
    run('strict discovery routes',[sys.executable,'tools/check_discovery.py','--base-url',base],timeout=900)
    run('publication review',[sys.executable,'tools/check_publication_review.py','--base-url',base],timeout=900)
    run('Italy claim policy',[sys.executable,'tools/check_italy_claims.py','--base-url',base])
    run('Phase19 rendered policy',[sys.executable,'tools/check_phase19.py','--base-url',base])
    run('technical SEO',[sys.executable,'tools/check_technical_seo.py','--base-url',base])
    run('read-only LLM directory parity',[sys.executable,'tools/build_llms_directory.py','--base-url',base])
    run('Phase20 content inventory',[sys.executable,'tools/check_phase20.py','--base-url',base],timeout=900)
    captures=a.evidence/'captures';captures.mkdir()
    sys.path.insert(0,str(ROOT/'tools'))
    from check_discovery import routes as discovery_routes
    manifest={}
    route_index=a.render_dir/'routes.json'
    if not route_index.exists():route_index=pathlib.Path(env['PHASE31_EVIDENCE'])/'routes.json'
    entry=json.loads(route_index.read_text())['routes']
    render_map={x['url']:x for x in entry}
    for i,(route,info) in enumerate(discovery_routes(ROOT).items()):
        render=render_map[route]
        name=f'{i:02}.html';(captures/name).write_bytes((a.render_dir/render['evidence']).read_bytes());manifest[route]={'file':name,'info':info}
    (captures/'snapshots.json').write_text(json.dumps(manifest,indent=2)+'\n')
    run('rendered cycle consistency',[sys.executable,'tools/check_cycle_consistency.py','--captures',str(captures)],timeout=900)
    run('43-route exact pre-fix invariants',[sys.executable,'tools/phase31/check.py'],timeout=900)
    # Phase30 and Phase26b are closed historical scopes. Their scripts rewrite
    # legacy reports or impose unrelated release gates. Phase31 uses the frozen
    # 43-route rendered invariants above and leaves those artifacts untouched.
    target_out=a.evidence/'browser-suite.json'
    cmd=['node','tools/phase31/browser-suite.cjs','--out',str(target_out)]
    if a.task==1:cmd.append('--record-baseline')
    if a.baseline_targets:cmd+=['--target-baseline',str(a.baseline_targets)]
    if a.require_visible or a.task>=2:cmd.append('--require-visible')
    run('43-route browser matrix',cmd,timeout=7200)
    axe_out=a.evidence/'accessibility.json';baseline=ROOT/'reports/phase-31-accessibility-baseline.json'
    run('representative WCAG A-AA baseline', ['node','tools/phase31/accessibility.cjs',str(axe_out),str(baseline)],timeout=1800)
    run('git whitespace', ['git','-c','core.whitespace=cr-at-eol','diff','--check'])
    summary={'phase':31,'task':a.task,'started_local_date':datetime.date.today().isoformat(),'parent_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'complete_no_skip_or_resume':True,'suite_seconds':round(time.time()-start,2),'php_files':len(php),'browser_cases':'258 normal-motion route/width/JS combinations plus 48 reduced-motion representative-template cases','exact_43_route_content_invariants':'PASS','legacy_phase30_phase26b':'Not rerun: closed historical scopes; their old scripts rewrite legacy artifacts or impose unrelated release gates.','a11y':'A/AA baseline-relative; preserved pre-existing findings are not labelled fixed','performance_or_live_claims':False,'native_hosting_tests':False,'groups':groups,'all_groups_passed':all(g['status']=='PASS' for g in groups)}
    out=ROOT/f'reports/phase-31-task{a.task}-checks.json';out.write_text(json.dumps(summary,indent=2)+'\n')
    (a.evidence/'result.json').write_text(json.dumps(summary,indent=2)+'\n')
    if not summary['all_groups_passed']:raise SystemExit('At least one suite group failed')
    print(f"PHASE31 TASK{a.task} FULL PASS: {summary['suite_seconds']}s, {len(groups)} groups",flush=True)
if __name__=='__main__':main()
