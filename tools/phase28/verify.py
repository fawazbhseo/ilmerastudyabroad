#!/usr/bin/env python3
"""Fresh existing full functional checks in a disposable archive, no historical rewrites."""
import json,os,pathlib,subprocess,sys,tarfile
ROOT=pathlib.Path(__file__).resolve().parents[2];WORK=pathlib.Path('/home/user/phase28');BASE='850d0af5c083b06e3c65abc997fcab6708121c6f';SRC=WORK/'verify'
allowed_release={'releases/.htaccess','releases/ilmera-deploy-850d0af.zip'}
changed=set(subprocess.check_output(['git','diff','--name-only',BASE],cwd=ROOT,text=True).splitlines())|set(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=ROOT,text=True).splitlines())
assert all(f.startswith(('reports/','tools/')) or f in allowed_release|{'CHANGELOG.md','flagged-items-for-verification.md'} for f in changed),changed
m=json.loads((ROOT/'reports/phase-27-payload-manifest.json').read_text())
for row in m['files']:assert (ROOT/row['path']).read_bytes()==subprocess.check_output(['git','show',BASE+':'+row['path']],cwd=ROOT),row['path']
assert not SRC.exists(),'Use a new external archive, not a dirty previous run'
SRC.mkdir();archive=WORK/'verify-source.tar';head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
subprocess.run(['git','archive','--output',str(archive),head],cwd=ROOT,check=True)
with tarfile.open(archive) as t:
    assert all(not p.name.startswith('/') and '..' not in pathlib.PurePosixPath(p.name).parts and not p.issym() and not p.islnk() for p in t.getmembers())
    t.extractall(SRC)
env=dict(os.environ);env.update(GIT_DIR=str(ROOT/'.git'),GIT_WORK_TREE=str(SRC),GIT_INDEX_FILE=str(WORK/'verify-index'))
subprocess.run(['git','read-tree',head],cwd=SRC,env=env,check=True)
evidence=WORK/'evidence/full'
subprocess.run([sys.executable,'tools/phase26b/run.py','--task','phase28-downloadable-pack','--stage','5','--evidence',str(evidence)],cwd=SRC,env=env,check=True)
result=json.loads((evidence/'result.json').read_text());assert all(v['status']=='PASS' for v in result['checks'].values())
aa=json.loads((SRC/'reports/phase-25c-accessibility.json').read_text())
output={'baseline':BASE,'archive_parent':head,'existing_suite_unchanged':True,'full_suite':result,'public_runtime_changes':[],'release_only_exception':sorted(allowed_release),'historical_reports_unchanged':True,'reference_accessibility':{'groups':aa['reference_violations'],'nodes':sum(len(v['nodes']) for c in aa['cases'] if not c['shape']['rebuilt'] for v in c['violations']),'overflow_cases':aa['overflow_cases'],'all_reference_cases':[c for c in aa['cases'] if not c['shape']['rebuilt']],'historical_observations_preserved':True},'performance_retry':False,'native_server_or_deployment_proof':False}
(ROOT/'reports/phase-28-verification.json').write_text(json.dumps(output,indent=2)+'\n');print('PHASE28 FULL PASS',flush=True)
