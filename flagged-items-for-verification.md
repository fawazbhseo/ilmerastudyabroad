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


## 22. Phase 9: Lithuania draft (OWNER VERIFICATION REQUIRED)

The complete supplied content is now in `destinations/lithuania.php`, still
`draft`, with ilmera_summary and summary_provenance preserved exactly.
Lithuania has five sourced categories in the data model: intro, costs,
visa_steps, documents and faqs. Three source URLs and four FAQs are present.
Five categories alone do not authorize publication. Technical source-host
acceptance is not editorial approval or evidence that a statement is current.
No source page or supplied fact was independently verified by this build.
The supplied 2026-10-15 dates are retained, not an independent review date.

This section and section 23 supersede earlier empty-Lithuania/Latvia notes,
including section 21's count of seven empty records. Czech, Slovakia,
Lithuania and Latvia now contain supplied sourced content; the other five
destination records remain empty drafts. All nine destinations remain draft.

### Lithuania source URLs: owner must open and confirm all three

- [ ] Migration Department of Lithuania: Services for persons abroad, Republic of India:
  https://migracija.lrv.lt/en/structure-and-contacts/information-for-visitors/services-for-persons-abroad/temporary-residence-permit-and-national-visa-services/republic-of-india/
- [ ] Study in Europe (European Commission): Lithuania country profile:
  https://education.ec.europa.eu/study-in-europe/country-profiles/lithuania
- [ ] VILNIUS TECH: Immigration regulations for full-time students:
  https://vilniustech.lt/en/international-students/immigration-regulations/immigration-regulations-full-time/

### Lithuania publication blockers

- [ ] Obtain explicit owner approval of vilniustech.lt as an official source.
  It is a university page, not a government host. Inclusion in the supplied
  official_source_hosts array allows technical validation only; it does not
  mean that owner approval has been completed.
- [ ] Resolve the reported conflict between the university's temporary
  residence permit guidance and the European Commission page, which still
  describes a national visa. Confirm the current process on the Migration
  Department page for India listed above before publishing. Reconcile the
  visa_steps and FAQ wording from current authoritative evidence; do not
  present technical acceptance of both sources as resolution of the conflict.
- [ ] Proof-of-funds and insurance minimums were deliberately left out because
  university sources gave different numbers. Do not add a minimum from memory
  or select one of the conflicting numbers without verification. Confirm the
  current requirements with the Migration Department and applicable official
  sources before adding any figures. The supplied generic funds/insurance
  wording is not a verified minimum.
- [ ] Confirm the remaining supplied tuition, living-cost, programme-count,
  service-fee, service-point, MIGRIS and document statements against the exact
  sources, including applicability to the intended student and route. Confirm
  accurate item and page-wide review dates before release.


## 23. Phase 9: Latvia draft (OWNER VERIFICATION REQUIRED)

The complete supplied content is now in `destinations/latvia.php`, still
`draft`, with ilmera_summary and summary_provenance preserved exactly.
Costs is intentionally empty: no official tuition figure was supplied as
verified evidence. The page has four sourced categories (intro, visa_steps,
documents and faqs), three source URLs and four FAQs. It cannot reach the
five-category publishing gate with its current data, even if status were
changed to published. Do not change status in this phase.

No source page or supplied fact was independently verified by this build.
The supplied 2026-10-15 dates are retained and need confirmation against the
actual review evidence. The supplied European Commission URL retains its
/fi/ path exactly; the owner must check its content and current applicability.

### Latvia source URLs: owner must open and confirm all three

- [ ] Embassy of Latvia in India: Long stay visa for students, Indian nationals:
  https://www2.mfa.gov.lv/en/newdelhi/consular-section/applying-for-a-long-stay-visa/students/indian-nationals
- [ ] Embassy of Latvia in India: Long stay visa for students:
  https://www2.mfa.gov.lv/en/newdelhi/consular-section/applying-for-a-long-stay-visa/students
- [ ] Study in Europe (European Commission): Latvia country profile:
  https://education.ec.europa.eu/fi/country-profiles/latvia

### Latvia publication blockers

- [ ] Add an official tuition source and at least one more sourced category
  before publishing. A reviewed, sourced Costs category can supply the fifth
  category. Do not invent a tuition amount, split an existing group to inflate
  the count, or use the ILMERA summary as an extra category. Costs stays empty
  until official evidence is obtained and approved.
- [ ] Re-confirm the Hello Verify and VFS steps on the embassy pages above
  before publishing and again before applying. Check verification and
  transaction-number requirements, appointment booking, service points,
  interview arrangements and application submission. Do not assume the
  supplied workflow remains current.
- [ ] Confirm the remaining supplied visa validity, residence-permit and
  insurance/document statements against their exact sources, including the
  intended applicant and route. Verify accurate item/page review dates.

### Draft safeguards and release checklist for both pages

Both pages remain draft, noindex and unlinked from live pages, sitemap.xml
and LLM recommendations. Noindex is not access control; direct requests can
render these drafts. The CSV remains an unchanged empty template and does
not yet mirror either populated PHP record.

Before any publication, resolve all source/process blockers and obtain
explicit owner sign-off. Fill the reviewed CSV rows with aligned source/date
fields, meet the five-category threshold and follow section 18's atomic
release checklist: published PHP/CSV status, accurate sitemap entry and
llms.txt recommendation in the same commit, with llms-full.txt consistent.
Do not force links to drafts or bypass the existing guards.

Technical validation passed: 78 PHP lints, 42 clean renders, exact preserved
summary/provenance lines, all six source URLs, eight visible/schema FAQ pairs,
draft aliases, no incoming links to drafts and exact/subdomain host-boundary
checks. Isolated status-only published fixtures confirmed that Lithuania
passes the technical gate while Latvia remains blocked at four categories;
repository statuses were never changed. Twelve Chromium cases covered both
pages at 375/768/1280px with JavaScript on/off, checking noindex, sources,
all FAQs, conditional Costs sections, layout and mobile menus. External
resources were blocked and no live source contents were checked. No test
artifacts are committed. Native hosting headers, Apache rewrites and
production rendering remain staging checks; no deployment was performed.


## 24. Phase 9: Services university-dependent claims (OWNER VERIFICATION REQUIRED)

The following current services.php claims need university-source verification
or softer wording. This phase records the blockers; it does not certify or
change these live claims:

- [ ] "IELTS Not Mandatory" for Russia, Lithuania and Latvia. Requirements
  depend on each university and programme. Verify with applicable university
  sources or soften the wording so it does not imply a country-wide waiver.
- [ ] "Lowest Tuition Fees" for Czech, Lithuania, Latvia and Russia. Fees
  depend on the university and programme. Verify with university sources or
  soften/remove the unsupported lowest-price comparison.
- [ ] The FAQ "What is the cheapest country to study abroad?" names Czech
  Republic, Lithuania, Latvia, Russia and Slovakia as among the most affordable
  and describes Germany's public-university tuition. Verify the named-country
  affordability and tuition claims with university sources or soften the
  wording rather than treating a country ranking as a universal fee promise.
  If the visible FAQ is revised, update its matching FAQPage answer too.

These checks do not authorize publishing either destination draft. Existing
Services content and its schema are unchanged and remain subject to review.


## 25. Phase 10: Germany draft (OWNER VERIFICATION REQUIRED)

The complete supplied content is now in `destinations/germany.php`, still
`draft`, with its existing ilmera_summary and summary_provenance preserved
exactly. It has five sourced categories (intro, costs, documents,
work_and_stay and faqs), one source URL and four FAQs. Five categories alone
do not authorize publication. Host acceptance and source coverage are
technical checks, not fact verification or editorial approval.

### Germany source URL: owner must open and confirm

- [ ] DAAD: Costs of education and living in Germany:
  https://www.daad.de/en/studying-in-germany/living-in-germany/finances/

### Germany publication blockers and missing official sources

- [ ] The supplied DAAD facts came from search snippets, not a confirmed
  full-page review. The owner must open the DAAD page and confirm every line
  of the intro, costs, documents, work wording and FAQs before publishing.
  Pay particular attention to the Technical University of Munich (TUM) fee
  amounts and whether the master fee is per semester. Confirm the applicable
  students, programmes, exceptions and current amounts from official sources;
  do not treat a snippet or the supplied review date as verification.
- [ ] Obtain an official German source for the blocked account amount. It was
  left out because no official source was confirmed. Do not invent the amount
  or infer that a generic proof-of-finances statement supplies it.
- [ ] Obtain an official German source for the APS certificate requirement
  for Indian applicants. It was left out because no official source was
  confirmed. Verify applicability before adding any requirement or exception.
- [ ] Record accurate source/item and page-wide review dates after the actual
  checks. The supplied 2026-10-15 metadata is retained, not a claim that this
  build independently reviewed the source page.


## 26. Phase 10: UK draft (OWNER VERIFICATION REQUIRED)

The complete supplied content is now in `destinations/uk.php`, still `draft`,
with its existing ilmera_summary and summary_provenance preserved exactly.
It has four sourced categories (intro, costs, documents and faqs), one source
URL and four FAQs. It remains below the five-category threshold, even with
an isolated published flag. Do not add a category without official evidence.

### UK source URL: owner must open and confirm

- [ ] GOV.UK: Financial evidence for Student and Child Student visa applicants:
  https://www.gov.uk/guidance/financial-evidence-for-student-and-child-student-route-applicants

### UK publication blockers and missing official coverage

- [ ] The supplied research records that all amounts were read from GOV.UK
  on 2026-10-15 and have changed before. Recheck all amounts on the day of
  publishing, including the London/outside-London living costs and applicable
  duration, and reconcile the intro, costs and FAQs. This build has not
  independently repeated that source review; supplied dates remain unchanged.
- [ ] Confirm the "India is not on the exempt list" FAQ again at publishing.
  It rests on the absence of India from the GOV.UK list, not an explicit
  India-specific rule in the supplied evidence. Check the current list and
  the distinction between providing financial evidence upfront and meeting
  the financial requirement. Keep the visible FAQ and schema consistent.
- [ ] Obtain official GOV.UK sources for visa application steps, which were
  not covered by the supplied financial-evidence page content.
- [ ] Obtain official GOV.UK sources for visa application fees and the health
  surcharge, which were not covered. Do not add amounts from memory.
- [ ] Obtain official GOV.UK sources for processing time and any TB test
  requirement, neither of which was covered. Verify applicability to the
  intended applicant and route rather than assuming a universal requirement.
- [ ] Confirm the remaining supplied financial evidence, accepted account/
  funds rules and timing statements, and record actual item/page review dates.


