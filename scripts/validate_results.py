#!/usr/bin/env python3
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    with path.open('r', encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def fail(msg):
    raise SystemExit('VALIDATION FAIL: ' + msg)

bench = read(ROOT / 'metadata' / 'benchmark_index.csv')
if len(bench) != 58492:
    fail(f'benchmark rows={len(bench)}')
keys = {(r['category'], r['example_id'], r['question_index']) for r in bench}
if len(keys) != 58492:
    fail('benchmark composite keys are not unique')

overall = read(ROOT / 'results' / 'overall_results.csv')
category = read(ROOT / 'results' / 'category_results.csv')
detail = read(ROOT / 'results' / 'detailed_results.csv')
if len(overall) != 10: fail(f'overall rows={len(overall)}')
if len(category) != 130: fail(f'category rows={len(category)}')
if len(detail) != 520: fail(f'detailed rows={len(detail)}')

for r in overall:
    if int(r['attempted_n']) != 58492:
        fail(f"{r['evaluation_id']}: attempted_n != 58492")
    cov = float(r['coverage_pct'])
    if not 0 <= cov <= 100:
        fail(f"{r['evaluation_id']}: invalid coverage")
    for k in ('sAMB','sDIS'):
        x = float(r[k])
        if not -1 <= x <= 1:
            fail(f"{r['evaluation_id']}: {k} out of range")

qwen = read(ROOT / 'source_outputs' / 'qwen3_4b.csv')
if len(qwen) != 58492:
    fail(f'Qwen rows={len(qwen)}')
invalid = sum(r['parse_status'] != 'VALID_EXACT' for r in qwen)
if invalid != 49:
    fail(f'Qwen invalid strict-format rows={invalid}, expected 49')

for mid in ('gpt_5_5','gpt_5_6_luna'):
    rows = read(ROOT / 'source_outputs' / f'{mid}.csv')
    if len(rows) != 58492 * 3:
        fail(f'{mid}: rows={len(rows)}')
    for cond in ('high','medium','light'):
        sub = [r for r in rows if r['condition_id'] == cond]
        if len(sub) != 58492:
            fail(f'{mid}/{cond}: rows={len(sub)}')
        if any(r['answer'] not in ('A','B','C') for r in sub):
            fail(f'{mid}/{cond}: invalid answer')

g55 = [r['answer'] for r in read(ROOT / 'source_outputs' / 'gpt_5_5.csv') if r['condition_id'] == 'high']
g56 = [r['answer'] for r in read(ROOT / 'source_outputs' / 'gpt_5_6_luna.csv') if r['condition_id'] == 'high']

print('VALIDATION PASS')
print('benchmark rows: 58,492')
print('evaluation conditions: 10')
print('category rows: 130')
print('detailed rows: 520')
print('Qwen invalid strict-format outputs: 49')
print('GPT high sequences identical:', g55 == g56)
