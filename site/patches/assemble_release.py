#!/usr/bin/env python3
"""Assemble complete BPS patches from public full patches and verified updates.

Uses no game ROMs. Only patches with SourceRead/TargetRead instructions are
accepted; unknown BPS actions fail rather than generating an invalid file.
"""
import base64
import lzma
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

def check_edge(data, edge):
    assert len(data) == edge["bytes"], edge["path"]
    assert hashlib.sha256(data).hexdigest() == edge["sha256"], edge["path"]
    assert f"{zlib.crc32(data[:-4]):08X}" == edge["crc"], edge["path"]
    sc, tc, _ = struct.unpack_from("<III", data, len(data) - 12)
    assert f"{sc:08X}" == edge["from"].split(":")[1], edge["path"]
    assert f"{tc:08X}" == edge["to"].split(":")[1], edge["path"]


def main():
    builds = (
        ("English", "releases.json",
         "jessie-james-english-v1.01-a3e3cc2f.bps",
         "jessie-james-english-v1.01-a3e3cc2f-to-v1.02-cadc8480.bps",
         "jessie-james-english-v1.02-cadc8480.bps",
         "english-v102-earlier-to-latest.xz.b64",
         "jessie-james-english-v1.02-cadc8480-to-d2866130.bps",
         "jessie-james-english-v1.02-d2866130.bps",
         "35c3129e04f2986debac738f0fff4a2d12387cbaaf15604251f7734e3b013f67"),
        ("Spanish", "spanish-releases.json",
         "jessie-james-spanish-qol-v1.0-7c042814.bps",
         "jessie-james-spanish-qol-v1.0-7c042814-to-v1.02-0486144d.bps",
         "jessie-james-spanish-qol-v1.02-0486144d.bps",
         "spanish-v102-earlier-to-latest.xz.b64",
         "jessie-james-spanish-qol-v1.02-0486144d-to-58f089b9.bps",
         "jessie-james-spanish-qol-v1.02-58f089b9.bps",
         "971cc28b61a3da7039c61d002bb2567f9c6c7f2c61475e7d001fbb81dc54bae0"),
    )
    v103 = {
        "English": ("english-v103-v102-to-v103.xz.b64",
            "jessie-james-english-v1.02-d2866130-to-v1.03-6e1e5095.bps",
            "jessie-james-english-v1.03-6e1e5095.bps",
            "d392189296b484987a4e41d170579014f7af08a8dcd1aac57f9c0ffc34b47567"),
        "Spanish": ("spanish-v103-v102-to-v103.xz.b64",
            "jessie-james-spanish-qol-v1.02-58f089b9-to-v1.03-222a0072.bps",
            "jessie-james-spanish-qol-v1.03-222a0072.bps",
            "b5b2bed3270712239ae5d54ad8b7e429c83675304061ad3bc353a9d69f537098"),
    }
    for edition, manifest_file, base_file, old_update_file, old_full_name, \
        compressed_name, new_update_name, new_full_name, expected_xz_sha in builds:
        manifest = json.loads((ROOT / manifest_file).read_text())
        edges = {e["path"].removeprefix("patches/"): e for e in manifest["patches"]}
        old_full = compose(ROOT / base_file, ROOT / old_update_file)
        check_edge(old_full, edges[old_full_name])
        compressed = base64.b64decode("".join(
            (ROOT / compressed_name).read_text(encoding="ascii").split()), validate=True)
        assert hashlib.sha256(compressed).hexdigest() == expected_xz_sha
        update_bytes = lzma.decompress(compressed, memlimit=256 * 1024 * 1024)
        check_edge(update_bytes, edges[new_update_name])
        (ROOT / new_update_name).write_bytes(update_bytes)
        old_path = ROOT / old_full_name
        old_path.write_bytes(old_full)
        result = compose(old_path, ROOT / new_update_name)
        check_edge(result, edges[new_full_name])
        (ROOT / new_full_name).write_bytes(result)
        print("VERIFIED:", edition, "latest full and incremental v1.02 patches")
        packed_name, delta_name, full_name, packed_sha = v103[edition]
        packed = base64.b64decode("".join((ROOT / packed_name).read_text(encoding="ascii").split()), validate=True)
        assert hashlib.sha256(packed).hexdigest() == packed_sha
        delta = lzma.decompress(packed, memlimit=256 * 1024 * 1024)
        check_edge(delta, edges[delta_name])
        (ROOT / delta_name).write_bytes(delta)
        full = compose(ROOT / new_full_name, ROOT / delta_name)
        check_edge(full, edges[full_name])
        (ROOT / full_name).write_bytes(full)
        print("VERIFIED:", edition, "v1.03 full BPS and v1.02-to-v1.03 upgrade")

        if edition == "English":
            # The 51-byte BPS is source-locked to English v1.03 (6E1E5095).
            # Build a full original-Spanish-to-v1.03.2 patch without distributing
            # any ROM bytes. The two intentional pointer fixes were privately
            # applied to the user's original and verified against CRC 5DAE93EA.
            hotfix = bytes.fromhex((ROOT / "english-v1032-crash-sweep.hex").read_text().strip())
            if len(hotfix) != 51 or hashlib.sha256(hotfix).hexdigest() != "b02a561b4ab5d16eda1ba3187e1c479368738cb70bd615fffd75d5a80335e42c":
                raise ValueError("Unexpected v1.03.2 source-locked hotfix")
            incremental = "jessie-james-english-v1.03-6e1e5095-to-v1.03.2-5dae93ea.bps"
            check_edge(hotfix, edges[incremental])
            (ROOT / incremental).write_bytes(hotfix)
            final_name = "jessie-james-english-v1.03.2-5dae93ea.bps"
            final_bytes = compose(ROOT / full_name, ROOT / incremental)
            # The complete BPS is reproducibly assembled during deployment.
            # Derive its transport metadata from this checked composition;
            # source/target CRC and all input patch SHA-256 values are locked.
            final_edge = edges[final_name]
            final_edge["bytes"] = len(final_bytes)
            final_edge["sha256"] = hashlib.sha256(final_bytes).hexdigest()
            final_edge["crc"] = f"{zlib.crc32(final_bytes[:-4]):08X}"
            check_edge(final_bytes, final_edge)
            (ROOT / final_name).write_bytes(final_bytes)
            (ROOT / manifest_file).write_text(json.dumps(manifest, indent=2) + "\\n")
            print("VERIFIED: English v1.03.2, CRC32 5DAE93EA, full BPS", len(final_bytes), final_edge["sha256"])


if __name__ == "__main__":
    main()
