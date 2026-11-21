#!/usr/bin/env python3
"""Source-independent v1.03 release candidate metadata probe (no ROMs)."""
import base64, hashlib, lzma, struct, sys, zlib
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "site" / "patches"
sys.path.insert(0, str(root))
from assemble_release import compose

entries = (
    ("english", "jessie-james-english-v1.02-d2866130.bps", "english-v103-v102-to-v103.xz.b64",
     "d392189296b484987a4e41d170579014f7af08a8dcd1aac57f9c0ffc34b47567",
     "cc00bda16123da85cac8a19a2df52037d767a0eb91839f9e5efbee5f9958f089",
     9159, 0xD2866130, 0x6E1E5095, 0xBE1FC6CD),
    ("spanish", "jessie-james-spanish-qol-v1.02-58f089b9.bps", "spanish-v103-v102-to-v103.xz.b64",
     "b5b2bed3270712239ae5d54ad8b7e429c83675304061ad3bc353a9d69f537098",
     "c8a5338246745573bb8711c134964f621165be33c4994c44ee2393b9f98a975a",
     9157, 0x58F089B9, 0x222A0072, 0xE73CC81D),
)
for edition, old_full_name, compressed_name, compressed_sha, delta_sha, delta_len, old_crc, new_crc, delta_crc in entries:
    compressed = base64.b64decode((root / compressed_name).read_text().strip(), validate=True)
    assert hashlib.sha256(compressed).hexdigest() == compressed_sha
    delta = lzma.decompress(compressed, memlimit=256*1024*1024)
    assert len(delta) == delta_len and hashlib.sha256(delta).hexdigest() == delta_sha
    assert zlib.crc32(delta[:-4]) == delta_crc
    assert struct.unpack("<III", delta[-12:]) == (old_crc, new_crc, delta_crc)
    temp = root / ("_candidate-" + edition + ".bps")
    try:
        temp.write_bytes(delta)
        full = compose(root / old_full_name, temp)
    finally:
        temp.unlink(missing_ok=True)
    assert struct.unpack("<II", full[-12:-4]) == (0x805E24CA, new_crc)
    assert struct.unpack("<I", full[-4:])[0] == zlib.crc32(full[:-4])
    print("CANDIDATE", edition, "full_bytes", len(full),
          "full_sha256", hashlib.sha256(full).hexdigest(),
          "full_crc", f"{zlib.crc32(full[:-4]):08X}",
          "delta_bytes", len(delta), "delta_crc", f"{delta_crc:08X}")
