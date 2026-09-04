#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from common_plot import EVALUATION_ORDER, DISPLAY_LABELS, overall_lookup, as_float, save_figure

lookup = overall_lookup()
labels = [DISPLAY_LABELS[e] for e in EVALUATION_ORDER]
values = [as_float(lookup[e]["sDIS"]) for e in EVALUATION_ORDER]
y = np.arange(len(values))

fig, ax = plt.subplots(figsize=(10.5, 6.2))
ax.barh(y, values)
ax.set_yticks(y, labels)
ax.axvline(0, linewidth=1)
ax.set_xlabel(r"$s_{DIS}$")
ax.set_title("Disambiguated-context bias score by evaluation condition")
ax.invert_yaxis()
ax.grid(axis="x", alpha=0.25)

max_abs = max(abs(v) for v in values if np.isfinite(v))
pad = max(0.01, max_abs * 0.12)
ax.set_xlim(-max_abs - pad, max_abs + pad)
fig.tight_layout()
save_figure(fig, "fig03_sdis_by_condition")
