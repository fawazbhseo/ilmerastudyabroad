# Live deployment: backup and checks

Owner checklist, 2026-10-16. Deploy directly to the live site; no staging step.

1. **Back up the live site first.** Download a complete copy of the current
   live files, including hidden files such as `.htaccess`, and save the settings
   needed to restore them. Label the backup with its date and time. Keep it
   outside the public website and confirm that you can open it before uploading
   anything. Keep private configuration private.

2. Upload only the reviewed release files. The Phase 13 `.htaccess` rules are
   already live; this checklist does not ask you to reapply them. Clear the
   site's cache if your hosting provides one.

3. **Test the actual live website**, on a phone and a computer. Open the
   homepage, Services, Contact, Blog, All Pages and `/sitemap.xml`. Follow links
   to all seven published destinations, 17 location guides and five articles.
   Check that each address opens the intended page with readable content.
   Try an old `.php` address and a missing address to check the existing
   redirects and not-found response.

4. On Contact, check the phone and WhatsApp links. Send one clearly labelled
   test enquiry through the offered contact method and confirm receipt. Check
   that the page describes online counselling, not a meeting location.

5. Open `/llms.txt` and `/llms-full.txt` on the live site. Check their page
   links, online-only wording and conditional scholarship/GCC notes. Check
   that a held address, such as `/study-in-russia`, is absent from the live
   sitemap and published page links. Hidden discovery is not access control.

6. **Do a no-cost external-citation broken-link check:** open every official
   source link on the published pages in a browser. Confirm that it reaches
   the expected official information, not an error or unrelated landing page.
   Record and resolve failed links; a page merely opening is not proof that
   it supports a claim.

7. After these checks pass, submit
   `https://ilmerastudyabroad.com/sitemap.xml` in Google Search Console for the
   live website. Watch its processing and indexing reports.

8. **If a page, redirect or enquiry check fails, restore the backed-up live
   files and relevant settings**, not just `.htaccess`. Clear the cache and
   repeat the live checks. Stop the release and fix the cause before trying
   again or submitting the changed sitemap.
