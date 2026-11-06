#!/usr/bin/env python3
"""Pin current committed runtime, rebuild exact131-file export with existing tool."""
import collections,hashlib,json,pathlib,subprocess,zipfile
R=pathlib.Path(__file__).resolve().parents[2];W=pathlib.Path('/home/user/phase30');p=R/'reports/phase-27-payload-manifest.json';m=json.loads(p.read_text());head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip();short=head[:7]
paths=sorted({r['path'] for r in m['files']}|{'deploy-check.php'});assert len(paths)==131
rows=[]
for f in paths:
 b=subprocess.check_output(['git','show',head+':'+f],cwd=R);assert b==(R/f).read_bytes(),('Runtime must be committed before export',f)
 rows.append({'path':f,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'temporary':True} if f=='deploy-check.php' else {'path':f,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
# Keep historical source inventory clearly historical, not a current131-file claim.
m.setdefault('phase27_historical_runtime_commit',m['source_commit']);m['source_commit']=head;m['files']=rows;m['upload_count']=131;m['scope']='Phase30: unchanged design/content except exact shared duplicate fix and temporary keyed/expiring deploy-check.php';m['temporary_payload_files']=['deploy-check.php'];m['count_basis']='Phase30 explicit allowlist131; historical Phase27 metadata below is historical only. releases/ and all reports/tools contents remain excluded except the two original deny policies.'
m['phase30_runtime_delta_from_a3d696f']=['includes/site-presentation.php','deploy-check.php'];m['all_htaccess']=json.loads((W/'old-manifest.json').read_text())['all_htaccess'];p.write_text(json.dumps(m,indent=2)+'\n')
out=W/('export-'+short);archive=W/('ilmera-deploy-'+short+'.zip')
subprocess.run(['python3','tools/phase27/export.py','--source-ref',head,'--out',str(out),'--zip',str(archive)],cwd=R,check=True)
with zipfile.ZipFile(archive) as z:
 names=z.namelist();assert len(names)==len(set(names))==len(rows)==131 and set(names)==set(paths)
 assert len([x for x in names if pathlib.Path(x).name=='.htaccess'])==8
 for row in rows:
  f=row['path'];b=z.read(f);assert hashlib.sha256(b).hexdigest()==row['sha256'] and len(b)==row['bytes']
  assert not f.endswith('.md') and not f.startswith(('.git/','releases/')) and '..' not in pathlib.PurePosixPath(f).parts
  if f.startswith(('reports/','tools/')):assert f in ['reports/.htaccess','tools/.htaccess'] and [s.strip() for s in b.decode().splitlines() if s.strip() and not s.startswith('#')]==['Require all denied']
 assert z.testzip() is None
release=R/'releases'/archive.name;release.write_bytes(archive.read_bytes());assert (R/'releases/.htaccess').read_bytes()==(R/'data/.htaccess').read_bytes()
counts=collections.Counter(str(pathlib.PurePosixPath(f).parent) for f in paths)
proof={'passed':True,'source_commit':head,'archive':release.relative_to(R).as_posix(),'bytes':archive.stat().st_size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'file_count':131,'all_hashes_and_sizes_match':True,'root_layout_no_wrapper':True,'all_eight_htaccess':m['all_htaccess'],'no_report_tool_content_except_two_deny_files':True,'no_markdown_git_releases':True,'temporary_file':'deploy-check.php','folder_counts':dict(sorted(counts.items())),'download_url':'https://raw.githubusercontent.com/fawazbhseo/ilmerastudyabroad/arena/48320ee5-ilmerastudyabroad/releases/'+archive.name,'external_clean_root':str(out)}
(R/'reports/phase-30-zip-proof.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof,indent=2))
