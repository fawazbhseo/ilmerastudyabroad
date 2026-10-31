# Phase30 exact deployment payload

**Current pack:131 files, including temporary deploy-check.php. After the owner deletes that file,130 remain.** This replaces the old130-file Phase28 artifact for this release; do not use the old117-file content-only pack. No agent deployment or owner/native-host acceptance is performed here.

Runtime source commit: `f54e4cc746fe54cfd89c228d8cf88635864c7ccb`. The only public runtime differences from a3d696f are the exact shared duplicate-answer fix in includes/site-presentation.php and temporary deploy-check.php. CSS, font, image, visual-system/config, all original .htaccess, publication/status/canonical/heading/FAQ/schema/link data and discovery bytes remain unchanged. Subsequent report/release commits do not change this runtime snapshot.

## Downloadable ZIP

[Download ilmera-deploy-f54e4cc.zip](https://raw.githubusercontent.com/fawazbhseo/ilmerastudyabroad/arena/48320ee5-ilmerastudyabroad/releases/ilmera-deploy-f54e4cc.zip)

Repository path: `releases/ilmera-deploy-f54e4cc.zip`. Size: **690538 bytes**. SHA256: `6ce9d3c98638a1cd454fd662cfc1d3a899ef5743d81e05b1147987f3552af459`.

Existing tools/phase27/export.py reads source_commit Git blobs and verifies every manifest hash. Reproduction: `python3 tools/phase27/export.py --source-ref f54e4cc746fe54cfd89c228d8cf88635864c7ccb --out /new/empty/folder --zip /new/artifact.zip`. Destination must not exist. ZIP metadata may vary on rebuild; exact per-file bytes/hashes are the runtime identity. The committed ZIP has no wrapper folder, duplicates, unsafe paths, Markdown, Git data, releases/ content or report/tool contents except reports/.htaccess and tools/.htaccess. All8 original policies are included unchanged.

## Temporary owner checker

Root deploy-check.php is intentional temporary131st payload member, not a published discovery page. Long random sole query key, strict GET/query guard, expiry valid through2026-11-15 UTC and fail closed from2026-11-16 00:00UTC. Noindex/no-store on allowed and denied responses. Fixed-path existence/readability/size/hash table only; no filesystem enumeration, contents, .htaccess reads, environment/server-path display, file parameter or writes. Critical assets/includes/JSON hashes match this manifest. Other original files and the checker itself are existence-only, avoiding a circular self-hash; offline ZIP tooling verifies all131 hashes.

Owner URL/key and native .php canonical-redirect caveat: reports/live-self-check.md. **Delete deploy-check.php immediately after one use.** The code is intentionally excepted from ordinary public-exposure200 probes and tested separately for wrong/missing/extra/traversal/expired requests. It is absent from all sitemap/robots/LLM/internal links. This is not strong authentication for private data; source/report key copies are not a secret vault.

## Files that must remain on disk

All includes/, data/, destinations/, places/ PHP dependencies remain PHP-readable and HTTP-denied by their unchanged child policies. Do not remove them to repair design. Nine required JSON inputs:

- `data/answer-map.json`
- `data/entity.json`
- `data/payment-disclosure.json`
- `data/seo-map.json`
- `data/service-scope.json`
- `data/team.json`
- `phase14-article-review.json`
- `phase14-location-review.json`
- `phase14-source-review.json`

The shared CSS is read from assets/css/visual-system.css by PHP and inlined. Germany's two variable font files are read from disk and embedded; other rebuilt families also require all7 static reference font weights. Include both font OFL licences, all7 image paths and favicon. Current presentation scripts are inline; disabled hero-still assets are not dependencies. External reference Google Fonts/GSAP/Three.js URLs remain unchanged and require owner/network/CSP checks.

## Do not upload

Every path outside the131-entry allowlist. Entire releases/ excluded, including its ZIP and deny .htaccess. Never deploy the whole checkout, Git metadata, reports/tools contents, Markdown/CSV/internal JSON exports, caches or generated evidence. The only internal-folder payload exceptions are their two deny-only policies. Retaining reports/.htaccess is required to keep all8 policies; no report content is included. releases/.htaccess is repository safety, not a ninth upload policy.

The owner-requested manual workflow temporarily uploads the ZIP into public_html for extraction, then deletes it immediately. Do not leave the ZIP publicly reachable or store backups under web access. Extract directly in public_html, overwrite existing files, preserve hidden files, remove the uploaded ZIP, then clear HTML/CDN cache and run the checker. Overwrite does not remove obsolete old files; reconcile extras against the backup without deleting unrelated hosting files. Detailed owner steps: reports/post-deploy-checklist.md/PDF.

## Expected payload counts, before temporary checker deletion

|Folder|Files, including hidden policies/licences|
|---|---|
|root|46|
|assets/css|1|
|assets/fonts|12|
|assets/images|7|
|blog|9|
|data|8|
|destinations|10|
|includes|18|
|places|18|
|reports|1|
|tools|1|

Counts sum131. Root drops from46 to45 after deleting deploy-check.php. Existing hosting extras are not included in these pack counts. reports/ and tools/ each contain ONLY .htaccess, no report or tool content.

## Clean-folder and native limits

phase-30-clean-payload-proof.json records a new empty exported folder, isolated PHP memory filesystem with only131 files and no host/source fallback,43 byte-identical repo/pack renders (38 published plus404 and4 held),38 unique sitemap URLs, all static assets/discovery/verification GET+HEAD and protected temporary-checker tests. Local adapter mirrors policy but does not execute native .htaccess. Native ACL/rewrite/ErrorDocument/cache/MIME/CSP, live file permissions, contact delivery, backup restoration and owner speed acceptance remain unverified. No fourth performance lab session or speed certification.

## Exact upload allowlist

- `.htaccess`
- `404.php`
- `about.php`
- `all-pages.php`
- `assets/css/visual-system.css`
- `assets/fonts/.htaccess`
- `assets/fonts/cormorant-garamond-OFL.txt`
- `assets/fonts/cormorant-garamond-latin.woff2`
- `assets/fonts/cormorant-garamond-reference-400.woff2`
- `assets/fonts/cormorant-garamond-reference-700.woff2`
- `assets/fonts/outfit-OFL.txt`
- `assets/fonts/outfit-latin.woff2`
- `assets/fonts/outfit-reference-300.woff2`
- `assets/fonts/outfit-reference-400.woff2`
- `assets/fonts/outfit-reference-500.woff2`
- `assets/fonts/outfit-reference-600.woff2`
- `assets/fonts/outfit-reference-700.woff2`
- `assets/images/fawazbh-192.webp`
- `assets/images/fawazbh-384.webp`
- `assets/images/ilmera.logo.png`
- `assets/images/jabirkj.png`
- `assets/images/jabirkj.webp`
- `assets/images/zaheer.png`
- `assets/images/zaheer.webp`
- `blog/cost-of-studying-abroad-for-indian-students.php`
- `blog/documents-needed-to-study-abroad-from-india.php`
- `blog/how-to-choose-study-abroad-consultant-karnataka.php`
- `blog/index.php`
- `blog/italy-dsu-scholarship-eligibility.php`
- `blog/scholarships-for-indian-students-study-abroad.php`
- `blog/study-abroad-counselling-from-coorg.php`
- `blog/study-abroad-with-academic-backlogs.php`
- `blog/study-in-germany-free-aps-certificate.php`
- `contact.php`
- `data/.htaccess`
- `data/answer-map.json`
- `data/entity.json`
- `data/payment-disclosure.json`
- `data/proof.php`
- `data/seo-map.json`
- `data/service-scope.json`
- `data/team.json`
- `deploy-check.php` TEMPORARY, delete after use
- `destinations/.htaccess`
- `destinations/czech-republic.php`
- `destinations/gcc.php`
- `destinations/germany.php`
- `destinations/italy.php`
- `destinations/latvia.php`
- `destinations/lithuania.php`
- `destinations/russia.php`
- `destinations/slovakia.php`
- `destinations/uk.php`
- `favicon.ico`
- `google10fa7a4178242a1f.html`
- `includes/.htaccess`
- `includes/breadcrumbs.php`
- `includes/destination-data.php`
- `includes/destination-page.php`
- `includes/entity.php`
- `includes/footer.php`
- `includes/header.php`
- `includes/links.php`
- `includes/payment-disclosure.php`
- `includes/place-data.php`
- `includes/place-page.php`
- `includes/posts.php`
- `includes/proof.php`
- `includes/service-scope.php`
- `includes/site-presentation.php`
- `includes/sitemap-data.php`
- `includes/visual-config.php`
- `includes/visual-system.php`
- `index.php`
- `llms-full.txt`
- `llms.txt`
- `phase14-article-review.json`
- `phase14-location-review.json`
- `phase14-source-review.json`
- `places/.htaccess`
- `places/belagavi.php`
- `places/bengaluru.php`
- `places/chikkamagaluru.php`
- `places/gonikoppal.php`
- `places/hassan.php`
- `places/karnataka.php`
- `places/kodagu.php`
- `places/kushalnagar.php`
- `places/madikeri.php`
- `places/mangaluru.php`
- `places/mysuru.php`
- `places/ponnampet.php`
- `places/shivamogga.php`
- `places/siddapura.php`
- `places/somwarpet.php`
- `places/udupi-manipal.php`
- `places/virajpet.php`
- `privacy-policy.php`
- `reports/.htaccess`
- `robots.txt`
- `services.php`
- `sitemap.php`
- `sitemap.xml`
- `study-abroad-consultants-in-karnataka.php`
- `study-abroad-consultants-in-kodagu.php`
- `study-abroad-counselling-belagavi.php`
- `study-abroad-counselling-bengaluru.php`
- `study-abroad-counselling-chikkamagaluru.php`
- `study-abroad-counselling-gonikoppal.php`
- `study-abroad-counselling-hassan.php`
- `study-abroad-counselling-kushalnagar.php`
- `study-abroad-counselling-madikeri.php`
- `study-abroad-counselling-mangaluru.php`
- `study-abroad-counselling-mysuru.php`
- `study-abroad-counselling-ponnampet.php`
- `study-abroad-counselling-shivamogga.php`
- `study-abroad-counselling-siddapura.php`
- `study-abroad-counselling-somwarpet.php`
- `study-abroad-counselling-udupi-manipal.php`
- `study-abroad-counselling-virajpet.php`
- `study-in-czech-republic.php`
- `study-in-gcc.php`
- `study-in-germany.php`
- `study-in-italy.php`
- `study-in-latvia.php`
- `study-in-lithuania.php`
- `study-in-russia.php`
- `study-in-slovakia.php`
- `study-in-uk.php`
- `terms.php`
- `tools/.htaccess`
