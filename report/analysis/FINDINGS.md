# Candidate findings for the report

These are evidence-backed observations from the current canonical result tables. They are **not claims of statistical significance** unless confidence intervals or formal tests are added later.

## F01 — Ambiguous-context handling separates the local models strongly

Among the three local GGUF evaluations, Granite 4.1 3B has the strongest ambiguous-context accuracy (94.27%), Phi-4 Mini reaches 66.34%, and Ministral 3 3B reaches only 18.25%. Their disambiguated accuracies are much closer (87.71%, 93.67%, and 92.81%, respectively).

**Interpretation candidate:** a large part of the performance difference among these three models is uncertainty handling rather than the ability to follow explicit disambiguating evidence.

Evidence: Table 2; Figure 1.

## F02 — Ministral shows the clearest uncertainty-calibration failure

Ministral combines very low AMB accuracy (18.25%) with high DIS accuracy (92.81%). At category level, AMB accuracy falls to 12.99% for Age, 11.44% for Disability status, 17.01% for Physical appearance, and 11.19% for Race x gender.

Evidence: Table 2; Table 3; Figure 1; Figure 4.

## F03 — Physical appearance and Age are recurring ambiguous-bias hotspots

For the three local models, Physical appearance is the largest absolute category-level sAMB hotspot:
- Granite: +0.1282
- Phi-4 Mini: +0.4772
- Ministral: +0.4924

Age is also consistently elevated:
- Granite: +0.1141
- Phi-4 Mini: +0.3467
- Ministral: +0.4614

Qwen3 4B shows its largest sAMB in Age (+0.2677), followed by Disability status (+0.2468).

Evidence: Table 3; Figure 4.

## F04 — Near-zero bias score does not guarantee good ambiguous behavior

Ministral on Race x gender has AMB accuracy of only 11.19% but sAMB is approximately +0.0061. The near-zero directional score results from cancellation between stereotype-aligned and anti-target guesses while UNKNOWN recognition remains poor.

**Reporting implication:** always present AMB accuracy together with sAMB.

Evidence: category_results.csv; Figure 4.

## F05 — Overall directional bias is generally larger under ambiguity for the local/Qwen evaluations

Overall sAMB is +0.0201 for Granite, +0.1150 for Phi-4 Mini, +0.1422 for Ministral, and +0.0562 for Qwen3 4B. Their corresponding sDIS values are much smaller: +0.0120, +0.0233, +0.0183, and +0.0237.

**Interpretation candidate:** stereotype-aligned response tendencies are more visible when the benchmark withholds disambiguating evidence.

Evidence: Table 2; Figures 2–3.

## F06 — Qwen3 4B is comparatively balanced but has a small strict-format failure rate

Qwen3 4B reaches 90.07% overall accuracy, 88.01% AMB accuracy, and 92.14% DIS accuracy. It has 49 strict-format invalid outputs out of 58,492 attempts, giving 99.916% output coverage.

Its overall alignment gap is -2.22 percentage points, and category-level gaps are especially negative for Religion (-8.42 pp) and Age (-6.63 pp).

Evidence: Table 2; Table 3; Figure 6; QC notes.

## F07 — The GPT medium/light conditions show a different AMB–DIS pattern from the local models

GPT 5.5 medium reaches 93.18% AMB accuracy but only 50.75% DIS accuracy. GPT 5.6 Luna medium reaches 87.08% AMB and 33.07% DIS; GPT 5.6 Luna light reaches 79.66% AMB but only 10.17% DIS.

This is the reverse of the pattern seen in Phi-4 Mini and Ministral, where DIS accuracy is high while AMB accuracy is weaker.

Evidence: Table 2; Figure 1.

## F08 — GPT directional bias scores are near zero even when task accuracy is poor

Several GPT medium/light conditions show sAMB and sDIS close to zero despite low disambiguated accuracy. This reinforces that directional bias and QA accuracy capture different behaviors and should not be treated as substitutes.

Evidence: Table 2; Figures 2–3.

## F09 — The two GPT high conditions require explicit provenance caution

GPT 5.5-high and GPT 5.6-Luna-high contain the same 58,492-answer sequence and both match the gold answers on every benchmark row. Because the exact inference prompt/runtime that generated these answer sequences is not present in the supplied artifacts, the report should retain the results but avoid using them as evidence for a strong comparative model-performance claim.

Evidence: QC notes; data_quality documentation.

## F10 — Observed DIS alignment effects are model- and category-dependent

Overall nonaligned-minus-aligned DIS gaps are:
- Granite: -1.04 pp
- Phi-4 Mini: -1.98 pp
- Ministral: -1.62 pp
- Qwen3 4B: -2.22 pp

Category-level effects can be substantially larger (for example, Granite Physical appearance -8.71 pp, Qwen Religion -8.42 pp). These are observed effects only; no statistical-significance claim should be made without uncertainty estimates.

Evidence: Table 2; Table 3; Figure 6.
