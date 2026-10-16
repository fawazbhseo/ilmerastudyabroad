<?php
require_once __DIR__ . '/entity.php';
/** Reviewed presentation overlays. Publication data and its source gates stay intact. */
function ilmera_presentation_escape($text)
{
    return htmlspecialchars($text, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

function ilmera_presentation_graph($node, $entry)
{
    if (!is_array($node)) return $node;
    $type = $node['@type'] ?? '';
    if (($node['@id'] ?? '') === 'https://ilmerastudyabroad.com/#organization' && $type === 'Organization') return ['@id'=>'https://ilmerastudyabroad.com/#organization'];
    if (($node['@id'] ?? '') === 'https://ilmerastudyabroad.com/#jabir' && $type === 'Person') return ['@id'=>'https://ilmerastudyabroad.com/#jabir'];
    if (in_array($type, ['WebPage', 'Article', 'BlogPosting', 'Service'], true)) {
        $node['description'] = $entry['description'];
        if (in_array($type, ['WebPage','Article','BlogPosting'], true) && in_array($entry['kind'], ['destination','article'], true)) $node['dateModified'] = '2026-10-16';
        if (isset($node['name'])) $node['name'] = $entry['title'];
        if (isset($node['headline'])) $node['headline'] = $entry['h1'];
    }
    if ($type === 'FAQPage' && !empty($entry['answer_data']['extra_faqs'])) {
        foreach ($entry['answer_data']['extra_faqs'] as $faq) $node['mainEntity'][] = ['@type'=>'Question','name'=>$faq['question'],'acceptedAnswer'=>['@type'=>'Answer','text'=>$faq['answer']]];
    }
    foreach ($node as $key => $value) {
        if (is_array($value)) $node[$key] = ilmera_presentation_graph($value, $entry);
    }
    if (isset($node['@graph'])) $node['@graph'] = array_values(array_filter($node['@graph'], static function($g){return isset($g['@type']);}));
    return $node;
}

function ilmera_present_page($html)
{
    if (!preg_match('~<link[^>]+rel="canonical"[^>]+href="https://ilmerastudyabroad.com([^"]*)"~', $html, $match)) return $html;
    $path = $match[1] ?: '/';
    $map = json_decode(file_get_contents(dirname(__DIR__) . '/data/seo-map.json'), true);
    if (!isset($map[$path]) || preg_match('~<meta[^>]+name="robots"[^>]+content="[^"]*noindex~i', $html)) return $html;
    $entry = $map[$path];
    $answers = json_decode(file_get_contents(dirname(__DIR__) . '/data/answer-map.json'), true);
    if (isset($answers[$path])) $entry['answer_data'] = $answers[$path];
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
        $graph = ilmera_presentation_graph($graph, $entry);
        if (!isset($graph['@graph']) && !isset($graph['@type'])) return '';
        return '<script type="application/ld+json">' . json_encode($graph, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT) . '</script>';
    }, $html);
    if (isset($entry['answer_data'])) {
        $answer = $entry['answer_data'];
        $block = '<div class="direct-answer-block" style="max-width:760px;margin:24px auto;text-align:left;"><h2>' . ilmera_presentation_escape($answer['question']) . '</h2><p class="direct-answer">' . ilmera_presentation_escape($answer['answer']) . '</p></div>';
        $html = preg_replace('~(<p class="seo-opening"[^>]*>.*?</p>)~s', '$1' . $block, $html, 1);
        if ($answer['extra_faqs']) {
            $faqHtml = '<section class="s-wrap article-body"><div class="container"><h2>Further questions</h2>';
            $entities = [];
            foreach ($answer['extra_faqs'] as $faq) {
                $faqHtml .= '<details class="il-faq"><summary>' . ilmera_presentation_escape($faq['question']) . '</summary><div><p>' . ilmera_presentation_escape($faq['answer']) . '</p></div></details>';
                $entities[] = ['@type'=>'Question','name'=>$faq['question'],'acceptedAnswer'=>['@type'=>'Answer','text'=>$faq['answer']]];
            }
            $html = str_replace('</main>', $faqHtml . '</div></section></main>', $html);
            if (!preg_match('~"@type"\s*:\s*"FAQPage"~', $html)) {
                $json = json_encode(['@context'=>'https://schema.org','@type'=>'FAQPage','@id'=>'https://ilmerastudyabroad.com'.$path.'#faq','mainEntity'=>$entities], JSON_UNESCAPED_SLASHES|JSON_HEX_TAG|JSON_HEX_AMP|JSON_HEX_APOS|JSON_HEX_QUOT);
                $html = str_replace('</head>', '<script type="application/ld+json">'.$json.'</script></head>', $html);
            }
        }
    }
    $html = str_replace('</head>', ilmera_entity_markup() . '</head>', $html);
    if (in_array($path, ['/about','/contact','/study-abroad-consultants-in-karnataka'], true)) $html = str_replace('</main>', ilmera_entity_visible() . '</main>', $html);
    if (in_array($entry['kind'], ['destination','article'], true)) {
        $review = '<p class="last-reviewed">Last reviewed <time datetime="2026-10-16">16 October 2026</time></p>';
        $html = preg_replace('~(<div class="direct-answer-block"[^>]*>)~', '$1'.$review, $html, 1);
    }
    return $html;
}

if (!defined('ILMERA_PRESENTATION_STARTED')) {
    define('ILMERA_PRESENTATION_STARTED', true);
    ob_start('ilmera_present_page');
}
