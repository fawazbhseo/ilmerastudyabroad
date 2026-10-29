<?php
require_once __DIR__ . '/visual-config.php';
/** Pure visual overlay: never change content, links, schema or publication data. */
function ilmera_visual_scene_policy($html)
{
    // OFF is intentionally sitewide, including the otherwise immutable references.
    // The default ON path emits no reference changes at all.
    if (!ILMERA_SCENES_ENABLED && strpos($html, 'id="ilmera-scenes-off"') === false) {
        $html = preg_replace('~<script\b[^>]*src="https://cdnjs\.cloudflare\.com/ajax/libs/three\.js/[^"]*"[^>]*></script>~', '', $html);
        $off = '#space-canvas,#vignette,#nebula-t,#nebula-b,#gold-shimmer,#gold-glow-css,#grain,#float-layer{display:none!important;} #hero,.mini-hero,.article-hero,.blog-hero,.legal-hero,.directory-hero,.err-wrap{background:#04060f!important;}';
        $html = str_replace('</head>', '<style id="ilmera-scenes-off">'.$off.'</style></head>', $html);
    }
    return $html;
}

function ilmera_visual_present($html)
{
    if (strpos($html, 'id="ilmera-visual-system"') !== false) return $html;
    preg_match('~<link[^>]+rel="canonical"[^>]+href="https://ilmerastudyabroad.com([^"]*)"~', $html, $match);
    $path = $match[1] ?? parse_url($_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH);
    if (defined('ILMERA_VISUAL_REQUEST_TEMPLATE') && ILMERA_VISUAL_REQUEST_TEMPLATE === 'error') $path = '/404';
    if (in_array($path, ['/', '/services', '/about', '/contact'], true)) return $html;
    $kind = ilmera_visual_template($path);
    if (!$kind || !in_array($kind, ILMERA_VISUAL_TEMPLATE_GROUPS, true)) return $html;
    $html = preg_replace('~<body>~', '<body class="p25 p25-' . $kind . '">', $html, 1);
    // Match the existing reference header's first-image loading attribute.
    // This changes fetch timing only, never image content, dimensions or URL.
    $html = preg_replace_callback('~(<nav id="il-nav">.*?)(<img\b[^>]*>)(.*?</nav>)~s', static function($p) {
        $image = $p[2];
        if (!preg_match('~\bloading=~', $image)) $image = preg_replace('~/?>(\s*)$~', ' loading="eager"/>$1', $image);
        return $p[1].$image.$p[3];
    }, $html, 1);
    // Inline shared CSS: no extra render-blocking request. Existing font stylesheet
    // is replaced with local same-family font faces, not another blocking stylesheet.
    $html = preg_replace('~<link\b[^>]*href="https://fonts\.googleapis\.com/[^>]*>~', '', $html);
    $html = preg_replace('~<link\b(?=[^>]*rel="preconnect")(?=[^>]*href="https://fonts\.(?:googleapis|gstatic)\.com")[^>]*>~', '', $html);
    // Keep the entire text/headings sequence, but place long introductions in
    // the first LIGHT reading section instead of extending a dark article hero.
    $intro = '';
    $canMoveIntro = preg_match('~<(?:section|div) class="(?:s-wrap )?(?:article-body|blog-sec|legal-sec|directory-content)"[^>]*>\s*<div class="container">~', $html);
    if ($canMoveIntro) $html = preg_replace_callback('~(<section class="(?:article-hero|blog-hero|legal-hero|directory-hero)"[^>]*>)(.*?)(</section>)~s', static function ($parts) use (&$intro) {
        $end = strpos($parts[2], '</h1>');
        if ($end === false) return $parts[0];
        $end += 5;
        $intro = substr($parts[2], $end);
        return $parts[1] . substr($parts[2], 0, $end) . $parts[3];
    }, $html, 1);
    if ($intro !== '') {
        $html = preg_replace_callback('~(<(?:section|div) class="(?:s-wrap )?(?:article-body|blog-sec|legal-sec|directory-content)"[^>]*>\s*<div class="container">)~', static function ($parts) use ($intro) { return $parts[1] . $intro; }, $html, 1);
    }
    if ($path === '/404') {
        // Preserve the abbreviated footer contents and every existing link.
        $html = preg_replace_callback('~(<section class="err-wrap">)(.*?)(</section>)~s', static function($p) {
            $end = strpos($p[2], '</h1>');
            if ($end === false) return $p[0];
            $end += 5;
            $tail = preg_replace('~</div>\s*$~', '', substr($p[2], $end));
            return $p[1].substr($p[2],0,$end).'</div>'.$p[3].'<section class="s-wrap article-body"><div class="container">'.$tail.'</div></section>';
        }, $html, 1);
        $html = preg_replace('~<footer style="[^"]*">~', '<footer id="il-footer">', $html, 1);
        $html = preg_replace('~(<footer id="il-footer">\s*)<div class="container" style="[^"]*">~', '$1<div class="container"><div class="ft-bottom">', $html, 1);
        $html = str_replace('<div style="display:flex;gap:20px;">', '<div class="ft-legal" style="display:flex;gap:20px;">', $html);
        $html = str_replace('<span style="font-size:12px;font-weight:300;color:var(--grey-mid);">', '<span class="ft-copy" style="font-size:12px;font-weight:300;color:var(--grey-mid);">', $html);
        $html = str_replace('</footer>', '</div></footer>', $html);
    }
    $template = $path === '/all-pages' ? 'directory' : ($path === '/404' ? 'error' : $kind);
    $css = file_get_contents(dirname(__DIR__) . '/assets/css/visual-system.css');
    // Self-hosted exact Latin reference weights; only first-frame faces preload.
    $fontPreload = '<link rel="preload" href="/assets/fonts/outfit-reference-300.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/assets/fonts/cormorant-garamond-reference-700.woff2" as="font" type="font/woff2" crossorigin>';
    if (in_array($template, ILMERA_VISUAL_INLINE_FONT_TEMPLATES, true)) {
        // Measured, per-template budget escape hatch only; never the default.
        $css = preg_replace("~@font-face\\{font-family:'(?:Outfit|Cormorant Garamond)';[^}]*\\}~", '', $css);
        foreach ([['Outfit','100 900','outfit-latin.woff2'],['Cormorant Garamond','300 700','cormorant-garamond-latin.woff2']] as $face) {
            $data = base64_encode(file_get_contents(dirname(__DIR__).'/assets/fonts/'.$face[2]));
            $css .= "@font-face{font-family:'{$face[0]}';font-style:normal;font-weight:{$face[1]};font-display:block;src:url('data:font/woff2;base64,{$data}') format('woff2');}";
        }
        $fontPreload = '';
    }
    if (in_array($template, ILMERA_VISUAL_PLAIN_HERO_TEMPLATES, true)) {
        $css .= "\nbody.p25 :is(.mini-hero,.article-hero,.blog-hero,.legal-hero,.directory-hero,.err-wrap){background:#04060f;}";
    }
    $heroStillTemplates = ['destination','place','article','blog'];
    if (in_array($template, $heroStillTemplates, true)) {
        $selectors = 'body.p25.p25-destination .article-hero,body.p25.p25-place .article-hero,body.p25.p25-article .article-hero,body.p25.p25-blog .blog-hero';
        $css .= "\n{$selectors}{background-color:#04060f;background-image:linear-gradient(180deg,rgba(4,6,15,.44),rgba(4,6,15,.68)),radial-gradient(ellipse at 50% 0%,rgba(201,168,76,.08),transparent 60%);background-size:cover,cover;background-position:center,center;background-repeat:no-repeat,no-repeat;}\n";
        $plainHero = !ILMERA_SCENES_ENABLED || in_array($template, ILMERA_VISUAL_PLAIN_HERO_TEMPLATES, true);
        if (!$plainHero) {
            $hero = '<canvas class="p32-hero-still" aria-hidden="true" role="presentation"></canvas>';
            $html = preg_replace_callback('~(<(?:section|div)\\b[^>]*class="[^"]*\\b(?:article-hero|blog-hero)\\b[^"]*"[^>]*>)~', static function($match) use ($hero) { return $match[1].$hero; }, $html, 1);
            $noscript = '<noscript><style>'.$selectors.'{background-image:linear-gradient(180deg,rgba(4,6,15,.44),rgba(4,6,15,.68)),url("/assets/images/hero-still-1440.webp");background-size:cover,cover;background-position:center,center;background-repeat:no-repeat,no-repeat;}@media(max-width:768px){'.$selectors.'{background-image:linear-gradient(180deg,rgba(4,6,15,.44),rgba(4,6,15,.68)),url("/assets/images/hero-still-640.webp");}}</style></noscript>';
            $html = str_replace('</body>', $noscript.'</body>', $html);
            $heroLoader = <<<'HTML'
<script>(function(){var canvas=document.querySelector('.p32-hero-still');if(!canvas)return;var reduced=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;if(reduced)canvas.style.transition='none';var connection=navigator.connection||navigator.mozConnection||navigator.webkitConnection;function slow(){if(!connection)return false;var type=String(connection.effectiveType||'').toLowerCase();return !!connection.saveData||/^(slow-2g|2g)$/.test(type)||(Number(connection.downlink)>0&&Number(connection.downlink)<1.1);}if(slow())return;var started=false;function load(){if(started)return;started=true;var image=new Image();image.decoding='async';image.onload=function(){var box=canvas.getBoundingClientRect(),ratio=Math.min(window.devicePixelRatio||1,2);if(!box.width||!box.height)return;canvas.width=Math.round(box.width*ratio);canvas.height=Math.round(box.height*ratio);var context=canvas.getContext('2d');if(!context)return;var scale=Math.max(canvas.width/image.naturalWidth,canvas.height/image.naturalHeight),drawWidth=image.naturalWidth*scale,drawHeight=image.naturalHeight*scale;context.drawImage(image,(canvas.width-drawWidth)/2,(canvas.height-drawHeight)/2,drawWidth,drawHeight);canvas.classList.add('is-loaded');};image.onerror=function(){canvas.classList.remove('is-loaded');};image.src=window.matchMedia('(max-width: 768px)').matches?'/assets/images/hero-still-640.webp':'/assets/images/hero-still-1440.webp';}function idleAfterLoad(){var done=false;var fallback=setTimeout(function(){if(!done){done=true;load();}},1500);if('requestIdleCallback' in window)requestIdleCallback(function(){if(!done){done=true;clearTimeout(fallback);load();}},{timeout:1500});}if(document.readyState==='complete')idleAfterLoad();else window.addEventListener('load',idleAfterLoad,{once:true});if(window.matchMedia){var motion=window.matchMedia('(prefers-reduced-motion: reduce)');if(motion.addEventListener)motion.addEventListener('change',function(event){if(event.matches)canvas.style.transition='none';});}})();</script>
HTML;
            $html = str_replace('</body>', $heroLoader.'</body>', $html);
        }
    }
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
function ilmera_visual_start($template = null)
{
    if ($template !== null && !defined('ILMERA_VISUAL_REQUEST_TEMPLATE')) define('ILMERA_VISUAL_REQUEST_TEMPLATE', $template);
    if (!defined('ILMERA_PRESENTATION_STARTED') && !defined('ILMERA_VISUAL_BUFFER_STARTED')) {
        define('ILMERA_VISUAL_BUFFER_STARTED', true);
        ob_start(static function($html) { return ilmera_visual_present(ilmera_visual_scene_policy($html)); });
    }
}
