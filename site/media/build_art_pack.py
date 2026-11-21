#!/usr/bin/env python3
"""Package the three approved artwork files for the public download."""
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

root = Path(__file__).resolve().parent
files = (
    ("GBA-Box-Art.jpg", "jessie-james-cover-snowmudk99.jpg"),
    ("Logo-with-Rocket-R.webp", "jessie-james-logo-snowmudk99.webp"),
    ("Logo-without-Rocket-R.webp", "jessie-james-logo-clean-snowmudk99.webp"),
)
output = root / "jessie-james-fan-art-pack.zip"
with ZipFile(output, "w") as zf:
    for archive_name, source_name in files:
        source = root / source_name
        content = source.read_bytes()
        if len(content) < 1000:
            raise ValueError(f"Missing or empty media: {source_name}")
        info = ZipInfo(archive_name, (2026, 11, 21, 0, 0, 0))
        info.compress_type = ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        zf.writestr(info, content, compress_type=ZIP_DEFLATED, compresslevel=9)
print(f"Created {output.name} ({output.stat().st_size} bytes)")
