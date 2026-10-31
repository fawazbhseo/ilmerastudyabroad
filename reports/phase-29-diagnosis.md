# Phase29 diagnosis: current content, missing design on Germany

2026-10-26. Report and diagnostic tools only. Starting/current runtime HEAD: `56914f22c1f9a8dd8eb16a05099faffbc2ff1f34`. Existing session branch only. No public site edit, hosting access, deployment, merge, new branch or new PR. The owner reports the live symptoms; no original screenshot or live response headers were available here. Network access is restricted to development/package hosts, so the live origin was not fetched. Rankings below are evidence-based hypotheses, not a claimed inspection of Hostinger.

## Finding in one paragraph

The strongest explanation is an **incomplete or unreadable on-disk design upload**, with an additional missing header include for the absent navigation. The stylesheet is not a browser stylesheet link: PHP reads `assets/css/visual-system.css` at `includes/visual-system.php:67` and inserts its contents inline. Germany also embeds two disk font files at line74. Missing disk CSS leaves current content, dark reading sections and an empty-looking gold CTA; missing disk fonts adds the default serif. The non-required `includes/header.php` include at `includes/destination-page.php:119` can independently fail with only a warning and omit the header. That explicit combination reproduced all five described visual symptoms while preserving current copy, online-only wording, footer and HTTP200. **No tested single fault reproduced all five. No pixel-exact live match is claimed without the original screenshot.**

The four references are deliberately excluded from this overlay (`visual-system.php:22`) and retain their original design implementation. Their continuing to look normal does not prove the new shared design files were uploaded correctly.

## Ranked causes, evidence, conditional fixes and owner confirmations

### 1. Missing, empty, wrong-case/wrong-location or PHP-unreadable disk assets; plus missing/unreadable header include

**Most likely family.** Tasks1-2 prove every required file is in the130-entry ZIP and matches its manifest hash, but that does not prove the host has it. Task3 `disk-css-missing` reproduces dark reading sections and a gold-on-gold CTA. `disk-fonts-missing` gives actual fallback serif glyphs. `no-assets` matches four of five symptoms; the header text and hamburger remain, so that single folder fault must not be called an exact match. `header-missing` removes navigation without breaking the whole page. The explicit `no-assets-header-missing` combination matches all five supplied visual features with200/current content/footer. Screenshots: [control](screenshots/phase-29/normal-top.png), [combined fault](screenshots/phase-29/no-assets-header-missing-top.png), [full combined page](screenshots/phase-29/no-assets-header-missing.png). Missing files were tested; native unreadable/zero-byte variants are inferred equivalent read/decode failures, not falsely claimed separately tested.

**Exact conditional fix, NOT APPLIED:** in the actual domain document root, re-upload verified payload bytes to:

- `public_html/assets/css/visual-system.css`
- `public_html/assets/fonts/outfit-latin.woff2`
- `public_html/assets/fonts/cormorant-garamond-latin.woff2`
- `public_html/includes/header.php`

Also restore the complete payload `assets/fonts/` and `assets/images/` contents for the other templates/logo. Use the existing130-file allowlist, not PHP-only or the entire repository. Preserve directory structure and case; no wrapper folder. Confirm PHP can read these files and traverse their parent directories under the actual hosting account. Do not use world-writable777 or remove the includes/data HTTP privacy denies. Purge cached HTML after correction, because the CSS/fonts are embedded at render time. This is a recommendation to the owner, not an action performed here.

**Owner confirms:** exact live files and hashes against phase-27-payload-manifest.json, PHP error log for the line67/74 reads and header include, then all five owner-sheet URL results and Germany's visible menu, Cormorant headings, light sections and readable CTA. An HTTP403 alone does not prove a PHP filesystem read is denied. A200 font download alone does not prove the PHP path is correct.

### 2. Cached HTML generated while design assets/header were absent, or a mixed stale PHP/HTML cache

**Plausible persistence mechanism.** All design CSS and Germany fonts are inside HTML, with no asset version query. Replacing disk files does not update already cached HTML. Task3 used actual end-Phase13 HTML and actual frozen predesign Germany HTML with current files. Neither reproduces all five: Phase13 lacks the current answer/CTA content; predesign still has a header and readable CTA. Thus ordinary old HTML cache alone is not established as the complete explanation. A cache containing an earlier already-broken render can preserve precisely that failure; that state was not independently obtained from the host.

