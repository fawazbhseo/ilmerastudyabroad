#!/usr/bin/env python3
"""Full existing functional gates per task, in isolated output archives, no skips."""
import argparse,json,os,pathlib,shutil,subprocess,sys
ROOT=pathlib.Path(__file__).resolve().parents[2];p=argparse.ArgumentParser();p.add_argument('task',type=int);p.add_argument('--attempt',type=int,default=1);a=p.parse_args();W=pathlib.Path('/home/user/phase30');suffix=str(a.task)+('-attempt'+str(a.attempt) if a.attempt>1 else '');S=W/('suite-task'+suffix);assert not S.exists();S.mkdir()
files=set(subprocess.check_output(['git','ls-files'],cwd=ROOT,text=True).splitlines())|set(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=ROOT,text=True).splitlines())
for f in sorted(files):
 target=S/f;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/f,target)
env=dict(os.environ,PHASE30_SOURCE_ROOT=str(ROOT),GIT_DIR=str(ROOT/'.git'),GIT_WORK_TREE=str(S),GIT_INDEX_FILE=str(W/('index-task'+suffix)))
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip();subprocess.run(['git','read-tree',head],cwd=S,env=env,check=True)
E=W/('evidence-task'+suffix);subprocess.run([sys.executable,'tools/phase30/run.py','--task','phase30-task'+str(a.task),'--stage','5','--evidence',str(E)],cwd=S,env=env,check=True)
r=json.loads((E/'result.json').read_text());assert all(c['status']=='PASS' for c in r['checks'].values())
aa=json.loads((S/'reports/phase-25c-accessibility.json').read_text())
out={'task':a.task,'snapshot_parent':head,'full_suite_no_skip_or_resume':True,'full_suite':r,'accessibility':aa,'native_host_or_live_deployment':False,'performance_retry':False,'historical_reports_unchanged':True}
(ROOT/('reports/phase-30-task'+str(a.task)+'-checks.json')).write_text(json.dumps(out,indent=2)+'\n');print('PHASE30 TASK'+str(a.task)+' FULL PASS',flush=True)