## 27. Phase 10: Italy draft (OWNER VERIFICATION REQUIRED)

The complete supplied content is now in `destinations/italy.php`, still
`draft`, with its existing ilmera_summary and summary_provenance preserved
exactly. It has four sourced categories (intro, visa_steps, documents and
faqs), one source URL and four FAQs. Costs is intentionally empty because no
official tuition source was found in the supplied research. The page cannot
reach the publishing gate with the current four categories; add reviewed,
officially sourced tuition content before any publication.

### Italy source URL: owner must open and confirm

- [ ] Consulate General of Italy in Bengaluru: Study in Italy:
  https://consbangalore.esteri.it/en/servizi-consolari-e-visti/servizi-per-il-cittadino-straniero/study-in-italy/

### Italy publication blockers

- [ ] Confirm the current-intake version of the official study visa checklist.
  The supplied content references 2025-2026, which must not be assumed to be
  the correct version for a future/current intake. Review and update the
  document wording from the consulate's applicable official checklist.
- [ ] Add an official tuition source and reviewed Costs items before
  publishing. Costs stays empty until evidence is obtained; do not invent
  fees or count the ILMERA scholarship summary as a sourced category.
- [ ] Confirm the VFS centre list and the video interview rule on the
  consulate page before publishing. Check that the supplied Bangalore,
  Chennai and Hyderabad list and mandatory video-interview wording remain
  current and applicable to the intended applicant and route.
- [ ] Confirm all other supplied admission, Universitaly, visa, processing,
  DOV and email-safety statements against the source page. Verify actual
  source/item and page-wide review dates. The supplied 2026-10-15 dates do
  not represent an independent source review by this build.

- [ ] Phase 12 owner claim: the owner has described Italian study as having
  tuition covered by scholarships of up to 8,000 euros at ILMERA partner
  institutions. No official source for that amount was found in the supplied
  research. The owner must supply the relevant institutional scholarship
  pages or written confirmation, including eligibility, coverage and amount.
  Keep the claim conditional until supported, not a country-wide fee promise
  or a record of completed awards to ILMERA students. No institution is named
  and no amount is added to the Italy destination data in this phase.

### Shared draft safeguards and release checks for all three pages

Germany, UK and Italy remain draft, noindex and unlinked from live pages,
sitemap.xml and LLM recommendations. Noindex is not access control; direct
requests can render the drafts. None of the three source pages or supplied
facts was independently verified by this build. Existing verification
blockers elsewhere in this file, including the Services claims, remain open.

The CSV is still the unchanged empty template, not a synchronized copy of
these populated PHP records. Resolve all blockers, fill reviewed CSV rows
with aligned sources/dates, meet the five-category threshold and obtain
explicit owner sign-off before release. Follow section 18's atomic release
checklist: publish PHP/CSV status, accurate sitemap entry and llms.txt
recommendation in one commit, keeping llms-full.txt consistent. Do not bypass
robots/link guards or force links to drafts.

This phase supersedes earlier empty-Germany/UK/Italy descriptions and counts:
seven destinations now have supplied sourced content; only Russia and GCC
remain empty. All nine destination statuses remain draft.

Full technical checks were repeated after each of the four tasks: 78 PHP
lints, 42 clean page renders and 252 Chromium page/width/JavaScript cases per
task (375/768/1280px, JavaScript on/off). Checks covered all pages' headings,
robots and mobile menus, destination native FAQs/source links/layout,
conditional Costs sections, exact summary/provenance retention, all nine
draft gates, source-host boundaries, aliases and absence of incoming draft
or discovery links. Germany has five categories; UK and Italy each have
four. Isolated published-data fixtures confirmed the five-category boundary
without changing repository status. External browser resources were blocked;
no live source contents were checked. No test artifacts are committed.
Native HTTP headers, Apache rewrites and production rendering remain staging
checks; no deployment was performed.


## 28. Phase 10: Russia and GCC not started (OWNER INPUT REQUIRED)

Russia and GCC have not been started: their existing empty draft records,
summaries and provenance are unchanged. They are not approved for publication.

- [ ] Russia needs official Russian or Indian government sources before
  adding facts. No fees, eligibility, visa or other rules should be supplied
  from memory or non-official snippets.
- [ ] GCC needs the owner to name which countries to cover before research
  or content population. Do not assume that one visa, fee or education rule
  applies across GCC countries or invent a country list.


## 29. Free-tuition claims to verify

Phase 11 task 2 is a read-only audit of site copy: no service, homepage,
About, blog, place or LLM content was edited. Locations below use 1-based
source-file line numbers at the Phase 11 audit, not rendered HTML lines.
Each code block reproduces the full source line exactly, including markup,
entities and PHP escaping, without its line terminator. Metadata and schema
are listed separately from visible text, even when wording repeats.

Source position from the supplied research so far, not a fresh verification:

- Germany has no tuition at most state universities, with exceptions such as
  Baden-Wurttemberg for non-EU students and TUM, and a semester contribution.
- Slovakia is free only for Slovak-language study. Do not present a branch
  label alone as proof that an English-taught programme is tuition-free.
- Italian institutions set their own tuition, and no official source for
  free tuition has been found. Existing DSU tuition-cover/waiver statements
  are conditional scholarship claims to verify, not evidence that Italy is
  free by default. This audit does not establish scholarship entitlement.

Review these statements with applicable government/university sources before
reusing them as verified claims. Qualified wording, negative qualifications,
conditional scholarship statements and contextual questions/headings are
retained to avoid hiding relevant wording. The label "unsure" means the line
is generic or combines countries/options so attribution to Germany, Italy
or Slovakia is unclear; it is not a determination that its statement is true.
"Reference only" means a slug/URL or guide reference, not an independent
free-tuition assertion. Ordinary free-consultation offers, IELTS waivers,
Schengen travel and GCC tax-free wording are not free-tuition claims and are
excluded unless the same line also contains relevant education wording.

### Audit coverage and shared content

Searched services.php, index.php, about.php, both LLM files, all seven blog
posts plus the blog index, all 17 place data files, all 17 thin place entry
pages and the shared place renderer. Search covered free/tuition-free/free
education, no/zero tuition, fee waivers/exemptions and tuition coverage,
followed by contextual review of the tuition lines. The place entries are
thin includes, with no independent tuition assertions. Their direct matches
below are guide-URL references, not new prose claims. The shared place
renderer's free offer is for consultation only. Empty place drafts contain
no tuition claims.

Also inspected includes/posts.php because its titles/excerpts and related-
guide data supply blog listings and place-page guide cards. Those shared
source locations are included separately rather than pretending the thin
entry files contain literal titles. A title/excerpt reference does not mean
it renders on every page; publication guards and related-guide selection
still apply. Blog documents/backlogs/Coorg pages had no independent literal
free-tuition prose beyond references listed here or shared guide content.

Model disclosure: this report was prepared using Arena.ai Agent Mode.
The underlying model identity is not disclosed.

### Exact source-line inventory

- `about.php:18` | claim or related tuition wording

```text
<meta name="keywords" content="study abroad consultant India, ILMERA Study Abroad, overseas education consultant, study in Germany free, study in Italy, study abroad with backlogs, low marks study abroad, student visa assistance, study in Europe from India, MBBS abroad, study in UK, Czech Republic universities"/>
```

- `about.php:136` | claim or related tuition wording

```text
        "Free tuition public universities in Germany",
```

- `about.php:671` | conditional or qualified wording

```text
      <p style="font-size:16px;font-weight:300;color:var(--grey-dark);line-height:1.78;margin-bottom:22px;">The most common questions we get from Coorg are about studying with a low PUC percentage, routes that skip IELTS, and free or near-free tuition. Public universities in Germany charge little to no tuition but require an <a href="https://www.aps-india.de/" rel="nofollow noopener" style="color:var(--navy);">APS certificate</a> from Indian applicants and proof of funds in a blocked account. Italy's regional DSU scholarships are income-assessed via ISEE and can cover tuition plus a living stipend. Russia, Slovakia, Lithuania and Latvia accept lower percentages and backlogs and frequently waive IELTS. Which of these fits depends entirely on your actual marksheet, which is what the free consultation is for.</p>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:150` | claim or related tuition wording

```text
    <p><strong>Short answer:</strong> the cheapest destinations for Indian students are usually the Czech Republic, Lithuania, Latvia, Slovakia and Russia, while German public universities charge little to no tuition regardless of nationality. But tuition is only part of the bill: living costs, visa funds, insurance and travel decide whether a destination is genuinely affordable for your family. This guide breaks down each of the nine destinations ILMERA works with, what drives the cost, and what you must budget beyond tuition.</p>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:157` | claim or related tuition wording

```text
      <li><strong>Tuition or semester contribution:</strong> from zero at most German public universities to substantial fees at UK universities; ranges vary by destination and programme.</li>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:170` | claim or related tuition wording

```text
        <tr><td>Germany</td><td>Little to no tuition at public universities; semester contribution applies</td><td>Moderate; blocked account required</td><td>Engineering, IT, tuition-free degrees</td></tr>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:171` | conditional or qualified wording

```text
        <tr><td>Italy</td><td>Public universities charge tuition; regional DSU scholarships can cover it and add a stipend for eligible students</td><td>Moderate, lower in smaller cities</td><td>Scholarship-driven students, arts and engineering</td></tr>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:175` | claim or related tuition wording

```text
        <tr><td>Slovakia</td><td>Free in some Slovak-language branches; paid English programmes</td><td>Low</td><td>Free-education routes, medicine</td></tr>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:183` | context heading/question

```text
    <h2>Where the Free-Education Routes Actually Apply</h2>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:184` | context heading/question

```text
    <p>Two of the nine destinations can genuinely approach zero tuition:</p>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:186` | claim or related tuition wording

```text
      <li><strong>Germany:</strong> most public universities charge no tuition for consecutive degrees; you pay a semester contribution and prove living funds through a blocked account. A few states levy fees in specific cases, so ILMERA checks the rule for each university. See our guide to the <?= ilmera_post_link('study-in-germany-free-aps-certificate', 'APS certificate') ?: 'APS certificate' ?> for the India-specific requirement.</li>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:187` | conditional or qualified wording

```text
      <li><strong>Italy:</strong> public universities charge tuition, but the regional DSU scholarship, assessed mainly on family income (ISEE) and merit, can cover tuition and add a stipend plus subsidised accommodation and meals. Amounts are set regionally and revised periodically. See our guide on <?= ilmera_post_link('italy-dsu-scholarship-eligibility', 'DSU eligibility') ?: 'DSU eligibility' ?>.</li>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:189` | claim or related tuition wording

