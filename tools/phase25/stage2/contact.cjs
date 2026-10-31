// Fonts and exact CDN script versions mirrored from npm. Motion frozen for comparison.
const {chromium}=require('playwright'),packed=require('@sparticuz/chromium'),fs=require('fs'),path=require('path'),{resources}=require('../resources.cjs');
const {PNG}=require('pngjs');
const routes={'services':'/services','germany':'/study-in-germany','mysuru':'/study-abroad-counselling-mysuru','article':'/blog/how-to-choose-study-abroad-consultant-karnataka','blog':'/blog/','privacy':'/privacy-policy','all-pages':'/all-pages','404':'/404'};
(async()=>{const phase=process.argv[2]||'before',out=process.env.SHOTS_OUT||'/home/user/phase25-evidence/s2/contact';fs.mkdirSync(out,{recursive:true});const browser=await chromium.launch({executablePath:await packed.executablePath(),args:[...packed.args.filter(a=>!['--single-process','--in-process-gpu'].includes(a)),'--disable-gpu-compositing','--disable-skia-runtime-opts','--force-color-profile=srgb','--disable-lcd-text','--run-all-compositor-stages-before-draw','--disable-threaded-animation','--disable-threaded-scrolling'],headless:true});const data=[],baseline=process.argv.includes('--baseline')?JSON.parse(fs.readFileSync('reports/phase-25-baseline-renders.json','utf8')):null;
 for(const width of [360,1280])for(const [name,route] of Object.entries(routes)){
 if(process.argv.includes('--wide')&&width!==1280)continue;const only=process.argv.find(s=>s.startsWith('--names='));if(only&&!only.slice(8).split(',').includes(name))continue;
 if(process.argv.includes('--pilots')&&['home','about','services','contact'].includes(name))continue;
 if(process.argv.includes('--teams')&&!['home','about'].includes(name))continue;
 const ctx=await browser.newContext({viewport:{width,height:900},deviceScaleFactor:1});await ctx.route('**/*',async r=>{if(r.request().isNavigationRequest()&&new URL(r.request().url()).hostname==='127.0.0.1'){
 const html=baseline?baseline.routes[route].html:await(await r.fetch()).text();
 const freeze='html{scroll-behavior:auto!important;} .why-card,.testi-card,.special-card,.reveal,.reveal-l,.reveal-r,[class*="anim-"]{opacity:1!important;transform:none!important;will-change:auto!important;} *,*::before,*::after{animation:none!important;transition:none!important;}';
 return r.fulfill({status:200,contentType:'text/html',body:html.replace('</head>','<style>'+freeze+'</style></head>')});
 }return resources(r);});
 await ctx.addInitScript(()=>{const get=HTMLCanvasElement.prototype.getContext;HTMLCanvasElement.prototype.getContext=function(...args){const c=get.apply(this,args);if(String(args[0]).includes('webgl'))c?.disable(c.DITHER);return c;};let seed=8127;Math.random=()=>((seed=(seed*16807)%2147483647)-1)/2147483646;performance.now=()=>1000;Date.now=()=>1792713600000;const realTimeout=window.setTimeout.bind(window);window.setTimeout=(f,...a)=>!document.querySelector('body.p25')&&f?.name==='spawnEl'?1:realTimeout(f,...a);const realInterval=window.setInterval.bind(window);window.setInterval=(f,...a)=>document.querySelector('body.p25')?realInterval(f,...a):1;const realRAF=window.requestAnimationFrame.bind(window);window.requestAnimationFrame=f=>document.querySelector('body.p25')?realRAF(f):1;window.cancelAnimationFrame=()=>{};});
 const page=await ctx.newPage();await page.goto('http://127.0.0.1:8080'+route,{waitUntil:'networkidle'});await page.evaluate(()=>document.fonts.ready);
 await page.evaluate(()=>{if(window.gsap){gsap.globalTimeline.getChildren(true,true,true).forEach(a=>a.progress(1));gsap.ticker.sleep();}});
 await page.addStyleTag({content:'html{scroll-behavior:auto!important;} .why-card,.testi-card,.special-card{will-change:auto!important;} .why-card,.testi-card,.special-card,.reveal,.reveal-l,.reveal-r,.anim,.anim-up,.anim-left,.anim-right,[class*="anim-"]{opacity:1!important;transform:none!important;}*,*::before,*::after{animation:none!important;transition:none!important;caret-color:transparent!important;}'});
 // Load existing lazy portraits without changing their dimensions or crop.
 await page.locator('img[loading=lazy]').evaluateAll(es=>es.forEach(e=>e.loading='eager'));await page.waitForTimeout(200);
 const row=await page.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight,teamSection:(()=>{let e=document.querySelector('#team');if(!e)return null;let r=e.getBoundingClientRect();return {x:r.x,y:r.y,width:r.width,height:r.height};})(),fonts:document.fonts.status,teams:[...document.querySelectorAll('#team .team-card,#team .testi-card')].map(e=>({height:e.getBoundingClientRect().height,width:e.getBoundingClientRect().width,name:e.querySelector('.team-name,.testi-name')?.textContent.trim(),bio:e.querySelector('.team-bio,.testi-text')?.textContent.trim(),rect:{x:e.getBoundingClientRect().x,y:e.getBoundingClientRect().y,width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height}}))}));
 // SwiftShader full-page surfaces above 8192px can repeat tiles. Stitch actual
 // viewport rasters instead. Fixed navigation appears only in the first tile.
 if(process.argv.includes('--measure-only')){data.push({phase,name,route,...row});await ctx.close();continue;}
 const stitched=new PNG({width,height:row.height});
 for(let y=0;y<row.height;y+=900){
  await page.evaluate(y=>{window.scrollTo(0,y);document.querySelector('#il-nav')?.style.setProperty('visibility',y?'hidden':'visible','important');},y);await page.waitForTimeout(40);
  const actual=await page.evaluate(()=>scrollY),tile=PNG.sync.read(await page.screenshot({animations:'disabled'}));
  PNG.bitblt(tile,stitched,0,y-actual,width,Math.min(900,row.height-y),0,y);
 }
 fs.writeFileSync(`${out}/${phase}-${name}-${width}.png`,PNG.sync.write(stitched));data.push({phase,name,route,...row});await ctx.close();console.log(phase,name,width,row.height);
 }await browser.close();if(process.argv.includes('--pilots')||process.argv.some(s=>s.startsWith('--names='))){const old=fs.existsSync(`${out}/${phase}-layout.json`)?JSON.parse(fs.readFileSync(`${out}/${phase}-layout.json`,'utf8')):[];const keys=new Set(data.map(r=>r.name+':'+r.width));data.push(...old.filter(r=>!keys.has(r.name+':'+r.width)));}fs.writeFileSync(`${out}/${phase}-layout.json`,JSON.stringify(data,null,2)+'\n');
})().catch(e=>{console.error(e);process.exit(1)});
