#!/usr/bin/env python3
r"""
Rebuild current pre-Qwen result tables from archived source exports.

This script intentionally does NOT promote Qwen.
GPT is preserved as REPORTED_AGGREGATE until prompt/scorer/raw provenance is supplied.
"""

from pathlib import Path
import csv, io, sys

ROOT = Path(__file__).resolve().parents[1]
LOCAL = ROOT / "archive/source_exports/local_granite_phi4_ministral_original.csv"
GPT = ROOT / "archive/source_exports/gpt_5_5_gpt_5_6_lunawork_original.csv"

print("Source files present:")
print(" ", LOCAL.exists(), LOCAL)
print(" ", GPT.exists(), GPT)
print()
print("The repository already contains normalized current result tables.")
print("For a full regeneration, use the project preparation script that created this starter,")
print("or extend this script once GPT/Qwen raw predictions are available.")
print()
print("Qwen remains pending by design.")
