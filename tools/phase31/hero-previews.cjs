#!/usr/bin/env node
// Capture approved hero-template previews and an unchanged Home control at desktop/mobile widths.
const fs=require('node:fs'),path=require('node:path'),cp=require('node:child_process'),crypto=require('node:crypto');
const {launchBrowser,routePinnedResources}=require('./browser.cjs');
const ROOT=path.resolve(__dirname,'../..');
const BASE=process.env.PHASE31_BASE_URL||'http://127.0.0.1:8080';
const dir=path.join(ROOT,'reports/screenshots/phase-31-task3');
const routes=[
 ['destination-published','/study-in-germany','.article-hero'],
 ['destination-held','/study-in-czech-republic','.article-hero'],
 ['place','/study-abroad-counselling-mysuru','.article-hero'],
 ['article-published','/blog/how-to-choose-study-abroad-consultant-karnataka','.article-hero'],
 ['article-held','/blog/italy-dsu-scholarship-eligibility','.article-hero'],
 ['blog-index','/blog/','.blog-hero'],
 ['control-home','/','#hero']
];
async function main(){
 fs.mkdirSync(dir,{recursive:true});const browser=await launchBrowser(),context=await browser.newContext({viewport:{width:1280,height:900},javaScriptEnabled:true});
 const results=[];
 try{
  const page=await context.newPage();await routePinnedResources(page);
  for(const width of [1280,360]){
   await page.setViewportSize({width,height:900});
   for(const [name,route,selector] of routes){
    const stillRequests=[];const onRequest=request=>{if(request.url().includes('/assets/images/hero-still-'))stillRequests.push(new URL(request.url()).pathname);};page.on('request',onRequest);
    const response=await page.goto(BASE+route,{waitUntil:'domcontentloaded',timeout:45000});
    if(!response||response.status()!==200)throw Error(`HTTP ${response?.status()} for ${route}`);
    await page.waitForTimeout(450);
    const hero=page.locator(selector);if(!(await hero.count()))throw Error(`Missing ${selector} for ${route} at ${width}`);
    const details=await hero.evaluate(element=>({background_image:getComputedStyle(element).backgroundImage,body_class:document.body.className,box:(()=>{const r=element.getBoundingClientRect();return{width:r.width,height:r.height}})()}));
    const file=`${name}-${width}.png`,filePath=path.join(dir,file),image=await hero.screenshot({path:filePath,animations:'disabled'});
    results.push({name,route,selector,width,height:900,http_status:response.status(),body_class:details.body_class,hero_width:details.box.width,hero_height:details.box.height,background_image:details.background_image,still_requests:stillRequests,screenshot:`reports/screenshots/phase-31-task3/${file}`,screenshot_bytes:image.length,screenshot_sha256:crypto.createHash('sha256').update(image).digest('hex')});
    page.off('request',onRequest);
   }
  }
 }finally{await browser.close();}
 const out={phase:31,task:3,source_head:cp.execFileSync('git',['rev-parse','HEAD'],{cwd:ROOT,encoding:'utf8'}).trim(),browser:'local pinned Chromium via Playwright',viewport_height:900,screenshot_count:results.length,results};
 fs.writeFileSync(path.join(ROOT,'reports/phase-31-task3-hero-previews.json'),JSON.stringify(out,null,2)+'\n');
 console.log(`PASS hero preview capture: ${results.length} screenshots, ${results.filter(x=>x.width===1280).length} desktop and ${results.filter(x=>x.width===360).length} mobile`);
}
main().catch(e=>{console.error(e.stack||e);process.exit(1)});
