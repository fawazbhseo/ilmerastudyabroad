# Phase 24b public-file exposure audit

Assumption: repository root is live web root. Inventory covers every current non-page file, including ignored Python
caches, and every enclosing folder. Git internals are represented by a whole-
namespace denial/exclusion instead of enumerating or reading credentials. No certificate or private certificate field is added.

## Result and access-policy changes

Before: reports/ and tools/ already had directory denies. Root Markdown notes,
phase JSON/CSV exports and data/includes/internal-data folders lacked explicit
repository access protection. robots.txt is not an access-control mechanism.
The older local adapter overblocked some folders relative to native config,
so its old 403s were never treated as native proof.

After: Apache 2.4/LiteSpeed-compatible `Require all denied` files in reports/,
tools/, includes/, data/, destinations/ and places/. Existing report/tool rules
are unchanged. Root rewrite bytes remain an exact prefix: only deny directives
are appended. Root FilesMatch denies Markdown/scripts/logs/backups, phase JSON,
private CSV exports and dotfiles; RedirectMatch 403 denies accidental Git URLs.
The CSV/dotfile/Git/internal-array denies are conservative additions, not page
publication changes. No public page, asset, discovery or verification route is
denied intentionally. No existing rewrite is changed.

No browser-fetched data/ file was found: browser fetch/XHR/axios/getJSON and
src/href/action references were reviewed in public PHP/HTML/JS source. JSON
reads are PHP-side. Therefore the whole data/ folder is denied without a
browser exception. Includes remain PHP-readable internally; HTTP denies do
not prevent server-side includes.

## Native limitation and exact owner tests

**Native Apache/LiteSpeed enforcement: NOT VERIFIED.** The local PHP WASM
adapter does not parse .htaccess or emulate rewrite/authz modules. Separate
adapter denial/positive probes pass, but do not prove the hosting engine,
AllowOverride or LiteSpeed directive support/configuration. No live site was
changed or tested. FAIL live clearance until owner verifies the actual host.

Every exact deny URL appears in `phase-24b-live-url-checks.txt` and the JSON
inventory. GET each on the live host: expected **403 or 404 with no file
contents and no directory listing**. A 404 for an absent probe does not prove
a rule protects an existing file. A 200, leaked content, redirect exposing
content or a server error is a failed release check; restore the complete
backup/settings before proceeding. Existing note/JSON/script files and
folder probes are included, not only invented nonexistent paths.

Positive GET checks must return 200: every published route, sitemap.xml,
robots.txt, llms.txt, llms-full.txt, verification HTML, favicon and every site
asset. They are exercised locally, separately from native-rule validation.
Do not submit an enquiry as part of these probes; real delivery still needs
its own separately authorized verification.

## Owner deployment decision

**Do not upload internal folders, notes, tooling, reports, caches, exports or
Git metadata into the live hosting folder.** Required runtime includes/data/
destination/place files currently use repository-relative PHP paths. They
cannot simply be omitted without breaking the site. Approve and test a
non-public runtime layout/path configuration before relocating or omitting
those required files. This phase adds defense-in-depth denies under the
requested web-root assumption; it does not move runtime files or deploy.
Complete backup and all-file/settings restore readiness remain prerequisites.

## Complete file inventory

221 non-page files: 203 denied, 18 intentionally public. Exact machine-readable rows include prior block, new rule, full URL and expected result. No log/backup file was found; deny/probe coverage still exists for both extensions.

