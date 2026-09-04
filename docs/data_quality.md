# Data quality status

## Ready
- Granite 4.1 3B — VERIFIED_FULL
- Phi-4 Mini 3.8B — VERIFIED_FULL
- Ministral 3 3B — VERIFIED_FULL

Each covers 58,492 / 58,492 questions with 0 invalid outputs.

## GPT
Status: REPORTED_AGGREGATE

What is already usable:
- full per-condition row counts
- valid/output coverage
- reported overall/category accuracies
- reported category-level sAMB / sDIS

What is not independently verified:
- exact prompt/protocol
- parser / invalid handling
- raw predictions
- exact canonical overall sAMB / sDIS reconstruction
- medium/low condition label text due source encoding corruption

## Qwen
Status: PENDING_REPAIR

Not promoted into report-ready results yet.
