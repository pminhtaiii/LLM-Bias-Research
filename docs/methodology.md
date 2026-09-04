# Methodology

## Evaluation scope

The repository compares six base model labels across ten evaluation conditions on the full 58,492-example BBQ benchmark.

## Canonical analysis categories

The 11 BBQ source categories are represented as 13 analysis categories by splitting:
- `Gender_identity` into explicit labels vs proper names;
- `Race_ethnicity` into explicit labels vs proper names.

`Race_x_gender` and `Race_x_SES` remain pooled categories.

## Scoring source

- Local three-model results are imported from the supplied verified summary exports.
- Qwen3 4B is rescored from the full raw prediction files.
- GPT 5.5 and GPT 5.6 Luna are rescored from the full answer files.

The canonical scorer uses the same `target_loc` direction for negative and non-negative questions, matching the BBQ scoring recipe.

Rows without usable `target_loc` remain part of accuracy calculations and are excluded only from directional bias/alignment metrics.
