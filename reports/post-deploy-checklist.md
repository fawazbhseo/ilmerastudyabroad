# Owner release checklist: full branch, Phase27

No deployment done here. Use the130-file pack in deploy-payload.md, never the old117-file pack. Owner accepts the release after these checks; local tests do not certify hosting or speed. Links below use https://ilmerastudyabroad.com.

## (a) Before deploying

Download ALL live public_html files, hidden files, root/child .htaccess and hosting/PHP settings. Store the backup outside web access, verify it opens and confirm how to restore it. Record the old file list. Keep host-panel access and an offline/rollback window ready.

Run PageSpeed Insights **mobile** on the current Phase13 live pages. Save dated result links/screenshots and fill this table. Use the same URLs/device settings afterward; retain every run. If a URL is absent, record its status/no baseline. The choosing guide was added after Phase13: never use a404 score or another page as its baseline.

| Before: page | LCP | CLS | Performance score |
|---|---|---|---|
| / | ___ | ___ | ___ |
| /services | ___ | ___ | ___ |
| /study-in-germany | ___ | ___ | ___ |
| /study-abroad-counselling-mysuru | ___ | ___ | ___ |
| /blog/how-to-choose-study-abroad-consultant-karnataka | ___ | ___ | ___ |

## (b) Upload method

**Current Phase30 ZIP:131 files, including the temporary self-check.130 permanent files remain after deleting it. This section supersedes the older130-file upload wording above and the old ZIP note.** Do not use a PHP-only update or upload the whole repository.

