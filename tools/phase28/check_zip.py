#!/usr/bin/env python3
"""Verify only manifest members, their bytes, eight policies and safe root layout."""
import argparse,hashlib,json,pathlib,stat,subprocess,zipfile
ROOT=pathlib.Path(__file__).resolve().parents[2]
p=argparse.ArgumentParser();p.add_argument('zip',type=pathlib.Path);p.add_argument('--out',type=pathlib.Path,required=True);a=p.parse_args()
m=json.loads((ROOT/'reports/phase-27-payload-manifest.json').read_text());rows={r['path']:r for r in m['files']};assert len(rows)==130
with zipfile.ZipFile(a.zip) as z:
    names=z.namelist();assert len(names)==len(set(names))==len(rows) and set(names)==set(rows)
    assert z.testzip() is None
    for f in names:
        assert not f.startswith('/') and '..' not in pathlib.PurePosixPath(f).parts and '\\' not in f
        assert not stat.S_ISLNK(z.getinfo(f).external_attr>>16)
        assert not f.endswith('.md') and not any(v in pathlib.PurePosixPath(f).parts for v in ['.git','releases','node_modules','__pycache__'])
        if f.startswith(('reports/','tools/')):assert f in ['reports/.htaccess','tools/.htaccess']
        b=z.read(f);assert len(b)==rows[f]['bytes'] and hashlib.sha256(b).hexdigest()==rows[f]['sha256'],f
        assert b==(ROOT/f).read_bytes(),('Current HEAD/worktree runtime differs',f)
        assert b==subprocess.check_output(['git','show','850d0af:'+f],cwd=ROOT),('Starting HEAD blob differs',f)
    denies=sorted(f for f in names if pathlib.Path(f).name=='.htaccess');assert len(denies)==8 and denies==sorted(m['all_htaccess'])
result={'archive':a.zip.name,'source_head':'850d0af5c083b06e3c65abc997fcab6708121c6f','manifest_runtime_commit':m['source_commit'],'file_count':len(names),'manifest_count':len(rows),'all_hashes_sizes_match':True,'all_current_runtime_bytes_match':True,'all_eight_htaccess':denies,'no_extra_or_duplicate_or_unsafe_entries':True,'no_markdown_git_releases_or_tool_report_contents':True,'root_layout_ready_for_public_html':True,'bytes':a.zip.stat().st_size,'sha256':hashlib.sha256(a.zip.read_bytes()).hexdigest(),'passed':True}
a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
