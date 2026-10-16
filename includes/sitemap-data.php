<?php
require_once __DIR__ . '/links.php';

/** Canonical indexable editorial routes, with no utility endpoints. */
function ilmera_sitemap_pages()
{
    $pages = [];
    // Editorial dates survive checkout/deploy; build-time mtimes do not.
    $staticDates = ['/' => '2026-10-16', '/services' => '2026-10-16', '/about' => '2026-10-16', '/contact' => '2026-10-16', '/blog/' => '2026-10-16', '/privacy-policy' => '2026-10-15', '/terms' => '2026-10-16', '/all-pages' => '2026-10-16'];
    foreach (ilmera_static_pages() as $page) {
        $page['name'] = $page['title'];
        $page['lastmod'] = $staticDates[$page['url']] ?? '';
        $pages[$page['url']] = $page;
    }
    foreach (ilmera_published_posts() as $post) {
        $url = '/blog/' . $post['slug'];
        if (!ilmera_target_published($url)) continue;
        $pages[$url] = ['url' => $url, 'name' => $post['title'], 'file' => 'blog/' . $post['slug'] . '.php', 'lastmod' => $post['dateModified']];
    }
    foreach (ilmera_published_destinations() as $page) {
        $source = ilmera_destination_load($page['slug']);
        $page['lastmod'] = $source['publication_review']['checked_on'] ?? '';
        $page['data_file'] = 'destinations/' . $page['slug'] . '.php';
        $page['template_file'] = 'includes/destination-page.php';
        $pages[$page['url']] = $page;
    }
    foreach (ilmera_indexable_locations() as $page) {
        $source = ilmera_place_load($page['slug']);
        $page['lastmod'] = $source['reviewed_on'] ?? '';
        $page['data_file'] = 'places/' . $page['slug'] . '.php';
        $page['template_file'] = 'includes/place-page.php';
        $pages[$page['url']] = $page;
    }
    return array_values($pages);
}

function ilmera_sitemap_lastmod($page)
{
    return ilmera_destination_date($page['lastmod'] ?? '');
}

function ilmera_sitemap_xml()
{
    $xml = '<?xml version="1.0" encoding="UTF-8"?>' . "\n";
    $xml .= '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' . "\n";
    foreach (ilmera_sitemap_pages() as $page) {
        $url = htmlspecialchars('https://ilmerastudyabroad.com' . $page['url'], ENT_XML1 | ENT_QUOTES, 'UTF-8');
        $xml .= "\n  <url>\n    <loc>" . $url . "</loc>\n";
        $date = ilmera_sitemap_lastmod($page);
        if ($date !== '') $xml .= '    <lastmod>' . $date . "</lastmod>\n";
        $xml .= "  </url>\n";
    }
    return $xml . "</urlset>\n";
}