**Exact conditional fix, NOT APPLIED:** after verifying the files in cause1, purge Hostinger Cache Manager and any enabled Hostinger CDN cache, then load a new private window. If correct files plus a fresh uncached request still emit old PHP markup, ask Hostinger to invalidate OPcache/restart the relevant PHP worker safely. No cache setting or PHP worker was changed here.

**Owner confirms:** whether the newly fetched HTML has `<style id="ilmera-visual-system">`, substantial shared rules such as `body.p25 .article-body`, nonempty `data:font/woff2;base64,` fonts and the expected header markup. A marker alone is insufficient: the missing-assets fixture still emits an almost-empty overlay marker. If the design returns only after HTML purge, retain that observation as cache evidence.

### 3. Mixed/old presentation PHP or non-default constants/buffer/canonical behavior

**Possible, less consistent than missing disk CSS.** Required `site-presentation.php`, `visual-system.php` and `visual-config.php` must match the payload together. Default template groups include all rebuilt families; an explicitly predefined empty group list was tested and produces an old layout, but not the blank CTA or absent header. False `ILMERA_SCENES_ENABLED` was tested and does not disable the design. Actual missing visual-system/config produces fatal500, not a complete200 old-looking page. Task2 lists every early return, body/head literal transform, buffer guard and exact canonical match; no hostname/HTTPS/PHP-version switch or error-suppressed visual include exists.

**Exact conditional fix, NOT APPLIED:** restore payload versions of `includes/site-presentation.php`, `includes/visual-system.php` and `includes/visual-config.php` if their hashes differ. Confirm `visual-config.php:9` contains `['destination','place','article','blog','legal','utility']`; identify and remove or correct an unintended earlier definition only if the host/bootstrap actually supplies one. Do not toggle the scene switch as a design repair. Confirm canonical remains `https://ilmerastudyabroad.com/study-in-germany`, literal body/head insertion points are intact and a foreign bootstrap does not predefine presentation buffer flags. No such host bootstrap has been observed, so no invented file/line is prescribed for it.

**Owner confirms:** emitted body has `p25 p25-destination`, inline shared CSS is nonempty and matches expected rules, constants/defaults are not overridden, and PHP includes all come from this domain's correct document root. Header-only failure is independently cause1, not proof all includes are missing.

### 4. Untracked hosting/security rules, filesystem ACLs, CSP or MIME configuration

**Unverified, conditional.** Task4 audits all8 payload .htaccess files. None blocks ordinary CSS/fonts; there is no assets/.htaccess and no universal unknown-file-to-PHP rule. The fonts child rule adds MIME/cache only. Private child denies are scoped to their own HTTP directories, not /assets or PHP filesystem reads. No native Apache/LiteSpeed engine or simulator is installed, so actual host behavior remains unverified. An extra parent/global rule or CSP may exist outside Git. No such rule or live response header has been obtained.

**Exact conditional fix, NOT APPLIED:** if host logs establish a filesystem read denial, restore normal owner-readable file/directory permissions, not HTTP privacy bypasses. For a proven extra catch-all rewriting static files, the host should exempt existing files/directories before that offending rule; the shipped root already rewrites only when a matching `.php` file exists. For proven wrong MIME, restore `text/css` for CSS and `font/woff2` for fonts. For a proven CSP rejection, have the host authorize the actual emitted inline style/script using an approved nonce/hash policy and allow the required `font-src 'self' data:` sources without weakening unrelated restrictions. The actual unknown host rule cannot honestly be named by file/line here. Do not add speculative rewrite exceptions, blanket unsafe-inline or remove private-directory denies.

**Owner confirms:** actual HTTP status, Content-Type, relevant CSP errors/headers, native error log and matching on-disk file. A CSS/font HTTP403 by itself is not enough: Task3 HTTP403/404 controls still show Germany's correct inline design. MIME errors on the diagnostic CSS URL alone cannot remove its server-inlined contents.

### 5. Subfolder deployment or browser asset URL failure alone

**Tested but does not match the complete Germany report.** A full payload under /preview breaks root-absolute logo/static-font URLs; root Germany URL becomes404. But __DIR__ disk CSS/data-font reads still succeed on the subfolder page, leaving Germany's light reading sections, custom headings and readable CTA. Other templates using static font URLs are more affected. HTTP-only CSS404/403 or all font404 likewise do not remove Germany's inline design.