| File | Before | After / expected |
| --- | --- | --- |
| `.gitignore` | no repository access block | root FilesMatch deny; 403 or 404, no file contents |
| `.htaccess` | server normally protects this config; do not depend on that default | root FilesMatch deny; 403 or 404, no file contents |
| `CHANGELOG.md` | no repository access block | root FilesMatch deny; 403 or 404, no file contents |
| `README.md` | no repository access block | root FilesMatch deny; 403 or 404, no file contents |
| `assets/images/fawazbh-192.webp` | no repository access block | intentional public asset/discovery/verification resource; 200 (sitemap.php may canonical-redirect under existing native rewrite) |
| `assets/images/fawazbh-384.webp` | no repository access block | intentional public asset/discovery/verification resource; 200 (sitemap.php may canonical-redirect under existing native rewrite) |
| `assets/images/fawazbh.webp` | no repository access block | intentional public asset/discovery/verification resource; 200 (sitemap.php may canonical-redirect under existing native rewrite) |
| `assets/images/ilmera.logo.navy.png` | no repository access block | intentional public asset/discovery/verification resource; 200 (sitemap.php may canonical-redirect under existing native rewrite) |
| `assets/images/ilmera.logo.png` | no repository access block | intentional public asset/discovery/verification resource; 200 (sitemap.php may canonical-redirect under existing native rewrite) |
| `assets/images/ilmera.png` | no repository access block | intentional public asset/discovery/verification resource; 200 (sitemap.php may canonical-redirect under existing native rewrite) |
| `assets/images/ilmera.white.png` | no repository access block | intentional public asset/discovery/verification resource; 200 (sitemap.php may canonical-redirect under existing native rewrite) |
| `assets/images/jabirkj.png` | no repository access block | intentional public asset/discovery/verification resource; 200 (sitemap.php may canonical-redirect under existing native rewrite) |
| `assets/images/jabirkj.webp` | no repository access block | intentional public asset/discovery/verification resource; 200 (sitemap.php may canonical-redirect under existing native rewrite) |
| `assets/images/zaheer.png` | no repository access block | intentional public asset/discovery/verification resource; 200 (sitemap.php may canonical-redirect under existing native rewrite) |
| `assets/images/zaheer.webp` | no repository access block | intentional public asset/discovery/verification resource; 200 (sitemap.php may canonical-redirect under existing native rewrite) |
| `data/.htaccess` | no repository access block | data/.htaccess: Require all denied; 403 or 404, no file contents |
| `data/answer-map.json` | no repository access block | data/.htaccess: Require all denied; 403 or 404, no file contents |
| `data/entity.json` | no repository access block | data/.htaccess: Require all denied; 403 or 404, no file contents |
| `data/payment-disclosure.json` | no repository access block | data/.htaccess: Require all denied; 403 or 404, no file contents |
| `data/proof.php` | no repository access block | data/.htaccess: Require all denied; 403 or 404, no file contents |
| `data/seo-map.json` | no repository access block | data/.htaccess: Require all denied; 403 or 404, no file contents |
| `data/service-scope.json` | no repository access block | data/.htaccess: Require all denied; 403 or 404, no file contents |
| `data/team.json` | no repository access block | data/.htaccess: Require all denied; 403 or 404, no file contents |
| `destinations-facts-template.csv` | no repository access block | root FilesMatch deny; 403 or 404, no file contents |
| `destinations/.htaccess` | no repository access block | destinations/.htaccess: Require all denied; 403 or 404, no file contents |
| `destinations/czech-republic.php` | no repository access block | destinations/.htaccess: Require all denied; 403 or 404, no file contents |
| `destinations/gcc.php` | no repository access block | destinations/.htaccess: Require all denied; 403 or 404, no file contents |
| `destinations/germany.php` | no repository access block | destinations/.htaccess: Require all denied; 403 or 404, no file contents |
| `destinations/italy.php` | no repository access block | destinations/.htaccess: Require all denied; 403 or 404, no file contents |
| `destinations/latvia.php` | no repository access block | destinations/.htaccess: Require all denied; 403 or 404, no file contents |
| `destinations/lithuania.php` | no repository access block | destinations/.htaccess: Require all denied; 403 or 404, no file contents |
| `destinations/russia.php` | no repository access block | destinations/.htaccess: Require all denied; 403 or 404, no file contents |
| `destinations/slovakia.php` | no repository access block | destinations/.htaccess: Require all denied; 403 or 404, no file contents |
| `destinations/uk.php` | no repository access block | destinations/.htaccess: Require all denied; 403 or 404, no file contents |
| `favicon.ico` | no repository access block | intentional public asset/discovery/verification resource; 200 (sitemap.php may canonical-redirect under existing native rewrite) |
| `flagged-items-for-verification.md` | no repository access block | root FilesMatch deny; 403 or 404, no file contents |
| `google10fa7a4178242a1f.html` | no repository access block | intentional public asset/discovery/verification resource; 200 (sitemap.php may canonical-redirect under existing native rewrite) |
| `includes/.htaccess` | no repository access block | includes/.htaccess: Require all denied; 403 or 404, no file contents |
| `includes/breadcrumbs.php` | no repository access block | includes/.htaccess: Require all denied; 403 or 404, no file contents |
| `includes/destination-data.php` | no repository access block | includes/.htaccess: Require all denied; 403 or 404, no file contents |
| `includes/destination-page.php` | no repository access block | includes/.htaccess: Require all denied; 403 or 404, no file contents |
| `includes/entity.php` | no repository access block | includes/.htaccess: Require all denied; 403 or 404, no file contents |
| `includes/footer.php` | no repository access block | includes/.htaccess: Require all denied; 403 or 404, no file contents |
| `includes/header.php` | no repository access block | includes/.htaccess: Require all denied; 403 or 404, no file contents |
| `includes/links.php` | no repository access block | includes/.htaccess: Require all denied; 403 or 404, no file contents |
| `includes/payment-disclosure.php` | no repository access block | includes/.htaccess: Require all denied; 403 or 404, no file contents |
| `includes/place-data.php` | no repository access block | includes/.htaccess: Require all denied; 403 or 404, no file contents |
| `includes/place-page.php` | no repository access block | includes/.htaccess: Require all denied; 403 or 404, no file contents |
| `includes/posts.php` | no repository access block | includes/.htaccess: Require all denied; 403 or 404, no file contents |
| `includes/proof.php` | no repository access block | includes/.htaccess: Require all denied; 403 or 404, no file contents |
| `includes/service-scope.php` | no repository access block | includes/.htaccess: Require all denied; 403 or 404, no file contents |
| `includes/site-presentation.php` | no repository access block | includes/.htaccess: Require all denied; 403 or 404, no file contents |
| `includes/sitemap-data.php` | no repository access block | includes/.htaccess: Require all denied; 403 or 404, no file contents |
| `llms-full.txt` | no repository access block | intentional public asset/discovery/verification resource; 200 (sitemap.php may canonical-redirect under existing native rewrite) |
| `llms.txt` | no repository access block | intentional public asset/discovery/verification resource; 200 (sitemap.php may canonical-redirect under existing native rewrite) |
| `phase14-article-review.json` | no repository access block | root FilesMatch deny; 403 or 404, no file contents |
| `phase14-audit-resolution.csv` | no repository access block | root FilesMatch deny; 403 or 404, no file contents |
| `phase14-location-review.json` | no repository access block | root FilesMatch deny; 403 or 404, no file contents |
| `phase14-publication-report.md` | no repository access block | root FilesMatch deny; 403 or 404, no file contents |
| `phase14-source-review.json` | no repository access block | root FilesMatch deny; 403 or 404, no file contents |
| `phase14-validation.json` | no repository access block | root FilesMatch deny; 403 or 404, no file contents |
| `places-facts-template.csv` | no repository access block | root FilesMatch deny; 403 or 404, no file contents |
| `places/.htaccess` | no repository access block | places/.htaccess: Require all denied; 403 or 404, no file contents |
| `places/belagavi.php` | no repository access block | places/.htaccess: Require all denied; 403 or 404, no file contents |
| `places/bengaluru.php` | no repository access block | places/.htaccess: Require all denied; 403 or 404, no file contents |
| `places/chikkamagaluru.php` | no repository access block | places/.htaccess: Require all denied; 403 or 404, no file contents |
| `places/gonikoppal.php` | no repository access block | places/.htaccess: Require all denied; 403 or 404, no file contents |
| `places/hassan.php` | no repository access block | places/.htaccess: Require all denied; 403 or 404, no file contents |
| `places/karnataka.php` | no repository access block | places/.htaccess: Require all denied; 403 or 404, no file contents |
| `places/kodagu.php` | no repository access block | places/.htaccess: Require all denied; 403 or 404, no file contents |
| `places/kushalnagar.php` | no repository access block | places/.htaccess: Require all denied; 403 or 404, no file contents |
| `places/madikeri.php` | no repository access block | places/.htaccess: Require all denied; 403 or 404, no file contents |
| `places/mangaluru.php` | no repository access block | places/.htaccess: Require all denied; 403 or 404, no file contents |
| `places/mysuru.php` | no repository access block | places/.htaccess: Require all denied; 403 or 404, no file contents |
| `places/ponnampet.php` | no repository access block | places/.htaccess: Require all denied; 403 or 404, no file contents |
| `places/shivamogga.php` | no repository access block | places/.htaccess: Require all denied; 403 or 404, no file contents |
| `places/siddapura.php` | no repository access block | places/.htaccess: Require all denied; 403 or 404, no file contents |
| `places/somwarpet.php` | no repository access block | places/.htaccess: Require all denied; 403 or 404, no file contents |
| `places/udupi-manipal.php` | no repository access block | places/.htaccess: Require all denied; 403 or 404, no file contents |
| `places/virajpet.php` | no repository access block | places/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/.htaccess` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/keyword-map.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/measurement-plan.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/off-page-plan.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/owner-inputs-needed.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/owner-questions.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-15-handoff.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-16-checks.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-16-citations.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-16-release-check.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-17-checks.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-17-source-opens.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-17-task-1-lines.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-17-verification.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-18-checks.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-18-llm-pages.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-18-release-check.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-18-strict-check.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-18-task-1-lines.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-19-checks.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-19-cycles.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-19-guide-review.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-19-on-page-changes.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-19-provisional-keyword-map.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-19-provisional-prompt-map.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-19-provisional-strategy-conflicts.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-19-release-check.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-19-technical-audit.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-19-technical.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-20-checks.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-20-cycles.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-20-map.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-20-on-page-review.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-20-progress.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-20-prompt-coverage.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-20-recommendations.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-20-release-check.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-22-checks.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-22-cycles.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-22-map.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-22-progress.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-22-release-check.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-22-scope-scan.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-23-checks.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-23-cycles.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-23-map.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-23-progress.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-23-registration-check.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-23-release-check.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-23-scan.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-23-team-inventory.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-24-checks.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-24-cycles.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-24-image-check.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-24-progress.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-24-registration-check.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-24-release-check.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-24-render-inventory.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-24b-bio-edits.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-24b-checks.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-24b-cycles.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-24b-exposure-audit.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-24b-exposure-audit.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-24b-live-url-checks.txt` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-24b-portfolio-check.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-24b-portrait-check.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-24b-progress.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/phase-24b-render-inventory.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/post-deploy-checklist.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/prompt-map.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/proof-slots.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/strategy-doc-conflicts.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/strategy-doc-research.json` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `reports/strategy-doc-summary.md` | reports/tools directory Require all denied | reports/.htaccess: Require all denied; 403 or 404, no file contents |
| `robots.txt` | no repository access block | intentional public asset/discovery/verification resource; 200 (sitemap.php may canonical-redirect under existing native rewrite) |
| `sitemap.php` | no repository access block | intentional public asset/discovery/verification resource; 200 (sitemap.php may canonical-redirect under existing native rewrite) |
| `sitemap.xml` | no repository access block | intentional public asset/discovery/verification resource; 200 (sitemap.php may canonical-redirect under existing native rewrite) |
| `tools/.htaccess` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/README.md` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/__pycache__/build_llms_directory.cpython-311.pyc` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/__pycache__/check_cycle_consistency.cpython-311.pyc` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/__pycache__/check_discovery.cpython-311.pyc` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/__pycache__/check_italy_claims.cpython-311.pyc` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/__pycache__/check_location_content.cpython-311.pyc` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/__pycache__/check_phase20.cpython-311.pyc` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/__pycache__/check_phase24.cpython-311.pyc` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/__pycache__/published_citations.cpython-311.pyc` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/__pycache__/team_bio_policy.cpython-311.pyc` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/blocked-names.txt` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/build-sitemap.php` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/build_llms_directory.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/check_cycle_consistency.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/check_destination_sources.php` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/check_discovery.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/check_italy_claims.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/check_location_content.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/check_phase19.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/check_phase20.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/check_phase20_handoff.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/check_phase22.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/check_phase23.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/check_phase24.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/check_phase24b.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/check_place_contact.php` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/check_place_publication.php` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/check_publication_review.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/check_technical_seo.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase20/README.md` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase20/browser.cjs` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase20/build_maps.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase20/run.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase20/server.cjs` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase22/build_prompt_map.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase22/run.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase23/browser.cjs` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase23/build_prompt_map.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase23/run.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase24/browser.cjs` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase24/build_portraits.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase24/run.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase24/server.cjs` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase24b/__pycache__/approved.cpython-311.pyc` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase24b/__pycache__/exposure.cpython-311.pyc` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase24b/approved.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase24b/browser.cjs` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase24b/exposure.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase24b/run.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/phase24b/server.cjs` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/published_citations.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/team_bio_policy.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/test_citations.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/test_discovery.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/test_italy_claims.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/test_llm_directory.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/test_llm_policy.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/test_presence.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/test_proof.php` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/test_public_exposure.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/test_strategy_schema.php` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/test_team_bio_policy.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |
| `tools/test_wording.py` | reports/tools directory Require all denied | tools/.htaccess: Require all denied; 403 or 404, no file contents |

