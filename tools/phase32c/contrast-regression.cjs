#!/usr/bin/env node
// Screenshot-based no-scene regression gate for the four Phase32c contrast nodes.
const fs=require('node:fs');
const path=require('node:path');
const {spawnSync}=require('node:child_process');
const {execFileSync}=require('node:child_process');
const ROOT=path.resolve(__dirname,'../..');
const REPRO=path.join(__dirname,'contrast-repro.cjs');
const BASE=process.env.PHASE32C_BASE_URL||'http://127.0.0.1:8094';
const SOURCE=`contrast-regression-${process.env.PHASE32C_REGRESSION_SHA||execFileSync('git',['rev-parse','--short','HEAD'],{cwd:ROOT,encoding:'utf8'}).trim()}`;
const OUT=path.join(ROOT,'reports',`phase-32c-${SOURCE}.json`);
const SHOTS=path.join(ROOT,'reports','screenshots','phase-32c',SOURCE);
const STATE='touch-coarse-scene-not-started';
const WIDTHS=[360,1280];
const ROUTES=['/','/about'];
const REQUIRED_IDS=new Set(['home-em','about-faq-h2','about-team-label','about-kodagu-label']);
const MIN_CONTRAST=4.5;
function runWidth(width,resume){
  const env={...process.env,PHASE32C_BASE_URL:BASE,PHASE32C_SOURCE:SOURCE,PHASE32C_OUT:OUT,PHASE32C_SHOTS:SHOTS,PHASE32C_ONLY_WIDTH:String(width),PHASE32C_ONLY_STATE:STATE};
  delete env.PHASE32C_ONLY_ROUTE;delete env.PHASE32C_LIMIT;
  if(resume)env.PHASE32C_RESUME='1';else delete env.PHASE32C_RESUME;
  const run=spawnSync(process.execPath,[REPRO],{cwd:ROOT,env,stdio:'inherit'});
  if(run.error)throw run.error;
  if(run.status!==0)throw new Error(`Contrast capture failed at ${width}px with exit ${run.status}`);
}
function main(){
  for(let i=0;i<WIDTHS.length;i++)runWidth(WIDTHS[i],i>0);
  const report=JSON.parse(fs.readFileSync(OUT,'utf8'));
  const expected=new Set(ROUTES.flatMap(route=>WIDTHS.map(width=>`${route}|${width}|${STATE}`)));
  const actual=new Set(report.cases.map(c=>`${c.route}|${c.width}|${c.state}`));
  const findings=report.cases.flatMap(c=>c.elements.map(e=>({route:c.route,width:c.width,state:c.state,sceneCalls:c.pageState.sceneCalls,webglContextCalls:c.pageState.webglContextCalls,enabled:c.device.javascriptEnabled,id:e.id,ratio:e.minimumSampledContrast,screenshot:e.screenshot})));
  const failures=[];
  if(report.caseCount!==4||actual.size!==expected.size)failures.push(`Expected four unique route/width cases, found ${report.caseCount}/${actual.size}`);
  for(const key of expected)if(!actual.has(key))failures.push(`Missing case ${key}`);
  if(findings.length!==8)failures.push(`Expected eight finding crops, found ${findings.length}`);
  for(const f of findings){
    if(!REQUIRED_IDS.has(f.id))failures.push(`Unexpected finding ${f.id}`);
    if(!Number.isFinite(f.ratio)||f.ratio<MIN_CONTRAST)failures.push(`${f.id} ${f.route} ${f.width}px is ${f.ratio}:1, below ${MIN_CONTRAST}:1`);
    if(f.sceneCalls!==0||f.webglContextCalls!==0)failures.push(`${f.route} ${f.width}px started a scene (calls ${f.sceneCalls}/${f.webglContextCalls})`);
    if(f.enabled!==true)failures.push(`${f.route} ${f.width}px did not run with JavaScript enabled`);
    if(!fs.existsSync(path.resolve(ROOT,f.screenshot)))failures.push(`Missing screenshot ${f.screenshot}`);
  }
  for(const route of ROUTES)for(const width of WIDTHS){
    const ids=new Set(findings.filter(f=>f.route===route&&f.width===width).map(f=>f.id));
    const expectedIds=route==='/'?['home-em']:['about-faq-h2','about-team-label','about-kodagu-label'];
    for(const id of expectedIds)if(!ids.has(id))failures.push(`Missing ${id} on ${route} at ${width}px`);
  }
  if(failures.length)throw new Error(failures.join('\n'));
  const min=Math.min(...findings.map(f=>f.ratio));
  console.log(`PASS: ${report.caseCount} fresh-browser cases, ${findings.length} screenshot crops, minimum contrast ${min.toFixed(3)}:1, no scene started.`);
  console.log(`REPORT ${path.relative(ROOT,OUT)}`);
}
main();
