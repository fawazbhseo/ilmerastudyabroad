"""Final bounded changed-template regression, not another reference retry."""
import json,pathlib,subprocess,time
R=pathlib.Path(__file__).resolve().parents[3];start=time.time();checks=[]
commands=[['php','tools/phase25/stage2/policy.php','on'],['php','tools/phase25/stage2/policy.php','off'],['php','tools/phase25/stage2/policy.php','inline'],['python3','tools/phase25/stage2/check.py'],['python3','tools/check_phase20.py','--base-url','http://127.0.0.1:8080'],['python3','tools/check_publication_review.py','--base-url','http://127.0.0.1:8080'],['python3','tools/check_discovery.py','--base-url','http://127.0.0.1:8080'],['python3','tools/check_technical_seo.py','--base-url','http://127.0.0.1:8080']]
for f in sorted(R.rglob('*.php')):
 p=subprocess.run(['php','-l',str(f)],cwd=R,capture_output=True,text=True);assert p.returncode==0 and 'No syntax errors detected' in p.stdout
for command in commands:
 p=subprocess.run(command,cwd=R,capture_output=True,text=True);assert p.returncode==0,(command,p.stdout,p.stderr);checks.append({'command':command,'passed':True,'tail':p.stdout[-1600:]})
aa=json.loads((R/'reports/phase-25-stage-2-final-destination-axe.json').read_text());assert len(aa['cases'])==6 and aa['axe_rebuilt_violations']==0 and not aa['overflow_cases']
chrome=json.loads((R/'reports/phase-25-stage-2-chrome.json').read_text());deviations=[r for r in chrome['rows'] if r['differences']]
report={'cycle':3,'scope':'Final changed destination font/hero template; fresh43-route semantic/protected-source/publication/discovery/SEO guards. Immutable-reference raster/axe/performance failures are retained without retry. No further cycles.','checks':checks,'php_files':len(list(R.rglob('*.php'))),'destination_axe_cases':6,'destination_axe_violations':0,'chrome_deviations':deviations,'core_checks_passed':True,'all_release_criteria_passed':False,'seconds':round(time.time()-start,2)}
(R/'reports/phase-25-stage-2-final-checks.json').write_text(json.dumps(report,indent=2)+'\n');print('Final cycle3 core PASS; known release criteria FAIL; seconds',report['seconds'])
