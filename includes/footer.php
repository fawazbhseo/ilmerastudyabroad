<?php require_once __DIR__ . '/links.php'; ?>
<style>
/* FOOTER */
#il-footer{background:#04060f;border-top:1px solid rgba(255,255,255,0.07);padding:80px 0 40px;position:relative;z-index:10;}
.ft-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:40px;margin-bottom:64px;}
.ft-grid > div{min-width:0;}
.ft-logo{display:flex;align-items:center;gap:10px;text-decoration:none;margin-bottom:4px;}
.ft-logo img{height:34px;width:auto;}
.ft-lname{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:22px;color:#fff;letter-spacing:.02em;}
.ft-lsub{font-size:10px;font-weight:300;color:#C8D3E8;letter-spacing:.3em;text-transform:uppercase;margin-top:2px;display:block;}
.ft-tagline{font-size:13px;font-weight:300;color:var(--grey-mid);max-width:220px;line-height:1.6;margin-top:12px;margin-bottom:20px;}
.ft-h4{font-size:12px;font-weight:500;color:var(--silver);text-transform:uppercase;letter-spacing:.14em;margin-bottom:20px;}
.ft-links{list-style:none;display:flex;flex-direction:column;gap:10px;}
.ft-links a{font-size:14px;font-weight:300;color:var(--grey-mid);text-decoration:none;transition:color .2s,transform .2s;display:inline-block;}
.ft-links a:hover{color:var(--white);transform:translateX(4px);}
.ft-ca{display:block;font-size:14px;font-weight:300;color:var(--grey-mid);text-decoration:none;margin-bottom:8px;transition:color .2s;}
.ft-ca:hover{color:var(--white);}
.ft-cta{font-size:11px;font-weight:500;text-transform:uppercase;letter-spacing:.1em;color:var(--gold);border:1px solid var(--gold);background:transparent;padding:8px 16px;border-radius:3px;transition:background .3s,color .3s;text-decoration:none;display:inline-block;margin-top:16px;}
.ft-cta:hover{background:var(--gold);color:var(--void);}
.social-row{display:flex;gap:12px;margin:20px 0;}
.social-btn{width:40px;height:40px;border-radius:50%;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);display:flex;align-items:center;justify-content:center;color:var(--grey-mid);text-decoration:none;transition:background .3s,color .3s,transform .3s;}
.social-btn:hover{background:var(--gold);color:var(--void);transform:scale(1.12);}
.ft-bottom{border-top:1px solid rgba(255,255,255,0.07);padding-top:28px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px;}
.ft-copy{font-size:12px;font-weight:300;color:var(--grey-mid);}
.ft-legal{display:flex;gap:20px;}
.ft-legal a{font-size:12px;font-weight:300;color:var(--grey-mid);text-decoration:none;transition:color .2s;}
.ft-legal a:hover{color:var(--white);}
@media(max-width:768px){.ft-grid{grid-template-columns:1fr 1fr;gap:32px;}.ft-bottom{flex-direction:column;text-align:center;}}
@media(max-width:480px){.ft-grid{grid-template-columns:1fr;}}
.ft-reviewed{margin-top:14px;font-size:11px;font-weight:300;color:var(--grey-mid);}
</style>

<!-- FOOTER -->
<footer id="il-footer">
<div class="container">
  <div class="ft-grid">
    <div>
      <a href="https://ilmerastudyabroad.com/" class="ft-logo" aria-label="ILMERA Study Abroad: Home">
        <img src="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png" alt="ILMERA Study Abroad logo" width="34" height="34" loading="lazy"/>
        <div style="display:flex;flex-direction:column;line-height:1;"><span class="ft-lname">ILMERA</span><span class="ft-lsub">Study Abroad</span></div>
      </a>
      <p class="ft-tagline">Your Gateway to Global Education. Based in Coorg, Kodagu, Karnataka.</p>
      <div class="social-row">
        <a href="https://www.linkedin.com/company/ilmerastudyabroad" class="social-btn" aria-label="LinkedIn"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg></a>
        <a href="https://www.instagram.com/ilmera.studyabroad" class="social-btn" aria-label="Instagram"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1.5" fill="currentColor"/></svg></a>
        <a href="https://www.facebook.com/ilmerastudyabroad" class="social-btn" aria-label="Facebook"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
        <a href="https://wa.me/421944485186" class="social-btn" aria-label="ILMERA on WhatsApp"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg></a>
      </div>
    </div>
    <div>
      <h4 class="ft-h4">Navigation</h4>
      <ul class="ft-links">
        <li><a href="https://ilmerastudyabroad.com/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/services">Services</a></li>
        <li><a href="/blog/">Blog</a></li>
        <li><a href="/contact">Contact</a></li>
        <?php if ($directoryLink = ilmera_link('/all-pages', 'All pages')): ?><li><?= $directoryLink ?></li><?php endif; ?>
      </ul>
    </div>
    <div>
      <h4 class="ft-h4">Destinations</h4>
      <ul class="ft-links">
        <li><a href="/services#germany">&#127465;&#127466; Germany</a></li>
        <li><a href="/services#italy">&#127470;&#127481; Italy</a></li>
        <li><a href="/services#uk">&#127468;&#127463; United Kingdom</a></li>
        <li><a href="/services#czech-republic">&#127464;&#127487; Czech Republic</a></li>
        <li><a href="/services#lithuania">&#127473;&#127481; Lithuania</a></li>
        <li><a href="/services#latvia">&#127473;&#127483; Latvia</a></li>
        <li><a href="/services#slovakia">&#127480;&#127472; Slovakia</a></li>
        <li><a href="/services#russia">&#127479;&#127482; Russia</a></li>
        <li><a href="/services#gcc">&#127760; GCC Countries</a></li>
      </ul>
    </div>
    <?php $footerDestinations = ilmera_published_destinations(); ?>
    <?php if ($footerDestinations): ?>
    <div>
      <h4 class="ft-h4">Country guides</h4>
      <ul class="ft-links">
        <?php foreach ($footerDestinations as $destinationGuide): ?>
        <li><?= ilmera_destination_link($destinationGuide['slug']) ?></li>
        <?php endforeach; ?>
      </ul>
    </div>
    <?php endif; ?>
    <?php $footerGuides = ilmera_published_posts(); ?>
    <?php if ($footerGuides): ?>
    <div>
      <h4 class="ft-h4">Guides</h4>
      <ul class="ft-links">
        <?php foreach ($footerGuides as $guide): ?>
        <li><?= ilmera_post_link($guide['slug']) ?></li>
        <?php endforeach; ?>
      </ul>
    </div>
    <?php endif; ?>
    <?php $footerLocations = ilmera_place_groups(); ?>
    <?php if ($footerLocations): ?>
    <div>
      <h4 class="ft-h4">Locations</h4>
      <?php foreach ($footerLocations as $group => $locations): ?>
      <h5 style="color:var(--silver);font-weight:400;margin:16px 0 10px;"><?= ilmera_post_escape($group) ?></h5>
      <ul class="ft-links">
        <?php foreach ($locations as $location): ?>
        <li><?= ilmera_place_link($location['slug']) ?></li>
        <?php endforeach; ?>
      </ul>
      <?php endforeach; ?>
    </div>
    <?php endif; ?>
    <div>
      <h4 class="ft-h4">Contact</h4>
      <a href="tel:+919019557427" class="ft-ca">&#128222; +91 90195 57427</a>
      <a href="tel:+919481084038" class="ft-ca">&#128222; +91 94810 84038</a>
      <a href="mailto:info@ilmerastudyabroad.com" class="ft-ca">&#9993; info@ilmerastudyabroad.com</a>
      <a href="https://wa.me/421944485186" class="ft-ca">&#128172; WhatsApp Us</a>
      <a href="/contact" class="ft-cta">Book Free Consultation</a>
    </div>
  </div>
  <div class="ft-bottom">
    <span class="ft-copy">&copy; 2026 ILMERA GROUP. All Rights Reserved.</span>
    <p class="ft-reviewed">Guides on this site are reviewed by the ILMERA team. Content updated: October 2026.</p>
    <div class="ft-legal"><a href="/privacy-policy">Privacy Policy</a><a href="/terms">Terms of Use</a></div>
  </div>
</div>
</footer>
