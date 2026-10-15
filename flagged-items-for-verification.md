# Flagged Items for Manual Verification

These are assumptions or gaps introduced during the SEO/AEO/GEO rewrite that
the site owner should confirm before or shortly after publishing. None of
them block the site from working correctly, but they affect accuracy or
brand polish.

## 1. Logo asset path (RESOLVED)
- All pages now consistently reference `assets/images/ilmera.logo.png` for
  the header logo, favicon, and `og:image`/`twitter:image` social preview
  tags. **Action needed:** confirm this exact file exists on the live server
  and renders correctly both as a small favicon (square crop) and as a large
  1200x630 social preview image; a dedicated square favicon and a dedicated
  social-preview image are usually sharper than reusing one logo file for
  both purposes.
- The header no longer references a separate "light theme" logo variant,
  because the light/dark theme toggle itself has been removed from the site
  (see item 4 below) : there is now only one visual theme, so only one logo
  file is needed.

## 2. Team photo filenames (RESOLVED)
- Standardized across the whole site to exactly:
  - `assets/images/ilmera.logo.png` (logo)
  - `assets/images/jabirkj.png` (Jabir KJ, Founder)
  - `assets/images/zaheer.png` (Zaheer KJ, CFO : lowercase "z")
  - `assets/images/fawazbh.webp` (Fawaz BH, CMO)
- **Action needed:** confirm these four files exist at these exact paths
  (case-sensitive) on the live server. `zaheer.png` was previously
  referenced inconsistently as `Zaheer.png` (capital Z) in some places :
  if the live server's filesystem is case-sensitive (most Linux hosts are),
  only one of those casings will actually work.

## 3. About page team cards (RESOLVED)
- Removed a duplicated "Jabir KJ" name that previously appeared twice in
  his team card.
- Unified all three team cards (Jabir/Fawaz/Zaheer) to the same structure:
  avatar image, name heading, role, then a bio paragraph of comparable
  length (roughly 55-60 words each, down from Jabir's ~115 words vs. ~65
  for the other two).
- Unified the `alt` attribute pattern on all three avatar images to
  "[Name], [Role] of/at ILMERA Study Abroad".

## 4. Light/dark theme toggle removed
- The `theme-toggle` button, its sun/moon icons, and the associated
  `localStorage`-based theme-switch script were removed from `header.php`
  at the site owner's request. The `html[data-theme="light"]` CSS rules
  elsewhere in `header.php`, `about.php`, and `contact.php` were left in
  place (they simply never trigger now, since nothing sets
  `data-theme="light"` anymore) rather than being stripped out, to avoid
  making a large, form of unrequested changes across multiple files.
  **Action needed:** if a future editor wants to fully remove all traces of
  the old light-theme feature (not just the button that triggered it), the
  `html[data-theme="light"]` CSS blocks in those three files can be deleted
  as a follow-up cleanup; leaving them in has no visible effect on the
  current site.

## 5. sitemap.php added alongside sitemap.xml
- `sitemap.php` was created per the site owner's request. Rather than
  duplicating the URL list in two independently maintained places (a
  risk for drift and a potential duplicate-content signal), `sitemap.php`
  301-redirects to the canonical `/sitemap.xml`, which remains the single
  source of truth and the one referenced in `robots.txt`.
- **Action needed:** none, unless the site owner specifically wants
  `sitemap.php` to generate its own independent XML instead of redirecting
  : in that case, say so and the redirect can be replaced with a PHP-
  generated sitemap (a version of this was drafted and is easy to restore).

## 6. Destination/eligibility facts to confirm against current official sources
The following figures were kept or written based on prior site content and
general knowledge, not independently verified this session. They should be
checked against current official/government sources before relying on them
for compliance-sensitive claims:
- UK Graduate Route: "up to 2 years of post-study work after completing a
  degree" (correct as a general rule at time of writing, but visa rules
  change; verify current validity).
- Italy DSU scholarship: described as regional, income-based (ISEE) and
  merit-based, potentially covering tuition, stipend, and subsidised housing
  and meals. Amounts and eligibility thresholds vary by region and by year
  and are intentionally not quoted as fixed numbers, but should be confirmed
  each admissions cycle.
- Germany: "public universities charge little to no tuition" and the APS
  certificate being "mandatory for Indian applicants since 2022" : confirm
  current APS requirement status and any tuition changes in the state(s)
  ILMERA actually places students in.
- Czech Republic / Lithuania / Latvia / Slovakia: described qualitatively as
  "low-cost" / "some tuition-free programmes" without specific fee figures.
  If specific fee ranges are added later, they must be sourced and dated.
- GCC (UAE, Saudi Arabia, Qatar, Kuwait, Bahrain, Oman): described as hosting
  "international branch campuses of UK, US and Australian universities" :
  true in general but should be confirmed for whichever specific campuses
  ILMERA actually works with.

## 7. Social handles and contact details
- Instagram handle standardized to `ilmera.studyabroad`; Facebook/LinkedIn
  standardized to `ilmerastudyabroad`. **Action needed:** confirm these
  handles are live, correctly spelled, and actually owned/managed by ILMERA
  before the site goes live, since a broken or wrong social link is a poor
  trust signal (E-E-A-T) for both human visitors and AI answer engines.
- WhatsApp number `+421 944485186` (a non-Indian country code) is used
  site-wide for the WhatsApp channel. This was already present in the
  inherited content and was not changed. **Action needed:** confirm this is
  intentional (e.g., a WhatsApp Business number) and correct if it should be
  an Indian number instead.

## 8. Minor cosmetic whitespace in about.php
- Two blank lines remain inside Jabir KJ's team card in the HTML source
  (between the avatar `<img>` and the `<h3>` name), left over from removing
  the duplicate name div. They collapse to nothing when rendered in a
  browser and have no visible or functional effect; flagged only for
  source-code tidiness if a future editor wants to remove them.

## 9. On the "#1 ranking" goal
No legitimate SEO/AEO/GEO work (on-page structure, schema, content quality,
crawler access, technical hygiene) can guarantee a #1 ranking on Google,
Bing, or any AI answer engine, because rankings are also driven by
competitor content, backlink profiles, domain authority/age, and ongoing
algorithm changes that are outside any single site's control. This project
strengthened every on-page and structured-data lever within a static site's
control (accurate schema, consistent NAP/contact data, clean URLs, crawler
access for AI bots, no fabricated claims that could trigger trust penalties).
Further ranking improvement beyond this point typically requires off-page
work (backlinks, reviews, citations) and ongoing content additions, which are
outside the scope of a one-time static-site rewrite.

