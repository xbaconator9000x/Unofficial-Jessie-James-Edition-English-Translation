#!/usr/bin/env python3
"""Configure GoatCounter pageviews and patcher events on the Pages deployment.

GoatCounter provides daily email summaries; Cloudflare independently tracks
website traffic. No ROM, save, file, or patch details are sent by this injector.
"""
import os
import re
import sys
from html import escape
from pathlib import Path

VARIABLE = "GOATCOUNTER_SITE_CODE"

def inject(source: str, code: str) -> str:
    code = code.strip().lower()
    if not code:
        return source
    if not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,60}[a-z0-9])?", code):
        raise ValueError("Invalid GoatCounter site code; expected its subdomain label only")
    if source.count("</body>") != 1 or "gc.zgo.at/count.js" in source:
        raise ValueError("Expected one </body> and no existing GoatCounter script")
    endpoint = "https://" + code + ".goatcounter.com/count"
    snippet = (
        "  <!-- Cookie-free website visits and anonymous patch events; no ROM content -->\n"
        f'  <script defer src="https://gc.zgo.at/count.js" '
        f'data-goatcounter="{escape(endpoint, quote=True)}"></script>\n'
    )
    return source.replace("</body>", snippet + "</body>")

def main() -> None:
    filename = Path(sys.argv[1] if len(sys.argv) > 1 else "site/index.html")
    code = os.environ.get(VARIABLE, "")
    if not code.strip():
        print(f"Patch-event counts inactive: add Actions variable {VARIABLE} to activate.")
        return
    source = filename.read_text(encoding="utf-8")
    filename.write_text(inject(source, code), encoding="utf-8")
    print("GoatCounter pageviews and patcher event tracker included in deployment artifact.")

if __name__ == "__main__":
    main()
