<?php require_once __DIR__ . '/includes/site-presentation.php';
require_once __DIR__ . '/includes/service-scope.php'; ?>
<?php
require_once __DIR__ . '/includes/breadcrumbs.php';
$pageTrail = [['name' => 'Home', 'url' => '/'], ['name' => 'Services', 'url' => '/services']];
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>

<!-- ═══════════════════ SEO META ═══════════════════ -->
<title>Study Abroad Consultants India | Germany, Italy, UK | ILMERA</title>
<meta name="description" content="Review ILMERA online counselling, academic checks, application, financial, scholarship and visa-document guidance. No outcomes are promised."/>
<meta name="keywords" content="Germany tuition planning, Italy scholarship eligibility, Slovakia teaching language, study costs and documents"/>
<meta name="author" content="ILMERA Study Abroad"/>
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"/>
<meta name="language" content="English"/>
<meta name="geo.region" content="IN-KA"/>
<meta name="geo.placename" content="Coorg, Karnataka, India"/>
<link rel="canonical" href="https://ilmerastudyabroad.com/services"/>

<!-- ═══════════════════ FAVICON ═══════════════════ -->
<link rel="icon" type="image/png" href="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<link rel="shortcut icon" type="image/png" href="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<link rel="apple-touch-icon" href="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>

<!-- ═══════════════════ OPEN GRAPH ═══════════════════ -->
<meta property="og:type" content="website"/>
<meta property="og:site_name" content="ILMERA Study Abroad"/>
<meta property="og:title" content="Study Abroad Consultants | Germany, Italy, UK, Russia & GCC | ILMERA"/>
<meta property="og:description" content="Review ILMERA online counselling, academic checks, application, financial, scholarship and visa-document guidance. No outcomes are promised."/>
<meta property="og:url" content="https://ilmerastudyabroad.com/services"/>
<meta property="og:image" content="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<meta property="og:image:alt" content="ILMERA Study Abroad: Your Gateway to Global Education"/>
<meta property="og:locale" content="en_IN"/>

<!-- ═══════════════════ TWITTER CARD ═══════════════════ -->
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="Study Abroad Consultants | Germany, Italy, UK, Russia & GCC | ILMERA"/>
<meta name="twitter:description" content="Study in Germany, Italy, the UK, Russia and beyond with ILMERA: admissions, visas, scholarships, no-IELTS and backlog-friendly routes."/>
<meta name="twitter:image" content="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<meta name="twitter:image:alt" content="ILMERA Study Abroad"/>

<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Outfit:wght@100;300;400;500;600;700&display=swap" rel="stylesheet"/>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js" defer></script>

<!-- ═══════════════════ STRUCTURED DATA (SEO / AEO / GEO) ═══════════════════ -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://ilmerastudyabroad.com/#organization",
      "name": "ILMERA Study Abroad",
      "alternateName": "ILMERA Study Abroad by ILMERA Group",
      "url": "https://ilmerastudyabroad.com",
      "logo": "https://ilmerastudyabroad.com/assets/images/ilmera.logo.png",
      "image": "https://ilmerastudyabroad.com/assets/images/ilmera.logo.png",
      "description": "ILMERA Study Abroad provides online-only counselling for Indian students, with no counselling premises. Services include academic and English-evidence review, admissions/application guidance, financial information, study-cost comparison, scholarship and supporting-document guidance, visa-document, appointment-procedure and refusal-related guidance, Germany APS guidance and Russia medicine counselling. ILMERA does not provide advice on working during study or staying after study. Responsible bodies make their own decisions; ILMERA does not promise outcomes.",
      "telephone": "+919019557427",
      "email": "info@ilmerastudyabroad.com",
      "foundingLocation": {"@type": "Place", "name": "Coorg, Karnataka, India"},
      "areaServed": ["Germany","Italy","United Kingdom","Czech Republic","Lithuania","Latvia","Slovakia","Russia","Saudi Arabia","UAE","Kuwait","Qatar","Bahrain","Oman","India"],
      "serviceType": ["ILMERA reviews a student's eligibility, academic qualifications, English-language evidence and admission criteria.", "ILMERA guides students on financial requirements, bank accounts and education loan information.", "ILMERA helps students identify scholarships and guides them through applications and required documents, including Italy DSU scholarships.", "ILMERA compares tuition fees and living expenses to help students choose study destinations.", "ILMERA guides students with visa documentation, appointment procedures and refusal-related guidance.", "ILMERA guides students on obtaining income certificates, MOI letters and other supporting documents.", "ILMERA guides students through APS requirements and document preparation for Germany.", "ILMERA offers counselling for students interested in studying medicine in Russia. Recognition and permission to practise are decided by the responsible authorities."],
      "contactPoint": [{
        "@type": "ContactPoint",
        "telephone": "+919019557427",
        "contactType": "customer service",
        "availableLanguage": ["English","Kannada","Malayalam","Hindi"],
        "areaServed": "IN"
      },{
        "@type": "ContactPoint",
        "telephone": "+919481084038",
        "contactType": "customer service",
        "areaServed": "IN"
      }],
      "sameAs": [
        "https://www.instagram.com/ilmera.studyabroad",
        "https://www.linkedin.com/company/ilmerastudyabroad"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://ilmerastudyabroad.com/#website",
      "url": "https://ilmerastudyabroad.com",
      "name": "ILMERA Study Abroad",
      "publisher": {"@id": "https://ilmerastudyabroad.com/#organization"}
    },
    {
      "@type": "WebPage",
      "@id": "https://ilmerastudyabroad.com/services/#webpage",
      "url": "https://ilmerastudyabroad.com/services",
      "name": "Study Abroad Services: Admissions, Visa, Scholarships | ILMERA",
      "isPartOf": {"@id": "https://ilmerastudyabroad.com/#website"},
      "about": {"@id": "https://ilmerastudyabroad.com/#organization"},
      "description": "ILMERA provides online academic review, application guidance, financial information, scholarship and visa-document guidance. No outcome is promised.",
      "breadcrumb": {"@id": "https://ilmerastudyabroad.com/services#breadcrumb"}
    },
    <?= json_encode(ilmera_scope_service_schema(), JSON_UNESCAPED_SLASHES | JSON_HEX_TAG) ?>,
    {
      "@type": "HowTo",
      "name": "How to Apply to Study Abroad with ILMERA",
      "description": "Step-by-step process to study abroad through ILMERA Study Abroad consultancy",
      "step": [
        {
                "@type": "HowToStep",
                "position": 1,
                "name": "Online Counselling",
                "text": "Online discussion of the help requested"
        },
        {
                "@type": "HowToStep",
                "position": 2,
                "name": "Profile Assessment",
                "text": "Review academic qualifications and admission criteria"
        },
        {
                "@type": "HowToStep",
                "position": 3,
                "name": "Country & University Match",
                "text": "Compare tuition fees and living expenses"
        },
        {
                "@type": "HowToStep",
                "position": 4,
                "name": "Application & Visa",
                "text": "Guidance on applications and visa documents"
        },
        {
                "@type": "HowToStep",
                "position": 5,
                "name": "Supporting Documents",
                "text": "Guidance on obtaining supporting documents"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://ilmerastudyabroad.com/services/#faq",
      "mainEntity": [
        {"@type":"Question","name":"Which countries can I study in with no IELTS?","acceptedAnswer":{"@type":"Answer","text":"Many programmes accept alternatives to IELTS, but English requirements vary by university and programme. Check the official programme page."}},
        {"@type":"Question","name":"Can I study abroad with low marks or backlogs?","acceptedAnswer":{"@type":"Answer","text":"Yes. Russia accepts students with low marks and academic backlogs for bachelor's degree programs. Slovakia, Lithuania and Latvia also accept students with lower academic scores. ILMERA reviews a student's eligibility, academic qualifications, English-language evidence and admission criteria."}},
        {"@type":"Question","name":"How do tuition and scholarship conditions differ?","acceptedAnswer":{"@type":"Answer","text":"At German public institutions, bachelor programmes and most master programmes normally have no tuition. Baden-Wuerttemberg charges non-EU tuition; Bavarian institutions may also charge. Semester contributions and living costs apply. Full-time Slovak-language study at public institutions normally has no tuition within the standard study duration. English-taught programmes charge tuition. Budget separately for living costs and other fees. Owner-provided conditional guidance. Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility. Do not rely on funding until written award terms confirm eligibility, coverage and payment."}},
        {"@type":"Question","name":"What conditional scholarship guidance does ILMERA provide for Italy?","acceptedAnswer":{"@type":"Answer","text":"Owner-provided conditional guidance. Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility. Do not rely on funding until written award terms confirm eligibility, coverage and payment."}},
        {"@type":"Question","name":"How does ILMERA support the visa application process?","acceptedAnswer":{"@type":"Answer","text":"ILMERA guides students with visa documentation, appointment procedures and refusal-related guidance. Universities, immigration authorities, scholarship bodies, lenders and banks make their own decisions. ILMERA does not decide admissions, visas, scholarships or loans and does not promise outcomes."}},
        {"@type":"Question","name":"How does teaching language affect tuition in Slovakia?","acceptedAnswer":{"@type":"Answer","text":"Full-time Slovak-language study at public institutions normally has no tuition within the standard study duration. English-taught programmes charge tuition. Budget separately for living costs and other fees."}},
        {"@type":"Question","name":"How do I get started with ILMERA?","acceptedAnswer":{"@type":"Answer","text":"Discuss online counselling by calling +91 90195 57427 or +91 94810 84038, emailing info@ilmerastudyabroad.com, or messaging on WhatsApp. ILMERA is based in Coorg, Kodagu, Karnataka, and consults with students by phone, WhatsApp and video call."}}
      ]
    }
  ]
}
</script>

<style>
:root{
  --void:#04060f;--deep-navy:#0a1628;--navy:#1A2E5A;--navy-light:#243659;
  --cool-white:#F0F4FF;--white:#FFFFFF;--grey-light:#E8EDF5;
  --grey-mid:#8A98B8;--grey-dark:#4A5568;--silver:#C8D3E8;
  --gold:#C9A84C;--gold-glow:rgba(201,168,76,0.28);
  --glass-fill:rgba(255,255,255,0.05);--glass-border:rgba(255,255,255,0.10);
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:'Outfit',sans-serif;font-weight:300;color:var(--white);background:var(--void);overflow-x:hidden;}