## 10. New Blog feature added (RESOLVED)
- `/blog` was added as a new listing page (originally `blog.php` at the site
  root; **moved to `blog/index.php` to fix a 404**, see item 12 below), linked
  from the main
  navigation (`header.php`, both desktop and mobile menus) and from the
  footer's Navigation list (`footer.php`). It is also included in
  `sitemap.xml`.
- Four initial articles were written as **individual static PHP pages** under
  `/blog/{slug}` (e.g. `/blog/study-in-germany-free-aps-certificate`), each
  with its own SEO meta tags, Open Graph/Twitter tags, and `BlogPosting` +
  `BreadcrumbList` JSON-LD. This matches the rest of the site's fully static,
  server-rendered approach (important for AI/answer-engine crawlers that do
  not execute JavaScript) and avoids the 404s that would have resulted from
  linking to detail pages that did not exist.
- A `blog_posts` table was also created via the Table API (schema + 4 rows)
  early in this work, before the static-page approach was finalized. **This
  table is currently unused** : no page reads from it. It can be deleted if
  the site owner does not plan to move the blog to a dynamic/database-backed
  model later, or kept as a head start if they do. Flagging so it is not
  mistaken for live content.
- **UPDATE:** all four articles are now attributed to a single author, **Fawaz
  BH, CMO**, per the site owner's explicit request (previously Zaheer KJ was
  credited on the Germany/APS article and Jabir KJ on the Italy/DSU article).
  **Action needed:** let us know if the site owner wants additional articles,
  a "read more" pagination system, or category filtering as the blog grows.

## 11. Jabir KJ's title corrected from "CEO" to "Founder" (RESOLVED)
- Jabir KJ is the Founder of ILMERA Study Abroad, not the CEO. Every "CEO"
  reference to him has been changed to "Founder" across `about.php`
  (meta tags, JSON-LD `Person.jobTitle` and `description`, FAQ answers,
  visible hero/story/Kodagu-section prose, and the visible team card),
  `index.php` (JSON-LD `founder`/`employee` Person objects, FAQ JSON-LD and
  its visible `<details>` duplicate, and the visible team card), `contact.php`
  (`ai-content-summary` meta tag), `llms.txt`, and `llms-full.txt`. The
  `Organization.founder` relationship (`{"@id": ".../#jabir"}`) itself was
  left unchanged, since that relationship was already correct.
- `llms-full.txt`'s leadership section previously stated that "Founder" was
  an informal, non-authoritative variant of Jabir KJ's title; that sentence
  was rewritten since Founder is now his standardized, authoritative title.
- **Action needed:** none : this is complete. Confirm no other internal
  documents or external listings (e.g. Google Business Profile, LinkedIn
  company page) still list Jabir KJ as "CEO".

## 12. Blog pages returning 404 (RESOLVED)
- **Root cause:** the site had both a `blog.php` file at the site root AND a
  `blog/` directory (holding the 4 article pages) at the same time. The
  `.htaccess` rewrite rule that maps `/blog` to `blog.php` only fires when
  `%{REQUEST_FILENAME}` is **not** an existing directory
  (`RewriteCond %{REQUEST_FILENAME} !-d`). Because `blog/` is a real
  directory on disk, that condition failed for every request to `/blog`, so
  Apache tried to serve the `blog/` directory itself instead of `blog.php`
  and found no index file there, resulting in a 404 (individual article
  pages like `/blog/study-in-germany-free-aps-certificate` were unaffected,
  since those exact paths are not directories).
- **Fix applied:** moved the listing page from `blog.php` to `blog/index.php`
  and added `DirectoryIndex index.php index.html` to `.htaccess`. Now a
  request for `/blog` resolves directly to the directory's own `index.php`
  through Apache's normal directory-index behavior, with no naming conflict.
  No links needed to change, since `header.php`, `footer.php`, `sitemap.xml`,
  and the JSON-LD `Blog`/`BreadcrumbList` entities all already pointed to the
  extension-less `/blog` path, not to `blog.php` directly.
- **Action needed:** after deploying, verify `/blog` and all 4
  `/blog/{slug}` article URLs load correctly (not just that they no longer
  404, but that they render the full page, since a clean console/absence of
  a 404 does not by itself confirm correct rendering).


## 13. Phase 1: unpublished draft claim inventory (OWNER VERIFICATION REQUIRED)

The following three posts are not live yet per the owner. They retain
`noindex, follow` and are not shown on the four-card listing. There are now
7 article files under `blog/`, but only the 4 indexable articles are included
in the sitemap. The cost, documents and scholarships drafts are excluded
while they retain `noindex`.

**Release rule (Phase 4):** After fact-checking, publish through
`includes/posts.php` status, accurate metadata dates, a `sitemap.xml` entry
with accurate lastmod and a verified `llms.txt` summary in **one commit**.
Do not remove robots guards; they follow the registry. Links populate
automatically. Verify every item below against the relevant university,
scholarship body, consulate or immigration source. Record source URL,
applicable intake/date, exceptions and owner sign-off. See section 16.
No current official-source verification was performed in this repair.

### A. `blog/cost-of-studying-abroad-for-indian-students.php`

**Cost figures and cost comparisons (including zero/free claims):**
There are no numeric currency amounts or fee ranges in this draft. Its
amount claims are qualitative, including zero tuition and a free consultation:

- Czech Republic, Lithuania, Latvia, Slovakia and Russia are described as
  usually the cheapest destinations for Indian students.
- German public universities: little to no tuition regardless of nationality;
  zero tuition at most public universities; semester contributions apply.
  Most public universities charge no tuition for consecutive degrees, but
  a few states levy fees in specific cases. Living costs are called moderate.
- Italy: public universities charge tuition; regional DSU can cover tuition
  and add a stipend, subsidised accommodation and meals. Living costs are
  moderate and lower in smaller cities. DSU is said to make Italy cheaper
  than its sticker price for many families.
- Czech Republic: among the lowest EU tuition levels; low-to-moderate living
  costs. Lithuania: low tuition and some of the lowest EU living costs;
  living costs labelled low. Latvia: low tuition and low living costs.
