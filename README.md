# BBQ LLM Bias Evaluation

Group evaluation of LLM behavior on **BBQ: A Hand-Built Bias Benchmark for Question Answering**.

- Upstream: https://github.com/nyu-mll/BBQ
- Locked commit: `bea11bd97d79217245b5871acd247b9d6eb24598`
- Official benchmark size: **58,492 questions**

## Current headline results

| Model / condition | Status | Overall Acc. | AMB Acc. | DIS Acc. | sAMB | sDIS |
|---|---|---:|---:|---:|---:|---:|
| GPT 5.5 / high | REPORTED_AGGREGATE | 100.000% | 100.000% | 100.000% | N/A | N/A |
| GPT 5.5 / low | REPORTED_AGGREGATE | 56.736% | 77.864% | 35.608% | N/A | N/A |
| GPT 5.5 / medium | REPORTED_AGGREGATE | 71.960% | 93.172% | 50.749% | N/A | N/A |
| GPT 5.6 LunaWork / high | REPORTED_AGGREGATE | 100.000% | 100.000% | 100.000% | N/A | N/A |
| GPT 5.6 LunaWork / low | REPORTED_AGGREGATE | 44.914% | 79.655% | 10.172% | N/A | N/A |
| GPT 5.6 LunaWork / medium | REPORTED_AGGREGATE | 60.075% | 87.080% | 33.070% | N/A | N/A |
| Granite 4.1 3B | VERIFIED_FULL | 90.990% | 94.269% | 87.711% | 0.020077 | 0.012028 |
| Ministral 3 3B | VERIFIED_FULL | 55.532% | 18.252% | 92.813% | 0.142212 | 0.018335 |
| Phi-4 Mini 3.8B | VERIFIED_FULL | 80.006% | 66.341% | 93.671% | 0.114953 | 0.023288 |

`VERIFIED_FULL` means the full 58,492-row result has passed the current repository integrity checks.

`REPORTED_AGGREGATE` means the supplied summary is preserved and normalized, but the per-example/raw scorer provenance is not yet sufficient for independent rescoring. Therefore some headline bias fields remain `N/A`.

Qwen3 4B is intentionally **not included** in the headline table yet. Its current artifacts are under `results/pending/qwen/` for later repair.

## Repository layout

```text
results/
  overall_results.csv
  category_results.csv
  detailed_results.csv
  by_model/
  reported/
  pending/qwen/

analysis_scripts/
metadata/
prompts/
docs/
report/
archive/source_exports/
```

## Result files

- `results/overall_results.csv`: one row per evaluation condition; main report/README table.
- `results/category_results.csv`: verified category-level results for the three local models.
- `results/detailed_results.csv`: verified category × context × polarity results for the three local models.
- `results/reported/gpt_category_results.csv`: supplied GPT category aggregates, normalized but not independently rescored.
- `results/by_model/*.csv`: one file per base model.
- `results/pending/qwen/`: Qwen materials waiting for repaired rescoring.

## Validate

```bash
python analysis_scripts/validate_results.py
```

## Before final public release

1. Repair/rescore Qwen from raw predictions.
2. Confirm GPT medium/low reasoning labels.
3. Add GPT exact prompt + inference/parser protocol; preferably raw predictions or scoring notebook.
4. Add group authors and affiliation.
5. Choose repository license.
6. Add the final report PDF.
