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

## Phase 16 maintenance note, 2026-10-16

The Phase 14 freeze paragraph above is historical. The only later LLM
permission is Phase 16 task 1: remove the held APS/DSU article link lines.
Both files must otherwise equal the Phase 15 handoff c2c8b9f bytes.
check_discovery.expected_llm_bytes enforces that exact authorized difference;
llms-full.txt remains unchanged. Do not edit names, wording, dates or other
LLM text under this limited permission.

Use an authorized PHP/Apache staging copy, not the adapter, for release
sign-off. Example commands (BASE is your authorized staging HTTPS origin):

```sh
find . -path './.git' -prune -o -type f -name '*.php' -exec php -l {} \;
python3 tools/test_discovery.py
python3 tools/test_citations.py
python3 tools/test_italy_claims.py
php tools/check_destination_sources.php
php tools/check_place_publication.php
php tools/check_place_contact.php
python3 tools/check_location_content.py
python3 tools/check_italy_claims.py --base-url "$BASE"
python3 tools/published_citations.py --base-url "$BASE" --output /tmp/current-citations.json
python3 tools/check_discovery.py --base-url "$BASE"
python3 tools/check_publication_review.py --base-url "$BASE"
```

The default discovery/publication commands currently FAIL, correctly, because
llms.txt still contains listed institution names under the edit restriction.
Both public LLM files also fail the release-wide prohibited-wording scan.
Do not remove list entries, exempt public LLM files or turn off name
checks to make the release appear to pass. A diagnostic core run with
check(..., enforce_names=False) isolates links/sitemap/robots only; it is not
a release command or a substitute for the strict result.

Maintain tools/blocked-names.txt when a new university alias is found. The
guard checks visible copy, metadata, alt/link attributes and decoded JSON-LD,
as well as both public LLM files. Only government citation anchors may retain
institution names; business affiliation and ordinary public copy may not.
Six regression cases cover these boundaries and escaped/URL aliases.

published_citations.py inventories all non-social external anchors, schema
citation fields and both public LLM files, without a destination-host
allowlist that could hide legacy/unknown-host references. It does not crawl
external sources or approve new hosts. Its explicit contact/social/owner-bio
exclusions are documented in the module. Three tests cover unfiltered footer
hosts, schema-only references and exclusions. Review the entire output.
For every external citation, perform an authorized GET with raw status and
redirect headers, require final HTTP 200, inspect the substantive body and
confirm the retained statement on an approved same-topic source. A successful
fetch wrapper or a soft-missing HTTP-200 body is not verification. The Phase
16 fetch interface did not expose raw status on success, so that transport
requirement remains unverified rather than assumed.

check_italy_claims.py requires the exact owner sentence at 8,000-euro contexts
plus matching local owner attribution and written-award caution. Four tests
cover the exact text, missing labels/cautions, common amount variants and
unrelated programme fees. It is not proof of an award or partner. Keep FAQ
schema/visible parity and test actual full answer readability at mobile
widths with JavaScript on/off; fixed FAQ height caps can hide qualifications.

The Phase 16 report records 83 PHP parses, 42 renders and 252 browser cases
fresh after each task. The local PHP 8.5 WASM adapter and Chromium captured
HTML/local-image replay do not verify native Apache or external assets.
Repeat real rewrite/redirect/query/access-control/HTTPS-host/contact checks,
raw external-source transport checks, and all default acceptance checks
before staging sign-off. Keep all four held pages excluded. Use the full
final rendered-main overlap measurement too, not just authored prose.

Reports: reports/phase-16-release-check.md, phase-16-checks.json and
phase-16-citations.json. Historical reports and blockers remain untouched;
new findings are appended. No main push, merge or deployment is implied.

## Phase 17 online-presence and GCC maintenance, 2026-10-16

The owner has now confirmed online-only counselling, with no physical office
or in-person counselling location anywhere, and university partnerships in
all six GCC countries. Only these owner-input uncertainties are closed.
Kuwait official student-rule evidence is still open. No page status may be
changed and neither LLM file may be edited under Phase 17 instructions.

Run the earlier strict validation commands plus:

```sh
python3 tools/test_presence.py
```

