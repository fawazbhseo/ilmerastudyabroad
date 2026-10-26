# Phase29 how rendered pages load the design

Clean130-file ZIP root, PHP8.5; no live-origin request. Every actual link, style, script and preload tag belonging to presentation is copied verbatim, without base64 elision, in the four linked .html extracts below. JSON-LD is excluded as schema, not design. Canonical tags are included because the PHP design classifier consumes them. Inline base template, header and footer styles/scripts are included too. The copies are evidence in private reports, never website files.

## Exact tag ledger

### /study-in-germany

Exact tags: [study-in-germany.html](phase-29-design-tags/study-in-germany.html). Full-render SHA256 `02f0efffe1b450c849852e21476a3b822199d6c654a9fe41ef9e8fa648f8638f`.

|Tag|Role|URL/path|Version query|Bytes|
|---|---|---|---|---|
|1|canonical URL, consumed by PHP overlay route classifier, not a design asset|https://ilmerastudyabroad.com/study-in-germany; fully-qualified absolute|False|77|
|2|favicon/image browser request|/assets/images/ilmera.logo.png; root-absolute, same origin|False|73|
|3|base template inline styling|Inline; inline, no HTTP path|False|4745|
|4|PHP-read shared CSS and fonts, exact inline payload|Inline; inline, no HTTP path|False|59532|
|5|inline font visibility gate; Promise/FontFaceSet support,3000ms timeout|Inline; inline, no HTTP path|False|416|
|6|base template inline styling|Inline; inline, no HTTP path|False|3991|
|7|inline navigation/footer/scroll interaction; no external design JS file|Inline; inline, no HTTP path|False|1098|
|8|base template inline styling|Inline; inline, no HTTP path|False|2805|
|9|inline navigation/footer/scroll interaction; no external design JS file|Inline; inline, no HTTP path|False|188|

Actual PHP include trace: `/internal/shared/auto_prepend_file.php`, `/internal/eval.php`, `study-in-germany.php`, `includes/site-presentation.php`, `includes/visual-system.php`, `includes/visual-config.php`, `includes/entity.php`, `includes/service-scope.php`, `includes/proof.php`, `includes/payment-disclosure.php`, `includes/destination-page.php`, `includes/destination-data.php`, `includes/place-data.php`, `includes/breadcrumbs.php`, `includes/links.php`, `includes/posts.php`, `destinations/germany.php`, `includes/header.php`, `destinations/italy.php`, `destinations/uk.php`, `destinations/czech-republic.php`, `destinations/lithuania.php`, `destinations/latvia.php`, `destinations/slovakia.php`, `destinations/russia.php`, `destinations/gcc.php`, `includes/footer.php`, `places/belagavi.php`, `places/bengaluru.php`, `places/chikkamagaluru.php`, `places/gonikoppal.php`, `places/hassan.php`, `places/karnataka.php`, `places/kodagu.php`, `places/kushalnagar.php`, `places/madikeri.php`, `places/mangaluru.php`, `places/mysuru.php`, `places/ponnampet.php`, `places/shivamogga.php`, `places/siddapura.php`, `places/somwarpet.php`, `places/udupi-manipal.php`, `places/virajpet.php`.

### /study-abroad-counselling-mysuru

Exact tags: [study-abroad-counselling-mysuru.html](phase-29-design-tags/study-abroad-counselling-mysuru.html). Full-render SHA256 `57ea4123dc4517e64bdbe7c35dda1ba8ce79d446fb1e1942c5ccec9884119614`.