/* CURSOR */
#cur-dot{position:fixed;width:6px;height:6px;background:var(--gold);border-radius:50%;pointer-events:none;z-index:9999;transform:translate(-50%,-50%);transition:width .15s,height .15s,background .2s;}
#cur-ring{position:fixed;width:32px;height:32px;border:1px solid rgba(201,168,76,0.5);border-radius:50%;pointer-events:none;z-index:9998;transform:translate(-50%,-50%);transition:width .3s,height .3s,border-color .3s;}
#cur-dot.hov{width:10px;height:10px;background:#fff;}
#cur-ring.hov{width:50px;height:50px;border-color:var(--gold);}
@media(max-width:768px){#cur-dot,#cur-ring{display:none!important;}}

/* CANVAS + OVERLAYS */
#space-canvas{position:fixed;inset:0;z-index:0;display:block;}
#vignette{position:fixed;inset:0;z-index:1;pointer-events:none;background:radial-gradient(ellipse at 50% 50%,transparent 25%,rgba(4,6,15,0.88) 100%);}
#nebula-t{position:fixed;top:-25vh;left:-15vw;width:75vw;height:75vh;z-index:1;pointer-events:none;background:radial-gradient(ellipse,rgba(15,35,85,0.5) 0%,transparent 70%);filter:blur(70px);animation:nA 22s ease-in-out infinite alternate;}
#nebula-b{position:fixed;bottom:-20vh;right:-10vw;width:65vw;height:60vh;z-index:1;pointer-events:none;background:radial-gradient(ellipse,rgba(8,18,55,0.45) 0%,transparent 70%);filter:blur(80px);animation:nA 30s ease-in-out infinite alternate-reverse;}
#gold-glow-css{position:fixed;top:10%;left:20%;width:60vw;height:50vh;z-index:1;pointer-events:none;background:radial-gradient(ellipse,rgba(201,168,76,0.055) 0%,transparent 65%);filter:blur(60px);animation:gP 10s ease-in-out infinite;}
#grain{position:fixed;inset:0;z-index:2;pointer-events:none;opacity:.025;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='250' height='250'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='250' height='250' filter='url(%23n)'/%3E%3C/svg%3E");background-repeat:repeat;}
@keyframes nA{0%{transform:translate(0,0) scale(1);}100%{transform:translate(38px,30px) scale(1.12);}}
@keyframes gP{0%,100%{opacity:.4;transform:scale(1);}50%{opacity:1;transform:scale(1.2);}}
#float-layer{position:fixed;inset:0;z-index:2;pointer-events:none;overflow:hidden;}
.f-elem{position:absolute;pointer-events:none;opacity:0;animation:floatUp linear infinite;}
@keyframes floatUp{0%{opacity:0;transform:translateY(0) rotate(0deg);}10%{opacity:.65;}85%{opacity:.45;}100%{opacity:0;transform:translateY(-110vh) rotate(540deg);}}
@media(max-width:768px){#float-layer{display:none;}}


/* LAYOUT */
.s-wrap{position:relative;z-index:10;}
.container{max-width:1200px;margin:0 auto;padding:0 60px;}
@media(max-width:768px){.container{padding:0 22px;}}
.sec-label{font-size:11px;font-weight:300;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);margin-bottom:16px;display:block;}
.sec-h2{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:48px;line-height:1.15;margin-bottom:64px;}
.sec-h2.dk{color:var(--deep-navy);}.sec-h2.lt{color:var(--white);}
@media(max-width:768px){.sec-h2{font-size:30px;margin-bottom:40px;}}

/* MINI HERO */
.mini-hero{position:relative;min-height:72vh;display:flex;align-items:center;justify-content:center;text-align:center;z-index:10;overflow:hidden;}
.mini-inner{position:relative;z-index:25;padding:130px 24px 60px;}
.breadcrumb{font-size:13px;font-weight:300;color:var(--grey-mid);margin-bottom:20px;}
.breadcrumb a{color:var(--grey-mid);text-decoration:none;transition:color .3s;}
.breadcrumb a:hover{color:var(--gold);}
.mini-hero h1{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:60px;color:var(--white);line-height:1.08;}
.mini-hero h1 em{font-style:italic;color:rgba(240,244,255,.8);display:block;}
.mini-hero-sub{font-size:18px;font-weight:300;color:var(--grey-mid);max-width:600px;margin:20px auto 0;line-height:1.7;}
.hud-badge{background:rgba(4,6,15,0.62);border:1px solid rgba(201,168,76,0.45);border-radius:10px;padding:10px 18px;text-align:center;backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);white-space:nowrap;}
.hud-badge-title{font-size:10px;font-weight:300;color:var(--gold);text-transform:uppercase;letter-spacing:.18em;display:block;margin-bottom:3px;}
.hud-badge-val{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:22px;color:var(--white);display:block;}
.hud-tag{background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);border-radius:8px;padding:6px 14px;font-size:12px;color:var(--white);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);}
.scroll-ind{position:absolute;bottom:32px;left:50%;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;gap:8px;z-index:10;transition:opacity .6s;}
.scroll-ind span{font-size:10px;color:rgba(138,152,184,.6);letter-spacing:.25em;text-transform:uppercase;}
.scroll-arr{width:18px;height:18px;border-right:1px solid rgba(138,152,184,.45);border-bottom:1px solid rgba(138,152,184,.45);transform:rotate(45deg);animation:bounce 1.8s ease-in-out infinite;}
@keyframes bounce{0%,100%{transform:rotate(45deg) translateY(0);}50%{transform:rotate(45deg) translateY(6px);}}
@media(max-width:768px){.mini-hero{min-height:auto;}.mini-hero h1{font-size:34px;}.mini-hero-sub{font-size:15px;}.mini-inner{padding:120px 22px 50px;}}

/* SERVICE SECTIONS */
.svc-sec{padding:110px 0;position:relative;overflow:hidden;}
.svc-sec.bg-dark{background:rgba(4,6,15,0.97);}
.svc-sec.bg-navy{background:rgba(10,22,40,0.98);}
.svc-sec.bg-light{background:rgba(240,244,255,0.97);}
.svc-grid{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center;max-width:1100px;margin:0 auto;padding:0 60px;}
.svc-grid.rev{direction:rtl;}.svc-grid.rev>*{direction:ltr;}
.svc-num{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:96px;color:var(--gold);opacity:.07;position:absolute;top:30px;left:70px;pointer-events:none;line-height:1;}
.svc-text{position:relative;}
.svc-icon{width:52px;height:52px;color:var(--gold);margin-bottom:22px;display:block;transition:transform .7s ease;}
.svc-text:hover .svc-icon{transform:rotate(360deg);}
.svc-text h2{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:42px;line-height:1.18;margin-bottom:18px;}
.on-dark h2{color:var(--white);}.on-light h2{color:var(--deep-navy);}
.svc-text p{font-size:16px;font-weight:300;line-height:1.75;margin-bottom:22px;}
.on-dark p{color:var(--grey-mid);}.on-light p{color:var(--grey-dark);}
.svc-list{list-style:none;margin-bottom:26px;}
.svc-list li{font-size:14px;font-weight:300;padding:8px 0 8px 30px;position:relative;line-height:1.5;}
.svc-list li .li-ico{position:absolute;left:0;top:7px;width:18px;text-align:center;}
.on-dark .svc-list li{color:var(--grey-mid);}.on-light .svc-list li{color:var(--grey-dark);}
.svc-cta{font-size:14px;font-weight:500;color:var(--gold);text-decoration:none;letter-spacing:.05em;position:relative;display:inline-block;}
.svc-cta::after{content:'';position:absolute;bottom:-2px;left:0;width:0;height:1px;background:var(--gold);transition:width .3s;}
.svc-cta:hover::after{width:100%;}

/* SHAPE BOXES */
.shape-box{display:flex;align-items:center;justify-content:center;height:300px;position:relative;}
@keyframes sPulse{0%,100%{transform:scale(1);opacity:.4;}50%{transform:scale(1.09);opacity:.65;}}
@keyframes sHex{from{transform:rotate(0deg);}to{transform:rotate(360deg);}}
@keyframes sSpin{from{transform:rotate(0deg);}to{transform:rotate(360deg);}}
@keyframes sSpinR{from{transform:rotate(360deg);}to{transform:rotate(0deg);}}