The discovery guard scans public text, metadata, alt/link attributes, decoded
JSON-LD and both public LLM files for physical-presence offers, including
plural premises, proximity, walk-in and meeting wording. Narrow exceptions
cover exact negative owner disclosures, the required no-travel sentence,
academic campus references and existing official immigration/interview text.
They do not exempt an entire paragraph or a second meeting offer. Nine
regression cases cover those boundaries. Government citation anchors are not
exempt from this presence guard, even though the separate names guard has a
source-label exception. The final phase audit also checks
actual location Service/Organization areaServed, absence of storefront types
and address/coordinates, visible notes, and 136 fresh full-main comparisons.

Place copy edits require fresh content hashes, authored pairwise checks and
full rendered-main overlap before updating phase14-location-review.json.
Keep every guide above 350 authored words and every pair below 15%; FAQ and
shared contact text do not count toward the prose minimum. Preserve statuses.

GCC scope_note is owner-confirmed six-country university application support;
review_notice separately identifies the five countries with sourced material
and the missing Kuwait rules. Metadata and WebPage/Service descriptions must
match both notes. Oman and Bahrain remain registration-only coverage. The
protected GCC intro_answer, slug, name, summary and provenance must not change.
Do not generalize an embassy registration request into admission/visa/work
rules or claim government/embassy business affiliation. A directory is not
proof of a current student rule. Update exact source rows after a real open.

The existing Contact address record is only a Coorg/Kodagu/Karnataka/India
postal locality, not a street, delivery address or counselling premises. Keep
that labelled partial record only in the Contact organisation. Do not invent
a registered address or add location street/geo data. Local areaServed is the
student audience for online counselling, never evidence of a local venue.

The strict global name/wording result remains blocked by restricted existing
LLM content. Never waive that failure or change those files to obtain a pass.
Local PHP adapter and captured-render browser checks are not native Apache,
external raw-transport or contact-delivery proof. The complete final results,
line/file inventories and limitations are in reports/phase-17-verification.md
and reports/phase-17-checks.json. No merge or deployment is implied.

## Phase 18: authorized LLM edits, strict replacement policy

The owner's Phase 18 approval supersedes the historical LLM byte restriction
above. No current check compares an LLM file with a historical frozen version.
`check_discovery.validate_llm_text` instead rejects blocked names, prohibited
cost wording, physical-presence implications, draft promotion and punctuation;
it requires explicit online-only counselling, the exact conditional Italy
sentence with immediate attribution/caution, and both exact visible GCC notes.
`check_publication_review.py` checks that the served bytes match the working
copy and records current hashes as identity evidence, not an edit prohibition.
Run `python3 tools/test_llm_policy.py` to exercise the policy failure cases.
The maintained internal alias list includes names removed during reconciliation.
This is not publication copy and must not be used to suggest partnerships.

### Published-page directory maintenance

No earlier LLM generator was found. Phase 18 adds a small maintained builder:

```sh
python3 tools/build_llms_directory.py --base-url http://127.0.0.1:8080
python3 tools/build_llms_directory.py --base-url http://127.0.0.1:8080 --write
python3 tools/test_llm_directory.py
```

Default mode checks idempotence and exact rendered title/meta-description
parity. `--write` updates the existing Markdown destination, location, blog
and index entries in both files, preserving the hand-maintained policy copy.
Only published, actually indexable pages qualify. Existing company/contact/
services/legal URLs remain in their established sections. Every indexable
site URL must be represented, and all 29 editorial directory entries plus
the blog and all-pages indexes must match the fresh rendered metadata.
`check_discovery.py` and the publication checker enforce this by default.
Use a local verification copy for this builder, never a mutation fixture
or a production docroot. Live smoke testing uses the owner checklist instead.

### Phase 18 strict defaults

Discovery now enforces prohibited cost wording across published visible copy,
metadata, decoded URLs, FAQ/schema and both LLM documents, not only inside the
LLM-specific policy. Government citation labels are not exempt from wording
or physical-presence checks. The narrow existing institution-label exception
remains separate. The publication command also requires the independent exact
Italy amount/attribution/caution check across the whole published site.
`python3 tools/test_wording.py` covers normalized/encoded wording regressions.
Drafts and the separate noindex utility page retain their existing boundaries.
