"""Compute comprehensive Round 2 metrics and save evaluation/results-v2/summary-stats-v2.json."""

from __future__ import annotations

import argparse
import json
import os
import statistics
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
SKILL_DIR = ROOT / "skills" / "vietnamese-human-readable-writing"
EVAL_DIR = ROOT / "evaluation"
RES_V1_DIR = EVAL_DIR / "results"
RES_V2_DIR = EVAL_DIR / "results-v2"

DIMS = [f"D{i}" for i in range(1, 10)]

ARM_A_PROMPT = (
    "Bạn là trợ lý AI hữu ích trả lời bằng tiếng Việt. Hãy thực hiện trực tiếp và đầy đủ "
    "yêu cầu của người dùng. Trả về chỉ nội dung câu trả lời cuối cùng dành cho người dùng, "
    "không kèm lời bình luận về quy trình của bạn."
)
ARM_B_PROMPT = (
    "Bạn là trợ lý AI hữu ích trả lời bằng tiếng Việt. Khi thực hiện yêu cầu của người dùng, "
    "hãy tuân thủ đầy đủ các nguyên tắc sau: Viết tiếng Việt rõ nghĩa và tự nhiên; Phù hợp đối "
    "tượng người đọc và ngữ cảnh; Không tự bịa thông tin chưa có căn cứ; Giữ đầy đủ dữ kiện và "
    "logic nghiệp vụ; Tránh nội dung dư thừa; Không làm mất chiều sâu chuyên môn. Trả về chỉ "
    "nội dung câu trả lời cuối cùng dành cho người dùng, không kèm lời bình luận về quy trình của bạn."
)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    """Read non-empty JSON lines from path."""
    with path.open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def file_stats(path: Path) -> dict[str, Any]:
    """Compute byte, char, word, line counts and heuristic token estimates for a text file."""
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    words = len(text.split())
    b = len(raw)
    return {
        "path": str(path.relative_to(ROOT)).replace("\\", "/"),
        "bytes": b,
        "chars": len(text),
        "words": words,
        "lines": len(text.splitlines()),
        "est_tokens_bytes_div_3_8": round(b / 3.8, 1),
        "est_tokens_chars_div_3_5": round(len(text) / 3.5, 1),
    }


def summarize_numeric(vals: list[float]) -> dict[str, Any]:
    """Summarize numeric distribution."""
    if not vals:
        return {"n": 0}
    s = sorted(vals)
    p95_idx = min(len(s) - 1, int(round(0.95 * (len(s) - 1))))
    return {
        "n": len(s),
        "mean": round(statistics.mean(s), 3),
        "median": round(statistics.median(s), 3),
        "min": round(s[0], 3),
        "max": round(s[-1], 3),
        "p95": round(s[p95_idx], 3),
        "sum": round(sum(s), 3),
    }


def analyze_v1_historical() -> dict[str, Any]:
    """Audit historical Rubric v1 numbers to document Round 2 errata transparently."""
    rows = load_jsonl(RES_V1_DIR / "held-out-raw-results.jsonl")
    verdicts = Counter(r["final_verdict"] for r in rows)
    raw_ab = Counter()
    mapped_p1_p2 = Counter()
    base_hf = []
    exp_hf = []
    base_words = []
    exp_words = []
    ratios = []
    anom = []

    for r in rows:
        for pkey in ("pass1", "pass2"):
            p = r[pkey]
            raw_ab[p["raw_winner"]] += 1
            mapped_p1_p2[p["mapped_winner"]] += 1
        bhf = sorted(set(r["pass1"]["baseline_eval"]["hard_fails"]) | set(r["pass2"]["baseline_eval"]["hard_fails"]))
        ehf = sorted(set(r["pass1"]["experiment_eval"]["hard_fails"]) | set(r["pass2"]["experiment_eval"]["hard_fails"]))
        if bhf:
            base_hf.append({"id": r["id"], "hf": bhf})
        if ehf:
            exp_hf.append({"id": r["id"], "hf": ehf})
        bw = r["base_words"]
        ew = r["exp_words"]
        base_words.append(bw)
        exp_words.append(ew)
        ratios.append(ew / bw)
        if r["final_verdict"] != "experiment":
            anom.append({
                "id": r["id"],
                "final_verdict": r["final_verdict"],
                "p1_raw": r["pass1"]["raw_winner"],
                "p1_mapped": r["pass1"]["mapped_winner"],
                "p2_raw": r["pass2"]["raw_winner"],
                "p2_mapped": r["pass2"]["mapped_winner"],
            })

    return {
        "n": len(rows),
        "verdicts": dict(verdicts),
        "raw_48_passes_AB": dict(raw_ab),
        "raw_48_passes_mapped": dict(mapped_p1_p2),
        "baseline_hf_cases": len(base_hf),
        "experiment_hf_cases": len(exp_hf),
        "mean_baseline_words": round(statistics.mean(base_words), 2),
        "mean_experiment_words": round(statistics.mean(exp_words), 2),
        "mean_of_pairwise_exp_over_base_ratio": round(statistics.mean(ratios), 4),
        "ratio_of_means_exp_over_base": round(sum(exp_words) / sum(base_words), 4),
        "non_exp_win_cases": anom,
    }


