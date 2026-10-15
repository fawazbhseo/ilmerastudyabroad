<?php
$fin = 'https://www.gov.uk/guidance/financial-evidence-for-student-and-child-student-route-applicants';
$finLabel = 'GOV.UK: Financial evidence for Student and Child Student visa applicants';
$d = '2026-10-15';

return [
    'slug' => 'uk',
    'name' => 'UK',
    'status' => 'draft',
    'intro_answer' => 'Applicants for a UK Student visa must show enough money to pay their course fees, as shown on the Confirmation of Acceptance for Studies, plus living costs of 1,171 pounds a month outside London or 1,529 pounds a month in London, for up to 9 months. Check GOV.UK for the current amounts.',
    'intro_answer_source_url' => $fin,
    'intro_answer_source_label' => $finLabel,
    'intro_answer_checked_on' => $d,
    'ilmera_summary' => 'Rules can change; ILMERA advises students to confirm current rules at the time of application.',
    'summary_provenance' => 'git:7dfac93:llms-full.txt section 4.3',
    'facts_last_checked' => $d,
    'official_source_hosts' => ['gov.uk'],
    'who_its_for' => [],
    'english_requirements' => [],
    'costs' => [
        ['text' => 'Applicants must show they have enough money to pay their course fees, which are shown on the Confirmation of Acceptance for Studies (CAS) sent by the education provider, plus living costs.', 'source_url' => $fin, 'source_label' => $finLabel, 'checked_on' => $d],
        ['text' => 'For most courses, GOV.UK sets living costs at 1,171 pounds for each month of the course outside London and 1,529 pounds for each month in London, up to a maximum of 9 months. These amounts changed in the past, so check the page for the current figures.', 'source_url' => $fin, 'source_label' => $finLabel, 'checked_on' => $d],
    ],
    'scholarships' => [],
    'visa_steps' => [],
    'intakes' => [],
    'documents' => [
        ['text' => 'Money can be shown through a student loan from a government, a government-sponsored loan company or a regulated student loans scheme, an official financial sponsorship, the applicant own money, a parent money with a letter confirming they agree to its use, or a partner money in some cases.', 'source_url' => $fin, 'source_label' => $finLabel, 'checked_on' => $d],
        ['text' => 'When using personal or family money, the funds must have been held for 28 days in a row, counted back from the closing balance date on the most recent evidence. The evidence must be from no more than 31 days before the visa application date.', 'source_url' => $fin, 'source_label' => $finLabel, 'checked_on' => $d],
        ['text' => 'Accepted evidence includes paper or electronic bank statements, building society passbooks, certificates of deposit and letters from the bank. The evidence must show the account holder name, the bank name and the amount held. Funds in another currency are converted to pounds at the OANDA spot rate on the application date.', 'source_url' => $fin, 'source_label' => $finLabel, 'checked_on' => $d],
        ['text' => 'These cannot be used as proof of funds: overdrafts, cryptocurrency, stocks and shares, pensions, accounts at banks not regulated in their own country, and accounts that do not use electronic record keeping.', 'source_url' => $fin, 'source_label' => $finLabel, 'checked_on' => $d],
    ],
    'work_and_stay' => [],
    'faqs' => [
        ['question' => 'How much money must Indian students show for a UK Student visa?', 'answer' => 'Enough to pay the course fees shown on the CAS plus living costs. GOV.UK sets living costs at 1,171 pounds a month outside London and 1,529 pounds a month in London, up to 9 months. Check the page for the current figures.', 'source_url' => $fin, 'source_label' => $finLabel, 'checked_on' => $d],
        ['question' => 'How long must the money be in the account for a UK Student visa?', 'answer' => 'The funds must have been held for 28 days in a row, counted back from the closing balance date on the most recent evidence, and the evidence must be from no more than 31 days before the application.', 'source_url' => $fin, 'source_label' => $finLabel, 'checked_on' => $d],
        ['question' => 'Can a parent money be used for a UK Student visa?', 'answer' => 'Yes, if the parent controls the account and provides a letter confirming they agree to the money being used for the student.', 'source_url' => $fin, 'source_label' => $finLabel, 'checked_on' => $d],
        ['question' => 'Can Indian students skip showing financial evidence for a UK Student visa?', 'answer' => 'GOV.UK lists nationalities that do not need to provide financial evidence upfront, and India is not on that list. Applicants must still meet the financial requirement, and a decision maker can ask for evidence in any case.', 'source_url' => $fin, 'source_label' => $finLabel, 'checked_on' => $d],
    ],
];