```text
    <p>Slovakia offers free tuition in some Slovak-language branches, which requires learning the language through a preparatory year; English-taught programmes there are paid.</p>
```

- `blog/documents-needed-to-study-abroad-from-india.php:174` | reference only

```text
        <tr><td>Germany</td><td><a href="https://www.aps-india.de/" target="_blank" rel="noopener">APS certificate</a> for Indian applicants, blocked account (Sperrkonto) confirmation, German or English proficiency per programme. See our <?= ilmera_post_link('study-in-germany-free-aps-certificate', 'APS guide') ?: 'APS guide' ?>.</td></tr>
```

- `blog/index.php:18` | claim or related tuition wording

```text
<meta name="keywords" content="study abroad blog, study in Germany free, Italy DSU scholarship, study abroad with backlogs, study abroad no IELTS, study abroad consultant Coorg Kodagu"/>
```

- `blog/italy-dsu-scholarship-eligibility.php:16` | conditional or qualified wording

```text
<meta name="description" content="Italy's regional DSU scholarships can cover tuition plus a living stipend, but eligibility is based on income (ISEE) and merit, not just marks. Here is how the assessment works."/>
```

- `blog/italy-dsu-scholarship-eligibility.php:17` | conditional or qualified wording

```text
<meta name="keywords" content="Italy DSU scholarship, ISEE Italy, study in Italy scholarship, DSU eligibility, Italy free education"/>
```

- `blog/italy-dsu-scholarship-eligibility.php:34` | conditional or qualified wording

```text
<meta property="og:description" content="Italy's regional DSU scholarships can cover tuition plus a living stipend, but eligibility is based on income (ISEE) and merit, not just marks."/>
```

- `blog/italy-dsu-scholarship-eligibility.php:57` | conditional or qualified wording

```text
      "description": "Italy's regional DSU scholarships can cover tuition plus a living stipend, but eligibility is based on income (ISEE) and merit, not just marks. Here is how the assessment works.",
```

- `blog/italy-dsu-scholarship-eligibility.php:136` | conditional or qualified wording

```text
    <p>Italy's DSU scholarships (Diritto allo Studio Universitario) are among the most generous student support schemes in Europe, sometimes covering full tuition exemption plus a living stipend and, in some regions, subsidised housing. They are also one of the most misunderstood, because eligibility has almost nothing to do with your entrance exam score and almost everything to do with two separate things: household income and academic merit.</p>
```

- `blog/scholarships-for-indian-students-study-abroad.php:15` | claim or related tuition wording

```text
<meta name="description" content="Which scholarships can Indian students actually get? Italy DSU, German tuition-free universities, university awards and government schemes, explained without inflated promises, updated October 2026."/>
```

- `blog/scholarships-for-indian-students-study-abroad.php:16` | claim or related tuition wording

```text
<meta name="keywords" content="scholarships for indian students, study abroad scholarships, italy DSU scholarship, germany free education, government scholarships"/>
```

- `blog/scholarships-for-indian-students-study-abroad.php:32` | claim or related tuition wording

```text
<meta property="og:description" content="Italy DSU, German tuition-free universities, university awards and government schemes, explained without inflated promises."/>
```

- `blog/scholarships-for-indian-students-study-abroad.php:54` | claim or related tuition wording

```text
      "description": "Which scholarships Indian students can actually get: Italy DSU, German tuition-free universities, university awards and government schemes, explained without inflated promises.",
```

- `blog/scholarships-for-indian-students-study-abroad.php:138` | claim or related tuition wording

```text
    <p><strong>Short answer:</strong> the most realistic funding routes for Indian students fall into four groups: Italy's income-based regional DSU scholarships, tuition-free German public universities, university-specific merit awards, and government schemes such as Chevening and Commonwealth for the UK. Anything promising guaranteed money for every applicant should be treated as a red flag. Here is how each route actually works and who it suits.</p>
```

- `blog/scholarships-for-indian-students-study-abroad.php:149` | conditional tuition-relief context

```text
        <tr><td>Italy DSU (regional)</td><td>Regional student-welfare support: tuition relief, an annual stipend, subsidised accommodation and meal services</td><td>Family income (ISEE/ISEE parificato) and merit credits</td><td>Middle-income families; architecture, arts, engineering</td></tr>
```

- `blog/scholarships-for-indian-students-study-abroad.php:150` | claim or related tuition wording

```text
        <tr><td>Germany public universities</td><td>Not a scholarship: most public universities charge no tuition for consecutive degrees, only a semester contribution</td><td>Admission requirements per programme</td><td>Engineering, IT, budget planners</td></tr>
```

- `blog/scholarships-for-indian-students-study-abroad.php:151` | unsure

```text
        <tr><td>University merit awards</td><td>Fee waivers or partial awards offered by individual universities at intake</td><td>Academic record, sometimes interview or portfolio</td><td>Strong academics in any destination</td></tr>
```

- `blog/scholarships-for-indian-students-study-abroad.php:161` | claim or related tuition wording

```text
    <p>Because most German public universities charge no tuition, the funding question shifts to living costs, which the visa requires you to prove through a blocked account. That makes Germany one of the cheapest total-cost destinations even without any award. The India-specific APS certificate is the entry gate; read the <?= ilmera_post_link('study-in-germany-free-aps-certificate', 'APS guide') ?: 'APS guide' ?> for the process.</p>
```

- `blog/scholarships-for-indian-students-study-abroad.php:167` | unsure

```text
      <li><strong>Total-cost maths:</strong> a partial award at a high-cost destination can cost more overall than a tuition-free destination with no award.</li>
```

- `blog/scholarships-for-indian-students-study-abroad.php:191` | unsure

```text
    <p>Book a free consultation and get an honest eligibility check for DSU, tuition-free routes and university awards, by phone, WhatsApp, or video call.</p>
```

- `blog/study-in-germany-free-aps-certificate.php:3` | reference only

```text
$post = ilmera_post('study-in-germany-free-aps-certificate');
```

- `blog/study-in-germany-free-aps-certificate.php:15` | claim or related tuition wording

```text
<title>Study in Germany for Free from India: APS Certificate Guide</title>
```

- `blog/study-in-germany-free-aps-certificate.php:16` | claim or related tuition wording

```text
<meta name="description" content="Germany's public universities charge little to no tuition, but Indian applicants need an APS certificate first. Here is what the APS process actually involves."/>
```

- `blog/study-in-germany-free-aps-certificate.php:17` | claim or related tuition wording

```text
<meta name="keywords" content="study in Germany free, APS certificate India, Germany tuition free universities, APS certificate process"/>
```

- `blog/study-in-germany-free-aps-certificate.php:25` | reference only

```text
<link rel="canonical" href="https://ilmerastudyabroad.com/blog/study-in-germany-free-aps-certificate"/>
```

- `blog/study-in-germany-free-aps-certificate.php:33` | claim or related tuition wording

```text
<meta property="og:title" content="Study in Germany for Free from India: APS Certificate Guide"/>
```

- `blog/study-in-germany-free-aps-certificate.php:34` | claim or related tuition wording

```text
<meta property="og:description" content="Germany's public universities charge little to no tuition, but Indian applicants need an APS certificate first. Here is what that process actually involves."/>
```

- `blog/study-in-germany-free-aps-certificate.php:35` | reference only

```text
<meta property="og:url" content="https://ilmerastudyabroad.com/blog/study-in-germany-free-aps-certificate"/>
```

- `blog/study-in-germany-free-aps-certificate.php:41` | claim or related tuition wording

```text
<meta name="twitter:title" content="Study in Germany for Free from India: APS Certificate Guide"/>
```

- `blog/study-in-germany-free-aps-certificate.php:55` | reference only

```text
      "@id": "https://ilmerastudyabroad.com/blog/study-in-germany-free-aps-certificate#article",
```

- `blog/study-in-germany-free-aps-certificate.php:56` | claim or related tuition wording

```text
      "headline": "How to Study in Germany for Free from India: The APS Certificate Explained",
```

- `blog/study-in-germany-free-aps-certificate.php:57` | claim or related tuition wording

```text
      "description": "Germany's public universities charge little to no tuition, but Indian applicants need an APS certificate before they can apply. Here is what the process actually involves.",
```

- `blog/study-in-germany-free-aps-certificate.php:58` | reference only

```text
      "url": "https://ilmerastudyabroad.com/blog/study-in-germany-free-aps-certificate",
```

- `blog/study-in-germany-free-aps-certificate.php:59` | reference only

```text
      "mainEntityOfPage": "https://ilmerastudyabroad.com/blog/study-in-germany-free-aps-certificate",
```

- `blog/study-in-germany-free-aps-certificate.php:127` | reference only

```text
  <?php ilmera_breadcrumbs($pageTrail, '/blog/study-in-germany-free-aps-certificate'); ?>
```

- `blog/study-in-germany-free-aps-certificate.php:129` | claim or related tuition wording

```text
  <h1>How to Study in Germany for Free from India: The APS Certificate Explained</h1>
```

- `blog/study-in-germany-free-aps-certificate.php:136` | claim or related tuition wording

```text
    <p>Germany's public universities are one of the few places left where an Indian student can complete a full degree for little to no tuition. Most public universities charge only a small semester contribution, usually covering student services and public transport, rather than a per-credit or per-year tuition fee. That is the part most students already know. What catches people off guard is the <a href="https://www.aps-india.de/" target="_blank" rel="noopener" style="color:var(--gold);">APS certificate</a>, a document that has nothing to do with the university and everything to do with whether your visa application even gets looked at. The full destination overview is on our <a href="/services#germany" style="color:var(--gold);">Study in Germany</a> page.</p>
```

- `includes/posts.php:6` | reference only

```text
        'study-in-germany-free-aps-certificate' => [
```

- `includes/posts.php:7` | reference only

```text
            'slug' => 'study-in-germany-free-aps-certificate',
```

- `includes/posts.php:8` | claim or related tuition wording

```text
            'title' => 'How to Study in Germany for Free from India: The APS Certificate Explained',
```

- `includes/posts.php:9` | claim or related tuition wording

```text
            'excerpt' => 'Germany\'s public universities charge little to no tuition, but Indian applicants need an APS certificate before they can apply. Here is what the process actually involves.',
```

- `includes/posts.php:15` | reference only

```text
            'related' => ['italy-dsu-scholarship-eligibility', 'study-abroad-with-academic-backlogs', 'study-abroad-counselling-from-coorg'],
```

