#!/usr/bin/env node
// Full non-performance browser invariants: 43 routes x 3 widths x JavaScript on/off.
const fs=require('node:fs'),path=require('node:path');
const {launchBrowser,routePinnedResources}=require('./browser.cjs');
const ROOT=path.resolve(__dirname,'../..');const BASE=process.env.PHASE31_BASE_URL||'http://127.0.0.1:8080';
const inventory=JSON.parse(fs.readFileSync(path.join(ROOT,'reports/phase-25-baseline-renders.json'),'utf8')).routes;
const routes=Object.keys(inventory).sort(),widths=[360,768,1280],jsStates=['on','off'];
const argv=process.argv.slice(2),get=(k,d)=>{const i=argv.indexOf(k);return i<0?d:argv[i+1]};
const OUT=get('--out','/home/user/phase31/browser-suite.json');
const TARGET_BASELINE=get('--target-baseline','');const RECORD=argv.includes('--record-baseline');const REQUIRE_VISIBLE=argv.includes('--require-visible');
const REDUCED_ROUTES=['/','/services','/about','/contact','/study-in-germany','/study-abroad-counselling-mysuru','/blog/how-to-choose-study-abroad-consultant-karnataka','/blog/'];
const key=(r,w,j,m)=>`${r}|${w}|${j}|${m}`;
function cssSig(s){return String(s||'').replace(/\s+/g,' ').trim();}
async function scrollPage(page){
 const h=await page.evaluate(()=>Math.max(document.documentElement.scrollHeight,document.body.scrollHeight)),v=900,w=await page.evaluate(()=>innerWidth);
 await page.mouse.move(Math.floor(w/2),450);
 for(let y=0;y<h;y+=680){await page.mouse.wheel(0,Math.min(680,h-y));await page.waitForTimeout(25);}
 await page.waitForTimeout(3000);await page.mouse.wheel(0,-(h+v));await page.waitForTimeout(100);
 return h;
}
async function main(){
 if(routes.length!==43)throw Error(`expected43 routes, got${routes.length}`);
 const browser=await launchBrowser(),contexts={};for(const js of jsStates)contexts[js]=await browser.newContext({viewport:{width:360,height:900},javaScriptEnabled:js==='on',reducedMotion:'no-preference'});
 const cases=[],targetMap={},allHidden=[];let count=0;
 try{
  const matrix=[...routes.flatMap(route=>widths.flatMap(width=>jsStates.map(js=>({route,width,js,motion:'normal'}))))];
  for(const route of REDUCED_ROUTES)for(const width of widths)for(const js of jsStates)matrix.push({route,width,js,motion:'reduced'});
  for(const c of matrix){
   const ctx=contexts[c.js];const page=await ctx.newPage();await page.setViewportSize({width:c.width,height:900});await page.emulateMedia({reducedMotion:c.motion==='reduced'?'reduce':'no-preference'});await routePinnedResources(page);
   const fails=[];page.on('requestfailed',r=>fails.push({url:r.url(),error:r.failure()?.errorText||''}));
   const res=await page.goto(BASE+(c.route==='/'?'/':c.route),{waitUntil:'domcontentloaded',timeout:45000});if(!res||res.status()!==200)throw Error(`HTTP ${res?.status()} ${c.route}`);
   await page.waitForTimeout(300);const height=await scrollPage(page);
   const shape=await page.evaluate(()=>{
    const selector=e=>e.id?'#'+e.id:e.tagName.toLowerCase()+(e.classList.length?'.'+[...e.classList].slice(0,2).join('.'):'');
    const isIntentionallyHidden=e=>!!e.closest('header,nav,footer,.scroll-ind,[hidden],[aria-hidden="true"],details:not([open]),.faq-a,.faq-ans,.mobile-menu,.nav-menu');
    const measureTargets=[...document.querySelectorAll('a[href],button,summary,input,select,textarea,[role="button"]')].filter(e=>{const r=e.getBoundingClientRect(),s=getComputedStyle(e);return r.width>0&&r.height>0&&s.display!=='none'&&s.visibility!=='hidden'&&!isIntentionallyHidden(e);});
    const targets=measureTargets.map((e,i)=>{const r=e.getBoundingClientRect();const text=(e.innerText||e.getAttribute('aria-label')||e.getAttribute('alt')||'').trim().replace(/\s+/g,' ').slice(0,100);const id=e.id||e.getAttribute('href')||e.getAttribute('name')||e.getAttribute('type')||'';return{key:`${e.tagName.toLowerCase()}|${id}|${text}|${i}`,tag:e.tagName.toLowerCase(),id,href:e.getAttribute('href'),text,width:+r.width.toFixed(2),height:+r.height.toFixed(2),x:+r.x.toFixed(2),y:+r.y.toFixed(2)};});
    const hidden=[];const walker=document.createTreeWalker(document.querySelector('main')||document.body,NodeFilter.SHOW_TEXT);let n;
    while((n=walker.nextNode())){const text=(n.nodeValue||'').replace(/\s+/g,' ').trim(),p=n.parentElement;if(!text||!p||isIntentionallyHidden(p))continue;let opacity=1,visible=true,reasons=[];for(let a=p;a&&a.nodeType===1;a=a.parentElement){const s=getComputedStyle(a);opacity*=parseFloat(s.opacity)||0;if(s.display==='none'){visible=false;reasons.push('display:none');}if(s.visibility==='hidden'||s.visibility==='collapse'){visible=false;reasons.push('visibility:'+s.visibility);}if(s.contentVisibility==='hidden'){visible=false;reasons.push('content-visibility:hidden');}}if(opacity<.05){visible=false;reasons.push('opacity:'+opacity.toFixed(3));}if(!visible){const r=document.createRange();r.selectNodeContents(n);const b=r.getBoundingClientRect();hidden.push({selector:selector(p),y:Math.round(b.top+scrollY),text:text.slice(0,120),opacity:Number(opacity.toFixed(3)),reasons:[...new Set(reasons)]});}}
    return{width:innerWidth,scrollWidth:document.documentElement.scrollWidth,bodyScrollWidth:document.body.scrollWidth,h1:[...document.querySelectorAll('h1')].length,mainText:(document.querySelector('main')?.innerText||'').trim().length,targets,hidden};
   });
   if(shape.scrollWidth>c.width+1||shape.bodyScrollWidth>c.width+1)throw Error(`horizontal overflow ${JSON.stringify({route:c.route,width:c.width,scroll:shape.scrollWidth,body:shape.bodyScrollWidth})}`);
   if(shape.h1!==1||shape.mainText===0)throw Error(`missing content landmark ${JSON.stringify({route:c.route,width:c.width,h1:shape.h1,main:shape.mainText})}`);
   if(REQUIRE_VISIBLE&&shape.hidden.length)throw Error(`invisible main text after scroll ${JSON.stringify({route:c.route,width:c.width,js:c.js,motion:c.motion,hidden:shape.hidden.slice(0,4)})}`);
   for(const t of shape.targets)targetMap[key(c.route,c.width,c.js,c.motion)+'|'+t.key]=t;
   for(const h of shape.hidden)allHidden.push({...h,route:c.route,width:c.width,javascript:c.js,motion:c.motion});
   const loadedImages=await page.evaluate(()=>[...document.querySelectorAll('img')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.height>0;}).map(e=>({src:new URL(e.currentSrc||e.src,location.href).pathname,complete:e.complete,naturalWidth:e.naturalWidth,naturalHeight:e.naturalHeight})));
   for(const im of loadedImages){if(!im.complete||im.naturalWidth<=0||im.naturalHeight<=0)throw Error(`image did not load ${c.route} ${JSON.stringify(im)}`);}
   cases.push({route:c.route,width:c.width,javascript:c.js,motion:c.motion,http_status:res.status(),page_height:height,scroll_width:shape.scrollWidth,h1:shape.h1,main_text_chars:shape.mainText,target_count:shape.targets.length,hidden_text_count:shape.hidden.length,loaded_images:loadedImages.length,request_failures:fails.filter(x=>!x.url.startsWith('https://fonts.googleapis.com/'))});
   await page.close();count++;console.log(`BROWSER ${count}/${matrix.length} ${c.route} ${c.width} JS-${c.js} ${c.motion} h=${height} hidden=${shape.hidden.length}`);
  }
 }finally{await browser.close();}
 const result={passed:true,browser:browser.version(),routes:routes.length,normal_cases:routes.length*widths.length*jsStates.length,reduced_motion_cases:REDUCED_ROUTES.length*widths.length*jsStates.length,total_cases:count,widths,javascript:jsStates,reduced_motion_template_routes:REDUCED_ROUTES,cases,hidden_text:allHidden,target_dimensions:targetMap,target_size_baseline_comparison:null,checks:['HTTP 200 for every frozen route','one H1 and non-empty main text','no horizontal overflow','all rendered img resources load','main-content hidden text inventory after complete slow scroll']};
 if(TARGET_BASELINE){const old=JSON.parse(fs.readFileSync(TARGET_BASELINE,'utf8'));const failures=[];const deltas=[];for(const [k,b] of Object.entries(old.targets||old)){const n=targetMap[k];if(!n)continue;const dw=n.width-b.width,dh=n.height-b.height;deltas.push({key:k,width_delta:+dw.toFixed(2),height_delta:+dh.toFixed(2)});if(dw<-.5||dh<-.5)failures.push({key:k,baseline:{width:b.width,height:b.height},current:{width:n.width,height:n.height}});}result.target_size_baseline_comparison={baseline:TARGET_BASELINE,compared:deltas.length,failures};if(failures.length)throw Error(`Existing interactive target dimensions shrank: ${JSON.stringify(failures.slice(0,20))}`);}
 const out=path.resolve(OUT);fs.mkdirSync(path.dirname(out),{recursive:true});fs.writeFileSync(out,JSON.stringify(result,null,2)+'\n');
 if(RECORD){const dest=path.join(ROOT,'reports/phase-31-target-baseline.json');fs.writeFileSync(dest,JSON.stringify({source_head:require('node:child_process').execFileSync('git',['rev-parse','HEAD'],{cwd:ROOT,encoding:'utf8'}).trim(),browser:result.browser,targets:targetMap},null,2)+'\n');}
 console.log(`BROWSER SUITE PASS ${count} cases; targets=${Object.keys(targetMap).length} hidden=${allHidden.length}`);
}
main().catch(e=>{console.error(e.stack||e);process.exit(1)});