/* PROCESS TIMELINE */
.process-sec{background:rgba(10,22,40,0.98);padding:130px 0;}
.process-hdr{text-align:center;margin-bottom:90px;}
.process-wrap{position:relative;max-width:1000px;margin:0 auto;padding:0 60px;}
.proc-line-bg{position:absolute;top:24px;left:calc(60px + 9%);right:calc(60px + 9%);height:2px;background:rgba(36,54,89,0.8);overflow:hidden;}
.proc-line-fill{height:100%;background:linear-gradient(to right,var(--gold),rgba(201,168,76,0.4));width:0;transition:width 1.4s ease;}
.process-steps{display:flex;position:relative;}
.proc-step{flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;padding:0 8px;}
.p-circle{width:50px;height:50px;border-radius:50%;border:2px solid rgba(36,54,89,0.9);background:rgba(10,22,40,1);display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',serif;font-weight:700;font-size:20px;color:var(--grey-mid);margin-bottom:22px;position:relative;z-index:1;flex-shrink:0;transition:border-color .5s,color .5s,transform .35s,box-shadow .35s;}
.p-circle.lit{border-color:var(--gold);color:var(--gold);transform:scale(1.12);box-shadow:0 0 20px var(--gold-glow);}
.proc-step h3{font-size:13px;font-weight:600;color:var(--white);text-transform:uppercase;letter-spacing:.07em;margin-bottom:8px;}
.proc-step p{font-size:12px;font-weight:300;color:var(--grey-mid);line-height:1.55;}
@media(max-width:768px){
  .svc-grid{grid-template-columns:1fr;gap:40px;padding:0 22px;}.svc-grid.rev{direction:ltr;}
  .svc-sec{padding:65px 0;}.shape-box{height:170px;order:-1;}
  .svc-num{font-size:64px;top:18px;left:24px;}
  .svc-text h2{font-size:30px;}
  .process-steps{flex-direction:column;gap:28px;}.proc-step{flex-direction:row;gap:18px;text-align:left;align-items:flex-start;}
  .proc-line-bg{display:none;}.process-wrap{padding:0 22px;}.process-sec{padding:70px 0;}.process-hdr{margin-bottom:50px;}
  .proc-step h3,.proc-step p{text-align:left;}
}

/* BUTTONS */
.btn-gold{font-size:13px;font-weight:500;text-transform:uppercase;letter-spacing:.1em;background:var(--gold);color:var(--void);border:none;padding:16px 36px;border-radius:3px;cursor:pointer;transition:background .3s,box-shadow .3s,transform .2s;text-decoration:none;display:inline-block;}
.btn-gold:hover{background:#d4b05a;box-shadow:0 0 40px var(--gold-glow);transform:translateY(-2px);}
.btn-ghost{font-size:13px;font-weight:500;text-transform:uppercase;letter-spacing:.1em;background:transparent;color:var(--white);border:1px solid rgba(255,255,255,0.2);padding:16px 36px;border-radius:3px;cursor:pointer;transition:background .3s,border-color .3s,transform .2s;text-decoration:none;display:inline-block;}
.btn-ghost:hover{background:rgba(255,255,255,0.06);border-color:rgba(255,255,255,0.4);transform:translateY(-2px);}
.cta-btn-row{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;}

.toast{position:fixed;bottom:30px;right:30px;background:rgba(0,180,80,0.12);border:1px solid rgba(0,180,80,0.4);backdrop-filter:blur(20px);padding:16px 24px;border-radius:12px;font-size:14px;color:#00d46a;z-index:9999;transform:translateY(20px);opacity:0;transition:all .4s ease;pointer-events:none;}
.toast.show{transform:translateY(0);opacity:1;}

/* Badge cards */
.badge-card{background:rgba(255,255,255,0.05);border:1px solid rgba(201,168,76,0.25);border-radius:12px;padding:22px 16px;text-align:center;transition:transform .3s,border-color .3s;}
.badge-card:hover{transform:translateY(-4px);border-color:rgba(201,168,76,0.5);}
.badge-icon{font-size:28px;display:block;margin-bottom:10px;line-height:1;}
.badge-title{font-size:13px;font-weight:600;color:var(--white);display:block;margin-bottom:6px;text-transform:uppercase;letter-spacing:.06em;}
.badge-sub{font-size:12px;font-weight:300;color:var(--gold);}
/* Country flag badges */
.country-flag-badge{display:inline-flex;align-items:center;gap:6px;font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;background:rgba(201,168,76,0.12);border:1px solid rgba(201,168,76,0.4);color:var(--gold);padding:6px 14px;border-radius:20px;margin-bottom:18px;line-height:1.3;}
.country-flag-badge .flag{font-size:14px;}
/* Highlight boxes */
.highlight-box{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.09);border-radius:10px;padding:18px 20px;margin-bottom:20px;}
.highlight-box.on-light{background:rgba(0,0,0,0.04);border-color:rgba(0,0,0,0.09);}
.highlight-title{font-size:12px;font-weight:600;color:var(--gold);text-transform:uppercase;letter-spacing:.1em;margin-bottom:12px;display:flex;align-items:center;gap:8px;}
/* Tags */
.tag-row{display:flex;flex-wrap:wrap;gap:8px;}
.tag{background:rgba(201,168,76,0.12);border:1px solid rgba(201,168,76,0.3);border-radius:20px;padding:4px 12px;font-size:12px;font-weight:300;color:var(--silver);}
.on-light .tag{color:var(--grey-dark);}
/* Service mini cards */
.service-mini-card{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.09);border-radius:14px;padding:32px 24px;transition:transform .3s,border-color .3s,box-shadow .3s;position:relative;overflow:hidden;}
.service-mini-card:hover{transform:translateY(-6px);border-color:rgba(201,168,76,0.35);box-shadow:0 16px 40px rgba(0,0,0,0.3);}
.smc-icon{font-size:32px;margin-bottom:16px;display:block;line-height:1;}
.service-mini-card h3{font-size:16px;font-weight:600;color:var(--white);margin-bottom:10px;}
.service-mini-card p{font-size:13px;font-weight:300;color:var(--grey-mid);line-height:1.6;}

/* FAQ */
.faq-sec{background:rgba(10,22,40,0.98);padding:110px 0;}
.faq-wrap{max-width:820px;margin:0 auto;}
.faq-item{border-bottom:1px solid rgba(255,255,255,0.08);transition:background .3s ease;}
.faq-q{width:100%;background:none;border:none;text-align:left;cursor:pointer;padding:24px 50px 24px 4px;font-family:'Outfit',sans-serif;font-size:17px;font-weight:500;color:var(--white);position:relative;display:block;}
.faq-q::after{content:'+';position:absolute;right:8px;top:50%;transform:translateY(-50%);font-size:26px;font-weight:300;color:var(--gold);transition:transform .3s;line-height:1;}
.faq-item.open .faq-q::after{transform:translateY(-50%) rotate(45deg);}
.faq-a{max-height:0;overflow:hidden;transition:max-height .4s ease,padding .4s ease;}
.faq-item.open .faq-a{max-height:none;padding:0 4px 24px;}
.faq-a p{font-size:15px;font-weight:300;color:var(--grey-mid);line-height:1.7;}
@media(max-width:768px){.faq-sec{padding:70px 0;}.faq-q{font-size:15px;padding:20px 44px 20px 4px;}}

@media(max-width:768px){
  .badge-card{padding:18px 12px;}
  .service-mini-card{padding:24px 18px;}
}

/* Responsive grids */
.badge-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;max-width:1100px;margin:0 auto;}
.svc-mini-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;max-width:1100px;margin:0 auto;}
@media(max-width:980px){.svc-mini-grid{grid-template-columns:1fr 1fr;}}
@media(max-width:600px){.svc-mini-grid{grid-template-columns:1fr;}.badge-grid{grid-template-columns:1fr 1fr;}}
@media(max-width:380px){.badge-grid{grid-template-columns:1fr;}}

/* ANIMATIONS */
.anim-fade-up    { opacity:0; transform:translateY(60px); transition:opacity .8s ease, transform .8s ease; }
.anim-fade-left  { opacity:0; transform:translateX(-60px); transition:opacity .8s ease, transform .8s ease; }
.anim-fade-right { opacity:0; transform:translateX(60px); transition:opacity .8s ease, transform .8s ease; }
.anim-scale-in   { opacity:0; transform:scale(0.88); transition:opacity .7s ease, transform .7s ease; }
.anim-visible    { opacity:1 !important; transform:none !important; }
@media(max-width:768px){
  .anim-fade-left,.anim-fade-right{transform:translateY(40px);}
}

.why-card::before, .service-mini-card::before {
  content:'';position:absolute;inset:0;border-radius:inherit;
  background:linear-gradient(135deg,transparent 0%,rgba(201,168,76,0.04) 50%,transparent 100%);
  opacity:0;transition:opacity .4s ease;pointer-events:none;
}
.service-mini-card:hover::before { opacity:1; }

@keyframes ringPulse {
  0%{box-shadow:0 0 0 0 var(--gold-glow);}70%{box-shadow:0 0 0 18px rgba(201,168,76,0);}100%{box-shadow:0 0 0 0 rgba(201,168,76,0);}
}
.btn-magnetic { transition:transform .25s cubic-bezier(.22,.61,.36,1); }
#scroll-progress{position:fixed;top:0;left:0;width:0%;height:2px;background:linear-gradient(90deg,var(--gold),rgba(201,168,76,0.4));z-index:9999;transition:width .1s linear;pointer-events:none;}
.svc-num{transition:opacity .5s;}



</style>
<noscript><style>.faq-a{max-height:none!important;overflow:visible;padding-bottom:22px;}</style></noscript>
</head>
<body>

<?php include __DIR__ . '/includes/header.php'; ?>


<!-- ═══ BACKGROUND ═══ -->
<canvas id="space-canvas"></canvas>
<div id="vignette"></div>
<div id="nebula-t"></div>
<div id="nebula-b"></div>
<div id="gold-glow-css"></div>
<div id="grain"></div>
<div id="float-layer"></div>
<div class="toast" id="toast"></div>

<main>

<!-- ═══ MINI HERO ═══ -->
<div class="mini-hero" id="miniHero">
  <div class="mini-inner">
    <?php ilmera_breadcrumbs($pageTrail, '/services'); ?>
    <h1 id="heroH1">Study Abroad<em>Destinations &amp; Services</em></h1>
    <p class="mini-hero-sub" id="heroSub">Online counselling, academic review and application guidance. Each responsible body makes its own decisions.</p>
  </div>
  <div class="scroll-ind" id="scrollInd"><span>Explore</span><div class="scroll-arr"></div></div>
</div>

<!-- ═══ QUICK BADGES ═══ -->
<section class="s-wrap" style="background:rgba(10,22,40,0.98);padding:50px 0;" aria-label="Study abroad highlights">
  <div class="container">
    <div class="badge-grid">
      <div class="badge-card"><span class="badge-icon">&#127891;</span><span class="badge-title">Tuition and scholarship planning</span><span class="badge-sub">Germany &middot; Italy &middot; Slovakia</span></div>
      <div class="badge-card"><span class="badge-icon">&#128201;</span><span class="badge-title">Low Marks? No Problem</span><span class="badge-sub">Russia &middot; Slovakia &middot; Lithuania &middot; Latvia</span></div>
      <div class="badge-card"><span class="badge-icon">&#128176;</span><span class="badge-title">Lowest Tuition Fees</span><span class="badge-sub">Czech &middot; Lithuania &middot; Latvia &middot; Russia</span></div>
      <div class="badge-card"><span class="badge-icon">&#10060;</span><span class="badge-title">IELTS Not Mandatory</span><span class="badge-sub">Russia &middot; Lithuania &middot; Latvia</span></div>
      <div class="badge-card"><span class="badge-icon">&#128196;</span><span class="badge-title">Backlogs Accepted</span><span class="badge-sub">Russia accepts low marks and backlogs</span></div>
      <div class="badge-card"><span class="badge-icon">&#128184;</span><span class="badge-title">DSU Stipend</span><span class="badge-sub">Italy DSU Scholarship</span></div>
    </div>
  </div>
</section>

<!-- ═══ GERMANY ═══ -->
<section class="svc-sec bg-navy s-wrap" id="germany">
  <span class="svc-num" aria-hidden="true">01</span>
  <div class="svc-grid">
    <div class="svc-text on-dark">
      <div class="country-flag-badge"><span class="flag">&#127465;&#127466;</span> Programme-specific tuition</div>
      <svg class="svc-icon" viewBox="0 0 52 52" fill="none" aria-hidden="true"><path d="M6 40 L26 6 L46 40 Z" stroke="currentColor" stroke-width="1.5" fill="none"/><line x1="14" y1="30" x2="38" y2="30" stroke="currentColor" stroke-width="1.5"/><circle cx="26" cy="38" r="3.5" fill="currentColor"/></svg>
      <h2><a href="<?= ilmera_place_escape(ilmera_destination_target('germany')) ?>" style="color:inherit;text-decoration:none;">Study in Germany</a><br><em style="font-style:italic;font-size:0.7em;color:var(--gold);">World-Class Education. Brighter Future.</em></h2>
      <p>At German public institutions, bachelor programmes and most master programmes normally have no tuition. Baden-Wuerttemberg charges non-EU tuition; Bavarian institutions may also charge. Semester contributions and living costs apply.</p>
      <div class="highlight-box">
        <div class="highlight-title"><span>&#11088;</span> Why Germany?</div>
        <ul class="svc-list">
          <li>At German public institutions, bachelor programmes and most master programmes normally have no tuition. Baden-Wuerttemberg charges non-EU tuition; Bavarian institutions may also charge. Semester contributions and living costs apply.</li>
          <li><span class="li-ico">&#127757;</span> Globally recognised degrees</li>
          <li><span class="li-ico">&#128188;</span> Post-study work options after graduation; the current rule depends on your pathway and destination</li>
          <li><span class="li-ico">&#128300;</span> Work opportunities during studies</li>
          <li><span class="li-ico">&#127961;</span> Safe, modern &amp; multicultural environment</li>
        </ul>
      </div>
      <div class="highlight-box">
        <div class="highlight-title"><span>&#127919;</span> Popular Fields</div>
        <div class="tag-row">
          <span class="tag">Engineering</span><span class="tag">Computer Science &amp; IT</span><span class="tag">Business &amp; Management</span><span class="tag">Health Sciences</span><span class="tag">Architecture &amp; Design</span>
        </div>
      </div>
      <a href="/contact" class="svc-cta">Apply for Germany &rarr;</a>
      <?php ilmera_render_guides(ilmera_country_guides('germany'), 'Planning guides', 3); ?>
    </div>
    <div class="shape-box">
      <div style="position:relative;width:200px;height:200px;">
        <div style="width:170px;height:170px;border-radius:50%;border:1px solid rgba(201,168,76,0.45);box-shadow:inset 0 0 50px rgba(201,168,76,0.08),0 0 50px rgba(201,168,76,0.08);animation:sPulse 4s ease-in-out infinite;position:absolute;inset:0;margin:auto;"></div>
        <div style="width:110px;height:110px;border-radius:50%;border:1px dashed rgba(201,168,76,0.28);animation:sPulse 6s ease-in-out infinite -3s;position:absolute;inset:0;margin:auto;"></div>
        <div style="position:absolute;inset:0;margin:auto;width:60px;height:60px;display:flex;align-items:center;justify-content:center;font-size:46px;">&#127465;&#127466;</div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ ITALY ═══ -->
