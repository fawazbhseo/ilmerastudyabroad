<?php require_once __DIR__ . '/includes/site-presentation.php'; ?>
<?php
require_once __DIR__ . '/includes/breadcrumbs.php';
$pageTrail = [['name' => 'Home', 'url' => '/'], ['name' => 'All pages', 'url' => '/all-pages']];
$staticGroups = [];
foreach (ilmera_static_pages() as $page) $staticGroups[$page['type']][] = $page;
$placeGroups = ilmera_place_groups();
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>All Pages | ILMERA Study Abroad</title>
<meta name="description" content="Browse published ILMERA pages, study abroad guides and location guides, grouped by type."/>
<meta name="robots" content="index, follow"/>
<meta name="theme-color" content="#04060f"/>
<link rel="canonical" href="https://ilmerastudyabroad.com/all-pages"/>
<link rel="icon" type="image/png" href="/assets/images/ilmera.logo.png"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&amp;family=Outfit:wght@300;400;500;600&amp;display=swap" rel="stylesheet"/>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"WebPage","@id":"https://ilmerastudyabroad.com/all-pages#webpage","url":"https://ilmerastudyabroad.com/all-pages","name":"All Pages | ILMERA Study Abroad","isPartOf":{"@id":"https://ilmerastudyabroad.com/#website"},"breadcrumb":{"@id":"https://ilmerastudyabroad.com/all-pages#breadcrumb"}}
</script>
<style>
:root{--void:#04060f;--deep-navy:#0a1628;--navy:#1A2E5A;--cool-white:#F0F4FF;--white:#fff;--grey-light:#E8EDF5;--grey-mid:#8A98B8;--grey-dark:#4A5568;--silver:#C8D3E8;--gold:#C9A84C;--gold-glow:rgba(201,168,76,0.28);--glass-border:rgba(255,255,255,0.10);}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%;}
body{font-family:'Outfit',sans-serif;font-weight:300;color:var(--white);background:var(--void);}
.container{max-width:1200px;margin:0 auto;padding:0 60px;}
.directory-hero{padding:150px 24px 60px;text-align:center;}
.breadcrumb{font-size:13px;color:var(--grey-mid);margin-bottom:20px;}
.breadcrumb a{color:var(--grey-mid);text-decoration:none;}
h1{font-family:'Cormorant Garamond',serif;font-size:52px;line-height:1.15;}
.directory-hero p{font-size:15px;color:var(--grey-mid);line-height:1.8;margin:18px auto 0;max-width:560px;}
.directory-content{padding:0 0 90px;}
.directory-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:28px;}
.directory-group{min-width:0;padding:32px;border:1px solid rgba(255,255,255,0.1);border-radius:18px;background:rgba(255,255,255,0.03);}
.directory-group h2{font-family:'Cormorant Garamond',serif;font-size:30px;margin-bottom:18px;}
.directory-group ul{padding-left:20px;line-height:1.8;}
.directory-group li{margin-bottom:12px;color:var(--grey-mid);}
.directory-group a{color:var(--gold);text-underline-offset:3px;overflow-wrap:anywhere;}
.directory-group a:hover,.breadcrumb a:hover{color:var(--white);}
a:focus-visible,button:focus-visible{outline:2px solid var(--gold);outline-offset:4px;}
@media(max-width:768px){.container{padding:0 24px;}.directory-hero{padding:110px 24px 40px;}h1{font-size:34px;}.directory-grid{grid-template-columns:1fr;}.directory-group{padding:26px 22px;}}
</style>
</head>
<body>
<?php include __DIR__ . '/includes/header.php'; ?>
<main>
<section class="directory-hero">
  <?php ilmera_breadcrumbs($pageTrail, '/all-pages'); ?>
  <h1>All pages</h1>
  <p>Browse our published pages and guides by type.</p>
</section>
<div class="directory-content">
  <div class="container directory-grid">
<?php if (!empty($staticGroups['Main pages'])): ?>
    <section class="directory-group">
      <h2>Main pages</h2>
      <ul>
<?php foreach ($staticGroups['Main pages'] as $page): ?>
        <li><?= ilmera_link($page['url'], $page['title']) ?></li>
<?php endforeach; ?>
      </ul>
    </section>
<?php endif; ?>
<?php $publishedGuides = ilmera_published_posts(); if ($publishedGuides): ?>
    <section class="directory-group">
      <h2>Blog guides</h2>
      <ul>
<?php foreach ($publishedGuides as $guide): ?>
        <li><?= ilmera_post_link($guide['slug']) ?></li>
<?php endforeach; ?>
      </ul>
    </section>
<?php endif; ?>
<?php $publishedDestinations = ilmera_published_destinations(); if ($publishedDestinations): ?>
    <section class="directory-group">
      <h2>Country guides</h2>
      <ul>
<?php foreach ($publishedDestinations as $destinationGuide): ?>
        <li><?= ilmera_destination_link($destinationGuide['slug']) ?></li>
<?php endforeach; ?>
      </ul>
    </section>
<?php endif; ?>
<?php foreach ($placeGroups as $group => $locations): ?>
    <section class="directory-group">
      <h2><?= ilmera_post_escape($group) ?></h2>
      <ul>
<?php foreach ($locations as $location): ?>
        <li><?= ilmera_place_link($location['slug']) ?></li>
<?php endforeach; ?>
      </ul>
    </section>
<?php endforeach; ?>
<?php foreach (['Legal pages', 'Directory'] as $group): if (empty($staticGroups[$group])) continue; ?>
    <section class="directory-group">
      <h2><?= ilmera_post_escape($group) ?></h2>
      <ul>
<?php foreach ($staticGroups[$group] as $page): ?>
        <li><?= ilmera_link($page['url'], $page['title']) ?></li>
<?php endforeach; ?>
      </ul>
    </section>
<?php endforeach; ?>
  </div>
</div>
</main>
<?php include __DIR__ . '/includes/footer.php'; ?>
<script>
window.addEventListener('DOMContentLoaded',function(){
  var nav=document.getElementById('il-nav');
  window.addEventListener('scroll',function(){if(nav)nav.classList.toggle('scrolled',window.scrollY>60);},{passive:true});

});
</script>
</body>
</html>
