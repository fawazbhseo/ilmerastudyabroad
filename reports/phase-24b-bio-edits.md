# Phase 24b biography alignment inventory

Both final owner texts are used verbatim. Portfolio findings:
`phase-24b-portfolio-check.md`. No requested detail needed more conservative
wording. Existing Jabir source bytes, profile data, portraits/titles/alts and
all university-blocklist entries are unchanged.

## Every active biography edit

1. About Fawaz team card: replace the previous card variant with the full
   approved bio, plain text, including the early-2025 date and diploma.
2. About Fawaz legacy Person description: replace its shorter variant.
3. About Fawaz legacy credential nodes: remove the separate detailed array;
   credentials now appear only in the exact approved bio. This avoids an
   extra institute Organization/name context and narrower certificate labels
   differing from the approved wording. Canonical Person remains the source.
4. About Fawaz legacy Person sameAs: exactly the two approved portfolio/LinkedIn
   URLs, no additional profile or institution link.
5. About Fawaz visible FAQ and matching FAQ schema answer: exact approved bio.
6. About Zaheer card, legacy Person description, visible FAQ and matching FAQ
   schema answer: exact new approved bio, replacing Phase 24's minimal sentence.
7. Home Fawaz card: replace the short role summary with the full approved bio.
8. Home Zaheer card: replace Phase 24 sentence with the new approved bio.
9. Home legacy Fawaz/Zaheer Person nodes: add the exact approved descriptions;
   Fawaz sameAs is exactly the two approved URLs. Title labels stay unchanged.
10. data/team.json: the two descriptions and Fawaz-only sameAs, with a current
    owner-review date/basis. Jabir record is byte-equivalent as JSON data.
11. Shared canonical Person descriptions: generated from team data on all 38
    published routes, with Fawaz sameAs only on his Person record.
12. llms.txt and llms-full.txt: existing-generator leadership biographies use
    the exact two approved texts. Existing directory/country facts unchanged.

Visible biography locations: Home `/`, About `/about` (cards and two person
FAQs). Schema descriptions: all 38 published routes, enumerated in the final
release report. Both LLM documents contain each bio once. Historical audit
inventories and negative-test/source-transform strings are internal evidence,
not active biographies; earlier blockers are not rewritten.

Adrex Media School is a digital-marketing training institute. The explicit
name guard masks only the two full exact approved bios for this institute;
it checks every university name against the original unmasked text. Stray
institute mentions and changed bios fail. Current render checks additionally
restrict use to the two visible bio locations, Person descriptions and About
FAQ answers. No service/partner affiliation is introduced.

Task 1 complete local suite: PASS, 556.92 seconds, 92 PHP lints, 43 renders,
258 browser cases, 36 team-photo checks and 1,278 FAQ interactions. Registration,
all non-bio schema and all non-team visible facts remain identical to baseline.
