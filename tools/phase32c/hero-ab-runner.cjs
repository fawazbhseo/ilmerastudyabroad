#!/usr/bin/env node
'use strict';

// One local-only Phase32c Task 3 run. No retries, resume, concurrent samples or analysis.
const fs=require('node:fs');
const path=require('node:path');
const http=require('node:http');
const crypto=require('node:crypto');
const {pathToFileURL}=require('node:url');
const {chromium}=require('playwright');
const packed=require('@sparticuz/chromium');
const {resources}=require('../phase25/resources.cjs');
const ROOT=path.resolve(__dirname,'../..');
const RUNTIME=process.env.PHASE32_RUNTIME||'/home/user/phase32c-runtime/node_modules';
const EVIDENCE=path.resolve(process.env.PHASE32C_HERO_EVIDENCE||'/home/user/phase32c-runtime/hero-ab');
const FIXTURE_PATH=path.join(EVIDENCE,'fixtures.json');
const MANIFEST_PATH=path.join(ROOT,'reports/phase-32c-hero-ab-fixtures.json');
const OUTPUT=path.resolve(process.env.PHASE32C_HERO_AB_RAW||path.join(EVIDENCE,'raw-samples.json'));
const PORT=Number(process.env.PHASE32C_HERO_AB_PORT||8091);
const BASE=`http://127.0.0.1:${PORT}`;
const ROUTES=[
  '/study-abroad-counselling-mysuru',
  '/blog/how-to-choose-study-abroad-consultant-karnataka',
];
const ARMS=['A','B-still','B-plain'];
const PRIMARY_ORDERS=[
  ['A','B-still','B-plain'],
  ['A','B-plain','B-still'],
  ['B-still','A','B-plain'],
  ['B-still','B-plain','A'],
  ['B-plain','A','B-still'],
  ['B-plain','B-still','A'],
  ['A','B-still','B-plain'],
  ['B-still','B-plain','A'],
  ['B-plain','A','B-still'],
];
const ORDER={
  added_transfer_bytes_strictly_less_than:150000,
  no_new_render_blocking_resource:true,
  CLS_no_worse_than_A_and_below:0.1,
  LCP_B_over_A_at_most:1.10,
  TBT_increase_ms_at_most:50,
};
const sha=bytes=>crypto.createHash('sha256').update(bytes).digest('hex');
const writeJson=(file,value)=>{
  const tmp=file+'.tmp';
  fs.writeFileSync(tmp,JSON.stringify(value,null,2)+'\n');
  fs.renameSync(tmp,file);
};
const mime=file=>({
  '.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8',
  '.png':'image/png','.webp':'image/webp','.jpg':'image/jpeg','.jpeg':'image/jpeg',
  '.svg':'image/svg+xml','.ico':'image/x-icon','.woff2':'font/woff2',
  '.txt':'text/plain; charset=utf-8','.xml':'application/xml; charset=utf-8',
  '.json':'application/json; charset=utf-8','.html':'text/html; charset=utf-8',
})[path.extname(file).toLowerCase()]||'application/octet-stream';
const sources={
  'A':path.join(EVIDENCE,'source/A'),
  'B-still':path.join(EVIDENCE,'source/B-still-ac2'),
  'B-plain':path.join(EVIDENCE,'source/B-plain-ac2'),
};
let fixtures=null;
let active={route:null,arm:null};
let extractedRuntime=null;
let fixtureServer=null;

