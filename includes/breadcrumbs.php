<?php
require_once __DIR__ . '/posts.php';
require_once __DIR__ . '/place-data.php';

function ilmera_breadcrumb_parent_ready($url)
{
    $path = rawurldecode(parse_url($url, PHP_URL_PATH) ?: '/');
    $path = preg_replace('/\.php\/?$/i', '', $path);
    if (preg_match('#^/blog/([a-z0-9-]+)/?$#i', $path, $match)) return ilmera_post_published(strtolower($match[1]));
    if (preg_match('#^/study-abroad-(?:counselling|consultants-in)-([a-z0-9-]+)/?$#i', $path, $match)) {
        return ilmera_place_indexable(ilmera_place_load(strtolower($match[1])));
    }
    return in_array($path, ['/', '/about', '/contact', '/services', '/blog', '/blog/', '/terms', '/privacy-policy', '/all-pages'], true);
}

function ilmera_breadcrumb_trail($trail)
{
    $items = [];
    foreach ($trail as $position => $item) {
        if (!isset($item['name'], $item['url'])) continue;
        if ($position < count($trail) - 1 && !ilmera_breadcrumb_parent_ready($item['url'])) continue;
        $items[] = ['name' => $item['name'], 'url' => $item['url']];
    }
    return $items;
}

function ilmera_breadcrumbs($trail, $canonical)
{
    $items = ilmera_breadcrumb_trail($trail);
    if (!$items) return;
    $schemaItems = [];
    echo '<nav class="breadcrumb" aria-label="Breadcrumb">';
    foreach ($items as $position => $item) {
        if ($position) echo ' &nbsp;/&nbsp; ';
        $name = htmlspecialchars($item['name'], ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
        if ($position < count($items) - 1) echo '<a href="' . htmlspecialchars($item['url'], ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') . '">' . $name . '</a>';
        else echo '<span aria-current="page">' . $name . '</span>';
        $schemaItems[] = ['@type' => 'ListItem', 'position' => $position + 1, 'name' => $item['name'], 'item' => 'https://ilmerastudyabroad.com' . $item['url']];
    }
    echo '</nav>';
    echo '<script type="application/ld+json">' . json_encode(['@context' => 'https://schema.org', '@type' => 'BreadcrumbList', '@id' => 'https://ilmerastudyabroad.com' . $canonical . '#breadcrumb', 'itemListElement' => $schemaItems], JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_UNESCAPED_SLASHES | JSON_INVALID_UTF8_SUBSTITUTE) . '</script>';
}