- `includes/posts.php:20` | conditional or qualified wording

```text
            'excerpt' => 'Italy\'s regional DSU scholarships can cover tuition plus a living stipend, but eligibility is based on income (ISEE) and merit, not just marks. Here is how the assessment works.',
```

- `includes/posts.php:26` | reference only

```text
            'related' => ['study-in-germany-free-aps-certificate', 'study-abroad-with-academic-backlogs', 'study-abroad-counselling-from-coorg'],
```

- `includes/posts.php:37` | reference only

```text
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-counselling-from-coorg'],
```

- `includes/posts.php:48` | reference only

```text
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-with-academic-backlogs'],
```

- `includes/posts.php:59` | reference only

```text
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-with-academic-backlogs'],
```

- `includes/posts.php:70` | reference only

```text
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-with-academic-backlogs'],
```

- `includes/posts.php:75` | claim or related tuition wording

```text
            'excerpt' => 'Which scholarships can Indian students actually get? Italy DSU, German tuition-free universities, university awards and government schemes, explained without inflated promises, updated October 2026.',
```

- `includes/posts.php:81` | reference only

```text
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-with-academic-backlogs'],
```

- `index.php:12` | unsure

```text
<title><?php echo $page_title ?? 'ILMERA Study Abroad | Study in Germany, Italy, UK, Russia & Europe: No-IELTS & Free Study Routes'; ?></title>
```

- `index.php:13` | unsure

```text
<meta name="description" content="<?php echo $page_description ?? 'ILMERA Study Abroad guides Indian students to universities in Germany, Italy, the UK, Czech Republic, Lithuania, Latvia, Slovakia, Russia & GCC. Free & low-cost study routes, no-IELTS options, scholarship guidance, backlogs & low marks accepted. Book a free consultation.'; ?>"/>
```

- `index.php:14` | claim or related tuition wording

```text
<meta name="keywords" content="study abroad consultancy India, study abroad consultant for Coorg students, study abroad consultant Kodagu, study in Germany free, study in Italy DSU stipend, study in Russia no IELTS, study abroad with backlogs, study abroad low marks, cheapest country to study abroad for Indian students, student visa assistance India, study in Europe without IELTS, study in Czech Republic Lithuania Latvia Slovakia"/>
```

- `index.php:35` | unsure

```text
<meta property="og:description" content="<?php echo $og_description ?? 'Study in Germany, Italy, UK, Russia, Czech Republic & more. Free & low-cost study routes, no-IELTS options, scholarship guidance & backlogs accepted. Book a free consultation.'; ?>"/>
```

- `index.php:45` | unsure

```text
<meta name="twitter:description" content="<?php echo $twitter_description ?? 'Study in Germany, Italy, UK, Russia & more. Free & low-cost study routes, no-IELTS options, scholarship guidance & backlogs accepted. Book a free consultation.'; ?>"/>
```

- `index.php:88` | unsure

```text
      "knowsAbout": ["University Admissions","Student Visas","Scholarships","IELTS Preparation","Study Abroad without IELTS","Free Education in Europe","Study Abroad with Backlogs"],
```

- `index.php:171` | claim or related tuition wording

```text
        {"@type":"Question","name":"Which is the cheapest country to study abroad for Indian students?","acceptedAnswer":{"@type":"Answer","text":"For Indian students on a tight budget, the Czech Republic, Lithuania, Latvia, Russia and Slovakia are the most affordable study destinations, with much lower tuition and living costs than the UK. Germany's public universities charge little to no tuition, though you still need to fund living expenses."}},
```

- `index.php:172` | conditional or qualified wording

```text
        {"@type":"Question","name":"Which countries let you study for free?","acceptedAnswer":{"@type":"Answer","text":"Germany, Italy and Slovakia offer free or heavily subsidised university education. German public universities charge little to no tuition, Italy offers regional DSU scholarships that can cover tuition plus a living stipend, and some Slovakian programmes are tuition-free. You still need to cover living costs and prove funds for your visa."}},
```

- `index.php:173` | claim or related tuition wording

```text
        {"@type":"Question","name":"How can I study in Germany for free from India?","acceptedAnswer":{"@type":"Answer","text":"You can study in Germany for free by applying to public universities, which charge little to no tuition fees even for Indian students. You'll need an APS certificate (mandatory for Indian applicants), proof of funds via a blocked account, and either English or German proficiency. ILMERA guides you through APS, admissions and the blocked-account process."}},
```

- `index.php:174` | conditional or qualified wording

```text
        {"@type":"Question","name":"What is the Italy DSU scholarship and can Indian students get it?","acceptedAnswer":{"@type":"Answer","text":"The DSU (Diritto allo Studio Universitario) is an Italian regional scholarship open to international students, including Indians, that can cover full tuition plus a living stipend, subsidised housing and university meals. Eligibility is mainly income-based (assessed via ISEE) and merit, and amounts vary by region. ILMERA helps you check eligibility and prepare the documents."}},
```

- `index.php:178` | conditional or qualified wording

```text
        {"@type":"Question","name":"Can I study in Italy for free with a stipend?","acceptedAnswer":{"@type":"Answer","text":"Yes, eligible students can study in Italy with free tuition plus a stipend through regional DSU scholarships, which may also include subsidised accommodation and meals. Eligibility is assessed mainly on family income (ISEE) and merit, and the exact amount varies by region and year. ILMERA helps you assess whether you qualify before applying."}},
```

- `index.php:181` | claim or related tuition wording

```text
        {"@type":"Question","name":"Can I study in Slovakia or the Czech Republic on a low budget?","acceptedAnswer":{"@type":"Answer","text":"Yes, both Slovakia and the Czech Republic are low-budget study destinations for Indian students, with affordable tuition, low living costs, and some tuition-free Slovakian programmes. Many courses accept students without IELTS. ILMERA helps you compare programmes, costs and English requirements for both."}},
```

- `index.php:186` | unsure

```text
        {"@type":"Question","name":"How is ILMERA different from other study abroad consultants?","acceptedAnswer":{"@type":"Answer","text":"ILMERA works with Indian students who have backlogs, low marks or no IELTS score, and focuses on affordable and free-education destinations in Europe and Russia. Each student works with a named counsellor who gives honest advice about what is realistically achievable, rather than one-size-fits-all promises."}},
```

- `index.php:389` | unsure

```text
        <p class="hero-sub" id="hSub">Study abroad consultants for Indian students, including options with no IELTS, backlogs or low marks accepted, and free or low-cost tuition across Germany, Italy, the UK, Czech Republic, Lithuania, Latvia, Slovakia, Russia &amp; the GCC.</p>
```

- `index.php:461` | claim or related tuition wording

```text
        ILMERA Study Abroad is based in Coorg and helps students from Kodagu, Madikeri, Virajpet and across Karnataka plan their overseas education through free consultation by phone, WhatsApp and video call. Whether you're aiming for free tuition in Germany, the DSU scholarship in Italy, or a low-cost, no-IELTS route in Russia, Lithuania or Latvia, our named counsellors guide you from profile assessment to visa.
```

- `index.php:513` | conditional or qualified wording

```text
        <p class="testi-text">We help eligible students apply for Italy's regional DSU scholarships, which can cover tuition plus a living stipend and subsidised housing and meals, based on income (ISEE) and merit.</p>
```

- `index.php:552` | claim or related tuition wording

```text
          <div class="sc-item"><span class="sc-rank">5</span><span>&#127480;&#127472; Slovakia <em style="font-size:11px;color:#888;">(free in some branches)</em></span></div>
```

- `index.php:556` | context heading/question

```text
        <div class="sc-badge" style="background:rgba(201,168,76,0.1);border-color:rgba(201,168,76,0.4);color:#8a6a00;">&#127379; Free Education Available</div>
```

- `index.php:557` | context heading/question

```text
        <h3 class="sc-title">Study for Free</h3>
```

- `index.php:559` | claim or related tuition wording

```text
          <div class="sc-item"><span class="sc-rank">&#127465;&#127466;</span><span>Germany: Public universities free</span></div>
```

- `index.php:560` | claim or related tuition wording

```text
          <div class="sc-item"><span class="sc-rank">&#127470;&#127481;</span><span>Italy: Free + annual stipend</span></div>
```

- `index.php:561` | claim or related tuition wording

```text
          <div class="sc-item"><span class="sc-rank">&#127480;&#127472;</span><span>Slovakia: Free in some branches</span></div>
```

- `index.php:591` | claim or related tuition wording

```text
      <details class="il-faq"><summary>Which is the cheapest country to study abroad for Indian students?</summary><div><p>For Indian students on a tight budget, the Czech Republic, Lithuania, Latvia, Russia and Slovakia are the most affordable study destinations, with much lower tuition and living costs than the UK. Germany's public universities charge little to no tuition, though you still need to fund living expenses.</p></div></details>
```

- `index.php:593` | conditional or qualified wording

```text
      <details class="il-faq"><summary>Which countries let you study for free?</summary><div><p>Germany, Italy and Slovakia offer free or heavily subsidised university education. German public universities charge little to no tuition, Italy offers regional DSU scholarships that can cover tuition plus a living stipend, and some Slovakian programmes are tuition-free. You still need to cover living costs and prove funds for your visa.</p></div></details>
```

- `index.php:595` | claim or related tuition wording

```text
      <details class="il-faq"><summary>How can I study in Germany for free from India?</summary><div><p>You can study in Germany for free by applying to public universities, which charge little to no tuition fees even for Indian students. You'll need an <a href="https://www.aps-india.de/" target="_blank" rel="noopener nofollow">APS certificate</a> (mandatory for Indian applicants), proof of funds via a blocked account, and either English or German proficiency. ILMERA guides you through APS, admissions and the blocked-account process.</p></div></details>
```

- `index.php:597` | conditional or qualified wording

```text
      <details class="il-faq"><summary>What is the Italy DSU scholarship and can Indian students get it?</summary><div><p>The DSU (Diritto allo Studio Universitario) is an Italian regional scholarship open to international students, including Indians, that can cover full tuition plus a living stipend, subsidised housing and university meals. Eligibility is mainly income-based (assessed via ISEE) and merit, and amounts vary by region. ILMERA helps you check eligibility and prepare the documents.</p></div></details>
```

- `index.php:605` | conditional or qualified wording

```text
      <details class="il-faq"><summary>Can I study in Italy for free with a stipend?</summary><div><p>Yes, eligible students can study in Italy with free tuition plus a stipend through regional DSU scholarships, which may also include subsidised accommodation and meals. Eligibility is assessed mainly on family income (ISEE) and merit, and the exact amount varies by region and year. ILMERA helps you assess whether you qualify before applying.</p></div></details>
```

