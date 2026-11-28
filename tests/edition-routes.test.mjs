import assert from "node:assert/strict";
import {readFileSync} from "node:fs";
import {findRoute} from "../site/bps.mjs";
const root = new URL("../site/",import.meta.url);
const read = name => readFileSync(new URL(name,root),"utf8");
const en = JSON.parse(read("patches/releases.json"));
const es = JSON.parse(read("patches/spanish-releases.json"));
const official = JSON.parse(read("patches/official-releases.json"));
const original="16777216:805E24CA";
const officialBase="16777216:9ED6BE84";
assert.deepEqual(Object.keys(en.versions).filter(x=>x in es.versions),[original]);
for(const m of [en,es,official]) {
 for(const key of Object.keys(m.versions)) assert.notEqual(findRoute(m.patches,key,m.target),null,key);
 assert.equal(findRoute(m.patches,m===official?officialBase:original,m.target).length,1);
 assert.deepEqual(findRoute(m.patches,m.target,m.target),[]);
}
for(const key of Object.keys(en.versions).filter(x=>x!==original)) assert.equal(findRoute(es.patches,key,es.target),null);
for(const key of Object.keys(es.versions).filter(x=>x!==original)) assert.equal(findRoute(en.patches,key,en.target),null);
assert.equal(en.latest,"1.04");
assert.equal(es.latest,"1.04");
assert.equal(official.latest,"1.04");
assert.equal(official.target,"16777216:EF0BB0A2");
for(const key of Object.keys(official.versions)) {
  assert.equal(findRoute(en.patches,key,en.target),null);
  assert.equal(findRoute(es.patches,key,es.target),null);
}
for(const key of [...Object.keys(en.versions),...Object.keys(es.versions)]) assert.equal(findRoute(official.patches,key,official.target),null);
assert.equal(findRoute(en.patches,"16777216:6E1E5095",en.target)?.length,1);
assert.equal(findRoute(en.patches,"16777216:519E0696",en.target)?.length,2);
assert.equal(findRoute(en.patches,original,en.target)?.length,1);
assert.equal(en.target,"16777216:43CAA1F3");
assert.ok(findRoute(en.patches,"16777216:CADC8480",en.target)?.length>0);
assert.ok(findRoute(en.patches,"16777216:D2866130",en.target).length>0);
assert.equal(es.target,"16777216:1C4A1771");
assert.ok(findRoute(es.patches,"16777216:0486144D",es.target)?.length>0);
assert.equal(findRoute(es.patches,"16777216:58F089B9",es.target).length,1);
assert.ok(findRoute(en.patches,"16777216:A3E3CC2F",en.target)?.length>0);
assert.ok(findRoute(es.patches,"16777216:7C042814",es.target)?.length>0);
const publicV10="16777216:C043455C";
assert.equal(en.versions[publicV10],"English v1.0");
const upgrade=findRoute(en.patches,publicV10,en.target);
assert.ok(upgrade?.length>0,"Released English v1.0 must upgrade to v1.04");
assert.equal(upgrade[0].from,publicV10);
assert.equal(upgrade[upgrade.length-1].to,en.target);
assert.equal(findRoute(es.patches,publicV10,es.target),null);
const html=read("index.html"), nav=html.match(/<nav class="main-menu"[\s\S]*?<\/nav>/)[0];
assert.deepEqual([...nav.matchAll(/href="#([^"]+)"/g)].map(x=>x[1]),[...html.matchAll(/<section class="window" id="([^"]+)"/g)].map(x=>x[1]));
for(const id of ["rom-file","patch-file","patch-run","patch-download","patch-status","patch-log","copy-report","rom-info","latest-version","hosted-patch-status"]) { for(const prefix of ['','es-','official-']) assert.equal([...html.matchAll(new RegExp('id="'+prefix+id+'"','g'))].length,1); }
assert.equal(read("spanish-patcher.mjs").includes('patches/spanish-releases.json'),true);
const gallery=html.match(/<section class="window" id="english-screenshots">[\s\S]*?<\/section>/)[0];
assert.deepEqual([...gallery.matchAll(/<img src="([^"]+)"/g)].map(x=>x[1]),["english-featured-gameplay.gif","english-dialogue.gif","english-train-dialogue.gif","english-rocket-base.gif","english-team-rocket-motto.gif","english-battle-mode.gif","english-hard-mode.gif","english-exp-all.png","english-save-mode.png","english-battle-qol.gif","english-battle-qol-2.gif","pokerail-english-map.jpg"]);
assert.equal([...nav.matchAll(/href="#([^"]+)"/g)].length,10);
console.log("Three independent edition routes, navigation order and separate controls passed");