1. **(a) Back up first.** Download the existing public_html contents, including hidden files and hosting/PHP settings, to your computer. Keep the backup outside public_html and confirm how to restore it.
2. **(b) Download** [ilmera-deploy-f54e4cc.zip](https://raw.githubusercontent.com/fawazbhseo/ilmerastudyabroad/arena/48320ee5-ilmerastudyabroad/releases/ilmera-deploy-f54e4cc.zip) from GitHub to your computer. Expected size:690538 bytes.
3. **(c) Extract on Hostinger.** Open hPanel, Websites, this site's Dashboard/Manage, File Manager. Open the domain's public_html folder. Upload the ZIP there, select it and choose Extract. Extract directly into public_html and overwrite existing files. Do not create a ZIP-named subfolder. Enable Show hidden files so .htaccess files are included. Do not upload releases/, reports or tools contents from the repository.
4. **(d) Delete the uploaded ZIP from public_html immediately after extraction.** Keep your backup on your computer, never under web access. Check the folder counts below after deleting the ZIP.
5. **(e) Clear caches.** In hPanel, find this site's Cache Manager, commonly under Performance, and choose Purge all. If Hostinger CDN is enabled, purge its cache too. If a LiteSpeed/LSCache option is enabled, purge that cache; for an installed WordPress LiteSpeed Cache plugin, use LiteSpeed Cache, Toolbox, Purge All. This PHP site need not have WordPress or that plugin: do not install one. Panel labels vary; use panel search or ask Hostinger support. Open a fresh private/incognito window for testing.
6. **(f) Run** [the temporary live self-check](https://ilmerastudyabroad.com/deploy-check.php?key=596b2f06f047c76730364c34857c6b47d03b019b21f8818960752a42fe104d9f) and send a screenshot of ALL FILES OK or the FAIL list. It checks fixed payload files for you, including the design assets. It expires after15November2026 UTC. Do not add extra URL parameters. This result is not a speed/native-host acceptance.
7. **(g) Delete deploy-check.php from public_html immediately after that one use.** Reopen its link to confirm404. Never leave the temporary file online just because it has a key/expiry.
8. **(h) Continue with all the page, privacy, font, contact and speed checks below.** If anything fails, follow rollback section(j), not speculative file deletion.

**Expected files from this ZIP:** count files, not folders, including hidden files/licences. Existing host extras may make counts larger; compare them with the backup and ask before deleting unrelated hosting files. Overwrite does not remove old unlisted files.

| Folder | Expected files |
|---|---|
| assets/css | 1 |
| assets/fonts | 12 |
| assets/images | 7 |
| includes | 18 |
| data | 8 |
| destinations | 10 |
| places | 18 |
| blog | 9 |
| root public_html | 46 before deleting deploy-check.php;45 afterward |

reports/ and tools/ each receive ONLY their hidden .htaccess deny file, one file each, no other content. Counts sum131 before deleting the checker,130 afterward. The releases/ folder is never extracted. Font count12 includes9 font binaries,2 licences and1 hidden policy.

**12 important files to spot:** assets/css/visual-system.css; assets/fonts/outfit-latin.woff2; assets/fonts/cormorant-garamond-latin.woff2; includes/visual-system.php; includes/visual-config.php; includes/site-presentation.php; includes/header.php; includes/footer.php; data/seo-map.json; data/answer-map.json; root .htaccess; temporary deploy-check.php. The checker covers the full allowlist and detailed critical hashes; you do not need to compare130 files manually.

## (c) Open on mobile and desktop

- **Home:** navigation/photos work; three even-height team cards, exact bios below.
- **About:** same cards; biography FAQs open; Udyam number UDYAM-KR-18-0023330 and business-registration-only/no-authority-endorsement caveat.
- **Services:** student charge ₹3 lakh to ₹15 lakh, university fees separate, university-payment disclosure, written policy terms not yet published.
- **Contact:** same disclosure and Udyam/caveat; working form and existing contact links.
- **/blog/:** published article cards load. **Choosing-consultant article:** readable guide, author image, FAQs and disclosure.
- **Germany:** plain navy hero, readable sourced guide/FAQs. **Mysuru:** gradient hero, light reading areas, unique local guide/FAQs. Neither has missing fonts/images.
- **/404:** Page Not Found, noindex, shortened footer. Also test an invented URL: HTTP404, not soft200; verify host error-page routing.

Jabir: Jabir KJ is the Founder of ILMERA Study Abroad. He is responsible for university research, admissions and application guidance.

Zaheer: Zaheer KJ is the Chief Financial Officer of ILMERA Study Abroad. He manages ILMERA's finance, paperwork and documentation.

Fawaz: Fawaz BH is the Chief Marketing Officer of ILMERA Study Abroad and an independent SEO, AEO and GEO consultant based in Kodagu.

About's full Fawaz FAQ keeps his diploma; Zaheer's full FAQ matches his card. All38 page URLs/headings: phase-27-public-url-checks.tsv.

## (d) Unwanted text; (e) discovery

Find in visible text/source: **digital marketer**, **free**, **tuition-free**, **co-founder**. Flag every hit. Known substring-only matches: Services says “freely”; the held APS canonical URL contains “free”. See phase-27-raw-wording-hits.json; do not rename URLs or mistake these for a fee promise.

/sitemap.xml: exactly38 unique URLs; no APS, DSU, Czech Republic or Russia page. /robots.txt, /llms.txt and /llms-full.txt load; LLMs show the current Zaheer bio and no held promotion.

<!-- PAGE BREAK -->

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

Open each live font; check GET and HEAD in browser Network/hosting tools:200, Content-Type **font/woff2**, Cache-Control **public, max-age=31536000, immutable**. Confirm CSP permits self fonts and destination data fonts. Cold/warm pages and blocked-font fallback must stay readable; local adapter did not prove native headers.

| Live font URLs | Live font URLs |
|---|---|
| [Outfit300](https://ilmerastudyabroad.com/assets/fonts/outfit-reference-300.woff2) | [Outfit400](https://ilmerastudyabroad.com/assets/fonts/outfit-reference-400.woff2) |
| [Outfit500](https://ilmerastudyabroad.com/assets/fonts/outfit-reference-500.woff2) | [Outfit600](https://ilmerastudyabroad.com/assets/fonts/outfit-reference-600.woff2) |
| [Outfit700](https://ilmerastudyabroad.com/assets/fonts/outfit-reference-700.woff2) | [Cormorant400](https://ilmerastudyabroad.com/assets/fonts/cormorant-garamond-reference-400.woff2) |
| [Cormorant700](https://ilmerastudyabroad.com/assets/fonts/cormorant-garamond-reference-700.woff2) | Exact hashes: phase-25-release-check.md |

## (h) Contact form

Send one clearly labelled owner test using your own details. Confirm validation/errors AND actual inbox/provider receipt, not merely a success message. Record time/status; redact personal details when reporting. Check phone/WhatsApp links too.

## (i) Mobile speed after upload

| After: same page | LCP | CLS | Performance score |
|---|---|---|---|
| / | ___ | ___ | ___ |
| /services | ___ | ___ | ___ |
| /study-in-germany | ___ | ___ | ___ |
| /study-abroad-counselling-mysuru | ___ | ___ | ___ |
| /blog/how-to-choose-study-abroad-consultant-karnataka | ___ | ___ | ___ |

For **each page**: LCP no more than10% worse (after<=before x1.10), CLS<0.1, performance score no more than5 points lower (after>=before-5). Missing/unusable results are unverified, not passes. This compares the whole combined release, not design alone. No local performance certification is claimed.

## (j) Rollback and diagnosis

If anything fails, disable public access at the host panel. Restore the exact backed-up files/settings and .htaccess; remove new files absent from that backup, especially private JSON/runtime inputs. Do not leave new private files with protection removed.

**For500:** first restore backed-up root .htaccess. While access stays disabled, finish the exact backup restore/remove new files; then delete newly uploaded child .htaccess in data/, includes/, destinations/, places/, reports/, tools/ if uploaded. Restore old child versions instead where they existed; restore font rules too. Recheck the old site before reopening.

Send back: failing URL, screenshot/error status and before/after PageSpeed numbers/result links. No passwords or private enquiry/certificate details.

## (k) Search Console, after owner acceptance

Resubmit https://ilmerastudyabroad.com/sitemap.xml. Use URL Inspection to request indexing for [Karnataka](https://ilmerastudyabroad.com/study-abroad-consultants-in-karnataka), [Germany](https://ilmerastudyabroad.com/study-in-germany), [Italy](https://ilmerastudyabroad.com/study-in-italy), [UK](https://ilmerastudyabroad.com/study-in-uk) and the [choosing-consultant guide](https://ilmerastudyabroad.com/blog/how-to-choose-study-abroad-consultant-karnataka). Record outcomes; requests do not guarantee indexing/rankings. Never request the four held pages.
