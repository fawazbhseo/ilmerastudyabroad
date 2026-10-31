#!/usr/bin/env node
// Inspect retained #miniHero tails and the bottom scroll cue on Contact at three widths.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const {launchBrowser,routePinnedResources}=require('../phase31/browser.cjs');
const ROOT=path.resolve(__dirname,'../..');const BASE=process.env.PHASE32_BASE_URL||process.env.PHASE31_BASE_URL||'http://127.0.0.1:8084';
const OUT=path.resolve(process.env.PHASE32_CONTACT_MINIHERO_OUT||path.join(ROOT,'reports/phase-32-contact-minihero-audit.json'));
const route='/contact',widths=[360,768,1280],jsStates=['on','off'],motions=['normal','reduced'];
async function main(){
 if(fs.existsSync(OUT))throw Error(`Refusing to overwrite ${OUT}`);
 const browser=await launchBrowser();const rows=[];
 try{
  for(const width of widths)for(const js of jsStates)for(const motion of motions){
   const context=await browser.newContext({viewport:{width,height:900},deviceScaleFactor:1,javaScriptEnabled:js==='on',reducedMotion:motion==='reduced'?'reduce':'no-preference'});
   const page=await context.newPage();await routePinnedResources(page);
   const response=await page.goto(BASE+route,{waitUntil:'domcontentloaded',timeout:45000});if(!response||response.status()!==200)throw Error(`HTTP ${response?.status()} for ${route} ${width}`);
   await page.waitForTimeout(500);
   const metrics=await page.locator('#miniHero').evaluate(hero=>{
    const rect=e=>{const r=e.getBoundingClientRect();return{x:+r.x.toFixed(2),y:+(r.top+scrollY).toFixed(2),width:+r.width.toFixed(2),height:+r.height.toFixed(2),bottom:+(r.bottom+scrollY).toFixed(2)}};
    const isVisible=e=>{let opacity=1;for(let n=e;n&&n.nodeType===1;n=n.parentElement){const s=getComputedStyle(n);if(s.display==='none'||s.visibility==='hidden'||s.contentVisibility==='hidden')return false;opacity*=Number.parseFloat(s.opacity)||0;}return opacity>=.05;};
    const texts=[];const walker=document.createTreeWalker(hero,NodeFilter.SHOW_TEXT);let node;
    while((node=walker.nextNode())){const text=(node.nodeValue||'').replace(/\s+/g,' ').trim(),parent=node.parentElement;if(!text||!parent||!isVisible(parent))continue;let absolute=false;for(let n=parent;n&&n!==hero;n=n.parentElement){const s=getComputedStyle(n);if(s.position==='absolute'||s.position==='fixed'){absolute=true;break;}}const range=document.createRange();range.selectNodeContents(node);const r=range.getBoundingClientRect();if(r.width<.5||r.height<.5)continue;texts.push({text:text.slice(0,140),selector:parent.id?'#'+parent.id:parent.tagName.toLowerCase()+(parent.classList.length?'.'+[...parent.classList].slice(0,2).join('.') :''),top:+(r.top+scrollY).toFixed(2),bottom:+(r.bottom+scrollY).toFixed(2),absolute,inside_scroll_cue:!!parent.closest('#scrollInd,.scroll-ind,.scroll-cue'),inside_hud:!!parent.closest('.hud-item')});}
    const inFlow=texts.filter(t=>!t.absolute&&!t.inside_scroll_cue&&!t.inside_hud);const lastFlow=inFlow.reduce((m,t)=>Math.max(m,t.bottom),0);const lastText=texts.reduce((m,t)=>Math.max(m,t.bottom),0);
    const cue=hero.querySelector('#scrollInd,.scroll-ind,.scroll-cue');const cueStyle=cue?getComputedStyle(cue):null;const cueRect=cue?rect(cue):null;const inner=hero.querySelector('.mini-inner');
    return{hero:rect(hero),hero_style:{min_height:getComputedStyle(hero).minHeight,height:getComputedStyle(hero).height,display:getComputedStyle(hero).display,position:getComputedStyle(hero).position,padding_top:getComputedStyle(hero).paddingTop,padding_bottom:getComputedStyle(hero).paddingBottom},mini_inner:inner?rect(inner):null,scroll_cue:cue?{selector:cue.id?'#'+cue.id:'.'+[...cue.classList].join('.'),rect:cueRect,display:cueStyle.display,visibility:cueStyle.visibility,opacity:cueStyle.opacity,position:cueStyle.position,bottom:cueStyle.bottom,text:(cue.innerText||'').replace(/\s+/g,' ').trim(),aria_hidden:cue.getAttribute('aria-hidden')}:null,visible_text:texts,flow_text_bottom:lastFlow,any_text_bottom:lastText,tail_after_flow_text:+Math.max(0,rect(hero).bottom-lastFlow).toFixed(2),tail_after_any_text:+Math.max(0,rect(hero).bottom-lastText).toFixed(2),cue_bottom_gap:cueRect?+Math.max(0,rect(hero).bottom-cueRect.bottom).toFixed(2):null,window:{inner_width:innerWidth,inner_height:innerHeight,device_pixel_ratio:devicePixelRatio}};
   });
   rows.push({route,width,javascript:js,motion,http_status:response.status(),metrics});
   await page.close();await context.close();
   console.log(`CONTACT ${width} JS-${js} ${motion} hero=${metrics.hero.height}px flow-tail=${metrics.tail_after_flow_text}px cue-gap=${metrics.cue_bottom_gap}px`);
  }
 }finally{await browser.close();}
 const result={phase:32,task:'contact_miniHero_tail_inspection',generated_at:new Date().toISOString(),source_head:require('node:child_process').execFileSync('git',['rev-parse','HEAD'],{cwd:ROOT,encoding:'utf8'}).trim(),base_url:BASE,browser:browser.version(),route,widths,javascript:jsStates,motion:motions,case_count:rows.length,complete:rows.length===12,method:'Pinned local Chromium/Playwright. Measure visible #miniHero text, flow content, absolute bottom scroll cue, CSS min-height and tails after DOMContentLoaded plus 500ms. No production request.',rows};
 fs.writeFileSync(OUT,JSON.stringify(result,null,2)+'\n');console.log(`AUDIT COMPLETE ${rows.length} ${OUT} sha256=${crypto.createHash('sha256').update(fs.readFileSync(OUT)).digest('hex')}`);
}
main().catch(e=>{console.error(e.stack||e);process.exit(1)});