def analyze_judge_calibration() -> dict[str, Any]:
    """Summarize Judge v2 calibration on planted defect cases."""
    rows = load_jsonl(RES_V2_DIR / "judge-calibration-results.jsonl")
    cases = []
    for r in rows:
        cases.append({
            "id": r["id"],
            "title": r["title"],
            "expected_good_hf": r["expected_good_hf"],
            "expected_flawed_hf": r["expected_flawed_hf"],
            "observed_good_hf": r["observed_good_hf"],
            "observed_flawed_hf": r["observed_flawed_hf"],
            "pass1_winner": r["pass1_winner"],
            "pass2_winner": r["pass2_winner"],
            "hf_match": r["hf_match"],
            "win_match": r["win_match"],
            "calibration_pass": r["calibration_pass"],
        })
    return {
        "n": len(rows),
        "win_match_count": sum(1 for r in rows if r["win_match"]),
        "hf_match_count": sum(1 for r in rows if r["hf_match"]),
        "calibration_pass_count": sum(1 for r in rows if r["calibration_pass"]),
        "cases": cases,
    }


def _extract_side_stats(
    rows: list[dict[str, Any]],
    left_key: str,
    right_key: str,
    left_eval_key: str,
    right_eval_key: str,
    left_hf_key: str,
    right_hf_key: str,
) -> dict[str, Any]:
    """Analyze a dual-pass blind A/B judge JSONL file uniformly."""
    verdicts = Counter(r["final_verdict"] for r in rows)
    consistent_n = sum(1 for r in rows if r["position_consistent"])
    raw_ab = Counter()
    mapped_48 = Counter()

    dim_scores: dict[str, dict[str, list[int]]] = {
        left_key: defaultdict(list),
        right_key: defaultdict(list),
    }
    hf_counts = {left_key: Counter(), right_key: Counter()}
    err_counts = {
        left_key: {"Minor": Counter(), "Major": Counter(), "Critical": Counter()},
        right_key: {"Minor": Counter(), "Major": Counter(), "Critical": Counter()},
    }
    hf_cases = {left_key: [], right_key: []}
    non_hf_verdicts = Counter()
    by_context: dict[str, Counter] = defaultdict(Counter)
    by_sim_flag: dict[str, Counter] = defaultdict(Counter)
    non_right_wins = []

    for r in rows:
        by_context[r["context"]][r["final_verdict"]] += 1
        if "simulated_real_world" in r:
            flag_key = "simulated_real_world" if r["simulated_real_world"] else "standard_unseen"
            by_sim_flag[flag_key][r["final_verdict"]] += 1

        l_hf = r[left_hf_key]
        r_hf = r[right_hf_key]
        if l_hf:
            hf_cases[left_key].append({"id": r["id"], "context": r["context"], "hf": l_hf})
        if r_hf:
            hf_cases[right_key].append({"id": r["id"], "context": r["context"], "hf": r_hf})
        if not l_hf and not r_hf:
            non_hf_verdicts[r["final_verdict"]] += 1

        for c in l_hf:
            hf_counts[left_key][c] += 1
        for c in r_hf:
            hf_counts[right_key][c] += 1

        for pkey in ("pass1", "pass2"):
            p = r[pkey]
            raw_ab[p["raw_winner"]] += 1
            mapped_48[p["mapped_winner"]] += 1

            for arm_name, ev in ((left_key, p[left_eval_key]), (right_key, p[right_eval_key])):
                for d in DIMS:
                    val = ev["scores"].get(d)
                    if val is not None:
                        dim_scores[arm_name][d].append(val)
                for err in ev.get("errors", []):
                    sev = err.get("severity", "Minor")
                    code = err.get("code", "UNKNOWN")
                    if sev in err_counts[arm_name]:
                        err_counts[arm_name][sev][code] += 1

        if r["final_verdict"] != right_key:
            non_right_wins.append({
                "id": r["id"],
                "context": r["context"],
                "title": r.get("title", ""),
                "final_verdict": r["final_verdict"],
                "p1_mapped": r["pass1"]["mapped_winner"],
                "p2_mapped": r["pass2"]["mapped_winner"],
                left_hf_key: l_hf,
                right_hf_key: r_hf,
                "p1_rationale": r["pass1"]["rationale"][:350],
                "p2_rationale": r["pass2"]["rationale"][:350],
            })

    mean_dims = {
        arm: {
            d: round(statistics.mean(dim_scores[arm][d]), 3) if dim_scores[arm][d] else None
            for d in DIMS
        }
        for arm in (left_key, right_key)
    }
    return {
        "n": len(rows),
        "arms": [left_key, right_key],
        "final_verdicts": dict(verdicts),
        "position_consistent_count": consistent_n,
        "position_consistency_rate": round(consistent_n / len(rows), 4) if rows else 0.0,
        "raw_passes_AB": dict(raw_ab),
        "raw_passes_mapped": dict(mapped_48),
        "hf_case_counts": {left_key: len(hf_cases[left_key]), right_key: len(hf_cases[right_key])},
        "hf_cases": hf_cases,
        "hf_code_counts": {k: dict(v) for k, v in hf_counts.items()},
        "non_hf_subgroup": {
            "n": sum(non_hf_verdicts.values()),
            "verdicts": dict(non_hf_verdicts),
        },
        "mean_scores": mean_dims,
        "error_severity_totals": {
            arm: {sev: sum(cnt.values()) for sev, cnt in sevs.items()}
            for arm, sevs in err_counts.items()
        },
        "error_code_counts": {
            arm: {sev: dict(cnt) for sev, cnt in sevs.items() if cnt}
            for arm, sevs in err_counts.items()
        },
        "by_context": {ctx: dict(cnt) for ctx, cnt in by_context.items()},
        "by_simulated_flag": {k: dict(v) for k, v in by_sim_flag.items()} if by_sim_flag else {},
        "non_winner_or_tie_cases": non_right_wins,
    }


