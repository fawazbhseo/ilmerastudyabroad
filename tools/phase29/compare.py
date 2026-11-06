#!/usr/bin/env python3
"""Compare explicit observable symptoms, never claim an unavailable owner's pixel match."""
import hashlib,json,pathlib
R=pathlib.Path(__file__).resolve().parents[2];p=R/'reports/phase-29-fault-results.json';d=json.loads(p.read_text());notes={
'normal':'Control: full130-file payload applies new design.',
'http-css-404':'CSS diagnostic URL404 verified, but no browser stylesheet request: PHP inline CSS is unchanged.',
'http-css-403':'CSS diagnostic URL403 verified, but filesystem read is allowed: unchanged inline design.',
'http-fonts-404':'All HTTP font paths404. Germany uses data fonts, so headings still use Cormorant.',
'scenes-off':'False changes decoration only; destination hero was already plain. Design remains.',
'config-missing':'Required config missing is fatal500, not an old-look complete page.',
'visual-missing':'Required visual-system missing is fatal500, no silent include fallback.',
'cached-phase13':'Actual end-Phase13 HTML with current static files: old content/old styling, no current direct-answer CTA. External Google font requests aborted, not evidence live Google fonts fail.',
'cached-predesign':'Actual frozen predesign Germany HTML with current assets: old dark layout, but header and CTA text visible. External Google fonts aborted, so default-serif observation is conditional on that external block.',
'changed-php-only':'Changed-since-Phase13 PHP subset in empty folder misses unchanged breadcrumbs.php and fails500. No JSON/assets; not the complete current content screenshot.',
'changed-php-over-phase13':'Actual Phase13 tree overlaid with changed PHP, assets removed. Required PHP now available but new JSON absent.200 dark/fallback fonts, no current direct-answer CTA. Not exact.',
'subfolder':'Whole payload under /preview; root-absolute image/font URLs break. Germany CSS and data fonts still inline and correct. Direct root Germany URL is404. Not the reported content-complete old look.',
'php-7.4':'Fatal undefined str_ends_with at includes/destination-data.php:140, also posts.php:126. PHP API compatibility issue, not styling-only fallback.',
'php-8.0':'PHP8.0 applies design successfully in local VM; not native-host certification.',
'php-8.1':'PHP8.1 applies design successfully in local VM; not native-host certification.',
'php-8.5':'PHP8.5 applies design successfully in local VM; not native-host certification.',
'disk-css-missing':'Warning-only missing PHP-read CSS: dark reading sections and identical gold CTA foreground/background. Fonts still inline and header present.',
'disk-fonts-missing':'Warning-only missing two disk font faces: actual fallback serif, but light sections and readable CTA/header remain.',
'no-assets':'All assets absent on disk: dark, fallback serif, blank-looking gold CTA and no light reading sections, but header text/hamburger remain. Four of five visual symptoms, not exact.',
'groups-disabled':'Deliberately predefined empty template groups skips overlay. Dark layout, but header and CTA text remain. Not exact. Requires non-default config/bootstrap not present in payload.',
'header-missing':'Non-required header include missing: warning,200 current content with absent nav, but correct light sections/fonts/readable CTA.',
'no-assets-header-missing':'Explicit COMBINATION: missing assets folder plus missing includes/header.php.200 retains current copy, online-only disclosure and footer, but matches all five stated visual symptoms. Not a pixel-exact owner screenshot comparison.'}
rows=[]
for c in d['cases']:
 m=c['metrics'];font=any('Serif' in f['familyName'] and 'Cormorant' not in f['familyName'] for f in c['actualHeadingFonts']);reading=m['firstReading'];cta=m['firstCTA'];dark=bool(reading and reading['background']=='rgba(10, 22, 40, 0.6)');symptoms={'dark_reading_layout':dark,'header_absent':m['nav'] is None,'default_serif_heading':font,'blank_gold_CTA':bool(cta and cta['text'] and cta['color']==cta['background']=='rgb(201, 168, 76)'),'no_light_reading_sections':dark};c['owner_description_comparison']=symptoms;c['matching_symptom_count']=sum(symptoms.values());c['note']=notes[c['case']];c['screenshot_sha256']=hashlib.sha256((R/c['screenshot']).read_bytes()).hexdigest();rows.append(c)
