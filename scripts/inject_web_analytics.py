#!/usr/bin/env python3
"""Cookie-free site analytics for the published GitHub Pages artifact.

The public Cloudflare site token is configured by default; an Actions variable can override it.
The token is a public site identifier, not an account API key or credential.
"""
import json
import os
import re
import sys
from pathlib import Path

TOKEN_VARIABLE = "CLOUDFLARE_WEB_ANALYTICS_TOKEN"
DEFAULT_SITE_TOKEN = "fadc19aedae34f09b7b4016821e8810f"
BEACON_URL = "https://static.cloudflareinsights.com/beacon.min.js"


def inject(html: str, token: str) -> str:
    token = token.strip()
    if not token:
        return html
    if not re.fullmatch(r"[a-fA-F0-9]{32}", token):
        raise ValueError(f"{TOKEN_VARIABLE} must be the 32-character hexadecimal site token")
    if html.count("</body>") != 1:
        raise ValueError("Expected exactly one closing </body> in the launcher HTML")
    if BEACON_URL in html:
        raise ValueError("Analytics beacon already present; refusing duplicate injection")
    settings = json.dumps({"token": token}, separators=(",", ":"))
    beacon = (
        "  <!-- Privacy-friendly site traffic analytics; no ROM or file contents transmitted -->\n"
        f'  <script defer src="{BEACON_URL}" data-cf-beacon=\'{settings}\'></script>\n'
    )
    return html.replace("</body>", beacon + "</body>")


def main() -> None:
    html_path = Path(sys.argv[1] if len(sys.argv) > 1 else "site/index.html")
    token = os.environ.get(TOKEN_VARIABLE) or DEFAULT_SITE_TOKEN
    if not token.strip():
        print(f"Web Analytics not enabled: set the Actions variable {TOKEN_VARIABLE} to activate.")
        return
    html = html_path.read_text(encoding="utf-8")
    html_path.write_text(inject(html, token), encoding="utf-8")
    print("Cloudflare Web Analytics beacon injected into the deployment artifact.")


if __name__ == "__main__":
    main()
