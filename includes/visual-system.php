<?php
require_once __DIR__ . '/visual-config.php';
/** Pure visual overlay: never change content, links, schema or publication data. */
function ilmera_visual_present($html)
{
    // OFF is intentionally sitewide, including the otherwise immutable references.
    // The default ON path emits no reference changes at all.
    if (!ILMERA_SCENES_ENABLED) {
        $html = preg_replace('~<script\b[^>]*src="https://cdnjs\.cloudflare\.com/ajax/libs/three\.js/[^"]*"[^>]*></script>~', '', $html);
        $off = '#space-canvas,#vignette,#nebula-t,#nebula-b,#gold-shimmer,#gold-glow-css,#grain,#float-layer{display:none!important;} #hero,.mini-hero,.article-hero,.blog-hero{background:#04060f!important;}';
        $html = str_replace('</head>', '<style id="ilmera-scenes-off">'.$off.'</style></head>', $html);
    }
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
    if (ILMERA_SCENES_ENABLED) {
        // Canvas is decorative and not an LCP image candidate. Absolute sizing
        // keeps content geometry independent of decoding, including JS-off.
        $html = preg_replace('~(<section class="(?:article-hero|blog-hero)"[^>]*>)~', '$1<canvas class="p25-hero-scene" aria-hidden="true" role="presentation"></canvas>', $html, 1);
        $html = str_replace('</head>', '<script src="/assets/js/hero-still.js" defer></script></head>', $html);
    }
    return str_replace('</head>', '<style id="ilmera-visual-system">' . file_get_contents(dirname(__DIR__) . '/assets/css/visual-system.css') . '</style></head>', $html);
}
