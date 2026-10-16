<?php
require_once __DIR__ . '/includes/breadcrumbs.php';
$pageTrail = [['name' => 'Home', 'url' => '/']];
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>

<!-- ════════════════════ PRIMARY SEO META ════════════════════ -->
<title><?php echo $page_title ?? 'ILMERA Study Abroad | Study in Germany, Italy, UK, Russia & Europe: No-IELTS & Study Cost Planning'; ?></title>
<meta name="description" content="Compare programme-specific tuition, living costs and scholarship conditions before choosing a destination. No award or admission outcome is guaranteed."/>
<meta name="keywords" content="Germany tuition planning, Italy scholarship eligibility, Slovakia teaching language, study costs and documents"/>
<meta name="author" content="ILMERA Study Abroad"/>
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"/>
<meta name="googlebot" content="index, follow"/>
<meta name="language" content="English"/>
<meta name="geo.region" content="IN-KA"/>
<meta name="geo.placename" content="Coorg, Karnataka, India"/>
<meta name="rating" content="general"/>
<meta name="theme-color" content="#04060f"/>
<link rel="canonical" href="<?php echo $page_canonical ?? 'https://ilmerastudyabroad.com/'; ?>"/>

<!-- ════════════════════ FAVICON ════════════════════ -->
<link rel="icon" type="image/png" href="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<link rel="shortcut icon" href="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<link rel="apple-touch-icon" href="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>

<!-- ════════════════════ OPEN GRAPH / FACEBOOK ════════════════════ -->
<meta property="og:type" content="website"/>
<meta property="og:site_name" content="ILMERA Study Abroad"/>
<meta property="og:url" content="<?php echo $page_url ?? 'https://ilmerastudyabroad.com/'; ?>"/>
<meta property="og:title" content="<?php echo $og_title ?? 'ILMERA Study Abroad: Your Gateway to Global Education'; ?>"/>
<meta property="og:description" content="Compare programme-specific tuition, living costs and scholarship conditions before choosing a destination. No award or admission outcome is guaranteed."/>
<meta property="og:image" content="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<meta property="og:image:alt" content="ILMERA Study Abroad logo"/>
<meta property="og:locale" content="en_IN"/>
<link rel="alternate" hreflang="en-in" href="https://ilmerastudyabroad.com/"/>
<link rel="alternate" hreflang="x-default" href="https://ilmerastudyabroad.com/"/>

<!-- ════════════════════ TWITTER / X CARD ════════════════════ -->
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="<?php echo $twitter_title ?? 'ILMERA Study Abroad: Your Gateway to Global Education'; ?>"/>
<meta name="twitter:description" content="Compare programme-specific tuition, living costs and scholarship conditions before choosing a destination. No award or admission outcome is guaranteed."/>
<meta name="twitter:image" content="https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"/>
<meta name="twitter:image:alt" content="ILMERA Study Abroad logo"/>

<!-- ════════════════════ FONTS + LIBS ════════════════════ -->
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Outfit:wght@100;300;400;500;600;700&display=swap" rel="stylesheet"/>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js" defer></script>

