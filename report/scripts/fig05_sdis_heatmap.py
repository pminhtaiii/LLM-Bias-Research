#!/usr/bin/env python3
from common_plot import draw_heatmap

draw_heatmap(
    metric="sDIS",
    title=r"Category-level disambiguated bias ($s_{DIS}$)",
    basename="fig05_sdis_heatmap",
    fixed_limit=None,  # set 0.15 to lock the scale
)
