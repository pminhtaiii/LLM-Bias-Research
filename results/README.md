# Result files

The canonical public results have three layers:

- `overall_results.csv` — one row per evaluation condition.
- `category_results.csv` — one row per evaluation condition × analysis category.
- `detailed_results.csv` — one row per evaluation condition × category × context × polarity.
- `by_model/` — convenience views with one file per base model.

The detailed result is intentionally the deepest public breakdown. Template/question-index diagnostics were removed from the main result structure to keep the repository focused.