<!-- ════════════════════ STRUCTURED DATA (SEO / AEO / GEO) ════════════════════ -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://ilmerastudyabroad.com/#organization",
      "name": "ILMERA Study Abroad",
      "alternateName": "ILMERA Study Abroad by ILMERA Group",
      "url": "https://ilmerastudyabroad.com/",
        "logo": {
        "@type": "ImageObject",
        "url": "https://ilmerastudyabroad.com/assets/images/ilmera.logo.png"
      },
      "image": "https://ilmerastudyabroad.com/assets/images/ilmera.logo.png",
      "description": "ILMERA Study Abroad is an online overseas education consultancy based in Coorg, Kodagu, Karnataka, offering university admissions, student visa assistance, scholarship guidance and career counselling for Germany, Italy, UK, Czech Republic, Lithuania, Latvia, Slovakia, Russia and GCC countries.",
            "email": "info@ilmerastudyabroad.com",
      "telephone": "+91-9019557427",

      "contactPoint": [
        {"@type":"ContactPoint","telephone":"+919019557427","contactType":"customer service","email":"info@ilmerastudyabroad.com","areaServed":"IN","availableLanguage":["English","Kannada","Malayalam","Hindi"]},
        {"@type":"ContactPoint","telephone":"+919481084038","contactType":"customer service","areaServed":"IN"}
      ],
      "areaServed": ["Germany","Italy","United Kingdom","Czech Republic","Lithuania","Latvia","Slovakia","Russia","Saudi Arabia","UAE","Kuwait","Qatar","Bahrain","Oman","India","Karnataka","Kodagu","Coorg"],
      "knowsAbout": ["University Admissions","Student Visas","Scholarships","IELTS Preparation","Study Abroad without IELTS","European study cost planning","Study Abroad with Backlogs"],
     "serviceType": ["University Admissions Counselling","Student Visa Assistance","Scholarship Guidance","Language Test Preparation","Pre-Departure Briefings","Career Counselling Abroad","Online Study Abroad Counselling"],
      "availableChannel": {
        "@type": "ServiceChannel",
        "serviceType": "Phone, WhatsApp and video call counselling",
        "availableLanguage": ["English","Malayalam","Kannada","Hindi"]
      },
       "sameAs": [
        "https://www.facebook.com/ilmerastudyabroad",
        "https://www.instagram.com/ilmera.studyabroad",
        "https://www.linkedin.com/company/ilmerastudyabroad"
      ],
      "founder": {
    "@type": "Person",
    "@id": "https://ilmerastudyabroad.com/#jabir",
    "name": "Jabir KJ",
    "jobTitle": "Founder",
    "worksFor": {"@id": "https://ilmerastudyabroad.com/#organization"},
    "image": "https://ilmerastudyabroad.com/assets/images/jabirkj.png",
    "sameAs": ["https://www.linkedin.com/in/jabir-kj-920300428"]
},
      "employee": [
        {
          "@type": "Person",
          "@id": "https://ilmerastudyabroad.com/#jabir",
          "name": "Jabir KJ",
          "jobTitle": "Founder",
          "worksFor": {"@id": "https://ilmerastudyabroad.com/#organization"},
          "image": "https://ilmerastudyabroad.com/assets/images/jabirkj.png",
          "sameAs": ["https://www.linkedin.com/in/jabir-kj-920300428"]
        },
        {
          "@type": "Person",
          "@id": "https://ilmerastudyabroad.com/#fawaz",
          "name": "Fawaz BH",
          "jobTitle": "CMO",
          "worksFor": {"@id": "https://ilmerastudyabroad.com/#organization"},
          "image": "https://ilmerastudyabroad.com/assets/images/fawazbh.webp",
          "url": "https://fawazbhseo.in",
          "sameAs": ["https://fawazbhseo.in"]
        },
        {
          "@type": "Person",
          "@id": "https://ilmerastudyabroad.com/#zaheer",
          "name": "Zaheer KJ",
          "jobTitle": "CFO",
          "worksFor": {"@id": "https://ilmerastudyabroad.com/#organization"},
          "image": "https://ilmerastudyabroad.com/assets/images/zaheer.png"
        }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://ilmerastudyabroad.com/#website",
      "url": "https://ilmerastudyabroad.com/",
      "name": "ILMERA Study Abroad",
      "description": "Study abroad consultancy for Germany, Italy, UK, Czech Republic, Lithuania, Latvia, Slovakia, Russia and GCC: admissions, visa, scholarships.",
      "publisher": {"@id": "https://ilmerastudyabroad.com/#organization"},
      "inLanguage": "en-IN",
            "potentialAction": {
        "@type": "ReadAction",
        "target": "https://ilmerastudyabroad.com/"
      }
    },
    {
      "@type": "WebPage",
      "@id": "https://ilmerastudyabroad.com/#webpage",
      "url": "https://ilmerastudyabroad.com/",
      "name": "ILMERA Study Abroad: Your Gateway to Global Education",
      "description": "Study in Germany, Italy, UK, Czech Republic, Lithuania, Latvia, Slovakia, Russia or GCC. Expert guidance on admissions, visa, scholarships and more.",
      "isPartOf": {"@id": "https://ilmerastudyabroad.com/#website"},
      "about": {"@id": "https://ilmerastudyabroad.com/#organization"},
      "inLanguage": "en-IN",
      "breadcrumb": {"@id": "https://ilmerastudyabroad.com/#breadcrumb"}
    },
    {
          
      "@type": "FAQPage",
      "@id": "https://ilmerastudyabroad.com/#faq",
      "mainEntity": [
        {"@type":"Question","name":"Can I study abroad if I have academic backlogs?","acceptedAnswer":{"@type":"Answer","text":"In many cases, yes. Russia is a route students with academic backlogs can discuss with ILMERA, with low tuition fees and no IELTS requirement at many universities. Eligibility depends on your specific marksheet, so ILMERA reviews each profile before applying."}},
        {"@type":"Question","name":"Can I study abroad with low marks or a low percentage?","acceptedAnswer":{"@type":"Answer","text":"Yes, students with low marks can study abroad. Russia, Slovakia, Lithuania and Latvia have universities with more accessible entry requirements than many universities in the UK or US. ILMERA reviews your specific percentage and matches you to countries and universities suited to your profile."}},
        {"@type":"Question","name":"Can I study abroad without IELTS?","acceptedAnswer":{"@type":"Answer","text":"Yes, you can study abroad without IELTS in several countries. Russia and Lithuania commonly waive IELTS, and many programmes in Latvia, Slovakia and the Czech Republic accept a Medium-of-Instruction (MOI) letter or an internal English test instead. Germany also frequently waives IELTS when your prior education was in English."}},
        {"@type":"Question","name":"How should I compare total study budgets?","acceptedAnswer":{"@type":"Answer","text":"Full-time Slovak-language study at public institutions normally has no tuition within the standard study duration. English-taught programmes charge tuition. Budget separately for living costs and other fees."}},
        {"@type":"Question","name":"How do tuition and scholarship conditions differ?","acceptedAnswer":{"@type":"Answer","text":"At German public institutions, bachelor programmes and most master programmes normally have no tuition. Baden-Wuerttemberg charges non-EU tuition; Bavarian institutions may also charge. Semester contributions and living costs apply. Full-time Slovak-language study at public institutions normally has no tuition within the standard study duration. English-taught programmes charge tuition. Budget separately for living costs and other fees. Owner-provided conditional guidance. Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility. Do not rely on funding until written award terms confirm eligibility, coverage and payment."}},
        {"@type":"Question","name":"What tuition costs should a Germany applicant check?","acceptedAnswer":{"@type":"Answer","text":"At German public institutions, bachelor programmes and most master programmes normally have no tuition. Baden-Wuerttemberg charges non-EU tuition; Bavarian institutions may also charge. Semester contributions and living costs apply."}},
        {"@type":"Question","name":"What conditional scholarship guidance applies to Italy?","acceptedAnswer":{"@type":"Answer","text":"Owner-provided conditional guidance. Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility. Do not rely on funding until written award terms confirm eligibility, coverage and payment."}},
        {"@type":"Question","name":"How much does it cost to study abroad from India?","acceptedAnswer":{"@type":"Answer","text":"The total cost of studying abroad from India varies widely by country. Budget European destinations like the Czech Republic, Lithuania, Latvia and Russia can cost significantly less per year than the UK, which is among the more expensive options. Your real cost depends on tuition, city, and living expenses; ILMERA gives you a country-by-country breakdown before you decide."}},
        {"@type":"Question","name":"Is studying in Russia good for Indian students with a low budget?","acceptedAnswer":{"@type":"Answer","text":"Yes, Russia is one of the most budget-friendly options for Indian students, with low tuition, affordable living costs, no IELTS requirement, and acceptance of backlogs and low marks. It's a common route for bachelor's and medical (MBBS) programmes. ILMERA helps you shortlist recognised universities and handle the admission and visa process."}},
        {"@type":"Question","name":"Do I need IELTS to study in the UK?","acceptedAnswer":{"@type":"Answer","text":"Most UK universities require IELTS (commonly 5.5–6.5 depending on the course), though some accept a Medium-of-Instruction letter or their own English test. The UK also offers a Graduate visa for post-study work: 2 years for applications on or before 31 December 2026, and 18 months for applications from 1 January 2027, per gov.uk. ILMERA advises whether your profile needs IELTS and which universities may waive it."}},
        {"@type":"Question","name":"Can I count on an Italy scholarship before a written award?","acceptedAnswer":{"@type":"Answer","text":"No. Owner-provided conditional guidance. Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility. Do not rely on funding until written award terms confirm eligibility, coverage and payment."}},
        {"@type":"Question","name":"Which European countries are cheapest and don't require IELTS?","acceptedAnswer":{"@type":"Answer","text":"The Czech Republic, Lithuania, Latvia and Slovakia are among the cheapest European destinations that often don't require IELTS, frequently accepting a Medium-of-Instruction letter or an internal English test instead. These countries also offer lower tuition and living costs than Western Europe. ILMERA confirms the current requirement for each programme before you apply."}},
        {"@type":"Question","name":"Can I study in Lithuania or Latvia after 12th with low marks?","acceptedAnswer":{"@type":"Answer","text":"Yes, Lithuania and Latvia accept Indian students after 12th with modest academic marks, offer English-taught bachelor's programmes, and often don't require IELTS. Tuition and living costs are among the lowest in the EU. ILMERA reviews your marksheet and shortlists programmes that match your profile."}},
        {"@type":"Question","name":"How does teaching language affect tuition in Slovakia?","acceptedAnswer":{"@type":"Answer","text":"Full-time Slovak-language study at public institutions normally has no tuition within the standard study duration. English-taught programmes charge tuition. Budget separately for living costs and other fees."}},
        {"@type":"Question","name":"Can I study in the GCC (UAE, Saudi Arabia, Qatar) as an Indian student?","acceptedAnswer":{"@type":"Answer","text":"Yes, Indian students can study in GCC countries such as the UAE, Saudi Arabia, Qatar, Kuwait, Bahrain and Oman, where cities like Dubai host international branch campuses of UK, US and Australian universities. This suits students who want a globally-recognised degree closer to home or near family working in the Gulf. ILMERA advises on universities, courses and student visas across the GCC."}},
        {"@type":"Question","name":"What is the step-by-step process to study abroad through a consultant?","acceptedAnswer":{"@type":"Answer","text":"The process is: a no-charge profile assessment, country and university shortlisting, application and admission, scholarship or funding guidance, visa documentation and application, then pre-departure preparation. With ILMERA, one counsellor guides you through every stage from first enquiry to arrival, so you always know the next step."}},
        {"@type":"Question","name":"When should I start my study abroad application and how long does it take?","acceptedAnswer":{"@type":"Answer","text":"You should ideally start 6–12 months before your intended intake, because admissions, scholarship deadlines (like Italy's DSU) and visa processing each take time. Starting early gives you the widest choice of universities and funding. ILMERA maps your timeline backwards from your target intake so you don't miss deadlines."}},
        {"@type":"Question","name":"What is ILMERA Study Abroad and is it legitimate?","acceptedAnswer":{"@type":"Answer","text":"ILMERA Study Abroad is an Indian study abroad consultancy, part of the ILMERA Group, based in Coorg, Kodagu, Karnataka, that guides students to universities in Germany, Italy, the UK, Czech Republic, Lithuania, Latvia, Slovakia, Russia and the GCC. It is led by a named, contactable team: Founder Jabir KJ, CMO Fawaz BH and CFO Zaheer KJ, and offers a no-charge initial consultation with honest eligibility advice rather than guaranteed-admission promises."}},
        {"@type":"Question","name":"How is ILMERA different from other study abroad consultants?","acceptedAnswer":{"@type":"Answer","text":"ILMERA is based in Coorg, Kodagu, and offers counselling by phone, WhatsApp and video call. Discuss your academic record, budget and course preferences before choosing an application route."}},
        {"@type":"Question","name":"Is there a study abroad consultant for students from Coorg and Kodagu?","acceptedAnswer":{"@type":"Answer","text":"Yes. ILMERA Study Abroad is based in Coorg and works with students from Kodagu and across Karnataka by phone, WhatsApp and video call. ILMERA counselling is online only; these channels do not involve travel to counselling premises. The full process, profile assessment, university shortlisting, admissions and visa support, covers Germany, Italy, the UK, Russia and other European destinations. Book a no-charge consultation to start from anywhere in Kodagu."}}
      ]
    },

    {
      "@type": "ItemList",
      "@id": "https://ilmerastudyabroad.com/#destinations",
      "name": "Study Abroad Destinations",
      "itemListElement": [
                {"@type":"ListItem","position":1,"name":"Study in Germany","url":<?= json_encode('https://ilmerastudyabroad.com' . ilmera_destination_target('germany'), JSON_UNESCAPED_SLASHES | JSON_HEX_TAG | JSON_HEX_AMP) ?>},
        {"@type":"ListItem","position":2,"name":"Study in Italy","url":<?= json_encode('https://ilmerastudyabroad.com' . ilmera_destination_target('italy'), JSON_UNESCAPED_SLASHES | JSON_HEX_TAG | JSON_HEX_AMP) ?>},
        {"@type":"ListItem","position":3,"name":"Study in the UK","url":<?= json_encode('https://ilmerastudyabroad.com' . ilmera_destination_target('uk'), JSON_UNESCAPED_SLASHES | JSON_HEX_TAG | JSON_HEX_AMP) ?>},
        {"@type":"ListItem","position":4,"name":"Study in Czech Republic","url":<?= json_encode('https://ilmerastudyabroad.com' . ilmera_destination_target('czech-republic'), JSON_UNESCAPED_SLASHES | JSON_HEX_TAG | JSON_HEX_AMP) ?>},
        {"@type":"ListItem","position":5,"name":"Study in Lithuania","url":<?= json_encode('https://ilmerastudyabroad.com' . ilmera_destination_target('lithuania'), JSON_UNESCAPED_SLASHES | JSON_HEX_TAG | JSON_HEX_AMP) ?>},
        {"@type":"ListItem","position":6,"name":"Study in Latvia","url":<?= json_encode('https://ilmerastudyabroad.com' . ilmera_destination_target('latvia'), JSON_UNESCAPED_SLASHES | JSON_HEX_TAG | JSON_HEX_AMP) ?>},
        {"@type":"ListItem","position":7,"name":"Study in Slovakia","url":<?= json_encode('https://ilmerastudyabroad.com' . ilmera_destination_target('slovakia'), JSON_UNESCAPED_SLASHES | JSON_HEX_TAG | JSON_HEX_AMP) ?>},
        {"@type":"ListItem","position":8,"name":"Study in Russia","url":<?= json_encode('https://ilmerastudyabroad.com' . ilmera_destination_target('russia'), JSON_UNESCAPED_SLASHES | JSON_HEX_TAG | JSON_HEX_AMP) ?>},
        {"@type":"ListItem","position":9,"name":"Study in GCC Countries","url":<?= json_encode('https://ilmerastudyabroad.com' . ilmera_destination_target('gcc'), JSON_UNESCAPED_SLASHES | JSON_HEX_TAG | JSON_HEX_AMP) ?>}

      ]
    }
  ]
}
</script>

<style>
:root{
  --void:#04060f;--deep-navy:#0a1628;--navy:#1A2E5A;
  --cool-white:#F0F4FF;--white:#FFFFFF;--grey-mid:#8A98B8;--grey-dark:#4A5568;--grey-light:#E8EDF5;
  --silver:#C8D3E8;--gold:#C9A84C;--gold-glow:rgba(201,168,76,0.3);
  --glass-fill:rgba(255,255,255,0.05);--glass-border:rgba(255,255,255,0.10);
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:'Outfit',sans-serif;font-weight:300;color:var(--white);background:var(--void);overflow-x:hidden;}

