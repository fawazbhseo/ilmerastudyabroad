#!/usr/bin/env python3
"""Prepare disposable diagnostic roots, never mutate checkout/runtime source."""
import hashlib,json,pathlib,subprocess,zipfile
R=pathlib.Path(__file__).resolve().parents[2];W=pathlib.Path('/home/user/phase29');W.mkdir(exist_ok=True)
m=json.loads((R/'reports/phase-27-payload-manifest.json').read_text());root=W/'payload';assert not root.exists();root.mkdir()
with zipfile.ZipFile(R/'releases/ilmera-deploy-850d0af.zip') as z:
 for row in m['files']:
  b=z.read(row['path']);assert hashlib.sha256(b).hexdigest()==row['sha256'];p=root/row['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
assert len([f for f in root.rglob('*') if f.is_file()])==130
# End-of-Phase13 history, not main/import baseline and not another page substituted.
old=W/'phase13';old.mkdir()
archive=subprocess.check_output(['git','archive','a643836'],cwd=R)
subprocess.run(['tar','-x','-C',str(old)],input=archive,check=True)
base=json.loads((R/'reports/phase-25-baseline-renders.json').read_text())
html=base['routes']['/study-in-germany']['html'];(W/'cached-predesign.html').write_bytes(html.encode())
changed=set(subprocess.check_output(['git','diff','--name-only','a643836','56914f2','--','*.php'],cwd=R,text=True).splitlines())
(W/'changed-php.json').write_text(json.dumps(sorted(changed)))
(W/'preparation.json').write_text(json.dumps({'exact_clean_payload_files':130,'source':'56914f2','zip':'releases/ilmera-deploy-850d0af.zip','phase13_ref':subprocess.check_output(['git','rev-parse','a643836'],cwd=R,text=True).strip(),'predesign_cache_source':'reports/phase-25-baseline-renders.json, actual frozen /study-in-germany HTML','predesign_cache_sha256':hashlib.sha256(html.encode()).hexdigest(),'changed_since_phase13_php_files':sorted(changed)},indent=2)+'\n')
print('Prepared clean130-file ZIP payload, actual Phase13 root, predesign cached HTML and changed-PHP ledger')
