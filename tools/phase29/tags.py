#!/usr/bin/env python3
"""Preserve exact rendered design tags; no beautification or base64 elision."""
import hashlib,json,pathlib,re
R=pathlib.Path(__file__).resolve().parents[2];W=pathlib.Path('/home/user/phase29');D=R/'reports/phase-29-design-tags';D.mkdir(exist_ok=True);rows=[]
for route in ['/study-in-germany','/study-abroad-counselling-mysuru','/blog/how-to-choose-study-abroad-consultant-karnataka','/blog/']:
 key=route.lstrip('/').replace('/','_');body=(W/'current-renders'/f'{key}.html').read_bytes();text=body.decode();tags=re.findall(r'<link\b[^>]*>|<style\b[^>]*>.*?</style>|<script\b[^>]*>.*?</script>',text,re.S|re.I);tags=[t for t in tags if not re.match(r'<script\b[^>]*type="application/ld\+json"',t)]
 data=[];out=[]
 for n,t in enumerate(tags,1):
  out.append(t);url=re.search(r'(?:href|src)="([^"]+)"',t.split('>',1)[0]);u=url[1] if url else None
  role='base template inline styling'
  if 'id="ilmera-visual-system"' in t:role='PHP-read shared CSS and fonts, exact inline payload'
  elif 'document.fonts' in t:role='inline font visibility gate; Promise/FontFaceSet support,3000ms timeout'
  elif '<script' in t:role='inline navigation/footer/scroll interaction; no external design JS file'
  elif u and '/fonts/' in u:role='above-fold static font preload (not emitted on destination)'
  elif 'canonical' in t:role='canonical URL, consumed by PHP overlay route classifier, not a design asset'
  elif 'icon' in t:role='favicon/image browser request'
  data.append({'tag':n,'role':role,'url':u,'path_kind':'inline, no HTTP path' if u is None else 'root-absolute, same origin' if u.startswith('/') else 'fully-qualified absolute' if u.startswith('https://') else 'relative','version_query':bool(u and '?' in u),'sha256':hashlib.sha256(t.encode()).hexdigest(),'bytes':len(t.encode())})
 destination=D/(key+'.html');destination.write_bytes(('\n'.join(out)+'\n').encode())
 file='blog/index.php' if route=='/blog/' else route.lstrip('/')+'.php';trace=json.loads((W/'diagnostics'/('normal-'+file.replace('/','_')+'.json')).read_text())
 rows.append({'route':route,'raw_html_sha256':hashlib.sha256(body).hexdigest(),'exact_tag_copy':destination.relative_to(R).as_posix(),'tags':data,'actual_executed_php_includes':trace['includes'],'php_warning_errors':trace['errors']})
(R/'reports/phase-29-design-loading.json').write_text(json.dumps({'source_head':'56914f2','method':'Clean ZIP-only PHP8.5 render; exact tag text, all link/style/script except non-design JSON-LD; canonical retained because classifier consumes it','routes':rows},indent=2)+'\n')
text='''# Phase29 how rendered pages load the design

Clean130-file ZIP root, PHP8.5; no live-origin request. Every actual link, style, script and preload tag belonging to presentation is copied verbatim, without base64 elision, in the four linked .html extracts below. JSON-LD is excluded as schema, not design. Canonical tags are included because the PHP design classifier consumes them. Inline base template, header and footer styles/scripts are included too. The copies are evidence in private reports, never website files.

## Exact tag ledger

'''
for row in rows:
 text+='### '+row['route']+'\n\nExact tags: ['+pathlib.Path(row['exact_tag_copy']).name+'](phase-29-design-tags/'+pathlib.Path(row['exact_tag_copy']).name+'). Full-render SHA256 `'+row['raw_html_sha256']+'`.\n\n|Tag|Role|URL/path|Version query|Bytes|\n|---|---|---|---|---|\n'
 for t in row['tags']:text+='|'+str(t['tag'])+'|'+t['role']+'|'+(t['url'] or 'Inline')+'; '+t['path_kind']+'|'+str(t['version_query'])+'|'+str(t['bytes'])+'|\n'
 text+='\nActual PHP include trace: '+', '.join('`'+s.replace('/site/','')+'`' for s in row['actual_executed_php_includes'])+'.\n\n'