<section class="svc-sec bg-light s-wrap" id="italy">
  <span class="svc-num" style="color:var(--deep-navy);" aria-hidden="true">02</span>
  <div class="svc-grid rev">
    <div class="svc-text on-light">
      <div class="country-flag-badge" style="background:rgba(0,100,40,0.1);border-color:rgba(0,150,60,0.4);color:#006428;"><span class="flag">&#127470;&#127481;</span> Conditional scholarship guidance</div>
      <svg class="svc-icon" viewBox="0 0 52 52" fill="none" aria-hidden="true"><polygon points="26,4 31,19 47,19 34,29 39,45 26,35 13,45 18,29 5,19 21,19" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>
      <h2><a href="<?= ilmera_place_escape(ilmera_destination_target('italy')) ?>" style="color:inherit;text-decoration:none;">Study in Italy</a><br><em style="font-style:italic;font-size:0.7em;color:var(--gold);">Your Dream Education Awaits!</em></h2>
      <p>Owner-provided conditional guidance. Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility. Do not rely on funding until written award terms confirm eligibility, coverage and payment.</p>
      <div class="highlight-box on-light" style="background:rgba(0,100,40,0.06);border-color:rgba(0,150,60,0.25);">
        <div class="highlight-title" style="color:#006428;"><span>&#127942;</span> Check award conditions</div>
        <ul class="svc-list">
          <li>Ask for written eligibility, award coverage and payment conditions before relying on funding.</li>




        </ul>
      </div>
      <div class="highlight-box on-light">
        <div class="highlight-title"><span>&#128218;</span> Available Programmes</div>
        <div class="tag-row"><span class="tag">PhD Programmes</span><span class="tag">Master's Programmes</span><span class="tag">Bachelor's (BSc)</span></div>
      </div>
      <div class="highlight-box on-light">
        <div class="highlight-title"><span>&#10024;</span> Additional Benefits</div>
        <ul class="svc-list">
          <li><span class="li-ico">&#127961;</span> Low cost of living in most student cities</li>
          <li><span class="li-ico">&#128188;</span> Work and study allowed</li>
          <li><span class="li-ico">&#128197;</span> Post-study permit options after graduation; current rules are confirmed at application time</li>
          <li><span class="li-ico">&#127466;&#127482;</span> Italian visa = access to all of Schengen Europe</li>
          <li><span class="li-ico">&#128706;</span> Long-term residence options after extended legal stay; requirements change, so confirm current rules</li>
          <li><span class="li-ico">&#9854;</span> No age limit for DSU applications</li>
        </ul>
      </div>
      <a href="/contact" class="svc-cta">Check Italy Scholarship Options &rarr;</a>
      <?php ilmera_render_guides(ilmera_country_guides('italy'), 'Planning guides', 3); ?>
    </div>
    <div class="shape-box">
      <div style="position:relative;width:200px;height:200px;">
        <svg viewBox="0 0 200 200" fill="none" style="width:190px;height:190px;animation:sSpin 18s linear infinite;" aria-hidden="true">
          <polygon points="100,12 188,62 188,138 100,188 12,138 12,62" stroke="rgba(0,150,60,0.45)" stroke-width="1.2" fill="none"/>
          <circle cx="100" cy="100" r="30" stroke="rgba(201,168,76,0.35)" stroke-width="1" fill="none"/>
          <circle cx="100" cy="100" r="8" fill="rgba(201,168,76,0.2)" stroke="rgba(201,168,76,0.6)" stroke-width="1"/>
        </svg>
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:46px;">&#127470;&#127481;</div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ UK ═══ -->
<section class="svc-sec bg-dark s-wrap" id="uk">
  <span class="svc-num" aria-hidden="true">03</span>
  <div class="svc-grid">
    <div class="svc-text on-dark">
      <div class="country-flag-badge"><span class="flag">&#127468;&#127463;</span> Globally Ranked</div>
      <svg class="svc-icon" viewBox="0 0 52 52" fill="none" aria-hidden="true"><rect x="8" y="12" width="36" height="28" rx="3" stroke="currentColor" stroke-width="1.5"/><line x1="8" y1="22" x2="44" y2="22" stroke="currentColor" stroke-width="1.5"/><circle cx="18" cy="33" r="4" stroke="currentColor" stroke-width="1.3"/></svg>
      <h2><a href="<?= ilmera_place_escape(ilmera_destination_target('uk')) ?>" style="color:inherit;text-decoration:none;">Study in the</a><br>United Kingdom</h2>
      <p>Compare universities in the UK by programme content, entry requirements, tuition and the qualification awarded. Check recognition requirements for your intended next step rather than assuming a particular career outcome.</p>
      <ul class="svc-list">
        <li><span class="li-ico">&#127963;</span> World-renowned universities with global rankings</li>
        <li><span class="li-ico">&#128218;</span> 1-year Master's programmes, faster and cost-effective</li>
        <li><span class="li-ico">&#128188;</span> Graduate visa: post-study work of 2 years for applications on or before 31 December 2026, 18 months from 1 January 2027 (per gov.uk)</li>
        <li><span class="li-ico">&#127760;</span> Multicultural, diverse campus environments</li>
        <li><span class="li-ico">&#127891;</span> Strong alumni networks worldwide</li>
      </ul>
      <a href="/contact" class="svc-cta">Apply for UK &rarr;</a>
      <?php ilmera_render_guides(ilmera_country_guides('uk'), 'Planning guides', 3); ?>
    </div>
    <div class="shape-box">
      <div style="position:relative;width:200px;height:200px;">
        <div style="position:absolute;inset:0;margin:auto;width:155px;height:155px;clip-path:polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);border:2px solid rgba(201,168,76,0.38);animation:sHex 9s linear infinite;"></div>
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:46px;">&#127468;&#127463;</div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ CZECH REPUBLIC ═══ -->
<section class="svc-sec bg-light s-wrap" id="czech-republic">
  <span class="svc-num" style="color:var(--deep-navy);" aria-hidden="true">04</span>
  <div class="svc-grid rev">
    <div class="svc-text on-light">
      <div class="country-flag-badge" style="background:rgba(0,0,150,0.08);border-color:rgba(0,0,180,0.35);color:#000096;"><span class="flag">&#127464;&#127487;</span> From &#8377;1.5 Lakh/Year</div>
      <svg class="svc-icon" viewBox="0 0 52 52" fill="none" aria-hidden="true"><rect x="6" y="6" width="30" height="40" rx="2" stroke="currentColor" stroke-width="1.5"/><line x1="13" y1="17" x2="29" y2="17" stroke="currentColor" stroke-width="1.2"/><line x1="13" y1="24" x2="29" y2="24" stroke="currentColor" stroke-width="1.2"/><line x1="13" y1="31" x2="22" y2="31" stroke="currentColor" stroke-width="1.2"/></svg>
      <h2><a href="<?= ilmera_place_escape(ilmera_destination_target('czech-republic')) ?>" style="color:inherit;text-decoration:none;">Study in Czech Republic</a><br><em style="font-style:italic;font-size:0.7em;color:var(--gold);">Unlock Your Future</em></h2>
      <p>The Czech Republic keeps tuition well below Western Europe, in the heart of Europe. Exact costs vary by university, city and programme, so check the official university page for current fees.</p>
      <div class="highlight-box on-light">
        <div class="highlight-title"><span>&#11088;</span> Why Czech Republic?</div>
        <ul class="svc-list">
          <li><span class="li-ico">&#128176;</span> Tuition varies by programme and university, staying well below Western Europe</li>
          <li><span class="li-ico">&#127969;</span> Low cost of living</li>
          <li><span class="li-ico">&#128197;</span> Post-study options after graduation; current rules are confirmed at application time</li>
          <li><span class="li-ico">&#128188;</span> Part-time work 20 hrs/week allowed</li>
          <li><span class="li-ico">&#127963;</span> Rich cultural heritage, central Europe location</li>
          <li><span class="li-ico">&#127466;&#127482;</span> Schengen visa: travel across Europe freely</li>
        </ul>
      </div>
      <a href="/contact" class="svc-cta">Apply for Czech Republic &rarr;</a>
      <?php ilmera_render_guides(ilmera_country_guides('czech-republic'), 'Planning guides', 3); ?>
    </div>
    <div class="shape-box">
      <div style="position:relative;width:200px;height:200px;">
        <svg viewBox="0 0 200 200" fill="none" style="width:190px;height:190px;animation:sSpinR 20s linear infinite;" aria-hidden="true">
          <polygon points="100,10 118,65 176,65 129,99 147,155 100,121 53,155 71,99 24,65 82,65" stroke="rgba(201,168,76,0.45)" stroke-width="1.2" fill="none"/>
          <circle cx="100" cy="100" r="40" stroke="rgba(0,0,180,0.3)" stroke-width="1" stroke-dasharray="5 4" fill="none"/>
        </svg>
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:46px;">&#127464;&#127487;</div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ LITHUANIA ═══ -->
<section class="svc-sec bg-navy s-wrap" id="lithuania">
  <span class="svc-num" aria-hidden="true">05</span>
  <div class="svc-grid">
    <div class="svc-text on-dark">
      <div class="country-flag-badge"><span class="flag">&#127473;&#127481;</span> Low Marks &middot; No IELTS</div>
      <svg class="svc-icon" viewBox="0 0 52 52" fill="none" aria-hidden="true"><path d="M6 36 Q22 18 40 24 L48 18 L46 28 L40 24" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/><path d="M11 40 L20 33 L25 38 L16 45 Z" stroke="currentColor" stroke-width="1.3" fill="none"/></svg>
      <h2><a href="<?= ilmera_place_escape(ilmera_destination_target('lithuania')) ?>" style="color:inherit;text-decoration:none;">Study in Lithuania</a><br><em style="font-style:italic;font-size:0.7em;color:var(--gold);">Start Your Career in Europe</em></h2>
      <p>Lithuania is one of Europe's most affordable and welcoming study destinations. English-taught programmes are available at several universities, and English requirements vary by university and programme, making it a good fit for students who want quality without barriers.</p>
      <ul class="svc-list">
        <li><span class="li-ico">&#128201;</span> Low marks accepted here</li>          <li><span class="li-ico">&#10060;</span> IELTS not mandatory for most programmes</li>          <li><span class="li-ico">&#127468;&#127463;</span> English-taught programmes available</li>
        <li><span class="li-ico">&#128176;</span> Affordable tuition and living costs</li>
        <li><span class="li-ico">&#127466;&#127482;</span> EU country, Schengen zone access</li>
        <li><span class="li-ico">&#128188;</span> Part-time work opportunities available</li>
      </ul>
      <a href="/contact" class="svc-cta">Apply for Lithuania &rarr;</a>
      <?php ilmera_render_guides(ilmera_country_guides('lithuania'), 'Planning guides', 3); ?>
    </div>
    <div class="shape-box">
      <div style="position:relative;width:200px;height:200px;">
        <div style="position:absolute;width:180px;height:180px;inset:0;margin:auto;border-radius:50%;border:1px solid rgba(201,168,76,0.28);animation:sPulse 5s ease-in-out infinite;"></div>
        <div style="position:absolute;width:120px;height:120px;inset:0;margin:auto;border-radius:50%;border:1px solid rgba(201,168,76,0.2);animation:sPulse 5s ease-in-out infinite -2.5s;"></div>
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:46px;">&#127473;&#127481;</div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ LATVIA ═══ -->
<section class="svc-sec bg-light s-wrap" id="latvia">
  <span class="svc-num" style="color:var(--deep-navy);" aria-hidden="true">06</span>
  <div class="svc-grid rev">
    <div class="svc-text on-light">
      <div class="country-flag-badge" style="background:rgba(150,0,0,0.08);border-color:rgba(180,0,0,0.35);color:#8b0000;"><span class="flag">&#127473;&#127483;</span> Low Fees &middot; Part-Time Work</div>
      <svg class="svc-icon" viewBox="0 0 52 52" fill="none" aria-hidden="true"><rect x="8" y="20" width="36" height="24" rx="2" stroke="currentColor" stroke-width="1.5"/><path d="M18 20 V15 A8 8 0 0 1 34 15 V20" stroke="currentColor" stroke-width="1.5" fill="none"/><circle cx="26" cy="31" r="5" stroke="currentColor" stroke-width="1.3"/></svg>
      <h2><a href="<?= ilmera_place_escape(ilmera_destination_target('latvia')) ?>" style="color:inherit;text-decoration:none;">Study in Latvia</a><br><em style="font-style:italic;font-size:0.7em;color:var(--gold);">Study Options. Application Guidance.</em></h2>
      <p>Latvia combines low tuition fees with affordable living costs and part-time work opportunities for students. Discuss your study plans and application questions with ILMERA.</p>
      <ul class="svc-list">
        <li><span class="li-ico">&#128201;</span> Low marks accepted, no high scores needed</li>
        <li><span class="li-ico">&#128176;</span> Low tuition fees and affordable living costs</li>
        <li><span class="li-ico">&#128188;</span> Part-time work opportunities for students</li>
        <li><span class="li-ico">&#127919;</span> Programme selection and application guidance</li>
        <li><span class="li-ico">&#127466;&#127482;</span> EU country with Schengen access</li>
        <li><span class="li-ico">&#127760;</span> English-taught programs available</li>
      </ul>
      <a href="/contact" class="svc-cta">Apply for Latvia &rarr;</a>
      <?php ilmera_render_guides(ilmera_country_guides('latvia'), 'Planning guides', 3); ?>
    </div>
    <div class="shape-box">
      <div style="position:relative;width:200px;height:200px;">
        <svg viewBox="0 0 200 200" fill="none" style="width:190px;height:190px;animation:sSpin 22s linear infinite;" aria-hidden="true">
          <rect x="22" y="22" width="156" height="156" rx="12" stroke="rgba(201,168,76,0.38)" stroke-width="1.2" fill="none"/>
          <rect x="44" y="44" width="112" height="112" rx="8" stroke="rgba(150,0,0,0.4)" stroke-width="1" fill="none" transform="rotate(18 100 100)"/>
          <circle cx="100" cy="100" r="28" stroke="rgba(201,168,76,0.42)" stroke-width="1.2" fill="none"/>
        </svg>
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:46px;">&#127473;&#127483;</div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ SLOVAKIA ═══ -->
<section class="svc-sec bg-dark s-wrap" id="slovakia">
  <span class="svc-num" aria-hidden="true">07</span>
  <div class="svc-grid">
    <div class="svc-text on-dark">
      <div class="country-flag-badge"><span class="flag">&#127480;&#127472;</span> Language-based tuition rules</div>
      <svg class="svc-icon" viewBox="0 0 52 52" fill="none" aria-hidden="true"><polygon points="26,4 31,19 47,19 34,29 39,45 26,35 13,45 18,29 5,19 21,19" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>
      <h2><a href="<?= ilmera_place_escape(ilmera_destination_target('slovakia')) ?>" style="color:inherit;text-decoration:none;">Study in Slovakia</a><br><em style="font-style:italic;font-size:0.7em;color:var(--gold);">Language and tuition conditions apply.</em></h2>
      <p>Full-time Slovak-language study at public institutions normally has no tuition within the standard study duration. English-taught programmes charge tuition. Budget separately for living costs and other fees.</p>
      <ul class="svc-list">
        <li>Full-time Slovak-language study at public institutions normally has no tuition within the standard study duration. English-taught programmes charge tuition. Budget separately for living costs and other fees.</li>
        <li><span class="li-ico">&#128201;</span> Low marks accepted, accessible for all students</li>
        <li><span class="li-ico">&#128176;</span> Very affordable tuition and living costs</li>
        <li><span class="li-ico">&#127466;&#127482;</span> EU country, Schengen zone, travel freely</li>          <li><span class="li-ico">&#127891;</span> Recognised European degrees</li>
          <li><span class="li-ico">&#127760;</span> English-medium programmes available</li>
      </ul>
      <a href="/contact" class="svc-cta">Apply for Slovakia &rarr;</a>
      <?php ilmera_render_guides(ilmera_country_guides('slovakia'), 'Planning guides', 3); ?>
    </div>
    <div class="shape-box">
      <div style="position:relative;width:200px;height:200px;">
        <div style="position:absolute;inset:0;margin:auto;width:155px;height:155px;clip-path:polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);border:2px solid rgba(201,168,76,0.38);animation:sHex 9s linear infinite;"></div>
        <div style="position:absolute;inset:0;margin:auto;width:100px;height:100px;clip-path:polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);border:1px solid rgba(201,168,76,0.2);animation:sHex 6s linear infinite reverse;"></div>
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:46px;">&#127480;&#127472;</div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ RUSSIA ═══ -->
<section class="svc-sec bg-navy s-wrap" id="russia">
  <span class="svc-num" aria-hidden="true">08</span>
  <div class="svc-grid">
    <div class="svc-text on-dark">
      <div class="country-flag-badge"><span class="flag">&#127479;&#127482;</span> Backlogs Accepted &middot; No IELTS</div>
      <svg class="svc-icon" viewBox="0 0 52 52" fill="none" aria-hidden="true"><circle cx="26" cy="22" r="12" stroke="currentColor" stroke-width="1.5"/><path d="M14 44 Q14 32 26 32 Q38 32 38 44" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>
      <h2><a href="<?= ilmera_place_escape(ilmera_destination_target('russia')) ?>" style="color:inherit;text-decoration:none;">Study in Russia</a><br><em style="font-style:italic;font-size:0.7em;color:var(--gold);">An Accessible Path to a Bachelor's Degree</em></h2>
      <p>Russia is a practical option for students with low marks or academic backlogs. You can complete your Bachelor's degree at a comparatively low cost, and entry requirements vary by university and programme.</p>
      <div class="highlight-box" style="background:rgba(200,0,0,0.06);border-color:rgba(200,0,0,0.2);">
        <div class="highlight-title" style="color:#e05555;"><span>&#128640;</span> Backlogs and Low Marks Accepted</div>
        <p style="font-size:13px;color:var(--grey-mid);line-height:1.6;margin-bottom:0;">If you have low marks or academic backlogs, you can still pursue your Bachelor's in Russia at a comparatively low cost; requirements vary by university.</p>
      </div>
      <ul class="svc-list">
        <li><span class="li-ico">&#10060;</span> IELTS not mandatory</li>
        <li><span class="li-ico">&#128201;</span> Low marks accepted</li>
        <li><span class="li-ico">&#128196;</span> Backlogs still eligible</li>
        <li><span class="li-ico">&#128176;</span> Very affordable fees and cost of living</li>
        <li><span class="li-ico">&#9992;</span> Straightforward visa process</li>
        <li><span class="li-ico">&#128188;</span> Part-time job possible</li>
        <li><span class="li-ico">&#127963;</span> Top-ranked universities with quality education</li>
      </ul>
      <a href="/contact" class="svc-cta">Apply for Russia &rarr;</a>
      <?php ilmera_render_guides(ilmera_country_guides('russia'), 'Planning guides', 3); ?>
    </div>
    <div class="shape-box">
      <div style="position:relative;width:200px;height:200px;">
        <div style="position:absolute;width:180px;height:180px;inset:0;margin:auto;border-radius:50%;border:1px solid rgba(200,0,0,0.3);animation:sPulse 4s ease-in-out infinite;"></div>
        <div style="position:absolute;width:130px;height:130px;inset:0;margin:auto;border-radius:50%;border:1px solid rgba(201,168,76,0.25);animation:sPulse 5s ease-in-out infinite -2s;"></div>
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:46px;">&#127479;&#127482;</div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ GCC ═══ -->
<section class="svc-sec bg-light s-wrap" id="gcc">
  <span class="svc-num" style="color:var(--deep-navy);" aria-hidden="true">09</span>
  <div class="svc-grid rev">
    <div class="svc-text on-light">
      <div class="country-flag-badge" style="background:rgba(0,100,0,0.08);border-color:rgba(0,130,0,0.35);color:#006400;"><span class="flag">&#127760;</span> UAE &middot; Saudi &middot; Kuwait &middot; Qatar &middot; Bahrain &middot; Oman</div>
      <svg class="svc-icon" viewBox="0 0 52 52" fill="none" aria-hidden="true"><circle cx="26" cy="26" r="18" stroke="currentColor" stroke-width="1.5" fill="none"/><ellipse cx="26" cy="26" rx="9" ry="18" stroke="currentColor" stroke-width="1" fill="none"/><line x1="8" y1="26" x2="44" y2="26" stroke="currentColor" stroke-width="1"/></svg>
      <h2><a href="<?= ilmera_place_escape(ilmera_destination_target('gcc')) ?>" style="color:inherit;text-decoration:none;">Study in GCC Countries</a><br><em style="font-style:italic;font-size:0.7em;color:var(--gold);">World-Class Campuses. Country-specific rules apply.</em></h2>
      <p>The GCC region (UAE, Saudi Arabia, Kuwait, Qatar, Bahrain and Oman) offers outstanding universities, internationally recognised degrees, and a thriving career environment with world-class infrastructure.</p>
      <ul class="svc-list">          <li><span class="li-ico">&#127963;</span> International branch campuses of global universities</li>
          <li><span class="li-ico">&#128188;</span> Strong employment and career opportunities</li>
          <li><span class="li-ico">&#127760;</span> English-medium instruction across programmes</li>
        <li><span class="li-ico">&#127961;</span> Modern, safe, multicultural environment</li>
        <li><span class="li-ico">&#128176;</span> Scholarships available for merit students</li>
        <li><span class="li-ico">&#127757;</span> Gateway to global career opportunities</li>
      </ul>
      <a href="/contact" class="svc-cta">Apply for GCC &rarr;</a>
      <?php ilmera_render_guides(ilmera_country_guides('gcc'), 'Planning guides', 3); ?>
    </div>
    <div class="shape-box">
      <div style="position:relative;width:200px;height:200px;">
        <svg viewBox="0 0 200 200" fill="none" style="width:190px;height:190px;animation:sSpinR 20s linear infinite;" aria-hidden="true">
          <polygon points="100,10 118,65 176,65 129,99 147,155 100,121 53,155 71,99 24,65 82,65" stroke="rgba(0,150,60,0.4)" stroke-width="1.2" fill="none"/>
          <circle cx="100" cy="100" r="35" stroke="rgba(201,168,76,0.35)" stroke-width="1" stroke-dasharray="5 4" fill="none"/>
        </svg>
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:42px;">&#127760;</div>
      </div>
    </div>
  </div>