- Slovakia: free tuition in some Slovak-language branches; English programmes
  are paid; low living costs. The free route is said to require a preparatory
  language-learning year.
- Russia: low tuition and low living costs.
- UK: substantial tuition, high living costs especially in London; a one-year
  Master's is said to shorten total cost.
- GCC (UAE, Saudi Arabia, Qatar, Kuwait, Bahrain, Oman): fees vary by university
  and branch campus; moderate-to-high living costs in Dubai/Qatar.
- Germany and Italy are said to genuinely approach zero tuition. This
  statement needs reconciling with the separate Slovakia free-tuition claim.
- Budget components: tuition/semester contribution; rent, food, transport,
  insurance; visa funds; application fees, APS certificate, document
  legalisation, flights and initial settlement money. City/programme
  differences, later-year tuition changes and scholarship renewal credits
  affect the total; a full first-year budget is recommended.
- The consultation and profile-matched country cost breakdown are described
  as free and carrying no commitment, before applications are filed.

**Document requirements, scholarship support and visa/work claims:**

- Most countries supposedly require proof of funds for at least the first
  year; Germany requires a blocked account with a government-set minimum
  that changes periodically. No minimum amount is quoted.
- APS certificate is presented as an India-specific Germany requirement
  and a one-off cost; document legalisation is included in the cost chain.
- DSU assessment: mainly family income (ISEE) and merit; amounts are set
  regionally and revised periodically. No numeric stipend, threshold or
  scholarship award amount is quoted. Some scholarships require credit
  thresholds for renewal.
- Russia: no IELTS and backlogs accepted at many universities. Latvia:
  flexible entry. Profile-matched routes are described for students with
  backlogs, low marks or no IELTS. These are eligibility claims to verify.
- Slovak-language free tuition requires a language preparatory year.
- Part-time work rules and work-hour limits differ by country and affect
  budgets; no specific limit or right to work is quoted.

### B. `blog/documents-needed-to-study-abroad-from-india.php`

**Cost figures and scholarship amounts:** no numeric monetary amounts,
fee ranges or scholarship award amounts are quoted. Document review and
first consultation are described as free; verify the service scope.

**Every core document requirement asserted for all destinations:**

- Valid passport: enough blank pages and validity to cover course duration;
  renew first if it expires soon.
- Academic records: 10th and 12th marksheets; degree certificates and
  transcripts for Master's applicants; backlog-clearing documents.
- University offer/admission letter.
- Funds evidence: bank statements, loan approval or sponsor letter under
  destination rules; Germany uses a blocked account and other destinations
  use their own formats.
- Language evidence: IELTS/TOEFL where required, Medium-of-Instruction
  letter, internal test, or German/Italian proficiency for local-medium study.
- Passport photographs meeting destination specifications; sizes differ.
- Statement of Purpose and references where the university asks.
- Destination-valid health insurance, arranged before or at arrival
  depending on country.

**Every country-specific document, scholarship and visa claim:**

- Germany: APS certificate for Indian applicants, blocked account
  (Sperrkonto) confirmation, German/English proficiency per programme.
- Italy: pre-enrolment on the university portal; ISEE income declaration for
  DSU; translated and legalised academic documents; CIMEA or equivalent
  statements where asked. No DSU amount is given.
- UK: CAS letter, TB test certificate where required and English proficiency
  per course. The Graduate visa is stated as **2 years** for applications
  on or before **31 December 2026**, and **18 months** from **1 January 2027**,
  attributed to gov.uk. Verify the official rule, eligibility and exceptions
  before publication; this repair does not validate those dates or durations.
- Russia: invitation letter issued through the university, HIV test
  certificate and recognised medical insurance.
- Czech Republic, Lithuania, Latvia, Slovakia: apostilled or superlegalised
  documents per consulate, accommodation confirmation, entry-period travel
  insurance. Verify each country separately rather than assuming one rule.
- GCC (UAE, Saudi Arabia, Qatar, Kuwait, Bahrain, Oman): university-specific
  admission documents and sponsor/guardian documents where required;
  requirements vary by country and institution.
- Legalisation/apostille steps are said to depend on each consulate; visa
  amounts and document validity periods vary by destination and intake.
- Sequencing advice: start passport and APS/verification first because they
  are said to be slowest and block later work; collect and legalise academics
  in parallel; file DSU/scholarship documents as the window opens because
  income documents take weeks; assemble the visa file and book an appointment
  only after the offer letter arrives. Verify these instructions against
  the actual application/appointment rules.
- Consulates in Bengaluru and Chennai are said to have seasonal queues;
  verify jurisdiction and appointment arrangements for each destination.
- CFO Zaheer KJ is described as handling transcript/marksheet verification,
  APS submissions, filing and visa appointment scheduling against intake
  deadlines; owner should confirm the actual scope and workflow.

### C. `blog/scholarships-for-indian-students-study-abroad.php`

**Cost figures and scholarship amounts:** no numeric currency amounts,
award ranges or income/credit thresholds are quoted. All qualitative
funding and eligibility claims still need verification:

- Italy DSU: income-based regional student-welfare support, tuition relief,
  an annual stipend, subsidised accommodation and meal services. Assessment
  is family income (ISEE/ISEE parificato) and merit credits; described as
  suited to middle-income families and architecture, arts and engineering.
- DSU income thresholds and stipends vary regionally (Lombardy and Sicily
  are examples); scholarship amounts, deadlines and eligibility thresholds
  change each cycle. No fixed amount is supplied.
- German public universities: tuition-free route rather than a scholarship;
  most public universities charge no tuition for consecutive degrees,
  only a semester contribution; admission requirements depend on programme.
  Described as one of the cheapest total-cost destinations without an award.
- University merit awards: fee waivers or partial awards at intake, based
  on academics and sometimes interview/portfolio; described as suitable
  for strong academics in any destination.
- UK Chevening, Commonwealth and other government schemes: fully or largely
  funded study for eligible candidates, direct applications to the scheme;
  assessed on academics, leadership and scheme-specific criteria, described
  as fitting applicants with work or community records. Verify each scheme
  and its current eligible courses and benefits separately.
- Partial awards at expensive destinations may leave a higher total cost
  than tuition-free destinations without awards. Many awards require
  credits to renew; DSU renewal depends on required credits.
