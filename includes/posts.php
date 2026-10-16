<?php
/* Post metadata is the single publication switch for article pages. */
function ilmera_posts()
{
    static $posts = [
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
            'title' => 'Italy\'s DSU Scholarship: Who Actually Qualifies',
            'excerpt' => 'Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility.',
            'category' => 'Italy',
            'readMinutes' => 4,
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
            'dateModified' => '2026-10-01',
            'status' => 'published',
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-counselling-from-coorg'],
        ],
        'study-abroad-counselling-from-coorg' => [
            'slug' => 'study-abroad-counselling-from-coorg',
            'title' => 'Study Abroad Counselling from Coorg: How the Process Works Without a City Office',
            'excerpt' => 'ILMERA is based in Coorg, Kodagu, and works with students by phone, WhatsApp, and video call. Here is exactly what that process looks like, step by step.',
            'category' => 'Coorg',
            'readMinutes' => 4,
            'datePublished' => '2025-09-03',
            'dateModified' => '2026-10-01',
            'status' => 'published',
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-with-academic-backlogs'],
        ],
        'cost-of-studying-abroad-for-indian-students' => [
            'slug' => 'cost-of-studying-abroad-for-indian-students',
            'title' => 'Cost of Studying Abroad for Indian Students: Country Comparison',
            'excerpt' => 'How much does it cost to study abroad from India? A country-by-country comparison of tuition and living costs across Germany, Italy, the UK, Russia and more, updated October 2026.',
            'category' => 'Costs',
            'readMinutes' => 6,
            'datePublished' => '2026-10-01',
            'dateModified' => '2026-10-01',
            'status' => 'draft',
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-with-academic-backlogs'],
        ],
        'documents-needed-to-study-abroad-from-india' => [
            'slug' => 'documents-needed-to-study-abroad-from-india',
            'title' => 'Documents Needed to Study Abroad from India: The Country-by-Country Checklist',
            'excerpt' => 'The document checklist for studying abroad from India: academic records, proof of funds, passport, language proof and country-specific extras like APS and blocked accounts, updated October 2026.',
            'category' => 'Visas',
            'readMinutes' => 6,
            'datePublished' => '2026-10-01',
            'dateModified' => '2026-10-01',
            'status' => 'draft',
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-with-academic-backlogs'],
        ],
        'scholarships-for-indian-students-study-abroad' => [
            'slug' => 'scholarships-for-indian-students-study-abroad',
            'title' => 'Scholarships for Indian Students to Study Abroad: The Honest Guide',
            'excerpt' => 'Which scholarships can Indian students actually get? Italy DSU, German conditional tuition planning universities, university awards and government schemes, explained without inflated promises, updated October 2026.',
            'category' => 'Scholarships',
            'readMinutes' => 6,
            'datePublished' => '2026-10-01',
            'dateModified' => '2026-10-01',
            'status' => 'draft',
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
    return $post && $post['status'] === 'published' && is_file(dirname(__DIR__) . '/blog/' . $post['slug'] . '.php');
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