## Every folder

- `assets/`: no folder deny intended; public page/asset namespace.
- `assets/images/`: no folder deny intended; public page/asset namespace.
- `blog/`: no folder deny intended; public page/asset namespace.
- `data/`: data/.htaccess; 403 or 404, no listing or file contents.
- `destinations/`: destinations/.htaccess; 403 or 404, no listing or file contents.
- `includes/`: includes/.htaccess; 403 or 404, no listing or file contents.
- `places/`: places/.htaccess; 403 or 404, no listing or file contents.
- `reports/`: reports/.htaccess; 403 or 404, no listing or file contents.
- `tools/`: tools/.htaccess; 403 or 404, no listing or file contents.
- `tools/__pycache__/`: tools/.htaccess; 403 or 404, no listing or file contents.
- `tools/phase20/`: tools/.htaccess; 403 or 404, no listing or file contents.
- `tools/phase22/`: tools/.htaccess; 403 or 404, no listing or file contents.
- `tools/phase23/`: tools/.htaccess; 403 or 404, no listing or file contents.
- `tools/phase24/`: tools/.htaccess; 403 or 404, no listing or file contents.
- `tools/phase24b/`: tools/.htaccess; 403 or 404, no listing or file contents.
- `tools/phase24b/__pycache__/`: tools/.htaccess; 403 or 404, no listing or file contents.
- `.git/ (never deploy)`: root RedirectMatch 403; never upload metadata; 403 or 404, no listing or file contents.

