const {chromium}=require('playwright'),packed=require('@sparticuz/chromium'),fs=require('fs'),{resources}=require('./resources.cjs');
const routes=['/study-in-germany','/study-abroad-counselling-mysuru','/blog/how-to-choose-study-abroad-consultant-karnataka','/blog/'];
(async()=>{const browser=await chromium.launch({executablePath:await packed.executablePath(),args:packed.args.filter(a=>!['--single-process','--in-process-gpu'].includes(a)),headless:true}),out=[];let faqChecks=0;
for(const js of [false,true])for(const width of [360,768,1280])for(const route of routes){
 const context=await browser.newContext({viewport:{width,height:900},javaScriptEnabled:js});await context.route('**/*',resources);const page=await context.newPage();await page.goto('http://127.0.0.1:8080'+route,{waitUntil:'networkidle'});await page.evaluate(()=>document.fonts.ready);
 const session=await context.newCDPSession(page);await session.send('DOM.enable');await session.send('CSS.enable');const doc=await session.send('DOM.getDocument');const fonts={};
 for(const [selector,family] of [['h1','Cormorant'],['.seo-opening','Outfit']]){const n=await session.send('DOM.querySelector',{nodeId:doc.root.nodeId,selector});fonts[selector]=(await session.send('CSS.getPlatformFontsForNode',{nodeId:n.nodeId})).fonts;if(!fonts[selector].some(f=>f.isCustomFont&&f.familyName.includes(family)))throw Error('Reference font fallback '+JSON.stringify({route,js,width,fonts}));}await session.detach();
 const shape=await page.evaluate(()=>({visibility:getComputedStyle(document.body).visibility,fontPending:document.documentElement.classList.contains('p25-font-pending'),scroll:document.documentElement.scrollWidth,width:innerWidth,h1:document.querySelector('h1')?.innerText,hero:document.querySelector('.article-hero,.blog-hero')?.getBoundingClientRect().height,firstLight:getComputedStyle(document.querySelector('main>section:nth-of-type(2)')).backgroundColor,canvas:document.querySelector('canvas')?{hidden:document.querySelector('canvas').getAttribute('aria-hidden'),role:document.querySelector('canvas').getAttribute('role'),width:document.querySelector('canvas').width}:null}));if(shape.visibility!=='visible'||shape.fontPending||shape.canvas!==null||shape.scroll>width+1||!shape.h1||shape.firstLight!=='rgb(240, 244, 255)')throw Error(JSON.stringify({route,js,width,shape}));
 for(const faq of await page.locator('details.il-faq').all()){await faq.locator('summary').click();await page.evaluate(()=>document.getAnimations().filter(a=>a.effect.getTiming().iterations!==Infinity).forEach(a=>a.finish()));if(!(await faq.evaluate(e=>e.open&&e.querySelector('div').scrollHeight<=e.querySelector('div').clientHeight+2)))throw Error('FAQ overflow '+route);await faq.locator('summary').click();faqChecks++;}
 if(js){
  if(width<=768){await page.locator('#hbg').click();if(await page.locator('#hbg').getAttribute('aria-expanded')!=='true')throw Error('Menu did not open');await page.keyboard.press('Escape');}
  await page.addScriptTag({path:require.resolve('axe-core/axe.min.js')});const axe=await page.evaluate(()=>axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa']}}));
  const violations=axe.violations.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.map(n=>({target:n.target,summary:n.failureSummary}))}));
  await page.keyboard.press('Tab');await page.locator('main a,main summary').first().focus();const focus=await page.locator(':focus').evaluate(e=>({width:getComputedStyle(e).outlineWidth,style:getComputedStyle(e).outlineStyle}));if(focus.width==='0px'||focus.style==='none')throw Error('Invisible focus '+route);
  const targets=await page.evaluate(()=>[...document.querySelectorAll('a,button,summary,input,select,textarea')].filter(e=>e.getClientRects().length&&!e.closest('[inert]')&&getComputedStyle(e).visibility!=='hidden').map(e=>({text:(e.getAttribute('aria-label')||e.innerText).slice(0,80),width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height,tag:e.tagName})).filter(e=>e.width<43.9||e.height<43.9));
  out.push({route,js,width,shape,fonts,violations,small_targets:targets});
 }else out.push({route,js,width,shape,fonts});await context.close();
}
// Static loader branches with actual browser network requests, not just source matching.
const states=[];for(const state of ['normal','reduced-motion','save-data','hidden']){
 const context=await browser.newContext({viewport:{width:360,height:900},reducedMotion:state==='reduced-motion'?'reduce':'no-preference'});await context.route('**/*',resources);let images=0;
 if(state==='save-data')await context.addInitScript(()=>Object.defineProperty(navigator,'connection',{value:{saveData:true}}));
 if(state==='hidden')await context.addInitScript(()=>{window.__hidden=true;Object.defineProperty(document,'hidden',{get:()=>window.__hidden});});
 const page=await context.newPage();page.on('request',r=>{if(r.url().includes('/hero-still-')&&r.url().endsWith('.webp'))images++;});await page.goto('http://127.0.0.1:8080/blog/',{waitUntil:'networkidle'});await page.waitForTimeout(1800);
 if(['save-data','hidden'].includes(state)&&images)throw Error('Still fetched in '+state);
 if(state==='hidden'){await page.evaluate(()=>{window.__hidden=false;document.dispatchEvent(new Event('visibilitychange'));});await page.waitForTimeout(1800);}
 if(images!==0)throw Error('Palette tier unexpectedly fetched a still '+JSON.stringify({state,images}));states.push({state,still_requests:images,hidden:'document.hidden branch emulated; not OS throttling proof'});await context.close();
}
await browser.close();const data={cases:out,faq_checks:faqChecks,scene_states:states,network:'npm-mirrored external fonts/scripts; local assets; never submits forms',passed:out.every(x=>!x.violations?.length&&!x.small_targets?.length)};fs.writeFileSync('reports/phase-25-pilot-qa.json',JSON.stringify(data,null,2)+'\n');console.log(JSON.stringify(data));if(!data.passed)process.exit(2);
})().catch(e=>{console.error(e);process.exit(1)});