</section>

<!-- Owner-confirmed service scope, 2026-10-22 -->
<section class="s-wrap" id="our-services" style="padding:70px 0;"><div class="container">
<h2 class="sec-h2 lt">Our Core Services</h2>
<?= ilmera_scope_sections() ?>
<h3>Existing tuition guidance</h3><p>At German public institutions, bachelor programmes and most master programmes normally have no tuition. Baden-Wuerttemberg charges non-EU tuition; Bavarian institutions may also charge. Semester contributions and living costs apply. Full-time Slovak-language study at public institutions normally has no tuition within the standard study duration. English-taught programmes charge tuition. Budget separately for living costs and other fees. Owner-provided conditional guidance. Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility. Do not rely on funding until written award terms confirm eligibility, coverage and payment.</p>
<p>IELTS is not mandatory for many Russia &amp; Lithuania programmes.</p>
</div></section>

<!-- ═══ PROCESS TIMELINE ═══ -->
<section class="s-wrap process-sec" id="process">
  <div class="container">
    <div class="process-hdr">
      <span class="sec-label">Step by Step</span>
      <h2 class="sec-h2 lt">The ILMERA Journey</h2>
    </div>
    <div class="process-wrap">
      <div class="proc-line-bg"><div class="proc-line-fill" id="procFill"></div></div>
      <div class="process-steps">
        <div class="proc-step"><div class="p-circle" id="pc1">1</div><h3>Online Counselling</h3><p>Online discussion of the help requested</p></div>
        <div class="proc-step"><div class="p-circle" id="pc2">2</div><h3>Profile Assessment</h3><p>Review academic qualifications and admission criteria</p></div>
        <div class="proc-step"><div class="p-circle" id="pc3">3</div><h3>Country &amp; University Match</h3><p>Compare tuition fees and living expenses</p></div>
        <div class="proc-step"><div class="p-circle" id="pc4">4</div><h3>Application &amp; Visa</h3><p>Guidance on applications and visa documents</p></div>
        <div class="proc-step"><div class="p-circle" id="pc5">5</div><h3>Supporting Documents</h3><p>Guidance on obtaining supporting documents</p></div>
      </div>
    </div>
    <div style="text-align:center;margin-top:72px;" class="cta-btn-row">
      <a href="/contact" class="btn-gold">Book Online Counselling</a>
      <a href="/contact" class="btn-ghost">Contact Us</a>
    </div>
  </div>