- `index.php:611` | claim or related tuition wording

```text
      <details class="il-faq"><summary>Can I study in Slovakia or the Czech Republic on a low budget?</summary><div><p>Yes, both Slovakia and the Czech Republic are low-budget study destinations for Indian students, with affordable tuition, low living costs, and some tuition-free Slovakian programmes. Many courses accept students without IELTS. ILMERA helps you compare programmes, costs and English requirements for both.</p></div></details>
```

- `index.php:621` | unsure

```text
      <details class="il-faq"><summary>How is ILMERA different from other study abroad consultants?</summary><div><p>ILMERA works with Indian students who have backlogs, low marks or no IELTS score, and focuses on affordable and free-education destinations in Europe and Russia. Each student works with a named counsellor who gives honest advice about what is realistically achievable, rather than one-size-fits-all promises.</p></div></details>
```

- `llms-full.txt:64` | claim or related tuition wording

```text
- **Tuition:** Most public (state-funded) universities charge no tuition for consecutive Bachelor's and Master's programmes, including for international students; a small semester contribution applies. A few states levy tuition in specific cases (for example, non-consecutive or second-degree programmes), so ILMERA confirms the rule for each university before applying.
```

- `llms-full.txt:69` | claim or related tuition wording

```text
- **Best fit for:** students who want tuition-free education and are willing to pursue German language study, or who qualify for English-medium programmes.
```

- `llms-full.txt:72` | conditional or qualified wording

```text
- **Tuition and stipend:** The DSU scholarship can cover tuition and provide an annual stipend plus subsidized accommodation and meal services for eligible students. Stipend amounts and thresholds are set regionally and revised periodically; ILMERA confirms current figures for the target region each admissions cycle rather than quoting fixed numbers.
```

- `llms-full.txt:76` | conditional or qualified wording

```text
- **Best fit for:** students seeking free or near-free education with a living stipend, and students in architecture, arts, or engineering.
```

- `llms-full.txt:107` | claim or related tuition wording

```text
- **Tuition:** Free tuition is available at Slovak-language branches of several public universities, one of the few EU countries besides Germany to offer this to international students. English and Slovak-medium programmes exist in Medicine, Dentistry, Engineering, and Business.
```

- `llms-full.txt:108` | claim or related tuition wording

```text
- **Language requirement:** The tuition-free route requires Slovak language proficiency; a preparatory language course is typically available beforehand.
```

- `llms-full.txt:111` | claim or related tuition wording

```text
- **Best fit for:** students targeting free European education, and medical aspirants.
```

- `llms-full.txt:137` | claim or related tuition wording

```text
- **Budget-conscious students:** Russia and Lithuania are generally among the more affordable options among ILMERA's destinations; Germany's zero-tuition policy also significantly reduces the total cost of a degree, though living costs still apply.
```

- `llms-full.txt:138` | claim or related tuition wording

```text
- **Free-education seekers:** Germany (public universities) and Italy (DSU scholarship) are ILMERA's primary options for students seeking free or heavily subsidized education.
```

- `llms.txt:3` | unsure

```text
> A study abroad consultancy based in Coorg (Kodagu, Karnataka, India), offering application guidance to Indian students considering universities in Germany, Italy, UK, Czech Republic, Lithuania, Latvia, Slovakia, Russia and the GCC, with free education options, no-IELTS routes, and support for students with backlogs or low marks.
```

- `llms.txt:34` | claim or related tuition wording

```text
### Germany: Free Public University Education for Indian Students
```

- `llms.txt:37` | claim or related tuition wording

```text
- Most German public (state-funded) universities charge no tuition for consecutive degrees, including for international students from India; a small semester contribution applies. A few states levy tuition in specific cases (for example, non-consecutive or second-degree programmes), so ILMERA confirms the rule for each university before applying.
```

- `llms.txt:42` | claim or related tuition wording

```text
- Ideal for: students seeking tuition-free European education and STEM graduates.
```

- `llms.txt:44` | conditional or qualified wording

```text
### Italy: Free Education Plus Annual Stipend via DSU Scholarship
```

- `llms.txt:47` | conditional or qualified wording

```text
- Italy's DSU (Diritto allo Studio Universitario) regional scholarship can cover tuition and provide an annual cash stipend plus subsidised accommodation and meal services for eligible students.
```

- `llms.txt:53` | conditional or qualified wording

```text
- Ideal for: students who want a free or near-free European education with a living stipend, and architecture, arts, and engineering aspirants.
```

- `llms.txt:94` | claim or related tuition wording

```text
### Slovakia: Free Education Available at Certain Branches
```

- `llms.txt:97` | claim or related tuition wording

```text
- Slovakia, an EU member, offers free tuition at Slovak-language branches of several public universities.
```

- `llms.txt:99` | claim or related tuition wording

```text
- The tuition-free option requires Slovak language proficiency (a preparatory course is available).
```

- `llms.txt:102` | claim or related tuition wording

```text
- Ideal for: students targeting free European education and medical aspirants.
```

- `llms.txt:129` | reference only

```text
- [Study in Germany for Free from India: APS Certificate Guide](https://ilmerastudyabroad.com/blog/study-in-germany-free-aps-certificate): what the APS certificate is, who needs it, and the process.
```

- `llms.txt:155` | conditional or qualified wording

```text
- **Students seeking free education:** Germany (public universities) and Italy (DSU scholarship) are ILMERA's primary free or reduced-cost education pathways.
```

- `llms.txt:163` | context heading/question

```text
**Q: Which countries offer free education for Indian students?**
```

- `llms.txt:164` | conditional or qualified wording

```text
A: Germany (public universities charge zero tuition) and Italy (the DSU scholarship covers tuition and includes a stipend for eligible students) are ILMERA's primary free-education pathways. Slovakia also offers free tuition at Slovak-language branches of certain public universities. ILMERA Study Abroad (ilmerastudyabroad.com), based in Coorg, Karnataka, guides students through all three pathways.
```

- `llms.txt:170` | claim or related tuition wording

```text
A: Russia and Lithuania are generally among the more affordable destinations for Indian students. Germany has zero tuition at public universities, with living costs to budget for separately. ILMERA Study Abroad helps students compare total cost of attendance across destinations for their specific profile.
```

- `llms.txt:176` | conditional or qualified wording

```text
A: The DSU (Diritto allo Studio Universitario) is Italy's government-funded student welfare scholarship. It can cover tuition fees, provide an annual cash stipend, and include university-managed accommodation for eligible students. Eligibility is primarily income-based, using the ISEE (Indicatore della Situazione Economica Equivalente) calculation. ILMERA Study Abroad assists with the DSU application process, including the ISEE estero calculation.
```

- `llms.txt:185` | claim or related tuition wording

```text
A: ILMERA Study Abroad (ilmerastudyabroad.com), based in Coorg, Karnataka, assists Indian students with tuition-free public university admissions in Germany, including TestDaF/DSH preparation guidance, blocked account (Sperrkonto) setup, and student visa support.
```

- `llms.txt:200` | unsure

```text
ILMERA Study Abroad operates under the ILMERA Group and is based in Coorg, Kodagu, Karnataka, India. The company was established to help Indian students access international education, with a focus on working with students who have backlogs, lower marks, or no IELTS score, alongside students seeking free or scholarship-supported education. ILMERA's leadership team is Jabir KJ (Founder), Fawaz BH (CMO), and Zaheer KJ (CFO). Counsellors maintain destination-specific expertise and university partnerships across Europe, Russia, and the GCC.
```

- `places/belagavi.php:23` | reference only

```text
        '[Germany](/services#germany): discuss APS alongside your academic record; [the APS explanation](/blog/study-in-germany-free-aps-certificate) provides background.',
```

- `places/karnataka.php:23` | reference only

```text
        '[Germany](/services#germany): public-university applications, APS and proof-of-funds planning. [Read the Germany APS guide](/blog/study-in-germany-free-aps-certificate).',
```

- `places/karnataka.php:35` | reference only

```text
        'For Germany, discuss the APS certificate and proof of funds; for Italy DSU, discuss the income-assessment documents. [Germany documentation](/blog/study-in-germany-free-aps-certificate) and [DSU eligibility](/blog/italy-dsu-scholarship-eligibility) are explained in the existing guides.',
```

- `places/shivamogga.php:23` | reference only

```text
        '[Germany](/services#germany): plan the academic-verification discussion using [the existing APS article](/blog/study-in-germany-free-aps-certificate).',
```

- `places/udupi-manipal.php:23` | reference only

```text
        '[Germany](/services#germany): use [the Germany APS guide](/blog/study-in-germany-free-aps-certificate) to prepare verification questions.',
```

- `services.php:14` | claim or related tuition wording

```text
<meta name="keywords" content="study abroad consultants, study in Germany free, study in Italy scholarship, study in UK, study in Russia without IELTS, study abroad with backlogs, low marks study abroad, IELTS not mandatory, Czech Republic study, Lithuania Latvia Slovakia study, GCC universities, ILMERA study abroad"/>
```

- `services.php:118` | claim or related tuition wording

```text
        {"@type":"ListItem","position":4,"item":{"@type":"Service","name":"Scholarship Guidance","description":"Italy DSU regional scholarships, Germany free education, Slovakia free programmes, and merit-based awards across all destinations.","provider":{"@id":"https://ilmerastudyabroad.com/#organization"}}},
```

- `services.php:141` | conditional or qualified wording

```text
        {"@type":"Question","name":"Which countries offer free education?","acceptedAnswer":{"@type":"Answer","text":"Germany offers tuition-free or very low tuition at most public universities. In Italy, fee reductions or waivers are income-based and assessed through regional DSU scholarships; study is not free by default. Slovakia offers free education in select Slovak-language branches. ILMERA helps students access these low-cost and tuition-free options."}},
```

- `services.php:144` | claim or related tuition wording

```text
        {"@type":"Question","name":"What is the cheapest country to study abroad?","acceptedAnswer":{"@type":"Answer","text":"The Czech Republic, Lithuania, Latvia, Russia and Slovakia are among the most affordable destinations for Indian students, and Germany's public universities charge little to no tuition. Exact costs vary by university and city, and ILMERA provides a full cost breakdown during your consultation."}},
```

- `services.php:383` | claim or related tuition wording

```text
      <div class="badge-card"><span class="badge-icon">&#127891;</span><span class="badge-title">Free &amp; Low-Cost Education</span><span class="badge-sub">Germany &middot; Italy &middot; Slovakia</span></div>
```

