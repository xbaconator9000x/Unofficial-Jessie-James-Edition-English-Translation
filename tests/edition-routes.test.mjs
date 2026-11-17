import assert from "node:assert/strict";
import {readFileSync} from "node:fs";
import {findRoute} from "../site/bps.mjs";
const root = new URL("../site/",import.meta.url);
const read = name => readFileSync(new URL(name,root),"utf8");
const en = JSON.parse(read("patches/releases.json"));
const es = JSON.parse(read("patches/spanish-releases.json"));
const original="16777216:805E24CA";
assert.deepEqual(Object.keys(en.versions).filter(x=>x in es.versions),[original]);
for(const m of [en,es]) {
 for(const key of Object.keys(m.versions)) assert.notEqual(findRoute(m.patches,key,m.target),null,key);
 assert.equal(findRoute(m.patches,original,m.target).length,1);
 assert.deepEqual(findRoute(m.patches,m.target,m.target),[]);
}
for(const key of Object.keys(en.versions).filter(x=>x!==original)) assert.equal(findRoute(es.patches,key,es.target),null);
assert.equal(findRoute(en.patches,es.target,en.target),null);
const html=read("index.html"), nav=html.match(/<nav class="main-menu"[\s\S]*?<\/nav>/)[0];
assert.deepEqual([...nav.matchAll(/href="#([^"]+)"/g)].map(x=>x[1]),[...html.matchAll(/<section class="window" id="([^"]+)"/g)].map(x=>x[1]));
for(const id of ["rom-file","patch-file","patch-run","patch-download","patch-status","patch-log","copy-report","rom-info","latest-version","hosted-patch-status"]) assert.equal([...html.matchAll(new RegExp('id="es-'+id+'"','g'))].length,1);
assert.equal(read("spanish-patcher.mjs").includes('patches/spanish-releases.json'),true);
console.log("Independent edition routes, navigation order and separate Spanish controls passed");
