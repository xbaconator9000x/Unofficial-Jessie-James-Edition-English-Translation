#!/usr/bin/env python3
import importlib.util
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "scripts" / "inject_patch_events.py"
spec = importlib.util.spec_from_file_location("inject_patch_events", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
HTML = "<!doctype html><html><head></head><body>Safe</body></html>"

class Tests(unittest.TestCase):
    def test_unconfigured_is_noop(self):
        self.assertEqual(module.inject(HTML, ""), HTML)

    def test_inject_events_only(self):
        result = module.inject(HTML, "jessie-james-tracker")
        self.assertIn('data-goatcounter="https://jessie-james-tracker.goatcounter.com/count"', result)
        self.assertIn('data-goatcounter-settings=\'{"no_onload":true}\'', result)
        self.assertEqual(result.count("gc.zgo.at/count.js"), 1)
        self.assertLess(result.index("gc.zgo.at/count.js"), result.index("</body>"))
        self.assertEqual(result.count("</body>"), 1)

    def test_reject_injection_and_duplicates(self):
        for v in ["a.b", "a/b", "abc' onclick='x", "-invalid", "x" * 70]:
            with self.subTest(v=v), self.assertRaises(ValueError):
                module.inject(HTML, v)
        with self.assertRaises(ValueError):
            module.inject(module.inject(HTML, "validsite"), "validsite")

    def test_cli_off_and_on(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "index.html"
            p.write_text(HTML, encoding="utf-8")
            env = os.environ.copy()
            env.pop(module.VARIABLE, None)
            subprocess.run([sys.executable, str(PATH), str(p)], env=env, check=True, capture_output=True)
            self.assertEqual(p.read_text(encoding="utf-8"), HTML)
            env[module.VARIABLE] = "jessie-james-tracker"
            subprocess.run([sys.executable, str(PATH), str(p)], env=env, check=True, capture_output=True)
            self.assertIn("gc.zgo.at/count.js", p.read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
