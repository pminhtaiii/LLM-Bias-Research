#!/usr/bin/env python3
from common_plot import draw_heatmap

draw_heatmap(
    metric="sAMB",
    title=r"Category-level ambiguous bias ($s_{AMB}$)",
    basename="fig04_samb_heatmap",
    fixed_limit=None,  # set 0.50 to lock the scale
)
