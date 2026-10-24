# Content release deploy payload

**Draft candidate only.** Requested release branch/PR cannot be created in this fixed-branch session. Do not upload the current arena/design checkout. Build from164d6de plus phase-26-team-only.patch in a separately authorized content-release checkout. No deployment performed.

## Exact upload allowlist

117 files. Preserve these relative paths and dotfiles. No other file is authorized by this manifest. SHA256/size for every file: phase-26-payload-manifest.json.

```text
.htaccess
404.php
about.php
all-pages.php
assets/images/fawazbh-192.webp
assets/images/fawazbh-384.webp
assets/images/fawazbh.webp
assets/images/ilmera.logo.navy.png
assets/images/ilmera.logo.png
assets/images/ilmera.png
assets/images/ilmera.white.png
assets/images/jabirkj.png
assets/images/jabirkj.webp
assets/images/zaheer.png
assets/images/zaheer.webp
blog/cost-of-studying-abroad-for-indian-students.php
blog/documents-needed-to-study-abroad-from-india.php
blog/how-to-choose-study-abroad-consultant-karnataka.php
blog/index.php
blog/italy-dsu-scholarship-eligibility.php
blog/scholarships-for-indian-students-study-abroad.php
blog/study-abroad-counselling-from-coorg.php
blog/study-abroad-with-academic-backlogs.php
blog/study-in-germany-free-aps-certificate.php
contact.php
data/.htaccess
data/answer-map.json
data/entity.json
data/payment-disclosure.json
data/proof.php
data/seo-map.json
data/service-scope.json
data/team.json
destinations/.htaccess
destinations/czech-republic.php
destinations/gcc.php
destinations/germany.php
destinations/italy.php
destinations/latvia.php
destinations/lithuania.php
destinations/russia.php
destinations/slovakia.php
destinations/uk.php
favicon.ico
google10fa7a4178242a1f.html
includes/.htaccess
includes/breadcrumbs.php
includes/destination-data.php
includes/destination-page.php
includes/entity.php
includes/footer.php
includes/header.php
includes/links.php
includes/payment-disclosure.php
includes/place-data.php
includes/place-page.php
includes/posts.php
includes/proof.php
includes/service-scope.php
includes/site-presentation.php
includes/sitemap-data.php
index.php
llms-full.txt
llms.txt
phase14-article-review.json
phase14-location-review.json
phase14-source-review.json
places/.htaccess
places/belagavi.php
places/bengaluru.php
places/chikkamagaluru.php
places/gonikoppal.php
places/hassan.php
places/karnataka.php
places/kodagu.php
places/kushalnagar.php
places/madikeri.php
places/mangaluru.php
places/mysuru.php
places/ponnampet.php
places/shivamogga.php
places/siddapura.php
places/somwarpet.php
places/udupi-manipal.php
places/virajpet.php
privacy-policy.php
robots.txt
services.php
sitemap.php
sitemap.xml
study-abroad-consultants-in-karnataka.php
study-abroad-consultants-in-kodagu.php
study-abroad-counselling-belagavi.php
study-abroad-counselling-bengaluru.php
study-abroad-counselling-chikkamagaluru.php
study-abroad-counselling-gonikoppal.php
study-abroad-counselling-hassan.php
study-abroad-counselling-kushalnagar.php
study-abroad-counselling-madikeri.php
study-abroad-counselling-mangaluru.php
study-abroad-counselling-mysuru.php
study-abroad-counselling-ponnampet.php
study-abroad-counselling-shivamogga.php
study-abroad-counselling-siddapura.php
study-abroad-counselling-somwarpet.php
study-abroad-counselling-udupi-manipal.php
study-abroad-counselling-virajpet.php
study-in-czech-republic.php
study-in-gcc.php
study-in-germany.php
study-in-italy.php
study-in-latvia.php
study-in-lithuania.php
study-in-russia.php
study-in-slovakia.php
study-in-uk.php
terms.php
```

## Exclusions and required exceptions

Do not upload reports/, tools/, any .md file, Git metadata, caches/__pycache__/, fixtures, node_modules, test runtimes, screenshots, CSV files, strategy/audit exports, backups/logs, or Phase25 design files/fonts/scenes. Do not upload the release reports or manifest themselves. Do not upload a private certificate.

**Do not blanket-exclude all internal JSON.** These exact runtime inputs MUST ship while remaining blocked to direct HTTP access:

- `phase14-source-review.json`
- `phase14-location-review.json`
- `phase14-article-review.json`
- `data/answer-map.json`
- `data/entity.json`
- `data/payment-disclosure.json`
- `data/seo-map.json`
- `data/service-scope.json`
- `data/team.json`

The three phase14 review journals are not disposable exports: includes/destination-data.php, includes/place-data.php and includes/posts.php read them to validate publication/fact/file-hash gates. Omitting them can silently remove reviewed routes from discovery or alter rendering. This fixes the proposed exclusion list without moving files or changing publication code. Other phase14 JSON (including phase14-validation.json), all CSV and other unlisted JSON are excluded. Six data/ JSON files are likewise runtime entity/team/answer/SEO/service/payment inputs, not upload-optional notes.

## Required protected runtime folders

- `data/` with data/.htaccess: PHP/JSON business/runtime projections.
- `includes/` with includes/.htaccess: server-side shared code.
- `destinations/` with destinations/.htaccess: nine source records, including held records.
- `places/` with places/.htaccess: seventeen source records.

Root .htaccess must also ship: its FilesMatch blocks the root phase14 JSON journals, notes/scripts/audits and Git namespace. Server-side PHP must still be able to read these files. reports/ and tools/ are excluded entirely; their historical deny files are not required payload. Native AllowOverride/Require/rewrite behavior must be checked on hosting before acceptance. A folder deny is not a file-permissions proof.

## Clean-folder completeness proof

Copied only these117 files into /home/user/phase26/payload, with no symlinks or copy of the candidate source tree. Started a separate fresh PHP8.5 WASM instance rooted there on8083. Compared all43 rendered routes byte-for-byte with the isolated source candidate: all matched, including all38 published routes and held/404 outputs. Fetched sitemap.xml (38 URLs), robots.txt, both LLM files, verification HTML and all12 first-party assets and compared actual bytes. Protected runtime-input probes return403/404 under the explicit local mirror. Evidence: phase-26-payload-checks.json.

Original external fonts/CDN scripts and contact service remain external dependencies, unchanged from164d6de. All first-party assets are proved locally; CDN availability, native MIME/cache/CSP, actual .htaccess enforcement and contact delivery are not proved. The adapter does not execute Apache directives. The temporary folder/archive is outside Git and not committed. Do not confuse local completeness with permission to deploy.
