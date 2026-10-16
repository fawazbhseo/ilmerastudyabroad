<?php
/** Reviewed presentation overlays. Publication data and its source gates stay intact. */
function ilmera_presentation_escape($text)
{
    return htmlspecialchars($text, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

function ilmera_presentation_graph($node, $entry)
{
    if (!is_array($node)) return $node;
    $type = $node['@type'] ?? '';
    if (in_array($type, ['WebPage', 'Article', 'BlogPosting', 'Service'], true)) {
        $node['description'] = $entry['description'];
        if (isset($node['name'])) $node['name'] = $entry['title'];
        if (isset($node['headline'])) $node['headline'] = $entry['h1'];
    }
    foreach ($node as $key => $value) {
        if (is_array($value)) $node[$key] = ilmera_presentation_graph($value, $entry);
    }
    return $node;
}

function ilmera_present_page($html)
{
    if (!preg_match('~<link[^>]+rel="canonical"[^>]+href="https://ilmerastudyabroad.com([^"]*)"~', $html, $match)) return $html;
    $path = $match[1] ?: '/';
    $map = json_decode(file_get_contents(dirname(__DIR__) . '/data/seo-map.json'), true);
    if (!isset($map[$path]) || preg_match('~<meta[^>]+name="robots"[^>]+content="[^"]*noindex~i', $html)) return $html;
    $entry = $map[$path];
    $title = ilmera_presentation_escape($entry['title']);
    $description = ilmera_presentation_escape($entry['description']);
    $html = preg_replace('~<title>.*?</title>~s', '<title>' . $title . '</title>', $html, 1);
    $html = preg_replace_callback('~<meta\b[^>]*>~i', static function ($match) use ($title, $description) {
        $tag = $match[0];
        if (preg_match('~(?:name|property)="(?:description|og:description|twitter:description)"~', $tag)) {
            return preg_replace('~content="[^"]*"~', 'content="' . $description . '"', $tag);
        }
        if (preg_match('~(?:name|property)="(?:og:title|twitter:title)"~', $tag)) {
            return preg_replace('~content="[^"]*"~', 'content="' . $title . '"', $tag);
        }
        return $tag;
    }, $html);
    $html = preg_replace('~(<h1\b[^>]*>).*?(</h1>)~s', '$1' . ilmera_presentation_escape($entry['h1']) . '$2', $html, 1);
    $opening = '<p class="seo-opening" style="max-width:760px;margin:18px auto;line-height:1.8;">' . ilmera_presentation_escape($entry['opening']) . '</p>';
    $html = preg_replace('~</h1>~', '</h1>' . $opening, $html, 1);
    $html = preg_replace_callback('~<script type="application/ld\+json">(.*?)</script>~s', static function ($match) use ($entry) {
        $graph = json_decode($match[1], true);
        if (!is_array($graph)) return $match[0];
        return '<script type="application/ld+json">' . json_encode(ilmera_presentation_graph($graph, $entry), JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT) . '</script>';
    }, $html);
    return $html;
}

if (!defined('ILMERA_PRESENTATION_STARTED')) {
    define('ILMERA_PRESENTATION_STARTED', true);
    ob_start('ilmera_present_page');
}
