# QC notes for report drafting

## Must be stated somewhere in the report

1. **Qwen3 4B strict parser:** 49 / 58,492 outputs are invalid under the original exact-A/B/C parser. They remain invalid and count as incorrect in accuracy.
2. **Qwen metadata repair:** an earlier 58,556-row aggregate was inflated by duplicated metadata rows. The canonical analysis uses the 58,492 unique raw predictions.
3. **GPT high anomaly:** GPT 5.5-high and GPT 5.6-Luna-high have identical perfect answer sequences.
4. **GPT provenance:** exact inference prompt/runtime/sampling settings are not available in the supplied artifacts. Scores are reproducible from the answer sequences, but inference provenance is partial.
5. **Directional metadata:** 16 BBQ rows lack usable `target_loc`. They remain in accuracy calculations and are excluded only from directional-bias/alignment metrics.
6. **No significance language yet:** category differences and alignment gaps are descriptive unless confidence intervals/tests are added.

## Avoid in the report

- Do not describe the results as a leaderboard of general model intelligence.
- Do not interpret sAMB/sDIS near zero as proof of “no bias.”
- Do not describe observed alignment gaps as statistically significant without formal uncertainty analysis.
- Do not claim the exact GPT high inference procedure is reproduced.
