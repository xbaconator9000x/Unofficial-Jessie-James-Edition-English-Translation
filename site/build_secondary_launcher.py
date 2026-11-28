#!/usr/bin/env python3
"""Preserve the previous enabled launcher URL alongside the public launcher.

Both pages expose the same editions. Keep the previous launcher-patches URLs
working for visitors with older bookmarks. Only verified BPS files are copied.
"""
from pathlib import Path
from shutil import copyfile
import hashlib
import json
import struct
import zlib

SITE = Path(__file__).resolve().parent
main = (SITE / "index.html").read_text(encoding="utf-8")
assert 'data-downloads-suspended="false"' in main, "Public website must be enabled"
assert '<a href="launcher.html">@xbaconator9000x</a>' in main, "Keep the old launcher link"
assert main.count('<body data-downloads-suspended="false">') == 1
secondary = main.replace(
    '<body data-downloads-suspended="false">',
    '<body data-downloads-suspended="false" data-patch-base="launcher-patches/">',
    1,
)

assert 'data-downloads-suspended="true"' not in secondary
assert 'class="suspension-notice"' not in secondary
assert 'data-patch-base="launcher-patches/"' in secondary
assert secondary.count('class="patcher-controls"') == 3
assert all(f'id="{prefix}patch-run"' in secondary for prefix in ('', 'es-', 'official-'))
assert '<a href="launcher.html">@xbaconator9000x</a>' in secondary

# The same HTML, CSS and JavaScript are used for both launchers.
# Only the patch base path differs.
(SITE / "launcher.html").write_text(secondary, encoding="utf-8")

mirror = SITE / "launcher-patches"
mirror.mkdir(exist_ok=True)
required = set()
for manifest_name in ("releases.json", "spanish-releases.json", "official-releases.json"):
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

print(f"PASS: linked secondary launcher with {len(required)} SHA-verified BPS patches; both public and legacy launchers enabled")
