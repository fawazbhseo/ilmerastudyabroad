# Owner proof slots

All slots in `data/proof.php` are empty. No strategy-document proof was used.
Empty, incomplete, unapproved or policy-rejected records render nothing:
no heading, placeholder, number or schema is emitted.

## Common approval fields

Each record needs `approved` set to boolean true, a supporting `source_url`
using HTTPS, and `reviewed_on` in YYYY-MM-DD format. Approval means the owner
has checked authenticity, accuracy, permission and current applicability.
A URL/date flag is not independent verification by this code. Do not publish
sensitive evidence or personal records. Technical checks also reject banned
copy, institutional aliases and premises claims. Human review is still needed
for names/claims not present in the maintained denylist.

## Fields that turn on each block

| Slot | Additional required fields | Visible placement | Allowed structured data |
| --- | --- | --- | --- |
| `testimonials` array | `display_name`, `text`, `consent: true` | About only | None: review and rating schema is prohibited |
| `placement_count` record or null | integer `value`, precise `definition`, `period` | About only | None: no unsuitable performance/rating property is invented |
| `founder_bios` array | existing founder `name` exactly Jabir KJ, `bio`, `consent: true` | About only | Matching description on the existing founder Person |
| `registration_details` array | `label`, `value` for verified registration identification | About and Contact | Matching Organization identifier PropertyValue |
| `fee_information` array | `service` matching an existing canonical service, `scope`, nonnegative numeric `price`, three-letter `currency`, `refund_terms` | Services and Contact | Matching Service/Offer through the canonical Organization |

For arrays, add a record only after verification; do not replace the empty
slots with example records. For a single placement record, replace null only
with evidenced, clearly defined information. Review scope and period before
publishing a count. Never infer a result from an enquiry or application.

The service names are in `data/entity.json`. Fees must specify the actual
written scope and refund terms. A registration identifier is not an address
or an affiliation. Founder biography text must not introduce unverified
credentials. Testimonial publication needs explicit consent and a traceable
real account; no incentive, manufactured praise or copied review is allowed.

After an owner edit, run the complete publication checks and inspect the
visible blocks and allowed schema together before deployment. The empty-slot
regression must be deliberately replaced with owner-approved populated-data
expectations if real proof is later enabled. Never add rating, review or
local-premises schema. All current slots must remain empty for this phase.
