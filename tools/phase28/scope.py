#!/usr/bin/env python3
"""Verify Phase28 touches only named internal files and excluded release artifacts."""
import hashlib,json,pathlib,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[2];BASE='850d0af5c083b06e3c65abc997fcab6708121c6f'
def git(*a):return subprocess.check_output(['git',*a],cwd=ROOT)
old=set(git('ls-tree','-r','--name-only',BASE).decode().splitlines());current=set(git('ls-files').decode().splitlines())|set(git('ls-files','--others','--exclude-standard').decode().splitlines())
changed=set(git('diff','--name-only',BASE).decode().splitlines())|set(git('ls-files','--others','--exclude-standard').decode().splitlines())
old_allowed={'reports/deploy-payload.md','reports/phase-27-payload-manifest.json','reports/post-deploy-checklist.md','reports/post-deploy-checklist.pdf','tools/phase27/export.py','CHANGELOG.md','flagged-items-for-verification.md'}
releases={'releases/.htaccess','releases/ilmera-deploy-850d0af.zip'}
assert changed&old<=old_allowed and not old-current
assert all(f.startswith(('reports/phase-28-','tools/phase28/')) or f in releases for f in changed-old)
unchanged=[]
for f in sorted(old-old_allowed):
    b=(ROOT/f).read_bytes();assert b==git('show',BASE+':'+f),f
    unchanged.append({'path':f,'sha256':hashlib.sha256(b).hexdigest()})
for f in ['CHANGELOG.md','flagged-items-for-verification.md']:
    before=git('show',BASE+':'+f);assert (ROOT/f).read_bytes().startswith(before),f
for f in (changed&old_allowed)-{'reports/post-deploy-checklist.pdf'}:
    before=git('show',BASE+':'+f);after=(ROOT/f).read_bytes()
    if b'\r\n' not in before:assert b'\r\n' not in after,f
    elif before.count(b'\n')==before.count(b'\r\n'):assert after.count(b'\n')==after.count(b'\r\n'),f
for f in changed-{'reports/post-deploy-checklist.pdf','releases/ilmera-deploy-850d0af.zip'}:
    b=(ROOT/f).read_bytes();prior=git('show',BASE+':'+f) if f in old else b''
    assert b.count('\u2014'.encode())<=prior.count('\u2014'.encode()),('New em dash',f)
m=json.loads((ROOT/'reports/phase-27-payload-manifest.json').read_text());previous=json.loads(git('show',BASE+':reports/phase-27-payload-manifest.json'));assert m['files']==previous['files'] and m['all_htaccess']==previous['all_htaccess']
for r in m['files']:assert hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()==r['sha256']
assert (ROOT/'releases/.htaccess').read_bytes()==(ROOT/'data/.htaccess').read_bytes()
proof={'passed':True,'baseline':BASE,'public_php_css_js_images_fonts_original_htaccess_sitemap_robots_llms_changes':[],'all_original_files_outside_explicit_internal_allowlist_byte_identical':True,'unchanged_original_file_count':len(unchanged),'unchanged_files':unchanged,'upload_manifest_files_hashes_and_eight_policies_unchanged':True,'root_logs_append_only':True,'existing_line_endings_preserved':True,'no_new_em_dashes':True,'excluded_release_exceptions':sorted(releases),'changed_paths':sorted(changed)}
(ROOT/'reports/phase-28-scope-proof.json').write_text(json.dumps(proof,indent=2)+'\n');print('PASS no public changes, append-only logs and unchanged line endings')