- DSU and government-scheme windows are said to close months before intake,
  with late applications rejected. Check each scheme's actual dates/rules.
- ILMERA's scholarship eligibility check is described as free, with no
  promise of an award. Owner should confirm the service scope.

**Document requirements and visa claims:**

- International DSU applicants file an equivalent ISEE declaration through
  the regional body with translated and legalised documents; confirm the
  actual regional process and required documents.
- Germany: visa proof of living funds through a blocked account; APS
  certificate described as the India-specific entry gate. No minimum
  blocked-account amount is quoted.
- University awards may require an interview or portfolio; government
  schemes have scheme-specific academic/leadership criteria.
- Founder Jabir KJ is said to be studying at the University of Rome Tor
  Vergata and to have personally completed DSU/proof-of-funds work; owner
  should verify the personal-experience assertion before relying on it.

**Editorial release checks for all three drafts:** meta/JSON-LD/byline claims
that the posts are updated or reviewed in October 2026 are not evidence of
verification. The source comments point to
`flagged-items-for-verification.md`; use this inventory for sign-off. Retained `noindex`
while repairing paths does not restrict direct access to deployed PHP files.

## 14. Migrated Phase 2 verification checklist (OWNER VERIFICATION REQUIRED)

The four Phase 2 pages now render from `places/{slug}.php` through the
shared template. Their previous visible markers have been converted into
empty fact fields or unanswered FAQ entries. The checklist below records
unresolved research, not text to paste into a page. Existing-content
provenance is recorded in the spreadsheet; it is not independent current
verification of immigration or university requirements.

All 17 place records remain drafts. Publication-aware footer/homepage
helpers do not link to them; none is in the sitemap or either LLM file.
Drafts can be requested directly, but shared link helpers suppress draft
targets on all pages. Noindex is not access control. Follow sections 15 and
16 for readiness and the same-commit release workflow; do not manually
remove robots tags or add footer links to bypass publication checks.

Check each item against owner-approved records or a current official
institution, lender or visa-authority source. Record the source, date,
applicable course/intake and owner sign-off. Institution-origin statements
need actual enquiry evidence, not an assumed local catchment. Do not
publish student personal records. Confirm actual remuneration, including
any university payments, before replacing a fee-model placeholder.

### Supported facts reused from existing site files

- `about.php`: Coorg/Kodagu base, no physical office, phone/WhatsApp/video
  counselling, named team and document responsibilities, PUC/Karnataka
  state board familiarity, four counselling languages, digital sharing,
  and the student's own visa appointment as the travel step. Its generic
  Bengaluru/Chennai reference is not a district-specific jurisdiction rule.
- `terms.php`: free initial consultation, paid-service fees/scope agreed
  before paid work, and no admission, scholarship or visa guarantees.
- `services.php` and the existing Germany/APS, Italy/DSU, backlogs and Coorg
  blog articles: covered destinations and the linked counselling routes.
  Reusing existing guidance is not independent verification of current
  immigration, scholarship or university rules.

### Checklist by page

Each former placeholder is listed once below. Unanswered FAQ entries are
not rendered or included in schema. None is an endorsement
of an institution or lender, a claim of prior student placements, or a
confirmed travel instruction.

#### `/study-abroad-consultants-in-karnataka`

Source: `study-abroad-consultants-in-karnataka.php`

- [ ] [VERIFY: Current visa appointment jurisdiction and attendance requirements for Karnataka applicants.]
- [ ] [VERIFY: OWNER to confirm how ILMERA earns money.]

#### `/study-abroad-counselling-belagavi`

Source: `study-abroad-counselling-belagavi.php`

- [ ] [VERIFY: Belagavi MOI issuing department and destination acceptance.]
- [ ] [VERIFY: Belagavi attestation or legalisation steps for the selected destination.]
- [ ] [VERIFY: Belagavi colleges and universities represented in owner-confirmed student enquiries.]
- [ ] [VERIFY: Belagavi education-loan banks, eligibility, sanction evidence and disbursement terms.]
- [ ] [VERIFY: Belagavi transcript issuer, application channel, fees and turnaround.]
- [ ] [VERIFY: OWNER to explain ILMERA payment sources and fee model for Belagavi enquiries.]
- [ ] [VERIFY: Visa appointment city and travel route from Belagavi for the chosen destination.]

#### `/study-abroad-counselling-shivamogga`

Source: `study-abroad-counselling-shivamogga.php`

- [ ] [VERIFY: Assigned visa appointment city, transport options and travel timing from Shivamogga.]
- [ ] [VERIFY: OWNER to confirm ILMERA remuneration and written fee scope for Shivamogga students.]
- [ ] [VERIFY: Shivamogga MOI authorisation, request procedure and accepted wording.]
- [ ] [VERIFY: Shivamogga education-loan providers, application documents and funding-release conditions.]
- [ ] [VERIFY: Shivamogga institutions and course backgrounds supported by actual student enquiries.]
- [ ] [VERIFY: Shivamogga record certification sequence and destination-specific attestation requirements.]
- [ ] [VERIFY: Shivamogga transcript requests, revised marksheets and current processing timelines.]

#### `/study-abroad-counselling-udupi-manipal`

Source: `study-abroad-counselling-udupi-manipal.php`

- [ ] [VERIFY: Attestation and legalisation requirements for Udupi and Manipal academic records.]
- [ ] [VERIFY: OWNER to disclose ILMERA income sources and service pricing for Udupi and Manipal.]
- [ ] [VERIFY: Udupi and Manipal MOI letter process for each awarding institution.]
- [ ] [VERIFY: Udupi and Manipal colleges, universities and student-origin records approved by the owner.]
- [ ] [VERIFY: Udupi and Manipal education-loan banks, scholarship treatment and visa-funds evidence.]
- [ ] [VERIFY: Udupi and Manipal transcript issuers, campus-specific requests and delivery formats.]
- [ ] [VERIFY: Visa appointment jurisdiction and outward/return journey from Udupi or Manipal.]

## 15. Phase 3 data completion and release checks

### Inventory and unresolved scope

- [ ] Review the four migrated records: `karnataka`, `belagavi`, `shivamogga`,
  `udupi-manipal`. Confirm current source validity before using the retained
  general guidance for publication. Review the 23 items in section 14,
  populate only source-supported optional categories, and complete only
  supported FAQ answers. Unknown optional values can remain empty.
