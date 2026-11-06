#!/usr/bin/env node
// Final palette/still scope verification for Phase32a, including measured fallbacks.
const fs=require('node:fs'),path=require('node:path');
const {launchBrowser,routePinnedResources}=require('../phase31/browser.cjs');
const ROOT=path.resolve(__dirname,'../..'),BASE=process.env.PHASE31_BASE_URL||'http://127.0.0.1:8094';
const widths=[360,768,1280];
const routes=[
 {route:'/study-in-germany',template:'destination',still:true},
 {route:'/study-abroad-counselling-mysuru',template:'place',still:false},
 {route:'/blog/how-to-choose-study-abroad-consultant-karnataka',template:'article',still:false},
 {route:'/blog/',template:'blog',still:true}
];
const path640='/assets/images/hero-still-640.webp',path1440='/assets/images/hero-still-1440.webp';
const asset=(pathname)=>path.join(ROOT,pathname.replace(/^\//,''));
(async()=>{
 const config=fs.readFileSync(path.join(ROOT,'includes/visual-config.php'),'utf8');
 if(!/define\('ILMERA_SCENES_ENABLED',\s*true\)/.test(config))throw Error('ILMERA_SCENES_ENABLED is not enabled by default');
 if(!/define\('ILMERA_VISUAL_PLAIN_HERO_TEMPLATES',\s*\['place','article'\]\)/.test(config))throw Error('Measured place/article fallback set is missing or changed');
 const sizes={mobile_bytes:fs.statSync(asset(path640)).size,desktop_bytes:fs.statSync(asset(path1440)).size};
 if(sizes.mobile_bytes>14000||sizes.desktop_bytes>40000)throw Error(`Still size budget failed: ${JSON.stringify(sizes)}`);
 const browser=await launchBrowser(),cases=[];
 try{
  for(const item of routes)for(const width of widths){
   const context=await browser.newContext({viewport:{width,height:900},javaScriptEnabled:true,reducedMotion:'no-preference'}),page=await context.newPage();
   const requests=[];let loadAt=null;page.on('load',()=>{loadAt=Date.now();});page.on('request',req=>{const u=new URL(req.url());if(u.pathname.includes('/assets/images/hero-still-'))requests.push({path:u.pathname,at:Date.now()});});
   await routePinnedResources(page);const response=await page.goto(BASE+item.route,{waitUntil:'load',timeout:45000});if(!response||response.status()!==200)throw Error(`HTTP ${response?.status()} ${item.route}`);await page.waitForTimeout(1700);
   const state=await page.evaluate(()=>{const hero=document.querySelector('.article-hero,.blog-hero');const canvas=document.querySelector('canvas.p32-hero-still');const style=document.querySelector('#ilmera-visual-system')?.textContent||'';return{body_class:document.body.className,hero:!!hero,background:hero?getComputedStyle(hero).backgroundImage:'',canvas:!!canvas,canvas_position:canvas?getComputedStyle(canvas).position:null,loader:document.documentElement.outerHTML.includes("document.querySelector('.p32-hero-still')"),hero_still_urls:(document.documentElement.outerHTML.match(/hero-still-(?:640|720|1440)\.webp/g)||[]).length,style_still_url_count:(style.match(/\/assets\/images\/hero-still-/g)||[]).length,transition:canvas?getComputedStyle(canvas).transitionDuration:null};});
   const isBlog=item.template==='blog',mobile=width<=768,expectedRequest=item.still&&(!isBlog||!mobile)?(mobile?path640:path1440):null;
   const actual=requests.map(r=>r.path);if(expectedRequest){if(!actual.includes(expectedRequest))throw Error(`Missing expected delayed still request ${expectedRequest}: ${item.route} ${width} ${JSON.stringify(requests)}`);if(requests.some(r=>r.at<(loadAt||0)))throw Error(`Still requested before window.load: ${item.route} ${width}`);}else if(actual.length)throw Error(`Unexpected still request for ${item.route} ${width}: ${JSON.stringify(requests)}`);
   if(!state.hero||!state.body_class.split(/\s+/).includes('p25-'+item.template))throw Error(`Wrong hero/template body on ${item.route}: ${JSON.stringify(state)}`);
   if(!item.still){if(state.canvas||state.loader||state.hero_still_urls||state.style_still_url_count||state.background.includes('url(')||!state.background.includes('linear-gradient'))throw Error(`Palette fallback not clean for ${item.route}: ${JSON.stringify(state)}`);}
   else if(!state.canvas||state.canvas_position!=='absolute'||!state.loader)throw Error(`Scene layer/loader missing on ${item.route}: ${JSON.stringify(state)}`);
   cases.push({route:item.route,template:item.template,width,http_status:response.status(),expected_still_request:expectedRequest,still_requests:requests,load_event_at:loadAt,state});await context.close();console.log(`PALETTE ${item.route} ${width} PASS`);
  }
  const dimensionContext=await browser.newContext({viewport:{width:1280,height:900},javaScriptEnabled:true}),dimensionPage=await dimensionContext.newPage();await routePinnedResources(dimensionPage);const dimensionResponse=await dimensionPage.goto(BASE+'/study-in-germany',{waitUntil:'load',timeout:45000});const dimensions=await dimensionPage.evaluate(async paths=>Promise.all(paths.map(async src=>{const image=new Image();image.src=src;await image.decode();return{src,width:image.naturalWidth,height:image.naturalHeight};})),[path640,path1440]);if(!dimensionResponse||dimensionResponse.status()!==200||dimensions[0].width!==640||dimensions[0].height!==800||dimensions[1].width!==1440||dimensions[1].height!==900)throw Error(`Responsive still dimensions invalid: ${JSON.stringify(dimensions)}`);await dimensionContext.close();
  const reducedContext=await browser.newContext({viewport:{width:360,height:900},javaScriptEnabled:true,reducedMotion:'reduce'}),page=await reducedContext.newPage();let reducedRequests=[];await routePinnedResources(page);page.on('request',req=>{const p=new URL(req.url()).pathname;if(p.includes('/assets/images/hero-still-'))reducedRequests.push(p);});const res=await page.goto(BASE+'/study-in-germany',{waitUntil:'load',timeout:45000});await page.waitForTimeout(1700);const reducedState=await page.evaluate(()=>({transition:getComputedStyle(document.querySelector('canvas.p32-hero-still')).transitionDuration,opacity:getComputedStyle(document.querySelector('canvas.p32-hero-still')).opacity,loaded:document.querySelector('canvas.p32-hero-still').classList.contains('is-loaded')}));if(!res||res.status()!==200||reducedState.transition!=='0s'||!reducedState.loaded||!reducedRequests.includes(path640))throw Error(`Reduced-motion still behavior failed: ${JSON.stringify({status:res?.status(),reducedState,reducedRequests})}`);await reducedContext.close();
  const report={status:'PASS',browser:browser.version(),local_only:true,scene_switch_enabled:true,plain_palette_fallback_templates:['place','article'],still_asset_sizes:sizes,still_dimensions:dimensions,still_size_budgets_bytes:{mobile_lte:14000,desktop_lte:40000},cases,reduced_motion:{route:'/study-in-germany',width:360,still_loaded:true,transition:reducedState.transition,requests:reducedRequests},existing_safeguards_referenced:'Phase32 hero smoke/contrast reports cover Save-Data, slow connections, 1500ms idle fallback, noscript, text LCP and contrast; this current check focuses on measured palette fallback and scope.'};
 const out=process.env.PHASE32A_PALETTE_OUT;if(out){fs.mkdirSync(path.dirname(path.resolve(out)),{recursive:true});fs.writeFileSync(path.resolve(out),JSON.stringify(report,null,2)+'\n');}
 console.log(`PALETTE PASS ${cases.length} route/viewport cases; reduced-motion PASS; assets ${sizes.mobile_bytes}/${sizes.desktop_bytes} bytes`);
 }finally{await browser.close();}
})().catch(e=>{console.error(e.stack||e);process.exit(1)});
