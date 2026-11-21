import assert from "node:assert/strict";
import {readFileSync, statSync} from "node:fs";
import {createHash} from "node:crypto";
const base = new URL("../", import.meta.url);
const content = path => readFileSync(new URL(path, base), "utf8");
const asset = path => readFileSync(new URL(path, base));
const html = content("site/index.html");
const readme = content("README.md");
const css = content("site/styles.css");
const english = JSON.parse(content("site/patches/releases.json"));
const spanish = JSON.parse(content("site/patches/spanish-releases.json"));
const files = [
  ["site/media/jessie-james-logo-snowmudk99.webp", "bf7f5a252b922498b3be6a5e82fe3f676660824a", "RIFF"],
  ["site/media/jessie-james-logo-clean-snowmudk99.webp", "3201579569a21bffdc6119b18d637a8a1854b89a", "RIFF"],
  ["site/media/jessie-james-cover-snowmudk99.jpg", "83b01ba6c54a1253815339bd890e0a6326bba8b1", "JPEG"]
];
for (const [path, expectedGitSha, type] of files) {
  const bytes = asset(path);
  assert.ok(bytes.length > 1000, path + " is missing or empty");
  const gitInput = Buffer.concat([Buffer.from("blob " + bytes.length + "\0"), bytes]);
  assert.equal(createHash("sha1").update(gitInput).digest("hex"), expectedGitSha, path + " does not match the approved upload");
  if (type === "RIFF") assert.equal(bytes.toString("ascii",0,4),"RIFF");
  if (type === "JPEG") assert.equal(bytes.subarray(0,3).toString("hex"),"ffd8ff");
  assert.ok(readme.includes(path), "README must link approved media " + path);
  assert.ok(html.includes(path.replace(/^site\//,"")), "Website must link approved media " + path);
}
assert.ok(html.includes('id="fanart"') && html.includes('href="#fanart"'));
assert.ok(readme.includes("SnowMudK99") && html.includes("SnowMudK99"));
assert.ok(html.includes("og:image") && html.includes("media/jessie-james-cover-snowmudk99.jpg"));
assert.ok(css.includes(".fan-cover") && css.includes(".rocket-hero"));
assert.ok(!html.includes('class="rocket-r"'), "Old standalone masthead should be replaced");
const sharedVersion = "v" + english.latest;
assert.ok(readme.includes("**English " + sharedVersion + "**"), "README latest version differs from English manifest");
assert.ok(readme.includes(english.target.split(":")[1]), "README English CRC32 is out of date");
assert.ok(readme.includes(spanish.target.split(":")[1]), "README Spanish CRC32 is out of date");
for (const entry of english.changelog) {
  assert.ok(readme.includes("### English v" + entry.version + " -- " + entry.date), "README missing changelog version " + entry.version);
  for (const item of entry.changes) {
    assert.ok(readme.includes(item.replace(/^--\s*/,"")), "README missing release note: " + item);
  }
}
const readmeQol = readme.split("### Quality of life")[1]?.split("## Original Spanish Screenshots")[0];
const siteQol = html.split('<h3>Quality of life</h3>')[1]?.split('</section>')[0];
assert.ok(readmeQol && siteQol, "Quality of life section missing in README or website");
for (const item of [
  "Major QOL additions in v1.02",
  "Nature mints",
  "Bottle caps and Golden bottle caps",
  "EV berries",
  "IV and EV readers",
  "Rocket HQ",
  "Five-digit prices",
  "reusable TM prices",
  "vitamin prices",
  "Oak's battle"
]) {
  assert.ok(readmeQol.includes(item), "README QOL section missing " + item);
  assert.ok(siteQol.includes(item), "Website QOL section missing " + item);
}
const latestQol = english.changelog.find(x=>x.version==="1.02")?.changes.filter(x=>x.startsWith("-- ")) ?? [];
for (const feature of latestQol) {
  const name = feature.slice(3).replace(/^Restored function to /,"").replace(/^Expanded price list to /,"");
  const key = name.startsWith("IV and EV readers") ? "IV and EV readers" :
    name.startsWith("Bottle caps") ? "Bottle caps and Golden bottle caps" :
    name.startsWith("five-digits") ? "Five-digit prices" : name;
  assert.ok(readmeQol.toLowerCase().includes(key.toLowerCase()), "README missing a released QOL feature: " + key);
  assert.ok(siteQol.toLowerCase().includes(key.toLowerCase()), "Website missing a released QOL feature: " + key);
}
assert.ok(readme.includes("## Fan art and emulator box art"));
assert.ok(content("site/media/README.md").includes("SnowMudK99"));
assert.ok(content(".github/workflows/pages.yml").includes("README.md"), "Site deploy must run when README changes");
console.log("PASS: website/README release parity, media integrity and attribution");
