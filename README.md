# BBQ LLM Bias Evaluation

Evaluation of social bias in large language models using
**BBQ: A Hand-Built Bias Benchmark for Question Answering**.

This repository contains the model outputs, canonical result tables,
scoring/validation utilities, and the final group report.

## Benchmark

- Upstream benchmark: https://github.com/nyu-mll/BBQ
- Locked commit: `bea11bd97d79217245b5871acd247b9d6eb24598`
- Evaluation size: **58,492 question-answering instances**
- Base model labels represented: **6**
- Evaluation conditions represented: **10**

The original BBQ benchmark is not redistributed as a new benchmark in this
repository. Benchmark data should be obtained from the locked upstream source.

## Evaluated conditions

- Granite 4.1 3B
- Phi-4 Mini 3.8B
- Ministral 3 3B
- Qwen3 4B Instruct
- GPT 5.5 — High / Medium / Light
- GPT 5.6 Luna — High / Medium / Light

The conditions were not produced under one fully controlled inference stack.
The local models share a common local protocol, Qwen uses a separate documented
runtime, and the complete server-side configuration of the GPT conditions was
not available.

## Overall results

| Model | Condition | Coverage | Overall Acc. | AMB Acc. | DIS Acc. | sAMB | sDIS | DIS gap |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Granite 4.1 3B | native | 100.000% | 90.990% | 94.269% | 87.711% | 0.020077 | 0.012028 | -1.043 pp |
| Phi-4 Mini 3.8B | native | 100.000% | 80.006% | 66.341% | 93.671% | 0.114953 | 0.023288 | -1.977 pp |
| Ministral 3 3B | native | 100.000% | 55.532% | 18.252% | 92.813% | 0.142212 | 0.018335 | -1.624 pp |
| Qwen3 4B Instruct | no_think_q6_k | 99.916% | 90.072% | 88.009% | 92.136% | 0.056166 | 0.023708 | -2.217 pp |
| GPT 5.5 | high* | 100.000% | 100.000% | 100.000% | 100.000% | 0.000000 | 0.005404 | 0.000 pp |
| GPT 5.5 | medium | 100.000% | 71.962% | 93.175% | 50.749% | 0.000000 | 0.010122 | -0.724 pp |
| GPT 5.5 | light | 100.000% | 56.734% | 77.864% | 35.605% | -0.000137 | 0.002074 | -0.162 pp |
| GPT 5.6 Luna | high* | 100.000% | 100.000% | 100.000% | 100.000% | 0.000000 | 0.005404 | 0.000 pp |
| GPT 5.6 Luna | medium | 100.000% | 60.078% | 87.082% | 33.075% | -0.000274 | 0.006183 | -0.511 pp |
| GPT 5.6 Luna | light | 100.000% | 44.914% | 79.655% | 10.172% | 0.000000 | 0.000000 | 0.206 pp |

> **Audit note.** `*` marks GPT High conditions. The supplied GPT 5.5-High
> and GPT 5.6-Luna-High answer sequences are identical and perfectly match the
> benchmark gold answers. Their complete inference configuration is unavailable,
> and the current non-zero `sDIS` values for these gold-perfect conditions are
> under scoring audit. These conditions are retained for transparency and are
> not used as the primary basis for model comparison.

The canonical exported values used by the current report are stored in
`results/overall_results.csv`.

Accuracy is computed over all attempted benchmark rows. Invalid outputs count
as incorrect under the project evaluation protocol. Directional-bias metrics
use valid target-scorable rows.

## Metric interpretation

- **AMB Acc.** — accuracy on ambiguous contexts, where the gold answer is
  `Unknown`.
- **DIS Acc.** — accuracy on disambiguated contexts.
- **sAMB** — ambiguous-context directional bias score.
- **sDIS** — disambiguated-context directional bias score.
- **DIS gap** — nonaligned minus aligned disambiguated accuracy, in percentage
  points.

Bias scores should be interpreted together with accuracy. A value close to zero
does not by itself imply appropriate model behavior.

## Repository structure

```text
report/
    Final report, LaTeX source, and report figures

results/
    Canonical result tables and by-model views

scripts/
    Result-building, scoring, and validation utilities

source_outputs/
    Available model outputs and supplied source artifacts

AUTHORS.md
    Project authorship information

LICENSE_TODO.md
    Current licensing status