## Exact live denial URLs

Each must return 403 or 404 without file contents/listing.

```text
https://ilmerastudyabroad.com/.git/
https://ilmerastudyabroad.com/.git/HEAD
https://ilmerastudyabroad.com/.gitignore
https://ilmerastudyabroad.com/.htaccess
https://ilmerastudyabroad.com/CHANGELOG.md
https://ilmerastudyabroad.com/README.md
https://ilmerastudyabroad.com/data/
https://ilmerastudyabroad.com/data/.htaccess
https://ilmerastudyabroad.com/data/answer-map.json
https://ilmerastudyabroad.com/data/entity.json
https://ilmerastudyabroad.com/data/payment-disclosure.json
https://ilmerastudyabroad.com/data/proof.php
https://ilmerastudyabroad.com/data/seo-map.json
https://ilmerastudyabroad.com/data/service-scope.json
https://ilmerastudyabroad.com/data/team.json
https://ilmerastudyabroad.com/destinations-facts-template.csv
https://ilmerastudyabroad.com/destinations/
https://ilmerastudyabroad.com/destinations/.htaccess
https://ilmerastudyabroad.com/destinations/czech-republic.php
https://ilmerastudyabroad.com/destinations/gcc.php
https://ilmerastudyabroad.com/destinations/germany.php
https://ilmerastudyabroad.com/destinations/italy.php
https://ilmerastudyabroad.com/destinations/latvia.php
https://ilmerastudyabroad.com/destinations/lithuania.php
https://ilmerastudyabroad.com/destinations/russia.php
https://ilmerastudyabroad.com/destinations/slovakia.php
https://ilmerastudyabroad.com/destinations/uk.php
https://ilmerastudyabroad.com/flagged-items-for-verification.md
https://ilmerastudyabroad.com/includes/
https://ilmerastudyabroad.com/includes/.htaccess
https://ilmerastudyabroad.com/includes/breadcrumbs.php
https://ilmerastudyabroad.com/includes/destination-data.php
https://ilmerastudyabroad.com/includes/destination-page.php
https://ilmerastudyabroad.com/includes/entity.php
https://ilmerastudyabroad.com/includes/footer.php
https://ilmerastudyabroad.com/includes/header.php
https://ilmerastudyabroad.com/includes/links.php
https://ilmerastudyabroad.com/includes/payment-disclosure.php
https://ilmerastudyabroad.com/includes/place-data.php
https://ilmerastudyabroad.com/includes/place-page.php
https://ilmerastudyabroad.com/includes/posts.php
https://ilmerastudyabroad.com/includes/proof.php
https://ilmerastudyabroad.com/includes/service-scope.php
https://ilmerastudyabroad.com/includes/site-presentation.php
https://ilmerastudyabroad.com/includes/sitemap-data.php
https://ilmerastudyabroad.com/phase14-article-review.json
https://ilmerastudyabroad.com/phase14-audit-resolution.csv
https://ilmerastudyabroad.com/phase14-location-review.json
https://ilmerastudyabroad.com/phase14-publication-report.md
https://ilmerastudyabroad.com/phase14-source-review.json
https://ilmerastudyabroad.com/phase14-validation.json
https://ilmerastudyabroad.com/phase24b-access-probe.bak
https://ilmerastudyabroad.com/phase24b-access-probe.cjs
https://ilmerastudyabroad.com/phase24b-access-probe.json
https://ilmerastudyabroad.com/phase24b-access-probe.log
https://ilmerastudyabroad.com/phase24b-access-probe.py
https://ilmerastudyabroad.com/places-facts-template.csv
https://ilmerastudyabroad.com/places/
https://ilmerastudyabroad.com/places/.htaccess
https://ilmerastudyabroad.com/places/belagavi.php
https://ilmerastudyabroad.com/places/bengaluru.php
https://ilmerastudyabroad.com/places/chikkamagaluru.php
https://ilmerastudyabroad.com/places/gonikoppal.php
https://ilmerastudyabroad.com/places/hassan.php
https://ilmerastudyabroad.com/places/karnataka.php
https://ilmerastudyabroad.com/places/kodagu.php
https://ilmerastudyabroad.com/places/kushalnagar.php
https://ilmerastudyabroad.com/places/madikeri.php
https://ilmerastudyabroad.com/places/mangaluru.php
https://ilmerastudyabroad.com/places/mysuru.php
https://ilmerastudyabroad.com/places/ponnampet.php
https://ilmerastudyabroad.com/places/shivamogga.php
https://ilmerastudyabroad.com/places/siddapura.php
https://ilmerastudyabroad.com/places/somwarpet.php
https://ilmerastudyabroad.com/places/udupi-manipal.php
https://ilmerastudyabroad.com/places/virajpet.php
https://ilmerastudyabroad.com/reports/
https://ilmerastudyabroad.com/reports/.htaccess
https://ilmerastudyabroad.com/reports/keyword-map.md
https://ilmerastudyabroad.com/reports/measurement-plan.md
https://ilmerastudyabroad.com/reports/off-page-plan.md
https://ilmerastudyabroad.com/reports/owner-inputs-needed.md
https://ilmerastudyabroad.com/reports/owner-questions.md
https://ilmerastudyabroad.com/reports/phase-15-handoff.md
https://ilmerastudyabroad.com/reports/phase-16-checks.json
https://ilmerastudyabroad.com/reports/phase-16-citations.json
https://ilmerastudyabroad.com/reports/phase-16-release-check.md
https://ilmerastudyabroad.com/reports/phase-17-checks.json
https://ilmerastudyabroad.com/reports/phase-17-source-opens.json
https://ilmerastudyabroad.com/reports/phase-17-task-1-lines.md
https://ilmerastudyabroad.com/reports/phase-17-verification.md
https://ilmerastudyabroad.com/reports/phase-18-checks.json
https://ilmerastudyabroad.com/reports/phase-18-llm-pages.json
https://ilmerastudyabroad.com/reports/phase-18-release-check.md
https://ilmerastudyabroad.com/reports/phase-18-strict-check.md
https://ilmerastudyabroad.com/reports/phase-18-task-1-lines.md
https://ilmerastudyabroad.com/reports/phase-19-checks.json
https://ilmerastudyabroad.com/reports/phase-19-cycles.md
https://ilmerastudyabroad.com/reports/phase-19-guide-review.md
https://ilmerastudyabroad.com/reports/phase-19-on-page-changes.md
https://ilmerastudyabroad.com/reports/phase-19-provisional-keyword-map.md
https://ilmerastudyabroad.com/reports/phase-19-provisional-prompt-map.md
https://ilmerastudyabroad.com/reports/phase-19-provisional-strategy-conflicts.md
https://ilmerastudyabroad.com/reports/phase-19-release-check.md
https://ilmerastudyabroad.com/reports/phase-19-technical-audit.md
https://ilmerastudyabroad.com/reports/phase-19-technical.json
https://ilmerastudyabroad.com/reports/phase-20-checks.json
https://ilmerastudyabroad.com/reports/phase-20-cycles.md
https://ilmerastudyabroad.com/reports/phase-20-map.json
https://ilmerastudyabroad.com/reports/phase-20-on-page-review.md
https://ilmerastudyabroad.com/reports/phase-20-progress.md
https://ilmerastudyabroad.com/reports/phase-20-prompt-coverage.md
https://ilmerastudyabroad.com/reports/phase-20-recommendations.json
https://ilmerastudyabroad.com/reports/phase-20-release-check.md
https://ilmerastudyabroad.com/reports/phase-22-checks.json
https://ilmerastudyabroad.com/reports/phase-22-cycles.md
https://ilmerastudyabroad.com/reports/phase-22-map.json
https://ilmerastudyabroad.com/reports/phase-22-progress.md
https://ilmerastudyabroad.com/reports/phase-22-release-check.md
https://ilmerastudyabroad.com/reports/phase-22-scope-scan.md
https://ilmerastudyabroad.com/reports/phase-23-checks.json
https://ilmerastudyabroad.com/reports/phase-23-cycles.md
https://ilmerastudyabroad.com/reports/phase-23-map.json
https://ilmerastudyabroad.com/reports/phase-23-progress.md
https://ilmerastudyabroad.com/reports/phase-23-registration-check.md
https://ilmerastudyabroad.com/reports/phase-23-release-check.md
https://ilmerastudyabroad.com/reports/phase-23-scan.md
https://ilmerastudyabroad.com/reports/phase-23-team-inventory.json
https://ilmerastudyabroad.com/reports/phase-24-checks.json
https://ilmerastudyabroad.com/reports/phase-24-cycles.md
https://ilmerastudyabroad.com/reports/phase-24-image-check.json
https://ilmerastudyabroad.com/reports/phase-24-progress.md
https://ilmerastudyabroad.com/reports/phase-24-registration-check.md
https://ilmerastudyabroad.com/reports/phase-24-release-check.md
https://ilmerastudyabroad.com/reports/phase-24-render-inventory.json
https://ilmerastudyabroad.com/reports/phase-24b-bio-edits.md
https://ilmerastudyabroad.com/reports/phase-24b-checks.json
https://ilmerastudyabroad.com/reports/phase-24b-cycles.md
https://ilmerastudyabroad.com/reports/phase-24b-exposure-audit.json
https://ilmerastudyabroad.com/reports/phase-24b-exposure-audit.md
https://ilmerastudyabroad.com/reports/phase-24b-live-url-checks.txt
https://ilmerastudyabroad.com/reports/phase-24b-portfolio-check.md
https://ilmerastudyabroad.com/reports/phase-24b-portrait-check.json
https://ilmerastudyabroad.com/reports/phase-24b-progress.md
https://ilmerastudyabroad.com/reports/phase-24b-render-inventory.json
https://ilmerastudyabroad.com/reports/post-deploy-checklist.md
https://ilmerastudyabroad.com/reports/prompt-map.md
https://ilmerastudyabroad.com/reports/proof-slots.md
https://ilmerastudyabroad.com/reports/strategy-doc-conflicts.md
https://ilmerastudyabroad.com/reports/strategy-doc-research.json
https://ilmerastudyabroad.com/reports/strategy-doc-summary.md
https://ilmerastudyabroad.com/tools/
https://ilmerastudyabroad.com/tools/.htaccess
https://ilmerastudyabroad.com/tools/README.md
https://ilmerastudyabroad.com/tools/__pycache__/
https://ilmerastudyabroad.com/tools/__pycache__/build_llms_directory.cpython-311.pyc
https://ilmerastudyabroad.com/tools/__pycache__/check_cycle_consistency.cpython-311.pyc
https://ilmerastudyabroad.com/tools/__pycache__/check_discovery.cpython-311.pyc
https://ilmerastudyabroad.com/tools/__pycache__/check_italy_claims.cpython-311.pyc
https://ilmerastudyabroad.com/tools/__pycache__/check_location_content.cpython-311.pyc
https://ilmerastudyabroad.com/tools/__pycache__/check_phase20.cpython-311.pyc
https://ilmerastudyabroad.com/tools/__pycache__/check_phase24.cpython-311.pyc
https://ilmerastudyabroad.com/tools/__pycache__/published_citations.cpython-311.pyc
https://ilmerastudyabroad.com/tools/__pycache__/team_bio_policy.cpython-311.pyc
https://ilmerastudyabroad.com/tools/blocked-names.txt
https://ilmerastudyabroad.com/tools/build-sitemap.php
https://ilmerastudyabroad.com/tools/build_llms_directory.py
https://ilmerastudyabroad.com/tools/check_cycle_consistency.py
https://ilmerastudyabroad.com/tools/check_destination_sources.php
https://ilmerastudyabroad.com/tools/check_discovery.py
https://ilmerastudyabroad.com/tools/check_italy_claims.py
https://ilmerastudyabroad.com/tools/check_location_content.py
https://ilmerastudyabroad.com/tools/check_phase19.py
https://ilmerastudyabroad.com/tools/check_phase20.py
https://ilmerastudyabroad.com/tools/check_phase20_handoff.py
https://ilmerastudyabroad.com/tools/check_phase22.py
https://ilmerastudyabroad.com/tools/check_phase23.py
https://ilmerastudyabroad.com/tools/check_phase24.py
https://ilmerastudyabroad.com/tools/check_phase24b.py
https://ilmerastudyabroad.com/tools/check_place_contact.php
https://ilmerastudyabroad.com/tools/check_place_publication.php
https://ilmerastudyabroad.com/tools/check_publication_review.py
https://ilmerastudyabroad.com/tools/check_technical_seo.py
https://ilmerastudyabroad.com/tools/phase20/
https://ilmerastudyabroad.com/tools/phase20/README.md
https://ilmerastudyabroad.com/tools/phase20/browser.cjs
https://ilmerastudyabroad.com/tools/phase20/build_maps.py
https://ilmerastudyabroad.com/tools/phase20/run.py
https://ilmerastudyabroad.com/tools/phase20/server.cjs
https://ilmerastudyabroad.com/tools/phase22/
https://ilmerastudyabroad.com/tools/phase22/build_prompt_map.py
https://ilmerastudyabroad.com/tools/phase22/run.py
https://ilmerastudyabroad.com/tools/phase23/
https://ilmerastudyabroad.com/tools/phase23/browser.cjs
https://ilmerastudyabroad.com/tools/phase23/build_prompt_map.py
https://ilmerastudyabroad.com/tools/phase23/run.py
https://ilmerastudyabroad.com/tools/phase24/
https://ilmerastudyabroad.com/tools/phase24/browser.cjs
https://ilmerastudyabroad.com/tools/phase24/build_portraits.py
https://ilmerastudyabroad.com/tools/phase24/run.py
https://ilmerastudyabroad.com/tools/phase24/server.cjs
https://ilmerastudyabroad.com/tools/phase24b/
https://ilmerastudyabroad.com/tools/phase24b/__pycache__/
https://ilmerastudyabroad.com/tools/phase24b/__pycache__/approved.cpython-311.pyc
https://ilmerastudyabroad.com/tools/phase24b/__pycache__/exposure.cpython-311.pyc
https://ilmerastudyabroad.com/tools/phase24b/approved.py
https://ilmerastudyabroad.com/tools/phase24b/browser.cjs
https://ilmerastudyabroad.com/tools/phase24b/exposure.py
https://ilmerastudyabroad.com/tools/phase24b/run.py
https://ilmerastudyabroad.com/tools/phase24b/server.cjs
https://ilmerastudyabroad.com/tools/published_citations.py
https://ilmerastudyabroad.com/tools/team_bio_policy.py
https://ilmerastudyabroad.com/tools/test_citations.py
https://ilmerastudyabroad.com/tools/test_discovery.py
https://ilmerastudyabroad.com/tools/test_italy_claims.py
https://ilmerastudyabroad.com/tools/test_llm_directory.py
https://ilmerastudyabroad.com/tools/test_llm_policy.py
https://ilmerastudyabroad.com/tools/test_presence.py
https://ilmerastudyabroad.com/tools/test_proof.php
https://ilmerastudyabroad.com/tools/test_public_exposure.py
https://ilmerastudyabroad.com/tools/test_strategy_schema.php
https://ilmerastudyabroad.com/tools/test_team_bio_policy.py
https://ilmerastudyabroad.com/tools/test_wording.py
```