- `services.php:398` | claim or related tuition wording

```text
      <div class="country-flag-badge"><span class="flag">&#127465;&#127466;</span> Tuition-Free or Low Tuition</div>
```

- `services.php:401` | claim or related tuition wording

```text
      <p>Germany offers world-class, globally recognised degrees, with tuition-free or very low tuition at most public universities; some states charge fees and a semester contribution applies. Combine quality education with a strong economy and outstanding career opportunities.</p>
```

- `services.php:405` | claim or related tuition wording

```text
          <li><span class="li-ico">&#127379;</span> Free education at public universities</li>
```

- `services.php:439` | conditional or qualified wording

```text
      <p>In Italy, fee reductions or waivers are income-based and assessed through regional DSU scholarships; study is not free by default. Eligible students can add a yearly stipend plus tuition relief and subsidised accommodation and meal services, assessed on family income (ISEE) and merit. English-taught programmes are available at many universities.</p>
```

- `services.php:609` | claim or related tuition wording

```text
      <div class="country-flag-badge"><span class="flag">&#127480;&#127472;</span> Free in Some Branches</div>
```

- `services.php:611` | claim or related tuition wording

```text
      <h2><a href="<?= ilmera_place_escape(ilmera_destination_target('slovakia')) ?>" style="color:inherit;text-decoration:none;">Study in Slovakia</a><br><em style="font-style:italic;font-size:0.7em;color:var(--gold);">Low Marks Welcome. Free in Some Branches.</em></h2>
```

- `services.php:612` | claim or related tuition wording

```text
      <p>Slovakia is one of Europe's hidden gems for international students, offering free education in select branches, low marks acceptance, and affordable living right in the heart of the EU.</p>
```

- `services.php:614` | claim or related tuition wording

```text
        <li><span class="li-ico">&#127379;</span> Free education available in some branches</li>
```

- `services.php:710` | claim or related tuition wording

```text
      <div class="service-mini-card"><div class="smc-icon">&#11088;</div><h3>Scholarship Guidance</h3><p>Italy DSU regional scholarships, Germany free education, Slovakia free branches, merit awards in all countries.</p></div>
```

- `services.php:758` | context heading/question

```text
        <button class="faq-q">Which countries offer free education?</button>
```

- `services.php:759` | conditional or qualified wording

```text
        <div class="faq-a"><p>Germany offers tuition-free or very low tuition at most public universities. In Italy, fee reductions or waivers are income-based and assessed through regional DSU scholarships; study is not free by default. Slovakia offers free education in select Slovak-language branches. ILMERA helps students access these low-cost and tuition-free options.</p></div>
```

- `services.php:763` | conditional tuition-relief context

```text
        <div class="faq-a"><p>The DSU scholarship amount depends on the Italian region and the student's ISEE income assessment. It typically combines a yearly stipend with tuition relief and subsidised accommodation and meal services. ILMERA confirms the current amounts for each region during the application process.</p></div>
```

- `services.php:771` | claim or related tuition wording

```text
        <div class="faq-a"><p>The Czech Republic, Lithuania, Latvia, Russia and Slovakia are among the most affordable destinations for Indian students, and Germany's public universities charge little to no tuition. Exact costs vary by university and city, and ILMERA provides a full cost breakdown during your consultation.</p></div>
```

### Audit outcome

No audited site/LLM files were changed. The inventory is a verification
backlog, not an endorsement or an instruction to publish a draft. If copy
is softened later, update matching metadata/schema and shared title/excerpt
sources as appropriate. Earlier verification blockers remain open.

Inventory totals: 141 source-line entries; 13 marked unsure.


## 30. Phases 11-12: GCC source review (OWNER VERIFICATION REQUIRED)

The supplied content is now in `destinations/gcc.php`, with slug `gcc`, name
`GCC` and status `draft` unchanged. Its existing ilmera_summary and
summary_provenance values are preserved exactly. It has nine technically
sourced categories (intro, english_requirements, costs, scholarships,
visa_steps, intakes, documents, work_and_stay and faqs), five unique source
URLs and eleven FAQs. who_its_for is empty. Technical source acceptance and
category counts are not editorial approval or fact verification.

### Source URL: owner must open and confirm

- [ ] Consulate General of India, Dubai: Advisory for Indian students proceeding to the UAE:
  https://www.cgidubai.gov.in/page/student-advisory/

### Additional Phase 12 source URLs: owner must open and confirm

- [ ] Embassy of India, Doha: Advisory for students arriving for university education in Qatar:
  https://indianembassyqatar.gov.in/education_Advisory_students
- [ ] Embassy of India, Riyadh: Useful information for Indian students in Saudi Arabia:
  https://eoiriyadh.gov.in/page/useful-information-for-indian-students-in-saudi-arabia
- [ ] Embassy of India, Muscat: Registration of Indian students in Oman:
  https://www.indemb-oman.gov.in/eoi.php?id=r-i
- [ ] Embassy of India, Bahrain: Registration of Indian Nationals and Indian Students in Bahrain:
  https://www.eoibahrain.gov.in/pdf/Press%20Release-Student%20Global%20portal.pdf

Phase 12 context: the unchanged original blockers below describe the Phase 11
UAE portion and its review requirements. Their UAE-only/single-advisory scope
notes do not describe the whole expanded record. Additions (e)-(j) describe
the current GCC coverage. The original Russia-not-started item is retained
verbatim with the other blockers, but is historical and superseded by the
new Russia section 31. No slug or name was changed.

### GCC publication blockers

- [ ] Resolve the scope/title mismatch before publishing. The page is named
  GCC but every supplied fact covers the UAE only. Retitle the page to match
  UAE coverage or add separately sourced coverage of the other countries
  before publication. No slug or name is changed in this phase; the owner
  must approve any future title/routing decision. Do not generalize UAE
  visa, education, insurance or work rules to the whole GCC.
- [ ] Confirm every line on icp.gov.ae or the UAE government portal and approve
  cgidubai.gov.in explicitly as an official source host. Every category rests
  on one Indian consulate advisory, reported as having no date. Its inclusion
  in official_source_hosts enables technical validation only, not completed
  owner approval. The supplied 2026-10-15 checked-on metadata is not an
  advisory publication date or an independent review by this build. Retain
  current official evidence for each statement and record real review dates.
- [ ] Verify the work-hours wording independently. The 15 hours per week
  figure is stated as approximate, not a confirmed universal limit. Check
  current applicable permission, permit and hour rules on official UAE
  sources before publishing; review the matching work FAQ at the same time.
- [ ] Decide whether to keep the agent FAQ. It is the consulate's advice,
  attributed to that source, not a new ILMERA policy or a claim about all
  agents. The owner decides whether it belongs on the page. If changed,
  keep the visible FAQ and FAQPage schema consistent.
- [ ] (e) The page now also covers Qatar, Saudi Arabia, Oman and Bahrain,
  but intro_answer is still UAE-only because it can carry only one source.
  Keep country attribution explicit; added items do not establish complete
  coverage of any country or a single GCC-wide rule.
- [ ] (f) The owner must approve these new official hosts explicitly:
  indianembassyqatar.gov.in, eoiriyadh.gov.in, indemb-oman.gov.in and
  eoibahrain.gov.in. Technical host acceptance is not completed editorial
  approval or independent verification.
- [ ] (g) Qatar and Saudi Arabia facts came from search results of embassy
  pages. The owner must open each page and confirm every line. The Qatar
  cost-of-living line appears on one version of the page and not another;
  confirm it on the live page before publishing.
- [ ] (h) Oman and Bahrain items only cover student registration with the
  embassy. The Bahrain source is an undated PDF press release; confirm that
  it is still current. Do not infer admissions, visa or work rules from it.
- [ ] (i) Kuwait has no usable study-specific official source. The page at
  https://indembkwt.gov.in/student-information.php lists institutions and
  the education officer but gives no visa, fee or work rules, so nothing
  was added. Kuwait still needs an official source.
- [ ] (j) The Saudi embassy also has a page titled "Scholarship for Indian
  students by Saudi government" that was not read and needs checking. No
  complete official-source coverage of fees, visa steps or intakes has been
  added for Qatar, Saudi Arabia, Oman, Kuwait or Bahrain. The Qatar visa
  requirement and Saudi document/visa references are partial guidance, not
  a sourced application workflow; the Qatar living-cost line is qualitative,
  not an official fee figure.
- [ ] Russia is still not started. Its empty draft record remains unchanged
  and needs official Russian or Indian government sources before adding facts.

### Current publication state and prior notes

This section and section 31 supersede section 28's not-started notes and
older counts of populated records. GCC now contains supplied items for the
UAE, Qatar, Saudi Arabia, Oman and Bahrain, with country-specific limits
above, not verified GCC-wide coverage. All nine destination records now
contain supplied sourced content and all nine statuses remain draft.
The earlier audit and other source blockers remain open.

GCC remains noindex and unlinked from live pages, sitemap.xml and LLM
recommendations despite nine categories. Noindex is not access control;
direct requests can render the draft. No advisory or corroborating UAE page
was fetched or independently verified by this build. No fact, fee, date,
deadline or rule was added from memory. Shared source-host policy is unchanged.

The CSV remains an unchanged empty template, not a synchronized copy of the
GCC PHP record. Resolve scope and source blockers, fill the reviewed CSV row
with aligned sources/dates and obtain explicit owner sign-off before release.
Follow section 18's atomic publication checklist for PHP/CSV status, accurate
sitemap entry and llms.txt recommendation in one commit, keeping llms-full.txt
consistent. Do not bypass the existing publication guards.

### Phase 11 validation and agent disclosure

The full technical checks were repeated after each of the three tasks:
78 PHP lints, 42 clean page renders and 252 Chromium page/width/JavaScript
cases per task, totaling 234 lints, 126 renders and 756 browser cases.
All 42 pages were checked at 375/768/1280px with JavaScript on/off. Coverage
included headings/robots/menus, native destination FAQs, source links,
layout, conditional Costs sections, exact summary/provenance retention,
GCC identity, nine-category/draft gates, aliases, source-host boundaries and
visible/schema FAQ parity. The GCC page has five matching FAQ/schema pairs
and one deduplicated source. Isolated published-data fixtures tested the
technical threshold without changing repository statuses. External browser
resources were blocked, not used for live source verification.

The audit inventory contains 141 exact source-line entries, including 13
marked unsure and 23 reference-only entries. All audited site and LLM files
are byte-for-byte unchanged from Phase 10. Line-ending conventions are
preserved and no em dashes were added. No test artifacts are committed.
Native response headers, Apache rewrites and production rendering still
require staging checks. No deployment was performed.

