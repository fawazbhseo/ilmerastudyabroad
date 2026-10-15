<?php
require_once __DIR__ . '/includes/breadcrumbs.php';
$pageTrail = [['name' => 'Home', 'url' => '/'], ['name' => 'Page not found', 'url' => '/404']];
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Page Not Found (404) | ILMERA Study Abroad</title>
<meta name="description" content="That page could not be found. Browse ILMERA Study Abroad's destinations, services and blog, or book a free consultation by phone, WhatsApp or video call."/>
<meta name="robots" content="noindex, follow"/>
<meta name="theme-color" content="#04060f"/>
<link rel="icon" type="image/png" href="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<link rel="shortcut icon" type="image/png" href="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>

<!-- Open Graph -->
<meta property="og:type" content="website"/>
<meta property="og:site_name" content="ILMERA Study Abroad"/>
<meta property="og:title" content="Page Not Found | ILMERA Study Abroad"/>
<meta property="og:description" content="That page could not be found. Explore destinations, services and guides, or book a free consultation."/>
<meta property="og:url" content="https://ilmerastudyabroad.com/404"/>
<meta property="og:image" content="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<meta property="og:locale" content="en_IN"/>

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="Page Not Found | ILMERA Study Abroad"/>
<meta name="twitter:description" content="That page could not be found. Explore destinations, services and guides, or book a free consultation."/>
<meta name="twitter:image" content="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>

<!-- Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Outfit:wght@100;300;400;500;600;700&display=swap" rel="stylesheet"/>

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
.container{max-width:1200px;margin:0 auto;padding:0 60px;}
@media(max-width:768px){.container{padding:0 24px;}}
/* NAV (matches site header; static for the error page) */
#il-nav{position:fixed;top:0;left:0;width:100%;height:70px;z-index:8000;display:flex;align-items:center;padding:0 60px;background:rgba(4,6,15,0.9);border-bottom:1px solid rgba(255,255,255,0.10);}
.nav-logo{display:flex;align-items:center;gap:10px;text-decoration:none;flex-shrink:0;}
.nav-logo img{height:38px;width:auto;display:block;}
.logo-name{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:24px;color:var(--white);letter-spacing:.02em;}
.logo-sub{font-size:10px;font-weight:300;color:var(--silver);letter-spacing:.3em;text-transform:uppercase;margin-top:2px;display:block;}
@media(max-width:768px){#il-nav{padding:0 20px;height:64px;}.nav-logo img{height:32px;}}
/* 404 HERO */
.err-wrap{position:relative;z-index:10;min-height:70vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:150px 24px 80px;background:radial-gradient(ellipse at 50% 0%,rgba(201,168,76,0.08),transparent 60%);}
.err-code{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:110px;line-height:1;color:var(--gold);opacity:.9;}
.err-h1{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:40px;color:var(--white);margin:18px 0 14px;}
.err-sub{font-size:16px;font-weight:300;color:var(--grey-mid);max-width:560px;margin:0 auto 36px;line-height:1.75;}
.btn-gold{font-size:13px;font-weight:500;text-transform:uppercase;letter-spacing:.1em;background:var(--gold);color:var(--void);border:none;padding:16px 36px;border-radius:3px;cursor:pointer;transition:background .3s,box-shadow .3s,transform .2s;text-decoration:none;display:inline-block;}
.btn-gold:hover{background:#d4b05a;box-shadow:0 0 40px var(--gold-glow);transform:translateY(-2px);}
.btn-ghost{font-size:13px;font-weight:500;text-transform:uppercase;letter-spacing:.1em;background:transparent;color:var(--white);border:1px solid rgba(255,255,255,0.2);padding:16px 36px;border-radius:3px;cursor:pointer;transition:background .3s,border-color .3s,transform .2s;text-decoration:none;display:inline-block;}
.btn-ghost:hover{background:rgba(255,255,255,0.06);border-color:rgba(255,255,255,0.4);transform:translateY(-2px);}
.err-btns{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-bottom:56px;}
.err-links{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;max-width:820px;margin:0 auto;}
.err-links a{font-size:14px;font-weight:300;color:var(--silver);border:1px solid rgba(255,255,255,0.12);border-radius:20px;padding:8px 18px;text-decoration:none;transition:color .3s,border-color .3s;}
.err-links a:hover{color:var(--gold);border-color:rgba(201,168,76,0.4);}
.err-label{font-size:11px;font-weight:300;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);display:block;margin-bottom:18px;}
@media(max-width:768px){.err-code{font-size:72px;}.err-h1{font-size:28px;}.err-wrap{padding:120px 20px 60px;}}
.breadcrumb{font-size:13px;font-weight:300;color:var(--grey-mid);margin-bottom:20px;}
.breadcrumb a{color:var(--grey-mid);text-decoration:none;}
</style>
</head>
<body>

<!-- NAV -->
<nav id="il-nav">
  <a href="https://ilmerastudyabroad.com/" class="nav-logo" aria-label="ILMERA Study Abroad: Home">
    <img src="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png" alt="ILMERA Study Abroad logo" width="38" height="38"/>
    <div style="display:flex;flex-direction:column;line-height:1;">
      <span class="logo-name">ILMERA</span>
      <span class="logo-sub">Study Abroad</span>
    </div>
  </a>
</nav>

<main>
<section class="err-wrap">
  <div>
    <?php ilmera_breadcrumbs($pageTrail, '/404'); ?>
    <span class="err-code">404</span>
    <h1 class="err-h1">This page could not be found</h1>
    <p class="err-sub">The link may be old or mistyped. Everything about studying in Germany, Italy, the UK, Russia and beyond is one click away, or book a free consultation and ask us directly.</p>
    <div class="err-btns">
      <a href="/" class="btn-gold">Back to Home</a>
      <a href="/contact" class="btn-ghost">Book Free Consultation</a>
    </div>
    <span class="err-label">Popular Pages</span>
    <div class="err-links">
      <a href="/services">Study Destinations</a>
      <a href="/services#germany">Study in Germany</a>
      <a href="/services#italy">Study in Italy</a>
      <a href="/services#uk">Study in the UK</a>
      <a href="/services#russia">Study in Russia</a>
      <a href="/about">About ILMERA</a>
      <a href="/blog/">Blog</a>
      <a href="/privacy-policy">Privacy Policy</a>
    </div>
  </div>
</section>
</main>

<!-- FOOTER -->
<footer style="background:#04060f;border-top:1px solid rgba(255,255,255,0.07);padding:40px 0;position:relative;z-index:10;">
  <div class="container" style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px;">
    <span style="font-size:12px;font-weight:300;color:var(--grey-mid);">&copy; 2026 ILMERA GROUP. All Rights Reserved.</span>
    <div style="display:flex;gap:20px;">
      <a href="/privacy-policy" style="font-size:12px;font-weight:300;color:var(--grey-mid);text-decoration:none;">Privacy Policy</a>
      <a href="/terms" style="font-size:12px;font-weight:300;color:var(--grey-mid);text-decoration:none;">Terms of Use</a>
      <?= ilmera_link('/all-pages', 'All pages', ['style' => 'font-size:12px;font-weight:300;color:var(--grey-mid);text-decoration:none;']) ?>
    </div>
  </div>
</footer>

</body>
</html>
