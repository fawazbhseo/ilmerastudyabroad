<?php
$current = trim(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH), '/');
if ($current === '') $current = 'home';
?>
<?php /* includes/header.php */ ?>
<style>
/* NAV */
#il-nav{position:fixed;top:0;left:0;width:100%;height:70px;z-index:8000;display:flex;align-items:center;padding:0 60px;transition:background .4s;}
#il-nav.scrolled{background:rgba(4,6,15,0.9);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid var(--glass-border);}
html[data-theme="light"] #il-nav.scrolled{background:rgba(244,246,251,0.9);}
.nav-logo{display:flex;align-items:center;gap:10px;text-decoration:none;flex-shrink:0;}
.nav-logo img{height:38px;width:auto;display:block;}
.nav-logo .logo-light{display:none;height:52px;transform:scale(1.5);transform-origin:left center;}
html[data-theme="light"] .nav-logo .logo-dark{display:none;}
html[data-theme="light"] .nav-logo .logo-light{display:block;}

.logo-name{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:24px;color:var(--white);letter-spacing:.02em;}
.logo-sub{font-size:10px;font-weight:300;color:var(--silver);letter-spacing:.3em;text-transform:uppercase;margin-top:2px;display:block;}
html[data-theme="light"] .logo-name{color:var(--navy,#1A2E5A);}
html[data-theme="light"] .logo-sub{color:var(--navy,#1A2E5A);opacity:.75;}
html[data-theme="light"] .nav-logo > div{margin-left:6px;}
.nav-links{display:flex;align-items:center;gap:36px;margin:0 auto;list-style:none;}
.nav-links a{font-size:14px;font-weight:400;color:var(--silver);text-decoration:none;letter-spacing:.05em;position:relative;transition:color .3s;padding-bottom:4px;}
.nav-links a::after{content:'';position:absolute;bottom:0;left:0;width:0;height:1px;background:var(--gold);transition:width .3s ease;}
.nav-links a:hover,.nav-links a.active{color:var(--white);}
html[data-theme="light"] .nav-links a{color:var(--navy,#1A2E5A);opacity:.75;}
html[data-theme="light"] .nav-links a:hover,html[data-theme="light"] .nav-links a.active{color:var(--navy,#1A2E5A);opacity:1;}
.nav-links a.active::after,.nav-links a:hover::after{width:100%;}
.nav-cta{font-size:12px;font-weight:500;text-transform:uppercase;letter-spacing:.1em;color:var(--gold);border:1px solid var(--gold);background:transparent;padding:10px 20px;border-radius:3px;cursor:pointer;transition:background .3s,color .3s;white-space:nowrap;flex-shrink:0;text-decoration:none;display:inline-block;}
.nav-cta:hover{background:var(--gold);color:var(--void);}
.hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;margin-left:auto;background:none;border:none;padding:4px;z-index:8100;}
.hamburger span{display:block;width:24px;height:2px;background:var(--white);border-radius:2px;transition:all .3s ease;}
html[data-theme="light"] .hamburger span{background:var(--navy,#1A2E5A);}
.hamburger.open span:nth-child(1){transform:translateY(7px) rotate(45deg);}
.hamburger.open span:nth-child(2){opacity:0;}
.hamburger.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg);}
#mob-nav{position:fixed;inset:0;background:rgba(4,6,15,0.97);z-index:7900;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity .4s;}
#mob-nav.open{opacity:1;pointer-events:all;}
.mob-links{list-style:none;text-align:center;display:flex;flex-direction:column;gap:32px;}
.mob-links a{font-family:'Cormorant Garamond',serif;font-weight:400;font-size:36px;color:var(--white);text-decoration:none;display:block;transform:translateX(30px);opacity:0;transition:transform .4s ease,opacity .4s ease,color .3s;}
.mob-links a:hover{color:var(--gold);}
#mob-nav.open .mob-links a{transform:translateX(0);opacity:1;}
#mob-nav.open .mob-links li:nth-child(1) a{transition-delay:.1s;}
#mob-nav.open .mob-links li:nth-child(2) a{transition-delay:.17s;}
#mob-nav.open .mob-links li:nth-child(3) a{transition-delay:.24s;}
#mob-nav.open .mob-links li:nth-child(4) a{transition-delay:.31s;}
#mob-nav.open .mob-links li:nth-child(5) a{transition-delay:.38s;}
@media(max-width:768px){#il-nav{padding:0 20px;height:64px;}.nav-links,.nav-cta{display:none;}.hamburger{display:flex;}.nav-logo img{height:32px;}}
</style>

<!-- ═══ NAV ═══ -->
<nav id="il-nav">
  <a href="https://ilmerastudyabroad.com/" class="nav-logo" aria-label="ILMERA Study Abroad: Home">
    <img src="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png" alt="ILMERA Study Abroad logo" width="38" height="38"/>
    <div style="display:flex;flex-direction:column;line-height:1;">
      <span class="logo-name">ILMERA</span>
      <span class="logo-sub">Study Abroad</span>
    </div>
  </a>
  <ul class="nav-links">
  <li><a href="https://ilmerastudyabroad.com/" class="<?php echo $current === 'home' ? 'active' : ''; ?>">Home</a></li>
  <li><a href="/about" class="<?php echo $current === 'about' ? 'active' : ''; ?>">About</a></li>
  <li><a href="/services" class="<?php echo $current === 'services' ? 'active' : ''; ?>">Services</a></li>
  <li><a href="/blog" class="<?php echo (strpos($current, 'blog') === 0) ? 'active' : ''; ?>">Blog</a></li>
  <li><a href="/contact" class="<?php echo $current === 'contact' ? 'active' : ''; ?>">Contact</a></li>
</ul>
  <a href="/contact" class="nav-cta">Book Consultation</a>
  <button class="hamburger" id="hbg" aria-label="Open menu"><span></span><span></span><span></span></button>
</nav>
<div id="mob-nav">
  <ul class="mob-links">
  <li><a href="https://ilmerastudyabroad.com/" class="<?php echo $current === 'home' ? 'active' : ''; ?>">Home</a></li>
  <li><a href="/about" class="<?php echo $current === 'about' ? 'active' : ''; ?>">About</a></li>
  <li><a href="/services" class="<?php echo $current === 'services' ? 'active' : ''; ?>">Services</a></li>
  <li><a href="/blog" class="<?php echo (strpos($current, 'blog') === 0) ? 'active' : ''; ?>">Blog</a></li>
  <li><a href="/contact" class="<?php echo $current === 'contact' ? 'active' : ''; ?>">Contact</a></li>
</ul>
</div>
