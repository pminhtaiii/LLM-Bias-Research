# BBQ LLM Bias Evaluation

Group evaluation of LLM behavior on **BBQ: A Hand-Built Bias Benchmark for Question Answering**.

- Upstream benchmark: https://github.com/nyu-mll/BBQ
- Locked commit: `bea11bd97d79217245b5871acd247b9d6eb24598`
- Benchmark size: **58,492 examples**
- Base model labels represented: **6**
- Evaluation conditions represented: **10**

## Overall results

| Model | Condition | Coverage | Overall Acc. | AMB Acc. | DIS Acc. | sAMB | sDIS | DIS gap |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Granite 4.1 3B | native | 100.000% | 90.990% | 94.269% | 87.711% | 0.020077 | 0.012028 | -1.043 pp |
| Phi-4 Mini 3.8B | native | 100.000% | 80.006% | 66.341% | 93.671% | 0.114953 | 0.023288 | -1.977 pp |
| Ministral 3 3B | native | 100.000% | 55.532% | 18.252% | 92.813% | 0.142212 | 0.018335 | -1.624 pp |
| Qwen3 4B Instruct | no_think_q6_k | 99.916% | 90.072% | 88.009% | 92.136% | 0.056166 | 0.023708 | -2.217 pp |
| GPT 5.5 | high | 100.000% | 100.000% | 100.000% | 100.000% | 0.000000 | 0.005404 | 0.000 pp |
| GPT 5.5 | medium | 100.000% | 71.962% | 93.175% | 50.749% | 0.000000 | 0.010122 | -0.724 pp |
| GPT 5.5 | light | 100.000% | 56.734% | 77.864% | 35.605% | -0.000137 | 0.002074 | -0.162 pp |
| GPT 5.6 Luna | high | 100.000% | 100.000% | 100.000% | 100.000% | 0.000000 | 0.005404 | 0.000 pp |
| GPT 5.6 Luna | medium | 100.000% | 60.078% | 87.082% | 33.075% | -0.000274 | 0.006183 | -0.511 pp |
| GPT 5.6 Luna | light | 100.000% | 44.914% | 79.655% | 10.172% | 0.000000 | 0.000000 | 0.206 pp |

The authoritative values are in `results/overall_results.csv`; this README intentionally stays compact.

Accuracy is computed over all attempted benchmark rows. Invalid outputs count as incorrect. Directional bias uses valid target-scorable rows.

## Repository structure

```text
benchmark/              BBQ upstream reference and fetch instructions
metadata/               compact benchmark index and model registry
source_outputs/         one source file per base model
results/                canonical result tables and by-model views
scripts/                fetch, rebuild, and validation scripts
notebooks/              original notebooks supplied by the group
docs/                   methodology, metrics, protocols, QC, limitations
report/                 final report location
```

## Main result files

- `results/overall_results.csv` — one row per evaluation condition.
- `results/category_results.csv` — condition × 13 analysis categories.
- `results/detailed_results.csv` — condition × category × context × polarity.
- `results/by_model/*.csv` — one convenience file per base model.

## Reproduce the result tables

The repository uses only the Python standard library.

```bash
python scripts/build_results.py
python scripts/validate_results.py
```

To fetch the exact upstream BBQ checkout used by the project:

```bash
python scripts/fetch_bbq.py
```

The full BBQ contexts, questions, answer choices, and gold labels are intentionally not duplicated here. They should be obtained from the locked upstream checkout.

## Source provenance

- **Granite 4.1 3B, Phi-4 Mini 3.8B, Ministral 3 3B**: verified full-BBQ summary exports.
- **Qwen3 4B**: full 58,492-row per-example predictions and raw outputs; rescored into the canonical schema.
- **GPT 5.5 / GPT 5.6 Luna**: complete answer sequences for high / medium / light conditions; rescored into the canonical schema.

## Data-quality notes

- Qwen3 4B contains **49 strict-format invalid outputs**. They remain invalid rather than being rescued.
- The earlier inflated Qwen summary was caused by duplicate metadata rows, not duplicate raw predictions.
- `GPT 5.5 / high` and `GPT 5.6 Luna / high` contain the same 58,492-answer sequence and both match the gold answer on every row. This is retained and documented as an audit limitation because the exact GPT inference prompt/runtime was not present in the supplied artifacts.

See `docs/` for methodology, metric definitions, inference provenance, data quality, and limitations.
