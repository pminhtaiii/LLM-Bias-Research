#!/usr/bin/env python3
from common_plot import EVALUATION_ORDER, draw_heatmap

gpt_ids = [eid for eid in EVALUATION_ORDER if eid.startswith("gpt_")]

draw_heatmap(
    metric="sAMB",
    title=r"GPT-only category-level ambiguous bias ($s_{AMB}$, zoomed scale)",
    basename="fig07_gpt_samb_heatmap_zoom",
    evaluation_ids=gpt_ids,
    fixed_limit=None,
    footer_note="Supplementary zoom; do not compare color intensity directly with the main heatmap.",
)
