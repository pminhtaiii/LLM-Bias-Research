from pathlib import Path
import csv
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
FIGURE_DIR = ROOT / "figures"

EVALUATION_ORDER = [
    "granite_4_1_3b__native",
    "phi4_mini_3_8b__native",
    "ministral_3_3b__native",
    "qwen3_4b__no_think_q6_k",
    "gpt_5_5__high",
    "gpt_5_5__medium",
    "gpt_5_5__light",
    "gpt_5_6_luna__high",
    "gpt_5_6_luna__medium",
    "gpt_5_6_luna__light",
]

DISPLAY_LABELS = {
    "granite_4_1_3b__native": "Granite 4.1 3B",
    "phi4_mini_3_8b__native": "Phi-4 Mini",
    "ministral_3_3b__native": "Ministral 3 3B",
    "qwen3_4b__no_think_q6_k": "Qwen3 4B",
    "gpt_5_5__high": "GPT 5.5-H",
    "gpt_5_5__medium": "GPT 5.5-M",
    "gpt_5_5__light": "GPT 5.5-L",
    "gpt_5_6_luna__high": "GPT 5.6-H",
    "gpt_5_6_luna__medium": "GPT 5.6-M",
    "gpt_5_6_luna__light": "GPT 5.6-L",
}

HEATMAP_CMAP = "RdBu_r"
PNG_DPI = 300
HEATMAP_DECIMALS = 3

def read_csv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def as_float(value):
    if value is None:
        return np.nan
    s = str(value).strip()
    return np.nan if not s else float(s)

def save_figure(fig, basename: str):
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURE_DIR / f"{basename}.png", dpi=PNG_DPI, bbox_inches="tight")
    fig.savefig(FIGURE_DIR / f"{basename}.pdf", bbox_inches="tight")
    plt.close(fig)

def overall_lookup():
    rows = read_csv(DATA_DIR / "overall_results.csv")
    return {r["evaluation_id"]: r for r in rows}

def category_rows():
    return read_csv(DATA_DIR / "category_results.csv")

def ordered_categories(rows):
    return sorted({r["category"] for r in rows})

def nice_symmetric_limit(max_abs: float) -> float:
    if not np.isfinite(max_abs) or max_abs <= 0:
        return 0.01
    exponent = math.floor(math.log10(max_abs))
    scale = 10 ** exponent
    normalized = max_abs / scale
    for candidate in (1.0, 1.5, 2.0, 2.5, 5.0, 10.0):
        if normalized <= candidate:
            return candidate * scale
    return 10.0 * scale

def build_heatmap_matrix(metric: str, evaluation_ids=None):
    rows = category_rows()
    categories = ordered_categories(rows)
    evaluation_ids = evaluation_ids or EVALUATION_ORDER
    lookup = {(r["evaluation_id"], r["category"]): r for r in rows}
    matrix = np.array([
        [as_float(lookup[(eid, cat)][metric]) for eid in evaluation_ids]
        for cat in categories
    ], dtype=float)
    return categories, evaluation_ids, matrix

def rgba_luminance(rgba):
    r, g, b, _ = rgba
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def format_cell(value: float, decimals: int = HEATMAP_DECIMALS) -> str:
    threshold = 0.5 * 10 ** (-decimals)
    if abs(value) < threshold:
        return f"{0:.{decimals}f}"
    return f"{value:+.{decimals}f}"

def draw_heatmap(metric, title, basename, evaluation_ids=None, fixed_limit=None, footer_note=None):
    categories, evaluation_ids, matrix = build_heatmap_matrix(metric, evaluation_ids)
    labels = [DISPLAY_LABELS[e] for e in evaluation_ids]

    observed_max = float(np.nanmax(np.abs(matrix)))
    limit = fixed_limit if fixed_limit is not None else nice_symmetric_limit(observed_max)

    norm = TwoSlopeNorm(vmin=-limit, vcenter=0.0, vmax=limit)
    cmap = plt.get_cmap(HEATMAP_CMAP)

    width = max(10.0, 1.08 * len(evaluation_ids) + 5.0)
    height = max(7.6, 0.52 * len(categories) + 2.7)

    fig, ax = plt.subplots(figsize=(width, height))
    image = ax.imshow(matrix, aspect="auto", cmap=cmap, norm=norm)

    ax.set_xticks(np.arange(len(labels)), labels, rotation=35, ha="right")
    ax.set_yticks(np.arange(len(categories)), categories)
    ax.set_xlabel("Evaluation condition")
    ax.set_ylabel("BBQ analysis category")
    ax.set_title(title)

    ax.set_xticks(np.arange(-0.5, len(labels), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(categories), 1), minor=True)
    ax.grid(which="minor", linewidth=0.6, alpha=0.35)
    ax.tick_params(which="minor", bottom=False, left=False)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            value = matrix[i, j]
            rgba = cmap(norm(value))
            text_color = "black" if rgba_luminance(rgba) > 0.58 else "white"
            ax.text(
                j, i, format_cell(value),
                ha="center", va="center",
                fontsize=7.1, color=text_color,
            )

    cbar = fig.colorbar(image, ax=ax, fraction=0.035, pad=0.025)
    cbar.set_label(metric)
    cbar.set_ticks(np.linspace(-limit, limit, 5))

    footer = (
        f"Symmetric color scale centered at 0; range = [{-limit:.3f}, +{limit:.3f}]. "
        "Cell labels show exact scores."
    )
    if footer_note:
        footer += " " + footer_note
    fig.text(0.5, 0.012, footer, ha="center", va="bottom", fontsize=8.5)
    fig.tight_layout(rect=(0, 0.035, 1, 1))
    save_figure(fig, basename)