text+='''## Conditions, fallbacks and source lines

- includes/site-presentation.php:2 requires visual-system.php; visual-system.php:2 requires visual-config.php. Both are require_once, not optional/file_exists/@include. Missing or genuinely unreadable required files fail fatally, not silently return old styling. Native PHP error display/logging controls visibility, not success.
- visual-config.php:4,9,11,13 defaults are guarded by defined(). A prepend/bootstrap may predefine constants. Empty or excluded ILMERA_VISUAL_TEMPLATE_GROUPS makes visual-system.php:24 return original markup. This can silently produce old styling. Scene false at visual-system.php:8-12 only hides decorative overlays; it does not disable light sections/fonts/header.
- site-presentation.php:151-154 starts output buffering once. visual-system.php:103-107 does not start a second buffer if ILMERA_PRESENTATION_STARTED or ILMERA_VISUAL_BUFFER_STARTED already exists. A foreign predefinition can suppress a required buffer. Callback failure is not an intentional old-theme fallback.
- site-presentation.php:58 returns unchanged HTML when its exact HTTPS canonical pattern does not match. Because its buffer is already started, the alternate visual buffer does not rescue this path. No HTTPS server detection: it is a literal HTML canonical comparison. Missing/nonmatching canonical or another-domain canonical can therefore skip styling there.
- site-presentation.php:61 delegates noindex/unmapped routes to visual_present; not a blanket design exclusion. visual-system.php:17-24 skips an existing ilmera-visual-system marker even if its contents are empty, explicitly excludes four references, and skips unclassified/disabled templates. visual-system.php:20 falls back to REQUEST_URI only when canonical capture is absent. Error constant can force /404 at line21. A /preview path without a valid canonical can fail classification.
- visual-system.php:25 only rewrites literal <body>. Altered body markup with attributes can miss the p25 class, leaving body-scoped rules inactive even if CSS was injected. Current four renders all match correctly.
- visual-system.php:35-36 removes Google stylesheet/preconnect tags before disk asset reads. Lines65 and72 use unguarded, non-error-suppressed file_get_contents. Missing/unreadable CSS gives a warning plus false/empty content, not a checked theme fallback. Missing inline font files generate empty data fonts. If production hides warnings, a content-complete but visually broken200 page can result. No file_exists/is_readable branch and no @ suppression protects these reads. This is the principal silent failure surface.
- visual-system.php:67-77 uses template constants to choose static root-absolute font URLs/preloads versus embedded data fonts. Destination emits NO /assets/css stylesheet link and NO HTTP font URL. No cache-busting version query on CSS/font/image paths or inline styles. Cached HTML freezes its inline CSS and embedded fonts until HTML cache is purged, even after replacing asset files.
- visual-system.php:79-87 chooses plain hero by template, inserts font gate and exact </head> replacement. Missing </head> prevents insertion; altered head/body markup can defeat string transforms. The gate waits at most3000ms for font API promises; it is not a PHP-version or host switch, and is not intended to permanently hide header/CTA.
- visual-system.php:38-51 moves article/blog/legal/directory hero introductions to light reading areas only when matching literal section/container patterns. A stale/different template may retain old placement. Germany's base template already has its answer paragraphs in the reading section.
- Includes/header.php reads REQUEST_URI:2 for active nav only. No environment/getenv/HTTP_HOST/HTTPS/PHP_VERSION/version_compare/file_exists/error-suppressed include controls the four rendered design injections. Host name is a hardcoded canonical classifier plus absolute image/navigation URLs, not a live CSS enable switch. Inline scripts still need browser CSP allowance; CSP is not set by tracked .htaccess.

A file_exists check in unrelated publication/data helpers is not a CSS fallback. The exhaustive source-site inventory differentiates those data availability gates. Newer PHP compatibility and the observable fault outcomes are tested in Task3 rather than inferred as a styling-only failure.
'''
(R/'reports/phase-29-design-loading.md').write_text(text)
print('Preserved exact design tags for4 routes and PHP include traces')
