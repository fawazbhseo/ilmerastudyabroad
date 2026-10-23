// Fonts and exact CDN script versions mirrored from npm. Motion frozen for comparison.
const {chromium}=require('playwright'),packed=require('@sparticuz/chromium'),fs=require('fs'),path=require('path'),{resources}=require('./resources.cjs');
const {PNG}=require('pngjs');
const routes={'home':'/','services':'/services','about':'/about','contact':'/contact','germany':'/study-in-germany','mysuru':'/study-abroad-counselling-mysuru','article':'/blog/how-to-choose-study-abroad-consultant-karnataka','blog':'/blog/'};
(async()=>{const phase=process.argv[2]||'before',out='reports/screenshots/phase-25';fs.mkdirSync(out,{recursive:true});const browser=await chromium.launch({executablePath:await packed.executablePath(),args:packed.args.filter(a=>!['--single-process','--in-process-gpu'].includes(a)),headless:true});const data=[];
 for(const width of [360,768,1280])for(const [name,route] of Object.entries(routes)){
 const ctx=await browser.newContext({viewport:{width,height:900},deviceScaleFactor:1});await ctx.route('**/*',resources);
 await ctx.addInitScript(()=>{let seed=8127;Math.random=()=>((seed=(seed*16807)%2147483647)-1)/2147483646;performance.now=()=>1000;window.requestAnimationFrame=()=>1;window.cancelAnimationFrame=()=>{};});
 const page=await ctx.newPage();await page.goto('http://127.0.0.1:8080'+route,{waitUntil:'networkidle'});await page.evaluate(()=>document.fonts.ready);
 await page.evaluate(()=>{if(window.gsap){gsap.globalTimeline.getChildren(true,true,true).forEach(a=>a.progress(1));gsap.ticker.sleep();}});
 await page.addStyleTag({content:'html{scroll-behavior:auto!important;} .reveal,.reveal-l,.reveal-r,.anim,.anim-up,.anim-left,.anim-right{opacity:1!important;transform:none!important;}*,*::before,*::after{animation:none!important;transition:none!important;caret-color:transparent!important;}'});
 // Load existing lazy portraits without changing their dimensions or crop.
 await page.locator('img[loading=lazy]').evaluateAll(es=>es.forEach(e=>e.loading='eager'));await page.waitForTimeout(200);
 const row=await page.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight,fonts:document.fonts.status,teams:[...document.querySelectorAll('#team .team-card,#team .testi-card')].map(e=>({height:e.getBoundingClientRect().height,width:e.getBoundingClientRect().width,name:e.querySelector('.team-name,.testi-name')?.textContent.trim(),bio:e.querySelector('.team-bio,.testi-text')?.textContent.trim(),rect:{x:e.getBoundingClientRect().x,y:e.getBoundingClientRect().y,width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height}}))}));
 // SwiftShader full-page surfaces above 8192px can repeat tiles. Stitch actual
 // viewport rasters instead. Fixed navigation appears only in the first tile.
 const stitched=new PNG({width,height:row.height});
 for(let y=0;y<row.height;y+=900){
  await page.evaluate(y=>{window.scrollTo(0,y);document.querySelector('#il-nav')?.style.setProperty('visibility',y?'hidden':'visible','important');},y);await page.waitForTimeout(40);
  const actual=await page.evaluate(()=>scrollY),tile=PNG.sync.read(await page.screenshot({animations:'disabled'}));
  PNG.bitblt(tile,stitched,0,y-actual,width,Math.min(900,row.height-y),0,y);
 }
 fs.writeFileSync(`${out}/${phase}-${name}-${width}.png`,PNG.sync.write(stitched));data.push({phase,name,route,...row});await ctx.close();console.log(phase,name,width,row.height);
 }await browser.close();fs.writeFileSync(`reports/phase-25-${phase}-layout.json`,JSON.stringify(data,null,2)+'\n');
})().catch(e=>{console.error(e);process.exit(1)});