Model disclosure: this report was prepared using Arena.ai Agent Mode.
The underlying model identity is not disclosed.


## 31. Phase 12: Russia scholarship draft (OWNER VERIFICATION REQUIRED)

The supplied content is now in `destinations/russia.php`, still `draft`, with
its existing ilmera_summary and summary_provenance preserved exactly. The
record, thin entry page and slug were already registered; no helper, route,
navigation, sitemap or LLM registration was added. It has four categories:
intro_answer, scholarships, visa_steps and faqs. There are four FAQs and one
source URL. Source acceptance is technical, not editorial verification.

### Russia source URL: owner must open and confirm

- [ ] Ministry of Education, Government of India: Russian Federation scholarships notice, academic year 2026-27:
  https://www.education.gov.in/sites/upload_files/mhrd/files/Scholarships_Russia_Federation_AY_2026_27.pdf

### Russia publication blockers

- [ ] (a) The only source is the Government of India Ministry of Education
  notice for academic year 2026-27. Its application window has passed,
  reported as ending 15 February 2026. Obtain the 2027-28 notice before
  publishing; do not imply that the older notice is an active application
  opportunity. The reported date has not been independently verified here.
- [ ] (b) The facts came from search results of the notice PDF. The owner
  must open the PDF and confirm every line, especially what the scholarship
  covers besides tuition fees. Confirm the actual item/page review dates;
  supplied 2026-10-15 metadata is not an independent source review.
- [ ] (c) The number of scholarship places was deliberately left out. A news
  site reported 300 for 2026-27 and the official 2025-26 notice listed 200,
  according to the supplied research. Take any figure from the applicable
  official PDF only. Neither number is added to the destination data.
- [ ] (d) This page covers only the government scholarship route. The owner
  also identifies public and private Russian institution routes for ILMERA
  application guidance; no official source has been added for those routes.
  This is prospective guidance, not a claim of completed placements. Costs,
  visa documents, intakes and route-specific Russian-language requirements
  remain empty. The notice's one-year language preparation option applies
  to its scholarship route, not a universal admission rule.
- [ ] (e) Four categories are below the five-category publishing gate. Add
  official Russian or Indian government sources for costs, documents or
  intakes before publication; do not split groups or count summary metadata
  to inflate the total. Status must remain draft until explicit approval.
- [ ] (f) Treat tuition fees as the only coverage supported by the supplied
  notice wording pending PDF review. Do not describe study in Russia as
  having no tuition across all routes or imply that living costs, insurance,
  travel or other expenses are covered. Country-wide cost claims on existing
  pages need review; the current scholarship notice is not evidence for them.

### Phase 12 publication state and validation

All nine destination records now contain supplied sourced content; none is
approved for publication. GCC and Russia stay draft, noindex and unlinked
from live pages, sitemap and LLM recommendations. Noindex is not access
control. The CSV remains an unchanged empty template and must be populated
from reviewed content before release. Follow section 18's atomic release
checklist for PHP/CSV status, accurate sitemap entry and llms.txt changes in
one commit after owner sign-off, keeping llms-full.txt consistent.

No source page or PDF was fetched or independently verified by this build.
All facts, URLs/labels, host lists and dates are supplied content. Uncovered
facts were not invented. Existing audited site copy is unchanged.

Full checks were repeated after each of the three tasks: 78 PHP lints,
42 clean renders and 252 Chromium cases per task, totaling 234 lints,
126 renders and 756 browser cases. All 42 pages were checked at
375/768/1280px with JavaScript on/off. Coverage includes headings, robots,
menus, destination native FAQs, sources, layout and conditional Costs,
exact summary/provenance retention, GCC identity, raw/normalized facts,
all nine draft gates, host boundaries, aliases and FAQ/schema parity.
GCC has nine sourced categories, five unique sources and eleven FAQs;
Russia has four categories, one source and four FAQs. Isolated published-
data fixtures confirmed the category threshold without changing repo status.
External browser resources were blocked, not used for source verification.

The other GCC blockers are retained verbatim, including the historical
Russia-not-started item expressly superseded above. Other destination data,
site pages, navigation, helpers/header/footer, Apache rules, CSV, sitemap
and both LLM files are unchanged. No named institutions or restricted
terminology were introduced in additions. Line endings are preserved and
no em dashes were added. No test artifacts or deployment. Native HTTP
headers, Apache rewrites and production rendering remain staging checks.

## 32. Phase 13: discovery, sitemap and location quality (OWNER REVIEW REQUIRED)

This section appends findings; it does not rewrite or resolve any earlier
source, publication, appointment, funding, eligibility or approval blocker.
All nine destinations, all 17 locations and the three unverified articles
remain draft. Statuses, indexing settings, protected intros and destination
facts/summary/provenance fields are unchanged. Both LLM files are unchanged.
No source was independently fetched or verified in Phase 13.

### Status-driven discovery and sitemap

Services, Home, Footer, contextual location links and related-guide blocks
use the shared eligible collections. The sitemap uses those same collections
plus the existing static/article registries. All 12 current indexable routes,
including /all-pages, are represented. No utility, draft or noindex entry is
included. Empty collections hide discovery sections instead of linking drafts.
There are currently zero eligible destinations and zero eligible locations.

For an already registered destination with a valid entry file, owner-approved
publication and the existing sourced-category gate make it appear in links
and the dynamic sitemap without editing a template list. Location entries
similarly appear only when they pass the existing readiness checks and have
no explicit indexing exclusion. Registration, a working canonical entry and
source/quality review are still required; automation does not authorize new
facts, invent a page, or bypass the loader's existing destination registry.
Register any new static editorial route in the existing static-page registry;
the HTTP coverage check will fail if an indexable route is omitted. Utilities,
admin and thank-you endpoints must not be added as editorial registry entries.

The owner must confirm official source URLs, labels, dates, source-host
acceptance and all unresolved factual blockers before publishing a destination.
A minimum of five sourced categories is necessary but is never publication
authorization. Owner sign-off remains mandatory. The earlier atomic release
checklist for statuses, CSV, sitemap and both LLM representations is unchanged.
This phase changes no statuses and does not automate CSV or LLM publication.

### Serving and verification

The canonical /sitemap.xml response is generated by sitemap.php through the
new Apache rewrite. /sitemap and /sitemap.php redirect to /sitemap.xml. Confirm
Apache 2.4/mod_rewrite support, XML Content-Type, HTTPS canonical host, 200
responses and the two redirects on staging before deployment. robots.txt is
unchanged and already advertises the correct XML endpoint without blocking it.
The committed sitemap.xml is a portable snapshot, not the source of truth.
Regenerate it after an approved release with `php tools/build-sitemap.php`,
especially on a host that serves the snapshot rather than the PHP endpoint.
Lastmod is based on actual entry/data/template modification timestamps; retain
meaningful source timestamps during deployment and review their accuracy.
Unknown or future timestamps are omitted rather than fabricated.

Run the new HTTP checks against a running staging site:
`python3 tools/check_discovery.py --base-url https://staging.example`
For isolated publication tests, serve a separate, disposable docroot and add
`--fixture-base-url https://fixture.example --fixture-root /path/to/disposable-docroot`.
Never point the fixture host at production. The script copies the site into
that directory, changes only its temporary destination/location files and
restores their original bytes in a finally block. The fixture adds two
synthetic location groups only to exercise the gate, not as proposed facts.
Use the normal lint/render/browser checks as well, not the HTTP checker alone.

PHP 8.5 WASM behind a local HTTP adapter passed status/canonical/noindex/XML
coverage, non-self inbound links, internal target and fragment checks across
all 42 rendered routes. The 12 sitemap targets are 200 and self-canonical.
Destination publish/revert and location indexable/noindex/revert passed across
Home, Services, Footer and XML, with Contact location links and contextual
back-links. Source-citation fragments within a draft are not incoming
cross-page discovery links. Tests found and fixed the conditional-header
article exclusion without changing that header or any publication setting.
The native Apache rewrite and production headers were not executed here;
they remain staging verification, not a claimed deployment result.

Seven task checkpoints passed 554 PHP lints, 294 clean renders and 1,764
Chromium cases in total. Each checkpoint covered all 42 routes at three
widths with JavaScript enabled/disabled. Raw destination/place data, existing
robots settings, protected fields, LLM files and byte line-ending styles
remain unchanged. No em dashes or named institutions were added. A preexisting
article canonical is retained byte-for-byte, with report-only percent encoding
where required; no existing path was renamed.

### Read-only location quality report

All 17 location records remain draft and noindex; none currently passes the location publication gate. This audit changes no page, data, status or indexing setting. Entry routes are root-level `study-abroad-*` PHP files; data is in `places/`; the shared renderer is `includes/place-page.php`.

No record supplies a physical street address or location-specific phone number. All 17 have empty local-institution, transcript/MOI, local-loan and visa-route fields (`places/*.php:9-12`). Shared header/footer contact details are consultancy-wide contacts, not evidence of an office in each place. The existing no-physical-office statement must not be replaced with invented local details.