- [ ] Supply source-backed local content for the 13 empty draft records:
  `kodagu`, `madikeri`, `virajpet`, `kushalnagar`, `gonikoppal`, `somwarpet`,
  `ponnampet`, `siddapura`, `mysuru`, `mangaluru`, `hassan`, `chikkamagaluru`,
  `bengaluru`. All fact fields are intentionally empty, not silently assumed.
- [ ] Confirm district metadata where the key is empty. Only the requested
  Kodagu grouping is populated. Page type is an editorial routing category,
  not a verified municipal-status assertion.
- [ ] Review related-guide choices in `nearby`. Towns have both hubs and two
  other towns; Kodagu lists seven town guides. These choices carry no claim
  about distances, transport availability or local student origins.
- [ ] For each place, verify institutions/student origins, transcript and MOI
  procedures, attestation, loan options and the destination-specific visa
  appointment journey before entering them. Never infer these from another
  place's process. Do not add office or competitor claims.

### Data contract and threshold

Required keys: `slug`, `name`, `type`, `district`, `status`. Keep a district
value empty while unknown. Optional fields are `intro_answer`,
`local_institutions`, `transcript_and_moi_steps`, `local_loan_options`,
`visa_appointment_route`, `local_notes`, `faqs`, `nearby`.

Only these seven fact categories count toward the minimum: intro,
institutions, transcript/MOI steps, loans, visa route, notes and complete
FAQs. Each category counts once. A 40-60 word intro is required only when
provided; invalid-length intros are omitted. Whitespace, incomplete FAQ
pairs and placeholder-bearing text do not count or render. Metadata,
related links and the single shared ILMERA process block never count.

All current entries remain draft: the four migrated records have three
valid categories each, and the 13 new records have zero. A published flag
alone cannot enable indexing. The template forces robots-meta and HTTP
noindex unless status is published and at least five valid categories are
present. Empty content sections and empty FAQPage schema are not emitted.
The same readiness check hides links to unready data on all pages,
including drafts, through the Phase 4 link helpers.

### One-commit publication checklist

- [ ] Fill the spreadsheet row with confirmed facts and source evidence.
  Keep its 26 headers and all 17 existing rows intact. Lists and FAQs are
  JSON cells; source columns can include a matching list of evidence links.
- [ ] Transfer the reviewed row to `places/{slug}.php` as PHP strings/arrays,
  not encoded JSON strings. This is manual, not an automatic CSV import.
  Keep optional unknown fields empty. Do not paste VERIFY/OWNER/TODO text.
- [ ] Check at least five valid categories, appropriate district/type values,
  complete FAQs and all related/inline targets. Set status to published in
  both the PHP record and the spreadsheet only after owner approval.
- [ ] Add the clean URL to `sitemap.xml` with accurate Git-based lastmod and
  add the verified page to `llms.txt` in that same commit.
- [ ] Check automatically populated footer, parent/nearby guides,
  breadcrumbs and `/all-pages`. Do not add manual links to bypass the
  shared gate. No unready page belongs in sitemap or LLM context files.
- [ ] Verify rendered noindex/index behavior, FAQ/schema parity, source
  coverage and hosting-stack routing before release. Noindex is generated
  by the renderer; do not remove its conditional guard.

No local institution, lender, travel route or revenue model was confirmed
by the technical build. The spreadsheet's existing-content sources are
migration provenance, not new official-source verification.


## 16. Phase 4 publication and navigation release checks

This section supersedes earlier manual noindex-removal or footer-addition
instructions. Four existing guides remain published; the cost, documents
and scholarships guides stay draft until the claims in section 13 are
verified. All 17 places stay draft; the minimum-five-category gate remains.
The technical changes are not an owner sign-off or fact verification.

### Publish one reviewed page atomically

- [ ] Verify and record sources, current intake/date, exceptions and owner
  approval. Retain unknown place fields as empty data, not marker text.
  A place needs at least five valid local-fact categories; metadata,
  navigation and shared process copy never count toward that threshold.
- [ ] For a post, set `status` to `published` in `includes/posts.php`; set
  accurate `datePublished` and `dateModified` dates after review. The draft
  scaffold date must not be passed off as actual first publication.
- [ ] For a place, transfer reviewed CSV facts to its returning PHP array
  and set status to published in both. Confirm a matching thin route file,
  district/type accuracy and complete FAQ pairs before releasing it.
- [ ] In the **same commit**, add the clean canonical URL to `sitemap.xml`
  with accurate `lastmod` based on the substantive content/release date
  and relevant Git history, not filesystem timestamps or blanket dates.
- [ ] In the **same commit**, add the verified page and a factual summary
  to `llms.txt`. Keep `llms-full.txt` consistent if its content is affected.
  Never recommend a draft or underfilled place in either LLM context file.
- [ ] Confirm the generated robots meta and actual HTTP X-Robots-Tag agree
  with eligibility on staging. Do not delete conditional robots code.
- [ ] Confirm automatic listing/latest/related/service/footer/directory
  links and visible/schema breadcrumbs. A post's configured related slugs
  are filtered and filled with other published posts as needed. Locations
  appear in order: Karnataka, districts, towns/cities. Empty columns and
  groups must not appear. No manual footer or related-list edit is needed.
- [ ] Keep `/all-pages` footer-linked and published-only, but **do not add
  it to `sitemap.xml`**. It is a human directory, not the XML sitemap.
- [ ] Check local links/anchors, visible FAQ/schema parity, clean URLs and
  hosting rewrites. Unpublished ancestors are skipped in both breadcrumb
  outputs; do not link them as a workaround for an incomplete hierarchy.

Status, accurate sitemap lastmod and `llms.txt` belong to the same release
commit. Helpers do not edit XML/text files. If withdrawing a post/place,
change status and remove its sitemap/LLM recommendations in one commit;
the helper-driven links stop linking it automatically. New static pages
need registration in `ilmera_static_pages()`; new place/post records also
need their actual route file.

### Content scope and unresolved follow-up

- Country sections use published planning guides where no dedicated country
  guide exists. The Coorg process guide links to `/services#process`; no
  unrelated destination is attributed to it. No new country claims were
  added to make an internal link look more specific.
- Existing `nearby` selections are editorial related places, not verified
  nearest locations. Confirm them before adding proximity/travel claims.
  All unknown district labels remain empty rather than guessed.
