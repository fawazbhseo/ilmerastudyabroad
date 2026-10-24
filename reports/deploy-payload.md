# Current full-branch deploy payload: Phase28 artifact, unchanged Phase27 runtime

**Replaces the stale117-file content-only list. This pack contains content phases14-26b AND Phase25 design. No deployment or owner acceptance performed.**

Source runtime commit: `a3d696f7942b2df5c76d660c2b9f3252881ce314` on `arena/48320ee5-ilmerastudyabroad`. Phase27 commits modify reports/tools/logs only, so runtime bytes remain this exact snapshot. Final documentation hash is reported in the Phase27 handoff, not falsely labelled as a new runtime build.

## Exact counts and identity

- **130 upload files**. Source snapshot has524 tracked files; **394 excluded tracked source files**. The final Phase27 file set adds23 internal paths: **417 total excluded tracked files out of547**; the130 upload files are unchanged. Exact final exclusions are in phase-27-excluded-files.json. Untracked caches, node_modules and Git internals are unbounded exclusions, not included in those counts.
- Per-file bytes/SHA256: [phase-27-payload-manifest.json](phase-27-payload-manifest.json). Every excluded source path/reason: [phase-27-excluded-files.json](phase-27-excluded-files.json). Neither report is uploaded.
- Offline reproducible export: `python3 tools/phase27/export.py --out /new/empty/temporary/folder --zip /new/artifact.zip`. This reads the pinned Git blobs, verifies every hash and refuses existing destinations. It does not deploy or regenerate site files.
- Historical Phase27 ZIP outside Git (superseded by the committed Phase28 download below): `/home/user/phase27/ilmera-phase27-a3d696f.zip`, 681792B, SHA256 `7c7fc3284b924df08b6c63c2ee27329d3b10298304b591679944a590b8f2fee4`. Its entries exactly match the manifest. Extract contents to the hosting root, not a wrapper folder; never upload the ZIP itself into the public folder.

## Phase28 downloadable repository artifact

Current-HEAD export: `releases/ilmera-deploy-850d0af.zip`,681792 bytes, SHA256 `31442c174e64b701a46db9bb935e88c85f0e201a4707297e70e9a3d06146d9d6`. Its130 entries match the unchanged upload manifest. The earlier external-only ZIP remains historical; use the committed artifact now. releases/ is excluded from all publication/export/discovery. Its deny rule is repository safety only, not a ninth upload policy. See phase-28-payload-proof.json for the fresh ZIP-extracted clean-folder proof with releases/ present in the repo.

## Mandatory runtime exceptions and privacy

Blanket internal-folder/JSON exclusions BREAK this application. Retain includes/, data/, destinations/, places/ PHP runtime and all nine JSON inputs below. PHP reads them on disk; no browser needs direct access. Do not move them without a separately tested path/layout change, which is out of scope here.

- `data/answer-map.json`
- `data/entity.json`
- `data/payment-disclosure.json`
- `data/seo-map.json`
- `data/service-scope.json`
- `data/team.json`
- `phase14-article-review.json`
- `phase14-location-review.json`
- `phase14-source-review.json`

The three root review journals gate approved publication/source/hash records. The six data JSON files drive canonical entity/team, answers, SEO and service/payment disclosures. `data/proof.php` is also mandatory. Dropping them can hide pages, remove disclosures or change structured data. The clean proof below verifies they were retained.

All8 payload .htaccess files are included unchanged. The ninth tracked policy, releases/.htaccess, protects the repository artifact folder and is excluded with that folder. Explicit safety exceptions to the reports/tools exclusion are **only reports/.htaccess and tools/.htaccess**, placed in otherwise empty directories. No report or tool content is uploaded. This reconciles the requirement to retain every .htaccess with excluding internal contents.

| Private scope | Protection to retain | Owner native check |
|---|---|---|
| Root review JSON/dotfiles/Markdown/CSV/Git | `.htaccess` |403/404, no contents; root rewrites still work |
| data/ | `data/.htaccess` |PHP readable, HTTP denied |
| includes/ | `includes/.htaccess` |PHP readable, HTTP denied |
| destinations/ | `destinations/.htaccess` |PHP arrays readable, HTTP denied |
| places/ | `places/.htaccess` |PHP arrays readable, HTTP denied |
| reports/ | `reports/.htaccess` only |No contents uploaded; HTTP denied |
| tools/ | `tools/.htaccess` only |No contents uploaded; HTTP denied |
| Public fonts, NOT private | `assets/fonts/.htaccess` |Font MIME/cache rules, not a directory deny |

