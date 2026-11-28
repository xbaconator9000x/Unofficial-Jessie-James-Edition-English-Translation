#!/usr/bin/env python3
"""Verify published v1.04 patches without requiring users' ROM files."""
from pathlib import Path
import hashlib, json, struct, zlib
root = Path(__file__).resolve().parents[1]
expected = {
    "releases.json": ("16777216:805E24CA", "16777216:43CAA1F3", "05c12190dbe5b2d130e86ebbadeb5fc39b637002936cb069b41d1a7a901b060e"),
    "spanish-releases.json": ("16777216:805E24CA", "16777216:1C4A1771", "d4b43d74a74e9078ec67426ec407d13fa5811c8560e1357eaaf6ef2ba6b75f39"),
    "official-releases.json": ("16777216:9ED6BE84", "16777216:EF0BB0A2", "95de71ef91aafb4dc775aefe5662e886ad416480ca5b88f184ea23d5239985fd"),
}
files = set()
for name, (base, target, full_hash) in expected.items():
    m = json.loads((root / "site" / "patches" / name).read_text())
    assert m["latest"] == "1.04" and m["target"] == target
    current = [e for e in m["patches"] if e["version"] == "1.04"]
    full = next(e for e in current if e["from"] == base)
    assert full["sha256"] == full_hash
    reachable = {target}
    while True:
        after = reachable | {e["from"] for e in m["patches"] if e["to"] in reachable}
        if reachable == after: break
        reachable = after
    assert set(m["versions"]) <= reachable
    for e in current:
        assert e["to"] == target
        filename = Path(e["path"]).name
        files.add(filename)
        b = (root / "downloads" / filename).read_bytes()
        assert len(b) == e["bytes"] and b[:4] == b"BPS1"
        assert hashlib.sha256(b).hexdigest() == e["sha256"]
        sc, tc, pc = struct.unpack("<III", b[-12:])
        assert f"{sc:08X}" == e["from"].split(":")[1]
        assert f"{tc:08X}" == target.split(":")[1]
        assert pc == zlib.crc32(b[:-4]) == int(e["crc"], 16)
        print("VERIFIED", filename)
assert files == {p.name for p in (root / "downloads").glob("*v1.04*.bps")}
assert len(files) == 13
assert not list((root / "downloads").glob("*.gba")) and not list((root / "downloads").glob("*.sav"))