/* ─── CURSOR ─────────────────────────────────────── */
#cur-dot{position:fixed;width:6px;height:6px;background:var(--gold);border-radius:50%;pointer-events:none;z-index:9999;transform:translate(-50%,-50%);transition:width .15s,height .15s,background .2s;}
#cur-ring{position:fixed;width:32px;height:32px;border:1px solid rgba(201,168,76,0.5);border-radius:50%;pointer-events:none;z-index:9998;transform:translate(-50%,-50%);transition:width .3s,height .3s,border-color .3s;}
#cur-dot.hov{width:10px;height:10px;background:#fff;}
#cur-ring.hov{width:50px;height:50px;border-color:var(--gold);}
@media(max-width:1024px){#cur-dot,#cur-ring{display:none!important;}}

/* ─── BACKGROUND CANVAS ──────────────────────────── */
#space-canvas{position:fixed;inset:0;z-index:0;display:block;}

/* ─── CSS OVERLAY LAYERS ─────────────────────────── */
#vignette{position:fixed;inset:0;z-index:1;pointer-events:none;background:radial-gradient(ellipse at 50% 50%,transparent 30%,rgba(4,6,15,0.85) 100%);}
#nebula-t{position:fixed;top:-20vh;left:-10vw;width:70vw;height:70vh;z-index:1;pointer-events:none;background:radial-gradient(ellipse,rgba(26,46,90,0.55) 0%,transparent 70%);filter:blur(60px);animation:nebulaD 18s ease-in-out infinite alternate;}
#nebula-b{position:fixed;bottom:-20vh;right:-10vw;width:60vw;height:60vh;z-index:1;pointer-events:none;background:radial-gradient(ellipse,rgba(13,27,62,0.5) 0%,transparent 70%);filter:blur(80px);animation:nebulaD 24s ease-in-out infinite alternate-reverse;}
#gold-shimmer{position:fixed;top:20%;left:30%;width:40vw;height:40vh;z-index:1;pointer-events:none;background:radial-gradient(ellipse,rgba(201,168,76,0.06) 0%,transparent 65%);filter:blur(50px);animation:shimmerPulse 8s ease-in-out infinite;}
@keyframes nebulaD{0%{transform:translate(0,0) scale(1);}100%{transform:translate(40px,30px) scale(1.12);}}
@keyframes shimmerPulse{0%,100%{opacity:.5;transform:scale(1);}50%{opacity:1;transform:scale(1.15);}}
#grain{position:fixed;inset:0;z-index:2;pointer-events:none;opacity:.028;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='250' height='250'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='250' height='250' filter='url(%23n)'/%3E%3C/svg%3E");background-repeat:repeat;}

/* Floating CSS educational elements */
#float-layer{position:fixed;inset:0;z-index:2;pointer-events:none;overflow:hidden;}
.f-elem{position:absolute;pointer-events:none;opacity:0;animation:floatUp linear infinite;}
@keyframes floatUp{0%{opacity:0;transform:translateY(0) rotate(0deg);}10%{opacity:.7;}85%{opacity:.5;}100%{opacity:0;transform:translateY(-110vh) rotate(720deg);}}

/* ─── HERO ───────────────────────────────────────── */
#hero{position:relative;min-height:100vh;display:flex;align-items:center;justify-content:center;z-index:10;overflow:hidden;}
.hero-inner{text-align:center;max-width:720px;padding:120px 24px 80px;position:relative;z-index:10;}
.hero-label{display:inline-block;font-size:11px;font-weight:300;letter-spacing:.4em;text-transform:uppercase;color:var(--gold);border:1px solid rgba(201,168,76,0.3);padding:6px 16px;border-radius:2px;margin-bottom:30px;}
.hero-h1{font-family:'Cormorant Garamond',serif;font-size:76px;font-weight:700;line-height:1.06;color:var(--white);margin-bottom:26px;}
.hero-h1 em{font-style:italic;color:rgba(240,244,255,0.85);display:block;}
.hero-sub{font-size:18px;font-weight:300;line-height:1.75;color:var(--grey-mid);max-width:580px;margin:0 auto 38px;}
.hero-btns{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-bottom:52px;}
.btn-gold{font-size:13px;font-weight:500;text-transform:uppercase;letter-spacing:.1em;background:var(--gold);color:var(--void);border:none;padding:16px 36px;border-radius:3px;cursor:pointer;transition:background .3s,box-shadow .3s,transform .2s;text-decoration:none;display:inline-block;}
.btn-gold:hover{background:#d4b05a;box-shadow:0 0 40px var(--gold-glow);transform:translateY(-2px);}
.btn-ghost{font-size:13px;font-weight:500;text-transform:uppercase;letter-spacing:.1em;background:transparent;color:var(--white);border:1px solid rgba(255,255,255,0.2);padding:16px 36px;border-radius:3px;cursor:pointer;transition:background .3s,border-color .3s,transform .2s;text-decoration:none;display:inline-block;}
.btn-ghost:hover{background:rgba(255,255,255,0.06);border-color:rgba(255,255,255,0.4);transform:translateY(-2px);}
.hero-div{width:40px;height:1px;background:rgba(255,255,255,0.12);margin:0 auto 30px;}
.hero-stats{display:flex;justify-content:center;}
.hero-stat{flex:1;text-align:center;padding:0 22px;border-right:1px solid rgba(255,255,255,0.08);}
.hero-stat:last-child{border-right:none;}
.stat-num{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:38px;color:var(--white);display:block;line-height:1;margin-bottom:7px;}
.stat-lbl{font-size:10px;font-weight:300;color:var(--grey-mid);text-transform:uppercase;letter-spacing:.18em;}
.scroll-ind{position:absolute;bottom:24px;left:50%;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;gap:8px;z-index:10;transition:opacity .6s;}
.scroll-ind span{font-size:10px;color:rgba(138,152,184,0.7);letter-spacing:.25em;text-transform:uppercase;}
.scroll-arr{width:18px;height:18px;border-right:1px solid rgba(138,152,184,0.5);border-bottom:1px solid rgba(138,152,184,0.5);transform:rotate(45deg);animation:bounce 1.8s ease-in-out infinite;}
@keyframes bounce{0%,100%{transform:rotate(45deg) translateY(0);}50%{transform:rotate(45deg) translateY(6px);}}
@media(max-width:768px){
  .hero-inner{padding:100px 20px 60px;}
  .hero-h1{font-size:38px;}.hero-sub{font-size:15px;}
  .hero-label{font-size:10px;letter-spacing:.25em;margin-bottom:22px;}
  .hero-btns{margin-bottom:40px;}
  .btn-gold,.btn-ghost{width:100%;max-width:300px;text-align:center;}
  .hero-stats{flex-wrap:wrap;gap:0;}
  .hero-stat{flex:0 0 50%;border-right:none;border-bottom:1px solid rgba(255,255,255,0.08);padding:16px 8px;}
  .hero-stat:nth-child(odd){border-right:1px solid rgba(255,255,255,0.08);}
  .hero-stat:nth-child(3),.hero-stat:nth-child(4){border-bottom:none;}
  .stat-num{font-size:30px;}
  .scroll-ind{display:none;}
}
@media(min-width:1440px){.hero-h1{font-size:90px;}}

/* ─── MARQUEE ─────────────────────────────────────── */
.marquee-strip{position:relative;z-index:10;background:rgba(13,27,62,0.6);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-top:1px solid rgba(255,255,255,0.05);border-bottom:1px solid rgba(255,255,255,0.05);padding:16px 0;overflow:hidden;}
.marquee-track{display:flex;width:max-content;animation:marquee 25s linear infinite;}
.marquee-inner{display:flex;align-items:center;}
.mq-item{font-size:13px;font-weight:300;color:var(--silver);letter-spacing:.18em;text-transform:uppercase;padding:0 32px;white-space:nowrap;}
.mq-div{color:var(--gold);font-size:12px;opacity:.6;}
@keyframes marquee{0%{transform:translateX(0);}100%{transform:translateX(-50%);}}
@media(max-width:768px){.mq-item{padding:0 20px;font-size:12px;}}

/* ─── WHY SECTION ─────────────────────────────────── */
.why-sec{position:relative;z-index:10;padding:130px 0;background:rgba(240,244,255,0.97);}
.why-hdr{text-align:center;margin-bottom:64px;}
.sec-label{font-size:11px;font-weight:300;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);margin-bottom:16px;display:block;}
.sec-h2{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:48px;line-height:1.15;margin-bottom:0;}
.sec-h2.dk{color:var(--deep-navy);}.sec-h2.lt{color:var(--white);}
@media(max-width:768px){.sec-h2{font-size:30px;}}
.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;max-width:1100px;margin:0 auto;}
.container{max-width:1200px;margin:0 auto;padding:0 60px;}
@media(max-width:768px){.container{padding:0 20px;}}
.why-card{background:#fff;padding:48px 36px;border-radius:14px;border:1px solid #E8EDF5;box-shadow:0 4px 40px rgba(10,22,40,0.08);transition:transform .35s,box-shadow .35s,border-color .35s;cursor:default;will-change:transform;position:relative;overflow:hidden;}
.why-card:hover{transform:translateY(-10px);box-shadow:0 20px 60px rgba(10,22,40,0.15);border-color:rgba(201,168,76,0.3);}
.why-icon{width:48px;height:48px;margin-bottom:24px;color:var(--gold);}
.why-card h3{font-size:20px;font-weight:600;color:var(--deep-navy);margin-bottom:12px;}
.why-card p{font-size:15px;font-weight:300;color:var(--grey-dark);line-height:1.7;}
@media(max-width:768px){.why-grid{grid-template-columns:1fr;}.why-sec{padding:80px 0;}.why-card{padding:36px 28px;}}
@media(min-width:769px) and (max-width:1024px){.why-grid{grid-template-columns:1fr 1fr;}}

/* STUDY ROUTES */
.testi-sec{position:relative;z-index:10;padding:130px 0;background:rgba(4,6,15,0.97);}
.testi-hdr{text-align:center;margin-bottom:64px;}
.testi-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;max-width:1100px;margin:0 auto;}
.testi-card{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);padding:40px;border-radius:16px;position:relative;overflow:hidden;transition:transform .35s,border-color .35s;}
.testi-card:hover{transform:translateY(-6px);border-color:rgba(201,168,76,0.3);}
.testi-text{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:18px;color:var(--grey-mid);line-height:1.7;margin-bottom:24px;position:relative;z-index:1;}
.testi-name{font-size:16px;font-weight:600;color:var(--white);margin-bottom:4px;}
.testi-dest{font-size:13px;font-weight:300;color:var(--gold);}
@media(max-width:768px){.testi-grid{grid-template-columns:1fr;}.testi-sec{padding:80px 0;}.testi-card{padding:32px 26px;}}
@media(min-width:769px) and (max-width:1024px){.testi-grid{grid-template-columns:1fr 1fr;}}

