<?php
require_once __DIR__ . '/posts.php';
require_once __DIR__ . '/place-data.php';
require_once __DIR__ . '/destination-data.php';

/** Reject explicit indexing exclusions without evaluating a page template. */
function ilmera_source_indexable($file, $checkHeaders = true)
{
    if (!is_file($file)) return false;
    $source = file_get_contents($file);
    $html = '';
    foreach (token_get_all($source) as $token) {
        if (is_array($token) && $token[0] === T_INLINE_HTML) $html .= $token[1];
    }
    preg_match_all('/<meta\b[^>]*>/i', $html, $tags);
    foreach ($tags[0] as $tag) {
        if (preg_match('/\bname\s*=\s*([\'"])(robots|googlebot)\1/i', $tag)
            && preg_match('/\bcontent\s*=\s*([\'"])(.*?)\1/i', $tag, $value)
            && preg_match('/\bnoindex\b/i', $value[2])) return false;
    }
    return !$checkHeaders || !preg_match('/header\s*\(\s*[\'"]X-Robots-Tag:\s*[^\'"]*\bnoindex\b/i', $source);
}

function ilmera_static_pages()
{
    static $published = null;
    if ($published !== null) return $published;
    $pages = [
        ['url' => '/', 'title' => 'Home', 'file' => 'index.php', 'type' => 'Main pages'],
        ['url' => '/services', 'title' => 'Services and destinations', 'file' => 'services.php', 'type' => 'Main pages'],
        ['url' => '/about', 'title' => 'About ILMERA and the team', 'file' => 'about.php', 'type' => 'Main pages'],
        ['url' => '/contact', 'title' => 'Contact ILMERA', 'file' => 'contact.php', 'type' => 'Main pages'],
        ['url' => '/blog/', 'title' => 'Blog', 'file' => 'blog/index.php', 'type' => 'Main pages'],
        ['url' => '/privacy-policy', 'title' => 'Privacy Policy', 'file' => 'privacy-policy.php', 'type' => 'Legal pages'],
        ['url' => '/terms', 'title' => 'Terms of Use', 'file' => 'terms.php', 'type' => 'Legal pages'],
        ['url' => '/all-pages', 'title' => 'All pages', 'file' => 'all-pages.php', 'type' => 'Directory'],
    ];
    return $published = array_values(array_filter($pages, static function ($page) {
        $file = dirname(__DIR__) . '/' . $page['file'];
        return ilmera_source_indexable($file);
    }));
}

function ilmera_target_published($url)
{
    if (!is_string($url) || strpos($url, '\\') !== false || strpos($url, '//') === 0) return false;
    $parts = parse_url($url);
    if ($parts === false || isset($parts['user']) || isset($parts['pass'])) return false;
    if (isset($parts['host']) && strtolower($parts['host']) !== 'ilmerastudyabroad.com') return false;
    if (isset($parts['scheme']) && !in_array(strtolower($parts['scheme']), ['http', 'https'], true)) return false;
    $path = strtolower(rawurldecode($parts['path'] ?? '/'));
    $path = rtrim(preg_replace('/\.php\/?$/i', '', $path), '/') ?: '/';
    if ($path === '/index') $path = '/';
    if ($path === '/blog/index') $path = '/blog';
    if (preg_match('#^/blog/([a-z0-9-]+)$#D', $path, $match)) return ilmera_post_published($match[1]) && ilmera_source_indexable(dirname(__DIR__) . '/blog/' . $match[1] . '.php');
    if (preg_match('#^/study-abroad-(?:counselling|consultants-in)-([a-z0-9-]+)$#D', $path, $match)) {
        $place = ilmera_place_load($match[1]);
        return ilmera_place_indexable($place) && $path === ilmera_place_url($place) && ilmera_source_indexable(dirname(__DIR__) . $path . '.php') && ilmera_source_indexable(__DIR__ . '/place-page.php', false);
    }
    if (preg_match('#^/study-in-([a-z0-9-]+)$#D', $path, $match)) {
        $destination = ilmera_destination_load($match[1]);
        return ilmera_destination_indexable($destination) && ilmera_source_indexable(dirname(__DIR__) . $path . '.php') && ilmera_source_indexable(__DIR__ . '/destination-page.php', false);
    }
    foreach (ilmera_static_pages() as $page) if ($path === (rtrim($page['url'], '/') ?: '/')) return true;
    return false;
}

