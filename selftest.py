"""Run the visible development episodes through the isolated policy protocol."""
import argparse
import pathlib
import subprocess
import sys
p = argparse.ArgumentParser()
p.add_argument("--data", default="../eval_dev/episodes.json")
p.add_argument("--limit", type=int, default=2)
a = p.parse_args()
here = pathlib.Path(__file__).resolve().parent
raise SystemExit(subprocess.call([sys.executable, "-B", str(here.parent / "eval_dev/harness.py"),
    "--candidate", str(here / "policy.py"), "--data", a.data, "--limit", str(a.limit)]))
