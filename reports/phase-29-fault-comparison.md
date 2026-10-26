# Phase29 mobile fault reproduction

390x844 viewport, device scale1, current committed130-file ZIP extracted into a new empty folder. Clean normal PHP VM has no original-checkout mount. Per-case filesystem faults exist only in disposable VM copies; HTTP faults are explicit response cases. All warnings captured with display_errors=0, to model production-style hidden warnings rather than convert every warning into an adapter500. Native filesystem permissions/Apache behavior are not simulated.22 cases,24 PNGs (full page each plus two viewport crops) under screenshots/phase-29/. No performance measurements or extra reliability lab.

**No original owner image was provided. We cannot claim pixel-exact live reproduction or a confirmed live root cause.** The explicitly labelled combination of missing assets/ plus missing includes/header.php matches all five textual symptoms and retains current online-only content/footer. No tested single fault matches all five. Missing the assets folder alone matches four; the nav text/hamburger remains visible, so claiming it explains the absent header would be incorrect.

## Matrix

Y = observed stated symptom. Missing content/fatal pages are not counted as a successful reproduction just because no navigation is visible.

|Case|HTTP|Dark reading|No header|Default serif|Blank gold CTA|No light sections|Match count|Screenshot / interpretation|
|---|---|---|---|---|---|---|---|---|
|http-css-404|200|N|N|N|N|N|0/5|[http-css-404](screenshots/phase-29/http-css-404.png). CSS diagnostic URL404 verified, but no browser stylesheet request: PHP inline CSS is unchanged.|
|http-css-403|200|N|N|N|N|N|0/5|[http-css-403](screenshots/phase-29/http-css-403.png). CSS diagnostic URL403 verified, but filesystem read is allowed: unchanged inline design.|
|http-fonts-404|200|N|N|N|N|N|0/5|[http-fonts-404](screenshots/phase-29/http-fonts-404.png). All HTTP font paths404. Germany uses data fonts, so headings still use Cormorant.|
|scenes-off|200|N|N|N|N|N|0/5|[scenes-off](screenshots/phase-29/scenes-off.png). False changes decoration only; destination hero was already plain. Design remains.|
|cached-phase13|200|Y|N|Y|N|Y|3/5|[cached-phase13](screenshots/phase-29/cached-phase13.png). Actual end-Phase13 HTML with current static files: old content/old styling, no current direct-answer CTA. External Google font requests aborted, not evidence live Google fonts fail.|
|cached-predesign|200|Y|N|Y|N|Y|3/5|[cached-predesign](screenshots/phase-29/cached-predesign.png). Actual frozen predesign Germany HTML with current assets: old dark layout, but header and CTA text visible. External Google fonts aborted, so default-serif observation is conditional on that external block.|
|changed-php-over-phase13|200|Y|N|Y|N|Y|3/5|[changed-php-over-phase13](screenshots/phase-29/changed-php-over-phase13.png). Actual Phase13 tree overlaid with changed PHP, assets removed. Required PHP now available but new JSON absent.200 dark/fallback fonts, no current direct-answer CTA. Not exact.|
|subfolder|200|N|N|N|N|N|0/5|[subfolder](screenshots/phase-29/subfolder.png). Whole payload under /preview; root-absolute image/font URLs break. Germany CSS and data fonts still inline and correct. Direct root Germany URL is404. Not the reported content-complete old look.|
|php-8.0|200|N|N|N|N|N|0/5|[php-8.0](screenshots/phase-29/php-8.0.png). PHP8.0 applies design successfully in local VM; not native-host certification.|
|php-8.1|200|N|N|N|N|N|0/5|[php-8.1](screenshots/phase-29/php-8.1.png). PHP8.1 applies design successfully in local VM; not native-host certification.|
|php-8.5|200|N|N|N|N|N|0/5|[php-8.5](screenshots/phase-29/php-8.5.png). PHP8.5 applies design successfully in local VM; not native-host certification.|
|disk-css-missing|200|Y|N|N|Y|Y|3/5|[disk-css-missing](screenshots/phase-29/disk-css-missing.png). Warning-only missing PHP-read CSS: dark reading sections and identical gold CTA foreground/background. Fonts still inline and header present.|
|disk-fonts-missing|200|N|N|Y|N|N|1/5|[disk-fonts-missing](screenshots/phase-29/disk-fonts-missing.png). Warning-only missing two disk font faces: actual fallback serif, but light sections and readable CTA/header remain.|
|no-assets|200|Y|N|Y|Y|Y|4/5|[no-assets](screenshots/phase-29/no-assets.png). All assets absent on disk: dark, fallback serif, blank-looking gold CTA and no light reading sections, but header text/hamburger remain. Four of five visual symptoms, not exact.|
|groups-disabled|200|Y|N|Y|N|Y|3/5|[groups-disabled](screenshots/phase-29/groups-disabled.png). Deliberately predefined empty template groups skips overlay. Dark layout, but header and CTA text remain. Not exact. Requires non-default config/bootstrap not present in payload.|
|normal|200|N|N|N|N|N|0/5|[normal](screenshots/phase-29/normal.png). Control: full130-file payload applies new design.|
|config-missing|500|N|Y|N|N|N|1/5|[config-missing](screenshots/phase-29/config-missing.png). Required config missing is fatal500, not an old-look complete page.|
|visual-missing|500|N|Y|N|N|N|1/5|[visual-missing](screenshots/phase-29/visual-missing.png). Required visual-system missing is fatal500, no silent include fallback.|
|changed-php-only|500|N|Y|N|N|N|1/5|[changed-php-only](screenshots/phase-29/changed-php-only.png). Changed-since-Phase13 PHP subset in empty folder misses unchanged breadcrumbs.php and fails500. No JSON/assets; not the complete current content screenshot.|
|php-7.4|500|N|Y|N|N|N|1/5|[php-7.4](screenshots/phase-29/php-7.4.png). Fatal undefined str_ends_with at includes/destination-data.php:140, also posts.php:126. PHP API compatibility issue, not styling-only fallback.|
|header-missing|200|N|Y|N|N|N|1/5|[header-missing](screenshots/phase-29/header-missing.png). Non-required header include missing: warning,200 current content with absent nav, but correct light sections/fonts/readable CTA.|
|no-assets-header-missing|200|Y|Y|Y|Y|Y|5/5|[no-assets-header-missing](screenshots/phase-29/no-assets-header-missing.png). Explicit COMBINATION: missing assets folder plus missing includes/header.php.200 retains current copy, online-only disclosure and footer, but matches all five stated visual symptoms. Not a pixel-exact owner screenshot comparison.|

