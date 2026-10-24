<?php
/* Post metadata is the single publication switch for article pages. */
function ilmera_posts()
{
    static $posts = [
        'how-to-choose-study-abroad-consultant-karnataka' => [
            'slug' => 'how-to-choose-study-abroad-consultant-karnataka',
            'title' => 'How to choose a study abroad consultant in Karnataka',
            'excerpt' => 'Ten practical checks for families comparing counselling scope, fees, document handling, privacy and responsibilities.',
            'category' => 'Planning',
            'readMinutes' => 6,
            'datePublished' => '2026-10-16',
            'dateModified' => '2026-10-16',
            'status' => 'published',
            'related' => ['study-abroad-counselling-from-coorg', 'documents-needed-to-study-abroad-from-india'],
        ],
        'study-in-germany-free-aps-certificate' => [
            'slug' => 'study-in-germany-free-aps-certificate',
            'title' => 'Germany Tuition and APS: Check the Applicable Route',
            'excerpt' => 'Check public-programme tuition exceptions, separate living costs and the APS procedure that applies to your academic background. No admission or visa outcome is guaranteed.',
            'category' => 'Germany',
            'readMinutes' => 5,
            'datePublished' => '2025-08-13',
            'dateModified' => '2026-10-16',
            'status' => 'draft',
            'related' => ['italy-dsu-scholarship-eligibility', 'study-abroad-with-academic-backlogs', 'study-abroad-counselling-from-coorg'],
        ],
        'italy-dsu-scholarship-eligibility' => [
            'slug' => 'italy-dsu-scholarship-eligibility',
            'title' => 'Italy Scholarship Planning: Verification Needed',
            'excerpt' => 'Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility.',
            'category' => 'Italy',
            'readMinutes' => 5,
            'datePublished' => '2025-08-20',
            'dateModified' => '2026-10-16',
            'status' => 'draft',
            'related' => ['study-in-germany-free-aps-certificate', 'study-abroad-with-academic-backlogs', 'study-abroad-counselling-from-coorg'],
        ],
        'study-abroad-with-academic-backlogs' => [
            'slug' => 'study-abroad-with-academic-backlogs',
            'title' => 'Studying Abroad with Academic Backlogs: What Is Actually Possible',
            'excerpt' => 'Backlogs do not automatically rule out studying abroad. Several countries have more flexible entry processes. Here is a realistic look at where those options exist.',
            'category' => 'No-IELTS',
            'readMinutes' => 4,
            'datePublished' => '2025-08-27',
            'dateModified' => '2026-10-16',
            'status' => 'published',
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-counselling-from-coorg'],
        ],
        'study-abroad-counselling-from-coorg' => [
            'slug' => 'study-abroad-counselling-from-coorg',
            'title' => 'Online Study Abroad Counselling for Coorg Students: How the Process Works',
            'excerpt' => 'ILMERA provides online counselling for students from Coorg and Kodagu by phone, WhatsApp and video call. Here is exactly what that process looks like, step by step.',
            'category' => 'Coorg',
            'readMinutes' => 4,
            'datePublished' => '2025-09-03',
            'dateModified' => '2026-10-16',
            'status' => 'published',
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-with-academic-backlogs'],
        ],
        'cost-of-studying-abroad-for-indian-students' => [
            'slug' => 'cost-of-studying-abroad-for-indian-students',
            'title' => 'Cost of Studying Abroad: Official Country Examples',
            'excerpt' => 'Compare sourced tuition and living-cost examples for six countries, plus UAE budgeting advice. Separate estimates from visa financial requirements.',
            'category' => 'Costs',
            'readMinutes' => 5,
            'datePublished' => '2026-10-16',
            'dateModified' => '2026-10-16',
            'status' => 'published',
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-with-academic-backlogs'],
        ],
        'documents-needed-to-study-abroad-from-india' => [
            'slug' => 'documents-needed-to-study-abroad-from-india',
            'title' => 'Documents Needed to Study Abroad: Build a Route-Specific Checklist',
            'excerpt' => 'Official document examples for selected study routes. Separate admission, financial evidence and visa instructions instead of relying on one universal checklist.',
            'category' => 'Visas',
            'readMinutes' => 5,
            'datePublished' => '2026-10-16',
            'dateModified' => '2026-10-16',
            'status' => 'published',
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-with-academic-backlogs'],
        ],
        'scholarships-for-indian-students-study-abroad' => [
            'slug' => 'scholarships-for-indian-students-study-abroad',
            'title' => 'Scholarships for Indian Students: Check Eligibility and Evidence',
            'excerpt' => 'Use official funding examples to distinguish tuition policy, scholarship opportunities and documented sponsorship. No unverified award amounts or promises.',
            'category' => 'Scholarships',
            'readMinutes' => 5,
            'datePublished' => '2026-10-16',
            'dateModified' => '2026-10-16',
            'status' => 'published',
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-with-academic-backlogs'],
        ],
    ];
    return $posts;
}

