<?php
/* Shared place renderer. Content comes from a reviewed place data array. */
if (!function_exists('ilmera_place_text')) {
    function ilmera_place_text($value)
    {
        if (!is_string($value)) return '';
        $text = trim(html_entity_decode(strip_tags($value), ENT_QUOTES | ENT_HTML5, 'UTF-8'));
        if (preg_match('/\[\s*(?:VERIFY|OWNER|TODO|TBD|PLACEHOLDER|CONFIRM|INSERT|ADD|FILL|PENDING|UNCONFIRMED)\b|\b(?:TODO|TBD|TBC|PLACEHOLDER)\b/iu', $text)) return '';
        return $text;
    }

    function ilmera_place_strings($value)
    {
        if (!is_array($value)) return [];
        $items = [];
        foreach ($value as $item) {
            $text = ilmera_place_text($item);
            if ($text !== '') $items[] = $text;
        }
        return $items;
    }

    function ilmera_place_normalize($data, $slug)
    {
        if (!is_array($data)) return null;
        foreach (['slug', 'name', 'type', 'district', 'status'] as $key) {
            if (!isset($data[$key]) || !is_string($data[$key])) return null;
        }
        if ($data['slug'] !== $slug || !preg_match('/^[a-z0-9]+(?:-[a-z0-9]+)*$/D', $slug)) return null;
        if (!in_array($data['type'], ['district-hub', 'town', 'city'], true)) return null;
        if (!in_array($data['status'], ['draft', 'published'], true)) return null;
        $result = array_intersect_key($data, array_flip(['slug', 'name', 'type', 'district', 'status']));
        $result['name'] = ilmera_place_text($data['name']);
        $result['district'] = ilmera_place_text($data['district']);
        if ($result['name'] === '') return null;
        $result['intro_answer'] = ilmera_place_text($data['intro_answer'] ?? '');
        $words = preg_match_all('/\S+/u', $result['intro_answer']);
        if ($words < 40 || $words > 60) $result['intro_answer'] = '';
        foreach (['local_institutions', 'transcript_and_moi_steps', 'local_loan_options', 'local_notes'] as $key) {
            $result[$key] = ilmera_place_strings($data[$key] ?? []);
        }
        $result['visa_appointment_route'] = ilmera_place_text($data['visa_appointment_route'] ?? '');
        $result['faqs'] = [];
        foreach (is_array($data['faqs'] ?? null) ? $data['faqs'] : [] as $faq) {
            if (!is_array($faq)) continue;
            $question = ilmera_place_text($faq['question'] ?? '');
            $answer = ilmera_place_text($faq['answer'] ?? '');
            if ($question !== '' && $answer !== '') $result['faqs'][] = ['question' => $question, 'answer' => $answer];
        }
        $result['nearby'] = [];
        foreach (is_array($data['nearby'] ?? null) ? $data['nearby'] : [] as $nearby) {
            if (is_string($nearby) && $nearby !== $slug && preg_match('/^[a-z0-9]+(?:-[a-z0-9]+)*$/D', $nearby)) {
                $result['nearby'][] = $nearby;
            }
        }
        $result['nearby'] = array_values(array_unique($result['nearby']));
        return $result;
    }

    function ilmera_place_load($slug)
    {
        static $cache = [];
        if (!is_string($slug) || !preg_match('/^[a-z0-9]+(?:-[a-z0-9]+)*$/D', $slug)) return null;
        if (array_key_exists($slug, $cache)) return $cache[$slug];
        $path = dirname(__DIR__) . '/places/' . $slug . '.php';
        if (!is_file($path)) return $cache[$slug] = null;
        $data = (static function ($file) { return include $file; })($path);
        return $cache[$slug] = ilmera_place_normalize($data, $slug);
    }

    function ilmera_place_fact_count($data)
    {
        $count = 0;
        foreach (['intro_answer', 'local_institutions', 'transcript_and_moi_steps', 'local_loan_options', 'visa_appointment_route', 'local_notes', 'faqs'] as $key) {
            if (!empty($data[$key])) $count++;
        }
        return $count;
    }

    function ilmera_place_indexable($data)
    {
        return is_array($data) && $data['status'] === 'published' && ilmera_place_fact_count($data) >= 5;
    }

    function ilmera_place_url($data)
    {
        $prefix = $data['type'] === 'district-hub' && in_array($data['slug'], ['karnataka', 'kodagu'], true)
            ? '/study-abroad-consultants-in-' : '/study-abroad-counselling-';
        return $prefix . $data['slug'];
    }

    function ilmera_place_escape($text)
    {
        return htmlspecialchars($text, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
    }

    function ilmera_place_inline($text)
    {
        $escaped = ilmera_place_escape($text);
        return preg_replace_callback('/\[([^\[\]]+)\]\((\/[^\s()]*)\)/u', static function ($match) {
            $path = html_entity_decode($match[2], ENT_QUOTES | ENT_HTML5, 'UTF-8');
            $parts = parse_url($path);
            if ($parts === false || isset($parts['host']) || isset($parts['scheme']) || strpos($path, '//') === 0 || strpos($path, '\\') !== false) return $match[1];
            $target = null;
            if (preg_match('#^/study-abroad-(?:counselling|consultants-in)-([a-z0-9-]+)(?:\.php)?/?$#i', rawurldecode($parts['path'] ?? ''), $slugMatch)) {
                $target = ilmera_place_load(strtolower($slugMatch[1]));
                if (!$target || (!empty($GLOBALS['ilmera_place_live']) && !ilmera_place_indexable($target))) return $match[1];
            }
            return '<a href="' . $match[2] . '" style="color:var(--gold);">' . $match[1] . '</a>';
        }, $escaped);
    }
}

$placeData = ilmera_place_load($place ?? null);
if (!$placeData) {
    http_response_code(404);
    header('X-Robots-Tag: noindex, follow');
    include dirname(__DIR__) . '/404.php';
    return;
}
$placeLive = ilmera_place_indexable($placeData);
$GLOBALS['ilmera_place_live'] = $placeLive;
if (!$placeLive) header('X-Robots-Tag: noindex, follow');
$placePath = ilmera_place_url($placeData);
$placeUrl = 'https://ilmerastudyabroad.com' . $placePath;
$placeHeading = ($placeData['type'] === 'district-hub' ? 'Study Abroad Consultancy for ' : 'Study Abroad Counselling for ') . $placeData['name'] . ' Students';
$placeTitle = $placeHeading . ' | ILMERA';
$placeDescription = $placeData['intro_answer'] !== '' ? $placeData['intro_answer'] : $placeTitle;
$placeLinks = [];
foreach ($placeData['nearby'] as $slug) {
    $target = ilmera_place_load($slug);
    if ($target && (!$placeLive || ilmera_place_indexable($target))) $placeLinks[] = $target;
}
$breadcrumbs = [['name' => 'Home', 'url' => '/']];
$parents = $placeData['slug'] === 'karnataka' ? [] : ['karnataka'];
if ($placeData['type'] === 'town' && $placeData['district'] === 'Kodagu') $parents[] = 'kodagu';
foreach ($parents as $slug) {
    $parent = ilmera_place_load($slug);
    if ($parent && (!$placeLive || ilmera_place_indexable($parent))) $breadcrumbs[] = ['name' => $parent['name'], 'url' => ilmera_place_url($parent)];
}
$breadcrumbs[] = ['name' => $placeData['name'], 'url' => $placePath];
$breadcrumbItems = [];
foreach ($breadcrumbs as $position => $crumb) {
    $breadcrumbItems[] = ['@type' => 'ListItem', 'position' => $position + 1, 'name' => $crumb['name'], 'item' => 'https://ilmerastudyabroad.com' . $crumb['url']];
}
$placeGraph = [
    ['@type' => 'WebPage', '@id' => $placeUrl . '#webpage', 'url' => $placeUrl, 'name' => $placeTitle, 'description' => $placeDescription, 'inLanguage' => 'en-IN', 'breadcrumb' => ['@id' => $placeUrl . '#breadcrumb'], 'mainEntity' => ['@id' => $placeUrl . '#service']],
    ['@type' => 'BreadcrumbList', '@id' => $placeUrl . '#breadcrumb', 'itemListElement' => $breadcrumbItems],
    ['@type' => 'Service', '@id' => $placeUrl . '#service', 'name' => $placeHeading . ' | ILMERA Study Abroad', 'serviceType' => 'Study abroad counselling', 'url' => $placeUrl, 'areaServed' => ['@type' => 'AdministrativeArea', 'name' => 'Karnataka, India']]
];
if ($placeData['faqs']) {
    $questions = [];
    foreach ($placeData['faqs'] as $faq) $questions[] = ['@type' => 'Question', 'name' => $faq['question'], 'acceptedAnswer' => ['@type' => 'Answer', 'text' => $faq['answer']]];
    $placeGraph[] = ['@type' => 'FAQPage', '@id' => $placeUrl . '#faq', 'isPartOf' => ['@id' => $placeUrl . '#webpage'], 'mainEntity' => $questions];
}
$placeJson = json_encode(['@context' => 'https://schema.org', '@graph' => $placeGraph], JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_INVALID_UTF8_SUBSTITUTE);
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
<title><?= ilmera_place_escape($placeTitle) ?></title>
<meta name="description" content="<?= ilmera_place_escape($placeDescription) ?>"/>
<meta name="robots" content="<?= $placeLive ? 'index, follow' : 'noindex, follow' ?>"><!-- Release checks: flagged-items-for-verification.md -->
<meta name="language" content="English"/>
<meta name="geo.region" content="IN-KA"/>
<meta name="geo.placename" content="Coorg, Karnataka, India"/>
<meta name="theme-color" content="#04060f"/>
<link rel="canonical" href="<?= ilmera_place_escape($placeUrl) ?>"/>
<link rel="icon" type="image/png" href="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<link rel="shortcut icon" type="image/png" href="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<link rel="apple-touch-icon" href="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<meta property="og:type" content="website"/>
<meta property="og:site_name" content="ILMERA Study Abroad"/>
<meta property="og:title" content="<?= ilmera_place_escape($placeTitle) ?>"/>
<meta property="og:description" content="<?= ilmera_place_escape($placeDescription) ?>"/>
<meta property="og:url" content="<?= ilmera_place_escape($placeUrl) ?>"/>
<meta property="og:image" content="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<meta property="og:locale" content="en_IN"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="<?= ilmera_place_escape($placeTitle) ?>"/>
<meta name="twitter:description" content="<?= ilmera_place_escape($placeDescription) ?>"/>
<meta name="twitter:image" content="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&amp;family=Outfit:wght@100;300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<script type="application/ld+json"><?= $placeJson ?></script>
<style>
:root{
  --void:#04060f;--deep-navy:#0a1628;--navy:#1A2E5A;
  --cool-white:#F0F4FF;--white:#FFFFFF;--grey-light:#E8EDF5;
  --grey-mid:#8A98B8;--grey-dark:#4A5568;--silver:#C8D3E8;
  --gold:#C9A84C;--gold-glow:rgba(201,168,76,0.28);
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%;}
body{font-family:'Outfit',sans-serif;font-weight:300;color:var(--white);background:var(--void);overflow-x:hidden;}
.s-wrap{position:relative;z-index:10;}
.container{max-width:800px;margin:0 auto;padding:0 60px;}
@media(max-width:768px){.container{padding:0 24px;}}

.article-hero{position:relative;padding:150px 24px 50px;text-align:center;background:radial-gradient(ellipse at 50% 0%,rgba(201,168,76,0.08),transparent 60%);}
.article-hero .breadcrumb{font-size:13px;font-weight:300;color:var(--grey-mid);margin-bottom:20px;max-width:800px;margin-left:auto;margin-right:auto;}
.article-hero .breadcrumb a{color:var(--grey-mid);text-decoration:none;transition:color .3s;}
.article-hero .breadcrumb a:hover{color:var(--gold);}
.article-tag{display:inline-block;font-size:11px;font-weight:500;text-transform:uppercase;letter-spacing:.1em;color:var(--gold);border:1px solid rgba(201,168,76,0.4);padding:5px 12px;border-radius:20px;margin-bottom:20px;}
.article-hero h1{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:44px;color:var(--white);line-height:1.2;max-width:820px;margin:0 auto;}
.article-byline{font-size:13px;color:var(--grey-mid);margin-top:22px;}
.article-byline .name{color:var(--silver);}
@media(max-width:768px){.article-hero h1{font-size:30px;}.article-hero{padding:110px 24px 40px;}}

.article-body{background:rgba(10,22,40,0.6);padding:20px 0 100px;}
.article-body .container{padding:0 60px;}
@media(max-width:768px){.article-body .container{padding:0 24px;}}
.article-body h2{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:28px;color:var(--white);margin:40px 0 16px;}
.article-body p{font-size:16px;font-weight:300;color:var(--grey-light);line-height:1.85;margin-bottom:20px;}
.article-body ul{margin:0 0 20px 20px;}
.article-body li{font-size:16px;font-weight:300;color:var(--grey-light);line-height:1.85;margin-bottom:10px;}
.article-body strong{color:var(--white);font-weight:500;}

.author-card{display:flex;align-items:center;gap:16px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:14px;padding:22px 24px;margin-top:48px;}
.author-card img{width:56px;height:56px;border-radius:50%;object-fit:cover;flex-shrink:0;}
.author-card .name{color:var(--white);font-size:15px;font-weight:500;}
.author-card .role{color:var(--gold);font-size:12px;text-transform:uppercase;letter-spacing:.06em;margin-top:2px;}

.article-cta{background:rgba(4,6,15,0.97);padding:80px 0;text-align:center;}
.article-cta h2{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:32px;color:var(--white);margin-bottom:16px;}
.article-cta p{font-size:15px;color:var(--grey-mid);margin-bottom:28px;max-width:520px;margin-left:auto;margin-right:auto;}
.btn-gold{font-size:13px;font-weight:500;text-transform:uppercase;letter-spacing:.1em;background:var(--gold);color:var(--void);border:none;padding:16px 36px;border-radius:3px;cursor:pointer;transition:background .3s,box-shadow .3s,transform .2s;text-decoration:none;display:inline-block;}
.btn-gold:hover{background:#d4b05a;box-shadow:0 0 40px var(--gold-glow);transform:translateY(-2px);}
.back-link{display:inline-block;margin-top:40px;color:var(--grey-mid);font-size:13px;text-decoration:none;transition:color .3s;}
.back-link:hover{color:var(--gold);}

.il-faq{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.10);border-radius:12px;margin-bottom:14px;overflow:hidden;transition:border-color .3s;}
.il-faq[open]{border-color:rgba(201,168,76,0.4);}
.il-faq summary{list-style:none;cursor:pointer;padding:22px 26px;font-family:'Outfit',sans-serif;font-size:17px;font-weight:500;color:var(--white);display:flex;justify-content:space-between;align-items:center;gap:16px;}
.il-faq summary::-webkit-details-marker{display:none;}
.il-faq summary::after{content:'+';font-size:24px;font-weight:300;color:var(--gold);transition:transform .3s;flex-shrink:0;}
.il-faq[open] summary::after{transform:rotate(45deg);}
.il-faq summary:hover{color:var(--gold);}
.il-faq > div{padding:0 26px 24px;}
.il-faq > div p{font-size:15px;font-weight:300;color:var(--grey-mid);line-height:1.75;margin:0;}
.article-body h3{font-size:19px;font-weight:500;color:var(--silver);margin:28px 0 10px;}
</style>
</head>
<body>
<?php include __DIR__ . '/header.php'; ?>
<main>
<section class="article-hero">
  <nav class="breadcrumb" aria-label="Breadcrumb"><?php foreach ($breadcrumbs as $position => $crumb): ?><?php if ($position): ?> &nbsp;/&nbsp; <?php endif; ?><?php if ($position < count($breadcrumbs) - 1): ?><a href="<?= ilmera_place_escape($crumb['url']) ?>"><?= ilmera_place_escape($crumb['name']) ?></a><?php else: ?><?= ilmera_place_escape($crumb['name']) ?><?php endif; ?><?php endforeach; ?></nav>
  <span class="article-tag"><?= ilmera_place_escape($placeData['name']) ?></span>
  <h1><?= ilmera_place_escape($placeHeading) ?></h1>
</section>
<section class="s-wrap article-body">
  <div class="container">
<?php if ($placeData['intro_answer'] !== ''): ?>
    <p><?= ilmera_place_escape($placeData['intro_answer']) ?></p>
<?php endif; ?>
<?php foreach (['local_institutions' => 'Local institutions', 'transcript_and_moi_steps' => 'Transcripts and Medium-of-Instruction letters', 'local_loan_options' => 'Local education-loan options', 'local_notes' => 'Local planning notes'] as $field => $heading): ?>
<?php if ($placeData[$field]): ?>
    <section>
      <h2><?= ilmera_place_escape($heading) ?></h2>
<?php foreach ($placeData[$field] as $text): ?>
      <p><?= ilmera_place_inline($text) ?></p>
<?php endforeach; ?>
    </section>
<?php endif; ?>
<?php endforeach; ?>
<?php if ($placeData['visa_appointment_route'] !== ''): ?>
    <section>
      <h2>Visa appointment planning</h2>
      <p><?= ilmera_place_inline($placeData['visa_appointment_route']) ?></p>
    </section>
<?php endif; ?>
<?php if ($placeData['faqs']): ?>
    <section>
      <h2>Frequently asked questions</h2>
<?php foreach ($placeData['faqs'] as $faq): ?>
      <details class="il-faq"><summary><?= ilmera_place_escape($faq['question']) ?></summary><div><p><?= ilmera_place_escape($faq['answer']) ?></p></div></details>
<?php endforeach; ?>
    </section>
<?php endif; ?>
    <section aria-labelledby="place-counselling-process" class="author-card" style="display:block;">
      <h2 id="place-counselling-process">How ILMERA counselling works</h2>
      <p>ILMERA Study Abroad is based in Coorg, Kodagu, and has no physical office. Counselling is by phone, WhatsApp and video call. The initial consultation is free; academic and financial documents are shared digitally for review. University admissions, scholarships and visas are not guaranteed.</p>
      <p>Counsellors review marks, backlogs, budget and course goals, discuss a university shortlist, and guide applications, visa documentation and pre-departure preparation.</p>
      <p>Visa-document guidance is provided through the same contact channels. Any visa appointment is the student's own appointment at the relevant consulate or VFS centre, not a meeting with ILMERA.</p>
      <p><a href="/contact" style="color:var(--gold);">Arrange a consultation</a> or read about <a href="/blog/study-abroad-counselling-from-coorg" style="color:var(--gold);">counselling from Coorg</a>.</p>
    </section>
<?php if ($placeLinks): ?>
    <section>
      <h2><?= $placeData['slug'] === 'kodagu' ? 'Kodagu place guides' : 'Related place guides' ?></h2>
      <ul>
<?php foreach ($placeLinks as $target): ?>
        <li><a href="<?= ilmera_place_escape(ilmera_place_url($target)) ?>" style="color:var(--gold);"><?= ilmera_place_escape($target['name']) ?></a></li>
<?php endforeach; ?>
      </ul>
    </section>
<?php endif; ?>
  </div>
</section>
</main>
<?php include __DIR__ . '/footer.php'; ?>
<script>
window.addEventListener('DOMContentLoaded',function(){
  window.addEventListener('scroll',function(){
    var nav=document.getElementById('il-nav');
    if(nav)nav.classList.toggle('scrolled',window.scrollY>60);
  },{passive:true});
  var hbg=document.getElementById('hbg'),mnav=document.getElementById('mob-nav');
  if(hbg&&mnav){
    hbg.addEventListener('click',function(){
      var o=hbg.classList.contains('open');
      hbg.classList.toggle('open',!o);mnav.classList.toggle('open',!o);
      document.body.style.overflow=o?'':'hidden';
      hbg.setAttribute('aria-expanded',String(!o));
    });
    mnav.querySelectorAll('a').forEach(function(link){
      link.addEventListener('click',function(){
        hbg.classList.remove('open');mnav.classList.remove('open');
        document.body.style.overflow='';hbg.setAttribute('aria-expanded','false');
      });
    });
  }
});
</script>
</body>
</html>