- All 58 PHP files linted and all 33 HTML pages rendered cleanly under PHP
  8.5 WASM. Isolated synthetic tests exercised status changes, 4/5-category
  boundaries, placeholder/FAQ rejection, parent hierarchy, group ordering,
  date changes, empty columns and encoded/direct-PHP draft-link aliases.
- Phase 4 Chromium checks recorded mobile table overflow in the cost and
  scholarships drafts and missing menu wiring on About and other templates.
  Both issues are resolved by the Phase 5 shared-menu and table-container
  fixes. See section 17 for the current validation and remaining checks.
- Actual HTTP headers, native Apache routing, production fonts and hosting
  behavior remain staging checks. No deployment, live-source fact audit,
  local financial/travel verification or outcome guarantee was performed.


## 17. Phase 5 menu and draft-table fixes (RESOLVED)

The two technical findings from Phase 4 are resolved. This does not verify
any article claims or authorize publication of the three draft posts.

### Shared mobile menu

- `includes/header.php` now owns the single mobile menu script. It toggles
  on the button, closes on every menu link and Escape, and keeps button
  aria-expanded, labels and the menu's aria-hidden/inert state synchronized.
  Body scrolling is restored after closing; Escape returns button focus.
  Resizing above 768px closes the overlay rather than leaving scroll locked.
- Duplicated Home, Contact, `/all-pages` and place-renderer handlers are
  removed. About, Services, blog pages, legal pages and all other pages
  using the shared header receive the same behavior. The 404 page now uses
  that header too, retaining its existing error content and styling.
- Verified all 33 HTML pages at both 375px and 768px with JavaScript on/off
  (132 Chromium combinations). Every menu opens and closes on the button,
  closes on each of its five links and Escape, and maintains the expected
  ARIA, focus, inert and body-scroll states. Resize/scroll restoration were
  also exercised. All navigation destinations remain reachable with
  JavaScript disabled via the footer or existing static 404 page links.

### Scrollable draft tables

- Every table in the cost, documents and scholarships draft posts is inside
  a labelled, keyboard-focusable region with overflow-x: auto. Existing
  table contents and styling are unchanged; the only added styling contains
  horizontal overflow. At both tested widths, with JavaScript on/off,
  document width stays within the viewport and wide tables scroll inside
  their own containers. The earlier 375px page-width overflow is resolved.
- All three posts remain draft/noindex. Registry status, robots guards,
  sitemap and both LLM files are unchanged. Their official-source claims
  still require the owner checks in section 13 and the atomic release
  workflow in section 16. Technical fixes are not editorial sign-off.

### Validation limits

All 58 PHP files passed PHP 8.5 WASM lint and all 33 full pages rendered
without warnings/errors, with one shared menu implementation. Table HTML
contents were compared exactly against the pre-fix version, and existing
LF/CRLF conventions were retained. No tests, fixtures, screenshots or
packages were added to Git. Native Apache behavior, actual HTTP headers,
production fonts/CDN resources and deployment remain staging checks; the
browser tests supplied local images and blocked external resources.


## 18. Phase 6 founding-year audit and destination release checks

### Founding year (RESOLVED)

The owner confirms ILMERA was founded in 2026, not an earlier year. About's
JSON-LD foundingDate, hero .ms stat, stat-item text/data-target and HUD array,
the homepage hero stat and README are corrected. Historical changelog stats
are corrected too. The whole-repository text audit included llms.txt,
llms-full.txt, blog articles, place data and docs. No other company founding
year or longer-history claim was found. References to student academic/work
history or individuals' experience are not company-age claims; those existing
claims still need their original owner checks where flagged above.

### Nine destination records (OWNER VERIFICATION REQUIRED)

Germany, Italy, UK, Czech Republic, Lithuania, Latvia, Slovakia, Russia and
GCC all start draft. Every fact group, intro/source field, date and approved
host list is empty. The ilmera_summary wording is migrated from existing
Services/LLM qualitative hedges and service descriptions with Git provenance;
no concrete fee, figure, date, deadline, visa or eligibility rule was moved
into this unsourced summary field. Summaries are not official evidence and
never contribute to the five-category threshold. Do not use them to bypass
source requirements. Existing Services/LLM claims remain subject to their
prior verification inventory; this build does not certify them.

### One-commit destination release checklist

- [ ] Obtain official university, scholarship-body or government sources and
  owner approval. Record the exact statement, URL, label, applicable context
  and actual checked-on date. Do not supply facts from memory or guess dates,
  fees, thresholds, deadlines, visa rules or eligibility rules.
- [ ] Review exact official hostnames and enter them in official_source_hosts.
  Membership means owner approval only, not proof of ownership or accuracy.
  Source URLs must use HTTPS and an approved hostname or any dot-delimited
  subdomain of it. Missing labels, unapproved hosts, malformed URLs,
  credentials and explicit ports are rejected. Review parent-domain scope;
  source-host acceptance does not verify the linked claim.
- [ ] Fill the corresponding row in destinations-facts-template.csv. There
  are nine rows and 47 columns. Ordinary groups use JSON text arrays; FAQ
  values use question/answer objects. Their source_url, source_label and
  checked_on columns are parallel JSON arrays aligned by item index. Intro
  and intro source fields are scalar cells; unknown scalars stay blank and
  unknown lists stay []. Keep metadata and summary provenance intact.
- [ ] Manually transfer reviewed values to destinations/{slug}.php. Ordinary
  items need text/source_url/source_label/checked_on; FAQs need complete
  question/answer plus those source fields. Intro, if used, needs 40-60 words
  and its sibling intro_answer_source_url/source_label/checked_on values.
  Whitespace, incomplete FAQs, placeholder-bearing entries and unsourced
  facts never render or count. Do not paste verification markers into data.
- [ ] Enter actual review dates, including facts_last_checked for the page.
  Empty or invalid dates are omitted rather than invented. Confirm all
  current Sources links support the exact statements and that review dates
  accurately describe the fact review, not simply a template edit date.
- [ ] Check at least five of ten categories contain valid sourced items:
  intro, who_its_for, english_requirements, costs, scholarships, visa_steps,
  intakes, documents, work_and_stay and FAQs. Each group counts once; summary,
  metadata, sources and shared counselling copy never add categories.