function ilmera_post($slug)
{
    $posts = ilmera_posts();
    return is_string($slug) && isset($posts[$slug]) ? $posts[$slug] : null;
}

function ilmera_post_published($slug)
{
    $post = ilmera_post($slug);
    if (!$post || $post['status'] !== 'published' || !is_file(dirname(__DIR__) . '/blog/' . $post['slug'] . '.php')) return false;
    $reviewed = ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'cost-of-studying-abroad-for-indian-students', 'documents-needed-to-study-abroad-from-india', 'scholarships-for-indian-students-study-abroad'];
    if (!in_array($slug, $reviewed, true)) return true;
    static $journal = null;
    if ($journal === null) {
        $file = dirname(__DIR__) . '/phase14-article-review.json';
        $journal = is_file($file) ? json_decode(file_get_contents($file), true) : [];
        if (!is_array($journal)) $journal = [];
    }
    $entry = $journal['articles'][$slug] ?? [];
    if (($entry['verified'] ?? false) !== true || !empty($entry['failed_gates']) ||
        hash_file('sha256', dirname(__DIR__) . '/blog/' . $slug . '.php') !== ($entry['file_sha256'] ?? '')) return false;
    foreach ($entry['metadata'] ?? [] as $key => $value) if (($post[$key] ?? null) !== $value) return false;
    if (empty($entry['sources']) || ($entry['approved_hosts_only'] ?? false) !== true) return false;
    $urls = [];
    foreach ($entry['sources'] as $source) {
        $url = $source['url'] ?? '';
        $host = strtolower(parse_url($url, PHP_URL_HOST) ?? '');
        $approved = preg_match('/(?:^|\.)(?:gov\.in|nic\.in)$/D', $host) === 1;
        foreach ($journal['approved_hosts'] ?? [] as $official) if ($host === $official || str_ends_with($host, '.' . $official)) $approved = true;
        if (!$approved || parse_url($url, PHP_URL_SCHEME) !== 'https' || empty($source['checked_on'])) return false;
        $urls[] = $url;
    }
    foreach ($entry['retained_claims'] ?? [] as $claim) {
        if (($claim['verified'] ?? false) !== true || empty($claim['source_urls'])) return false;
        foreach ($claim['source_urls'] as $url) if (!in_array($url, $urls, true)) return false;
    }
    return !empty($entry['retained_claims']);
}

function ilmera_published_posts($latest = false)
{
    $posts = array_values(array_filter(ilmera_posts(), static function ($post) { return ilmera_post_published($post['slug']); }));
    if ($latest) usort($posts, static function ($a, $b) { return strcmp($b['datePublished'], $a['datePublished']) ?: strcmp($a['slug'], $b['slug']); });
    return $posts;
}

function ilmera_post_related($slug, $limit = 3)
{
    $post = ilmera_post($slug);
    if (!$post) return [];
    $found = [];
    foreach (array_merge($post['related'], array_keys(ilmera_posts())) as $candidate) {
        if ($candidate !== $slug && ilmera_post_published($candidate)) $found[$candidate] = ilmera_post($candidate);
        if (count($found) >= $limit) break;
    }
    return array_values($found);
}

function ilmera_post_escape($text)
{
    return htmlspecialchars($text, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}
