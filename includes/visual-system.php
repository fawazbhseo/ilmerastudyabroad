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
    preg_match('~<link[^>]+rel="canonical"[^>]+href="https://ilmerastudyabroad.com([^"]*)"~', $html, $match);
    $path = $match[1] ?? parse_url($_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH);
    if (in_array($path, ['/', '/services', '/about', '/contact'], true)) return $html;
    $kind = ilmera_visual_template($path);
    if (!$kind || !in_array($kind, ILMERA_VISUAL_TEMPLATE_GROUPS, true)) return $html;
    $html = preg_replace('~<body>~', '<body class="p25 p25-' . $kind . '">', $html, 1);
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
    $css = file_get_contents(dirname(__DIR__) . '/assets/css/visual-system.css');
    // Self-hosted exact Latin reference weights; only first-frame faces preload.
    $fontPreload = '<link rel="preload" href="/assets/fonts/outfit-reference-300.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/assets/fonts/cormorant-garamond-reference-700.woff2" as="font" type="font/woff2" crossorigin>';
    $fontGate = <<<'HTML'
<script>(function(){if(!document.fonts)return;var root=document.documentElement,timer;function show(){root.classList.remove('p25-font-pending');clearTimeout(timer);}root.classList.add('p25-font-pending');timer=setTimeout(show,3000);Promise.all([document.fonts.load('300 16px Outfit'),document.fonts.load('700 48px "Cormorant Garamond"')]).then(function(){return document.fonts.ready;}).then(show,show);})();</script>
HTML;
    return str_replace('</head>', $fontPreload.'<style id="ilmera-visual-system">'.$css.'</style>'.$fontGate.'</head>', $html);
}

/** Classify actual existing templates, never publication status or SEO data. */
function ilmera_visual_template($path)
{
    if (strpos($path ?? '', '/study-in-') === 0) return 'destination';
    if (strpos($path ?? '', '/study-abroad-') === 0) return 'place';
    if ($path === '/blog/') return 'blog';
    if (strpos($path ?? '', '/blog/') === 0) return 'article';
    if (in_array($path, ['/privacy-policy', '/terms'], true)) return 'legal';
    if (in_array($path, ['/all-pages', '/404'], true)) return 'utility';
    return null;
}

/** Held/error pages get only this pure visual buffer, not SEO presentation. */
function ilmera_visual_start()
{
    if (!defined('ILMERA_PRESENTATION_STARTED') && !defined('ILMERA_VISUAL_BUFFER_STARTED')) {
        define('ILMERA_VISUAL_BUFFER_STARTED', true);
        ob_start(static function($html) { return ilmera_visual_present(ilmera_visual_scene_policy($html)); });
    }
}