</section>

<!-- ═══ FAQ (AEO / GEO) ═══ -->
<section class="s-wrap faq-sec" id="faq">
  <div class="container">
    <div style="text-align:center;margin-bottom:50px;">
      <span class="sec-label">Frequently Asked Questions</span>
      <h2 class="sec-h2 lt">Study Abroad: Your Questions Answered</h2>
    </div>
    <div class="faq-wrap">
      <div class="faq-item">
        <button class="faq-q">Which countries can I study in with no IELTS?</button>
        <div class="faq-a"><p>Many programmes accept alternatives to IELTS, but English requirements vary by university and programme. Check the official programme page.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">Can I study abroad with low marks or backlogs?</button>
        <div class="faq-a"><p>Yes. Russia accepts students with low marks and academic backlogs for bachelor's degree programs. Slovakia, Lithuania and Latvia also accept students with lower academic scores. ILMERA reviews a student's eligibility, academic qualifications, English-language evidence and admission criteria.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">How do tuition and scholarship conditions differ?</button>
        <div class="faq-a"><p>At German public institutions, bachelor programmes and most master programmes normally have no tuition. Baden-Wuerttemberg charges non-EU tuition; Bavarian institutions may also charge. Semester contributions and living costs apply. Full-time Slovak-language study at public institutions normally has no tuition within the standard study duration. English-taught programmes charge tuition. Budget separately for living costs and other fees. Owner-provided conditional guidance. Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility. Do not rely on funding until written award terms confirm eligibility, coverage and payment.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">What conditional scholarship guidance does ILMERA provide for Italy?</button>
        <div class="faq-a"><p>Owner-provided conditional guidance. Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility. Do not rely on funding until written award terms confirm eligibility, coverage and payment.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">How does ILMERA support the visa application process?</button>
        <div class="faq-a"><p>ILMERA guides students with visa documentation, appointment procedures and refusal-related guidance. Universities, immigration authorities, scholarship bodies, lenders and banks make their own decisions. ILMERA does not decide admissions, visas, scholarships or loans and does not promise outcomes.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">How does teaching language affect tuition in Slovakia?</button>
        <div class="faq-a"><p>Full-time Slovak-language study at public institutions normally has no tuition within the standard study duration. English-taught programmes charge tuition. Budget separately for living costs and other fees.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">How do I get started with ILMERA?</button>
        <div class="faq-a"><p>Discuss online counselling by calling +91 90195 57427 or +91 94810 84038, emailing info@ilmerastudyabroad.com, or messaging on WhatsApp. ILMERA is based in Coorg, Kodagu, Karnataka, and consults with students by phone, WhatsApp and video call.</p></div>
      </div>
    </div>
  </div>
</section>

<div class="container">
  <?php ilmera_discovery_links(ilmera_published_destinations(), 'Destination guides'); ?>
  <?php ilmera_discovery_links(ilmera_indexable_locations(), 'Location guides'); ?>
</div>
<div class="container"><section class="source-review"><h2>Tuition guidance sources</h2><p>Checked 16 October 2026: <a href="https://www.daad.de/en/studying-in-germany/living-in-germany/finances/">DAAD tuition and living costs</a>; <a href="https://www.minedu.sk/skolne-na-vysokych-skolach-v-sr/">Slovak Ministry tuition rules</a>; <a href="https://www.universitaly.it/it/studenti-stranieri">Universitaly international student procedures</a>. The Italy scholarship statement is owner-provided conditional guidance, not an officially confirmed award. Confirm written award terms before budgeting it.</p></section></div>
</main>

<?php include __DIR__ . '/includes/footer.php'; ?>