assert len(rows)==22;combo=next(r for r in rows if r['case']=='no-assets-header-missing');assert combo['matching_symptom_count']==5 and combo['status']==200 and combo['metrics']['onlineOnly'] and combo['metrics']['footer'] is not None
assert all(r['matching_symptom_count']<5 for r in rows if r['case']!='no-assets-header-missing')
d.update(cases=rows,owner_original_screenshot_available=False,pixel_exact_live_match_verified=False,all_five_description_symptoms_reproduced_by='no-assets-header-missing',screenshots_count=24);p.write_text(json.dumps(d,indent=2)+'\n')
text='''# Phase29 mobile fault reproduction

390x844 viewport, device scale1, current committed130-file ZIP extracted into a new empty folder. Clean normal PHP VM has no original-checkout mount. Per-case filesystem faults exist only in disposable VM copies; HTTP faults are explicit response cases. All warnings captured with display_errors=0, to model production-style hidden warnings rather than convert every warning into an adapter500. Native filesystem permissions/Apache behavior are not simulated.22 cases,24 PNGs (full page each plus two viewport crops) under screenshots/phase-29/. No performance measurements or extra reliability lab.

**No original owner image was provided. We cannot claim pixel-exact live reproduction or a confirmed live root cause.** The explicitly labelled combination of missing assets/ plus missing includes/header.php matches all five textual symptoms and retains current online-only content/footer. No tested single fault matches all five. Missing the assets folder alone matches four; the nav text/hamburger remains visible, so claiming it explains the absent header would be incorrect.

## Matrix

Y = observed stated symptom. Missing content/fatal pages are not counted as a successful reproduction just because no navigation is visible.

|Case|HTTP|Dark reading|No header|Default serif|Blank gold CTA|No light sections|Match count|Screenshot / interpretation|
|---|---|---|---|---|---|---|---|---|
'''
for c in rows:
 s=c['owner_description_comparison'];text+='|'+c['case']+'|'+str(c['status'])+'|'+ '|'.join('Y' if s[k] else 'N' for k in ['dark_reading_layout','header_absent','default_serif_heading','blank_gold_CTA','no_light_reading_sections'])+'|'+str(c['matching_symptom_count'])+'/5|['+c['case']+'](screenshots/phase-29/'+c['case']+'.png). '+c['note']+'|\n'
text+='''
## Important distinctions

- (a)/(b) URL404/403 is not a failed server filesystem read. Current Germany never requests that CSS URL. Disk-css-missing separately models the actual unchecked read at visual-system.php:67.
- (c) HTTP font404 leaves embedded fonts intact. Disk-fonts-missing separately removes the two files read at visual-system.php:74. No-assets removes CSS, fonts and images together, explicitly a folder-level fault.
- (d) scenes false and config absent are separate tests: one leaves styling intact, the other fails required include. (e) required visual-system.php has no silent fallback; missing is fatal. A native unreadable require is expected fatal too, but no native ACL engine was available, so unreadability itself is not falsely claimed tested.
- (f) Actual Phase13 and actual predesign frozen HTML are used, not fabricated lookalikes or another page. Old cached HTML may lack current content or keep a readable CTA/header. These do not exactly match. A cache that captured an already asset-broken render could preserve that same failure; this is an additional cache state, not an independent font/CSS URL fault.
- (g) Both interpretations tested: PHP-only changed set in a clean folder fails for an unchanged required helper; overlay onto the actual Phase13 tree retains old helper files but omits new JSON/assets. New content data/API files, not just changed PHP, are mandatory.
- (h) Under /preview, __DIR__ disk reads still work and Germany data fonts remain correct. Root-absolute images break. Other templates using static HTTP fonts would lose those fonts. Wrong root URL404 is not a successful reproduction of the reported rendered Germany page.
- (i)7.4 fails on a real PHP8 function dependency, not merely newer syntax.8.0/8.1/8.5 all render the design. These are WASM versions, not Hostinger/native deployment certification.

## Mechanism of the strongest combined reproduction

PHP still runs ilmera_visual_present: it moves the answer/CTA into the reading section and adds p25. The stylesheet read fails without an explicit guard; Google font links were already removed. Empty CSS loses light backgrounds and the higher-specificity CTA override. includes/destination-page.php:113 gives article-body links the gold foreground, matching the button's gold background when the visual override at assets/css/visual-system.css:96 is absent. Empty embedded font data falls back to the installed serif. Missing header.php is only include, not require, at destination-page.php:119, so it warns and omits navigation while keeping the page/footer alive. The new content is therefore not evidence the entire deploy payload arrived.

Read actualHeadingFonts in the JSON rather than trusting computed font-family: the CSS family name can still say Cormorant while the real glyph font is DejaVu Serif. The control uses a custom Cormorant face. First-party absolute logo URLs are mapped to the same fault root, never fetched from live production. Other external providers are aborted; cached predesign font conclusions are limited accordingly.
'''
(R/'reports/phase-29-fault-comparison.md').write_text(text)
print('22 cases,24 screenshots; only explicit missing-assets+missing-header combination matches all5 description symptoms')
