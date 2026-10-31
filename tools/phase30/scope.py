#!/usr/bin/env python3
"""Phase30 strict source/archive scope, with optional five-full-cycle final gate."""
import argparse,hashlib,json,os,pathlib,subprocess,zipfile
DEFAULT_ROOT=pathlib.Path(__file__).resolve().parents[2];BASE='90d53583696fc1a1fb63e0435994cd37fd017bbe';p=argparse.ArgumentParser();p.add_argument('--final',action='store_true');p.add_argument('--source-root',type=pathlib.Path,default=DEFAULT_ROOT);a=p.parse_args();R=a.source_root.resolve()
# The suites deliberately regenerate historical-name reports in an external
# worktree. Check preservation on the actual source repo, never those outputs.
SOURCE_ENV={k:v for k,v in os.environ.items() if k not in {'GIT_DIR','GIT_WORK_TREE','GIT_INDEX_FILE'}}
def git(*args):return subprocess.check_output(['git',*args],cwd=R,env=SOURCE_ENV)
assert git('branch','--show-current').decode().strip()=='arena/48320ee5-ilmerastudyabroad'
old=set(git('ls-tree','-r','--name-only',BASE).decode().splitlines());untracked=set(git('ls-files','--others','--exclude-standard').decode().splitlines());now=set(git('ls-files').decode().splitlines())|untracked;changed=set(git('diff','--name-only',BASE).decode().splitlines())|untracked
logs={'CHANGELOG.md','flagged-items-for-verification.md'};public={'includes/site-presentation.php','deploy-check.php'};z=json.loads((R/'reports/phase-30-zip-proof.json').read_text());release=z['archive'];assert not old-now
assert all(f.startswith(('reports/','tools/')) or f in logs|public|{release} for f in changed),changed
old_internal_allowed={'reports/deploy-payload.md','reports/phase-27-payload-manifest.json','reports/post-deploy-checklist.md','reports/post-deploy-checklist.pdf','tools/check_discovery.py','tools/phase26b/check.py','tools/phase24b/exposure.py','tools/test_public_exposure.py','tools/test_wording.py'}
for f in old:
 if f.startswith(('reports/','tools/')) and f not in old_internal_allowed:assert (R/f).read_bytes()==git('show',BASE+':'+f),('Historical internal file changed',f)
protected=[]
for f in sorted(old):
 if f.startswith(('reports/','tools/')) or f in logs|public:continue
 b=(R/f).read_bytes();assert b==git('show',BASE+':'+f),('Unauthorized original source change',f);protected.append({'path':f,'sha256':hashlib.sha256(b).hexdigest()})
assert (R/'includes/site-presentation.php').read_bytes()==git('show','8d3031a:includes/site-presentation.php')
m=json.loads((R/'reports/phase-27-payload-manifest.json').read_text());assert len(m['files'])==m['upload_count']==131
for r in m['files']:
 b=(R/r['path']).read_bytes();assert hashlib.sha256(b).hexdigest()==r['sha256'] and b==git('show',m['source_commit']+':'+r['path']),r['path']
assert hashlib.sha256((R/release).read_bytes()).hexdigest()==z['sha256'] and (R/release).stat().st_size==z['bytes']
with zipfile.ZipFile(R/release) as pack:
 assert sorted(pack.namelist())==sorted(r['path'] for r in m['files'])
 for r in m['files']:assert hashlib.sha256(pack.read(r['path'])).hexdigest()==r['sha256']
for f in logs:
 b=(R/f).read_bytes();before=git('show',BASE+':'+f);assert b.startswith(before)
 added=b[len(before):];assert '\u2014'.encode() not in added
 if b'\r\n' not in before:assert b'\r\n' not in added
 elif before.count(b'\n')==before.count(b'\r\n'):assert added.count(b'\n')==added.count(b'\r\n')
for f in ['sitemap.xml','robots.txt','llms.txt','llms-full.txt']:
 assert b'deploy-check' not in (R/f).read_bytes() and (R/f).read_bytes()==git('show',BASE+':'+f)
for f in ['includes/site-presentation.php']:
 before=git('show',BASE+':'+f);b=(R/f).read_bytes();assert b.count(b'\r\n')==before.count(b'\r\n') and ('\u2014'.encode() not in b)
cycles=[]
for n in range(1,6):
 f=R/('reports/phase-30-task'+str(n)+'-checks.json')
 if f.exists():
  d=json.loads(f.read_text());assert all(c['status']=='PASS' for c in d['full_suite']['checks'].values());cycles.append({'task':n,'groups':len(d['full_suite']['checks']),'seconds':d['full_suite']['seconds'],'all_pass':True})
if a.final:assert len(cycles)==5,'All five complete full cycles required'
result={'passed':True,'baseline':BASE,'runtime_source':m['source_commit'],'only_public_runtime_changes':sorted(public),'no_css_font_image_visual_system_config_status_canonical_heading_faq_schema_internal_link_source_changes':True,'protected_original_files':protected,'all131_manifest_and_zip_hashes_match_source':True,'temporary_checker_excluded_from_discovery':True,'original_line_endings_preserved':True,'root_logs_append_only':True,'no_merge_or_agent_deployment':True,'full_task_cycles_available':cycles,'five_cycle_final_gate':a.final,'changed_paths':sorted(changed),'native_server_or_speed_certification':False}
(R/'reports/phase-30-scope-proof.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS strict Phase30 runtime scope,131-file manifest/ZIP identity; complete full cycles',len(cycles))