<!-- ═══ THREE.JS SPACE ENGINE + GSAP + INTERACTIONS ═══ -->
<script>
window.addEventListener('DOMContentLoaded',function(){
(function(){
'use strict';
function lerp(a,b,t){return a+(b-a)*t;}
function rnd(a,b){return a+(b-a)*Math.random();}
function isMob(){return window.innerWidth<768;}
function isTouch(){return 'ontouchstart' in window||navigator.maxTouchPoints>0;}

var mx=window.innerWidth/2,my=window.innerHeight/2,scrollY=0;

/* CURSOR */
var dot=document.getElementById('cur-dot'),ring=document.getElementById('cur-ring');
if(!dot){dot=Object.assign(document.createElement('div'),{id:'cur-dot'});document.body.appendChild(dot);}
if(!ring){ring=Object.assign(document.createElement('div'),{id:'cur-ring'});document.body.appendChild(ring);}
var cx=mx,cy=my;
if(!isTouch()&&!isMob()){
  document.addEventListener('mousemove',function(e){mx=e.clientX;my=e.clientY;dot.style.left=mx+'px';dot.style.top=my+'px';});
  (function aC(){cx=lerp(cx,mx,.18);cy=lerp(cy,my,.18);ring.style.left=cx+'px';ring.style.top=cy+'px';requestAnimationFrame(aC);})();
  document.querySelectorAll('a,button').forEach(function(el){el.addEventListener('mouseenter',function(){dot.classList.add('hov');ring.classList.add('hov');});el.addEventListener('mouseleave',function(){dot.classList.remove('hov');ring.classList.remove('hov');});});
  document.body.style.cursor='none';
}

/* SCROLL / NAV */
window.addEventListener('scroll',function(){scrollY=window.scrollY;var nav=document.getElementById('il-nav');if(nav)nav.classList.toggle('scrolled',scrollY>60);if(scrollY>80){var s=document.getElementById('scrollInd');if(s)s.style.opacity='0';}},{passive:true});

/* FAQ ACCORDION */
document.querySelectorAll('.faq-item .faq-q').forEach(function(btn){
  btn.addEventListener('click',function(){
    var item=btn.closest('.faq-item');
    item.classList.toggle('open');
  });
});

/* THREE.JS SPACE ENGINE */
if(window.THREE){
var canvas=document.getElementById('space-canvas');
var W=window.innerWidth,H=window.innerHeight;
var scene=new THREE.Scene();
var cam=new THREE.PerspectiveCamera(65,W/H,.1,2000);
cam.position.set(0,0,130);
var ren=new THREE.WebGLRenderer({canvas:canvas,alpha:true,antialias:false,powerPreference:'high-performance'});
ren.setPixelRatio(Math.min(devicePixelRatio,2));ren.setSize(W,H);ren.setClearColor(0x04060f,1);
window.addEventListener('resize',function(){W=window.innerWidth;H=window.innerHeight;ren.setSize(W,H);cam.aspect=W/H;cam.updateProjectionMatrix();});

/* L01: Deep star field */
(function(){
  var N=isMob()?700:2000;
  var g=new THREE.BufferGeometry(),pos=new Float32Array(N*3),col=new Float32Array(N*3);
  var pal=[[1,.95,.85],[.78,.88,1],[1,.72,.5],[.7,.92,1],[1,1,1],[.88,.78,1]];
  for(var i=0;i<N;i++){pos[i*3]=rnd(-900,900);pos[i*3+1]=rnd(-600,600);pos[i*3+2]=rnd(-700,-60);var c=pal[Math.floor(Math.random()*pal.length)];col[i*3]=c[0];col[i*3+1]=c[1];col[i*3+2]=c[2];}
  g.setAttribute('position',new THREE.BufferAttribute(pos,3));
  g.setAttribute('color',new THREE.BufferAttribute(col,3));
  scene.add(new THREE.Points(g,new THREE.PointsMaterial({size:.9,vertexColors:true,transparent:true,opacity:.85,sizeAttenuation:true})));
})();

/* L02: Twinkling mid stars */
var midMat;
(function(){
  var N=isMob()?180:500;
  var g=new THREE.BufferGeometry(),pos=new Float32Array(N*3);
  for(var i=0;i<N;i++){pos[i*3]=rnd(-450,450);pos[i*3+1]=rnd(-320,320);pos[i*3+2]=rnd(-120,0);}
  g.setAttribute('position',new THREE.BufferAttribute(pos,3));
  midMat=new THREE.PointsMaterial({color:0xddeeff,size:1.6,transparent:true,opacity:.75});
  scene.add(new THREE.Points(g,midMat));
})();

/* L03: Nebula dust */
(function(){
  var N=isMob()?60:200;
  var g=new THREE.BufferGeometry(),pos=new Float32Array(N*3),col=new Float32Array(N*3);
  for(var i=0;i<N;i++){pos[i*3]=rnd(-350,350);pos[i*3+1]=rnd(-250,250);pos[i*3+2]=rnd(-250,-30);col[i*3]=rnd(.05,.3);col[i*3+1]=rnd(.1,.28);col[i*3+2]=rnd(.4,.9);}
  g.setAttribute('position',new THREE.BufferAttribute(pos,3));
  g.setAttribute('color',new THREE.BufferAttribute(col,3));
  scene.add(new THREE.Points(g,new THREE.PointsMaterial({size:9,vertexColors:true,transparent:true,opacity:.16,sizeAttenuation:true})));
})();

/* L04: Globe */
var globe,globeRing;
(function(){
  globe=new THREE.LineSegments(new THREE.WireframeGeometry(new THREE.SphereGeometry(48,24,16)),new THREE.LineBasicMaterial({color:0x1a3570,transparent:true,opacity:.38}));
  globe.position.set(isMob()?65:135,10,-85);
  scene.add(globe);
  globeRing=new THREE.Mesh(new THREE.TorusGeometry(51,1.2,8,80),new THREE.MeshBasicMaterial({color:0xc9a84c,transparent:true,opacity:.18}));
  globeRing.rotation.x=Math.PI/2;globeRing.position.copy(globe.position);
  scene.add(globeRing);
  var r2=new THREE.Mesh(new THREE.TorusGeometry(51,0.5,6,80),new THREE.MeshBasicMaterial({color:0x4488ff,transparent:true,opacity:.12}));
  r2.rotation.z=Math.PI/4;r2.position.copy(globe.position);
  scene.add(r2);
})();

/* L05: Document planes */
var docObjs=[];
(function(){
  var N=isMob()?3:8;
  for(var i=0;i<N;i++){
    var g=new THREE.Group();
    var pane=new THREE.Mesh(new THREE.PlaneGeometry(7,9),new THREE.MeshBasicMaterial({color:i%2===0?0x1a2a55:0x0a1830,transparent:true,opacity:.55,side:THREE.DoubleSide}));
    var border=new THREE.LineLoop(new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(-3.5,-4.5,0),new THREE.Vector3(3.5,-4.5,0),new THREE.Vector3(3.5,4.5,0),new THREE.Vector3(-3.5,4.5,0)]),new THREE.LineBasicMaterial({color:0xc9a84c,transparent:true,opacity:.45}));
    for(var l=0;l<5;l++){var y=l*1.5-3;g.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(-2.8,y,.01),new THREE.Vector3(2.8,y,.01)]),new THREE.LineBasicMaterial({color:0x5577aa,transparent:true,opacity:.3})));}
    var stamp=new THREE.Mesh(new THREE.CircleGeometry(1.5,12),new THREE.MeshBasicMaterial({color:0xc9a84c,wireframe:true,transparent:true,opacity:.28}));stamp.position.set(1.8,-3,.01);
    g.add(pane);g.add(border);g.add(stamp);
    g.position.set(rnd(-210,210),rnd(-150,150),rnd(-210,-15));
    g.rotation.set(rnd(-.8,.8),rnd(-1,1),rnd(-.5,.5));
    docObjs.push({g:g,vx:rnd(-.03,.03),vy:rnd(-.035,.035),vr:rnd(-.0025,.0025)});
    scene.add(g);
  }
})();

/* L06: Orbiting graduation caps */
var capOrb=[];
(function(){
  var N=isMob()?3:5;
  for(var i=0;i<N;i++){
    var g=new THREE.Group();
    g.add(new THREE.Mesh(new THREE.BoxGeometry(4,.28,4),new THREE.MeshBasicMaterial({color:0xc9a84c,transparent:true,opacity:.7})));
    var top=new THREE.Mesh(new THREE.SphereGeometry(.55,6,6),new THREE.MeshBasicMaterial({color:0xc9a84c,transparent:true,opacity:.8}));top.position.set(0,.38,0);g.add(top);
    g.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(1.5,0,1.5),new THREE.Vector3(2.7,-2.2,2.7)]),new THREE.LineBasicMaterial({color:0xc9a84c,transparent:true,opacity:.55})));
    capOrb.push({g:g,angle:(i/N)*Math.PI*2,r:rnd(68,105),y:rnd(-22,22),spd:rnd(.0004,.0009)*(i%2?1:-1)});
    scene.add(g);
  }
})();

/* L07: Open books */
var bookObjs=[];
(function(){
  var N=isMob()?3:7;
  for(var i=0;i<N;i++){
    var g=new THREE.Group();
    var c=i%2===0?0x223388:0x1a2a66;
    var lp=new THREE.Mesh(new THREE.BoxGeometry(3.8,.08,5.2),new THREE.MeshBasicMaterial({color:c,transparent:true,opacity:.6}));lp.position.set(-2,0,0);lp.rotation.y=-.2;
    var rp=new THREE.Mesh(new THREE.BoxGeometry(3.8,.08,5.2),new THREE.MeshBasicMaterial({color:c,transparent:true,opacity:.6}));rp.position.set(2,0,0);rp.rotation.y=.2;
    var sp=new THREE.Mesh(new THREE.BoxGeometry(.32,.14,5.2),new THREE.MeshBasicMaterial({color:0xc9a84c,transparent:true,opacity:.65}));
    g.add(lp);g.add(rp);g.add(sp);
    g.position.set(rnd(-200,200),rnd(-140,140),rnd(-190,-15));
    g.rotation.set(rnd(-1.1,1.1),rnd(-1.1,1.1),rnd(-1.1,1.1));
    bookObjs.push({g:g,vx:rnd(-.032,.032),vy:rnd(-.038,.038),vr:rnd(-.0028,.0028)});
    scene.add(g);
  }
})();

/* L08: DNA Helix */
var helix=new THREE.Group();
(function(){
  var N=65,R=10,pitch=2.1;
  var p1=[],p2=[];
  for(var i=0;i<N;i++){var t=(i/N)*Math.PI*7;p1.push(new THREE.Vector3(Math.cos(t)*R,i*pitch-N*pitch/2,Math.sin(t)*R));p2.push(new THREE.Vector3(Math.cos(t+Math.PI)*R,i*pitch-N*pitch/2,Math.sin(t+Math.PI)*R));}
  helix.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(p1),new THREE.LineBasicMaterial({color:0x3366ff,transparent:true,opacity:.5})));
  helix.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(p2),new THREE.LineBasicMaterial({color:0xc9a84c,transparent:true,opacity:.5})));
  for(var j=0;j<N;j+=3){var t2=(j/N)*Math.PI*7;var a=new THREE.Vector3(Math.cos(t2)*R,j*pitch-N*pitch/2,Math.sin(t2)*R);var sph=new THREE.Mesh(new THREE.SphereGeometry(1,6,6),new THREE.MeshBasicMaterial({color:j%6===0?0xc9a84c:0x4477ff,transparent:true,opacity:.7}));sph.position.copy(a);helix.add(sph);}
  helix.position.set(isMob()?-65:-150,0,-65);
  scene.add(helix);
})();

/* L09: Icosahedron */
var icoGroup=new THREE.Group();
(function(){
  icoGroup.add(new THREE.LineSegments(new THREE.WireframeGeometry(new THREE.IcosahedronGeometry(17,0)),new THREE.LineBasicMaterial({color:0x2244aa,transparent:true,opacity:.32})));
  icoGroup.add(new THREE.LineSegments(new THREE.WireframeGeometry(new THREE.IcosahedronGeometry(11,0)),new THREE.LineBasicMaterial({color:0xc9a84c,transparent:true,opacity:.16})));
  icoGroup.position.set(isMob()?-60:-125,-25,-75);
  scene.add(icoGroup);
})();

/* L10: Constellation network */
var constMesh;
(function(){
  var N=isMob()?14:26;
  var pts=[];
  for(var i=0;i<N;i++)pts.push(new THREE.Vector3(rnd(-220,220),rnd(-155,155),rnd(-230,-65)));
  var dp=new Float32Array(N*3);
  pts.forEach(function(p,i){dp[i*3]=p.x;dp[i*3+1]=p.y;dp[i*3+2]=p.z;});
  var dg=new THREE.BufferGeometry();dg.setAttribute('position',new THREE.BufferAttribute(dp,3));
  scene.add(new THREE.Points(dg,new THREE.PointsMaterial({color:0xaabbee,size:2.6,transparent:true,opacity:.62})));
  var lp=[];
  for(var a=0;a<N;a++)for(var b=a+1;b<N;b++)if(pts[a].distanceTo(pts[b])<145)lp.push(pts[a],pts[b]);
  if(lp.length){constMesh=new THREE.LineSegments(new THREE.BufferGeometry().setFromPoints(lp),new THREE.LineBasicMaterial({color:0x1e3060,transparent:true,opacity:.25}));scene.add(constMesh);}
})();

var camCX=0,camCY=0,gTX=0,gTY=0;
var clk={t:performance.now(),el:0};

