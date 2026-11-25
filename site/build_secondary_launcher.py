#!/usr/bin/env python3
"""Build a linked, enabled launcher from the suspended public landing page.

The main page stays suspended. This alternative is linked only from the
existing @xbaconator9000x credit and uses a separate set of verified BPS assets.
No ROMs are included or copied. The README is untouched.
"""
from pathlib import Path
from shutil import copyfile
import hashlib
import json
import struct
import zlib

SITE = Path(__file__).resolve().parent
main = (SITE / "index.html").read_text(encoding="utf-8")
assert 'data-downloads-suspended="true"' in main, "Primary website must remain suspended"
assert '<a href="launcher.html">@xbaconator9000x</a>' in main, "The credit must be the only entrance"

def replace_once(content, before, after):
    if content.count(before) != 1:
        raise ValueError("Launcher template mismatch: " + before[:100])
    return content.replace(before, after)

secondary = main
updates = [
    ('<body data-downloads-suspended="true">',
     '<body data-downloads-suspended="false" data-patch-base="launcher-patches/">'),
    ("    <div class=\"suspension-notice\" role=\"status\"><strong>Downloads have been disabled for the time being, as per MrNightology's request</strong></div>\n", ""),
    ('<h2>English downloads suspended</h2>', '<h2>Patch your ROM</h2>'),
    ('<p class="small" id="hosted-patch-status" role="status">English patch downloads are temporarily disabled.</p>',
     '<p class="small" id="hosted-patch-status" role="status">Checking hosted patch availability…</p>'),
    ('<p>English patch downloads and in-browser patching are suspended for the time being. The release information remains available for reference.</p>',
     "<p>Choose the original Spanish FINAL v1.1 ROM or an earlier English release, including v1.03 and the Aqua ship hotfix. The patcher verifies your ROM and updates it to v1.03.2. A clean FireRed ROM won't work.</p>"),
    ('<p class="small" id="es-hosted-patch-status" role="status">Las descargas de parches están suspendidas temporalmente.</p>',
     '<p class="small" id="es-hosted-patch-status" role="status">Comprobando la disponibilidad del parche…</p>'),
    ('<p>Las descargas y la aplicación de parches en esta web están suspendidas temporalmente. La información sobre las mejoras sigue disponible.</p>',
     '<p>Selecciona la ROM original <em>Jessie &amp; James Edition FINAL v1.1</em> en español, la versión española QoL v1.0 o cualquier versión QoL v1.02. El parcheador actualizará a v1.03. No utilices FireRed sin modificar ni la versión inglesa.</p>'),
]
for old, new in updates:
    secondary = replace_once(secondary, old, new)

assert 'data-downloads-suspended="true"' not in secondary
assert 'class="suspension-notice"' not in secondary
assert 'data-patch-base="launcher-patches/"' in secondary
assert secondary.count('class="patcher-controls"') == 2
assert 'id="patch-run"' in secondary and 'id="es-patch-run"' in secondary
assert '<a href="launcher.html">@xbaconator9000x</a>' in secondary

# The same HTML, CSS and JavaScript are used for both launchers.
# Only status text and download state differ.
(SITE / "launcher.html").write_text(secondary, encoding="utf-8")

mirror = SITE / "launcher-patches"
mirror.mkdir(exist_ok=True)
required = set()
for manifest_name in ("releases.json", "spanish-releases.json"):
    manifest = json.loads((SITE / "patches" / manifest_name).read_text(encoding="utf-8"))
    for edge in manifest["patches"]:
        source = SITE / edge["path"]
        if source.parent != SITE / "patches" or source.suffix != ".bps":
            raise ValueError("Unexpected patch source: " + str(source))
        data = source.read_bytes()
        if len(data) != edge["bytes"] or data[:4] != b"BPS1":
            raise ValueError("Unexpected BPS file size or signature: " + str(source))
        if hashlib.sha256(data).hexdigest() != edge["sha256"]:
            raise ValueError("Unexpected patch checksum: " + str(source))
        sc, tc, pc = struct.unpack_from("<III", data, len(data) - 12)
        if f"{sc:08X}" != edge["from"].split(":")[1] or f"{tc:08X}" != edge["to"].split(":")[1]:
            raise ValueError("Unexpected BPS source or target CRC: " + str(source))
        if pc not in (0, zlib.crc32(data[:-4])):
            raise ValueError("Unexpected BPS integrity checksum: " + str(source))
        target = mirror / source.name
        copyfile(source, target)
        required.add(target.name)
for extra in mirror.iterdir():
    if extra.name not in required:
        raise ValueError("Unexpected secondary download file: " + str(extra))
assert len(required) >= 19
for module in ("patcher.mjs", "spanish-patcher.mjs"):
    script = (SITE / module).read_text(encoding="utf-8")
    assert "hostedPath" in script and "dataset.patchBase" in script
    assert "fetch(hostedPath(edge.path)" in script
    assert "fetch(hostedPath(full.path)" in script

print(f"PASS: linked secondary launcher with {len(required)} SHA-verified BPS patches; primary unchanged")
