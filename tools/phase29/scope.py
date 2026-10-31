#!/usr/bin/env python3
"""Verify Phase29 is reports/tools only plus explicitly authorized append-only logs."""
import ast,hashlib,json,pathlib,subprocess
R=pathlib.Path(__file__).resolve().parents[2];BASE='56914f22c1f9a8dd8eb16a05099faffbc2ff1f34'
def git(*a):return subprocess.check_output(['git',*a],cwd=R)
assert git('branch','--show-current').decode().strip()=='arena/48320ee5-ilmerastudyabroad'
old=set(git('ls-tree','-r','--name-only',BASE).decode().splitlines());untracked=set(git('ls-files','--others','--exclude-standard').decode().splitlines());current=set(git('ls-files').decode().splitlines())|untracked;changed=set(git('diff','--name-only',BASE).decode().splitlines())|untracked
logs={'CHANGELOG.md','flagged-items-for-verification.md'};assert not old-current
assert all(p.startswith(('reports/','tools/')) or p in logs for p in changed)
unchanged=[]
for f in sorted(old-logs):
 b=(R/f).read_bytes();assert b==git('show',BASE+':'+f),f
 unchanged.append({'path':f,'sha256':hashlib.sha256(b).hexdigest()})
for f in logs:
 before=git('show',BASE+':'+f);after=(R/f).read_bytes();assert after.startswith(before),f
 added=after[len(before):];assert '\u2014'.encode() not in added,f
 if b'\r\n' in before and before.count(b'\n')==before.count(b'\r\n'):assert added.count(b'\n')==added.count(b'\r\n'),f
 elif b'\r\n' not in before:assert b'\r\n' not in added,f
for f in current-old:
 if not f.endswith('.png'):assert '\u2014'.encode() not in (R/f).read_bytes(),('New em dash',f)
m=json.loads((R/'reports/phase-27-payload-manifest.json').read_text())
for r in m['files']:assert hashlib.sha256((R/r['path']).read_bytes()).hexdigest()==r['sha256'],r['path']
z=R/'releases/ilmera-deploy-850d0af.zip';assert z.read_bytes()==git('show',BASE+':releases/ilmera-deploy-850d0af.zip')
faults=json.loads((R/'reports/phase-29-fault-results.json').read_text());assert len(faults['cases'])==22
for c in faults['cases']:assert hashlib.sha256((R/c['screenshot']).read_bytes()).hexdigest()==c['screenshot_sha256']
assert len(list((R/'reports/screenshots/phase-29').glob('*.png')))==24
for f in (R/'tools/phase29').glob('*.py'):ast.parse(f.read_text(),filename=str(f))
for f in (R/'tools/phase29').glob('*.cjs'):subprocess.run(['node','--check',str(f)],check=True)
proof={'passed':True,'baseline':BASE,'changed_paths':sorted(changed),'new_paths_restricted_to_reports_tools':True,'public_runtime_changes':[],'all_preexisting_files_except_append_only_logs_byte_identical':True,'unchanged_original_file_count':len(unchanged),'unchanged_original_files':unchanged,'all_130_payload_hashes_unchanged':True,'deployment_zip_bytes_unchanged':True,'root_logs_append_only':True,'original_line_endings_preserved':True,'no_new_em_dashes':True,'diagnostic_cases':22,'screenshot_count':24,'screenshot_hashes_verified':True,'diagnostic_python_and_javascript_syntax':'PASS','native_server_or_live_origin_or_deployment_proof':False}
(R/'reports/phase-29-scope-proof.json').write_text(json.dumps(proof,indent=2)+'\n')
print('PASS original source bytes/line endings,130 manifest hashes, ZIP,22 cases/24 screenshots, tools syntax, append-only logs; changed paths',len(changed))
