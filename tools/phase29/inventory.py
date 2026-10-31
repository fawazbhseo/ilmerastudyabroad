#!/usr/bin/env python3
"""Read-only runtime/ZIP inventory and source read/require site ledger."""
import hashlib,json,pathlib,re,zipfile
R=pathlib.Path(__file__).resolve().parents[2];M=json.loads((R/'reports/phase-27-payload-manifest.json').read_text());host='https://ilmerastudyabroad.com'
rows=[];sites=[]
with zipfile.ZipFile(R/'releases/ilmera-deploy-850d0af.zip') as z:
 for f in M['files']:
  p=f['path'];b=(R/p).read_bytes();assert hashlib.sha256(b).hexdigest()==f['sha256'] and z.read(p)==b
  parent=p.split('/')[0];private=parent in ['includes','data','destinations','places','tools','reports'] or p.startswith('phase14-') or p.endswith('.htaccess')
  policy=['.htaccess']+([parent+'/.htaccess'] if private and '/' in p and (R/parent/'.htaccess').exists() else [])+(['assets/fonts/.htaccess'] if p.startswith('assets/fonts/') and p!='assets/fonts/.htaccess' else [])
  url=host+'/'+p;browser='No direct browser request; PHP filesystem dependency' if private else 'Route or static dependency, see role'
  if private: status='403 or404, never raw contents';mime='Error response type is host-specific, not PHP/JSON source'
  else:
   status='200';mime={'.php':'text/html (sitemap.php: application/xml)','.json':'application/json','.css':'text/css','.woff2':'font/woff2','.webp':'image/webp','.png':'image/png','.ico':'image/x-icon','.txt':'text/plain','.html':'text/html','.xml':'application/xml'}.get(pathlib.Path(p).suffix,'host-specific')
  role='Payload runtime/support dependency'
  if p=='assets/css/visual-system.css':role='Critical SERVER-DISK read, inserted as inline style. Browser does NOT fetch this CSS URL';browser='Diagnostic URL only; no stylesheet link, no query version'
  elif p.endswith('-latin.woff2'):role='Critical SERVER-DISK read for destination embedded data fonts; NOT HTTP-dependent there';browser='No HTTP request for destination; inline data:font/woff2'
  elif p.endswith('.woff2'):role='HTTP font for place/article/blog/legal/directory/404; destination removes these faces';browser='Root-absolute /'+p+'; no version query'
  elif p.startswith('includes/'):role='PHP require/include or presentation dependency; never upload elsewhere'
  elif p in ['index.php','services.php','about.php','contact.php']:role='Reference route, deliberately excluded from visual overlay'
  elif p.startswith('assets/images/'):role='Actual header/footer/proof/team image, conditional on rendered template'
  if p.endswith('.php') and not private:
   url=host+('/blog/' if p=='blog/index.php' else '/' if p=='index.php' else '/sitemap.xml' if p=='sitemap.php' else '/'+p[:-4]);browser='Page request, PHP executes includes server-side'
  rows.append(dict(path=p,live_url=url,expected_status=status,expected_content_type=mime,browser_request=browser,role=role,in_payload_hash_match=True,bytes=len(b),sha256=f['sha256'],governing_htaccess=policy))
  if p.endswith('.php'):
   for i,line in enumerate(b.decode().splitlines(),1):
    if re.search(r'\b(?:require(?:_once)?|include(?:_once)?|file_get_contents|file_exists|is_readable|readfile|fopen|defined|define)\b',line):sites.append(dict(file=p,line=i,code=line))
assert len(rows)==130
(R/'reports/phase-29-runtime-inventory.json').write_text(json.dumps({'source_head':'56914f22c1f9a8dd8eb16a05099faffbc2ff1f34','all_130_current_and_zip_hashes_match':True,'files':rows,'runtime_read_include_and_constant_sites':sites},indent=2)+'\n')
text='''# Phase29 design runtime inventory

Source HEAD56914f22c1f9a8dd8eb16a05099faffbc2ff1f34. All130 manifest files match both current bytes/SHA256 and the committed deployment ZIP. This deliberately exhaustive ledger includes data/support and reference-only files so a filesystem dependency is not mistaken for a browser download. No public edit.

## Critical distinction

The design stylesheet is **read by PHP from disk and inlined**, not linked over HTTP. Destination fonts are also read from disk and embedded as data URLs. Thus an HTTP404/403 for /assets/css/visual-system.css or HTTP font failure alone does NOT prove or reproduce Germany's design failure. Missing/unreadable disk assets can break it even if PHP content and footer are current. The header/logo CSS and footer CSS are inline in their includes; the overlay is still needed for correct layout and contrast.

No external local JS file is needed by the rebuilt templates at current HEAD. The generated assets/js/hero-still.js and still images are unused and correctly outside this payload. Rebuilt navigation/footer/font-gate scripts are inline. Reference pages retain their original external Google Fonts, GSAP/ScrollTrigger/Three.js dependencies where present, not evidence these must load on Germany. Exact rendered tags are recorded in Task2.

## Constants and template coverage

includes/visual-config.php:4 ILMERA_SCENES_ENABLED defaults true; false removes scenes, not the design. Line9 ILMERA_VISUAL_TEMPLATE_GROUPS defaults destination/place/article/blog/legal/utility. Line11 ILMERA_VISUAL_INLINE_FONT_TEMPLATES defaults destination. Line13 ILMERA_VISUAL_PLAIN_HERO_TEMPLATES defaults destination. Predefined constants override defaults. Utility covers directory and404. References are explicitly excluded.

Other internal buffer constants: ILMERA_PRESENTATION_STARTED, ILMERA_VISUAL_BUFFER_STARTED and ILMERA_VISUAL_REQUEST_TEMPLATE (forced error classification). PHP includes and disk reads use __DIR__/dirname(__DIR__), not current browser URL, HTTPS detection or host-dependent asset directories. Root-absolute font URLs require deployment at domain root.

## Exact runtime/support files

Status/type entries are expectations, not live probes. Private dependency URLs are diagnostic only: their contents must never be browser-readable. A .htaccess file itself is not a public dependency. Governing policy is inherited root plus the listed child file. There is NO assets/.htaccess in the payload or current tree.

| Exact path | Live/diagnostic URL | Expected status; type | Browser usage / role | Payload hash | Governing rules |
|---|---|---|---|---|---|
'''
for r in rows:text+='| `'+r['path']+'` | '+r['live_url']+' | '+r['expected_status']+'; '+r['expected_content_type']+' | '+r['browser_request']+'; '+r['role']+' | MATCH, `'+r['sha256']+'` | '+', '.join('`'+p+'`' for p in r['governing_htaccess'])+' |\n'
text+='\n## Every source include/read/constant site in the payload\n\nThe machine ledger above retains exact source statements. Dynamic template/data selection is resolved by the destination/place/blog registries and publication review JSON, not a remote CSS configuration service. These dependencies must remain PHP-readable while HTTP-denied.\n\n'
for s in sites:text+='- `'+s['file']+':'+str(s['line'])+'`: `'+s['code'].strip().replace('`','\\`')+'`\n'
(R/'reports/phase-29-runtime-inventory.md').write_text(text)