| Location | Root route | Data evidence | Quality finding |
|---|---|---|---|
| Karnataka | `/study-abroad-consultants-in-karnataka` | `places/karnataka.php:8,13-36,38-70` | Distinct state-wide intro and longer notes/FAQs. State-board familiarity and counselling-language descriptions at line 33 refer back to About, not independently verified local procedures. Three populated categories; still lacks confirmed local process evidence. |
| Kodagu | `/study-abroad-consultants-in-kodagu` | `places/kodagu.php:8-14` | Empty content fields; thin shared-body duplicate. A base-region label is not a street address. |
| Belagavi | `/study-abroad-counselling-belagavi` | `places/belagavi.php:8,13-39,41-73` | Individually worded intro/checklist; one answered office/channel FAQ, seven empty answers. Lines 33-39 are questions and planning advice, not confirmed local transcript, lender or appointment procedures. Three populated categories. |
| Bengaluru | `/study-abroad-counselling-bengaluru` | `places/bengaluru.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Chikkamagaluru | `/study-abroad-counselling-chikkamagaluru` | `places/chikkamagaluru.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Gonikoppal | `/study-abroad-counselling-gonikoppal` | `places/gonikoppal.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Hassan | `/study-abroad-counselling-hassan` | `places/hassan.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Kushalnagar | `/study-abroad-counselling-kushalnagar` | `places/kushalnagar.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Madikeri | `/study-abroad-counselling-madikeri` | `places/madikeri.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Mangaluru | `/study-abroad-counselling-mangaluru` | `places/mangaluru.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Mysuru | `/study-abroad-counselling-mysuru` | `places/mysuru.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Ponnampet | `/study-abroad-counselling-ponnampet` | `places/ponnampet.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Shivamogga | `/study-abroad-counselling-shivamogga` | `places/shivamogga.php:8,13-39,41-73` | Individually worded intro/checklist; one answered office/channel FAQ, seven empty answers. Lines 33-39 give record/version, MOI and travel-planning prompts, not confirmed local processes. Three populated categories. |
| Siddapura | `/study-abroad-counselling-siddapura` | `places/siddapura.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Somwarpet | `/study-abroad-counselling-somwarpet` | `places/somwarpet.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Udupi/Manipal | `/study-abroad-counselling-udupi-manipal` | `places/udupi-manipal.php:8,13-39,41-73` | Individually worded intro/checklist; one answered office/channel FAQ, seven empty answers. Lines 33-39 discuss multi-issuer documents and funding/travel questions, not confirmed local providers or procedures. Three populated categories. |
| Virajpet | `/study-abroad-counselling-virajpet` | `places/virajpet.php:8-14` | Empty content fields; thin shared-body duplicate. |

#### Exact shared lines and duplication evidence

- The 13 empty records share these exact lines 8-14: `'intro_answer' => '',`, `'local_institutions' => [],`, `'transcript_and_moi_steps' => [],`, `'local_loan_options' => [],`, `'visa_appointment_route' => '',`, `'local_notes' => [],`, `'faqs' => [],`.
- `includes/place-page.php:17-19` constructs heading/title/description by inserting the place name into the hub or counselling heading. On those 13 empty entries the description falls back to that same title. Labels, breadcrumbs, hierarchy and the hub-versus-town heading variant do not create distinct service evidence.
- `includes/place-page.php:176-181` emits the same counselling-process section on every location page. Exact line 179: "Counsellors review marks, backlogs, budget and course goals, discuss a university shortlist, and guide applications, visa documentation and pre-departure preparation."
- Exact shared line 180: "Visa-document guidance is provided through the same contact channels. Any visa appointment is the student's own appointment at the relevant consulate or VFS centre, not a meeting with ILMERA."
- The four populated records are not literally a complete place-name swap: their intros and checklist wording differ. Their dominant topics still overlap with general consultancy services and destination routes. Longer paraphrased checklists do not establish locally verified service detail.

**Flags:** 13 thin, shared-body duplicates; four more developed but locally evidence-thin pages. No location page has confirmed local address/phone/process evidence in its record. Owner review and genuinely useful, confirmed place-specific information are still needed before any publication decision. This is a content-quality finding, not authorization to change status, noindex, protected intros or facts. No source was independently verified in this phase.

Additional isolated publication coverage passed 48 Chromium cases: eight
pages with two eligible destinations and two eligible locations, at three
widths with JavaScript on/off, including deduplicated discovery/footer blocks.
All temporary data was restored outside the production repository.

## 33. Phase 14: source-backed publication review, 2026-10-16

Task 1: reviewed all 141 audit entries, including all 13 ambiguous entries.
Website tuition assertions are being qualified by country; article-specific
APS corrections follow in task 2. Reference-only paths remain unchanged.
The two ambiguous LLM entries and every other LLM audit entry are deferred
under the explicit file freeze. Both LLM files must remain unchanged.
Germany guidance was checked against the opened DAAD finance page, including
Baden-Wuerttemberg and Bavaria exceptions, contributions and living expenses.
Slovak-language duration rules and charged foreign-language study were checked
on the opened Slovak Ministry tuition page. Universitaly procedures were
opened, but do not substantiate the owner scholarship amount or partner claim.
The exact owner Italy sentence is conditional commercial guidance, not an
independently verified award. The Italy DSU article is withheld as draft while
its regional conditions and unsupported benefit claims await official evidence.
Generic merit-award context is not attributed to a country or marked verified.
Prior source blockers remain unresolved unless a later task explicitly records
opened evidence and the exact corrected lines. No search snippet is evidence.

Phase A source URLs opened on 2026-10-16:
- https://www.daad.de/en/studying-in-germany/living-in-germany/finances/
  Confirmed general public-course tuition conditions, Baden-Wuerttemberg,
  Bavaria, semester contributions and separate living expenses.
- https://www.minedu.sk/skolne-na-vysokych-skolach-v-sr/
  Confirmed language and standard-duration conditions; foreign-language fees.
- https://www.universitaly.it/it/studenti-stranieri
  Confirmed admissions/visa responsibilities only, not scholarship amounts.
  Initial /tuition-fees/ ministry URL was a missing page and is not evidence.
Affected website files: about.php, index.php, services.php, blog/index.php,
blog/cost-of-studying-abroad-for-indian-students.php,
blog/scholarships-for-indian-students-study-abroad.php,
blog/italy-dsu-scholarship-eligibility.php and includes/posts.php.
Their audited tuition paragraphs, metadata and FAQ/schema counterparts were
rewritten. Generic award context remains unverified, not country-specific.
All source-line references above refer to the preserved historical audit;
no statement in that audit is treated as proof of current verification.

Task 2, checked 2026-10-16: the existing APS article keeps its canonical slug.
Its title, description, visible introduction and structured headline/description
now describe tuition conditions and procedure applicability rather than a
universal entitlement. DAAD finance and visa pages were opened; APS India
was opened and supports document verification, general applicability and its
procedure overview, not a universal requirement or a promised processing time.
APS host aps-india.de is outside the existing owner-approved source-host list,
so the article is now draft/noindex. It is not included among the 29 original
draft pages. To release it, replace its APS-specific material with an opened
source on an approved host, or obtain an explicit later source-policy change.
The Italy DSU article remains withheld for unsupported regional benefits.
Contact tuition FAQs and decorative labels were also qualified by country;
contact.php uses the same opened Phase A tuition sources, not general
zero-cost claims. No source was verified from a search excerpt.

### Phase B task 3: opened-source review, 2026-10-16

Reviewed in order: Germany, Italy, Slovakia, UK, Czech Republic, Lithuania,
Latvia, GCC, Russia. phase14-source-review.json records each retained field,
URL, checked date and exact confirmed text. Every original fact/FAQ field is
accounted for; unsupported, superseded and disallowed-source lines are removed
rather than marked verified. Summary and provenance values are unchanged.

| Page | Opened source evidence and changes | Remaining source gate |
|---|---|---|
| Germany | DAAD finance: tuition exceptions, corrected contribution range, separate living costs and limited work; visas and side-jobs pages also opened. | None for retained lines; categories checked next. |
| Italy | Bengaluru consulate: admissions, pre-enrolment, appointments, interview, processing, DOV and email warning. Opened linked checklist is 2025-26, not a later intake checklist. Universitaly current procedures also opened, but not added to the destination host list. | No invented later-intake checklist or scholarship entitlement. |
| Slovakia | EC profile and embassy national-visa/contact pages opened. Old generic email-booking and document-age claims removed. The international-organisation source was opened but excluded by the stricter host policy. | Reconfirm the study-specific booking method before applying. |
| UK | GOV.UK financial guidance and English/overview pages opened. Funding amounts confirmed, and exemptions clarified. | None for retained lines; categories checked next. |
| Czech Republic | Embassy current application/booking pages, old 2018 checklist, Interior study visa and archived funds page opened. Tuition portal redirected to a missing page. Current translation, appointment and insurance conditions retained; outdated tuition/range and archived funds claims removed. | Original tuition source unavailable; redirected portal host is outside existing approval. Keep draft pending approved replacement evidence. |
| Lithuania | EC tuition/insurance profile and Migration Department India appointment page opened. Institution-specific immigration source opened but excluded; its D-visa regime and funds statements removed. | Do not resolve conflicting visa descriptions using an unapproved institutional source. |
| Latvia | Embassy Indian-national and general student pages and EC profile opened. Existing appointment, verification and insurance lines confirmed. | None for retained lines; categories checked next. |
| GCC | Dubai advisory redirects to a 2026 document, opened through relevant sections. Qatar advisory, Saudi student table and Bahrain PDF opened. Bahrain release is dated 31 May 2022. Oman URL returned File not found; Kuwait has no usable evidence. | Exclude Oman/Kuwait. Visible scope note required before publishing the remaining four-country material. |
| Russia | Cited Ministry PDF returned a missing page. Search did not supply an opened current replacement. | Zero verified categories this session. Keep all existing source dates unchanged; current notice and expired-window details remain unverified. |

No source-host list was broadened. Non-government/institution-specific hosts
were removed, not silently approved. A successful HTTP page load containing
an error or archive banner is not current factual verification. The JSON
contains no claim that an unavailable Russian notice was read.

### Phase B task 4: substantive category completion

Only opened, approved sources were used for additions, checked 2026-10-16.
Germany gained the DAAD student/prospective-student visa distinction. Italy
gained the consulate statement that each institution sets tuition. UK gained
GOV.UK eligibility and English-evidence rules, including provider assessment
and the degree-level B2 requirement, not a universal test waiver. Latvia gained
the EC profile living-cost estimate, explicitly separate from tuition.
Exact new lines, URLs and dates are in phase14-source-review.json.
Verified category totals: Germany 6, Italy 5, Slovakia 5, UK 6,
Czech Republic 4, Lithuania 5, Latvia 5, GCC 9 and Russia 0.
The Czech tuition-portal and Russian notice failures are not filled with
generic or invented categories. They remain exact publication blockers.
The JSON also records the approved-host snapshot; no new host was approved.

### Phase B task 5: publication decisions

Published Germany, Italy, Slovakia, UK, Lithuania, Latvia and the scoped GCC
guide. Each has at least five genuine sourced categories, a verified intro,
no restricted promotional wording or named institutions, and matched visible
FAQs and schema. The runtime gate now matches every intro/fact/FAQ text,
question, source URL, label and date to the committed review journal; changing
one without review removes publication eligibility. Status alone is not a gate.
The reviewed approved-host snapshot must also match each citation host.

Czech Republic remains draft: four verified categories and an unresolved
tuition source/redirect-host gate. Russia remains draft: zero verified
categories and a missing current notice. Its expired supplied date and lack
of verification are visibly disclosed, without upgrading old source dates.
GCC visibly names its four-country scope, explicitly excludes Oman/Kuwait,
and labels the Bahrain registration notice as dated 31 May 2022 rather than
current visa advice. The country sections each carry their own source.
Both LLM files remain unchanged; discovery snapshot work is scheduled in E.
