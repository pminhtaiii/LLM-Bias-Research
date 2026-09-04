#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from common_plot import EVALUATION_ORDER, DISPLAY_LABELS, overall_lookup, as_float, save_figure

lookup = overall_lookup()
labels = [DISPLAY_LABELS[e] for e in EVALUATION_ORDER]
x = np.arange(len(EVALUATION_ORDER))
width = 0.26

overall = [as_float(lookup[e]["overall_accuracy_pct"]) for e in EVALUATION_ORDER]
amb = [as_float(lookup[e]["ambig_accuracy_pct"]) for e in EVALUATION_ORDER]
dis = [as_float(lookup[e]["disambig_accuracy_pct"]) for e in EVALUATION_ORDER]

fig, ax = plt.subplots(figsize=(13.5, 6.4))
ax.bar(x - width, overall, width, label="Overall")
ax.bar(x, amb, width, label="AMB")
ax.bar(x + width, dis, width, label="DIS")
ax.set_ylabel("Accuracy (%)")
ax.set_title("Overall, ambiguous, and disambiguated BBQ accuracy")
ax.set_xticks(x, labels, rotation=35, ha="right")
ax.set_ylim(0, 105)
ax.legend()
ax.grid(axis="y", alpha=0.25)
fig.tight_layout()
save_figure(fig, "fig01_accuracy_by_condition")