**Exact conditional fix, NOT APPLIED:** publish extracted root contents into the domain's actual public_html document root, with `/assets/` and `/includes/` alongside the page entry files, rather than editing every asset URL or placing the archive folder below the document root. Confirm direct root URLs from the owner sheet. If genuine intended subfolder hosting is required, that is a separate authorized URL/layout change, not applied here.

### 6. PHP-only partial deployment, missing required PHP/config or unsupported PHP version

**Real failures, weak match to the reported complete page.** Task3 tests changed-since-Phase13 PHP only in an empty folder: fatal missing unchanged breadcrumbs.php. Overlaying changed PHP onto the real end-Phase13 tree but omitting assets/new JSON yields dark/fallback fonts but lacks the current direct-answer CTA. Germany7.4 fails on `str_ends_with()` at `includes/destination-data.php:140` (also used in `includes/posts.php:126`), not a silent theme-only fallback.8.0/8.1/8.5 render the correct design locally. These version tests are not native-host compatibility/security certification; old8.x test versions are not recommendations for continued hosting support.

**Exact conditional fix, NOT APPLIED:** restore every130-file payload member, including the9 JSON runtime exceptions and unchanged helpers, not only changed PHP. Restore missing required visual/config includes. If the actual log identifies an unsupported PHP API, select a currently host-supported maintained PHP8.x version and run normal owner smoke checks. Do not add ad-hoc polyfills or edit publication evidence here.

**Owner confirms:**200 versus500 response, actual PHP version, exact error message and full payload count/hashes. A blank500 is not the owner's current-content screenshot.

## Decisive evidence and limits

- Task1: [runtime inventory](phase-29-runtime-inventory.md), JSON hashes and exact source read/include sites. All130 current/ZIP/manifest paths and hashes match, including the CSS,9 fonts and all8 upload policies. No generated hero-still JS/image dependency was omitted.
- Task2: [rendered design loading](phase-29-design-loading.md) and four verbatim tag extracts, including full data fonts and CSS. No standalone CSS link exists on the four tested rebuilt pages.
- Task3: [fault matrix](phase-29-fault-comparison.md),22 cases/24 screenshots, actual glyph font measurements, CTA foreground/background equality and captured PHP errors. Only the explicitly combined missing-assets/header case matches all five textual symptoms. The supplied screenshot itself was not available for exact image comparison.
- Task4: [server rules](phase-29-server-rules.md), all8 policy line/hash records and static path reasoning. Native execution is unverified. No hosting setting has been changed.
- [One-page owner sheet](live-design-check.md): five exact URLs, expected results, re-upload targets and cache/private-window steps. Offline print check:1 A4 page.
- [Duplicate paragraph audit](phase-29-duplicate-paragraphs.md):23 exact normalized duplicates out of38 published routes,0 additional near matches under explicit thresholds. Six destinations including Germany and17 place pages. This is a separate deterministic injection/original-introduction duplication, not a cache/design-loading fault. The proposed narrow guarded de-duplication must preserve source citations and publication gates; no paragraph was removed.

## Owner URL checks

1. https://ilmerastudyabroad.com/assets/css/visual-system.css
2. https://ilmerastudyabroad.com/assets/fonts/outfit-latin.woff2
3. https://ilmerastudyabroad.com/assets/fonts/cormorant-garamond-latin.woff2
4. https://ilmerastudyabroad.com/assets/images/ilmera.logo.png
5. https://ilmerastudyabroad.com/study-in-germany

The top hypothesis is confirmed only by owner/server evidence, not by the packaged ZIP alone. Do not apply a speculative code fix before checking file placement/readability, header presence and fresh HTML. Existing performance, privacy, source/business/certificate, native hosting, contact/backup and held-page blockers remain open. No fourth performance session or acceptance claim.

## Scope and handoff

phase-29-scope-proof.json verifies every preexisting file except the two append-only root logs is byte-identical to56914f2, all130 manifest hashes and deployment ZIP unchanged, new paths restricted to reports/tools, line endings preserved and no new em dashes. phase-29-changed-files.md lists every changed file. Commits/pushes are task checkpoints on the existing session branch. Final pushed hash and PR1 checkpoint are supplied in the final response, not self-referentially inserted into this report. No merge or deployment.
