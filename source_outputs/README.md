# Source outputs

This folder is **model-centric**: one file per base model.

The source granularity differs because the group did not retain the same artifacts for every model:

- `granite_4_1_3b.csv`, `phi4_mini_3_8b.csv`, `ministral_3_3b.csv`:
  verified summary exports containing only the result levels used by the public repository.
- `qwen3_4b.csv`:
  full 58,492-row per-example predictions, including raw output and parse status.
- `gpt_5_5.csv`, `gpt_5_6_luna.csv`:
  full answer files for three conditions (`high`, `medium`, `light`) combined into one file per base model.

No contributor/member names are encoded into the result hierarchy.