## Exact positive live URLs

Each must return 200 with the expected public resource.

```text
https://ilmerastudyabroad.com/
https://ilmerastudyabroad.com/about
https://ilmerastudyabroad.com/all-pages
https://ilmerastudyabroad.com/assets/images/fawazbh-192.webp
https://ilmerastudyabroad.com/assets/images/fawazbh-384.webp
https://ilmerastudyabroad.com/assets/images/fawazbh.webp
https://ilmerastudyabroad.com/assets/images/ilmera.logo.navy.png
https://ilmerastudyabroad.com/assets/images/ilmera.logo.png
https://ilmerastudyabroad.com/assets/images/ilmera.png
https://ilmerastudyabroad.com/assets/images/ilmera.white.png
https://ilmerastudyabroad.com/assets/images/jabirkj.png
https://ilmerastudyabroad.com/assets/images/jabirkj.webp
https://ilmerastudyabroad.com/assets/images/zaheer.png
https://ilmerastudyabroad.com/assets/images/zaheer.webp
https://ilmerastudyabroad.com/blog/
https://ilmerastudyabroad.com/blog/cost-of-studying-abroad-for-indian-students
https://ilmerastudyabroad.com/blog/documents-needed-to-study-abroad-from-india
https://ilmerastudyabroad.com/blog/how-to-choose-study-abroad-consultant-karnataka
https://ilmerastudyabroad.com/blog/scholarships-for-indian-students-study-abroad
https://ilmerastudyabroad.com/blog/study-abroad-counselling-from-coorg
https://ilmerastudyabroad.com/blog/study-abroad-with-academic-backlogs
https://ilmerastudyabroad.com/contact
https://ilmerastudyabroad.com/favicon.ico
https://ilmerastudyabroad.com/google10fa7a4178242a1f.html
https://ilmerastudyabroad.com/llms-full.txt
https://ilmerastudyabroad.com/llms.txt
https://ilmerastudyabroad.com/privacy-policy
https://ilmerastudyabroad.com/robots.txt
https://ilmerastudyabroad.com/services
https://ilmerastudyabroad.com/sitemap.xml
https://ilmerastudyabroad.com/study-abroad-consultants-in-karnataka
https://ilmerastudyabroad.com/study-abroad-consultants-in-kodagu
https://ilmerastudyabroad.com/study-abroad-counselling-belagavi
https://ilmerastudyabroad.com/study-abroad-counselling-bengaluru
https://ilmerastudyabroad.com/study-abroad-counselling-chikkamagaluru
https://ilmerastudyabroad.com/study-abroad-counselling-gonikoppal
https://ilmerastudyabroad.com/study-abroad-counselling-hassan
https://ilmerastudyabroad.com/study-abroad-counselling-kushalnagar
https://ilmerastudyabroad.com/study-abroad-counselling-madikeri
https://ilmerastudyabroad.com/study-abroad-counselling-mangaluru
https://ilmerastudyabroad.com/study-abroad-counselling-mysuru
https://ilmerastudyabroad.com/study-abroad-counselling-ponnampet
https://ilmerastudyabroad.com/study-abroad-counselling-shivamogga
https://ilmerastudyabroad.com/study-abroad-counselling-siddapura
https://ilmerastudyabroad.com/study-abroad-counselling-somwarpet
https://ilmerastudyabroad.com/study-abroad-counselling-udupi-manipal
https://ilmerastudyabroad.com/study-abroad-counselling-virajpet
https://ilmerastudyabroad.com/study-in-gcc
https://ilmerastudyabroad.com/study-in-germany
https://ilmerastudyabroad.com/study-in-italy
https://ilmerastudyabroad.com/study-in-latvia
https://ilmerastudyabroad.com/study-in-lithuania
https://ilmerastudyabroad.com/study-in-slovakia
https://ilmerastudyabroad.com/study-in-uk
https://ilmerastudyabroad.com/terms
```

Local adapter results (not native engine results): `{"status": "PASS local adapter only", "denied_or_absent_probes": 223, "public_resources_200": 55, "site_assets_200": 12, "native_engine_rules_tested": false}`.
