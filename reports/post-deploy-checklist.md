# Content release: owner post-deploy checklist

**Draft only: release/content-phase-24b and its PR are not created in this session. No deployment performed.** Use the verified164d6de content candidate plus the narrow team patch, never the arena/design tree. Local WASM tests do not prove hosting behavior.

## 1. Before uploading

- Download a full live-site backup, including hidden files, old root .htaccess, subfolder rules, assets and hosting/PHP configuration. Store it outside the public folder. Record the complete old file list; verify the archive opens and rehearse restoration in staging.
- Arrange a maintenance window and rollback access. Use only the117 exact files in deploy-payload.md / phase-26-payload-manifest.json. Keep the three required root review JSON journals, six data JSON inputs and four runtime folder deny files. Exclude reports/tools/Markdown/CSV/Git/caches. Confirm native PHP, rewrite and Require/AllowOverride support first.

## 2. Open desktop and mobile pages

- Home and About: original design/photos/names/titles, three even cards with the exact texts below. Shorter team sections may move later sections upward; header/footer styles do not change.
  - Jabir KJ is the Founder of ILMERA Study Abroad. He is responsible for university research, admissions and application guidance.
  - Zaheer KJ is the Chief Financial Officer of ILMERA Study Abroad and a digital marketer. He manages ILMERA's finance and paperwork.
  - Fawaz BH is the Chief Marketing Officer of ILMERA Study Abroad and an independent SEO, AEO and GEO consultant based in Kodagu.
- About: open Fawaz/Zaheer FAQs; complete credential bios remain. About and Contact: approved Udyam line present, no private certificate details.
- Services: existing student service charge of ₹3 lakh to ₹15 lakh, separate university fees, university-payment disclosure and unpublished written-policy notice remain visible. This is a display check, not independent fee/policy proof.
- Open **all38 published URLs** in phase-26-public-url-checks.tsv:200, expected heading/content, canonical, images, FAQ and navigation. It includes every destination/place, blog/article, legal and directory page. Held Russia/Czech/APS/DSU pages must stay excluded from discovery.
- /sitemap.xml: exactly38 unique published URLs, all direct200/self-canonical. /robots.txt: correct sitemap URL. /llms.txt and /llms-full.txt: original full bios, disclosure and38 published URLs, no held entries. Compare against candidate files.

## 3. Check denied files

Follow redirects: each of these20 URLs must end at403/404 with no contents/listing. Test real runtime files as well as absent files. Full inventory: phase-26-internal-url-checks.txt.

https://ilmerastudyabroad.com/.git/HEAD
https://ilmerastudyabroad.com/README.md
https://ilmerastudyabroad.com/CHANGELOG.md
https://ilmerastudyabroad.com/flagged-items-for-verification.md
https://ilmerastudyabroad.com/phase14-source-review.json
https://ilmerastudyabroad.com/phase14-location-review.json
https://ilmerastudyabroad.com/phase14-article-review.json
https://ilmerastudyabroad.com/phase14-validation.json
https://ilmerastudyabroad.com/phase14-audit-resolution.csv
https://ilmerastudyabroad.com/destinations-facts-template.csv
https://ilmerastudyabroad.com/places-facts-template.csv
https://ilmerastudyabroad.com/data/team.json
https://ilmerastudyabroad.com/data/proof.php
https://ilmerastudyabroad.com/data/entity.json
https://ilmerastudyabroad.com/data/seo-map.json
https://ilmerastudyabroad.com/includes/posts.php
https://ilmerastudyabroad.com/destinations/germany.php
https://ilmerastudyabroad.com/places/mysuru.php
https://ilmerastudyabroad.com/reports/phase-24b-release-check.md
https://ilmerastudyabroad.com/tools/check_discovery.py

## 4. Contact and rollback

Submit one clearly labelled owner test using owner-controlled details. Verify validation/errors and actual inbox/provider receipt, not just a success toast. Record timestamp/status, redact personal data; do not open accounts or send customer outreach.

If any page errors or an internal file leaks: stop, keep the site offline and restore the exact backed-up files and old root .htaccess. Remove all newly uploaded files absent from the backup, especially protected JSON/runtime inputs. Remove new .htaccess files in data/, includes/, destinations/, places/, reports/ and tools/ if uploaded; restore old versions instead where they existed. **Never remove denies while leaving new private inputs behind an old unprotected root.** Recheck the old site before reopening. Native ACL/MIME/CSP/cache/redirect/delivery and backup proof remain owner checks.
