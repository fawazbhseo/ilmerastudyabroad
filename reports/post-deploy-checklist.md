# Owner release checklist: Phase32c payload (no deployment)

No deployment or hosting change has been made. This owner checklist covers the 137-file payload built from source commit `065934a`; local tests do not certify the live host or speed. Use the exact ZIP and checksum below. Live checks are still required before owner acceptance.

## (a) Before deploying

Download ALL existing `public_html` files, including hidden files, root and child `.htaccess` files, and hosting/PHP settings. Store the backup outside web access, verify it opens, record the old file list, and confirm the restore procedure. Keep host-panel access and a rollback window ready.

Before upload, run PageSpeed Insights on mobile for these exact URLs. Save the date, PSI result URL and screenshot; use the same URLs and device settings after upload. If a page has no valid baseline, record that fact; never substitute a 404 or another page.

| Page | PSI result URL/date | LCP | TBT | CLS | Score | Transfer (B) | Existing blockers |
|---|---|---|---|---|---|---|---|
| Home `/` | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Services `/services` | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Germany `/study-in-germany` | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Mysuru `/study-abroad-counselling-mysuru` | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Choosing guide | ___ | ___ | ___ | ___ | ___ | ___ | ___ |

Choosing guide URL: `/blog/how-to-choose-study-abroad-consultant-karnataka`. Record transfer bytes and the exact render-blocking URL set from the PSI/Lighthouse report or browser network capture. A missing baseline remains unverified, not a pass.

## (b) Upload method