All7 static reference weights AND2 variable faces are included: PHP reads the variable pair for destination data URIs. Include the shared visual CSS and its PHP helpers, genuine PNG/WebP portraits, both font OFL licences and favicon. The old1.5MB Fawaz original and unused alternate logos are excluded, with no rendered reference. Generated hero-still JS/images are disabled and unreferenced, so excluded. Procedural scenes use the unchanged external Three.js dependency, not a local still.

## Do not upload

Every file not in the exact allowlist. In particular: report/tool contents except their2 deny-only files; all Markdown including all.md/README/CHANGELOG/flagged items; all other phase*.json/internal JSON/CSV exports; Git metadata/credentials; runtime caches/__pycache__/.cache/node_modules; fixtures/test-only PHP/Python/JS; generated screenshots, evidence/snapshots, old archives/ZIPs and unused assets. **Exclude the entire releases/ folder, including its ZIP and deny .htaccess.** It is not a website route or sitemap entry. Keep backups outside web access. The9 runtime JSON exceptions above are intentional, not optional exports.

Never point public_html at an entire Git checkout. Git deployment must use a private checkout then publish only this allowlist, with no .git or other excluded files. If the host cannot filter, use manual upload of the pack. Replacing files does not delete old unlisted files: reconcile against the old backup and remove obsolete internal artifacts while access is disabled. No new public source/path design is introduced.

## Clean-folder proof

**PASS locally**, details: [phase-27-payload-proof.json](phase-27-payload-proof.json).

- Only130 listed files copied into a new empty temporary folder; no symlinks. Files and ZIP hash-match source.
- Fresh PHP8.5 WASM engine populated an isolated `/site` memory filesystem with ONLY that payload. No host filesystem mount; explicit probe cannot see the original checkout. Static HTTP also roots at the clean folder. No original-source fallback.
- All43 route outputs byte-identical to both repo HTTP renders and frozen repo snapshots:38 published,404 and4 held routes. **Zero differences**. This includes full design, current finance-only Zaheer, canonical Person/FAQ, published status and disclosures.
- `/sitemap.xml`, `/robots.txt`, `/llms.txt`, `/llms-full.txt`, verification HTML and20 asset/runtime/licence paths fetched byte-exact via GET and HEAD. Exactly38 unique sitemap entries, no APS/DSU/Czech/Russia route.
- All14 first-party assets referenced by rendered HTML/CSS, plus6 runtime/licence/default-browser dependencies, are present.9 font faces, visual stylesheet,7 image paths,2 licences and favicon make20 checked paths. Rooted source code reads CSS/variable-font files only within payload.
- Private runtime/root/report/tool/Git probes return local403 with no contents. This adapter manually mirrors the access policy: it DOES NOT execute .htaccess. Native Apache/LiteSpeed/AllowOverride/ACL/rewrite/ErrorDocument/cache/MIME/CSP and actual contact delivery/backup restore are NOT proved.

External assets remain external and unchanged: Google Fonts on the four references, GSAP/ScrollTrigger and Three.js on applicable pages. Their original URLs are recorded in the manifest; Google CSS may request further gstatic resources. They cannot be served from this folder without changing public code. Local first-party completeness is proved, not offline/CDN availability or live CSP/network timing. The contact provider also remains external. Owner must test these on the real host.

Raw search caveat: `free` substring hits are7 legacy held APS URL identifiers and2 existing `freely` words on Services, not prohibited standalone fee wording. No digital-marketer/tuition-free/co-founder hit in rendered routes. Exact inventory: phase-27-raw-wording-hits.json. Do not rename URLs or edit prose in this reports-only phase; owner must distinguish these known substrings from prohibited copy.

## Exact upload list (files, not whole unfiltered folders)

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

Phase28 direct GitHub download: https://raw.githubusercontent.com/fawazbhseo/ilmerastudyabroad/arena/48320ee5-ilmerastudyabroad/releases/ilmera-deploy-850d0af.zip
The branch-ref GitHub Contents API binary was fetched and matched all681792 bytes/SHA256. Direct raw-host fetching is outside this sandbox network allowlist.
