#!/usr/bin/env python3
"""Rebuild all canonical result tables from the committed source outputs.

No third-party Python packages are required.
"""
from pathlib import Path
from scoring import (
    read_csv, write_csv, fnum, inum, r6,
    load_benchmark_index, enrich_prediction, score_slice, score_overall,
)

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'results'
SOURCE = ROOT / 'source_outputs'

benchmark = load_benchmark_index(ROOT / 'metadata' / 'benchmark_index.csv')
bench_by_number = {r['number']: r for r in benchmark}

registry = {
    'granite_4_1_3b__native': ('granite_4_1_3b','Granite 4.1 3B','native','summary_export','VERIFIED_SUMMARY','KNOWN'),
    'phi4_mini_3_8b__native': ('phi4_mini_3_8b','Phi-4 Mini 3.8B','native','summary_export','VERIFIED_SUMMARY','KNOWN'),
    'ministral_3_3b__native': ('ministral_3_3b','Ministral 3 3B','native','summary_export','VERIFIED_SUMMARY','KNOWN'),
    'qwen3_4b__no_think_q6_k': ('qwen3_4b','Qwen3 4B Instruct','no_think_q6_k','raw_predictions','RESCORED','KNOWN'),
    'gpt_5_5__high': ('gpt_5_5','GPT 5.5','high','raw_answers','RESCORED','PARTIAL'),
    'gpt_5_5__medium': ('gpt_5_5','GPT 5.5','medium','raw_answers','RESCORED','PARTIAL'),
    'gpt_5_5__light': ('gpt_5_5','GPT 5.5','light','raw_answers','RESCORED','PARTIAL'),
    'gpt_5_6_luna__high': ('gpt_5_6_luna','GPT 5.6 Luna','high','raw_answers','RESCORED','PARTIAL'),
    'gpt_5_6_luna__medium': ('gpt_5_6_luna','GPT 5.6 Luna','medium','raw_answers','RESCORED','PARTIAL'),
    'gpt_5_6_luna__light': ('gpt_5_6_luna','GPT 5.6 Luna','light','raw_answers','RESCORED','PARTIAL'),
}

OVERALL_FIELDS = [
    'evaluation_id','model_id','model_name','condition_id','source_type','scoring_status','inference_provenance',
    'attempted_n','valid_n','invalid_n','coverage_pct','overall_accuracy_pct','ambig_accuracy_pct','disambig_accuracy_pct',
    'sAMB','sDIS','aligned_dis_accuracy_pct','nonaligned_dis_accuracy_pct','alignment_gap_pp'
]
CATEGORY_FIELDS = [
    'evaluation_id','model_id','model_name','condition_id','source_type','scoring_status','inference_provenance',
    'category','n','valid_n','invalid_n','coverage_pct','overall_accuracy_pct','ambig_accuracy_pct','disambig_accuracy_pct',
    'sAMB','sDIS','aligned_dis_accuracy_pct','nonaligned_dis_accuracy_pct','alignment_gap_pp'
]
DETAIL_FIELDS = [
    'evaluation_id','model_id','model_name','condition_id','source_type','scoring_status','inference_provenance',
    'category','context','polarity','n','valid_n','invalid_n','coverage_pct','accuracy_pct',
    'unknown_rate_valid_pct','bias_scorable_valid_n','bias_type','bias_score','aligned_dis_accuracy_pct',
    'nonaligned_dis_accuracy_pct','alignment_gap_pp','n_biased','n_anti','n_unknown'
]
BY_MODEL_FIELDS = [
    'result_level','evaluation_id','model_id','model_name','condition_id','source_type','scoring_status','inference_provenance',
    'category','context','polarity','n','valid_n','invalid_n','coverage_pct','overall_accuracy_pct',
    'ambig_accuracy_pct','disambig_accuracy_pct','accuracy_pct','unknown_rate_valid_pct',
    'sAMB','sDIS','bias_type','bias_score','aligned_dis_accuracy_pct','nonaligned_dis_accuracy_pct','alignment_gap_pp',
    'n_biased','n_anti','n_unknown','bias_scorable_valid_n'
]

raw_eval = {}
qwen = read_csv(SOURCE / 'qwen3_4b.csv')
raw_eval['qwen3_4b__no_think_q6_k'] = [
    enrich_prediction(bench_by_number[int(r['number'])], inum(r['prediction'])) for r in qwen
]

answer_map = {'A':0,'B':1,'C':2}
for mid in ('gpt_5_5','gpt_5_6_luna'):
    source = read_csv(SOURCE / f'{mid}.csv')
    for cond in ('high','medium','light'):
        rows = []
        for r in source:
            if r['condition_id'] != cond:
                continue
            pred = answer_map.get(r['answer'].strip().upper())
            rows.append(enrich_prediction(bench_by_number[int(r['number'])], pred))
        raw_eval[f'{mid}__{cond}'] = rows

overall, category, detail = [], [], []

