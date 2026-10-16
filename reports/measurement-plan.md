# Measurement decision

Date: 2026-10-16. No analytics implementation was found in executable PHP,
JavaScript or HTML: no existing tag manager, analytics measurement ID, tracker
initialisation or event transport. The task adds no analytics tag, event
sender, cookie mechanism or third-party script.

**Owner decision outstanding:** choose whether to use analytics and approve
the provider, property, consent/privacy approach and actual success signal.
This is not a request to add a tag without permission.

If approved later:

- Count descriptive contact links as `contact_cta_click`, with `page_type`
  (`destination`, `location`, `article` or `other`) and a non-sensitive route.
  Existing CTAs already carry the page-type label for a future approved
  implementation; no tracking event is sent now.
- Count `contact_enquiry_confirmed` only after the actual contact system
  confirms success. A click, form submit attempt or opened messaging app is
  not confirmed delivery. Use the originating page type where known.
- Do not send names, email addresses, phone numbers, document contents,
  academic records, message text or personal query strings.
- Test events in the owner's approved property and check real enquiry receipt
  separately. No live delivery or event reception has been verified here.

The source search covered root/blog PHP, shared includes and any local script
assets, excluding historical reports and dependencies. Analytics-related
words in documentation are not an installed tag. Privacy wording must be
reviewed with the owner before any later tracking implementation.
