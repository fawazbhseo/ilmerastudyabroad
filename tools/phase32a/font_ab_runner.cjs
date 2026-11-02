#!/usr/bin/env node
// Fresh two-route font candidate A/B. Stores raw samples only, with no retries or analysis.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const {pathToFileURL}=require('node:url');
const {chromium}=require('playwright'),packed=require('@sparticuz/chromium');
const {resources}=require('../phase25/resources.cjs');
const ROOT=path.resolve(__dirname,'../..');
const RUNTIME=process.env.PHASE32_RUNTIME||'/home/user/phase32a-runtime/node_modules';
const {inflate}=require(path.join(RUNTIME,'@sparticuz/chromium/build/cjs/lambdafs.cjs'));
const EVIDENCE=path.resolve(process.env.PHASE32A_FONT_EVIDENCE||'/home/user/phase32a-runtime/phase32a-font-ab-run01');
const FIXTURE_PATH=path.join(EVIDENCE,'fixtures.json'),SELECTED_PATH=path.join(EVIDENCE,'selected.json');
const PORT=Number(process.env.PHASE32A_FONT_PORT||8093),BASE=`http://127.0.0.1:${PORT}`;
const OUTPUT=path.resolve(process.env.PHASE32A_FONT_OUTPUT||path.join(ROOT,'reports/phase-32a-font-ab-run-01-raw.json'));
const ROUTES=['/study-abroad-counselling-mysuru','/blog/how-to-choose-study-abroad-consultant-karnataka'];
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const writeJson=(file,value)=>fs.writeFileSync(file,JSON.stringify(value,null,2)+'\n');
function select(route,variant){const tmp=SELECTED_PATH+'.tmp';writeJson(tmp,{route,variant});fs.renameSync(tmp,SELECTED_PATH);}
function chromeArgs(){return[...packed.args.filter(a=>!['--single-process','--in-process-gpu'].includes(a)),'--remote-debugging-port=9222'];}
async function ensureRuntime(){const root=await inflate(path.join(RUNTIME,'@sparticuz/chromium/bin/al2023.tar.br'));process.env.LD_LIBRARY_PATH=path.join(root,'lib')+':'+(process.env.LD_LIBRARY_PATH||'');}
async function checkFixtureServer(fixtures,manifest){
 for(const route of ROUTES)for(const arm of ['A','B']){select(route,arm);const response=await fetch(BASE+route);const body=Buffer.from(await response.arrayBuffer());if(response.status!==200||body.toString('utf8')!==fixtures[route][arm])throw Error(`Font fixture server mismatch for ${route} ${arm}: HTTP ${response.status}, sha=${sha(body)}`);}
 if(manifest.fixture_json_sha256!==sha(fs.readFileSync(FIXTURE_PATH)))throw Error('Font fixture changed after freeze');
}
async function main(){
 await ensureRuntime();
 if(!fs.existsSync(FIXTURE_PATH)||!fs.existsSync(SELECTED_PATH))throw Error('Frozen two-route font fixture and selected.json are required');
 const fixtureBytes=fs.readFileSync(FIXTURE_PATH),fixtures=JSON.parse(fixtureBytes),manifest=JSON.parse(fs.readFileSync(path.join(ROOT,'reports/phase-32a-font-ab-run-01-fixtures.json'),'utf8'));
 if(sha(fixtureBytes)!==manifest.fixture_json_sha256)throw Error('Font fixture hash does not match the committed manifest');
 if(JSON.stringify(Object.keys(fixtures))!==JSON.stringify(ROUTES))throw Error('Font fixture routes/order differ from the frozen protocol');
 if(manifest.content_invariant_failures!==0||manifest.route_count!==2)throw Error('Font fixture content invariant guard failed');
 await checkFixtureServer(fixtures,manifest);
 if(process.argv.includes('--preflight-only')){let browser,cdp;try{browser=await chromium.launch({executablePath:await packed.executablePath(),args:chromeArgs(),headless:true});const version=browser.version();if(!version.startsWith('143.'))throw Error(`Expected Chromium 143, got ${version}`);cdp=await chromium.connectOverCDP('http://127.0.0.1:9222');console.log(`PASS font fixture/Chromium preflight: ${version}, all four A/B bodies match, zero Lighthouse samples`);}finally{if(cdp)await cdp.close().catch(()=>{});if(browser)await browser.close().catch(()=>{});}return;}
 if(fs.existsSync(OUTPUT))throw Error(`Refusing to overwrite prior raw font evidence ${OUTPUT}`);
 const {default:lighthouse}=await import(pathToFileURL(require.resolve('lighthouse/core/index.js')));
 const report={phase:'32a',task:'fresh_font_candidate_ab',status:'RUNNING',started_at:new Date().toISOString(),environment:{local_only:true,fixture_sha256:sha(fixtureBytes),A_source_commit:manifest.A_source_commit,B_candidate:'font-display:swap with body visibility gate removed',browser:'Chromium 143 via @sparticuz/chromium',playwright:require('playwright/package.json').version,lighthouse:require('lighthouse/package.json').version,base_url:BASE},protocol:{route_order:ROUTES,samples_per_arm_per_route:7,total_expected_samples:28,fresh_chromium_process_per_sample:true,serial:true,parallel_samples:0,round_order:'For each route: A/B on even rounds, B/A on odd rounds, seven rounds per arm; no retry, resume or skipped samples',lighthouse_model:'Default mobile simulated Slow4G and 4x CPU',candidate_scope:'Only seven local font-face display values changed from block to swap, plus removal of the p25-font-pending body visibility rule. Families, file URLs, font weights, preloads, markup, page copy and assets otherwise match.',font_decision_rule:'Candidate LCP must improve on both routes and CLS must be no worse on either route. No font source change unless both conditions pass.',metrics_retained:['absolute LCP ms','CLS','TBT ms','total transfer bytes','request count','font request URLs/bytes/status','render-blocking URLs','LCP element','warnings','observer events'],analysis:'Raw samples only. Do not calculate medians, IQRs, ratios or candidate outcome until the raw file is committed and pushed.'},samples:[],session:{status:'RUNNING',completed_samples:0,expected_samples:28,failed_sample:null}};
 writeJson(OUTPUT,report);let browserVersion='unknown';
 try{
  for(const route of ROUTES){for(let round=0;round<7;round++){
   const arms=round%2?['B','A']:['A','B'];
   for(const arm of arms){select(route,arm);const sample={route,round,arm,order:arms.join('/'),started_at:new Date().toISOString(),status:'STARTED'};report.samples.push(sample);writeJson(OUTPUT,report);let browser,cdp;
    try{
     browser=await chromium.launch({executablePath:await packed.executablePath(),args:chromeArgs(),headless:true});browserVersion=browser.version();if(!browserVersion.startsWith('143.'))throw Error(`Expected Chromium 143, got ${browserVersion}`);
     cdp=await chromium.connectOverCDP('http://127.0.0.1:9222');const context=cdp.contexts()[0];await context.route('**/*',resources);const events=[];await context.exposeBinding('__p32aFontEmit',(_,event)=>events.push(event));
     await context.addInitScript(()=>{const emit=event=>window.__p32aFontEmit(event).catch(()=>{});try{new PerformanceObserver(list=>{for(const e of list.getEntries())emit({kind:'lcp',time:e.startTime,size:e.size,tag:e.element?.tagName||null});}).observe({type:'largest-contentful-paint',buffered:true});}catch(_){}try{document.fonts?.addEventListener('loadingdone',()=>emit({kind:'fonts_ready',time:performance.now(),faces:[...document.fonts].map(f=>({family:f.family,weight:f.weight,style:f.style,status:f.status}))}));}catch(_){}});
     const {lhr}=await lighthouse(BASE+route,{port:9222,output:'json',logLevel:'error',onlyCategories:['performance'],disableFullPageScreenshot:true,maxWaitForLoad:15000,disableStorageReset:false});if(lhr.runtimeError)throw Error(JSON.stringify(lhr.runtimeError));
     const audits=lhr.audits,network=audits['network-requests']?.details?.items||[];Object.assign(sample,{status:'PASS',completed_at:new Date().toISOString(),lcp_ms:audits['largest-contentful-paint']?.numericValue,cls:audits['cumulative-layout-shift']?.numericValue,tbt_ms:audits['total-blocking-time']?.numericValue,transfer_bytes:audits['total-byte-weight']?.numericValue,requests:network.length,lcp_element:audits['largest-contentful-paint-element']?.details?.items?.[0]?.items?.[0]?.node?.snippet||null,font_network:network.filter(x=>x.resourceType==='Font').map(x=>({url:x.url,transferSize:x.transferSize,resourceSize:x.resourceSize,startTime:x.startTime,endTime:x.endTime,statusCode:x.statusCode})),render_blocking:(audits['render-blocking-resources']?.details?.items||[]).map(x=>x.url),warnings:lhr.runWarnings||[],observer_events:events});
     for(const key of ['lcp_ms','cls','tbt_ms','transfer_bytes','requests'])if(!Number.isFinite(sample[key]))throw Error(`Missing non-finite metric ${key}`);
     report.session.completed_samples++;console.log(`FONT SAMPLE ${report.session.completed_samples}/28 ${route} round${round} ${arm} status=PASS`);
    }catch(error){sample.status='FAIL';sample.completed_at=new Date().toISOString();sample.error=String(error.stack||error);report.status='INCOMPLETE';report.session.status='INCOMPLETE';report.session.failed_sample={route,round,arm,error:String(error.message||error)};writeJson(OUTPUT,report);throw error;}
    finally{if(cdp)await cdp.close().catch(()=>{});if(browser)await browser.close().catch(()=>{});}
    writeJson(OUTPUT,report);
   }
  }}
  report.status='COMPLETE';report.finished_at=new Date().toISOString();report.environment.chromium=browserVersion;report.session.status='COMPLETE';report.session.complete_samples=report.samples.length===28;writeJson(OUTPUT,report);console.log(`FONT RAW COMPLETE ${report.samples.length}/28 ${OUTPUT} SHA256=${sha(fs.readFileSync(OUTPUT))}`);
 }catch(error){console.error(error.stack||error);process.exitCode=1;}
}
main();