# Import the three verified local summary exports.
for cid, meta in registry.items():
    mid,mname,cond,stype,sstatus,iprov = meta
    if stype != 'summary_export':
        continue
    src = read_csv(SOURCE / f'{mid}.csv')
    ov = next(r for r in src if r['Result Level'] == 'OVERALL')
    overall.append({
        'evaluation_id':cid,'model_id':mid,'model_name':mname,'condition_id':cond,
        'source_type':stype,'scoring_status':sstatus,'inference_provenance':iprov,
        'attempted_n':inum(ov['N']),'valid_n':inum(ov['Valid']),'invalid_n':inum(ov['Invalid']),
        'coverage_pct':fnum(ov['Coverage (%)']),'overall_accuracy_pct':fnum(ov['Overall Accuracy (%)']),
        'ambig_accuracy_pct':fnum(ov['AMB Accuracy / UNKNOWN (%)']),'disambig_accuracy_pct':fnum(ov['DIS Accuracy (%)']),
        'sAMB':fnum(ov['sAMB [-1,1]']),'sDIS':fnum(ov['sDIS [-1,1]']),
        'aligned_dis_accuracy_pct':fnum(ov['Aligned DIS Accuracy (%)']),
        'nonaligned_dis_accuracy_pct':fnum(ov['Nonaligned DIS Accuracy (%)']),
        'alignment_gap_pp':fnum(ov['Nonaligned - Aligned (pp)']),
    })
    for r in src:
        if r['Result Level'] == 'CATEGORY':
            category.append({
                'evaluation_id':cid,'model_id':mid,'model_name':mname,'condition_id':cond,
                'source_type':stype,'scoring_status':sstatus,'inference_provenance':iprov,
                'category':r['Analysis Category'],'n':inum(r['N']),'valid_n':inum(r['Valid']),'invalid_n':inum(r['Invalid']),
                'coverage_pct':fnum(r['Coverage (%)']),'overall_accuracy_pct':fnum(r['Overall Accuracy (%)']),
                'ambig_accuracy_pct':fnum(r['AMB Accuracy / UNKNOWN (%)']),'disambig_accuracy_pct':fnum(r['DIS Accuracy (%)']),
                'sAMB':fnum(r['sAMB [-1,1]']),'sDIS':fnum(r['sDIS [-1,1]']),
                'aligned_dis_accuracy_pct':fnum(r['Aligned DIS Accuracy (%)']),
                'nonaligned_dis_accuracy_pct':fnum(r['Nonaligned DIS Accuracy (%)']),
                'alignment_gap_pp':fnum(r['Nonaligned - Aligned (pp)']),
            })
        elif r['Result Level'] == 'CATEGORY_CONTEXT_POLARITY':
            ctx = r['Context']
            detail.append({
                'evaluation_id':cid,'model_id':mid,'model_name':mname,'condition_id':cond,
                'source_type':stype,'scoring_status':sstatus,'inference_provenance':iprov,
                'category':r['Analysis Category'],'context':ctx,'polarity':r['Question Polarity'],
                'n':inum(r['N']),'valid_n':inum(r['Valid']),'invalid_n':inum(r['Invalid']),
                'coverage_pct':fnum(r['Coverage (%)']),'accuracy_pct':fnum(r['Overall Accuracy (%)']),
                'unknown_rate_valid_pct':fnum(r['UNKNOWN Response Rate Valid (%)']),'bias_scorable_valid_n':inum(r['Scorable N']),
                'bias_type':'sAMB' if ctx == 'ambig' else 'sDIS',
                'bias_score':fnum(r['sAMB [-1,1]'] if ctx == 'ambig' else r['sDIS [-1,1]']),
                'aligned_dis_accuracy_pct':None if ctx == 'ambig' else fnum(r['Aligned DIS Accuracy (%)']),
                'nonaligned_dis_accuracy_pct':None if ctx == 'ambig' else fnum(r['Nonaligned DIS Accuracy (%)']),
                'alignment_gap_pp':None if ctx == 'ambig' else fnum(r['Nonaligned - Aligned (pp)']),
                'n_biased':inum(r['n_biased']),'n_anti':inum(r['n_anti']),'n_unknown':inum(r['n_unknown']),
            })

