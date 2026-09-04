#!/usr/bin/env python3
"""Fetch the locked upstream BBQ repository into benchmark/BBQ-upstream."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'benchmark' / 'BBQ-upstream'
URL = 'https://github.com/nyu-mll/BBQ.git'
COMMIT = 'bea11bd97d79217245b5871acd247b9d6eb24598'

if DEST.exists():
    raise SystemExit(f'{DEST} already exists. Remove it first for a fresh clone.')
subprocess.run(['git', 'clone', URL, str(DEST)], check=True)
subprocess.run(['git', '-C', str(DEST), 'checkout', COMMIT], check=True)
print('Fetched BBQ at locked commit:', COMMIT)
