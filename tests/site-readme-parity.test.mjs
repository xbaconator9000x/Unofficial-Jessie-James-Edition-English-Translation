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
  // The clean logo is supplied in the downloadable three-image ZIP, not displayed separately.
  if (!path.endsWith("logo-clean-snowmudk99.webp")) {
    assert.ok(readme.includes(path), "README must link approved media " + path);
    assert.ok(html.includes(path.replace(/^site\//,"")), "Website must link approved media " + path);
  }
}
assert.ok(html.includes('id="fanart"') && html.includes('href="#fanart"'));
assert.ok(readme.includes("u/SnowMudK99") && html.includes("u/SnowMudK99"));
const suspension = "Downloads have been disabled for the time being, as per MrNightology's request";
assert.ok(readme.includes(suspension) && html.includes(suspension), "Suspension notice must appear in README and website");
assert.ok(html.includes('data-downloads-suspended="true"'), "Download suspension must be enabled on the public website");
assert.ok(css.includes('body[data-downloads-suspended="true"] .patcher-controls { display: none; }'), "Suspended download controls must remain hidden");
for (const patcher of ["site/patcher.mjs", "site/spanish-patcher.mjs"]) {
  const script = content(patcher);
  assert.ok(script.includes("downloadsSuspended") && script.includes("dataset.downloadsSuspended"), patcher + " must block downloads");
}
const workflow = content(".github/workflows/pages.yml");
assert.ok(workflow.includes("Remove downloadable patches from public website artifact") && workflow.includes('site / "patches").rglob("*.bps")'), "Primary patch directory must exclude downloadable BPS files");
assert.ok(workflow.includes("Build verified secondary launcher"), "Deployment must build the linked secondary launcher");
assert.ok(html.includes('<a href="launcher.html">@xbaconator9000x</a>'), "The secondary launcher must be linked only from the footer credit");
assert.ok(content("site/build_secondary_launcher.py").includes('data-patch-base="launcher-patches/"'), "The enabled launcher must route its verified patches independently");

assert.ok(html.includes("og:image") && html.includes("media/jessie-james-cover-snowmudk99.jpg"));
assert.ok(css.includes(".fan-cover") && css.includes(".rocket-hero"));
assert.ok(!html.includes('class="rocket-r"'), "Old standalone masthead should be replaced");
// The user requested the existing README remain unchanged; check historical parity only.
const sharedVersion = "v1.03.2";
assert.ok(readme.includes("**English " + sharedVersion + "**"), "README latest version differs from English manifest");
assert.ok(readme.includes("5DAE93EA"), "README English CRC32 is out of date");
assert.ok(readme.includes("222A0072"), "README Spanish CRC32 is out of date");
for (const entry of english.changelog.filter(entry => entry.version !== "1.04")) {
  assert.ok(readme.includes("### English v" + entry.version + " -- " + entry.date), "README missing changelog version " + entry.version);
  for (const item of entry.changes) {
    assert.ok(readme.includes(item.replace(/^--\s*/,"")), "README missing release note: " + item);
  }
}
const spanishReadme = readme.split("## Prefer to play español?")[1]?.split("## What is Jessie & James Edition?")[0];
const spanishSite = html.split('<section class="window" id="spanish">')[1]?.split("</section>")[0];
assert.ok(spanishReadme && spanishSite, "Missing Spanish patch section");
for (const feature of ["Modo difícil opcional", "Modos de combate Clásico y Moderno", "EXP. ALL opcional", "Mentas de Naturaleza", "Chapas Plateadas y Doradas", "los seis objetos Power", "lectores de EV e IV", "mayor capacidad de la Mochila", "Cuerda Huida reutilizable", "precios de hasta cinco cifras"]) {
  assert.ok(spanishReadme.includes(feature), "README Spanish feature missing: " + feature);
  assert.ok(spanishSite.includes(feature), "Website Spanish feature missing: " + feature);
}

const readmeQol = readme.split("### Quality of life")[1]?.split("### Other additions")[0];
const siteQol = html.split("<h3>Quality of life</h3>")[1]?.split("<h3>Other additions</h3>")[0];
assert.ok(readmeQol && siteQol, "Missing consolidated QoL section");
const qolFeatures = [
  "Classic / Modern battles",
  "Optional Hard Mode",
  "EXP. ALL",
  "Nature colours",
  "Move details",
  "Effectiveness indicators",
  "Nature Mints and Bottle Caps",
  "EV training items",
  "EV and IV readers",
  "Expanded Bag storage",
  "Reusable Escape Rope",
  "Five-digit prices"
];
for (const feature of qolFeatures) {
  assert.ok(readmeQol.includes("**" + feature + "**"), "README missing QoL feature: " + feature);
  assert.ok(siteQol.includes("<strong>" + feature + "</strong>"), "Website missing QoL feature: " + feature);
}
for (const [label,section] of [["README",readmeQol],["website",siteQol]]) {
  for (const patchNote of [
    "Crash fix", "movement pointer", "EV/IV reader fix",
    "Fixed a glitch", "Major QOL additions in v1.02",
    "New in v1.03", "Item prices", "vitamin prices", "Title music"
  ]) {
    assert.ok(!section.includes(patchNote), label + " QoL section should not include patch notes or unrelated additions: " + patchNote);
  }
}
const readmeExtra = readme.split("### Other additions")[1]?.split("## Original Spanish Screenshots")[0];
const siteExtra = html.split("<h3>Other additions</h3>")[1]?.split("</section>")[0];
assert.ok(readmeExtra?.includes("Team Rocket motto theme") && siteExtra?.includes("Team Rocket motto theme"), "Title music should remain outside QoL");
assert.ok(readme.includes("### English v1.03 -- 22 November 2026") && readme.includes("Fixed EV/IV reader glitch") && readme.includes("Repaired movement pointer/dialogue overlap"), "Crash and EV/IV fixes must stay in release history");

import {execFileSync} from "node:child_process";
execFileSync("python3", ["site/media/build_art_pack.py"], {cwd:new URL("../",import.meta.url),stdio:"pipe"});
const zip = asset("site/media/jessie-james-fan-art-pack.zip");
assert.ok(zip.length > 1000 && zip.toString("ascii",0,2)==="PK");
const archiveCheck = `from zipfile import ZipFile
from pathlib import Path
p=Path("site/media")
z=ZipFile(p/"jessie-james-fan-art-pack.zip")
expected={"GBA-Box-Art.jpg":"jessie-james-cover-snowmudk99.jpg","Logo-with-Rocket-R.webp":"jessie-james-logo-snowmudk99.webp","Logo-without-Rocket-R.webp":"jessie-james-logo-clean-snowmudk99.webp"}
assert set(z.namelist())==set(expected)
for item, source in expected.items():
    assert z.read(item)==(p/source).read_bytes()
print("Verified 3-image artwork ZIP")
`;
execFileSync("python3", ["-c", archiveCheck], {cwd:new URL("../",import.meta.url),stdio:"pipe"});
const section = html.split('id="fanart"')[1]?.split('id="report"')[0];
assert.ok(section && section.includes('href="#art-credit"'));
assert.ok(!section.includes("SnowMudK99") && !section.includes("media notes"));
assert.ok(!html.includes('class="artist-credit"'));
assert.ok(html.includes('id="art-credit"') && html.includes("u/SnowMudK99"));
const footer = html.split('<footer class="footer" id="credits">')[1]?.split('</footer>')[0];
assert.ok(footer, "Missing website credits footer");
const artistPosition = footer.indexOf('id="art-credit"');
assert.ok(artistPosition > footer.indexOf('English localisation and patcher maintenance') && artistPosition < footer.indexOf('class="end-mark"'), "Artwork credit must appear with the other credits, above the end mark");
assert.ok(!html.includes('class="art-credit-footer"'), "No separate artist credit below the end mark");
const readmeCredits = readme.split('## Credits')[1];
assert.ok(readmeCredits.indexOf('Box art and logos -- **u/SnowMudK99**') > readmeCredits.indexOf('English localisation and patcher maintenance'), "Artist credit should sit alongside other README credits");
assert.ok(readmeCredits.indexOf('Box art and logos -- **u/SnowMudK99**') < readmeCredits.indexOf('Small Team Rocket R icons'), "README artist credit should precede source/media credits");
assert.ok(readme.includes('<a id="art-credit"></a>'));
for (const line of ["Download for use in emulators that use GBA cover art", "GBA box art (JPG)", "Logo with Rocket R (WEBP)", "Logo without Rocket R (WEBP)"]) {
    assert.ok(readme.includes(line) && html.includes(line), "Artwork summary mismatch: " + line);
}
const path = "media/jessie-james-fan-art-pack.zip";
assert.ok(html.includes('href="' + path + '"'));
assert.ok(readme.includes(path));
assert.ok(readme.includes("## Fan art and emulator box art"));
assert.ok(content("site/media/README.md").includes("SnowMudK99"));
assert.ok(content(".github/workflows/pages.yml").includes("README.md"), "Site deploy must run when README changes");
console.log("PASS: website/README release parity, media integrity and attribution");
