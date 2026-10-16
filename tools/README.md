# Publication verification

Run against an authorised PHP/Apache staging copy with the repository's clean
URL configuration. Do not run mutation fixtures against a production docroot.

```sh
php tools/check_destination_sources.php
php tools/check_place_contact.php
php tools/check_place_publication.php
python3 tools/check_location_content.py
python3 tools/check_publication_review.py --base-url https://your-staging-host
python3 tools/check_discovery.py --base-url https://your-staging-host
php tools/build-sitemap.php
```

The Python checkers use the standard library. The location checker calls PHP
CLI to read the data arrays; `--data-json` accepts an equivalent exported object
with a `places` key. The source/date journals are editorial evidence records,
not live crawlers. Passing a machine check does not establish factual truth.
Open the official text, confirm support and approval, review the copy, then
update the appropriate journal. Never mark a failed fetch as verified.

`check_location_content.py --write-report` replaces the authored-copy report.
A publication review also needs the full rendered-main overlap measurement;
absence of that measurement keeps the location cohort blocked. Editing any
peer requires another pairwise review. City names are normalised before the
five-token coverage calculation. The prose minimum excludes headings, FAQs,
shared contact text and navigation. There are 136 comparisons for 17 guides.

`check_discovery.py` supports `--fixture-base-url` and `--fixture-root` together.
The fixture root must be a separately served copy, never the real root. It
copies the current reviewed data, exercises status/source/cohort/article
mismatches and explicit noindex headers, then restores the modified records.
Held APS and DSU records must remain excluded even after status-only toggles.

The Phase 14 run used PHP 8.5 WASM for parser/HTTP checks and Chromium for
captured-render checks at widths 375, 768 and 1280, with JavaScript on/off.
This does not prove native Apache behavior or external network resources.
On Apache 2.4, test `/sitemap`, `/sitemap.php`, `/sitemap.xml`, clean PHP routes,
query-string preservation and appropriate include/data/tool access controls.
The inherited `[END]` sitemap rule needs native staging verification before
release. No deployment or merge is implied by a repository publication flag.

Do not edit either LLM file during this phase. Their frozen SHA-256 hashes are
recorded in `phase14-validation.json`. A separate authorised content and
publication-status reconciliation is required for those files.
