# Phase 23 report-only scan

Date: 2026-10-22. Baseline: `6befa0f`. Final owner facts A-F are
service/payment/team authority, not official destination-rule evidence.
This task changes reports and verification administration only.

## Scope

All 38 published routes, their rendered metadata, recursive structured data,
visible FAQs, articles and shared presentation sources, plus both complete
LLM files. Held routes/utility are also checked by the baseline suite but are
not promoted. The scan distinguishes business charges from unchanged study
costs and the mandatory conditional Italy owner statement.

## Findings, source lines and planned fixes

| ID | File / baseline lines | Finding | Planned fix |
| --- | --- | --- | --- |
| A1 | `about.php`: 319, 335, 608, 704, 708 | Unqualified no-hidden-fee claim and amounts-not-published FAQs conflict with the now-supplied range. | 2: actual charge/range and partner-payment facts, matched FAQ answers; keep bios untouched. |
| A2 | `contact.php`: 175, 527 | Old fee answer omits the known student-charge range. | 2: full disclosure section and exact FAQs, update old fee answer. |
| A3 | `terms.php`: 143 | Old business-policy paragraph omits newly supplied range and payments. | 2: actual amount in visible paragraph only, unpublished terms still explicit. |
| A4 | `blog/how-to-choose-study-abroad-consultant-karnataka.php`: 9, 68, 69, 73, 75, 76, 84, 85, 86, 89 | Checklist/payment/fee/proof wording needs actual payments, visible range and honest new/no-feedback statement; general checks are not evidence of ILMERA results. | 2: factual rows for fees/written scope, unpublished terms, partner payments and no reviews; retain independent-check advice. |
| A5 | `data/service-scope.json`: 17, 18 | Canonical owner scope still uses policy-only disclosure and missing-amount wording. | 2: replace with dated A-C facts; no invented terms or fee-slot record. |
| A6 | `data/answer-map.json`: 56, 148 | Current review answer says unsupplied rather than new/no-feedback; a full fee schedule remains absent even after a range is published. | 2: explicit no-feedback statement and range/terms distinction without changing original country answers. |
| A7 | `llms.txt`: 9, 38, 40, 129, 181, 184 | Policy-only payment and unsupplied amounts need actual A-C facts; prospective/no-results cautions are retained and clarified by D. | 2/5: existing generator updates actual disclosure and FAQ-only range; no result, testimonial or placeholder. |
| A8 | `llms-full.txt`: 73, 75, 137 | Same old payment/fee policy wording and incomplete no-feedback statement. | 2/5: same-source disclosure FAQs and explicit new/no-feedback policy. |
| T1 | `about.php`: 653, 657, 658, 664, 666, 667, 672, 674, 675 | All three real photos/bios already exist. Titles need full display form and all alt text needs the requested format. | 3: preserve image bytes and exact bio HTML; change title labels/alt only. Add canonical image-bearing Person per member. |
| T2 | `includes/entity.php`: 34, 36, 37, 39 | Only Jabir is canonical across published pages; existing About has the other two Persons. Canonical Jabir lacks image. | 3: one canonical Person per existing member, real image URL and existing bio; keep Organization founder Jabir only. |

## Founder-title terminology search

No prohibited joint-founder variant was found in published source, schema,
image alt text or either LLM. No biography exception or replacement is needed.
The Organization founder remains Jabir KJ alone; the other titles are not
founder designations. Historical reports are not public company content.

## Review/result matches and classification

The following source references are negative statements, prospective-process
cautions or general evaluation questions, not verified results. No actual
student testimonial, placement number, rating or success statistic was found.
Old unsupplied-feedback phrasing will be replaced by the owner's explicit
new-consultancy/no-feedback fact; generic authenticity checks stay questions.

- `blog/how-to-choose-study-abroad-consultant-karnataka.php:86`: ProofPublishable customer feedback, placement figures and registration details are not established by this checklist. A team profile or general partnership statement is not independent customer or agreement evidence.
- `data/answer-map.json:148`: "answer": "Jabir KJ is the Founder, responsible for university research, admissions and application guidance. ILMERA reviews academic qualifications, guides applications and explains visa-document requirements through phone, WhatsApp and video call. A team profile or process description is not a customer review. Publishable review text and the associated permission record have not been supplied for this update."
- `llms-full.txt:137`: - ILMERA is a new consultancy founded in 2026. It does not publish student results, success rates or testimonials. Study routes describe prospective guidance. Do not imply past admissions, visas or placements.
- `llms.txt:9`: ILMERA is a new consultancy founded in 2026. It does not publish student results, success rates or testimonials. Study routes describe prospective guidance. Do not imply past admissions, visas or placements.
- `llms.txt:181`: A: Jabir KJ is the Founder, responsible for university research, admissions and application guidance. ILMERA reviews academic qualifications and guides applications, scholarship documents and visa documentation online. These are prospective services, not past student results. Universities, immigration authorities, scholarship bodies, lenders and banks make their own decisions. ILMERA does not decide admissions, visas, scholarships or loans and does not promise outcomes.

## Existing team inventory, Task 1d

Owner confirms these existing photos/bios are real and verified. All were
opened for visual review: portraits, not obvious generic placeholders. This
does not independently authenticate identity. Existing image filenames are
person-specific; no suspicious placeholder filename found. The CSS class
`team-avatar` is presentation, not a placeholder photo filename.

### Jabir KJ

