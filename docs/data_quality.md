# Data quality and repairs

## Local three-model results

Granite 4.1 3B, Phi-4 Mini 3.8B, and Ministral 3 3B each report the full **58,492** BBQ examples with **0 invalid outputs**. The supplied source is an already-verified summary export rather than per-example raw output.

## Qwen3 4B

The newly supplied raw prediction files resolve the earlier coverage concern:

- total rows: **58,492**
- unique `(category, example_id)` keys: **58,492**
- all official category counts match
- valid parsed outputs: **58,443**
- invalid format outputs: **49**
- output coverage: **99.9162%**

All 49 invalid outputs are strict-format failures where the post-thinking answer is `B.` or `C.` rather than exactly `B` or `C`. They are **not rescued**; this preserves the original strict parser policy.

The earlier Qwen summary had **58,556** rows because the supplied `additional_metadata.csv` contains 64 duplicate metadata rows. The canonical build uses a de-duplicated benchmark index, so those duplicates no longer inflate scoring.

## GPT 5.5 / GPT 5.6 Luna

All six supplied answer files contain exactly **58,492** sequential answers and every answer is a valid A/B/C choice.

The original GPT scoring notebook had two issues that are not used in the canonical results:

1. accuracy was computed after filtering to rows with `target_loc`, which unnecessarily removed the 16 rows lacking directional metadata;
2. its `biased_selected` logic flipped target direction on non-negative questions, while the BBQ scoring recipe defines bias by whether `target_loc` is selected across both polarities.

The canonical result files are rescored from the raw answer sequences using the common scorer in this repository.

### High-condition anomaly

`GPT 5.5 / high` and `GPT 5.6 Luna / high` contain the **same 58,492 answer sequence**, and that sequence matches the gold answer on every row.

The repository retains these supplied results, but flags them as an audit limitation because the inference prompt/runtime that generated them is unavailable in the supplied artifacts.
