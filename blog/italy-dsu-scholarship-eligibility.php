<?php
require_once __DIR__ . '/../includes/posts.php';
$post = ilmera_post('italy-dsu-scholarship-eligibility');
require_once __DIR__ . '/../includes/breadcrumbs.php';
$pageTrail = [['name' => 'Home', 'url' => '/'], ['name' => 'Blog', 'url' => '/blog/'], ['name' => $post['title'], 'url' => '/blog/' . $post['slug']]];
if (!ilmera_post_published($post['slug'])) header('X-Robots-Tag: noindex, follow');
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge"/>

<title><?= htmlspecialchars($post['title'], ENT_QUOTES, 'UTF-8') ?> | ILMERA</title>
<meta name="description" content="<?= htmlspecialchars($post['excerpt'], ENT_QUOTES, 'UTF-8') ?>"/>
<meta name="author" content="Fawaz BH"/>
<meta name="robots" content="<?= ilmera_post_published($post['slug']) ? 'index, follow' : 'noindex, follow' ?>"/><!-- Status: includes/posts.php; release checks: flagged-items-for-verification.md -->
<meta name="googlebot" content="<?= ilmera_post_published($post['slug']) ? 'index, follow' : 'noindex, follow' ?>"/>
<meta name="language" content="English"/>
<meta name="geo.region" content="IN-KA"/>
<meta name="geo.placename" content="Coorg, Karnataka, India"/>
<meta name="theme-color" content="#04060f"/>
<link rel="canonical" href="https://ilmerastudyabroad.com/blog/italy-dsu-scholarship-eligibility"/>

<link rel="icon" type="image/png" href="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<link rel="shortcut icon" type="image/png" href="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<link rel="apple-touch-icon" href="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>

<meta property="og:type" content="article"/>
<meta property="og:site_name" content="ILMERA Study Abroad"/>
<meta property="og:title" content="<?= htmlspecialchars($post['title'], ENT_QUOTES, 'UTF-8') ?>"/>
<meta property="og:description" content="<?= htmlspecialchars($post['excerpt'], ENT_QUOTES, 'UTF-8') ?>"/>
<meta property="og:url" content="https://ilmerastudyabroad.com/blog/italy-dsu-scholarship-eligibility"/>
<meta property="og:image" content="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<meta property="og:image:secure_url" content="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<meta property="og:locale" content="en_IN"/>

<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="<?= htmlspecialchars($post['title'], ENT_QUOTES, 'UTF-8') ?>"/>
<meta name="twitter:description" content="<?= htmlspecialchars($post['excerpt'], ENT_QUOTES, 'UTF-8') ?>"/>
<meta name="twitter:image" content="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>

<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Outfit:wght@100;300;400;500;600;700&display=swap" rel="stylesheet"/>

<?php
$articleFaqs = [];
$articleUrl = 'https://ilmerastudyabroad.com/blog/' . $post['slug'];
$articleGraph = [[
    '@type' => 'BlogPosting', '@id' => $articleUrl . '#article', 'url' => $articleUrl,
    'headline' => $post['title'], 'description' => $post['excerpt'],
    'mainEntityOfPage' => $articleUrl, 'dateModified' => $post['dateModified'],
    'inLanguage' => 'en-IN', 'articleSection' => $post['category'],
    'author' => ['@type' => 'Person', '@id' => 'https://ilmerastudyabroad.com/#fawaz', 'name' => 'Fawaz BH'],
    'publisher' => ['@id' => 'https://ilmerastudyabroad.com/#organization'],
    'citation' => [
    'https://consbangalore.esteri.it/en/servizi-consolari-e-visti/servizi-per-il-cittadino-straniero/study-in-italy/',
]
]];
if (ilmera_post_published($post['slug'])) $articleGraph[0]['datePublished'] = $post['datePublished'];
if ($articleFaqs) {
    $questions = [];
    foreach ($articleFaqs as $faq) $questions[] = ['@type' => 'Question', 'name' => $faq['question'], 'acceptedAnswer' => ['@type' => 'Answer', 'text' => $faq['answer']]];
    $articleGraph[] = ['@type' => 'FAQPage', '@id' => $articleUrl . '#faq', 'mainEntity' => $questions];
}
?>
<script type="application/ld+json"><?= json_encode(['@context' => 'https://schema.org', '@graph' => $articleGraph], JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT) ?></script>

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
</style>
</head>
<body>

<?php include __DIR__ . '/../includes/header.php'; ?>

<main>
<section class="article-hero">
  <?php ilmera_breadcrumbs($pageTrail, '/blog/italy-dsu-scholarship-eligibility'); ?>
  <span class="article-tag">Italy</span>
  <h1><?= htmlspecialchars($post['title'], ENT_QUOTES, 'UTF-8') ?></h1>
  <p class="article-byline">By <span class="name">Fawaz BH, CMO</span> &middot; Reviewed <time datetime="2026-10-16">16 October 2026</time></p>
</section>
<section class="s-wrap article-body">
  <div class="container">
    <p>Do not use this draft to determine DSU eligibility or an application amount. Income thresholds, required household evidence, renewal rules and deadlines are not confirmed here. A current approved official award call is needed before those details can be published.</p>
    <div class="confirm">Draft review notice: no current regional award call on an approved host has been opened. The conditional owner statement below is not an officially verified award or evidence of a partner arrangement.</div>
    <h2>Owner-supplied conditional guidance</h2>
    <p>Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility.</p>
    <h2>What the opened official background confirms</h2>
    <p>The Italian consulate says institutions set their own admission requirements and tuition fees. Its admissions guidance does not verify the owner-supplied scholarship amount or establish a regional award entitlement. <a href="#source-IT">[IT]</a></p>
    <h2>Planning questions</h2>
    <p>Before a publication decision, obtain the current official award call, the eligible programme and intake, the award coverage and amount, and documentary authority for any partner claim. This draft supplies none of those missing confirmations.</p>
    <section aria-labelledby="article-sources"><h2 id="article-sources">Official sources</h2>
      <p>Source text reviewed on <time datetime="2026-10-16">16 October 2026</time>. Estimates retain their stated scope; historical editions are not treated as current rules.</p>
      <ul>
        <li id="source-IT"><a href="https://consbangalore.esteri.it/en/servizi-consolari-e-visti/servizi-per-il-cittadino-straniero/study-in-italy/" rel="noopener noreferrer">Italian Consulate Bengaluru: study in Italy</a></li>
      </ul>
    </section>
    <div class="author-card">
      <img src="/assets/images/fawazbh-192.webp" alt="Fawaz BH, CMO of ILMERA Study Abroad" width="56" height="56" loading="lazy"/>
      <div>
        <div class="name">Fawaz BH</div>
        <div class="role">CMO, ILMERA Study Abroad</div>
      </div>
    </div>
    <?php ilmera_render_guides(ilmera_post_related($post['slug'])); ?>
    <?= ilmera_post_service_links($post['slug']) ?>
    <p><a href="/services">Study planning services</a> or <a href="/contact">discuss your questions with ILMERA</a>.</p>
    <a href="/blog/" class="back-link">&larr; Back to articles</a>
  </div>
</section>
</main>

<?php include __DIR__ . '/../includes/footer.php'; ?>

</body>
</html>
