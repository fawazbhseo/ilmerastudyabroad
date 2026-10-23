<?php
require_once __DIR__ . '/visual-config.php';
/** Pure visual overlay: never change content, links, schema or publication data. */
function ilmera_visual_scene_policy($html)
{
    // OFF is intentionally sitewide, including the otherwise immutable references.
    // The default ON path emits no reference changes at all.
    if (!ILMERA_SCENES_ENABLED) {
        $html = preg_replace('~<script\b[^>]*src="https://cdnjs\.cloudflare\.com/ajax/libs/three\.js/[^"]*"[^>]*></script>~', '', $html);
        $off = '#space-canvas,#vignette,#nebula-t,#nebula-b,#gold-shimmer,#gold-glow-css,#grain,#float-layer{display:none!important;} #hero,.mini-hero,.article-hero,.blog-hero{background:#04060f!important;}';
        $html = str_replace('</head>', '<style id="ilmera-scenes-off">'.$off.'</style></head>', $html);
    }
    return $html;
}

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
    // Keep the entire text/headings sequence, but place long introductions in
    // the first LIGHT reading section instead of extending a dark article hero.
    $intro = '';
    $canMoveIntro = preg_match('~<section class="s-wrap (?:article-body|blog-sec)"[^>]*>\s*<div class="container">~', $html);
    if ($canMoveIntro) $html = preg_replace_callback('~(<section class="(?:article-hero|blog-hero)"[^>]*>)(.*?)(</section>)~s', static function ($parts) use (&$intro) {
        $end = strpos($parts[2], '</h1>');
        if ($end === false) return $parts[0];
        $end += 5;
        $intro = substr($parts[2], $end);
        return $parts[1] . substr($parts[2], 0, $end) . $parts[3];
    }, $html, 1);
    if ($intro !== '') {
        $html = preg_replace_callback('~(<section class="s-wrap (?:article-body|blog-sec)"[^>]*>\s*<div class="container">)~', static function ($parts) use ($intro) { return $parts[1] . $intro; }, $html, 1);
    }
    if (ILMERA_SCENES_ENABLED && (ILMERA_PILOT_SCENE_TIERS[$pilots[$match[1]]] ?? 'plain') === 'still') {
        // Canvas is decorative and not an LCP image candidate. Absolute sizing
        // keeps content geometry independent of decoding, including JS-off.
        $html = preg_replace('~(<section class="(?:article-hero|blog-hero)"[^>]*>)~', '$1<canvas class="p25-hero-scene" aria-hidden="true" role="presentation"></canvas>', $html, 1);
        $html = str_replace('</head>', '<script src="/assets/js/hero-still.js" defer></script></head>', $html);
    }
    $css = file_get_contents(dirname(__DIR__) . '/assets/css/visual-system.css');
    // Self-hosted exact Latin reference weights; only first-frame faces preload.
    $fontPreload = '<link rel="preload" href="/assets/fonts/outfit-reference-300.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/assets/fonts/cormorant-garamond-reference-700.woff2" as="font" type="font/woff2" crossorigin>';
    $fontGate = <<<'HTML'
<script>(function(){if(!document.fonts)return;var root=document.documentElement,timer;function show(){root.classList.remove('p25-font-pending');clearTimeout(timer);}root.classList.add('p25-font-pending');timer=setTimeout(show,3000);Promise.all([document.fonts.load('300 16px Outfit'),document.fonts.load('700 48px "Cormorant Garamond"')]).then(function(){return document.fonts.ready;}).then(show,show);})();</script>
HTML;
    return str_replace('</head>', $fontPreload.'<style id="ilmera-visual-system">'.$css.'</style>'.$fontGate.'</head>', $html);
}
