#!/usr/bin/env node
// Representative WCAG A/AA scan using pinned axe; compares stable node identities to Task1 baseline.
const fs=require('node:fs'),path=require('node:path');const {launchBrowser,routePinnedResources}=require('./browser.cjs');
const ROOT=path.resolve(__dirname,'../..'),BASE=process.env.PHASE31_BASE_URL||'http://127.0.0.1:8080';
const routes=['/','/services','/about','/contact','/study-in-germany','/study-abroad-counselling-mysuru','/blog/how-to-choose-study-abroad-consultant-karnataka','/blog/'];
const out=process.argv[2]||'/home/user/phase31/accessibility.json';const baselinePath=process.argv[3]||path.join(ROOT,'reports/phase-31-accessibility-baseline.json');
const {execFileSync}=require('node:child_process');const axePath=require.resolve('axe-core/axe.min.js');
const key=v=>`${v.route}|${v.id}|${v.impact}|${v.target}`;
(async()=>{
 const b=await launchBrowser(),ctx=await b.newContext({viewport:{width:1280,height:900},javaScriptEnabled:true,reducedMotion:'reduce'}),cases=[];
 try{for(const route of routes){const p=await ctx.newPage();await routePinnedResources(p);const res=await p.goto(BASE+route,{waitUntil:'domcontentloaded',timeout:45000});if(!res||res.status()!==200)throw Error('HTTP '+route);await p.waitForTimeout(3000);await p.addScriptTag({path:axePath});const result=await p.evaluate(async()=>{const r=await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa']}});return{version:axe.version,violations:r.violations.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.map(n=>({target:n.target.join(' '),summary:n.failureSummary||'',html:n.html.slice(0,280)}))}))};});const violations=result.violations.flatMap(v=>v.nodes.map(n=>({route,id:v.id,impact:v.impact,target:n.target,summary:n.summary,html:n.html})));cases.push({route,width:1280,javascript:'on',motion:'reduced',axe:result.version,violation_count:violations.length,violations});await p.close();console.log(`AXE ${route} ${violations.length}`);}}finally{await b.close();}
 let delta=null,deltaFailures=[];
 if(fs.existsSync(baselinePath)){
  const baseline=JSON.parse(fs.readFileSync(baselinePath,'utf8'));const old=new Set(baseline.cases.flatMap(c=>c.violations.map(key))),now=new Set(cases.flatMap(c=>c.violations.map(key)));
  const added=[...now].filter(x=>!old.has(x)),removed=[...old].filter(x=>!now.has(x));
  delta={baseline:baselinePath,baseline_violation_nodes:old.size,current_violation_nodes:now.size,added,removed};
  if(added.length)deltaFailures=added;
 }
 const report={status:deltaFailures.length?'FAIL':'PASS_BASELINE_RELATIVE',axe_core:'4.11.0',run_only:['wcag2a','wcag2aa','wcag21a','wcag21aa'],representative_routes:routes,width:1280,javascript:true,reduced_motion:true,settle_ms:3000,cases,delta,delta_failures:deltaFailures,interpretation:'Existing immutable-reference findings remain recorded. PASS_BASELINE_RELATIVE means only that no new stable node/rule identities were added versus Task1; it does not mean zero violations or a full-site accessibility certification.'};
 fs.mkdirSync(path.dirname(path.resolve(out)),{recursive:true});fs.writeFileSync(out,JSON.stringify(report,null,2)+'\n');
 if(!fs.existsSync(baselinePath))fs.writeFileSync(baselinePath,JSON.stringify(report,null,2)+'\n');
 console.log(report.status,'nodes',cases.reduce((a,c)=>a+c.violation_count,0),'delta',deltaFailures.length);
 if(deltaFailures.length)process.exit(1);
})().catch(e=>{console.error(e.stack||e);process.exit(1)});