|Tag|Role|URL/path|Version query|Bytes|
|---|---|---|---|---|
|1|canonical URL, consumed by PHP overlay route classifier, not a design asset|https://ilmerastudyabroad.com/study-abroad-counselling-mysuru; fully-qualified absolute|False|92|
|2|favicon/image browser request|https://ilmerastudyabroad.com/assets/images/ilmera.logo.png; fully-qualified absolute|False|102|
|3|favicon/image browser request|https://ilmerastudyabroad.com/assets/images/ilmera.logo.png; fully-qualified absolute|False|111|
|4|favicon/image browser request|https://ilmerastudyabroad.com/assets/images/ilmera.logo.png; fully-qualified absolute|False|97|
|5|base template inline styling|Inline; inline, no HTTP path|False|4591|
|6|above-fold static font preload (not emitted on destination)|/assets/fonts/outfit-reference-300.woff2; root-absolute, same origin|False|108|
|7|above-fold static font preload (not emitted on destination)|/assets/fonts/cormorant-garamond-reference-700.woff2; root-absolute, same origin|False|120|
|8|PHP-read shared CSS and fonts, exact inline payload|Inline; inline, no HTTP path|False|23531|
|9|inline font visibility gate; Promise/FontFaceSet support,3000ms timeout|Inline; inline, no HTTP path|False|416|
|10|base template inline styling|Inline; inline, no HTTP path|False|3991|
|11|inline navigation/footer/scroll interaction; no external design JS file|Inline; inline, no HTTP path|False|1098|
|12|base template inline styling|Inline; inline, no HTTP path|False|2805|
|13|inline navigation/footer/scroll interaction; no external design JS file|Inline; inline, no HTTP path|False|256|

Actual PHP include trace: `/internal/shared/auto_prepend_file.php`, `/internal/eval.php`, `study-abroad-counselling-mysuru.php`, `includes/site-presentation.php`, `includes/visual-system.php`, `includes/visual-config.php`, `includes/entity.php`, `includes/service-scope.php`, `includes/proof.php`, `includes/payment-disclosure.php`, `includes/place-page.php`, `includes/place-data.php`, `includes/breadcrumbs.php`, `includes/links.php`, `includes/posts.php`, `includes/destination-data.php`, `places/mysuru.php`, `places/belagavi.php`, `places/bengaluru.php`, `places/chikkamagaluru.php`, `places/gonikoppal.php`, `places/hassan.php`, `places/karnataka.php`, `places/kodagu.php`, `places/kushalnagar.php`, `places/madikeri.php`, `places/mangaluru.php`, `places/ponnampet.php`, `places/shivamogga.php`, `places/siddapura.php`, `places/somwarpet.php`, `places/udupi-manipal.php`, `places/virajpet.php`, `includes/header.php`, `destinations/germany.php`, `destinations/italy.php`, `destinations/uk.php`, `destinations/czech-republic.php`, `destinations/lithuania.php`, `destinations/latvia.php`, `destinations/slovakia.php`, `destinations/russia.php`, `destinations/gcc.php`, `includes/footer.php`.

### /blog/how-to-choose-study-abroad-consultant-karnataka

Exact tags: [blog_how-to-choose-study-abroad-consultant-karnataka.html](phase-29-design-tags/blog_how-to-choose-study-abroad-consultant-karnataka.html). Full-render SHA256 `192fbb8d0462f267525f5d37084035533adf10361c074983cb13b9274b4bee4d`.

|Tag|Role|URL/path|Version query|Bytes|
|---|---|---|---|---|
|1|canonical URL, consumed by PHP overlay route classifier, not a design asset|https://ilmerastudyabroad.com/blog/how-to-choose-study-abroad-consultant-karnataka; fully-qualified absolute|False|112|
|2|base template inline styling|Inline; inline, no HTTP path|False|4267|
|3|above-fold static font preload (not emitted on destination)|/assets/fonts/outfit-reference-300.woff2; root-absolute, same origin|False|108|
|4|above-fold static font preload (not emitted on destination)|/assets/fonts/cormorant-garamond-reference-700.woff2; root-absolute, same origin|False|120|
|5|PHP-read shared CSS and fonts, exact inline payload|Inline; inline, no HTTP path|False|23531|
|6|inline font visibility gate; Promise/FontFaceSet support,3000ms timeout|Inline; inline, no HTTP path|False|416|
|7|base template inline styling|Inline; inline, no HTTP path|False|3991|
|8|inline navigation/footer/scroll interaction; no external design JS file|Inline; inline, no HTTP path|False|1098|
|9|base template inline styling|Inline; inline, no HTTP path|False|2805|

