// Pinned local browser bootstrap for repeatable Phase31 evidence.
const path=require('node:path');
const fs=require('node:fs');
const {chromium:playwright}=require('playwright');
const sparticuz=require('@sparticuz/chromium');
const {inflate}=require(path.join(process.env.PHASE31_RUNTIME||'/home/user/phase31/runtime/node_modules','@sparticuz/chromium/build/cjs/lambdafs.cjs'));
const RUNTIME=process.env.PHASE31_RUNTIME||'/home/user/phase31/runtime/node_modules';
const BASE_URL=process.env.PHASE31_BASE_URL||'http://127.0.0.1:8080';
let extracted;
async function launchBrowser(){
  if(!extracted){
    extracted=await inflate(path.join(RUNTIME,'@sparticuz/chromium/bin/al2023.tar.br'));
    process.env.LD_LIBRARY_PATH=path.join(extracted,'lib')+':'+(process.env.LD_LIBRARY_PATH||'');
  }
  const executablePath=await sparticuz.executablePath();
  const browser=await playwright.launch({headless:true,executablePath,args:sparticuz.args});
  const expected='143.';
  if(!browser.version().startsWith(expected))throw new Error(`Pinned Chromium expected ${expected}x, got ${browser.version()}`);
  return browser;
}
async function routePinnedResources(page){
  const gsapDir=path.join(RUNTIME,'gsap/dist');
  const threeDir=path.join(RUNTIME,'three/build');
  await page.route('**/*',async route=>{
    const u=new URL(route.request().url());
    if(u.hostname==='cdnjs.cloudflare.com'){
      let f=null;
      if(u.pathname==='/ajax/libs/gsap/3.12.2/gsap.min.js')f=path.join(gsapDir,'gsap.min.js');
      if(u.pathname==='/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js')f=path.join(gsapDir,'ScrollTrigger.min.js');
      if(u.pathname==='/ajax/libs/three.js/r128/three.min.js')f=path.join(threeDir,'three.min.js');
      if(f&&fs.existsSync(f))return route.fulfill({status:200,contentType:'text/javascript; charset=utf-8',body:fs.readFileSync(f)});
      return route.abort('blockedbyclient');
    }
    if(u.hostname==='fonts.googleapis.com'||u.hostname==='fonts.gstatic.com')return route.abort('blockedbyclient');
    if(u.hostname==='ilmerastudyabroad.com'){
      const target=BASE_URL+u.pathname+u.search;
      const response=await route.fetch({url:target});
      return route.fulfill({response});
    }
    if(u.hostname==='127.0.0.1'||u.hostname==='localhost')return route.continue();
    return route.abort('blockedbyclient');
  });
}
module.exports={launchBrowser,routePinnedResources};
