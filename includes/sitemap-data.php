<?php
require_once __DIR__ . '/links.php';

/** Canonical indexable editorial routes, with no utility endpoints. */
function ilmera_sitemap_pages()
{
    $pages = [];
    foreach (ilmera_static_pages() as $page) {
        $page['name'] = $page['title'];
        $pages[$page['url']] = $page;
    }
    foreach (ilmera_published_posts() as $post) {
        $url = '/blog/' . $post['slug'];
        if (!ilmera_target_published($url)) continue;
        $pages[$url] = ['url' => $url, 'name' => $post['title'], 'file' => 'blog/' . $post['slug'] . '.php'];
    }
    foreach (ilmera_published_destinations() as $page) {
        $page['data_file'] = 'destinations/' . $page['slug'] . '.php';
        $page['template_file'] = 'includes/destination-page.php';
        $pages[$page['url']] = $page;
    }
    foreach (ilmera_indexable_locations() as $page) {
        $page['data_file'] = 'places/' . $page['slug'] . '.php';
        $page['template_file'] = 'includes/place-page.php';
        $pages[$page['url']] = $page;
    }
    return array_values($pages);
}

function ilmera_sitemap_lastmod($page)
{
    $times = [];
    foreach (['file', 'data_file', 'template_file'] as $field) {
        if (!isset($page[$field])) continue;
        $file = dirname(__DIR__) . '/' . $page[$field];
        if (is_file($file)) $times[] = filemtime($file);
    }
    if (!$times) return '';
    $timestamp = max($times);
    return $timestamp > 0 && $timestamp <= time() ? gmdate('Y-m-d', $timestamp) : '';
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
