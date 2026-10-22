<?php require_once __DIR__ . '/../includes/site-presentation.php'; ?>
<?php
require_once __DIR__ . '/../includes/breadcrumbs.php';
$pageTrail = [['name' => 'Home', 'url' => '/'], ['name' => 'Blog', 'url' => '/blog/']];
?>
<?php require_once __DIR__ . '/../includes/posts.php'; ?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge"/>

<!-- ════════════════════════════════════════════════════════════
     PRIMARY SEO META: Blog
════════════════════════════════════════════════════════════ -->
<title>Study Abroad Blog | ILMERA Study Abroad</title>
<meta name="description" content="Practical guidance from ILMERA Study Abroad on studying in Germany, Italy, and other destinations, plus honest answers on backlogs, no-IELTS routes, and consultation from Coorg."/>
<meta name="keywords" content="Germany tuition planning, Italy scholarship eligibility, Slovakia teaching language, study costs and documents"/>
<meta name="author" content="ILMERA Study Abroad"/>
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"/>
<meta name="googlebot" content="index, follow"/>
<meta name="language" content="English"/>
<meta name="geo.region" content="IN-KA"/>
<meta name="geo.placename" content="Coorg, Karnataka, India"/>
<meta name="theme-color" content="#04060f"/>
<link rel="canonical" href="https://ilmerastudyabroad.com/blog/"/>

<!-- Favicons -->
<link rel="icon" type="image/png" href="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<link rel="shortcut icon" type="image/png" href="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<link rel="apple-touch-icon" href="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>

<!-- Open Graph -->
<meta property="og:type" content="website"/>
<meta property="og:site_name" content="ILMERA Study Abroad"/>
<meta property="og:title" content="Study Abroad Blog | ILMERA Study Abroad"/>
<meta property="og:description" content="Practical guidance on studying in Germany, Italy, and other destinations, plus honest answers on backlogs, no-IELTS routes, and consultation from Coorg."/>
<meta property="og:url" content="https://ilmerastudyabroad.com/blog/"/>
<meta property="og:image" content="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<meta property="og:image:secure_url" content="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<meta property="og:image:alt" content="ILMERA Study Abroad: Your Gateway to Global Education"/>
<meta property="og:locale" content="en_IN"/>

<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="Study Abroad Blog | ILMERA Study Abroad"/>
<meta name="twitter:description" content="Practical guidance on studying abroad: Germany, Italy, backlogs, no-IELTS routes, and consultation from Coorg."/>
<meta name="twitter:image" content="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>

<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Outfit:wght@100;300;400;500;600;700&display=swap" rel="stylesheet"/>

<!-- ════════════════════════════════════════════════════════════
     STRUCTURED DATA (SEO + AEO + GEO)
════════════════════════════════════════════════════════════ -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://ilmerastudyabroad.com/blog/#webpage",
      "url": "https://ilmerastudyabroad.com/blog/",
      "name": "Study Abroad Blog | ILMERA Study Abroad",
      "description": "Practical guidance from ILMERA Study Abroad on studying in Germany, Italy, and other destinations, plus honest answers on backlogs, no-IELTS routes, and consultation from Coorg.",
      "isPartOf": {"@id": "https://ilmerastudyabroad.com/#website"},
      "inLanguage": "en-IN",
      "breadcrumb": {"@id": "https://ilmerastudyabroad.com/blog/#breadcrumb"}
    },
    {
      "@type": "Blog",
      "@id": "https://ilmerastudyabroad.com/blog/#blog",
      "url": "https://ilmerastudyabroad.com/blog/",
      "name": "ILMERA Study Abroad Blog",
      "publisher": {"@id": "https://ilmerastudyabroad.com/#organization"},
      "blogPost": <?= json_encode(array_map(static function ($post) {
          return ['@type' => 'BlogPosting', 'headline' => $post['title'], 'url' => 'https://ilmerastudyabroad.com/blog/' . $post['slug'], 'datePublished' => $post['datePublished'], 'dateModified' => $post['dateModified'], 'author' => ['@id' => 'https://ilmerastudyabroad.com/#fawaz']];
      }, ilmera_published_posts()), JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_UNESCAPED_SLASHES) ?>
    }
  ]
}
</script>

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
.container{max-width:1200px;margin:0 auto;padding:0 60px;}
@media(max-width:768px){.container{padding:0 24px;}}

