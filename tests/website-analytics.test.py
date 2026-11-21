#!/usr/bin/env python3
"""Smoke tests for the optional Cloudflare Web Analytics deploy hook."""
import importlib.util
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "scripts" / "inject_web_analytics.py"
spec = importlib.util.spec_from_file_location("inject_web_analytics", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
TOKEN = "bc40a2d1b5834453aba85c1b9a3054da"
HTML = "<!doctype html><html><head></head><body>Safe content</body></html>"


class WebsiteAnalyticsTests(unittest.TestCase):
    def test_disabled_by_default(self):
        self.assertEqual(module.inject(HTML, ""), HTML)

    def test_valid_token_one_beacon_before_body(self):
        result = module.inject(HTML, TOKEN)
        self.assertEqual(result.count(module.BEACON_URL), 1)
        self.assertEqual(result.count("</body>"), 1)
        self.assertIn('"token":"' + TOKEN + '"', result)
        self.assertIn("Safe content", result)
        self.assertLess(result.index(module.BEACON_URL), result.index("</body>"))
        self.assertNotIn("cookies", result.lower())

    def test_invalid_token_rejected(self):
        for token in ("", "not-a-token", "bad' onclick='x", "0" * 33):
            if not token:
                continue
            with self.subTest(token=token):
                with self.assertRaises(ValueError):
                    module.inject(HTML, token)

    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError):
            module.inject(module.inject(HTML, TOKEN), TOKEN)

    def test_cli_disabled_is_noop(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "index.html"
            f.write_text(HTML, encoding="utf-8")
            env = os.environ.copy()
            env.pop(module.TOKEN_VARIABLE, None)
            subprocess.run([sys.executable, str(PATH), str(f)], env=env, check=True, capture_output=True)
            self.assertEqual(f.read_text(encoding="utf-8"), HTML)

    def test_cli_inserts_valid_beacon(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "index.html"
            f.write_text(HTML, encoding="utf-8")
            env = os.environ.copy()
            env[module.TOKEN_VARIABLE] = TOKEN
            subprocess.run([sys.executable, str(PATH), str(f)], env=env, check=True, capture_output=True)
            self.assertIn(module.BEACON_URL, f.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