function ilmera_link($url, $label, $attributes = [])
{
    if (!ilmera_target_published($url)) return '';
    $html = '<a href="' . ilmera_post_escape($url) . '"';
    foreach ($attributes as $name => $value) {
        if (in_array($name, ['class', 'style', 'title', 'aria-label'], true)) $html .= ' ' . $name . '="' . ilmera_post_escape($value) . '"';
    }
    return $html . '>' . ilmera_post_escape($label) . '</a>';
}

function ilmera_post_link($slug, $label = null, $attributes = [])
{
    $post = ilmera_post($slug);
    return $post && ilmera_post_published($slug) ? ilmera_link('/blog/' . $slug, $label ?? $post['title'], $attributes) : '';
}

function ilmera_place_link($slug, $attributes = [])
{
    $place = ilmera_place_load($slug);
    return ilmera_place_indexable($place) ? ilmera_link(ilmera_place_url($place), $place['name'], $attributes) : '';
}

function ilmera_place_groups()
{
    $groups = ['Karnataka' => [], 'Districts' => [], 'Towns and cities' => []];
    foreach (ilmera_indexable_locations() as $place) {
        $group = $place['slug'] === 'karnataka' ? 'Karnataka' : ($place['type'] === 'district-hub' ? 'Districts' : 'Towns and cities');
        $groups[$group][] = $place;
    }
    foreach ($groups as &$places) usort($places, static function ($a, $b) { return strcasecmp($a['name'], $b['name']); });
    unset($places);
    return array_filter($groups);
}

function ilmera_ranked_guides($slugs, $limit = 2)
{
    $posts = [];
    foreach (array_unique($slugs) as $slug) {
        if (ilmera_post_published($slug)) $posts[] = ilmera_post($slug);
        if (count($posts) >= $limit) break;
    }
    return $posts;
}

function ilmera_country_guides($country)
{
    $specific = [
        'germany' => ['study-in-germany-free-aps-certificate'],
        'italy' => ['italy-dsu-scholarship-eligibility', 'scholarships-for-indian-students-study-abroad'],
        'russia' => ['study-abroad-with-academic-backlogs'],
    ];
    return ilmera_ranked_guides(array_merge($specific[$country] ?? [], ['documents-needed-to-study-abroad-from-india', 'cost-of-studying-abroad-for-indian-students', 'study-abroad-counselling-from-coorg']));
}

function ilmera_place_guides()
{
    return ilmera_ranked_guides(['study-abroad-counselling-from-coorg', 'documents-needed-to-study-abroad-from-india', 'cost-of-studying-abroad-for-indian-students', 'study-abroad-with-academic-backlogs'], 3);
}

function ilmera_render_guides($posts, $heading = 'Related guides', $level = 2)
{
    $posts = array_values(array_filter($posts, static function ($post) { return ilmera_post_published($post['slug']); }));
    if (!$posts) return;
    $level = in_array($level, [2, 3], true) ? $level : 2;
    echo '<section class="related-guides" aria-label="' . ilmera_post_escape($heading) . '" style="margin-top:32px;">';
    echo '<h' . $level . ' style="font-family:Outfit,sans-serif;font-size:20px;line-height:1.4;margin-bottom:16px;">' . ilmera_post_escape($heading) . '</h' . $level . '>';
    echo '<ul style="padding-left:20px;line-height:1.7;">';
    foreach ($posts as $post) echo '<li style="margin-bottom:10px;">' . ilmera_post_link($post['slug'], null, ['style' => 'color:inherit;text-decoration:underline;text-underline-offset:3px;']) . '</li>';
    echo '</ul></section>';
}

