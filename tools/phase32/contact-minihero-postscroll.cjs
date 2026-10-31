#!/usr/bin/env node
// Match Phase31's full-scroll, settle and return-to-top state for Contact #miniHero only.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const ROOT=path.resolve(__dirname,'../..');const BASE=process.env.PHASE32_BASE_URL||'http://127.0.0.1:8084';
process.env.PHASE31_BASE_URL=BASE;
const {launchBrowser,routePinnedResources}=require('../phase31/browser.cjs');
const OUT=path.resolve(process.env.PHASE32_CONTACT_POSTSCROLL_OUT||'/home/user/phase32-runtime/phase32-contact-tail-postscroll.json');
const widths=[360,768,1280],jsStates=['on','off'],motions=['normal','reduced'];
async function measure(page){return page.locator('#miniHero').evaluate(hero=>{
 const box=e=>{const r=e.getBoundingClientRect();return{x:+r.x.toFixed(2),y:+(r.top+scrollY).toFixed(2),width:+r.width.toFixed(2),height:+r.height.toFixed(2),bottom:+(r.bottom+scrollY).toFixed(2)}};
 const visible=e=>{let opacity=1;for(let n=e;n&&n.nodeType===1;n=n.parentElement){const s=getComputedStyle(n);if(s.display==='none'||s.visibility==='hidden'||s.contentVisibility==='hidden')return false;opacity*=Number.parseFloat(s.opacity)||0;}return opacity>=.05;};
 const texts=[];const walker=document.createTreeWalker(hero,NodeFilter.SHOW_TEXT);let node;
 while((node=walker.nextNode())){const text=(node.nodeValue||'').replace(/\s+/g,' ').trim(),parent=node.parentElement;if(!text||!parent||!visible(parent))continue;let absolute=false;for(let n=parent;n&&n!==hero;n=n.parentElement){const s=getComputedStyle(n);if(s.position==='absolute'||s.position==='fixed'){absolute=true;break;}}const range=document.createRange();range.selectNodeContents(node);const r=range.getBoundingClientRect();if(r.width<.5||r.height<.5)continue;texts.push({text:text.slice(0,140),selector:parent.id?'#'+parent.id:parent.tagName.toLowerCase()+(parent.classList.length?'.'+[...parent.classList].slice(0,2).join('.') :''),top:+(r.top+scrollY).toFixed(2),bottom:+(r.bottom+scrollY).toFixed(2),absolute,inside_scroll_cue:!!parent.closest('#scrollInd,.scroll-ind,.scroll-cue'),inside_hud:!!parent.closest('.hud-item')});}
 const inFlow=texts.filter(t=>!t.absolute&&!t.inside_scroll_cue&&!t.inside_hud),lastFlow=inFlow.reduce((m,t)=>Math.max(m,t.bottom),0),lastAny=texts.reduce((m,t)=>Math.max(m,t.bottom),0);
 const cue=hero.querySelector('#scrollInd,.scroll-ind,.scroll-cue'),cueStyle=cue?getComputedStyle(cue):null,cueBox=cue?box(cue):null;
 return{hero:box(hero),hero_style:{min_height:getComputedStyle(hero).minHeight,height:getComputedStyle(hero).height,display:getComputedStyle(hero).display,position:getComputedStyle(hero).position,padding_top:getComputedStyle(hero).paddingTop,padding_bottom:getComputedStyle(hero).paddingBottom},scroll_cue:cue?{rect:cueBox,display:cueStyle.display,visibility:cueStyle.visibility,opacity:cueStyle.opacity,position:cueStyle.position,bottom:cueStyle.bottom,text:(cue.innerText||'').replace(/\s+/g,' ').trim(),aria_hidden:cue.getAttribute('aria-hidden'),text_visible:visible(cue)}:null,visible_text:texts,flow_text_bottom:lastFlow,any_visible_text_bottom:lastAny,tail_after_flow_text:+Math.max(0,box(hero).bottom-lastFlow).toFixed(2),tail_after_visible_text:+Math.max(0,box(hero).bottom-lastAny).toFixed(2),cue_bottom_gap:cueBox?+Math.max(0,box(hero).bottom-cueBox.bottom).toFixed(2):null,scroll_y:Math.round(scrollY)};
});}
async function scrollLikePhase31(page){
 const height=await page.evaluate(()=>Math.max(document.documentElement.scrollHeight,document.body.scrollHeight));
 const viewport=await page.evaluate(()=>innerHeight),step=Math.max(500,Math.round(viewport*.68)),width=await page.evaluate(()=>innerWidth);
 await page.mouse.move(Math.floor(width/2),Math.floor(viewport/2));let samples=0;
 for(let y=0;y<height;y+=step){await page.mouse.wheel(0,Math.min(step,height-y));await page.waitForTimeout(60);samples++;}
 await page.waitForTimeout(3000);await page.mouse.wheel(0,-(height+viewport));await page.waitForTimeout(150);
 if((await page.evaluate(()=>window.scrollY))>2){await page.evaluate(()=>{document.documentElement.style.scrollBehavior='auto';document.body.style.scrollBehavior='auto';window.scrollTo(0,0);});await page.waitForFunction(()=>window.scrollY<=2,{timeout:5000});}
 return{document_height:height,viewport_height:viewport,scroll_samples:samples,settle_ms:3000,returned_to_top:(await page.evaluate(()=>window.scrollY))<=2,final_scroll_y:Math.round(await page.evaluate(()=>window.scrollY))};
}
async function main(){
 if(fs.existsSync(OUT))throw Error(`Refusing to overwrite ${OUT}`);
 const browser=await launchBrowser(),contexts={},rows=[];
 for(const js of jsStates)contexts[js]=await browser.newContext({viewport:{width:360,height:900},deviceScaleFactor:1,javaScriptEnabled:js==='on'});
 try{for(const width of widths)for(const js of jsStates)for(const motion of motions){
  const page=await contexts[js].newPage();await page.setViewportSize({width,height:900});await page.emulateMedia({reducedMotion:motion==='reduced'?'reduce':'no-preference'});await routePinnedResources(page);
  const response=await page.goto(BASE+'/contact',{waitUntil:'domcontentloaded',timeout:45000});if(!response||response.status()!==200)throw Error(`HTTP ${response?.status()} at width ${width}`);
  await page.waitForTimeout(500);const scrolling=await scrollLikePhase31(page);const metrics=await measure(page);
  rows.push({route:'/contact',width,javascript:js,motion,http_status:response.status(),scrolling,metrics});
  console.log(`POSTSCROLL ${width} JS-${js} ${motion} scrollY=${metrics.scroll_y} cue-opacity=${metrics.scroll_cue?.opacity} flow-tail=${metrics.tail_after_flow_text} cue-gap=${metrics.cue_bottom_gap}`);
  await page.close();
 }}finally{for(const context of Object.values(contexts))await context.close().catch(()=>{});await browser.close();}
 const result={phase:32,task:'contact_miniHero_post_scroll_tail_inspection',generated_at:new Date().toISOString(),source_head:require('node:child_process').execFileSync('git',['rev-parse','HEAD'],{cwd:ROOT,encoding:'utf8'}).trim(),base_url:BASE,browser:browser.version(),route:'/contact',widths,javascript:jsStates,motion:motions,case_count:rows.length,complete:rows.length===12,method:'Pinned local Chromium/Playwright. Mirrors Phase31 slow wheel scroll, 3-second settle, return to top and fallback; measures only #miniHero and its cue. No sharp or pixel analysis.',rows};
 const data=JSON.stringify(result,null,2)+'\n';fs.writeFileSync(OUT,data);console.log(`AUDIT COMPLETE ${rows.length} ${OUT} sha256=${crypto.createHash('sha256').update(data).digest('hex')}`);
}
main().catch(e=>{console.error(e.stack||e);process.exit(1)});