**Current package:** `ilmera-deploy-065934a.zip`, exactly 137 files, 833,237 bytes, SHA-256 `3c56cdf481f639f98c689a26af517454576fae6d9ec9237c9e145eb38dfa8b57`. [Download the raw ZIP from this branch](https://raw.githubusercontent.com/fawazbhseo/ilmerastudyabroad/arena/48320ee5-ilmerastudyabroad/releases/ilmera-deploy-065934a.zip). It has no wrapper directory. The manifest and exact allowlist are in `reports/phase-27-payload-manifest.json`; upload-scope details are in `reports/phase-32c-upload-scope.json`.

1. **Back up first.** Complete the backup in section (a); do not continue unless it can be opened and restored.
2. **Download and verify** the ZIP size and SHA-256 above on your computer.
3. **Extract on Hostinger.** In hPanel, open this site's File Manager and the domain's `public_html`. Upload the ZIP there, select it and choose Extract directly into `public_html`, overwriting matching files. Do not create a ZIP-named subfolder. Enable Show hidden files. Do not extract a repository `releases/` folder. The ZIP contains only the deny-only `reports/.htaccess` and `tools/.htaccess` policies in those two folders.
4. **Delete the uploaded ZIP from `public_html` immediately after extraction.** Keep the backup outside web access. Check the counts below.
5. **Clear caches.** In hPanel use this site's Cache Manager and Purge all. If Hostinger CDN or LiteSpeed/LSCache is enabled, purge it too. This PHP site need not have WordPress or the LiteSpeed plugin; do not install one. Open a fresh private/incognito window for tests.
6. **Run once** the [temporary live self-check](https://ilmerastudyabroad.com/deploy-check.php?key=596b2f06f047c76730364c34857c6b47d03b019b21f8818960752a42fe104d9f). Send a screenshot of ALL FILES OK or the FAIL list. It checks the fixed payload allowlist. It expires after 15 November 2026 UTC. Do not add URL parameters. This is not a speed or native-host acceptance.
7. **Delete `deploy-check.php` from `public_html` immediately after that one use.** Reopen its link and confirm 404. Never leave the temporary file online.
8. Continue with all page, privacy, font, contact and speed checks below. If anything fails, follow section (j), not speculative file deletion.

**Expected files after extraction:** count files, not folders, including hidden files and licences. Existing host extras may make counts larger; compare with the backup and ask before deleting unrelated files. Overwrite does not remove old unlisted files.

| Folder | Expected files |
|---|---:|
| `assets/css` | 1 |
| `assets/fonts` | 16 |
| `assets/images` | 9 |
| `includes` | 18 |
| `data` | 8 |
| `destinations` | 10 |
| `places` | 18 |
| `blog` | 9 |
| root `public_html` | 46 before checker removal; 45 afterward |
| `reports` | 1 hidden deny file only |
| `tools` | 1 hidden deny file only |

Counts sum to 137 before deleting `deploy-check.php`, then 136. The font folder has 13 WOFF2 files, two licences and one hidden policy. Eight payload `.htaccess` policies are included; `releases/.htaccess` is intentionally excluded. The legacy 720px still and unused helper are excluded. Do not delete host files absent from the ZIP without comparing the backup.

**Spot-check after extraction:** root `.htaccess`; `assets/css/visual-system.css`; the Outfit and Cormorant faces; `assets/images/hero-still-640.webp` and `hero-still-1440.webp`; `includes/visual-system.php`; `includes/visual-config.php`; `includes/site-presentation.php`; `includes/header.php`; `includes/footer.php`; `data/seo-map.json`; `data/answer-map.json`; and temporary `deploy-check.php`. The checker covers the full allowlist and detailed critical hashes; this is not a manual 137-file audit.

## (c) Open on mobile and desktop

Use the 43-route inventory in `reports/phase-25-baseline-renders.json` for a route/status sweep, including expected non-indexable routes. Then visually smoke-test Home, Services, About, Contact, `/blog/`, Germany, Mysuru, the choosing guide and `/404`; also try an invented URL and confirm HTTP 404 rather than soft 200.

- **Home:** navigation/photos work; three even-height team cards, exact bios below.
- **About:** same cards; biography FAQs open; Udyam number UDYAM-KR-18-0023330 and business-registration-only/no-authority-endorsement caveat.
- **Services:** student charge ₹3 lakh to ₹15 lakh, university fees separate, university-payment disclosure, written policy terms not yet published.
- **Contact:** same disclosure and Udyam/caveat; working form and existing contact links.
- **/blog/:** published article cards load. **Choosing-consultant article:** readable guide, author image, FAQs and disclosure.
- **Germany:** plain navy hero, readable sourced guide/FAQs. **Mysuru:** gradient hero, light reading areas, unique local guide/FAQs. Neither has missing fonts/images. Mysuru and the chosen article remain on the plain-palette hero; no hero still is expected on those two routes.
- **/404:** Page Not Found, noindex, shortened footer. Verify the host error-page route as well as an invented URL.

Jabir: Jabir KJ is the Founder of ILMERA Study Abroad. He is responsible for university research, admissions and application guidance.

Zaheer: Zaheer KJ is the Chief Financial Officer of ILMERA Study Abroad. He manages ILMERA's finance, paperwork and documentation.

Fawaz: Fawaz BH is the Chief Marketing Officer of ILMERA Study Abroad and an independent SEO, AEO and GEO consultant based in Kodagu.

About's full Fawaz FAQ keeps his diploma; Zaheer's full FAQ matches his card. All38 page URLs/headings: phase-27-public-url-checks.tsv.

## (d) Unwanted text; (e) discovery

Find in visible text/source: **digital marketer**, **free**, **tuition-free**, **co-founder**. Flag every hit. Known substring-only matches: Services says “freely”; the held APS canonical URL contains “free”. See phase-27-raw-wording-hits.json; do not rename URLs or mistake these for a fee promise.

/sitemap.xml: exactly38 unique URLs; no APS, DSU, Czech Republic or Russia page. /robots.txt, /llms.txt and /llms-full.txt load; LLMs show the current Zaheer bio and no held promotion.


## (f) Private URL checks

Each link must finish at403/404, with no file contents/listing. Full list: phase-27-internal-url-checks.txt. These are clickable full live URLs, including files present in the pack.

| Check | Check |
|---|---|
| [/.git/HEAD](https://ilmerastudyabroad.com/.git/HEAD) | [/README.md](https://ilmerastudyabroad.com/README.md) |
| [/CHANGELOG.md](https://ilmerastudyabroad.com/CHANGELOG.md) | [/flagged-items-for-verification.md](https://ilmerastudyabroad.com/flagged-items-for-verification.md) |
| [/phase14-source-review.json](https://ilmerastudyabroad.com/phase14-source-review.json) | [/phase14-location-review.json](https://ilmerastudyabroad.com/phase14-location-review.json) |
| [/phase14-article-review.json](https://ilmerastudyabroad.com/phase14-article-review.json) | [/phase14-validation.json](https://ilmerastudyabroad.com/phase14-validation.json) |
| [/destinations-facts-template.csv](https://ilmerastudyabroad.com/destinations-facts-template.csv) | [/places-facts-template.csv](https://ilmerastudyabroad.com/places-facts-template.csv) |
| [/data/team.json](https://ilmerastudyabroad.com/data/team.json) | [/data/proof.php](https://ilmerastudyabroad.com/data/proof.php) |
| [/data/entity.json](https://ilmerastudyabroad.com/data/entity.json) | [/data/seo-map.json](https://ilmerastudyabroad.com/data/seo-map.json) |
| [/includes/posts.php](https://ilmerastudyabroad.com/includes/posts.php) | [/destinations/germany.php](https://ilmerastudyabroad.com/destinations/germany.php) |
| [/places/mysuru.php](https://ilmerastudyabroad.com/places/mysuru.php) | [/reports/owner-inputs-needed.md](https://ilmerastudyabroad.com/reports/owner-inputs-needed.md) |
| [/tools/check_discovery.py](https://ilmerastudyabroad.com/tools/check_discovery.py) | [/assets/fonts/.htaccess](https://ilmerastudyabroad.com/assets/fonts/.htaccess) |

## (g) Fonts and headers

Check GET and HEAD for each live WOFF2 file: HTTP 200, Content-Type **font/woff2**, Cache-Control **public, max-age=31536000, immutable**. Confirm CSP permits self-hosted fonts and destination data fonts. Check cold/warm pages and readable fallback. Local adapters did not prove native response headers.

| Cormorant files | Outfit files |
|---|---|
| [Latin](https://ilmerastudyabroad.com/assets/fonts/cormorant-garamond-latin.woff2) | [Latin](https://ilmerastudyabroad.com/assets/fonts/outfit-latin.woff2) |
| [Reference 300](https://ilmerastudyabroad.com/assets/fonts/cormorant-garamond-reference-300.woff2) | [Reference 300](https://ilmerastudyabroad.com/assets/fonts/outfit-reference-300.woff2) |
| [Reference 300 italic](https://ilmerastudyabroad.com/assets/fonts/cormorant-garamond-reference-300-italic.woff2) | [Reference 400](https://ilmerastudyabroad.com/assets/fonts/outfit-reference-400.woff2) |
| [Reference 400](https://ilmerastudyabroad.com/assets/fonts/cormorant-garamond-reference-400.woff2) | [Reference 500](https://ilmerastudyabroad.com/assets/fonts/outfit-reference-500.woff2) |
| [Reference 400 italic](https://ilmerastudyabroad.com/assets/fonts/cormorant-garamond-reference-400-italic.woff2) | [Reference 600](https://ilmerastudyabroad.com/assets/fonts/outfit-reference-600.woff2) |
| [Reference 600](https://ilmerastudyabroad.com/assets/fonts/cormorant-garamond-reference-600.woff2) | [Reference 700](https://ilmerastudyabroad.com/assets/fonts/outfit-reference-700.woff2) |
| [Reference 700](https://ilmerastudyabroad.com/assets/fonts/cormorant-garamond-reference-700.woff2) | Exact hashes: `reports/phase-27-payload-manifest.json` |

## (h) Contact form

Send one clearly labelled owner test using your own details. Confirm validation/errors AND actual inbox/provider receipt, not merely a success message. Record time/status; redact personal details when reporting. Check phone/WhatsApp links too.

## (i) Mobile speed after upload

Use PageSpeed Insights mobile on the same five URLs and settings as section (a). Keep dated result links/screenshots. No PSI result has been supplied by this local release work.

| Page | PSI result URL/date | LCP | TBT | CLS | Score | Added transfer (B) | New blocking URLs |
|---|---|---|---|---|---|---|---|
| Home `/` | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Services `/services` | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Germany `/study-in-germany` | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Mysuru `/study-abroad-counselling-mysuru` | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Choosing guide | ___ | ___ | ___ | ___ | ___ | ___ | ___ |

For each page, pass only when added transfer is **strictly below 150,000 bytes**, there are **no new render-blocking resources**, `LCP_after / LCP_before <= 1.10`, `CLS_after <= CLS_before` and `CLS_after < 0.10`, `TBT_after - TBT_before <= 50 ms`, and the performance score is no more than 5 points lower (`after >= before - 5`). Use the same URL and mobile settings. Missing or unusable results, or a missing baseline, are unverified and not passes. This is a whole-release comparison. Local simulated Lighthouse results are not PSI or field results and do not certify live speed.

## (j) Rollback and diagnosis

If a page, privacy check or response fails, disable public access at the host panel if needed. Restore the exact backed-up files, hosting/PHP settings and root/child `.htaccess` versions. Remove only files introduced by this upload that were absent from the backup, including the temporary checker and any new asset files. Do not leave private data accessible or protection removed.

**For HTTP 500 errors:** first restore the backed-up root `.htaccess`. Keep access disabled while completing the exact backup restore. If restoring the full backup requires removing new child policies, delete only the newly uploaded `.htaccess` files in `data/`, `includes/`, `destinations/`, `places/`, `reports/` and `tools/` where no older version existed; restore backed-up versions where they did. Restore prior font rules. Recheck the old site before reopening access.

Send the failing URL, screenshot/status and before/after PageSpeed result links. Do not send passwords or private enquiry/certificate details.

## (k) Search Console, after owner acceptance

Resubmit https://ilmerastudyabroad.com/sitemap.xml. Use URL Inspection to request indexing for [Karnataka](https://ilmerastudyabroad.com/study-abroad-consultants-in-karnataka), [Germany](https://ilmerastudyabroad.com/study-in-germany), [Italy](https://ilmerastudyabroad.com/study-in-italy), [UK](https://ilmerastudyabroad.com/study-in-uk) and the [choosing-consultant guide](https://ilmerastudyabroad.com/blog/how-to-choose-study-abroad-consultant-karnataka). Record outcomes; requests do not guarantee indexing/rankings. Never request the four held pages.

## (l) Upload-relevant changes since Phase31b `796879d`

These are the 11 changed upload paths in the current payload. The unchanged 1440px still remains included because current templates reference it; it is not an additional changed path since this baseline.

- `about.php`
- `assets/css/visual-system.css`
- `assets/fonts/cormorant-garamond-reference-300-italic.woff2`
- `assets/fonts/cormorant-garamond-reference-300.woff2`
- `assets/fonts/cormorant-garamond-reference-400-italic.woff2`
- `assets/fonts/cormorant-garamond-reference-600.woff2`
- `assets/images/hero-still-640.webp`
- `deploy-check.php`
- `includes/visual-config.php`
- `includes/visual-system.php`
- `index.php`

Full source/count/exclusion detail: `reports/phase-32c-upload-scope.json`. Payload ZIP checks and 43-route/31-asset clean-copy parity: `reports/phase-32c-payload-parity.json`. No live host check or deployment is claimed.