Actual PHP include trace: `/internal/shared/auto_prepend_file.php`, `/internal/eval.php`, `blog/how-to-choose-study-abroad-consultant-karnataka.php`, `includes/site-presentation.php`, `includes/visual-system.php`, `includes/visual-config.php`, `includes/entity.php`, `includes/service-scope.php`, `includes/proof.php`, `includes/payment-disclosure.php`, `includes/posts.php`, `includes/breadcrumbs.php`, `includes/links.php`, `includes/place-data.php`, `includes/destination-data.php`, `includes/header.php`, `includes/footer.php`, `destinations/germany.php`, `destinations/italy.php`, `destinations/uk.php`, `destinations/czech-republic.php`, `destinations/lithuania.php`, `destinations/latvia.php`, `destinations/slovakia.php`, `destinations/russia.php`, `destinations/gcc.php`, `places/belagavi.php`, `places/bengaluru.php`, `places/chikkamagaluru.php`, `places/gonikoppal.php`, `places/hassan.php`, `places/karnataka.php`, `places/kodagu.php`, `places/kushalnagar.php`, `places/madikeri.php`, `places/mangaluru.php`, `places/mysuru.php`, `places/ponnampet.php`, `places/shivamogga.php`, `places/siddapura.php`, `places/somwarpet.php`, `places/udupi-manipal.php`, `places/virajpet.php`.

### /blog/

Exact tags: [blog_.html](phase-29-design-tags/blog_.html). Full-render SHA256 `c679d79b00adb7092b328e505483d091560873f89ccc8d7987d3d03d697b877d`.

|Tag|Role|URL/path|Version query|Bytes|
|---|---|---|---|---|
|1|canonical URL, consumed by PHP overlay route classifier, not a design asset|https://ilmerastudyabroad.com/blog/; fully-qualified absolute|False|66|
|2|favicon/image browser request|https://ilmerastudyabroad.com/assets/images/ilmera.logo.png; fully-qualified absolute|False|102|
|3|favicon/image browser request|https://ilmerastudyabroad.com/assets/images/ilmera.logo.png; fully-qualified absolute|False|111|
|4|favicon/image browser request|https://ilmerastudyabroad.com/assets/images/ilmera.logo.png; fully-qualified absolute|False|97|
|5|base template inline styling|Inline; inline, no HTTP path|False|3675|
|6|above-fold static font preload (not emitted on destination)|/assets/fonts/outfit-reference-300.woff2; root-absolute, same origin|False|108|
|7|above-fold static font preload (not emitted on destination)|/assets/fonts/cormorant-garamond-reference-700.woff2; root-absolute, same origin|False|120|
|8|PHP-read shared CSS and fonts, exact inline payload|Inline; inline, no HTTP path|False|23531|
|9|inline font visibility gate; Promise/FontFaceSet support,3000ms timeout|Inline; inline, no HTTP path|False|416|
|10|base template inline styling|Inline; inline, no HTTP path|False|3991|
|11|inline navigation/footer/scroll interaction; no external design JS file|Inline; inline, no HTTP path|False|1098|
|12|base template inline styling|Inline; inline, no HTTP path|False|2805|

Actual PHP include trace: `/internal/shared/auto_prepend_file.php`, `/internal/eval.php`, `blog/index.php`, `includes/site-presentation.php`, `includes/visual-system.php`, `includes/visual-config.php`, `includes/entity.php`, `includes/service-scope.php`, `includes/proof.php`, `includes/payment-disclosure.php`, `includes/breadcrumbs.php`, `includes/links.php`, `includes/posts.php`, `includes/place-data.php`, `includes/destination-data.php`, `includes/header.php`, `includes/footer.php`, `destinations/germany.php`, `destinations/italy.php`, `destinations/uk.php`, `destinations/czech-republic.php`, `destinations/lithuania.php`, `destinations/latvia.php`, `destinations/slovakia.php`, `destinations/russia.php`, `destinations/gcc.php`, `places/belagavi.php`, `places/bengaluru.php`, `places/chikkamagaluru.php`, `places/gonikoppal.php`, `places/hassan.php`, `places/karnataka.php`, `places/kodagu.php`, `places/kushalnagar.php`, `places/madikeri.php`, `places/mangaluru.php`, `places/mysuru.php`, `places/ponnampet.php`, `places/shivamogga.php`, `places/siddapura.php`, `places/somwarpet.php`, `places/udupi-manipal.php`, `places/virajpet.php`.

## Conditions, fallbacks and source lines

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