/* HERO */
.blog-hero{position:relative;padding:150px 24px 70px;text-align:center;background:radial-gradient(ellipse at 50% 0%,rgba(201,168,76,0.08),transparent 60%);}
.blog-hero .breadcrumb{font-size:13px;font-weight:300;color:var(--grey-mid);margin-bottom:20px;}
.blog-hero .breadcrumb a{color:var(--grey-mid);text-decoration:none;transition:color .3s;}
.blog-hero .breadcrumb a:hover{color:var(--gold);}
.blog-hero h1{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:56px;color:var(--white);line-height:1.15;}
.blog-hero p.sub{font-size:16px;font-weight:300;color:var(--grey-mid);margin-top:18px;max-width:620px;margin-left:auto;margin-right:auto;line-height:1.7;}
@media(max-width:768px){.blog-hero h1{font-size:34px;}.blog-hero{padding:110px 24px 40px;}}

/* GRID */
.blog-sec{background:rgba(10,22,40,0.6);padding:20px 0 110px;}
.blog-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:32px;max-width:1100px;margin:0 auto;}
@media(max-width:800px){.blog-grid{grid-template-columns:1fr;}}
.blog-card{background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:18px;padding:36px;transition:transform .3s,border-color .3s,box-shadow .3s;display:flex;flex-direction:column;}
.blog-card:hover{transform:translateY(-6px);border-color:rgba(201,168,76,0.35);box-shadow:0 20px 50px rgba(0,0,0,0.3);}
.blog-tag{display:inline-block;font-size:11px;font-weight:500;text-transform:uppercase;letter-spacing:.1em;color:var(--gold);border:1px solid rgba(201,168,76,0.4);padding:5px 12px;border-radius:20px;margin-bottom:18px;align-self:flex-start;}
.blog-card h2{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:24px;color:var(--white);line-height:1.3;margin-bottom:14px;}
.blog-card p{font-size:15px;font-weight:300;color:var(--grey-mid);line-height:1.75;margin-bottom:22px;flex-grow:1;}
.blog-meta{display:flex;justify-content:space-between;align-items:center;font-size:12px;color:var(--grey-mid);border-top:1px solid rgba(255,255,255,0.08);padding-top:16px;margin-top:auto;}
.blog-meta .author{color:var(--silver);}
.blog-read{color:var(--gold);text-decoration:none;font-size:13px;font-weight:500;text-transform:uppercase;letter-spacing:.06em;display:inline-flex;align-items:center;gap:6px;margin-top:16px;transition:gap .2s;}
.blog-read:hover{gap:10px;}

/* CTA */
.blog-cta{background:rgba(4,6,15,0.97);padding:80px 0;text-align:center;}
.blog-cta h2{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:36px;color:var(--white);margin-bottom:16px;}
.blog-cta p{font-size:15px;color:var(--grey-mid);margin-bottom:28px;max-width:520px;margin-left:auto;margin-right:auto;}
.btn-gold{font-size:13px;font-weight:500;text-transform:uppercase;letter-spacing:.1em;background:var(--gold);color:var(--void);border:none;padding:16px 36px;border-radius:3px;cursor:pointer;transition:background .3s,box-shadow .3s,transform .2s;text-decoration:none;display:inline-block;}
.btn-gold:hover{background:#d4b05a;box-shadow:0 0 40px var(--gold-glow);transform:translateY(-2px);}
</style>
</head>
<body>

<?php include __DIR__ . '/../includes/header.php'; ?>

<main>

<!-- BLOG HERO -->
<section class="blog-hero">
  <?php ilmera_breadcrumbs($pageTrail, '/blog/'); ?>
  <h1>Study Abroad Blog</h1>
  <p class="sub">Practical, honest guidance from the ILMERA Study Abroad team on Germany, Italy, backlogs, no-IELTS routes, and what consultation from Coorg actually looks like.</p>
</section>

<!-- BLOG GRID -->
<section class="s-wrap blog-sec">
  <div class="container">
    <div class="blog-grid">

<?php foreach (ilmera_published_posts() as $listedPost): ?>
      <article class="blog-card">
        <span class="blog-tag"><?= ilmera_post_escape($listedPost['category']) ?></span>
        <h2><?= ilmera_post_escape($listedPost['title']) ?></h2>
        <p><?= ilmera_post_escape($listedPost['excerpt']) ?></p>
        <div class="blog-meta">
          <span class="author">Fawaz BH, CMO</span>
          <span><?= (int) $listedPost['readMinutes'] ?> min read</span>
        </div>
        <a href="/blog/<?= ilmera_post_escape($listedPost['slug']) ?>" class="blog-read">Read <?= ilmera_post_escape($listedPost['title']) ?> &rarr;</a>
      </article>
<?php endforeach; ?>

    </div>
  </div>
</section>

<!-- CTA -->
<section class="blog-cta">
  <div class="container">
    <h2>Have a Question We Haven't Covered?</h2>
    <p>Book a online consultation and get an honest answer for your specific profile, by phone, WhatsApp, or video call.</p>
    <a href="/contact" class="btn-gold">Book a online Consultation</a>
  </div>
</section>

</main>

<?php include __DIR__ . '/../includes/footer.php'; ?>

</body>
</html>