## Important distinctions

- (a)/(b) URL404/403 is not a failed server filesystem read. Current Germany never requests that CSS URL. Disk-css-missing separately models the actual unchecked read at visual-system.php:67.
- (c) HTTP font404 leaves embedded fonts intact. Disk-fonts-missing separately removes the two files read at visual-system.php:74. No-assets removes CSS, fonts and images together, explicitly a folder-level fault.
- (d) scenes false and config absent are separate tests: one leaves styling intact, the other fails required include. (e) required visual-system.php has no silent fallback; missing is fatal. A native unreadable require is expected fatal too, but no native ACL engine was available, so unreadability itself is not falsely claimed tested.
- (f) Actual Phase13 and actual predesign frozen HTML are used, not fabricated lookalikes or another page. Old cached HTML may lack current content or keep a readable CTA/header. These do not exactly match. A cache that captured an already asset-broken render could preserve that same failure; this is an additional cache state, not an independent font/CSS URL fault.
- (g) Both interpretations tested: PHP-only changed set in a clean folder fails for an unchanged required helper; overlay onto the actual Phase13 tree retains old helper files but omits new JSON/assets. New content data/API files, not just changed PHP, are mandatory.
- (h) Under /preview, __DIR__ disk reads still work and Germany data fonts remain correct. Root-absolute images break. Other templates using static HTTP fonts would lose those fonts. Wrong root URL404 is not a successful reproduction of the reported rendered Germany page.
- (i)7.4 fails on a real PHP8 function dependency, not merely newer syntax.8.0/8.1/8.5 all render the design. These are WASM versions, not Hostinger/native deployment certification.

## Mechanism of the strongest combined reproduction

PHP still runs ilmera_visual_present: it moves the answer/CTA into the reading section and adds p25. The stylesheet read fails without an explicit guard; Google font links were already removed. Empty CSS loses light backgrounds and the higher-specificity CTA override. includes/destination-page.php:115 gives article-body links the gold foreground, matching the button's gold background when the visual override at assets/css/visual-system.css:94 is absent. Empty embedded font data falls back to the installed serif. Missing header.php is only include, not require, at destination-page.php:119, so it warns and omits navigation while keeping the page/footer alive. The new content is therefore not evidence the entire deploy payload arrived.

Read actualHeadingFonts in the JSON rather than trusting computed font-family: the CSS family name can still say Cormorant while the real glyph font is DejaVu Serif. The control uses a custom Cormorant face. First-party absolute logo URLs are mapped to the same fault root, never fetched from live production. Other external providers are aborted; cached predesign font conclusions are limited accordingly.
