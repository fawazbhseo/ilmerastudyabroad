<?php
require_once __DIR__ . '/destination-data.php';
require_once __DIR__ . '/breadcrumbs.php';
$destinationData = ilmera_destination_load($destination ?? null);
if (!$destinationData) {
    http_response_code(404);
    header('X-Robots-Tag: noindex, follow');
    include dirname(__DIR__) . '/404.php';
    return;
}
$destinationLive = ilmera_destination_indexable($destinationData);
if (!$destinationLive) header('X-Robots-Tag: noindex, follow');
$destinationPath = ilmera_destination_url($destinationData);
$destinationUrl = 'https://ilmerastudyabroad.com' . $destinationPath;
$destinationHeading = 'Study in ' . $destinationData['name'];
$destinationTitle = $destinationHeading . ' | ILMERA Study Abroad';
$destinationDescription = $destinationData['intro_answer'] ?: ($destinationData['ilmera_summary'] ?: $destinationTitle);
if ($destinationData['slug'] === 'gcc') $destinationDescription = $destinationData['scope_note'] . ' ' . $destinationData['review_notice'];
$destinationTrail = [['name' => 'Home', 'url' => '/'], ['name' => 'Services', 'url' => '/services'], ['name' => $destinationHeading, 'url' => $destinationPath]];
$destinationSources = ilmera_destination_sources($destinationData);
$destinationGraph = [
    ['@type' => 'WebPage', '@id' => $destinationUrl . '#webpage', 'url' => $destinationUrl, 'name' => $destinationTitle, 'description' => $destinationDescription, 'inLanguage' => 'en-IN', 'breadcrumb' => ['@id' => $destinationUrl . '#breadcrumb'], 'mainEntity' => ['@id' => $destinationUrl . '#service']],
    ['@type' => 'Service', '@id' => $destinationUrl . '#service', 'url' => $destinationUrl, 'name' => $destinationTitle, 'serviceType' => 'Study abroad counselling', 'provider' => ['@id' => 'https://ilmerastudyabroad.com/#organization']]
];
if ($destinationData['slug'] === 'gcc') {
    $destinationGraph[1]['description'] = $destinationDescription;
    $destinationGraph[1]['areaServed'] = array_map(static function ($country) { return ['@type' => 'Country', 'name' => $country]; }, ['UAE', 'Saudi Arabia', 'Qatar', 'Kuwait', 'Oman', 'Bahrain']);
}
if ($destinationData['faqs']) {
    $questions = [];
    foreach ($destinationData['faqs'] as $faq) $questions[] = ['@type' => 'Question', 'name' => $faq['question'], 'acceptedAnswer' => ['@type' => 'Answer', 'text' => $faq['answer']]];
    $destinationGraph[] = ['@type' => 'FAQPage', '@id' => $destinationUrl . '#faq', 'mainEntity' => $questions];
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title><?= ilmera_place_escape($destinationTitle) ?></title>
<meta name="description" content="<?= ilmera_place_escape($destinationDescription) ?>"/>
<meta name="robots" content="<?= $destinationLive ? 'index, follow' : 'noindex, follow' ?>"/>
<meta name="theme-color" content="#04060f"/>
<link rel="canonical" href="<?= ilmera_place_escape($destinationUrl) ?>"/>
<link rel="icon" type="image/png" href="/assets/images/ilmera.logo.png"/>
<meta property="og:type" content="website"/>
<meta property="og:site_name" content="ILMERA Study Abroad"/>
<meta property="og:title" content="<?= ilmera_place_escape($destinationTitle) ?>"/>
<meta property="og:description" content="<?= ilmera_place_escape($destinationDescription) ?>"/>
<meta property="og:url" content="<?= ilmera_place_escape($destinationUrl) ?>"/>
<meta property="og:image" content="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&amp;family=Outfit:wght@300;400;500;600&amp;display=swap" rel="stylesheet"/>
<script type="application/ld+json"><?= json_encode(['@context' => 'https://schema.org', '@graph' => $destinationGraph], JSON_UNESCAPED_SLASHES | JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_INVALID_UTF8_SUBSTITUTE) ?></script>
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
.article-body a{color:var(--gold);overflow-wrap:anywhere;}
.source-citation{font-size:12px;white-space:nowrap;}
.sources-list li{scroll-margin-top:90px;}
</style>
</head>
<body>
<?php include __DIR__ . '/header.php'; ?>
<main>
<section class="article-hero">
  <?php ilmera_breadcrumbs($destinationTrail, $destinationPath); ?>
  <h1><?= ilmera_place_escape($destinationHeading) ?></h1>
</section>
<section class="s-wrap article-body">
  <div class="container">
<?php foreach (['scope_note', 'review_notice'] as $notice): if ($destinationData[$notice] === '') continue; ?>
    <p class="verification-note"><?= ilmera_place_escape($destinationData[$notice]) ?></p>
<?php endforeach; ?>
<?php if ($destinationData['intro_answer'] !== ''): ?>
    <p><?= ilmera_place_escape($destinationData['intro_answer']) ?><?= ilmera_destination_citation($destinationData['intro_source'], $destinationSources) ?></p>
<?php endif; ?>
<?php if ($destinationData['ilmera_summary'] !== ''): ?>
    <section class="author-card" style="display:block;">
      <h2>ILMERA overview</h2>
      <p><?= ilmera_place_escape($destinationData['ilmera_summary']) ?></p>
    </section>
<?php endif; ?>
<?php foreach (ilmera_destination_groups() as $field => $heading): if (!$destinationData[$field]) continue; ?>
    <section>
      <h2><?= ilmera_place_escape($heading) ?></h2>
      <ul>
<?php foreach ($destinationData[$field] as $item): ?>
        <li><?= ilmera_place_escape($item['text']) ?><?= ilmera_destination_citation($item, $destinationSources) ?></li>
<?php endforeach; ?>
      </ul>
    </section>
<?php endforeach; ?>
<?php if ($destinationData['faqs']): ?>
    <section>
      <h2>Frequently asked questions</h2>
<?php foreach ($destinationData['faqs'] as $faq): ?>
      <details class="il-faq"><summary><?= ilmera_place_escape($faq['question']) ?></summary><div><p><?= ilmera_place_escape($faq['answer']) ?></p></div></details>
      <p>FAQ source<?= ilmera_destination_citation($faq, $destinationSources) ?></p>
<?php endforeach; ?>
    </section>
<?php endif; ?>
<?php if ($destinationSources): ?>
    <section>
      <h2>Sources</h2>
<?php if ($destinationData['facts_last_checked'] !== ''): ?>
      <p>Facts last checked: <time datetime="<?= ilmera_place_escape($destinationData['facts_last_checked']) ?>"><?= ilmera_place_escape($destinationData['facts_last_checked']) ?></time></p>
<?php endif; ?>
      <ol class="sources-list">
<?php foreach ($destinationSources as $index => $source): ?>
        <li id="source-<?= $index + 1 ?>"><a href="<?= ilmera_place_escape($source['source_url']) ?>" rel="noopener noreferrer"><?= ilmera_place_escape($source['source_label']) ?></a><?php if ($source['checked_on'] !== ''): ?> (checked <time datetime="<?= ilmera_place_escape($source['checked_on']) ?>"><?= ilmera_place_escape($source['checked_on']) ?></time>)<?php endif; ?></li>
<?php endforeach; ?>
      </ol>
    </section>
<?php endif; ?>
    <?php if ($destinationLive) ilmera_discovery_links(ilmera_published_destinations(), 'Other destinations', $destinationPath); ?>
    <section class="author-card" style="display:block;">
      <h2>Counselling with ILMERA</h2>
      <p>ILMERA counselling is online only, by phone, WhatsApp and video call, with no counselling premises.</p>
      <p><?= ilmera_link('/services', 'Explore our services', ['style' => 'color:var(--gold);']) ?> or <?= ilmera_link('/contact', 'contact ILMERA', ['style' => 'color:var(--gold);']) ?>.</p>
    </section>
  </div>
</section>
</main>
<?php include __DIR__ . '/footer.php'; ?>
<script>
window.addEventListener('scroll',function(){
  var nav=document.getElementById('il-nav');
  if(nav)nav.classList.toggle('scrolled',window.scrollY>60);
},{passive:true});
</script>
</body>
</html>