/* ─── SPECIAL CARDS ───────────────────────────────── */
.s-wrap{background:rgba(240,244,255,0.97);padding:80px 0 100px;position:relative;z-index:10;}
.special-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:24px;max-width:900px;margin:0 auto;}
.special-card{background:#fff;border:1px solid var(--grey-light);border-radius:14px;padding:28px 24px;box-shadow:0 4px 30px rgba(10,22,40,0.07);transition:transform .3s,box-shadow .3s;}
.special-card:hover{transform:translateY(-6px);box-shadow:0 16px 50px rgba(10,22,40,0.13);}
.sc-badge{display:inline-block;font-size:11px;font-weight:600;letter-spacing:.08em;padding:5px 14px;border-radius:20px;border:1px solid;margin-bottom:14px;}
.sc-title{font-size:18px;font-weight:600;color:var(--deep-navy);margin-bottom:16px;}
.sc-list{display:flex;flex-direction:column;gap:10px;}
.sc-item{display:flex;align-items:flex-start;gap:12px;font-size:14px;font-weight:300;color:var(--grey-dark);line-height:1.5;}
.sc-rank{min-width:28px;height:28px;border-radius:50%;background:var(--deep-navy);color:#fff;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:600;flex-shrink:0;}
@media(max-width:768px){.special-grid{grid-template-columns:1fr;}.special-card{padding:24px 20px;}.s-wrap{padding:60px 0 70px;}}

/* ─── CTA ────────────────────────────────────────── */
.cta-sec{position:relative;z-index:10;padding:110px 0;text-align:center;background:linear-gradient(135deg,rgba(13,27,62,0.98) 0%,rgba(4,6,15,0.98) 100%);overflow:hidden;}
.cta-beam{position:absolute;top:0;left:50%;width:2px;height:100%;background:linear-gradient(to bottom,transparent,rgba(201,168,76,0.15),transparent);animation:beamSw 10s ease-in-out infinite alternate;transform-origin:top center;}
@keyframes beamSw{0%{transform:translateX(-50%) rotate(-18deg) scaleX(80);}100%{transform:translateX(-50%) rotate(18deg) scaleX(80);}}
.cta-h2{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:54px;color:var(--white);margin-bottom:16px;position:relative;}
.cta-sub{font-size:17px;font-weight:300;color:var(--grey-mid);margin-bottom:40px;position:relative;}
@media(max-width:768px){.cta-h2{font-size:32px;}.cta-sec{padding:80px 0;}.cta-sub{font-size:15px;}}

/* ANIMATIONS */
.reveal,.reveal-l,.reveal-r{}
.anim-fade-up{opacity:0;transform:translateY(60px);transition:opacity .8s ease,transform .8s ease;}
.anim-fade-left{opacity:0;transform:translateX(-60px);transition:opacity .8s ease,transform .8s ease;}
.anim-fade-right{opacity:0;transform:translateX(60px);transition:opacity .8s ease,transform .8s ease;}
.anim-scale-in{opacity:0;transform:scale(0.88);transition:opacity .7s ease,transform .7s ease;}
.anim-visible{opacity:1!important;transform:none!important;}
.why-card::before,.testi-card::before{content:'';position:absolute;inset:0;border-radius:inherit;background:linear-gradient(135deg,transparent 0%,rgba(201,168,76,0.04) 50%,transparent 100%);opacity:0;transition:opacity .4s ease;pointer-events:none;}
.why-card:hover::before,.testi-card:hover::before{opacity:1;}
#scroll-progress{position:fixed;top:0;left:0;width:0%;height:2px;background:linear-gradient(90deg,var(--gold),rgba(201,168,76,0.4));z-index:9999;transition:width .1s linear;pointer-events:none;}
.il-faq{background:#fff;border:1px solid #E8EDF5;border-radius:12px;margin-bottom:14px;box-shadow:0 4px 30px rgba(10,22,40,0.06);overflow:hidden;transition:border-color .3s;}
.il-faq[open]{border-color:rgba(201,168,76,0.4);}
.il-faq summary{list-style:none;cursor:pointer;padding:22px 26px;font-family:'Outfit',sans-serif;font-size:17px;font-weight:500;color:var(--deep-navy);display:flex;justify-content:space-between;align-items:center;gap:16px;}
.il-faq summary::-webkit-details-marker{display:none;}
.il-faq summary::after{content:'+';font-size:24px;font-weight:300;color:var(--gold);transition:transform .3s;flex-shrink:0;}
.il-faq[open] summary::after{transform:rotate(45deg);}
.il-faq summary:hover{color:#8a6a00;}
.il-faq > div{padding:0 26px 24px;}
.il-faq > div p{font-size:15px;font-weight:300;color:var(--grey-dark);line-height:1.75;margin:0;}
@media(max-width:768px){.il-faq summary{font-size:15px;padding:18px 20px;}.il-faq > div{padding:0 20px 20px;}}
.breadcrumb{font-size:13px;font-weight:300;color:var(--grey-mid);margin-bottom:20px;}
.breadcrumb a{color:var(--grey-mid);text-decoration:none;}
</style>

</head>
<body>

<?php include __DIR__ . '/includes/header.php'; ?>

<!-- BACKGROUND -->
<canvas id="space-canvas" aria-hidden="true" role="presentation"></canvas>
<div id="vignette" aria-hidden="true"></div>
<div id="nebula-t" aria-hidden="true"></div>
<div id="nebula-b" aria-hidden="true"></div>
<div id="gold-shimmer" aria-hidden="true"></div>
<div id="grain" aria-hidden="true"></div>
<div id="float-layer" aria-hidden="true"></div>


<main>
<!-- ═══ HERO ═══ -->
<section id="hero">
  <div class="hero-inner">
    <?php ilmera_breadcrumbs($pageTrail, '/'); ?>
    <div class="hero-label" id="hLabel">ILMERA GROUP PRESENTS</div>
       <h1 class="hero-h1" id="hH1">Study Abroad from India<em>Germany · Italy · UK · Russia &amp; Europe</em></h1>
        <p class="hero-sub" id="hSub">Compare programme-specific tuition, living costs and scholarship conditions before choosing a destination. No award or admission outcome is guaranteed.</p>
    <div class="hero-btns" id="hBtns">
          <a href="/services" class="btn-gold">Explore Study Destinations</a>
      <a href="/contact" class="btn-ghost">Book no-charge Consultation</a>
    </div>
    <div class="hero-div" id="hDiv"></div>
    <div class="hero-stats" id="hStats">
                  <div class="hero-stat"><span class="stat-num" data-target="9" data-suffix="">9</span><span class="stat-lbl">Study Destinations</span></div>
      <div class="hero-stat"><span class="stat-num" data-target="3" data-suffix="">3</span><span class="stat-lbl">Named Counsellors</span></div>
      <div class="hero-stat"><span class="stat-num" data-target="4" data-suffix="">4</span><span class="stat-lbl">Languages Spoken</span></div>
                  <div class="hero-stat"><span class="stat-num" data-target="2026" data-suffix="">2026</span><span class="stat-lbl">Founded</span></div>

    </div>
  </div>
  <div class="scroll-ind" id="scrollInd"><span>Explore</span><div class="scroll-arr"></div></div>
</section>

<!-- MARQUEE -->
<div class="marquee-strip">
  <div class="marquee-track">
    <div class="marquee-inner">
      <span class="mq-item">&#127465;&#127466; Germany</span><span class="mq-div">&#10022;</span>
      <span class="mq-item">&#127470;&#127481; Italy</span><span class="mq-div">&#10022;</span>
      <span class="mq-item">&#127468;&#127463; United Kingdom</span><span class="mq-div">&#10022;</span>
      <span class="mq-item">&#127464;&#127487; Czech Republic</span><span class="mq-div">&#10022;</span>
      <span class="mq-item">&#127473;&#127481; Lithuania</span><span class="mq-div">&#10022;</span>
      <span class="mq-item">&#127473;&#127483; Latvia</span><span class="mq-div">&#10022;</span>
      <span class="mq-item">&#127480;&#127472; Slovakia</span><span class="mq-div">&#10022;</span>
      <span class="mq-item">&#127479;&#127482; Russia</span><span class="mq-div">&#10022;</span>
      <span class="mq-item">&#127760; GCC Countries</span><span class="mq-div">&#10022;</span>
    </div>
    <div class="marquee-inner" aria-hidden="true">
      <span class="mq-item">&#127465;&#127466; Germany</span><span class="mq-div">&#10022;</span>
      <span class="mq-item">&#127470;&#127481; Italy</span><span class="mq-div">&#10022;</span>
      <span class="mq-item">&#127468;&#127463; United Kingdom</span><span class="mq-div">&#10022;</span>
      <span class="mq-item">&#127464;&#127487; Czech Republic</span><span class="mq-div">&#10022;</span>
      <span class="mq-item">&#127473;&#127481; Lithuania</span><span class="mq-div">&#10022;</span>
      <span class="mq-item">&#127473;&#127483; Latvia</span><span class="mq-div">&#10022;</span>
      <span class="mq-item">&#127480;&#127472; Slovakia</span><span class="mq-div">&#10022;</span>
      <span class="mq-item">&#127479;&#127482; Russia</span><span class="mq-div">&#10022;</span>
      <span class="mq-item">&#127760; GCC Countries</span><span class="mq-div">&#10022;</span>
    </div>
  </div>
</div>

<!-- STATUS-DRIVEN DESTINATION LINKS -->
<?php $homeDestinations = ilmera_published_destinations(); if ($homeDestinations): ?>
<section style="position:relative;z-index:10;background:rgba(4,6,15,0.97);padding:60px 0;">
  <div class="container">
    <h2 class="sec-h2 lt reveal" style="text-align:center;font-size:34px;margin-bottom:36px;">Choose Your Study Destination</h2>
    <div style="display:flex;flex-wrap:wrap;gap:12px;justify-content:center;max-width:900px;margin:0 auto;">
<?php foreach ($homeDestinations as $destinationGuide): ?>
      <?= ilmera_link($destinationGuide['url'], $destinationGuide['name'], ['class' => 'btn-ghost']) ?>
<?php endforeach; ?>
    </div>
  </div>
</section>
<?php endif; ?>
<div class="container"><?php ilmera_discovery_links(ilmera_indexable_locations(), 'Locations we support'); ?></div>

<!-- SERVICE AREA: COORG / KODAGU (service-area business, no physical office claimed) -->
<section class="s-wrap" id="coorg-kodagu">
  <div class="container">
    <div style="text-align:center;margin-bottom:40px;">
      <span class="sec-label">Serving Students Across Karnataka</span>
      <h2 class="sec-h2 dk reveal">Study Abroad Guidance for Coorg &amp; Kodagu Students</h2>
    </div>
    <div style="max-width:820px;margin:0 auto;text-align:center;">
      <p style="font-size:16px;font-weight:300;color:var(--grey-dark);line-height:1.8;">
        ILMERA Study Abroad is based in Coorg and helps students from Kodagu, Madikeri, Virajpet and across Karnataka plan their overseas education through conditional consultation by phone, WhatsApp and video call. Whether you're aiming for conditional tuition in Germany, the DSU scholarship in Italy, or a low-cost, no-IELTS route in Russia, Lithuania or Latvia, our named counsellors guide you from profile assessment to visa.
      </p>
      <p style="font-size:15px;font-weight:300;color:var(--grey-dark);line-height:1.8;margin-top:16px;">
        Students from Kodagu often have strong academics but limited access to specialised study-abroad advice locally. ILMERA closes that gap: you get the same country-by-country cost breakdowns, eligibility checks (including for backlogs and low marks), and honest guidance that students in Bangalore or Mangalore receive, from wherever you are in Coorg.
      </p>
      <p style="font-size:13px;font-weight:300;color:var(--grey-mid);line-height:1.7;margin-top:14px;">ILMERA operates online only, by phone, WhatsApp and video call, with no counselling premises. Your own visa appointment may take place at the relevant consulate or VFS centre.</p>
      <a href="/contact" class="btn-gold reveal" style="margin-top:28px;">Book a no-charge Online Consultation</a>
    </div>
  </div>
</section>

<!-- WHY ILMERA -->
<section class="why-sec">
  <div class="container">
    <div class="why-hdr">
      <span class="sec-label">Why Choose Us</span>
      <h2 class="sec-h2 dk reveal">Why Indian Students Choose ILMERA</h2>
    </div>
    <div class="why-grid">
                 <article class="why-card reveal">
        <svg class="why-icon" aria-hidden="true" focusable="false" viewBox="0 0 48 48" fill="none"><circle cx="24" cy="24" r="10" stroke="currentColor" stroke-width="1.5"/><line x1="24" y1="4" x2="24" y2="14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><line x1="24" y1="34" x2="24" y2="44" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><line x1="4" y1="24" x2="14" y2="24" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><line x1="34" y1="24" x2="44" y2="24" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><circle cx="24" cy="24" r="3" fill="currentColor"/></svg>
                <h3>A Named Team, Not Faceless Agents</h3>
        <p>You work with real, named people, Founder Jabir KJ, CFO Zaheer KJ and CMO Fawaz BH, who specialise in matching each student's marks, budget and goals to the right country and university. Meet the team below.</p>
      </article>
      <article class="why-card reveal">
        <svg class="why-icon" viewBox="0 0 48 48" fill="none"><path d="M8 24 C8 14 14 8 24 8 C34 8 40 14 40 24" stroke="currentColor" stroke-width="1.5" fill="none"/><path d="M8 24 C8 34 14 40 24 40 C34 40 40 34 40 24" stroke="currentColor" stroke-width="1.5" fill="none" stroke-dasharray="4 2"/><circle cx="8" cy="24" r="3" fill="currentColor"/><circle cx="24" cy="8" r="3" fill="currentColor"/><circle cx="40" cy="24" r="3" fill="currentColor"/><circle cx="24" cy="40" r="3" fill="currentColor"/></svg>
        <h3>End-to-End Support</h3>
        <p>ILMERA offers guidance on admissions, visas, scholarships and pre-departure preparation, starting with your enquiry.</p>
      </article>
      <article class="why-card reveal">
        <svg class="why-icon" viewBox="0 0 48 48" fill="none"><polygon points="24,4 29,18 44,18 32,27 37,42 24,33 11,42 16,27 4,18 19,18" stroke="currentColor" stroke-width="1.5" fill="none"/><circle cx="24" cy="24" r="5" fill="currentColor" opacity="0.25"/></svg>
                <h3>Personalised, Honest Guidance</h3>
        <p>Every student gets a counsellor who maps their exact marks, budget and goals to the right country and university, and tells them honestly when a route won't work. No false promises, no hidden agents.</p>
      </article>
    </div>
  </div>
</section>

<!-- STUDY ROUTES -->
<section class="testi-sec">
  <div class="container">
    <div class="testi-hdr">
            <span class="sec-label">How We Help</span>
      <h2 class="sec-h2 lt reveal">Study Routes ILMERA Guides</h2>
    </div>
    <div class="testi-grid">
            <article class="testi-card reveal-r">
        <p class="testi-text">We guide students toward destinations that fit their goals, like the UK's Graduate visa: 2 years of post-study work for applications on or before 31 December 2026, and 18 months from 1 January 2027, per gov.uk.</p>
        <div class="testi-name">What ILMERA Helps With</div>
        <div class="testi-dest">&#127468;&#127463; United Kingdom: Admissions &amp; Visa</div>
      </article>
      <article class="testi-card reveal-r">
        <p class="testi-text">Owner-provided conditional guidance. Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility. Do not rely on funding until written award terms confirm eligibility, coverage and payment.</p>
        <div class="testi-name">What ILMERA Helps With</div>
        <div class="testi-dest">&#127470;&#127481; Italy: Conditional Scholarship Guidance</div>
      </article>
      <article class="testi-card reveal-r">
        <p class="testi-text">For students with backlogs or a low percentage, we discuss low-cost, no-IELTS bachelor's routes in Russia and other budget-friendly countries where such profiles are accepted.</p>
        <div class="testi-name">What ILMERA Helps With</div>
        <div class="testi-dest">&#127479;&#127482; Russia: Backlogs &amp; No-IELTS Routes</div>
      </article>
    </div>
  </div>
</section>

<!-- SPECIAL CATEGORIES -->
<section class="s-wrap">
  <div class="container">
    <div style="text-align:center;margin-bottom:56px;">
      <span class="sec-label">We Have A Path For Everyone</span>
      <h2 class="sec-h2 dk reveal">No Barrier Too Big</h2>
    </div>
    <div class="special-grid">
      <div class="special-card reveal-l">
        <div class="sc-badge" style="background:rgba(220,0,0,0.08);border-color:rgba(200,0,0,0.3);color:#cc0000;">&#128201; Low Marks? No Problem!</div>
        <h3 class="sc-title">Low Marks Accepted</h3>
        <div class="sc-list">
          <div class="sc-item"><span class="sc-rank">1</span><span>&#127479;&#127482; Russia</span></div>
          <div class="sc-item"><span class="sc-rank">2</span><span>&#127480;&#127472; Slovakia</span></div>
          <div class="sc-item"><span class="sc-rank">3</span><span>&#127473;&#127481; Lithuania</span></div>
          <div class="sc-item"><span class="sc-rank">4</span><span>&#127473;&#127483; Latvia</span></div>
        </div>
      </div>
      <div class="special-card reveal-r">
        <div class="sc-badge" style="background:rgba(0,100,0,0.08);border-color:rgba(0,150,0,0.3);color:#006400;">&#128184; Lowest Tuition Fees</div>
        <h3 class="sc-title">Most Affordable Destinations</h3>
        <div class="sc-list">
          <div class="sc-item"><span class="sc-rank">1</span><span>&#127464;&#127487; Czech Republic</span></div>
          <div class="sc-item"><span class="sc-rank">2</span><span>&#127473;&#127481; Lithuania</span></div>
          <div class="sc-item"><span class="sc-rank">3</span><span>&#127473;&#127483; Latvia</span></div>
          <div class="sc-item"><span class="sc-rank">4</span><span>&#127479;&#127482; Russia</span></div>
          <div class="sc-item"><span class="sc-rank">5</span><span>&#127480;&#127472; Slovakia <em style="font-size:11px;color:#888;">(conditional in some branches)</em></span></div>
        </div>
      </div>
      <div class="special-card reveal-l">
        <div class="sc-badge" style="background:rgba(201,168,76,0.1);border-color:rgba(201,168,76,0.4);color:#8a6a00;">&#127379; Language-based tuition rules</div>
        <h3 class="sc-title">Plan Study Funding</h3>
        <div class="sc-list">
          <div class="sc-item"><span class="sc-rank">&#127465;&#127466;</span><span>At German public institutions, bachelor programmes and most master programmes normally have no tuition. Baden-Wuerttemberg charges non-EU tuition; Bavarian institutions may also charge. Semester contributions and living costs apply.</span></div>
          <div class="sc-item"><span class="sc-rank">&#127470;&#127481;</span><span>Owner-provided conditional guidance. Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility. Do not rely on funding until written award terms confirm eligibility, coverage and payment.</span></div>
          <div class="sc-item"><span class="sc-rank">&#127480;&#127472;</span><span>Full-time Slovak-language study at public institutions normally has no tuition within the standard study duration. English-taught programmes charge tuition. Budget separately for living costs and other fees.</span></div>
        </div>
      </div>
      <div class="special-card reveal-r">
        <div class="sc-badge" style="background:rgba(100,0,0,0.08);border-color:rgba(150,0,0,0.3);color:#8b0000;">&#128196; Backlogs Accepted</div>
        <h3 class="sc-title">Academic Backlogs?</h3>
        <div class="sc-list">
          <div class="sc-item"><span class="sc-rank">&#127479;&#127482;</span><span>Russia: backlogs accepted at many universities, low fees, no IELTS needed.</span></div>
        </div>
        <p style="font-size:13px;color:var(--grey-dark);margin-top:14px;line-height:1.65;">Have academic backlogs? Russia is a practical option, with accessible fees and no IELTS requirement at many universities.</p>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="why-sec" id="faq" style="padding:110px 0;">
  <div class="container">
    <div class="why-hdr">
      <span class="sec-label">Answers For Indian Students</span>
      <h2 class="sec-h2 dk reveal">Study Abroad FAQs (2026)</h2>
    </div>
    <div style="max-width:820px;margin:0 auto;">

      <details class="il-faq"><summary>Can I study abroad if I have academic backlogs?</summary><div><p>In many cases, yes. Russia is a route students with academic backlogs can discuss with ILMERA, with low tuition fees and no IELTS requirement at many universities. Eligibility depends on your specific marksheet, so ILMERA reviews each profile before applying.</p></div></details>

      <details class="il-faq"><summary>Can I study abroad with low marks or a low percentage?</summary><div><p>Yes, students with low marks can study abroad. Russia, Slovakia, Lithuania and Latvia have universities with more accessible entry requirements than many universities in the UK or US. ILMERA reviews your specific percentage and matches you to countries and universities suited to your profile.</p></div></details>

      <details class="il-faq"><summary>Can I study abroad without IELTS?</summary><div><p>Yes, you can study abroad without IELTS in several countries. Russia and Lithuania commonly waive IELTS, and many programmes in Latvia, Slovakia and the Czech Republic accept a Medium-of-Instruction (MOI) letter or an internal English test instead. Germany also frequently waives IELTS when your prior education was in English.</p></div></details>

      <details class="il-faq"><summary>How should I compare total study budgets?</summary><div><p>Full-time Slovak-language study at public institutions normally has no tuition within the standard study duration. English-taught programmes charge tuition. Budget separately for living costs and other fees.</p></div></details>

      <details class="il-faq"><summary>How do tuition and scholarship conditions differ?</summary><div><p>At German public institutions, bachelor programmes and most master programmes normally have no tuition. Baden-Wuerttemberg charges non-EU tuition; Bavarian institutions may also charge. Semester contributions and living costs apply. Full-time Slovak-language study at public institutions normally has no tuition within the standard study duration. English-taught programmes charge tuition. Budget separately for living costs and other fees. Owner-provided conditional guidance. Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility. Do not rely on funding until written award terms confirm eligibility, coverage and payment.</p></div></details>

      <details class="il-faq"><summary>What tuition costs should a Germany applicant check?</summary><div><p>At German public institutions, bachelor programmes and most master programmes normally have no tuition. Baden-Wuerttemberg charges non-EU tuition; Bavarian institutions may also charge. Semester contributions and living costs apply.</p></div></details>

      <details class="il-faq"><summary>What conditional scholarship guidance applies to Italy?</summary><div><p>Owner-provided conditional guidance. Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility. Do not rely on funding until written award terms confirm eligibility, coverage and payment.</p></div></details>

      <details class="il-faq"><summary>How much does it cost to study abroad from India?</summary><div><p>The total cost of studying abroad from India varies widely by country. Budget European destinations like the Czech Republic, Lithuania, Latvia and Russia can cost significantly less per year than the UK, which is among the more expensive options. Your real cost depends on tuition, city, and living expenses; ILMERA gives you a country-by-country breakdown before you decide.</p></div></details>

      <details class="il-faq"><summary>Is studying in Russia good for Indian students with a low budget?</summary><div><p>Yes, Russia is one of the most budget-friendly options for Indian students, with low tuition, affordable living costs, no IELTS requirement, and acceptance of backlogs and low marks. It's a common route for bachelor's and medical (MBBS) programmes. ILMERA helps you shortlist recognised universities and handle the admission and visa process.</p></div></details>

      <details class="il-faq"><summary>Do I need IELTS to study in the UK?</summary><div><p>Most UK universities require IELTS (commonly 5.5–6.5 depending on the course), though some accept a Medium-of-Instruction letter or their own English test. The UK also offers a Graduate visa for post-study work: 2 years for applications on or before 31 December 2026, and 18 months for applications from 1 January 2027, per <a href="https://www.gov.uk/graduate-visa" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline;">gov.uk</a>. ILMERA advises whether your profile needs IELTS and which universities may waive it.</p></div></details>

      <details class="il-faq"><summary>Can I count on an Italy scholarship before a written award?</summary><div><p>No. Owner-provided conditional guidance. Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility. Do not rely on funding until written award terms confirm eligibility, coverage and payment.</p></div></details>

      <details class="il-faq"><summary>Which European countries are cheapest and don't require IELTS?</summary><div><p>The Czech Republic, Lithuania, Latvia and Slovakia are among the cheapest European destinations that often don't require IELTS, frequently accepting a Medium-of-Instruction letter or an internal English test instead. These countries also offer lower tuition and living costs than Western Europe. ILMERA confirms the current requirement for each programme before you apply.</p></div></details>

      <details class="il-faq"><summary>Can I study in Lithuania or Latvia after 12th with low marks?</summary><div><p>Yes, Lithuania and Latvia accept Indian students after 12th with modest academic marks, offer English-taught bachelor's programmes, and often don't require IELTS. Tuition and living costs are among the lowest in the EU. ILMERA reviews your marksheet and shortlists programmes that match your profile.</p></div></details>

      <details class="il-faq"><summary>How does teaching language affect tuition in Slovakia?</summary><div><p>Full-time Slovak-language study at public institutions normally has no tuition within the standard study duration. English-taught programmes charge tuition. Budget separately for living costs and other fees.</p></div></details>

      <details class="il-faq"><summary>Can I study in the GCC (UAE, Saudi Arabia, Qatar) as an Indian student?</summary><div><p>Yes, Indian students can study in GCC countries such as the UAE, Saudi Arabia, Qatar, Kuwait, Bahrain and Oman, where cities like Dubai host international branch campuses of UK, US and Australian universities. This suits students who want a globally-recognised degree closer to home or near family working in the Gulf. ILMERA advises on universities, courses and student visas across the GCC.</p></div></details>

      <details class="il-faq"><summary>What is the step-by-step process to study abroad through a consultant?</summary><div><p>The process is: a no-charge profile assessment, country and university shortlisting, application and admission, scholarship or funding guidance, visa documentation and application, then pre-departure preparation. With ILMERA, one counsellor guides you through every stage from first enquiry to arrival, so you always know the next step.</p></div></details>

      <details class="il-faq"><summary>When should I start my study abroad application and how long does it take?</summary><div><p>You should ideally start 6–12 months before your intended intake, because admissions, scholarship deadlines (like Italy's DSU) and visa processing each take time. Starting early gives you the widest choice of universities and funding. ILMERA maps your timeline backwards from your target intake so you don't miss deadlines.</p></div></details>

      <details class="il-faq"><summary>What is ILMERA Study Abroad and is it legitimate?</summary><div><p>ILMERA Study Abroad is an Indian study abroad consultancy, part of the ILMERA Group, based in Coorg, Kodagu, Karnataka, that guides students to universities in Germany, Italy, the UK, Czech Republic, Lithuania, Latvia, Slovakia, Russia and the GCC. It is led by a named, contactable team: Founder Jabir KJ, CMO Fawaz BH and CFO Zaheer KJ, and offers a no-charge initial consultation with honest eligibility advice rather than guaranteed-admission promises.</p></div></details>

      <details class="il-faq"><summary>How is ILMERA different from other study abroad consultants?</summary><div><p>ILMERA is based in Coorg, Kodagu, and offers counselling by phone, WhatsApp and video call. Discuss your academic record, budget and course preferences before choosing an application route.</p></div></details>

      <details class="il-faq"><summary>Is there a study abroad consultant for students from Coorg and Kodagu?</summary><div><p>Yes. ILMERA Study Abroad is based in Coorg and works with students from Kodagu and across Karnataka by phone, WhatsApp and video call. ILMERA counselling is online only; these channels do not involve travel to counselling premises. The full process, profile assessment, university shortlisting, admissions and visa support, covers Germany, Italy, the UK, Russia and other European destinations. Book a no-charge consultation to start from anywhere in Kodagu.</p></div></details>

    </div>
  </div>
</section>

<!-- TEAM -->
<section class="testi-sec" id="team" style="padding-top:110px;padding-bottom:110px;">
  <div class="container">
    <div class="testi-hdr">
      <span class="sec-label">The People Behind ILMERA</span>
      <h2 class="sec-h2 lt reveal">Meet Our Team</h2>
    </div>
    <div class="testi-grid">
      <article class="testi-card reveal-r" itemscope itemtype="https://schema.org/Person">
        <picture><source srcset="/assets/images/jabirkj.webp" type="image/webp"/><img src="/assets/images/jabirkj.png" alt="Jabir KJ, Founder of ILMERA Study Abroad" itemprop="image" width="96" height="96" loading="lazy" style="width:96px;height:96px;border-radius:50%;object-fit:cover;border:1px solid rgba(201,168,76,0.4);margin-bottom:20px;"/></picture>
        <div class="testi-name" itemprop="name"><a href="https://www.linkedin.com/in/jabir-kj-920300428" style="color:inherit;text-decoration:none;border-bottom:1px solid rgba(201,168,76,0.5);" itemprop="url" target="_blank" rel="noopener">Jabir KJ</a></div>
        <div class="testi-dest" itemprop="jobTitle">Founder</div>
        <p class="testi-text" style="font-size:15px;margin-top:16px;font-style:normal;">Leads ILMERA's mission to make studying abroad accessible for Indian students, including those with backlogs, low marks or no IELTS.</p>
        <a href="https://www.linkedin.com/in/jabir-kj-920300428" target="_blank" rel="noopener" aria-label="Jabir KJ on LinkedIn" style="display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:50%;border:1px solid rgba(201,168,76,0.35);margin-top:20px;transition:border-color .3s,background .3s;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.02-3.03-1.85-3.03-1.85 0-2.14 1.45-2.14 2.94v5.66H9.36V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.11 20.45H3.56V9h3.55v11.45z" fill="#C9A84C"/></svg>
        </a>
      </article>
      <article class="testi-card reveal-r" itemscope itemtype="https://schema.org/Person">
        <img src="/assets/images/fawazbh.webp" alt="Fawaz BH, CMO at ILMERA Study Abroad" itemprop="image" width="96" height="96" loading="lazy" style="width:96px;height:96px;border-radius:50%;object-fit:cover;border:1px solid rgba(201,168,76,0.4);margin-bottom:20px;"/>
        <div class="testi-name" itemprop="name"><a href="https://fawazbhseo.in" style="color:inherit;text-decoration:none;border-bottom:1px solid rgba(201,168,76,0.5);" itemprop="url">Fawaz BH</a></div>
        <div class="testi-dest" itemprop="jobTitle">CMO</div>
        <p class="testi-text" style="font-size:15px;margin-top:16px;font-style:normal;">Drives ILMERA's digital presence and helps students find clear, honest information about their study-abroad options.</p>
        <a href="https://www.linkedin.com/in/fawazbh" target="_blank" rel="noopener" aria-label="Fawaz BH on LinkedIn" style="display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:50%;border:1px solid rgba(201,168,76,0.35);margin-top:20px;transition:border-color .3s,background .3s;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.02-3.03-1.85-3.03-1.85 0-2.14 1.45-2.14 2.94v5.66H9.36V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.11 20.45H3.56V9h3.55v11.45z" fill="#C9A84C"/></svg>
        </a>
      </article>
      <article class="testi-card reveal-r" itemscope itemtype="https://schema.org/Person">
        <picture><source srcset="/assets/images/zaheer.webp" type="image/webp"/><img src="/assets/images/zaheer.png" alt="Zaheer KJ, CFO at ILMERA Study Abroad" itemprop="image" width="96" height="96" loading="lazy" style="width:96px;height:96px;border-radius:50%;object-fit:cover;border:1px solid rgba(201,168,76,0.4);margin-bottom:20px;"/></picture>
        <div class="testi-name" itemprop="name">Zaheer KJ</div>
        <div class="testi-dest" itemprop="jobTitle">CFO</div>
        <p class="testi-text" style="font-size:15px;margin-top:16px;font-style:normal;">Manages admissions, visa documentation and end-to-end coordination so every student's process runs smoothly.</p>
      </article>
    </div>
  </div>
</section>

<?php $latestGuides = array_slice(ilmera_published_posts(true), 0, 3); ?>
<?php if ($latestGuides): ?>
<section class="testi-sec" id="latest-guides" aria-label="Latest guides">
  <div class="container">
    <span class="sec-label">From the Blog</span>
    <?php ilmera_render_guides($latestGuides, 'Latest guides'); ?>
  </div>
</section>
<?php endif; ?>

<!-- CTA -->
<section class="cta-sec">

  <div class="cta-beam"></div>
  <div class="container" style="position:relative;">
    <h2 class="cta-h2 reveal">Your Dream University<br>Awaits in 9 Countries</h2>
        <p class="cta-sub reveal">Germany · Italy · UK · Czech Republic · Lithuania · Latvia · Slovakia · Russia · GCC: no-charge consultation, no commitment.</p>
    <a href="/contact" class="btn-gold reveal" style="font-size:14px;padding:18px 48px;">Book Your no-charge Consultation</a>
    <p class="cta-sub reveal" style="margin-top:24px;font-size:15px;">Email us: <a href="mailto:info@ilmerastudyabroad.com" style="color:var(--gold);text-decoration:none;">info@ilmerastudyabroad.com</a></p>
  </div>
</section>
<div class="container"><section class="source-review"><h2>Tuition guidance sources</h2><p>Checked 16 October 2026: <a href="https://www.daad.de/en/studying-in-germany/living-in-germany/finances/">DAAD tuition and living costs</a>; <a href="https://www.minedu.sk/skolne-na-vysokych-skolach-v-sr/">Slovak Ministry tuition rules</a>; <a href="https://www.universitaly.it/it/studenti-stranieri">Universitaly international student procedures</a>. The Italy scholarship statement is owner-provided conditional guidance, not an officially confirmed award. Confirm written award terms before budgeting it.</p></section></div>
</main>

<?php include __DIR__ . '/includes/footer.php'; ?>

<!-- ═══ JAVASCRIPT ═══ -->
<script>
window.addEventListener('DOMContentLoaded',function(){
(function(){
'use strict';
function lerp(a,b,t){return a+(b-a)*t;}
function rnd(a,b){return a+(b-a)*Math.random();}
function isMob(){return window.innerWidth<768;}
function isTouch(){return 'ontouchstart' in window||navigator.maxTouchPoints>0;}

var mx=window.innerWidth/2,my=window.innerHeight/2;

/* cursor (desktop only) */
if(!isTouch() && window.innerWidth>1024){
  var dot=Object.assign(document.createElement('div'),{id:'cur-dot'});
  var ring=Object.assign(document.createElement('div'),{id:'cur-ring'});
  document.body.appendChild(dot);document.body.appendChild(ring);
  var cx=mx,cy=my;
  document.addEventListener('mousemove',function(e){mx=e.clientX;my=e.clientY;dot.style.left=mx+'px';dot.style.top=my+'px';});
  (function aC(){cx=lerp(cx,mx,.18);cy=lerp(cy,my,.18);ring.style.left=cx+'px';ring.style.top=cy+'px';requestAnimationFrame(aC);})();
  document.querySelectorAll('a,button').forEach(function(el){
    el.addEventListener('mouseenter',function(){dot.classList.add('hov');ring.classList.add('hov');});
    el.addEventListener('mouseleave',function(){dot.classList.remove('hov');ring.classList.remove('hov');});
  });
  document.body.style.cursor='none';
}

/* nav scroll */
window.addEventListener('scroll',function(){
  var nav=document.getElementById('il-nav');
  if(nav)nav.classList.toggle('scrolled',window.scrollY>60);
  if(window.scrollY>80){var s=document.getElementById('scrollInd');if(s)s.style.opacity='0';}
},{passive:true});

/* ═══ THREE.JS BACKGROUND ═══ */
if(window.THREE){
var canvas=document.getElementById('space-canvas');
var W=window.innerWidth,H=window.innerHeight;
var scene=new THREE.Scene();
var cam=new THREE.PerspectiveCamera(65,W/H,0.1,2000);
cam.position.set(0,0,120);
var ren=new THREE.WebGLRenderer({canvas:canvas,alpha:true,antialias:false,powerPreference:'high-performance'});
ren.setPixelRatio(Math.min(devicePixelRatio,2));ren.setSize(W,H);ren.setClearColor(0x04060f,1);
window.addEventListener('resize',function(){W=window.innerWidth;H=window.innerHeight;ren.setSize(W,H);cam.aspect=W/H;cam.updateProjectionMatrix();});

/* stars */
(function(){
  var N=isMob()?500:1600;var g=new THREE.BufferGeometry();
  var pos=new Float32Array(N*3),col=new Float32Array(N*3);
  var sc=[[1,.95,.85],[.8,.88,1],[1,.75,.55],[.7,.9,1],[1,1,1]];
  for(var i=0;i<N;i++){pos[i*3]=rnd(-800,800);pos[i*3+1]=rnd(-500,500);pos[i*3+2]=rnd(-600,-50);var c=sc[Math.floor(Math.random()*sc.length)];col[i*3]=c[0];col[i*3+1]=c[1];col[i*3+2]=c[2];}
  g.setAttribute('position',new THREE.BufferAttribute(pos,3));g.setAttribute('color',new THREE.BufferAttribute(col,3));
  scene.add(new THREE.Points(g,new THREE.PointsMaterial({size:1.4,vertexColors:true,transparent:true,opacity:.9,sizeAttenuation:true})));
})();
var midStarMat;
(function(){
  var N=isMob()?150:500;var g=new THREE.BufferGeometry();var pos=new Float32Array(N*3);
  for(var i=0;i<N;i++){pos[i*3]=rnd(-400,400);pos[i*3+1]=rnd(-300,300);pos[i*3+2]=rnd(-100,0);}
  g.setAttribute('position',new THREE.BufferAttribute(pos,3));
  midStarMat=new THREE.PointsMaterial({color:0xe8f0ff,size:1.5,transparent:true,opacity:.8});
  scene.add(new THREE.Points(g,midStarMat));
})();

/* globe */
var globe,globeGlow;
(function(){
  globe=new THREE.LineSegments(new THREE.WireframeGeometry(new THREE.SphereGeometry(55,28,18)),new THREE.LineBasicMaterial({color:0x1e3a6e,transparent:true,opacity:.45}));
  globe.position.set(isMob()?50:130,-10,-80);scene.add(globe);
  globeGlow=new THREE.Mesh(new THREE.TorusGeometry(58,1.5,8,80),new THREE.MeshBasicMaterial({color:0xc9a84c,transparent:true,opacity:.18}));
  globeGlow.rotation.x=Math.PI/2;globeGlow.position.copy(globe.position);scene.add(globeGlow);
  var eqM=new THREE.Mesh(new THREE.TorusGeometry(56,0.4,6,120),new THREE.MeshBasicMaterial({color:0x4488ff,transparent:true,opacity:.25}));
  eqM.position.copy(globe.position);scene.add(eqM);
})();

/* grad caps */
var capOrbiters=[];
(function(){
  var count=isMob()?2:5;
  for(var i=0;i<count;i++){
    var g=new THREE.Group();
    g.add(new THREE.Mesh(new THREE.BoxGeometry(4,0.3,4),new THREE.MeshBasicMaterial({color:0xc9a84c,transparent:true,opacity:.7})));
    g.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(1.5,0,1.5),new THREE.Vector3(2.5,-2,2.5)]),new THREE.LineBasicMaterial({color:0xc9a84c,transparent:true,opacity:.6})));
    var btn=new THREE.Mesh(new THREE.SphereGeometry(.5,6,6),new THREE.MeshBasicMaterial({color:0xc9a84c,transparent:true,opacity:.8}));btn.position.set(0,.4,0);g.add(btn);
    capOrbiters.push({g:g,angle:(i/count)*Math.PI*2,radius:rnd(70,110),yOff:rnd(-30,30),speed:rnd(.0003,.0008)*(Math.random()<.5?1:-1),tilt:rnd(-.4,.4)});
    scene.add(g);
  }
})();

/* books */
var bookObjs=[];
(function(){
  var count=isMob()?2:6;
  for(var i=0;i<count;i++){
    var g=new THREE.Group();
    var lp=new THREE.Mesh(new THREE.BoxGeometry(3.5,.1,5),new THREE.MeshBasicMaterial({color:0x3a5a9a,transparent:true,opacity:.6}));lp.position.set(-1.8,0,0);lp.rotation.y=-.25;
    var rp=new THREE.Mesh(new THREE.BoxGeometry(3.5,.1,5),new THREE.MeshBasicMaterial({color:0x4a6ab0,transparent:true,opacity:.6}));rp.position.set(1.8,0,0);rp.rotation.y=.25;
    var sp=new THREE.Mesh(new THREE.BoxGeometry(.4,.2,5),new THREE.MeshBasicMaterial({color:0xc9a84c,transparent:true,opacity:.7}));
    g.add(lp);g.add(rp);g.add(sp);
    g.position.set(rnd(-180,180),rnd(-120,120),rnd(-180,-10));g.rotation.set(rnd(-1,1),rnd(-1,1),rnd(-1,1));
    bookObjs.push({g:g,vy:rnd(-.04,.04),vx:rnd(-.03,.03),vrot:rnd(-.003,.003)});scene.add(g);
  }
})();

/* helix */
var helixGroup=new THREE.Group();
(function(){
  var N=60,R=12,pitch=2.2;var pts1=[],pts2=[];
  for(var i=0;i<N;i++){var t=(i/N)*Math.PI*6;pts1.push(new THREE.Vector3(Math.cos(t)*R,i*pitch-N*pitch/2,Math.sin(t)*R));pts2.push(new THREE.Vector3(Math.cos(t+Math.PI)*R,i*pitch-N*pitch/2,Math.sin(t+Math.PI)*R));}
  helixGroup.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts1),new THREE.LineBasicMaterial({color:0x4488ff,transparent:true,opacity:.5})));
  helixGroup.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts2),new THREE.LineBasicMaterial({color:0xc9a84c,transparent:true,opacity:.5})));
  for(var i=0;i<N;i+=4){var t=(i/N)*Math.PI*6;var a=new THREE.Vector3(Math.cos(t)*R,i*pitch-N*pitch/2,Math.sin(t)*R);var b=new THREE.Vector3(Math.cos(t+Math.PI)*R,i*pitch-N*pitch/2,Math.sin(t+Math.PI)*R);helixGroup.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints([a,b]),new THREE.LineBasicMaterial({color:0xffffff,transparent:true,opacity:.15})));var d=new THREE.Mesh(new THREE.SphereGeometry(1.2,6,6),new THREE.MeshBasicMaterial({color:i%8===0?0xc9a84c:0x4488ff,transparent:true,opacity:.7}));d.position.copy(a);helixGroup.add(d);}
  helixGroup.position.set(isMob()?-70:-160,0,-60);scene.add(helixGroup);
})();