def analyze_v3_reaudit() -> dict[str, Any]:
    """Analyze Rubric v2 re-audit on historical 24 v3 pairs and migration from Rubric v1."""
    rows = load_jsonl(RES_V2_DIR / "v3-reaudit-rubric-v2.jsonl")
    stats = _extract_side_stats(
        rows,
        left_key="baseline",
        right_key="v3",
        left_eval_key="baseline_eval",
        right_eval_key="v3_eval",
        left_hf_key="baseline_hf_union",
        right_hf_key="v3_hf_union",
    )
    migration = Counter(f"{r['v1_final_verdict']} -> {r['final_verdict']}" for r in rows)
    changed_cases = [
        {
            "id": r["id"],
            "context": r["context"],
            "v1_verdict": r["v1_final_verdict"],
            "v2_verdict": r["final_verdict"],
            "baseline_hf_v2": r["baseline_hf_union"],
            "v3_hf_v2": r["v3_hf_union"],
        }
        for r in rows
        if r["v1_final_verdict"] != ("experiment" if r["final_verdict"] == "v3" else r["final_verdict"])
    ]
    stats["v1_to_v2_migration"] = dict(migration)
    stats["changed_or_hf_audited_cases"] = changed_cases
    return stats


def analyze_trigger_eval() -> dict[str, Any]:
    """Compute trigger Precision, Recall, F1, and list misclassifications."""
    rows = load_jsonl(RES_V2_DIR / "trigger-eval-results.jsonl")
    tp = sum(1 for r in rows if r["expected_trigger"] and r["observed_trigger"])
    tn = sum(1 for r in rows if not r["expected_trigger"] and not r["observed_trigger"])
    fp = sum(1 for r in rows if not r["expected_trigger"] and r["observed_trigger"])
    fn = sum(1 for r in rows if r["expected_trigger"] and not r["observed_trigger"])
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) else 0.0
    by_cat: dict[str, dict[str, int]] = defaultdict(lambda: {"total": 0, "correct": 0})
    errors = []
    for r in rows:
        by_cat[r["category"]]["total"] += 1
        if r["correct"]:
            by_cat[r["category"]]["correct"] += 1
        else:
            errors.append(r)
    return {
        "n": len(rows),
        "tp": tp,
        "tn": tn,
        "fp": fp,
        "fn": fn,
        "accuracy": round((tp + tn) / len(rows), 4) if rows else 0.0,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "by_category": dict(by_cat),
        "misclassified": errors,
    }


