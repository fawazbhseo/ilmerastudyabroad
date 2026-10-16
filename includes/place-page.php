<?php
require_once __DIR__ . '/place-data.php';
require_once __DIR__ . '/breadcrumbs.php';
require_once __DIR__ . '/links.php';

$placeData = ilmera_place_load($place ?? null);
if (!$placeData) {
    http_response_code(404);
    header('X-Robots-Tag: noindex, follow');
    include dirname(__DIR__) . '/404.php';
    return;
}
$placeLive = ilmera_place_indexable($placeData);
if (!$placeLive) header('X-Robots-Tag: noindex, follow');
$placePath = ilmera_place_url($placeData);
$placeUrl = 'https://ilmerastudyabroad.com' . $placePath;
$placeHeading = ($placeData['type'] === 'district-hub' ? 'Study Abroad Consultancy for ' : 'Study Abroad Counselling for ') . $placeData['name'] . ' Students';
$placeHeading = $placeData['heading'] ?: $placeHeading;
$placeTitle = $placeData['page_title'] ?: $placeHeading . ' | ILMERA';
$placeDescription = $placeData['meta_description'] ?: ($placeData['intro_answer'] ?: $placeTitle);
$placeLinks = [];
foreach ($placeData['nearby'] as $slug) {
    $target = ilmera_place_load($slug);
    if ($target && ilmera_target_published(ilmera_place_url($target))) $placeLinks[] = $target;
}
$breadcrumbs = [['name' => 'Home', 'url' => '/']];
// Related guides are editorial links, not unsourced administrative claims.
$parents = [];
$placeParents = [];
$breadcrumbs[] = ['name' => $placeData['name'], 'url' => $placePath];
$placeLinks = array_values(array_filter($placeLinks, static function ($target) use ($parents) { return !in_array($target['slug'], $parents, true); }));
$placeGraph = [
    ['@type' => 'WebPage', '@id' => $placeUrl . '#webpage', 'url' => $placeUrl, 'name' => $placeTitle, 'description' => $placeDescription, 'inLanguage' => 'en-IN', 'breadcrumb' => ['@id' => $placeUrl . '#breadcrumb'], 'mainEntity' => ['@id' => $placeUrl . '#service']],
    ['@type' => 'Service', '@id' => $placeUrl . '#service', 'name' => $placeHeading . ' | ILMERA Study Abroad', 'serviceType' => 'Online study abroad counselling', 'url' => $placeUrl, 'areaServed' => ['@type' => 'Place', 'name' => $placeData['name']], 'provider' => ['@type' => 'Organization', '@id' => 'https://ilmerastudyabroad.com/#organization', 'name' => 'ILMERA Study Abroad', 'url' => 'https://ilmerastudyabroad.com/', 'telephone' => '+919019557427', 'description' => 'Online counselling only; no counselling premises.', 'areaServed' => ['@type' => 'Place', 'name' => $placeData['name']]]]
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
  <?php ilmera_breadcrumbs($breadcrumbs, $placePath); ?>
  <span class="article-tag"><?= ilmera_place_escape($placeData['name']) ?></span>
  <h1><?= ilmera_place_escape($placeHeading) ?></h1>
</section>
<section class="s-wrap article-body">
  <div class="container">
<?php if ($placeData['intro_answer'] !== ''): ?>
    <p><?= ilmera_place_escape($placeData['intro_answer']) ?></p>
<?php endif; ?>
<?php foreach ($placeData['sections'] as $section): ?>
    <section class="place-editorial-section">
      <h2><?= ilmera_place_escape($section['heading']) ?></h2>
<?php foreach ($section['paragraphs'] as $paragraph): ?>
      <p><?= ilmera_place_escape($paragraph) ?></p>
<?php endforeach; ?>
    </section>
<?php endforeach; ?>
<?php foreach (['local_institutions' => 'Local institutions', 'transcript_and_moi_steps' => 'Transcripts and Medium-of-Instruction letters', 'local_loan_options' => 'Local education-loan options', 'local_notes' => 'Local planning notes'] as $field => $heading): ?>
<?php if ($placeData[$field]): ?>
    <section>
      <h2><?= ilmera_place_escape($heading) ?></h2>
<?php foreach ($placeData[$field] as $text): ?>
      <p><?= ilmera_place_inline($text, $placeLive) ?></p>
<?php endforeach; ?>
    </section>
<?php endif; ?>
<?php endforeach; ?>
<?php if ($placeData['visa_appointment_route'] !== ''): ?>
    <section>
      <h2>Visa appointment planning</h2>
      <p><?= ilmera_place_inline($placeData['visa_appointment_route'], $placeLive) ?></p>
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
      <p>Contact ILMERA online by phone, WhatsApp or video call.</p>
      <p><a href="/contact" style="color:var(--gold);">Discuss this plan</a></p>
    </section>
<?php if ($placeParents): ?>
    <section>
      <h2>Parent location guides</h2>
      <ul>
<?php foreach ($placeParents as $parent): ?>
        <li><?= ilmera_place_link($parent['slug'], ['style' => 'color:var(--gold);']) ?></li>
<?php endforeach; ?>
      </ul>
    </section>
<?php endif; ?>
<?php if ($placeLinks): ?>
    <section>
      <h2><?= $placeData['slug'] === 'kodagu' ? 'Kodagu place guides' : 'Related place guides' ?></h2>
      <ul>
<?php foreach ($placeLinks as $target): ?>
        <li><?= ilmera_place_link($target['slug'], ['style' => 'color:var(--gold);']) ?></li>
<?php endforeach; ?>
      </ul>
    </section>
<?php endif; ?>
    <p><?= ilmera_link('/services', 'Explore study abroad services', ['style' => 'color:var(--gold);']) ?></p>
    <?php if ($placeLive && !$placeLinks && !$placeParents) ilmera_discovery_links(ilmera_indexable_locations(), 'Other location guides', $placePath); ?>
    <?= ilmera_place_destination_links($placeData) ?>
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

});
</script>
</body>
</html>