var clock={then:performance.now(),el:0};
function animate(){
  requestAnimationFrame(animate);
  var now=performance.now(),dt=(now-clock.then)/1000;clock.then=now;clock.el+=dt;var t=clock.el;
  var nmx=isMob()?0:(mx/W-.5)*2,nmy=isMob()?0:(my/H-.5)*2;
  if(midStarMat)midStarMat.opacity=.6+.3*Math.sin(t*1.2);
  if(globe){globe.rotation.y+=.0006;globe.rotation.x=lerp(globe.rotation.x,nmy*-.4,.04);var gs=1+.015*Math.sin(t*.8);globe.scale.set(gs,gs,gs);if(globeGlow){globeGlow.rotation.x=Math.PI/2+t*.3;globeGlow.scale.copy(globe.scale);}}
  capOrbiters.forEach(function(o){o.angle+=o.speed;var x=Math.cos(o.angle)*o.radius+(globe?globe.position.x:0);var z=Math.sin(o.angle)*o.radius*.6+(globe?globe.position.z:0);o.g.position.set(x,o.yOff+Math.sin(o.angle*2)*8,z);o.g.rotation.y+=.008;o.g.rotation.x=o.tilt+Math.sin(t+o.angle)*.1;o.g.scale.setScalar(.7+.15*Math.sin(t+o.angle));});
  bookObjs.forEach(function(b){b.g.position.y+=b.vy;b.g.position.x+=b.vx;b.g.rotation.y+=b.vrot;if(b.g.position.y>150)b.g.position.y=-150;if(b.g.position.y<-150)b.g.position.y=150;if(b.g.position.x>200)b.g.position.x=-200;if(b.g.position.x<-200)b.g.position.x=200;});
  if(helixGroup){helixGroup.rotation.y+=.004;helixGroup.rotation.x=nmy*.15;helixGroup.position.y=Math.sin(t*.4)*15;}
  cam.position.x=lerp(cam.position.x,nmx*-8,.04);cam.position.y=lerp(cam.position.y,nmy*5,.04);cam.lookAt(0,0,0);
  ren.render(scene,cam);
}
animate();
}

