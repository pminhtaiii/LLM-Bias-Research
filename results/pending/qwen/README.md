# Qwen3 4B — pending repair

Qwen is intentionally excluded from canonical/report-ready results for now.

Known from the supplied notebooks:
- Qwen3 4B Instruct
- `Qwen3-4B-Q6_K.gguf`
- Kaggle Tesla T4
- `llama-cpp-python==0.3.35`
- `n_ctx=2048`
- `temperature=0`
- `max_tokens=10`
- `/no_think`

Current supplied summary has a row-count mismatch and should be rescored from raw predictions before promotion.

Files preserved here:
- `source/qwen_bbq_scores_original.csv`
- inference notebook
- original scoring notebook

Later requirement:
- raw `qwen_*_predictions.csv` files (preferably as one ZIP)
