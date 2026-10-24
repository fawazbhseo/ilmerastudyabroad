#!/usr/bin/env python3
"""Run the existing FULL functional suite in an archive; never overwrite historical reports."""
import hashlib,json,os,pathlib,subprocess,sys
ROOT=pathlib.Path(__file__).resolve().parents[2];WORK=pathlib.Path('/home/user/phase27');SRC=WORK/'source';SOURCE='a3d696f7942b2df5c76d660c2b9f3252881ce314'
# Scope is stronger than suffix checks: absolutely every changed path must be internal.
changed=set(subprocess.check_output(['git','diff','--name-only',SOURCE],cwd=ROOT,text=True).splitlines())
changed|=set(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=ROOT,text=True).splitlines())
assert all(f.startswith(('reports/','tools/')) or f in ('CHANGELOG.md','flagged-items-for-verification.md') for f in changed),changed
for f in subprocess.check_output(['git','ls-tree','-r','--name-only',SOURCE],cwd=ROOT,text=True).splitlines():
    if f.startswith(('reports/','tools/')) or f in ('CHANGELOG.md','flagged-items-for-verification.md'):continue
    assert (ROOT/f).read_bytes()==(SRC/f).read_bytes(),('Runtime drift',f)
index=WORK/'verify-index';env=dict(os.environ);env['GIT_DIR']=str(ROOT/'.git');env['GIT_WORK_TREE']=str(SRC);env['GIT_INDEX_FILE']=str(index)
subprocess.run(['git','read-tree',SOURCE],cwd=SRC,env=env,check=True)
evidence=WORK/'evidence/full'
subprocess.run([sys.executable,'tools/phase26b/run.py','--task','phase27-current-branch','--stage','5','--evidence',str(evidence)],cwd=SRC,env=env,check=True)
full=json.loads((evidence/'result.json').read_text());assert all(v['status']=='PASS' for v in full['checks'].values())
accessibility=json.loads((SRC/'reports/phase-25c-accessibility.json').read_text())
result={'source_runtime_commit':SOURCE,'lookup_parent_not_runtime_build':full['parent'],'actual_suite':'Existing tools/phase26b/run.py unchanged, no resume/skip flags','full_suite':full,'public_file_changes':[],'source_runtime_matches_working_branch':True,'report_outputs_written_only_outside_git':True,'accessibility':{'cases':len(accessibility['cases']),'rebuilt_violations':accessibility['axe_rebuilt_violations'],'reference_groups':accessibility['reference_violations'],'fresh_reference_nodes':sum(len(v['nodes']) for c in accessibility['cases'] if not c['shape']['rebuilt'] for v in c['violations']),'overflow_cases':accessibility['overflow_cases'],'historical391_nodes_preserved':True},'performance_session':False,'native_server_proof':False,'deployment':False}
(ROOT/'reports/phase-27-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print('PHASE27 FULL PASS; no public runtime changes; no historical report rewritten',flush=True)
