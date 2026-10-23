<?php
require_once __DIR__ . '/visual-config.php';
/** Pure visual overlay: never change content, links, schema or publication data. */
function ilmera_visual_present($html)
{
    if (!ILMERA_VISUAL_PILOTS_ENABLED) return $html;
    if (!preg_match('~<link[^>]+rel="canonical"[^>]+href="https://ilmerastudyabroad.com([^"]*)"~', $html, $match)) return $html;
    $pilots = [
        '/study-in-germany' => 'destination',
        '/study-abroad-counselling-mysuru' => 'place',
        '/blog/how-to-choose-study-abroad-consultant-karnataka' => 'article',
        '/blog/' => 'blog'
    ];
    if (!isset($pilots[$match[1]])) return $html;
    $html = preg_replace('~<body>~', '<body class="p25 p25-' . $pilots[$match[1]] . '">', $html, 1);
    // Inline shared CSS: no extra render-blocking request. Existing font stylesheet
    // is replaced with local same-family font faces, not another blocking stylesheet.
    $html = preg_replace('~<link\b[^>]*href="https://fonts\.googleapis\.com/[^>]*>~', '', $html);
    return str_replace('</head>', '<style id="ilmera-visual-system">' . file_get_contents(dirname(__DIR__) . '/assets/css/visual-system.css') . '</style></head>', $html);
}