/* ═══ FLOATING ICONS (desktop only, fixes mobile overlap) ═══ */
if(window.innerWidth>768){
var eduIcons=[
  '<svg width="32" height="32" viewBox="0 0 32 32" fill="none"><path d="M16 6 L30 12 L16 18 L2 12 Z" stroke="#C9A84C" stroke-width="1.2" fill="none" opacity="0.8"/><path d="M8 15 L8 22 Q16 26 24 22 L24 15" stroke="#C9A84C" stroke-width="1.2" fill="none" opacity="0.8"/></svg>',
  '<svg width="36" height="28" viewBox="0 0 36 28" fill="none"><path d="M18 6 Q10 4 2 6 L2 24 Q10 22 18 24" stroke="#4488ff" stroke-width="1.2" fill="none" opacity="0.7"/><path d="M18 6 Q26 4 34 6 L34 24 Q26 22 18 24" stroke="#4488ff" stroke-width="1.2" fill="none" opacity="0.7"/><line x1="18" y1="9" x2="18" y2="24" stroke="#4488ff" stroke-width="1" opacity="0.5"/></svg>',
  '<svg width="36" height="28" viewBox="0 0 36 28" fill="none"><rect x="2" y="2" width="32" height="24" rx="2" stroke="#C9A84C" stroke-width="1.2" fill="none" opacity="0.6"/><circle cx="28" cy="19" r="4" stroke="#C9A84C" stroke-width=".8" fill="none" opacity="0.5"/></svg>',
  '<svg width="36" height="36" viewBox="0 0 36 36" fill="none"><circle cx="18" cy="18" r="3" fill="#aabbff" opacity="0.8"/><ellipse cx="18" cy="18" rx="15" ry="9" stroke="#4488ff" stroke-width="1" fill="none" opacity="0.5"/><ellipse cx="18" cy="18" rx="15" ry="9" stroke="#4488ff" stroke-width="1" fill="none" opacity="0.5" transform="rotate(60 18 18)"/></svg>',
  '<svg width="32" height="32" viewBox="0 0 32 32" fill="none"><polygon points="16,2 19.5,12 30,12 21.5,18.5 24.5,29 16,23 7.5,29 10.5,18.5 2,12 12.5,12" stroke="#C9A84C" stroke-width="1.2" fill="none" opacity="0.65"/></svg>'
];
var floatLayer=document.getElementById('float-layer');
function spawnFloatEl(){
  var el=document.createElement('div');el.className='f-elem';el.innerHTML=eduIcons[Math.floor(Math.random()*eduIcons.length)];
  var dur=rnd(12,22),delay=rnd(0,3);
  el.style.cssText='left:'+rnd(2,95)+'%;bottom:-60px;transform:scale('+rnd(0.5,1.3)+') rotate('+rnd(-30,30)+'deg);animation-duration:'+dur+'s;animation-delay:'+delay+'s;opacity:0;filter:blur(.5px);';
  floatLayer.appendChild(el);setTimeout(function(){el.remove();},(dur+delay+2)*1000);
}
setInterval(spawnFloatEl,1800);
for(var si=0;si<6;si++)setTimeout(spawnFloatEl,si*700);
}