function chromeArgs(){
  return[...packed.args.filter(arg=>!['--single-process','--in-process-gpu'].includes(arg)),'--remote-debugging-port=9222'];
}
async function ensureChromiumRuntime(){
  if(!extractedRuntime){
    const {inflate}=require(path.join(RUNTIME,'@sparticuz/chromium/build/cjs/lambdafs.cjs'));
    extractedRuntime=await inflate(path.join(RUNTIME,'@sparticuz/chromium/bin/al2023.tar.br'));
    process.env.LD_LIBRARY_PATH=path.join(extractedRuntime,'lib')+':'+(process.env.LD_LIBRARY_PATH||'');
  }
}
function send(res,status,body,contentType){
  const bytes=Buffer.isBuffer(body)?body:Buffer.from(body);
  res.writeHead(status,{'Content-Type':contentType,'Content-Length':bytes.length,'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'});
  res.end(bytes);
}
function startFixtureServer(){
  fixtureServer=http.createServer((req,res)=>{
    let pathname;
    try{pathname=decodeURIComponent(new URL(req.url,BASE).pathname);}catch{return send(res,400,'Bad request','text/plain; charset=utf-8');}
    if(req.method!=='GET'&&req.method!=='HEAD')return send(res,405,'Method not allowed','text/plain; charset=utf-8');
    if(pathname===active.route&&fixtures[active.route]?.[active.arm]){
      const body=Buffer.from(fixtures[active.route][active.arm]);
      res.writeHead(200,{'Content-Type':'text/html; charset=utf-8','Content-Length':body.length,'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'});
      return res.end(req.method==='HEAD'?undefined:body);
    }
    if(pathname.startsWith('/assets/')){
      const root=sources[active.arm];
      const file=path.resolve(root,'.'+pathname);
      if(!root||!file.startsWith(root+path.sep)||!fs.existsSync(file)||!fs.statSync(file).isFile())return send(res,404,'Not found','text/plain; charset=utf-8');
      const body=fs.readFileSync(file);
      res.writeHead(200,{'Content-Type':mime(file),'Content-Length':body.length,'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'});
      return res.end(req.method==='HEAD'?undefined:body);
    }
    return send(res,404,'Not found','text/plain; charset=utf-8');
  });
  return new Promise((resolve,reject)=>{
    fixtureServer.once('error',reject);
    fixtureServer.listen(PORT,'127.0.0.1',()=>resolve());
  });
}
function closeFixtureServer(){
  return new Promise(resolve=>{if(!fixtureServer)return resolve();fixtureServer.close(()=>resolve());});
}
async function routeResources(route,arm){
  const u=new URL(route.request().url());
  if((u.hostname==='ilmerastudyabroad.com'||u.hostname==='www.ilmerastudyabroad.com')&&u.pathname.startsWith('/assets/')){
    const root=sources[arm];
    const file=path.resolve(root,'.'+decodeURIComponent(u.pathname));
    if(!file.startsWith(root+path.sep)||!fs.existsSync(file)||!fs.statSync(file).isFile())return route.abort('blockedbyclient');
    return route.fulfill({status:200,body:fs.readFileSync(file),contentType:mime(file),headers:{'Cache-Control':'no-store','Access-Control-Allow-Origin':'*'}});
  }
  return resources(route);
}
function observePage(context,events,failures){
  const attach=page=>{
    page.on('requestfailed',request=>failures.push({url:request.url(),failure:request.failure()?.errorText||'unknown'}));
  };
  for(const page of context.pages())attach(page);
  context.on('page',attach);
  context.exposeBinding('__p32cEmit',(_,event)=>events.push(event));
  context.addInitScript(()=>{
    const emit=event=>window.__p32cEmit(event).catch(()=>{});
    const watch=()=>{
      if(!document.documentElement)return false;
      new MutationObserver(()=>emit({kind:'paint_gate',time:performance.now(),pending:document.documentElement.classList.contains('p25-font-pending')})).observe(document.documentElement,{attributes:true,attributeFilter:['class']});
      return true;
    };
    if(!watch()){
      const observer=new MutationObserver(()=>{if(watch())observer.disconnect();});
      observer.observe(document,{childList:true});
    }
    if(document.fonts)document.fonts.addEventListener('loadingdone',()=>emit({kind:'fonts_ready',time:performance.now(),faces:[...document.fonts].map(face=>({family:face.family,weight:face.weight,status:face.status}))}));
    new PerformanceObserver(list=>{
      for(const entry of list.getEntries()){
        const element=entry.element,style=element?getComputedStyle(element):null;
        emit({kind:'lcp',time:entry.startTime,size:entry.size,tag:element?.tagName||null,selector:element?.id?'#'+element.id:(typeof element?.className==='string'?'.'+element.className.trim().replace(/\s+/g,'.'):null),font:style?{family:style.fontFamily,size:style.fontSize,weight:style.fontWeight}:null});
      }
    }).observe({type:'largest-contentful-paint',buffered:true});
  });
}
function samplePlan(){
  const plan=[];
  for(let round=0;round<9;round++){
    const routeOrder=round%2===0?[ROUTES[0],ROUTES[1]]:[ROUTES[1],ROUTES[0]];
    for(const route of routeOrder){
      const arms=[...PRIMARY_ORDERS[round]];
      if(route===ROUTES[0]){
        const a=arms.indexOf('A');
        arms.splice(a+(round%2===0?1:0),0,'A-repeat');
      }
      for(let position=0;position<arms.length;position++)plan.push({round,route,arm:arms[position],order:arms.join('>'),order_position:position+1});
    }
  }
  return plan;
}
async function sampleOne(lighthouse,step,sequence,total,report){
  active={route:step.route,arm:step.arm==='A-repeat'?'A':step.arm};
  const sample={sample_index:sequence,route:step.route,round:step.round,arm:step.arm,order:step.order,order_position:step.order_position,started_at:new Date().toISOString(),fresh_browser_process:true,status:'STARTED'};
  report.samples.push(sample);
  writeJson(OUTPUT,report);
  let browser,cdp;
  const events=[],requestFailures=[];
  try{
    browser=await chromium.launch({executablePath:await packed.executablePath(),args:chromeArgs(),headless:true});
    const browserVersion=browser.version();
    if(!browserVersion.startsWith('143.'))throw new Error(`Expected pinned Chromium 143, received ${browserVersion}`);
    cdp=await chromium.connectOverCDP('http://127.0.0.1:9222');
    const context=cdp.contexts()[0];
    await context.route('**/*',route=>routeResources(route,active.arm));
    observePage(context,events,requestFailures);
    const {lhr}=await lighthouse(BASE+step.route,{port:9222,output:'json',logLevel:'error',onlyCategories:['performance'],disableFullPageScreenshot:true,maxWaitForLoad:20000,disableStorageReset:false});
    if(lhr.runtimeError)throw new Error(JSON.stringify(lhr.runtimeError));
    const audits=lhr.audits;
    const network=audits['network-requests']?.details?.items||[];
    const sanitize=url=>url?.startsWith('data:')?'data:font;sha256='+sha(Buffer.from(url)):url;
    const networkRows=network.map(item=>({
      url:sanitize(item.url),resourceType:item.resourceType||null,statusCode:item.statusCode??null,
      transferSize:item.transferSize??null,resourceSize:item.resourceSize??null,
      startTime:item.startTime??null,endTime:item.endTime??null,
      isSecure:item.isSecure??null,protocol:item.protocol||null,
    }));
    const blocking=(audits['render-blocking-resources']?.details?.items||[]).map(item=>sanitize(item.url)).filter(Boolean);
    const lcpElement=audits['largest-contentful-paint-element']?.details?.items?.[0]?.node;
    const lcpSnippet=lcpElement?.snippet||'';
    Object.assign(sample,{
      status:'PASS',completed_at:new Date().toISOString(),browser_version:browserVersion,
      lcp_ms:audits['largest-contentful-paint']?.numericValue??null,
      cls:audits['cumulative-layout-shift']?.numericValue??null,
      tbt_ms:audits['total-blocking-time']?.numericValue??null,
      transfer_bytes:audits['total-byte-weight']?.numericValue??null,
      requests:networkRows.length,
      render_blocking:blocking,
      network:networkRows,
      font_network:networkRows.filter(item=>item.resourceType==='Font'||/\.(?:woff2?|ttf|otf)(?:[?#]|$)/i.test(item.url||'')),
      still_requests:networkRows.filter(item=>/hero-still-(?:640|720|1440)\.webp(?:[?#]|$)/i.test(item.url||'')),
      lcp_element:{selector:lcpElement?.selector||null,text_sha256:sha(Buffer.from(lcpSnippet)),snippet_chars:lcpSnippet.length},
      passive_events:events,
      request_failures:requestFailures,
      warnings:lhr.runWarnings||[],
      lighthouse_settings:{form_factor:lhr.configSettings?.formFactor||null,throttling_method:lhr.configSettings?.throttlingMethod||null,throttling:lhr.configSettings?.throttling||null},
      metric_source:'Lighthouse mobile simulated run. Values are raw per-sample audit results; no summary or budget pass/fail is computed here.',
    });
    console.log(`RAW_SAMPLE ${String(sequence).padStart(2,'0')}/${total} PASS round=${step.round+1} route=${step.route} arm=${step.arm}`);
  }catch(error){
    sample.status='FAILED';
    sample.completed_at=new Date().toISOString();
    sample.error=String(error?.stack||error);
    sample.passive_events=events;
    sample.request_failures=requestFailures;
    report.status='INCOMPLETE';
    report.session={status:'STOPPED_ON_FIRST_FAILURE',planned_samples:total,completed_samples:report.samples.length};
    report.failure='No retry or resume was attempted.';
    writeJson(OUTPUT,report);
    throw error;
  }finally{
    if(cdp)await cdp.close().catch(()=>{});
    if(browser)await browser.close().catch(()=>{});
  }
  writeJson(OUTPUT,report);
}
async function smokeFixtures(){
  await ensureChromiumRuntime();
  const rows=[];
  await startFixtureServer();
  try{
    for(const route of ROUTES)for(const arm of ARMS){
      active={route,arm};
      let browser,cdp;
      try{
        browser=await chromium.launch({executablePath:await packed.executablePath(),args:chromeArgs(),headless:true});
        const version=browser.version();
        if(!version.startsWith('143.'))throw new Error(`Expected pinned Chromium 143, received ${version}`);
        cdp=await chromium.connectOverCDP('http://127.0.0.1:9222');
        const context=cdp.contexts()[0];
        await context.route('**/*',request=>routeResources(request,arm));
        const page=context.pages()[0]||await context.newPage();
        await page.setViewportSize({width:360,height:800});
        const response=await page.goto(BASE+route,{waitUntil:'load',timeout:60000});
        if(response?.status()!==200)throw new Error(`Fixture response status ${response?.status()} for ${arm} ${route}`);
        await page.evaluate(()=>document.fonts?.ready||Promise.resolve());
        if(arm==='B-still')await page.waitForFunction(()=>document.querySelector('.p32-hero-still')?.classList.contains('is-loaded'),null,{timeout:10000});
        const state=await page.evaluate(()=>({h1Count:document.querySelectorAll('h1').length,heroCanvases:document.querySelectorAll('canvas.p32-hero-still').length,stillLoaded:!!document.querySelector('canvas.p32-hero-still.is-loaded'),fontPending:document.documentElement.classList.contains('p25-font-pending')}));
        if(state.h1Count!==1)throw new Error(`Expected one H1 for ${arm} ${route}`);
        if(arm==='B-still'&&(state.heroCanvases!==1||!state.stillLoaded))throw new Error(`Still did not load for ${arm} ${route}`);
        if(arm!=='B-still'&&state.heroCanvases!==0)throw new Error(`Unexpected hero still canvas for ${arm} ${route}`);
        rows.push({route,arm,status:'PASS',browser_version:version,...state});
        console.log(`FIXTURE_SMOKE PASS route=${route} arm=${arm}`);
      }finally{
        if(cdp)await cdp.close().catch(()=>{});
        if(browser)await browser.close().catch(()=>{});
      }
    }
  }finally{
    await closeFixtureServer();
  }
  const out=path.join(EVIDENCE,'smoke.json');
  writeJson(out,{fixture_manifest_sha256:sha(fs.readFileSync(MANIFEST_PATH)),status:'PASS',cases:rows});
  console.log(`FIXTURE_SMOKE_COMPLETE ${rows.length} fresh-browser route/arm checks`);
}
async function main(){
  if(!process.env.NODE_PATH)throw new Error('Set NODE_PATH to the pinned runtime node_modules for the local resource mirrors');
  const fixtureBytes=fs.readFileSync(FIXTURE_PATH);
  const manifest=JSON.parse(fs.readFileSync(MANIFEST_PATH,'utf8'));
  if(sha(fixtureBytes)!==manifest.fixture_json_sha256)throw new Error('Fixture JSON hash does not match the committed fixture manifest');
  const {execFileSync}=require('node:child_process');
  const runtimeDiff=execFileSync('git',['diff','--name-only',manifest.source_commits.B_current,'HEAD','--','*.php','*.css','*.js','*.txt','assets/**','data/**','destinations/**','places/**','blog/**','includes/**'],{cwd:ROOT,encoding:'utf8'}).trim();
  if(runtimeDiff)throw new Error(`Current site runtime differs from frozen B source ${manifest.source_commits.B_current}: ${runtimeDiff}`);
  const chromiumPackageVersion=JSON.parse(fs.readFileSync(path.join(RUNTIME,'@sparticuz/chromium/package.json'),'utf8')).version;
  if(require('playwright/package.json').version!=='1.58.2'||chromiumPackageVersion!=='143.0.4'||require('lighthouse/package.json').version!=='12.8.2')throw new Error('Pinned Playwright, Chromium or Lighthouse package version mismatch');
  fixtures=JSON.parse(fixtureBytes);
  if(Object.keys(fixtures).length!==ROUTES.length||ROUTES.some(route=>!fixtures[route]))throw new Error('Fixture route inventory mismatch');
  for(const route of ROUTES)for(const arm of ARMS)if(typeof fixtures[route][arm]!=='string')throw new Error(`Missing ${arm} fixture for ${route}`);
  if(fs.existsSync(OUTPUT))throw new Error(`Refusing to overwrite raw sample output ${OUTPUT}`);
  if(process.argv.includes('--smoke-only')){
    await smokeFixtures();
    return;
  }
  if(process.argv.includes('--preflight-only')){
    await ensureChromiumRuntime();
    let browser,cdp;
    try{
      browser=await chromium.launch({executablePath:await packed.executablePath(),args:chromeArgs(),headless:true});
      const version=browser.version();
      if(!version.startsWith('143.'))throw new Error(`Expected pinned Chromium 143, received ${version}`);
      cdp=await chromium.connectOverCDP('http://127.0.0.1:9222');
      console.log(`PASS Task 3 browser launch/CDP preflight: Chromium ${version}; no page navigation and no performance sample`);
    }finally{
      if(cdp)await cdp.close().catch(()=>{});
      if(browser)await browser.close().catch(()=>{});
    }
    return;
  }
  await ensureChromiumRuntime();
  const plan=samplePlan();
  if(plan.length!==63)throw new Error(`Expected 63 planned fresh-browser samples, got ${plan.length}`);
  const report={
    phase:'32c',task:'3_hero_still_three_arm_ab',status:'RUNNING',started_at:new Date().toISOString(),
    environment:{local_only:true,base_url:BASE,browser:'Chromium 143 via @sparticuz/chromium 143.0.4',playwright:require('playwright/package.json').version,lighthouse:require('lighthouse/package.json').version,node:process.version,fixture_sha256:sha(fixtureBytes),A_source_commit:manifest.source_commits.A,B_source_commit:manifest.source_commits.B_current,php_wasm:manifest.rendering.runtime},
    method:{samples_per_primary_arm_per_route:9,primary_arms:ARMS,fresh_chromium_process_per_sample:true,total_expected_samples:63,route_order:'Alternate Mysuru/article first position on odd/even rounds.',primary_arm_order:'Use a predetermined balanced schedule of all six three-arm permutations, then repeat three rotations so each primary arm occupies each sample position three times.',A_A_repeat:'Nine additional A-repeat samples on Mysuru. Each is adjacent to that round\'s primary A sample; the A-repeat is placed before/after A on alternating rounds.',serial:true,parallel_samples:0,retries:0,resume:false,performance_model:'Lighthouse mobile simulated run; effective Lighthouse throttling settings are retained per sample.',resource_delivery:'Local PHP-WASM-rendered HTML and selected-arm local assets, plus pinned npm mirrors for fonts and scene scripts. Unsupported external requests are blocked. No production host or live network is measured.',full_page_report_screenshot:false,metrics_retained:['LCP','CLS','TBT','total-byte-weight transfer bytes','request count','render-blocking URL list','network request transfer records','font network records','hero still requests','LCP/font/paint-gate events','warnings and failed requests'],fixed_budgets:ORDER,interpretation:'Simulated local evidence only. Not PageSpeed Insights, field data, production/CDN timing, deployment proof or a live-speed claim.'},
    fixture_manifest_sha256:sha(fs.readFileSync(MANIFEST_PATH)),planned_order:plan,samples:[],session:{status:'RUNNING',planned_samples:plan.length},
  };
  writeJson(OUTPUT,report);
  await startFixtureServer();
  const {default:lighthouse}=await import(pathToFileURL(require.resolve('lighthouse/core/index.js')));
  try{
    for(let index=0;index<plan.length;index++)await sampleOne(lighthouse,plan[index],index+1,plan.length,report);
    const counts={};
    for(const route of ROUTES){
      counts[route]={A:0,'B-still':0,'B-plain':0,'A-repeat':0};
      for(const sample of report.samples)if(sample.route===route)counts[route][sample.arm]++;
    }
    if(counts[ROUTES[0]].A!==9||counts[ROUTES[0]]['A-repeat']!==9||counts[ROUTES[0]]['B-still']!==9||counts[ROUTES[0]]['B-plain']!==9||counts[ROUTES[1]].A!==9||counts[ROUTES[1]]['A-repeat']!==0||counts[ROUTES[1]]['B-still']!==9||counts[ROUTES[1]]['B-plain']!==9)throw new Error(`Final sample-count validation failed: ${JSON.stringify(counts)}`);
    if(report.samples.some(sample=>sample.status!=='PASS'))throw new Error('At least one planned sample did not pass');
    report.status='COMPLETE';
    report.completed_at=new Date().toISOString();
    report.session={status:'COMPLETE',planned_samples:plan.length,completed_samples:report.samples.length,sample_counts:counts};
    report.analysis_status='NOT_STARTED';
    writeJson(OUTPUT,report);
    console.log(`RAW_COMPLETE ${report.samples.length} samples. Summary statistics and budget decisions were not computed.`);
  }finally{
    await closeFixtureServer();
  }
}
main().then(()=>process.exit(0)).catch(error=>{console.error(error.stack||error);process.exit(1);});