function animate(){
  requestAnimationFrame(animate);
  var now=performance.now(),dt=(now-clk.t)/1000;clk.t=now;clk.el+=dt;
  var t=clk.el;
  var nmx=isMob()?0:(mx/W-.5)*2,nmy=isMob()?0:(my/H-.5)*2;

  if(midMat)midMat.opacity=.55+.28*Math.sin(t*1.1);
  if(globe){globe.rotation.y+=.0007;gTX=lerp(gTX,nmy*-.35,.04);gTY=lerp(gTY,nmx*.35,.04);globe.rotation.x=gTX;globe.rotation.z=gTY*.18;var gs=1+.013*Math.sin(t*.78);globe.scale.set(gs,gs,gs);if(globeRing){globeRing.rotation.x=Math.PI/2+t*.3;globeRing.scale.copy(globe.scale);}}
  docObjs.forEach(function(d){d.g.position.x+=d.vx;d.g.position.y+=d.vy;d.g.rotation.y+=d.vr;d.g.rotation.x+=d.vr*.4;if(Math.abs(d.g.position.y)>155)d.vy*=-1;if(Math.abs(d.g.position.x)>215)d.vx*=-1;});
  capOrb.forEach(function(o){o.angle+=o.spd;var bx=globe?globe.position.x:135,bz=globe?globe.position.z:-85;o.g.position.set(Math.cos(o.angle)*o.r+bx,o.y+Math.sin(o.angle*1.4)*10,Math.sin(o.angle)*o.r*.55+bz);o.g.rotation.y+=.009;o.g.scale.setScalar(.65+.17*Math.sin(t*.9+o.angle));});
  bookObjs.forEach(function(b){b.g.position.x+=b.vx;b.g.position.y+=b.vy;b.g.rotation.y+=b.vr;if(Math.abs(b.g.position.y)>145)b.vy*=-1;if(Math.abs(b.g.position.x)>205)b.vx*=-1;});
  if(helix){helix.rotation.y+=.005;helix.rotation.x=nmy*.11;helix.position.y=Math.sin(t*.35)*16;}
  if(icoGroup){icoGroup.rotation.x+=.003;icoGroup.rotation.y+=.005;icoGroup.rotation.z+=.002;icoGroup.position.y=Math.sin(t*.4)*18;}
  if(constMesh)constMesh.material.opacity=.12+.13*Math.sin(t*.52);

  camCX=lerp(camCX,nmx*-9,.05);camCY=lerp(camCY,nmy*5.5,.05);
  cam.position.x=camCX;cam.position.y=camCY;cam.lookAt(0,0,0);
  ren.render(scene,cam);
}
animate();
}

/* CSS FLOATING ICONS (desktop only) */
if(!isMob()){
var icons=[
  '<svg width="34" height="34" viewBox="0 0 34 34" fill="none"><path d="M17 5 L31 11 L17 17 L3 11 Z" stroke="#C9A84C" stroke-width="1.2" fill="none" opacity="0.75"/><path d="M9 14 L9 22 Q17 26 25 22 L25 14" stroke="#C9A84C" stroke-width="1.2" fill="none" opacity="0.75"/></svg>',
  '<svg width="38" height="30" viewBox="0 0 38 30" fill="none"><rect x="2" y="2" width="34" height="26" rx="2" stroke="#C9A84C" stroke-width="1.2" fill="none" opacity="0.55"/><line x1="8" y1="10" x2="30" y2="10" stroke="#C9A84C" stroke-width=".8" opacity="0.38"/><circle cx="30" cy="21" r="4.5" stroke="#C9A84C" stroke-width=".8" fill="none" opacity="0.5"/></svg>',
  '<svg width="36" height="36" viewBox="0 0 36 36" fill="none"><circle cx="18" cy="18" r="3.5" fill="#aabbff" opacity="0.85"/><ellipse cx="18" cy="18" rx="15" ry="9" stroke="#4488ff" stroke-width="1" fill="none" opacity="0.5"/><ellipse cx="18" cy="18" rx="15" ry="9" stroke="#4488ff" stroke-width="1" fill="none" opacity="0.5" transform="rotate(60 18 18)"/></svg>',
  '<svg width="36" height="36" viewBox="0 0 36 36" fill="none"><circle cx="18" cy="18" r="14" stroke="#C9A84C" stroke-width="1.2" fill="none" opacity="0.6"/><ellipse cx="18" cy="18" rx="7" ry="14" stroke="#C9A84C" stroke-width=".9" fill="none" opacity="0.5"/><line x1="4" y1="18" x2="32" y2="18" stroke="#C9A84C" stroke-width=".8" opacity="0.38"/></svg>',
  '<svg width="34" height="34" viewBox="0 0 34 34" fill="none"><polygon points="17,2 20.5,12 31,12 22.5,18.5 25.5,29 17,23 8.5,29 11.5,18.5 3,12 13.5,12" stroke="#C9A84C" stroke-width="1.2" fill="none" opacity="0.65"/></svg>',
];
var fl=document.getElementById('float-layer');
function spawnEl(){
  if(!fl)return;
  var el=document.createElement('div');el.className='f-elem';
  el.innerHTML=icons[Math.floor(Math.random()*icons.length)];
  var dur=rnd(13,24),sc=rnd(.5,1.4);
  el.style.cssText='left:'+rnd(2,95)+'%;bottom:-60px;transform:scale('+sc+') rotate('+rnd(-30,30)+'deg);animation-duration:'+dur+'s;animation-delay:'+rnd(0,3)+'s;filter:blur(.4px);';
  fl.appendChild(el);
  setTimeout(function(){el.remove();},(dur+5)*1000);
}
setInterval(spawnEl,1600);
for(var si=0;si<6;si++)setTimeout(spawnEl,si*650);
}

/* GSAP HERO + REVEALS */
if(window.gsap&&window.ScrollTrigger){
  gsap.registerPlugin(ScrollTrigger);
  var tl=gsap.timeline({delay:.25});
  tl.fromTo('#heroH1',{opacity:0,y:55},{opacity:1,y:0,duration:.9,ease:'power3.out'},0);
  tl.fromTo('#heroSub',{opacity:0,y:25},{opacity:1,y:0,duration:.7,ease:'power2.out'},.5);
  tl.fromTo('.breadcrumb',{opacity:0},{opacity:1,duration:.6},.3);
}
})();
});
</script>

<!-- ═══ SCROLL ANIMATIONS / INTERACTIONS ═══ -->
<script>
window.addEventListener('DOMContentLoaded',function(){
(function(){
'use strict';
function isMob(){return window.innerWidth<768;}

/* Scroll progress bar */
var prog=document.createElement('div');prog.id='scroll-progress';document.body.appendChild(prog);
window.addEventListener('scroll',function(){var pct=(window.scrollY/(document.body.scrollHeight-window.innerHeight))*100;prog.style.width=Math.min(pct,100)+'%';},{passive:true});

/* Generic reveal observer */
function reveal(selector,cls,stagger){
  var els=document.querySelectorAll(selector);
  if(!els.length)return;
  els.forEach(function(el){el.classList.add(cls);});
  var obs=new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(!e.isIntersecting)return;
      e.target.classList.add('anim-visible');
      obs.unobserve(e.target);
    });
  },{threshold:0.12,rootMargin:'0px 0px -50px 0px'});
  els.forEach(function(el){obs.observe(el);});
}

/* Headings + labels */
reveal('.sec-h2','anim-fade-up');
reveal('.sec-label','anim-fade-up');

/* Service text/shape alternating */
document.querySelectorAll('.svc-grid').forEach(function(grid){
  var rev=grid.classList.contains('rev');
  var txt=grid.querySelector('.svc-text');
  var shp=grid.querySelector('.shape-box');
  if(txt)txt.classList.add(rev?'anim-fade-right':'anim-fade-left');
  if(shp)shp.classList.add(rev?'anim-fade-left':'anim-fade-right');
});
(function(){
  var els=document.querySelectorAll('.svc-text,.shape-box');
  var obs=new IntersectionObserver(function(entries){entries.forEach(function(e){if(!e.isIntersecting)return;e.target.classList.add('anim-visible');obs.unobserve(e.target);});},{threshold:0.12});
  els.forEach(function(el){obs.observe(el);});
})();

/* Staggered grids */
function staggerGrid(selector,childSel){
  var grid=document.querySelector(selector);
  if(!grid)return;
  var cards=grid.querySelectorAll(childSel);
  cards.forEach(function(c){c.classList.add('anim-fade-up');});
  var obs=new IntersectionObserver(function(entries){
    if(!entries[0].isIntersecting)return;
    cards.forEach(function(c,i){setTimeout(function(){c.classList.add('anim-visible');},i*110);});
    obs.disconnect();
  },{threshold:0.1});
  obs.observe(grid);
}
staggerGrid('.badge-grid','.badge-card');
staggerGrid('.svc-mini-grid','.service-mini-card');

/* FAQ items */
reveal('.faq-item','anim-fade-up');

/* Process steps + fill */
(function(){
  var steps=document.querySelectorAll('.proc-step');
  var fill=document.getElementById('procFill');
  if(!steps.length)return;
  steps.forEach(function(s){s.classList.add('anim-fade-up');});
  var obs=new IntersectionObserver(function(entries){
    if(!entries[0].isIntersecting)return;
    steps.forEach(function(s,i){setTimeout(function(){s.classList.add('anim-visible');},i*160);});
    if(fill)setTimeout(function(){fill.style.width='100%';},200);
    document.querySelectorAll('.p-circle').forEach(function(c,i){setTimeout(function(){c.classList.add('lit');},i*220+300);});
    obs.disconnect();
  },{threshold:0.15});
  obs.observe(document.querySelector('.process-steps')||steps[0]);
})();

/* Magnetic buttons (desktop) */
if(!isMob()){
  document.querySelectorAll('.btn-gold,.btn-ghost,.nav-cta').forEach(function(btn){
    btn.classList.add('btn-magnetic');
    var bounds;
    btn.addEventListener('mouseenter',function(){bounds=btn.getBoundingClientRect();});
    btn.addEventListener('mousemove',function(e){if(!bounds)return;var dx=((e.clientX-bounds.left)/bounds.width-0.5)*14;var dy=((e.clientY-bounds.top)/bounds.height-0.5)*8;btn.style.transform='translate('+dx+'px,'+dy+'px)';});
    btn.addEventListener('mouseleave',function(){btn.style.transform='translate(0,0)';bounds=null;});
  });
  /* Card 3D tilt */
  document.querySelectorAll('.service-mini-card,.badge-card').forEach(function(card){
    var b;
    card.addEventListener('mouseenter',function(){b=card.getBoundingClientRect();});
    card.addEventListener('mousemove',function(e){if(!b)return;var rx=((e.clientY-b.top-b.height/2)/(b.height/2))*-6;var ry=((e.clientX-b.left-b.width/2)/(b.width/2))*6;card.style.transform='perspective(900px) rotateX('+rx+'deg) rotateY('+ry+'deg) translateY(-6px)';});
    card.addEventListener('mouseleave',function(){card.style.transition='transform .5s cubic-bezier(.22,.61,.36,1),box-shadow .35s,border-color .35s';card.style.transform='perspective(900px) rotateX(0) rotateY(0) translateY(0)';b=null;});
  });
}

/* GSAP ScrollTrigger refinements */
if(window.gsap&&window.ScrollTrigger){
  gsap.registerPlugin(ScrollTrigger);
  ScrollTrigger.refresh();
}
})();
});
</script>

</body>
</html>
