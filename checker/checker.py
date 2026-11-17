#!/usr/bin/env python3
"""canon-forge constraint checker (v0.1).

Compares a generated-asset description against the canon rule set and
reports anachronism violations. Standard library only — no installs.

Usage:
    python3 checker/checker.py examples/asset-anachronistic.json
    python3 checker/checker.py examples/asset-anachronistic.json --save examples/report.txt
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULES_PATH = ROOT / "canon" / "rules" / "late-tang.json"


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def asset_fields(asset):
    """Flatten the asset description into {field: text} for rule matching."""
    fields = asset.get("fields", {})
    return {k: " ".join(str(v) for v in vals) for k, vals in fields.items()}


def check_asset(asset, rules):
    """Return a list of violation dicts for one asset."""
    fields = asset_fields(asset)
    violations = []
    for rule in rules:
        if not rule.get("enforced", False):
            continue  # defined-but-not-enforced rules are reported separately
        check = rule.get("check", {})
        if check.get("type") != "forbidden_terms":
            continue  # required_terms not enforceable at v0.1 (context-dependent)
        scope = rule.get("scope", [])
        for field in scope:
            text = fields.get(field, "")
            for term in check.get("terms", []):
                if term and term in text:
                    violations.append({
                        "rule_id": rule["id"],
                        "category": rule["category"],
                        "field": field,
                        "matched_term": term,
                        "statement": rule["statement"],
                        "basis": rule["basis"],
                    })
    return violations


def defined_not_enforced(rules):
    return [r for r in rules if not r.get("enforced", False)]


def main():
    ap = argparse.ArgumentParser(description="canon-forge anachronism checker")
    ap.add_argument("asset", help="path to the asset-description JSON")
    ap.add_argument("--save", help="also write the report to this path")
    args = ap.parse_args()

    ruleset = load_json(RULES_PATH)
    asset = load_json(args.asset)

    violations = check_asset(asset, ruleset["rules"])
    pending = defined_not_enforced(ruleset["rules"])
    enforced_count = sum(1 for r in ruleset["rules"] if r.get("enforced"))

    lines = []
    lines.append(f"# canon-forge report — {asset.get('asset_id', 'unknown asset')}")
    lines.append(f"ruleset: {ruleset['ruleset']} | era: {ruleset['era']}")
    lines.append(f"enforced rules checked: {enforced_count} | violations found: {len(violations)}")
    lines.append("")
    if violations:
        for v in violations:
            lines.append(f"[VIOLATION] {v['rule_id']} ({v['category']}) — field={v['field']}, term='{v['matched_term']}'")
            lines.append(f"    rule: {v['statement']}")
            lines.append(f"    basis: {v['basis']}")
            lines.append("")
    else:
        lines.append("No violations. Asset complies with the enforced canon rules.")
        lines.append("")
    if pending:
        lines.append(f"Note: {len(pending)} rules are defined but not yet enforced at v0.1:")
        for r in pending:
            lines.append(f"  - {r['id']}: {r['statement']}")

    report = "\n".join(lines)
    print(report)
    if args.save:
        Path(args.save).write_text(report, encoding="utf-8")
        print(f"\n(report saved to {args.save})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
