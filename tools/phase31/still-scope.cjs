#!/usr/bin/env node
// Verify responsive still-image scope across the frozen 43-route local render inventory.
const fs=require('node:fs'),path=require('node:path'),cp=require('node:child_process');
const {launchBrowser,routePinnedResources}=require('./browser.cjs');
const ROOT=path.resolve(__dirname,'../..');
const BASE=process.env.PHASE31_BASE_URL||'http://127.0.0.1:8080';
const inventory=JSON.parse(fs.readFileSync(path.join(ROOT,'reports/phase-25-baseline-renders.json'),'utf8')).routes;
const routes=Object.keys(inventory).sort(),widths=[360,768,1280];
const template=route=>route.startsWith('/study-in-')?'destination':route.startsWith('/study-abroad-')?'place':route==='/blog/'?'blog':route.startsWith('/blog/')?'article':null;
async function main(){
 if(routes.length!==43)throw Error(`expected 43 frozen routes, got ${routes.length}`);
 const browser=await launchBrowser(),context=await browser.newContext({viewport:{width:1280,height:900},javaScriptEnabled:true,reducedMotion:'no-preference'});
 const cases=[],observedResponses=[];
 try{
  for(const route of routes){
   const kind=template(route),selector=kind==='blog'?'.blog-hero':kind?'.article-hero':null;
   for(const width of widths){
    const page=await context.newPage();await page.setViewportSize({width,height:900});await routePinnedResources(page);
    const requests=[];page.on('request',r=>{if(r.url().includes('/assets/images/hero-still-'))requests.push(new URL(r.url()).pathname);});
    page.on('response',r=>{if(r.url().includes('/assets/images/hero-still-'))observedResponses.push({path:new URL(r.url()).pathname,status:r.status()});});
    const response=await page.goto(BASE+(route==='/'?'/':route),{waitUntil:'domcontentloaded',timeout:45000});
    if(!response||response.status()!==200)throw Error(`HTTP ${response?.status()} for ${route}`);
    await page.waitForTimeout(100);
    const state=await page.evaluate(sel=>{
     const style=document.querySelector('#ilmera-visual-system')?.textContent||'';
     const hero=sel?document.querySelector(sel):null;
     return{body_class:document.body.className,hero_exists:!!hero,background_image:hero?getComputedStyle(hero).backgroundImage:'',style_still_refs:(style.match(/\/assets\/images\/hero-still-/g)||[]).length};
    },selector);
    const expected=kind?(width<=768?'/assets/images/hero-still-720.webp':'/assets/images/hero-still-1440.webp'):null;
    if(kind){
     if(!state.body_class.split(/\s+/).includes('p25-'+kind))throw Error(`wrong body template for ${route}: ${state.body_class}`);
     if(!state.hero_exists||state.style_still_refs!==2||!state.background_image.includes(expected))throw Error(`missing responsive still for ${route} ${width}: ${JSON.stringify(state)}`);
    }else if(state.style_still_refs!==0||state.background_image.includes('hero-still-')||requests.length){
     throw Error(`still escaped approved template scope for ${route} ${width}: ${JSON.stringify({state,requests})}`);
    }
    cases.push({route,width,template:kind||'none',expected_still:expected,body_class:state.body_class,hero_exists:state.hero_exists,computed_background_image:state.background_image,inline_still_url_count:state.style_still_refs,still_requests:requests,http_status:response.status()});
    await page.close();
   }
  }
 }finally{await browser.close();}
 for(const required of ['/assets/images/hero-still-720.webp','/assets/images/hero-still-1440.webp']){
  if(!observedResponses.some(x=>x.path===required&&x.status===200))throw Error(`responsive still failed to load: ${required}`);
 }
 const allowed=cases.filter(x=>x.template!=='none');
 const heldRoutes=routes.filter(route=>inventory[route]?.info?.status==='draft'&&template(route));
 const heldDestinations=heldRoutes.filter(route=>template(route)==='destination');
 const out={phase:31,task:3,passed:true,source_head:cp.execFileSync('git',['rev-parse','HEAD'],{cwd:ROOT,encoding:'utf8'}).trim(),browser:'local pinned Chromium via Playwright',route_count:routes.length,widths,case_count:cases.length,allowed_templates:['destination','place','article','blog'],allowed_route_count:[...new Set(allowed.map(x=>x.route))].length,approved_held_routes:heldRoutes,approved_held_destinations:heldDestinations,responsive_assets:observedResponses,checks:['still CSS appears only on approved template outputs','held destination and article routes keep their approved template role and still','360px and 768px use 720px still','1280px uses 1440px still','at least one successful response for each responsive asset','reference, legal and utility routes do not request or embed the still'],cases};
 fs.writeFileSync(path.join(ROOT,'reports/phase-31-task3-still-scope.json'),JSON.stringify(out,null,2)+'\n');
 console.log(`PASS responsive still scope: ${cases.length} route/viewport cases; ${allowed.length} approved-template views; ${heldDestinations.length} held destination routes; ${heldRoutes.length} held eligible routes total`);
}
main().catch(e=>{console.error(e.stack||e);process.exit(1)});
