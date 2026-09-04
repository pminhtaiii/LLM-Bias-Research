#!/usr/bin/env python3
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
FILES = [
    "fig01_accuracy_by_condition.py",
    "fig02_samb_by_condition.py",
    "fig03_sdis_by_condition.py",
    "fig04_samb_heatmap.py",
    "fig05_sdis_heatmap.py",
    "fig06_alignment_gap.py",
    "fig07_gpt_samb_heatmap_zoom.py",
    "fig08_gpt_sdis_heatmap_zoom.py",
]

for filename in FILES:
    print(f"Building {filename}...")
    runpy.run_path(str(HERE / filename), run_name="__main__")

print("ALL FIGURES BUILT SUCCESSFULLY")
