# Result schema

## `results/overall_results.csv`
Headline table. One row per evaluation condition.

`verification_status` is critical:
- `VERIFIED_FULL`: independently checked full BBQ result.
- `REPORTED_AGGREGATE`: supplied aggregate is preserved, but raw/scorer provenance is incomplete.

## `results/category_results.csv`
Verified canonical category-level result. Currently contains the three local models only.

## `results/detailed_results.csv`
Verified model × category × context × polarity result. Currently contains the three local models only.

## `results/reported/gpt_category_results.csv`
GPT category aggregates exactly normalized from the supplied source file. Kept separate because source taxonomy/provenance is not yet fully harmonized.

## `results/by_model/`
One file per base model. Files may contain multiple evaluation conditions for the same base model.

## `results/pending/qwen/`
Qwen artifacts waiting for repair/rescoring.