function ilmera_post_service_links($slug)
{
    $targets = [
        'study-in-germany-free-aps-certificate' => ['germany' => 'Study in Germany'],
        'italy-dsu-scholarship-eligibility' => ['italy' => 'Study in Italy'],
        'study-abroad-with-academic-backlogs' => ['russia' => 'Study in Russia'],
        'study-abroad-counselling-from-coorg' => ['process' => 'Our counselling process'],
        'cost-of-studying-abroad-for-indian-students' => ['germany' => 'Study in Germany', 'italy' => 'Study in Italy'],
        'documents-needed-to-study-abroad-from-india' => ['germany' => 'Study in Germany', 'italy' => 'Study in Italy'],
        'scholarships-for-indian-students-study-abroad' => ['italy' => 'Study in Italy', 'germany' => 'Study in Germany'],
    ];
    $links = [];
    foreach ($targets[$slug] ?? [] as $section => $label) {
        $url = ilmera_post_published($slug) && in_array($section, ilmera_destination_slugs(), true) ? ilmera_destination_target($section) : '/services#' . $section;
        $link = ilmera_link($url, $label, ['style' => 'color:var(--gold);']);
        if ($link !== '') $links[] = $link;
    }
    $contact = ilmera_link('/contact', 'Contact ILMERA about your plans', ['style' => 'color:var(--gold);']);
    if ($contact !== '') $links[] = $contact;
    return $links ? '<p style="margin-top:24px;">' . implode(' &middot; ', $links) . '</p>' : '';
}

function ilmera_published_destinations()
{
    $destinations = [];
    foreach (ilmera_destination_slugs() as $slug) {
        $destination = ilmera_destination_load($slug);
        if ($destination && $destination['status'] === 'published' && ilmera_target_published(ilmera_destination_url($destination))) {
            $destination['url'] = ilmera_destination_url($destination);
            $destination['file'] = ltrim($destination['url'], '/') . '.php';
            $destinations[] = $destination;
        }
    }
    return $destinations;
}

/** Indexable location entries, separate from country destinations. */
function ilmera_indexable_locations()
{
    $locations = [];
    foreach (glob(dirname(__DIR__) . '/places/*.php') as $file) {
        $place = ilmera_place_load(basename($file, '.php'));
        if (!$place || !ilmera_target_published(ilmera_place_url($place))) continue;
        $place['url'] = ilmera_place_url($place);
        $place['file'] = ltrim($place['url'], '/') . '.php';
        $locations[] = $place;
    }
    usort($locations, static function ($a, $b) { return strcasecmp($a['name'], $b['name']); });
    return $locations;
}

function ilmera_destination_target($slug)
{
    if (!in_array($slug, ilmera_destination_slugs(), true)) return '/services';
    $url = '/study-in-' . $slug;
    return ilmera_target_published($url) ? $url : '/services#' . $slug;
}

function ilmera_destination_link($slug, $label = null, $attributes = [])
{
    $destination = ilmera_destination_load($slug);
    return $destination ? ilmera_link(ilmera_destination_url($destination), $label ?? ('Study in ' . $destination['name']), $attributes) : '';
}

function ilmera_place_destination_links($data)
{
    if (!ilmera_place_indexable($data)) return '';
    $content = array_intersect_key($data, array_flip(['intro_answer', 'local_institutions', 'transcript_and_moi_steps', 'local_loan_options', 'visa_appointment_route', 'local_notes', 'faqs']));
    $text = '';
    array_walk_recursive($content, static function ($value) use (&$text) { if (is_string($value)) $text .= ' ' . $value; });
    $links = [];
    foreach (ilmera_published_destinations() as $destination) {
        $name = preg_quote($destination['name'], '/');
        if ($destination['slug'] === 'uk') $name = '(?:UK|United Kingdom)';
        if (preg_match('/(?<![a-z])' . $name . '(?![a-z])/i', $text)) {
            $link = ilmera_destination_link($destination['slug'], null, ['style' => 'color:var(--gold);']);
            if ($link !== '') $links[] = '<li>' . $link . '</li>';
        }
    }
    return $links ? '<section><h2>Destination guides</h2><ul>' . implode('', $links) . '</ul></section>' : '';
}
