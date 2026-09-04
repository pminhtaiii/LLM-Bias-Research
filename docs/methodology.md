# Methodology status

## Benchmark
BBQ, locked to the upstream commit in `metadata/benchmark_lock.json`.

## Verified local evaluations
Granite 4.1 3B, Phi-4 Mini 3.8B, and Ministral 3 3B:
- full 58,492-question BBQ
- 100% output coverage
- 0 invalid outputs
- common local prompt and deterministic decoding profile recorded in `metadata/models.csv`

## GPT aggregate evaluations
The supplied source contains:
- GPT 5.5: three reasoning conditions
- GPT 5.6 LunaWork: three reasoning conditions
- each condition totals 58,492 questions with 58,492 valid answers

The exact prompt, inference settings, parser/scorer, and raw predictions were not supplied. Therefore these are preserved as `REPORTED_AGGREGATE`, not presented as independently verified predictions.

Medium/low condition labels were inferred from mojibake in the supplied CSV and must be confirmed before final publication.

## Qwen
Held in pending until raw predictions are available for repaired rescoring.