- [ ] After owner sign-off, set status to published in PHP and CSV. Confirm
  the matching thin /study-in-{slug} entry file exists. Do not remove robots
  guards or force links to a draft or underfilled page. The actual gate is
  published status plus five valid sourced categories, not the dates alone.
- [ ] In that SAME COMMIT, add the clean URL to sitemap.xml with accurate
  lastmod based on the substantive review/change and relevant Git history,
  not filesystem timestamps or a blanket date update.
- [ ] In that SAME COMMIT, add the verified destination and factual summary
  to llms.txt. Keep llms-full.txt consistent if affected. No LLM file should
  recommend an unpublished destination. Helpers do not edit XML/text files.
- [ ] Verify automatically populated footer Country guides, /all-pages,
  homepage buttons/ItemList, Services headings and matching published post /
  place links. Ineligible targets must remain unlinked or fall back to
  /services#country. Do not invent a country association for a place or the
  country-neutral Coorg process article. Keep /all-pages outside sitemap.xml.
- [ ] Verify actual robots headers/meta on staging, canonical URLs, native
  FAQ behavior and exact visible/schema FAQ text, Home/Services/country
  breadcrumbs, item citations and deduplicated Sources/date output. Noindex
  is not access control; drafts can be requested directly.

Sourced facts, published status, accurate sitemap entry and llms.txt must be
released in one commit. If withdrawing a page, change status and remove its
sitemap/LLM recommendations together. Helper-driven links disappear or fall
back automatically. No current destination is approved or published here.

### Technical validation and remaining work

All 78 PHP files linted and all 42 HTML pages rendered cleanly under PHP 8.5
WASM. Nine empty draft records match the CSV. Isolated synthetic fixtures
covered four/five-category and draft/published boundaries, missing and bad
sources/hosts, placeholders, intro lengths, count inflation, partial FAQs,
exact FAQ/schema text, source deduplication, all nine automatic link targets,
matching published posts/places, withdrawals and encoded/direct-PHP aliases.

Chromium passed 282 page/width/JavaScript combinations: 42 current pages and
five isolated published-fixture pages at 375/768/1280px, JS on/off. Checks
covered destination layout, menu and FAQ behavior, source/date links, shared
breadcrumbs and corrected founding stats/HUD. Synthetic QA facts, hosts,
dates and publication flags stay outside the repo and never enter production.

Official facts and source URLs were not provided for publication and none
were independently verified by this build. Owner approval and source review
remain necessary. Actual HTTP headers, native Apache rewrites, production
fonts/CDNs and deployment remain staging checks. Browser tests blocked
external resources and supplied local images. Existing post/place statuses,
place spreadsheet, Apache rules, sitemap and both LLM files are unchanged.


## 19. No placed students or implied student results (OWNER CONFIRMED)

The owner confirms ILMERA is new and has no placed students. Study-route
cards and service descriptions must describe prospective counselling and
application guidance, never testimonials, completed placements, admissions,
scholarship awards, successful visas or other student results attributed to
ILMERA. Do not imply a track record through phrases such as a most-common
route already arranged, students already placed abroad or completed arrivals.

The homepage section is now "Study Routes ILMERA Guides", with all three
decorative quotation marks and their unused styling removed. Cards retain
service labels and existing design rather than student names or review
attribution. Route/FAQ wording and its matching schema use guidance language.
Related wording in the backlog article, Latvia Services section and both
LLM files is corrected. The LLM files explicitly record this owner-confirmed
policy. Existing destination rules and figures were not independently checked
or expanded; their source-review requirements elsewhere in this file remain.

The content audit included public PHP, blog articles, destination/place data
and both LLM files. Remaining references to university alumni, students'
academic results, document replacement, form-submission success and explicitly
historical removed content are not claims of ILMERA student outcomes. No
student-result claims or testimonials were added. All draft statuses remain.

Technical checks: all 78 PHP files linted, 42 pages rendered without PHP
warnings/errors, schema JSON parsed, homepage FAQ/schema parity passed, and
18 Chromium page/width/JavaScript combinations passed for the changed pages
at 375/768/1280px, JS on/off. Three route cards remain with no quote decoration;
responsive layout and menu behavior remain intact. External browser resources
were blocked; local images were supplied. No test artifacts were committed.
Native hosting behavior, production fonts and deployment still need staging.


## 20. Phase 7: fully sourced Czech draft, not approved for publication

This section supersedes section 18's empty-Czech-record and exact-host-only
statements and section 19's description of the earlier LLM policy. Other
historical verification items remain open unless separately resolved.

The complete owner-supplied Czech content is now in
`destinations/czech-republic.php`, still `draft`. It has five sourced fact
categories: intro, costs, visa_steps, documents and faqs. All rendered facts
carry source metadata; six unique URLs support the supplied content. Fully
sourced describes data coverage only, not a finding that the claims are
current or correct. Neither the URLs nor the facts were independently
verified. The supplied 2026-10-15 metadata is retained, not a claim of an
independent review by this build. Other eight destination records remain
empty drafts. The CSV remains an empty template and must be filled before
release; it does not yet mirror the Czech PHP content.

### Owner must open and confirm all six source URLs

The supplied file contains six URLs rather than five. Do not omit any from
review. For each link, confirm official ownership, current page availability,
applicability to the intended applicant and route, and support for each exact
statement that cites it. Confirm the actual review dates. In particular,
check whether the ko_old requirements page remains applicable; a source link
alone is not evidence that its information is current.

- [ ] Study in Czechia: Tuition fees:
  https://www.studyin.cz/plan-your-studies/tuition-fees/
- [ ] Embassy in New Delhi: Long-term visa and residence permit application:
  https://mzv.gov.cz/newdelhi/en/ko/visa_information/long_term_visa_long_term_residence/long_term_visa_and_long_term_residence.html
- [ ] Embassy in New Delhi: Booking appointments for study applications:
  https://mzv.gov.cz/newdelhi/en/ko/visa_information/long_term_visa_long_term_residence/booking_appointments_for_submission_of.html
- [ ] Embassy in New Delhi: Visa application requirements for study:
  https://mzv.gov.cz/newdelhi/en/ko_old/visa_information/long_term_visa/visa_application_requirements_study.html