/* ═══ GSAP ANIMATIONS ═══ */
if(window.gsap&&window.ScrollTrigger){
  gsap.registerPlugin(ScrollTrigger);
  var tl=gsap.timeline({delay:.3});
  tl.fromTo('#hLabel',{opacity:0,y:20,scale:.9},{opacity:1,y:0,scale:1,duration:.6,ease:'back.out(1.7)'},0);
  tl.fromTo('#hH1',{opacity:0,y:60},{opacity:1,y:0,duration:.9,ease:'power3.out'},.35);
  tl.fromTo('#hSub',{opacity:0,y:25},{opacity:1,y:0,duration:.7,ease:'power2.out'},.85);
  tl.fromTo('#hBtns',{opacity:0,y:18},{opacity:1,y:0,duration:.6,ease:'power2.out'},1.2);
  tl.fromTo('#hDiv',{opacity:0},{opacity:1,duration:.4},1.55);
  tl.fromTo('#hStats',{opacity:0,y:12},{opacity:1,y:0,duration:.6,ease:'power2.out'},1.6);

  function rev(sel,from){gsap.utils.toArray(sel).forEach(function(el){gsap.fromTo(el,from,{opacity:1,x:0,y:0,duration:.9,ease:'power3.out',scrollTrigger:{trigger:el,start:'top 88%',once:true}});});}
  rev('.reveal',{opacity:0,y:55});rev('.reveal-l',{opacity:0,x:-60});rev('.reveal-r',{opacity:0,x:60});
  var wc=gsap.utils.toArray('.why-card');if(wc.length)gsap.fromTo(wc,{opacity:0,y:70,scale:.94},{opacity:1,y:0,scale:1,duration:.75,ease:'power3.out',stagger:.16,scrollTrigger:{trigger:wc[0],start:'top 88%',once:true}});
  var tc=gsap.utils.toArray('.testi-card');if(tc.length)gsap.fromTo(tc,{opacity:0,x:60},{opacity:1,x:0,duration:.75,ease:'power3.out',stagger:.16,scrollTrigger:{trigger:tc[0],start:'top 88%',once:true}});
  var sc=gsap.utils.toArray('.special-card');if(sc.length)gsap.fromTo(sc,{opacity:0,y:50,scale:.92},{opacity:1,y:0,scale:1,duration:.7,ease:'back.out(1.5)',stagger:.16,scrollTrigger:{trigger:sc[0],start:'top 88%',once:true}});
  ScrollTrigger.refresh();
}else{
  document.querySelectorAll('.reveal,.reveal-l,.reveal-r').forEach(function(el){el.style.opacity='1';});
}

/* scroll progress */
var prog=document.createElement('div');prog.id='scroll-progress';document.body.appendChild(prog);
window.addEventListener('scroll',function(){var pct=(window.scrollY/(document.body.scrollHeight-window.innerHeight))*100;prog.style.width=Math.min(pct,100)+'%';},{passive:true});

/* card tilt (desktop only) */
if(window.innerWidth>1024){
  document.querySelectorAll('.why-card,.testi-card,.special-card').forEach(function(card){
    var b;
    card.addEventListener('mouseenter',function(){b=card.getBoundingClientRect();});
    card.addEventListener('mousemove',function(e){if(!b)return;var rx=((e.clientY-b.top-b.height/2)/(b.height/2))*-6;var ry=((e.clientX-b.left-b.width/2)/(b.width/2))*6;card.style.transform='perspective(900px) rotateX('+rx+'deg) rotateY('+ry+'deg) translateY(-6px)';});
    card.addEventListener('mouseleave',function(){card.style.transition='transform .5s cubic-bezier(.22,.61,.36,1)';card.style.transform='perspective(900px) rotateX(0) rotateY(0) translateY(0)';b=null;});
  });
}
})();
});
</script>
</body>
</html>
