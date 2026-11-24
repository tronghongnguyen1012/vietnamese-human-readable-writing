"""Validate datasets, cross-split lexical overlap, calibration/trigger suites, and SKILL.md compliance."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED_FIELDS = {
    "id",
    "split",
    "context",
    "title",
    "input",
    "purpose",
    "audience",
    "must_preserve",
    "target_errors_to_avoid",
    "evaluation_focus",
    "actionability_applicable",
    "reference_notes",
}

VALID_CONTEXTS_V1 = {
    "casual_chat",
    "concept_explanation",
    "problem_analysis",
    "workplace_communication",
    "business_docs",
    "technical_docs",
    "reports_guides_training",
    "editing_rewriting",
}

VALID_CONTEXTS_V2 = {
    "technical_depth",
    "ambiguity_no_fabrication",
    "natural_conversation",
    "hybrid_docs",
    "real_world_long_docs",
}

VALID_ERROR_CODES = {
    "S-01", "S-02", "S-03", "S-04", "S-05", "S-06",
    "P-01", "P-02", "P-03", "P-04",
    "D-01", "D-02", "D-03", "D-04",
    "R-01", "R-02", "R-03", "R-04",
    "HF-1", "HF-2", "HF-3", "HF-4", "HF-5", "HF-6",
}

VALID_CRITERIA = {f"D{i}" for i in range(1, 10)}


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(f"Missing dataset file: {path}")
    records: list[dict] = []
    with path.open("r", encoding="utf-8") as fh:
        for line_no, raw_line in enumerate(fh, start=1):
            line = raw_line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path.name}:{line_no} invalid JSON: {exc}") from exc
            records.append(obj)
    return records


def validate_dataset(records: list[dict], expected_split: str, valid_contexts: set[str], filename: str) -> list[str]:
    errors: list[str] = []
    contexts_seen: dict[str, int] = {ctx: 0 for ctx in valid_contexts}

    for idx, rec in enumerate(records, start=1):
        prefix = f"{filename}[#{idx} id={rec.get('id', '?')}]"
        missing = REQUIRED_FIELDS - set(rec.keys())
        if missing:
            errors.append(f"{prefix} missing fields: {sorted(missing)}")
            continue

        if rec["split"] != expected_split:
            errors.append(f"{prefix} expected split='{expected_split}', got '{rec['split']}'")

        ctx = rec["context"]
        if ctx not in valid_contexts:
            errors.append(f"{prefix} invalid context: '{ctx}'")
        else:
            contexts_seen[ctx] += 1

        if not isinstance(rec["must_preserve"], list) or not rec["must_preserve"]:
            errors.append(f"{prefix} must_preserve must be a non-empty list")

        if not isinstance(rec["target_errors_to_avoid"], list) or not rec["target_errors_to_avoid"]:
            errors.append(f"{prefix} target_errors_to_avoid must be a non-empty list")
        else:
            invalid_errs = set(rec["target_errors_to_avoid"]) - VALID_ERROR_CODES
            if invalid_errs:
                errors.append(f"{prefix} invalid error codes: {sorted(invalid_errs)}")

        if not isinstance(rec["evaluation_focus"], list) or not rec["evaluation_focus"]:
            errors.append(f"{prefix} evaluation_focus must be a non-empty list")
        else:
            invalid_crit = set(rec["evaluation_focus"]) - VALID_CRITERIA
            if invalid_crit:
                errors.append(f"{prefix} invalid evaluation_focus codes: {sorted(invalid_crit)}")

        if not isinstance(rec["actionability_applicable"], bool):
            errors.append(f"{prefix} actionability_applicable must be boolean")

        for text_field in ("id", "title", "input", "purpose", "audience", "reference_notes"):
            if not isinstance(rec[text_field], str) or not rec[text_field].strip():
                errors.append(f"{prefix} '{text_field}' must be a non-empty string")

    missing_ctx = [c for c, cnt in contexts_seen.items() if cnt == 0]
    if missing_ctx:
        errors.append(f"{filename} missing contexts: {missing_ctx}")

    return errors


def normalize_tokens(text: str) -> set[str]:
    cleaned = re.sub(r"[^\w\s]", " ", text.lower())
    return {t for t in cleaned.split() if len(t) > 1}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def check_cross_overlap(
    groups: list[tuple[str, list[dict]]],
    threshold: float = 0.35,
) -> tuple[list[dict], list[str]]:
    flagged: list[dict] = []
    errors: list[str] = []
    max_sim = 0.0

    for i in range(len(groups)):
        name_a, recs_a = groups[i]
        for j in range(i + 1, len(groups)):
            name_b, recs_b = groups[j]
            for ra in recs_a:
                tok_a = normalize_tokens(ra["input"])
                for rb in recs_b:
                    if ra["input"].strip() == rb["input"].strip():
                        errors.append(f"Exact input duplicate: {name_a}:{ra['id']} == {name_b}:{rb['id']}")
                    sim = jaccard(tok_a, normalize_tokens(rb["input"]))
                    if sim > max_sim:
                        max_sim = sim
                    if sim >= threshold:
                        flagged.append({
                            "pair": f"{name_a}:{ra['id']} <-> {name_b}:{rb['id']}",
                            "jaccard": round(sim, 3),
                        })
                        errors.append(
                            f"High lexical overlap ({sim:.3f} >= {threshold}): {name_a}:{ra['id']} vs {name_b}:{rb['id']}"
                        )
    return {"max_jaccard_similarity": round(max_sim, 3), "flagged_pairs": flagged}, errors


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", text, flags=re.DOTALL)
    if not match:
        raise ValueError("Missing valid YAML frontmatter delimited by ---")
    yaml_block, body = match.group(1), match.group(2)

    fields: dict[str, str] = {}
    lines = yaml_block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.strip().startswith("#"):
            i += 1
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not m:
            raise ValueError(f"Unsupported frontmatter line: {line}")
        key, val = m.group(1), m.group(2).strip()
        if val in (">-", ">", "|", "|-"):
            folded: list[str] = []
            i += 1
            while i < len(lines) and (lines[i].startswith("  ") or not lines[i].strip()):
                folded.append(lines[i].strip())
                i += 1
            fields[key] = " ".join(part for part in folded if part).strip()
            continue
        fields[key] = val.strip('"').strip("'")
        i += 1
    return fields, body


def validate_skill(skill_dir: Path, strict_tool_agnostic: bool = False) -> tuple[list[str], dict]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [f"Missing {skill_md}"], {}

    raw = skill_md.read_text(encoding="utf-8")
    try:
        fm, body = parse_frontmatter(raw)
    except ValueError as exc:
        return [f"SKILL.md frontmatter error: {exc}"], {}

    name = fm.get("name", "")
    desc = fm.get("description", "")

    if not name:
        errors.append("SKILL.md frontmatter missing 'name'")
    else:
        if name != skill_dir.name:
            errors.append(f"SKILL.md name '{name}' != parent folder '{skill_dir.name}'")
        if len(name) > 64:
            errors.append(f"SKILL.md name exceeds 64 chars ({len(name)})")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
            errors.append(f"SKILL.md name '{name}' violates lowercase hyphenated spec")

    if not desc:
        errors.append("SKILL.md frontmatter missing 'description'")
    else:
        if len(desc) > 1024:
            errors.append(f"SKILL.md description exceeds 1024 chars ({len(desc)})")
        if not desc.startswith("Use when"):
            errors.append("SKILL.md description should start with 'Use when'")

    if strict_tool_agnostic and "read_file" in body:
        errors.append("SKILL.md contains hardcoded tool name 'read_file' (violates FIX-05 tool-agnostic spec)")

    rel_links = re.findall(r"\[[^\]]+\]\((\./[^)]+|references/[^)]+)\)", body)
    if not rel_links:
        errors.append("SKILL.md contains no relative links to references/")
    for link in rel_links:
        target = (skill_dir / link).resolve()
        if not target.exists():
            errors.append(f"Broken relative link in SKILL.md: {link} -> {target}")

    ref_sizes = {}
    for ref_path in sorted((skill_dir / "references").glob("*.md")):
        rtxt = ref_path.read_text(encoding="utf-8")
        ref_sizes[ref_path.name] = {
            "lines": len(rtxt.splitlines()),
            "words": len(rtxt.split()),
            "chars": len(rtxt),
            "bytes": len(rtxt.encode("utf-8")),
        }

    stats = {
        "skill_name": name,
        "description_chars": len(desc),
        "total_lines": len(raw.splitlines()),
        "body_words": len(body.split()),
        "total_chars": len(raw),
        "total_bytes": len(raw.encode("utf-8")),
        "relative_links_checked": len(rel_links),
        "references": ref_sizes,
    }
    return errors, stats


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Vi Writer datasets and skill.")
    parser.add_argument("--check-skill", action="store_true", help="Also validate SKILL.md and reference links.")
    parser.add_argument("--allow-read-file", action="store_true", help="Allow legacy read_file check override.")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[2]
    eval_dir = repo_root / "evaluation"

    dev_records = load_jsonl(eval_dir / "development.jsonl")
    reg_records = load_jsonl(eval_dir / "held-out-test.jsonl")
    v2_records = load_jsonl(eval_dir / "held-out-v2.jsonl")
    cal_records = load_jsonl(eval_dir / "judge-calibration.jsonl")
    trg_records = load_jsonl(eval_dir / "trigger-eval.jsonl")

    errors: list[str] = []
    errors.extend(validate_dataset(dev_records, "dev", VALID_CONTEXTS_V1, "development.jsonl"))
    errors.extend(validate_dataset(reg_records, "held_out", VALID_CONTEXTS_V1, "held-out-test.jsonl"))
    errors.extend(validate_dataset(v2_records, "held_out_v2", VALID_CONTEXTS_V2, "held-out-v2.jsonl"))

    if len(dev_records) < 16:
        errors.append(f"development.jsonl has {len(dev_records)} cases (< 16)")
    if len(reg_records) < 24:
        errors.append(f"held-out-test.jsonl has {len(reg_records)} cases (< 24)")
    if len(v2_records) < 24:
        errors.append(f"held-out-v2.jsonl has {len(v2_records)} cases (< 24)")
    if len(cal_records) < 6:
        errors.append(f"judge-calibration.jsonl has {len(cal_records)} cases (< 6)")
    if len(trg_records) < 12:
        errors.append(f"trigger-eval.jsonl has {len(trg_records)} queries (< 12)")

    all_ids = [r.get("id") for r in dev_records + reg_records + v2_records + cal_records + trg_records]
    if len(all_ids) != len(set(all_ids)):
        errors.append("Duplicate IDs detected across datasets")

    overlap_stats, overlap_errs = check_cross_overlap([
        ("dev", dev_records),
        ("reg_v3", reg_records),
        ("held_out_v2", v2_records),
    ])
    errors.extend(overlap_errs)

    skill_stats = None
    if args.check_skill:
        skill_dir = repo_root / "skills" / "vietnamese-human-readable-writing"
        skill_errs, skill_stats = validate_skill(skill_dir, strict_tool_agnostic=not args.allow_read_file)
        errors.extend(skill_errs)

    summary = {
        "status": "FAIL" if errors else "PASS",
        "counts": {
            "development": len(dev_records),
            "regression_v3": len(reg_records),
            "held_out_v2": len(v2_records),
            "judge_calibration": len(cal_records),
            "trigger_eval": len(trg_records),
        },
        "cross_dataset_overlap": overlap_stats,
        "skill_stats": skill_stats,
        "errors": errors,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
