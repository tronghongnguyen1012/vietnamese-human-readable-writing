"""Compute aggregate statistics from Held-Out A/B evaluation and Variance Check runs."""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

CONTEXT_ORDER = [
    "casual_chat",
    "concept_explanation",
    "problem_analysis",
    "workplace_communication",
    "business_docs",
    "technical_docs",
    "reports_guides_training",
    "editing_rewriting",
]

CRITERIA = [f"D{i}" for i in range(1, 10)]


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def mean(values: list[float]) -> float | None:
    if not values:
        return None
    return round(sum(values) / len(values), 3)


def compute_criteria_means(records: list[dict], side_key: str) -> dict[str, float | None]:
    buckets: dict[str, list[float]] = {d: [] for d in CRITERIA}
    for rec in records:
        p1_scores = rec["pass1"][side_key]["scores"]
        p2_scores = rec["pass2"][side_key]["scores"]
        for d in CRITERIA:
            vals = [v for v in (p1_scores.get(d), p2_scores.get(d)) if v is not None]
            if vals:
                buckets[d].append(sum(vals) / len(vals))
    return {d: mean(buckets[d]) for d in CRITERIA}


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    results_dir = repo_root / "evaluation" / "results"
    raw_path = results_dir / "held-out-raw-results.jsonl"
    var_path = results_dir / "held-out-variance-results.jsonl"
    out_path = results_dir / "summary-stats.json"

    records = load_jsonl(raw_path)
    variance_records = load_jsonl(var_path) if var_path.exists() else []

    verdict_counts = Counter(r["final_verdict"] for r in records)
    p1_counts = Counter(r["pass1"]["mapped_winner"] for r in records)
    p2_counts = Counter(r["pass2"]["mapped_winner"] for r in records)
    consistent_cases = sum(1 for r in records if r["position_consistent"])

    base_hf_cases = 0
    exp_hf_cases = 0
    base_hf_codes: Counter[str] = Counter()
    exp_hf_codes: Counter[str] = Counter()
    non_hf_records: list[dict] = []

    for r in records:
        b_hfs = set(r["pass1"]["baseline_eval"]["hard_fails"]) | set(r["pass2"]["baseline_eval"]["hard_fails"])
        e_hfs = set(r["pass1"]["experiment_eval"]["hard_fails"]) | set(r["pass2"]["experiment_eval"]["hard_fails"])
        if b_hfs:
            base_hf_cases += 1
            base_hf_codes.update(b_hfs)
        if e_hfs:
            exp_hf_cases += 1
            exp_hf_codes.update(e_hfs)
        if not b_hfs and not e_hfs:
            non_hf_records.append(r)

    base_means = compute_criteria_means(records, "baseline_eval")
    exp_means = compute_criteria_means(records, "experiment_eval")
    delta_means = {
        d: (round(exp_means[d] - base_means[d], 3) if exp_means[d] is not None and base_means[d] is not None else None)
        for d in CRITERIA
    }

    non_hf_verdicts = Counter(r["final_verdict"] for r in non_hf_records)
    non_hf_base_means = compute_criteria_means(non_hf_records, "baseline_eval")
    non_hf_exp_means = compute_criteria_means(non_hf_records, "experiment_eval")
    non_hf_delta_means = {
        d: (
            round(non_hf_exp_means[d] - non_hf_base_means[d], 3)
            if non_hf_exp_means[d] is not None and non_hf_base_means[d] is not None
            else None
        )
        for d in CRITERIA
    }

    by_context: dict[str, dict] = {}
    grouped = defaultdict(list)
    for r in records:
        grouped[r["context"]].append(r)

    for ctx in CONTEXT_ORDER:
        items = grouped[ctx]
        c_verdicts = Counter(x["final_verdict"] for x in items)
        b_words = [x["base_words"] for x in items]
        e_words = [x["exp_words"] for x in items]
        ratios = [x["exp_words"] / x["base_words"] for x in items if x["base_words"] > 0]
        refs_used_cases = sum(1 for x in items if x.get("refs_loaded"))
        ref_files = Counter(ref for x in items for ref in x.get("refs_loaded", []))
        ctx_b_hf = sum(
            1
            for x in items
            if (x["pass1"]["baseline_eval"]["hard_fails"] or x["pass2"]["baseline_eval"]["hard_fails"])
        )
        ctx_e_hf = sum(
            1
            for x in items
            if (x["pass1"]["experiment_eval"]["hard_fails"] or x["pass2"]["experiment_eval"]["hard_fails"])
        )
        by_context[ctx] = {
            "n": len(items),
            "verdicts": dict(c_verdicts),
            "baseline_hf_cases": ctx_b_hf,
            "experiment_hf_cases": ctx_e_hf,
            "avg_base_words": mean(b_words),
            "avg_exp_words": mean(e_words),
            "avg_word_ratio": mean(ratios),
            "refs_loaded_cases": refs_used_cases,
            "refs_loaded_rate": round(refs_used_cases / len(items), 3) if items else 0.0,
            "ref_files_used": dict(ref_files),
        }

    all_b_words = [r["base_words"] for r in records]
    all_e_words = [r["exp_words"] for r in records]
    all_ratios = [r["exp_words"] / r["base_words"] for r in records if r["base_words"] > 0]

    # Variance stats
    run1_map = {r["id"]: r for r in records}
    var_verdicts = Counter(v["mapped_winner"] for v in variance_records)
    var_consistent_vs_run1 = 0
    var_base_hf = 0
    var_exp_hf = 0
    var_b_words = []
    var_e_words = []
    var_details = []

    for v in variance_records:
        cid = v["id"]
        r1 = run1_map.get(cid)
        r1_verdict = r1["final_verdict"] if r1 else None
        r1_p1_verdict = r1["pass1"]["mapped_winner"] if r1 else None
        same_as_final = (v["mapped_winner"] == r1_verdict)
        if same_as_final:
            var_consistent_vs_run1 += 1
        b_hf = v["baseline_eval"]["hard_fails"]
        e_hf = v["experiment_eval"]["hard_fails"]
        if b_hf:
            var_base_hf += 1
        if e_hf:
            var_exp_hf += 1
        var_b_words.append(v["base_words"])
        var_e_words.append(v["exp_words"])
        var_details.append({
            "id": cid,
            "context": v["context"],
            "run1_final_verdict": r1_verdict,
            "run1_pass1_verdict": r1_p1_verdict,
            "run2_verdict": v["mapped_winner"],
            "same_as_run1_final": same_as_final,
            "run1_exp_words": r1["exp_words"] if r1 else None,
            "run2_exp_words": v["exp_words"],
            "run2_refs_loaded": v.get("refs_loaded", []),
            "run2_base_hf": b_hf,
            "run2_exp_hf": e_hf,
        })

    summary = {
        "held_out_total": len(records),
        "overall": {
            "final_verdicts": dict(verdict_counts),
            "experiment_win_rate": round(verdict_counts.get("experiment", 0) / len(records), 4) if records else 0.0,
            "pass1_verdicts": dict(p1_counts),
            "pass2_verdicts": dict(p2_counts),
            "position_consistent_cases": consistent_cases,
            "position_consistency_rate": round(consistent_cases / len(records), 4) if records else 0.0,
            "avg_base_words": mean(all_b_words),
            "avg_exp_words": mean(all_e_words),
            "avg_word_ratio": mean(all_ratios),
        },
        "hard_fails": {
            "baseline_hf_cases": base_hf_cases,
            "experiment_hf_cases": exp_hf_cases,
            "baseline_hf_codes": dict(base_hf_codes),
            "experiment_hf_codes": dict(exp_hf_codes),
        },
        "criteria_means_all": {
            "baseline": base_means,
            "experiment": exp_means,
            "delta": delta_means,
        },
        "non_hf_subgroup": {
            "n": len(non_hf_records),
            "verdicts": dict(non_hf_verdicts),
            "baseline": non_hf_base_means,
            "experiment": non_hf_exp_means,
            "delta": non_hf_delta_means,
        },
        "by_context": by_context,
        "variance_check": {
            "n": len(variance_records),
            "run2_verdicts": dict(var_verdicts),
            "same_as_run1_final_count": var_consistent_vs_run1,
            "consistency_rate": round(var_consistent_vs_run1 / len(variance_records), 4) if variance_records else 0.0,
            "run2_baseline_hf_cases": var_base_hf,
            "run2_experiment_hf_cases": var_exp_hf,
            "avg_run2_base_words": mean(var_b_words),
            "avg_run2_exp_words": mean(var_e_words),
            "details": var_details,
        },
    }

    out_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