# Rescore Qwen/GPT from the full per-example/answer files.
for cid, rows in raw_eval.items():
    mid,mname,cond,stype,sstatus,iprov = registry[cid]
    om = score_overall(rows)
    overall.append({
        'evaluation_id':cid,'model_id':mid,'model_name':mname,'condition_id':cond,
        'source_type':stype,'scoring_status':sstatus,'inference_provenance':iprov,
        'attempted_n':om['n'],'valid_n':om['valid_n'],'invalid_n':om['invalid_n'],'coverage_pct':r6(om['coverage_pct']),
        'overall_accuracy_pct':r6(om['accuracy_pct']),'ambig_accuracy_pct':r6(om['ambig_accuracy_pct']),
        'disambig_accuracy_pct':r6(om['disambig_accuracy_pct']),'sAMB':r6(om['sAMB']),'sDIS':r6(om['sDIS']),
        'aligned_dis_accuracy_pct':r6(om['aligned_dis_accuracy_pct']),
        'nonaligned_dis_accuracy_pct':r6(om['nonaligned_dis_accuracy_pct']),
        'alignment_gap_pp':r6(om['alignment_gap_pp']),
    })
    for cat in sorted({r['analysis_category'] for r in rows}):
        cr = [r for r in rows if r['analysis_category'] == cat]
        cm = score_overall(cr)
        category.append({
            'evaluation_id':cid,'model_id':mid,'model_name':mname,'condition_id':cond,
            'source_type':stype,'scoring_status':sstatus,'inference_provenance':iprov,
            'category':cat,'n':cm['n'],'valid_n':cm['valid_n'],'invalid_n':cm['invalid_n'],'coverage_pct':r6(cm['coverage_pct']),
            'overall_accuracy_pct':r6(cm['accuracy_pct']),'ambig_accuracy_pct':r6(cm['ambig_accuracy_pct']),
            'disambig_accuracy_pct':r6(cm['disambig_accuracy_pct']),'sAMB':r6(cm['sAMB']),'sDIS':r6(cm['sDIS']),
            'aligned_dis_accuracy_pct':r6(cm['aligned_dis_accuracy_pct']),
            'nonaligned_dis_accuracy_pct':r6(cm['nonaligned_dis_accuracy_pct']),
            'alignment_gap_pp':r6(cm['alignment_gap_pp']),
        })
        for ctx in ('ambig','disambig'):
            for pol in ('neg','nonneg'):
                dr = [r for r in cr if r['context_condition'] == ctx and r['question_polarity'] == pol]
                dm = score_slice(dr)
                detail.append({
                    'evaluation_id':cid,'model_id':mid,'model_name':mname,'condition_id':cond,
                    'source_type':stype,'scoring_status':sstatus,'inference_provenance':iprov,
                    'category':cat,'context':ctx,'polarity':pol,
                    'n':dm['n'],'valid_n':dm['valid_n'],'invalid_n':dm['invalid_n'],'coverage_pct':r6(dm['coverage_pct']),
                    'accuracy_pct':r6(dm['accuracy_pct']),'unknown_rate_valid_pct':r6(dm['unknown_rate_valid_pct']),
                    'bias_scorable_valid_n':dm['bias_scorable_valid_n'],'bias_type':dm['bias_type'],'bias_score':r6(dm['bias_score']),
                    'aligned_dis_accuracy_pct':r6(dm['aligned_dis_accuracy_pct']),
                    'nonaligned_dis_accuracy_pct':r6(dm['nonaligned_dis_accuracy_pct']),
                    'alignment_gap_pp':r6(dm['alignment_gap_pp']),
                    'n_biased':dm['n_biased'],'n_anti':dm['n_anti'],'n_unknown':dm['n_unknown'],
                })

model_order = {'granite_4_1_3b':0,'phi4_mini_3_8b':1,'ministral_3_3b':2,'qwen3_4b':3,'gpt_5_5':4,'gpt_5_6_luna':5}
cond_order = {'native':0,'no_think_q6_k':0,'high':0,'medium':1,'light':2}
overall.sort(key=lambda r:(model_order[r['model_id']], cond_order.get(r['condition_id'],9)))
category.sort(key=lambda r:(model_order[r['model_id']], cond_order.get(r['condition_id'],9), r['category']))
detail.sort(key=lambda r:(model_order[r['model_id']], cond_order.get(r['condition_id'],9), r['category'], r['context'], r['polarity']))

write_csv(RESULTS / 'overall_results.csv', OVERALL_FIELDS, overall)
write_csv(RESULTS / 'category_results.csv', CATEGORY_FIELDS, category)
write_csv(RESULTS / 'detailed_results.csv', DETAIL_FIELDS, detail)

# Model-centric convenience views.
for mid in model_order:
    rows = []
    for r in overall:
        if r['model_id'] == mid:
            rows.append({'result_level':'OVERALL', **r, 'category':'ALL','context':'ALL','polarity':'ALL',
                         'n':r['attempted_n'],'accuracy_pct':r['overall_accuracy_pct']})
    for r in category:
        if r['model_id'] == mid:
            rows.append({'result_level':'CATEGORY', **r, 'context':'ALL','polarity':'ALL',
                         'accuracy_pct':r['overall_accuracy_pct']})
    for r in detail:
        if r['model_id'] == mid:
            rows.append({'result_level':'CATEGORY_CONTEXT_POLARITY', **r})
    write_csv(RESULTS / 'by_model' / f'{mid}.csv', BY_MODEL_FIELDS, rows)

print('BUILD PASS')
print('overall rows:', len(overall))
print('category rows:', len(category))
print('detailed rows:', len(detail))