def analyze_overhead() -> dict[str, Any]:
    """Compute file sizes, prompt byte/token overhead, reference loading stats, verbosity, and latency."""
    skill_md_path = SKILL_DIR / "SKILL.md"
    skill_stats = file_stats(skill_md_path)
    skill_text = skill_md_path.read_text(encoding="utf-8")
    # Body after closing frontmatter '---'
    parts = skill_text.split("---", 2)
    skill_body_bytes = len(parts[2].lstrip("\r\n").encode("utf-8")) if len(parts) == 3 else skill_stats["bytes"]

    ref_files = {}
    for p in sorted((SKILL_DIR / "references").glob("*.md")):
        ref_files[p.name] = file_stats(p)

    arm_prompts_bytes = {
        "Group_A_Neutral": len(ARM_A_PROMPT.encode("utf-8")),
        "Group_B_Simple_Prompt": len(ARM_B_PROMPT.encode("utf-8")),
        "Group_C0_SKILL_Only": skill_body_bytes,
        "Group_C_SKILL_Base": skill_body_bytes,
    }

    gen_files = {
        "Group_A_Neutral": load_jsonl(RES_V2_DIR / "held-out-v2-gen-A.jsonl"),
        "Group_B_Simple_Prompt": load_jsonl(RES_V2_DIR / "held-out-v2-gen-B.jsonl"),
        "Group_C_Full_Skill_v4": load_jsonl(RES_V2_DIR / "held-out-v2-gen-C.jsonl"),
        "Group_C0_Ablation_12": load_jsonl(RES_V2_DIR / "held-out-v2-gen-C0.jsonl"),
    }
    reg_v4_rows = load_jsonl(RES_V2_DIR / "regression-v4-raw.jsonl")
    reg_v3_rows = load_jsonl(RES_V1_DIR / "held-out-raw-results.jsonl")

    arms_perf = {}
    for arm, rows in gen_files.items():
        words = [r["words"] for r in rows]
        chars = [r["chars"] for r in rows]
        out_bytes = [len(r["output"].encode("utf-8")) for r in rows]
        lat = [r["latency_sec"] for r in rows]
        in_bytes = []
        for r in rows:
            if arm == "Group_A_Neutral":
                b = arm_prompts_bytes["Group_A_Neutral"]
            elif arm == "Group_B_Simple_Prompt":
                b = arm_prompts_bytes["Group_B_Simple_Prompt"]
            elif arm == "Group_C0_Ablation_12":
                b = arm_prompts_bytes["Group_C0_SKILL_Only"]
            else:
                b = arm_prompts_bytes["Group_C_SKILL_Base"] + sum(
                    ref_files[rn]["bytes"] for rn in r.get("refs_loaded", []) if rn in ref_files
                )
            in_bytes.append(b)
        arms_perf[arm] = {
            "n": len(rows),
            "skill_prompt_bytes": summarize_numeric(in_bytes),
            "skill_prompt_est_tokens_b_div_3_8": round(statistics.mean(in_bytes) / 3.8, 1),
            "output_words": summarize_numeric(words),
            "output_chars": summarize_numeric(chars),
            "output_bytes": summarize_numeric(out_bytes),
            "output_est_tokens_b_div_3_8": round(statistics.mean(out_bytes) / 3.8, 1),
            "latency_sec": summarize_numeric(lat),
        }

    def ref_dist(rows: list[dict[str, Any]]) -> dict[str, Any]:
        num_counts = Counter(len(r.get("refs_loaded", [])) for r in rows)
        file_counts = Counter(ref for r in rows for ref in r.get("refs_loaded", []))
        return {
            "n": len(rows),
            "refs_count_per_case": {str(k): v for k, v in sorted(num_counts.items())},
            "refs_frequency": dict(file_counts),
        }

    return {
        "skill_md": skill_stats,
        "skill_md_body_bytes": skill_body_bytes,
        "skill_md_body_est_tokens_b_div_3_8": round(skill_body_bytes / 3.8, 1),
        "references": ref_files,
        "all_references_total_bytes": sum(v["bytes"] for v in ref_files.values()),
        "prompt_overhead_static_bytes": arm_prompts_bytes,
        "held_out_v2_arms_performance": arms_perf,
        "regression_v4_verbosity": {
            "v4_words": summarize_numeric([r["v4_words"] for r in reg_v4_rows]),
            "v3_words": summarize_numeric([r["exp_words"] for r in reg_v3_rows]),
            "v4_latency_sec": summarize_numeric([r["latency_sec"] for r in reg_v4_rows]),
        },
        "reference_loading_held_out_v2_C": ref_dist(gen_files["Group_C_Full_Skill_v4"]),
        "reference_loading_regression_v4": ref_dist(reg_v4_rows),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze Round 2 results and generate summary-stats-v2.json")
    parser.add_argument("--allow-partial", action="store_true", help="Skip sections whose JSONL files do not exist yet")
    args = parser.parse_args()

    out: dict[str, Any] = {}

    sections = [
        ("historical_v3_rubric_v1", analyze_v1_historical),
        ("judge_calibration_v2", analyze_judge_calibration),
        ("v3_reaudit_rubric_v2", analyze_v3_reaudit),
        (
            "regression_v4_vs_v3",
            lambda: _extract_side_stats(
                load_jsonl(RES_V2_DIR / "regression-v4-vs-v3.jsonl"),
                left_key="v3",
                right_key="v4",
                left_eval_key="v3_eval",
                right_eval_key="v4_eval",
                left_hf_key="v3_hf_union",
                right_hf_key="v4_hf_union",
            ),
        ),
        (
            "held_out_v2_C_vs_B",
            lambda: _extract_side_stats(
                load_jsonl(RES_V2_DIR / "held-out-v2-judge-C-vs-B.jsonl"),
                left_key="B",
                right_key="C",
                left_eval_key="B_eval",
                right_eval_key="C_eval",
                left_hf_key="B_hf_union",
                right_hf_key="C_hf_union",
            ),
        ),
        (
            "held_out_v2_C_vs_A",
            lambda: _extract_side_stats(
                load_jsonl(RES_V2_DIR / "held-out-v2-judge-C-vs-A.jsonl"),
                left_key="A",
                right_key="C",
                left_eval_key="A_eval",
                right_eval_key="C_eval",
                left_hf_key="A_hf_union",
                right_hf_key="C_hf_union",
            ),
        ),
        (
            "held_out_v2_C_vs_C0",
            lambda: _extract_side_stats(
                load_jsonl(RES_V2_DIR / "held-out-v2-judge-C-vs-C0.jsonl"),
                left_key="C0",
                right_key="C",
                left_eval_key="C0_eval",
                right_eval_key="C_eval",
                left_hf_key="C0_hf_union",
                right_hf_key="C_hf_union",
            ),
        ),
        ("trigger_eval", analyze_trigger_eval),
        ("runtime_overhead", analyze_overhead),
    ]

    missing = []
    for name, fn in sections:
        try:
            out[name] = fn()
        except FileNotFoundError as exc:
            if not args.allow_partial:
                raise
            missing.append({"section": name, "missing_file": str(exc)})

    if missing:
        out["_missing_sections"] = missing

    out_path = RES_V2_DIR / "summary-stats-v2.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {out_path.relative_to(ROOT)} ({len(out)} sections, missing={len(missing)})")


if __name__ == "__main__":
    main()