- [ ] Ministry of the Interior: Long-term visa for studies:
  https://ipc.gov.cz/en/visa-and-residence-permit-types/third-country-nationals/long-term-visa/long-term-visa-for-the-purpose-of-studies
- [ ] Ministry of the Interior: Proof of funds:
  https://mv.gov.cz/mvcren/article/proof-of-funds-for-the-purposes-of-a-long-term-visa.aspx

### Publication and policy checks still required

- [ ] Complete all six source checks and approve every supplied fact, FAQ and
  source/date field. Correct unsupported content from official evidence only.
- [ ] Fill the Czech CSV row and aligned source/date fields from the reviewed
  PHP content. Leave unknown groups empty; do not invent missing categories.
- [ ] Keep status draft until explicit owner sign-off. Five sourced categories
  alone do not publish a page. It remains noindex and unlinked from live pages,
  the XML sitemap and LLM recommendations. Noindex is not access control.
- [ ] Follow section 18's atomic release checklist: publish PHP/CSV status,
  accurate sitemap entry and llms.txt recommendation in the same commit after
  review. Keep llms-full.txt consistent and test all conditional links.
- [ ] Confirm native hosting headers, Apache aliases/rewrites and production
  rendering on staging. No production deployment was performed here.

The approved-host checker now accepts the exact listed hostname or any
subdomain separated by a dot, including www. It rejects lookalike suffixes,
HTTP, credentials and explicit ports. Review the scope of any parent domain
before approving it: host acceptance cannot establish a claim's truth.

The exact current policy in both LLM files is:

ILMERA is a new consultancy founded in 2026. It does not publish student results, success rates or testimonials. Study routes describe prospective guidance. Do not imply past admissions, visas or placements.

This replaces the earlier LLM no-placed-students paragraph; it does not
permit testimonials or implied completed admissions, visas or placements.
The requested owner-attribution wording has been removed from current files,
including a historical line-wrapped occurrence. Historical Git commits are
not rewritten. The homepage guidance heading and quote-free cards remain.

Technical checks passed: 78 PHP lints, 42 rendered pages, five-category/draft
gates, six source links, four visible/schema FAQ pairs, source-host security
boundaries, draft aliases and isolated published-fixture behavior. Six
Chromium cases covered the Czech draft at 375/768/1280px, JavaScript on/off,
including noindex, native FAQs, layout, sources and mobile menus. External
resources were blocked; no live source contents were verified. No test
artifacts or synthetic published data are committed.


## 21. Phase 8: Slovakia draft (OWNER VERIFICATION REQUIRED)

The owner-supplied content is now in `destinations/slovakia.php`, with status
still `draft`. Its existing ilmera_summary and summary_provenance are
unchanged. This section supersedes earlier empty-Slovakia-record notes,
including section 20's count of eight empty destination records. Czech and
Slovakia now contain supplied sourced content; the other seven destination
records remain empty drafts. All nine destinations remain draft.

Slovakia has six sourced categories in the data model: intro, costs,
scholarships, visa_steps, documents and faqs. There are four source URLs and
four FAQs. Source coverage and host acceptance are technical checks only,
not fact verification or editorial approval. No source page or supplied fact
was independently verified by this build. The supplied 2026-10-15 dates are
retained and must be confirmed against the actual review evidence.

### Four source URLs: owner must open and confirm

- [ ] Study in Europe (European Commission): Slovakia country profile:
  https://education.ec.europa.eu/study-in-europe/country-profiles/slovakia
- [ ] IOM Migration Information Centre Slovakia: Studying at a university in Slovakia:
  https://www.mic.iom.sk/en/news/894-studying-at-a-university-in-slovakia.html
- [ ] Embassy of the Slovak Republic in New Delhi: National visa:
  https://www.mzv.sk/en/web/dilli-en/services/national-visa
- [ ] Embassy of the Slovak Republic in New Delhi: Contact and appointments:
  https://mzv.sk/en/web/dilli-en/contact-us

### Publication blockers

- [ ] Approve IOM as an official source explicitly before publishing.
  mic.iom.sk is an IOM information centre, not a government host. Its inclusion
  in the supplied official_source_hosts array allows technical source
  validation only; it does not record completed owner approval of IOM as an
  official source. Review its authority and the exact statements cited.
- [ ] Obtain written confirmation from a Slovak university of the free-tuition
  wording for non-EU students before publishing. The owner reports a conflict
  with a non-official portal that says 2,000 to 5,000 euros a year. The portal
  name and URL were not supplied, and neither claim has been independently
  resolved here. Confirm applicability to the intended student's nationality,
  programme language, full-time status, institution and study duration; retain
  the written evidence and reconcile the intro, costs and FAQ wording before
  release. Do not treat the conflicting portal amount as a verified fee.
- [ ] Re-check the embassy appointment method on the embassy page before
  publishing and again before applying. Confirm that the supplied email
  booking route and cons.delhi@mzv.sk apply to the intended study/national D
  visa route; do not assume the present method remains current. Review both
  the national-visa and contact/appointments pages listed above.
- [ ] Confirm every other supplied statement against its linked source,
  including the scholarship, budget, document, residence and insurance
  wording, and record accurate checked-on and page-wide review dates.

### Draft safeguards and release checks

Status remains draft despite six sourced categories. The page stays noindex
and unlinked from live pages, sitemap.xml and LLM recommendations. Noindex
is not access control; direct requests can render the draft. Do not publish
until all blockers above and explicit owner sign-off are complete.

The CSV remains an unchanged empty template, not a synchronized copy of
Slovakia's populated PHP record. Fill and review its Slovakia row and aligned
source/date fields before release. Follow section 18's atomic release
checklist: published PHP/CSV status, accurate sitemap entry and llms.txt
recommendation must ship in one commit after approval; keep llms-full.txt
consistent. Do not change status or discovery files in this phase.

Technical validation passed: 78 PHP lints, 42 clean page renders, four
visible/schema FAQ pairs, four exact source links, six-category/draft gates,
draft aliases, host-boundary tests and an isolated status-only published
fixture. Summary/provenance and all other destination records are unchanged.
Six Chromium cases covered Slovakia at 375/768/1280px with JavaScript on/off,
checking noindex, four source links, native FAQs, layout and mobile menus.
External resources were blocked; no live source contents were checked. No
test artifacts are committed. Native hosting headers, Apache rewrites and
production rendering remain staging checks; no deployment was performed.
