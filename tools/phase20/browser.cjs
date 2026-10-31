const {chromium}=require('playwright'),packed=require('@sparticuz/chromium'),fs=require('fs');
(async()=>{
 const manifest=JSON.parse(fs.readFileSync(process.argv[2]+'/snapshots.json','utf8'));
 const browser=await chromium.launch({executablePath:await packed.executablePath(),args:packed.args.filter(a=>!['--single-process','--in-process-gpu'].includes(a)),headless:true});let cases=0,faqs=0;
 for(const js of [false,true])for(const width of [375,768,1280]){
  const context=await browser.newContext({viewport:{width,height:900},javaScriptEnabled:js});
  await context.route('**/*',async route=>{if(new URL(route.request().url()).hostname==='127.0.0.1')await route.continue();else await route.abort();});
  const page=await context.newPage();
  for(const route of Object.keys(manifest)){
   const r=await page.goto('http://127.0.0.1:8080'+route,{waitUntil:'load'});if(r.status()!==200)throw Error(route+' HTTP '+r.status());
   if(js&&route==='/contact'){await page.locator('.contact-info').scrollIntoViewIfNeeded();await page.waitForSelector('.contact-info.anim-visible');}
   // Exercise scroll-triggered reveals before checking final layout, including JS-off pages.
   if(js)await page.evaluate(async()=>{
    for(let y=0;y<document.documentElement.scrollHeight;y+=700){window.scrollTo(0,y);await new Promise(requestAnimationFrame);}
    const finite=document.getAnimations().filter(a=>a.effect.getTiming().iterations!==Infinity);
    await Promise.all(finite.map(a=>a.finished.catch(()=>{})));window.scrollTo(0,0);
   });
   const check=await page.evaluate(()=>({width:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth,h1:document.querySelectorAll('h1').length}));
   if(check.scroll>width+1||check.h1!==1)throw Error(JSON.stringify({route,js,width,check}));
   const faq=page.locator('details.il-faq');
   for(let i=0;i<await faq.count();i++){
    const el=faq.nth(i);await el.locator('summary').click();
    const shape=await el.evaluate(e=>{let box=e.querySelector('div');return {open:e.open,text:box?.innerText.trim(),height:box?.clientHeight,scroll:box?.scrollHeight};});
    if(!shape.open||!shape.text||shape.scroll>shape.height+2)throw Error(JSON.stringify({route,js,width,faq:i,shape}));
    await el.locator('summary').click();faqs++;
   }
   const custom=page.locator('.faq-item');
   for(let i=0;i<await custom.count();i++){
    const el=custom.nth(i);if(js)await el.locator('.faq-q').click();
    const shape=await el.locator('.faq-ans,.faq-a').evaluate(e=>({height:e.clientHeight,scroll:e.scrollHeight,text:e.innerText.trim()}));
    if(!shape.text||shape.height===0||shape.scroll>shape.height+2)throw Error(JSON.stringify({route,js,width,customFAQ:i,shape}));
    faqs++;
   }
   cases++;
  }
  await context.close();
 }
 await browser.close();console.log(JSON.stringify({status:'PASS',cases,faq_expansions:faqs,viewports:[375,768,1280],javascript:[false,true],external_requests:'aborted; no live font/performance/delivery assertion'}));
})().catch(e=>{console.error(e);process.exit(1)});
