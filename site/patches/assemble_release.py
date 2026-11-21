#!/usr/bin/env python3
"""Assemble complete BPS patches from public full patches and verified updates.

Uses no game ROMs. Only patches with SourceRead/TargetRead instructions are
accepted; unknown BPS actions fail rather than generating an invalid file.
"""
import hashlib
import json
import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def number(data, index):
    value, shift = 0, 1
    while True:
        if index >= len(data) - 12:
            raise ValueError("Truncated BPS")
        b = data[index]
        index += 1
        value += (b & 127) * shift
        if b & 128:
            return value, index
        shift *= 128
        value += shift

def encoded(value):
    out = bytearray()
    while True:
        b = value & 127
        value >>= 7
        if not value:
            out.append(b | 128)
            return out
        out.append(b)
        value -= 1

def get_literals(path):
    raw = path.read_bytes()
    if raw[:4] != b"BPS1":
        raise ValueError("Invalid BPS signature")
    sc, tc, pc = struct.unpack_from("<III", raw, len(raw) - 12)
    calc = zlib.crc32(raw[:-4])
    if pc not in (0, calc):
        raise ValueError("BPS checksum mismatch")
    at = 4
    source_size, at = number(raw, at)
    size, at = number(raw, at)
    metadata_size, at = number(raw, at)
    at += metadata_size
    if source_size != size or size != 16777216:
        raise ValueError("Unexpected ROM size")
    mask, values = bytearray(size), bytearray(size)
    pos = 0
    while pos < size:
        op, at = number(raw, at)
        mode, count = op % 4, op // 4 + 1
        end = pos + count
        if end > size:
            raise ValueError("BPS output overflow")
        if mode == 1:
            if at + count > len(raw) - 12:
                raise ValueError("Truncated BPS literal")
            mask[pos:end] = b"\x01" * count
            values[pos:end] = raw[at:at + count]
            at += count
        elif mode != 0:
            raise ValueError("Unsupported BPS instruction")
        pos = end
    if at != len(raw) - 12:
        raise ValueError("Trailing BPS data")
    return size, sc, tc, mask, values

def compose(base, update):
    size, source_crc, intermediate_crc, mask, data = get_literals(base)
    update_size, update_source, target_crc, edits, replacement = get_literals(update)
    if update_size != size or update_source != intermediate_crc:
        raise ValueError("Source and update do not match")
    for i, flag in enumerate(edits):
        if flag:
            mask[i], data[i] = 1, replacement[i]
    out = bytearray(b"BPS1")
    out += encoded(size) + encoded(size) + encoded(0)
    pos = 0
    while pos < size:
        flag, end = mask[pos], pos + 1
        while end < size and mask[end] == flag:
            end += 1
        out += encoded((end - pos - 1) * 4 + (1 if flag else 0))
        if flag:
            out += data[pos:end]
        pos = end
    out += struct.pack("<II", source_crc, target_crc)
    out += struct.pack("<I", zlib.crc32(out))
    return out

def main():
    builds = (
        ("english", "releases.json",
         "jessie-james-english-v1.01-a3e3cc2f.bps",
         "jessie-james-english-v1.01-a3e3cc2f-to-v1.02-cadc8480.bps",
         "jessie-james-english-v1.02-cadc8480.bps"),
        ("spanish", "spanish-releases.json",
         "jessie-james-spanish-qol-v1.0-7c042814.bps",
         "jessie-james-spanish-qol-v1.0-7c042814-to-v1.02-0486144d.bps",
         "jessie-james-spanish-qol-v1.02-0486144d.bps"),
    )
    for edition, manifest_file, source, delta, output in builds:
        result = compose(ROOT / source, ROOT / delta)
        manifest = json.loads((ROOT / manifest_file).read_text())
        edge = next(x for x in manifest["patches"] if x["path"] == "patches/" + output)
        assert len(result) == edge["bytes"]
        assert hashlib.sha256(result).hexdigest() == edge["sha256"]
        assert f"{zlib.crc32(result[:-4]):08X}" == edge["crc"]
        (ROOT / output).write_bytes(result)
        print("Verified", edition, output)

if __name__ == "__main__":
    main()
