# BBQ benchmark source

This repository evaluates models on **BBQ: A Hand-Built Bias Benchmark for Question Answering**.

- Upstream repository: https://github.com/nyu-mll/BBQ
- Locked commit: `bea11bd97d79217245b5871acd247b9d6eb24598`
- Official benchmark size: **58,492 examples**

The complete benchmark text is not copied into this repository. Use:

```bash
python scripts/fetch_bbq.py
```

to clone the upstream repository and check out the locked commit under `benchmark/BBQ-upstream/`.

`metadata/benchmark_index.csv` is a compact alignment/scoring index only. It contains identifiers, category/context/polarity information, gold label, UNKNOWN location, `target_loc`, and `label_type`; it does not duplicate full question/context text.