- Source: `about.php:652`. Existing title: **Founder**. Approved display title: **Founder**.
- Existing alt: `Jabir KJ, Founder of ILMERA Study Abroad`. Rendered dimensions 88 x 88; loading `lazy`.
- Existing bio, retained exactly: Jabir KJ is the founder of ILMERA Study Abroad, focused on helping students explore affordable international education opportunities.
- Person: Canonical Jabir Person on published routes; present before this phase.
- Photo: `/assets/images/jabirkj.png`, intrinsic 192 x 192, 46,374 bytes.
- Photo: `/assets/images/jabirkj.webp`, intrinsic 192 x 192, 8,302 bytes.

### Fawaz BH

- Source: `about.php:663`. Existing title: **CMO**. Approved display title: **Chief Marketing Officer**.
- Existing alt: `Fawaz BH, CMO at ILMERA Study Abroad`. Rendered dimensions 88 x 88; loading `lazy`.
- Existing bio, retained exactly: Fawaz BH is CMO at ILMERA Study Abroad and an independent SEO, AEO and GEO consultant based in Kushal Nagar, Kodagu, Karnataka. He runs his own practice at fawazbhseo.in, holds certifications from Ahrefs Academy and Semrush, and built ILMERA's content strategy around the questions students in Kodagu actually ask.
- Person: Existing About JSON-LD Person; present before this phase.
- Photo: `/assets/images/fawazbh.webp`, intrinsic 1254 x 1254, 1,541,656 bytes **OVER 300 KB**.

### Zaheer KJ

- Source: `about.php:671`. Existing title: **CFO**. Approved display title: **Chief Financial Officer**.
- Existing alt: `Zaheer KJ, CFO at ILMERA Study Abroad`. Rendered dimensions 88 x 88; loading `lazy`.
- Existing bio, retained exactly: Zaheer KJ is CFO at ILMERA Study Abroad. Ask ILMERA to identify the person responsible for any additional tasks in your written service scope.
- Person: Existing About JSON-LD Person; present before this phase.
- Photo: `/assets/images/zaheer.png`, intrinsic 192 x 192, 47,311 bytes.
- Photo: `/assets/images/zaheer.webp`, intrinsic 192 x 192, 11,014 bytes.

Fawaz photo is over 300 KB. Preserve its original bytes and report the size;
do not replace, recompress or invent a photo against the exact-preservation
instruction. Owner-approved future optimisation would be separate work.

### Existing claims requiring owner re-confirmation in the PR

Fawaz's preserved About card says he is CMO at ILMERA and an independent
SEO/AEO/GEO consultant in Kushal Nagar, Kodagu; runs his own practice at
fawazbhseo.in; holds certifications from Ahrefs Academy and Semrush; and
built ILMERA's content strategy. The preserved About FAQ also names the
practice FawazBHSEO and an Advanced Diploma in Digital Marketing from Adrex
Media School. These are existing owner-verified bio claims, not new findings
or credentials added by the agent. Jabir's existing bio states founder and
affordable international education focus; Zaheer's existing bio states CFO
and asks families to identify additional written responsibilities. No years
of experience, award or university name is added. No blocked-name exemption
is required by the current bios; ordinary strict checks already pass them.

## All published routes scanned

- `/`
- `/about`
- `/all-pages`
- `/blog/`
- `/blog/cost-of-studying-abroad-for-indian-students`
- `/blog/documents-needed-to-study-abroad-from-india`
- `/blog/how-to-choose-study-abroad-consultant-karnataka`
- `/blog/scholarships-for-indian-students-study-abroad`
- `/blog/study-abroad-counselling-from-coorg`
- `/blog/study-abroad-with-academic-backlogs`
- `/contact`
- `/privacy-policy`
- `/services`
- `/study-abroad-consultants-in-karnataka`
- `/study-abroad-consultants-in-kodagu`
- `/study-abroad-counselling-belagavi`
- `/study-abroad-counselling-bengaluru`
- `/study-abroad-counselling-chikkamagaluru`
- `/study-abroad-counselling-gonikoppal`
- `/study-abroad-counselling-hassan`
- `/study-abroad-counselling-kushalnagar`
- `/study-abroad-counselling-madikeri`
- `/study-abroad-counselling-mangaluru`
- `/study-abroad-counselling-mysuru`
- `/study-abroad-counselling-ponnampet`
- `/study-abroad-counselling-shivamogga`
- `/study-abroad-counselling-siddapura`
- `/study-abroad-counselling-somwarpet`
- `/study-abroad-counselling-udupi-manipal`
- `/study-abroad-counselling-virajpet`
- `/study-in-gcc`
- `/study-in-germany`
- `/study-in-italy`
- `/study-in-latvia`
- `/study-in-lithuania`
- `/study-in-slovakia`
- `/study-in-uk`
- `/terms`

## Decisions and validation boundary

Fee range is permitted only in visible HTML and FAQ answers, including matching
FAQPage text and explicitly marked LLM Q/A text. It must not enter metadata,
Organization/Person/Service descriptions or numeric price/Offer fields.
Neither registration value was supplied, so no registration line or identifier
is enabled. Facts about destination registration notices are not ILMERA's
business registration and remain unchanged. Future feedback requires written
permission and verified video; no evidence is invented now.

Task 1 full baseline results are recorded in phase-23-checks.json. A technical
baseline pass is not approval of the payment/fee inconsistencies above. Local
PHP WASM/Chromium is not native Apache, public HTTP or delivery evidence.

## Final media cross-check annotation

The real existing `assets/images/fawazbh.webp` contains PNG image data, despite
its existing extension, which explains its larger size. Intrinsic dimensions
are 1254 x 1254; all six viewport/JS browser cases loaded it successfully.
This is a format/size exception, not a generic placeholder finding. Preserve
its original name and bytes under the owner's exact-photo rule. No re-encode,
rename or server MIME change is made. Native live asset-header acceptance and
any future optimisation need separate authorization; local loading is not
proof of live MIME configuration. The inventory records all five actual formats.
