#!/usr/bin/env python3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    with path.open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f))

def main():
    overall=read(ROOT/"results/overall_results.csv")
    if len(overall) != 9:
        raise SystemExit(f"FAIL: expected 9 current evaluation conditions (3 verified local + 6 GPT reported), got {len(overall)}")

    ids=set()
    for r in overall:
        eid=r["evaluation_id"]
        if eid in ids:
            raise SystemExit(f"FAIL duplicate evaluation_id: {eid}")
        ids.add(eid)

        attempted=int(float(r["attempted_n"]))
        valid=int(float(r["valid_n"]))
        if attempted != 58492:
            raise SystemExit(f"FAIL {eid}: attempted_n={attempted}")
        if valid != 58492:
            raise SystemExit(f"FAIL {eid}: valid_n={valid}")

        for field in ("sAMB","sDIS"):
            value=r[field].strip()
            if value:
                x=float(value)
                if not -1 <= x <= 1:
                    raise SystemExit(f"FAIL {eid}: {field} out of range")

    verified=[r for r in overall if r["verification_status"]=="VERIFIED_FULL"]
    reported=[r for r in overall if r["verification_status"]=="REPORTED_AGGREGATE"]
    if len(verified)!=3:
        raise SystemExit(f"FAIL expected 3 VERIFIED_FULL, got {len(verified)}")
    if len(reported)!=6:
        raise SystemExit(f"FAIL expected 6 REPORTED_AGGREGATE, got {len(reported)}")

    cats=read(ROOT/"results/category_results.csv")
    detailed=read(ROOT/"results/detailed_results.csv")
    if len(cats)!=39:
        raise SystemExit(f"FAIL verified category rows expected 39, got {len(cats)}")
    if len(detailed)!=156:
        raise SystemExit(f"FAIL verified detailed rows expected 156, got {len(detailed)}")

    print("VALIDATION PASS")
    print("Overall conditions:",len(overall))
    print("  VERIFIED_FULL:",len(verified))
    print("  REPORTED_AGGREGATE:",len(reported))
    print("Verified category rows:",len(cats))
    print("Verified detailed rows:",len(detailed))
    print("Qwen is pending and intentionally absent from headline results.")

if __name__=="__main__":
    main()
