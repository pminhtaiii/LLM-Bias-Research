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

Accuracy is computed over all attempted benchmark rows; invalid outputs count as incorrect. Bias metrics use valid target-scorable rows only.

## Repository structure

```text
benchmark/                upstream reference; no duplicated full BBQ text
metadata/                 benchmark index + model registry
source_outputs/           one source file per base model
results/                  overall, category, detailed, and by-model results
scripts/                  build/validation entry points
notebooks/                original Qwen/GPT notebooks that were actually supplied
docs/                     methodology, metrics, protocols, QC, limitations
report/                   report outline / later final report
```

## Source provenance

- Granite 4.1 3B, Phi-4 Mini 3.8B, Ministral 3 3B: verified summary exports.
- Qwen3 4B: full raw per-example predictions; rescored canonically.
- GPT 5.5 / GPT 5.6 Luna: full answer sequences; rescored canonically. Exact inference prompt/runtime was not present in the supplied files.

## Important QC notes

- Qwen3 4B has **49 strict-format invalid outputs**; coverage is below 100%.
- The earlier Qwen 58,556-row summary was caused by **64 duplicated metadata rows**; the raw predictions themselves contain the correct 58,492 examples.
- `GPT 5.5 / high` and `GPT 5.6 Luna / high` contain the same 58,492 answer sequence and both match the gold answers on every row. The results are retained, with this anomaly documented rather than explained without evidence.
- The original GPT scoring notebook is preserved only as provenance. Canonical results use the common scoring definition documented in `docs/metrics.md`.

## Validate

```bash
python scripts/validate_results.py
```

## Benchmark text and answers

The complete BBQ contexts, questions, answer choices, and gold labels should be obtained from the upstream BBQ repository at the locked commit rather than duplicated here. `metadata/benchmark_index.csv` contains only the compact fields required to align and score the supplied outputs.

## Before final submission

Add the group author names/affiliation, choose a repository license, and place the final report under `report/`.
