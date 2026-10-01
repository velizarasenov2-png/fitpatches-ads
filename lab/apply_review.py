#!/usr/bin/env python3
"""Apply a compliance review (verdicts + literal edits) to draft variants → reviewed.json.

Usage:
  python3 lab/apply_review.py team/lab/runs/<run_id> drafts/copywriter.json drafts/strategist.json

Reads <run_dir>/drafts/compliance.json:
  [{"name", "verdict": "ok|fix|stop", "issues": [...], "changes": "...",
    "edits": [{"old": "exact substring", "new": "replacement"}]}]
Each edit replaces every occurrence of `old` in the variant's ad text fields. Edits that match
nothing are reported (the reviewer copied the text inexactly) so they can be fixed by hand.
Writes <run_dir>/reviewed.json (drafts + "compliance" field) for lab/build_round.py.
"""
import json
import os
import sys

TEXT_KEYS = {"hook_words", "hook_visual", "visual", "on_screen_text", "text", "primary_texts",
             "headlines", "offer", "shot"}


def replace(obj, old, new, key=""):
    """Return (new_obj, hits)."""
    if isinstance(obj, str):
        if key in TEXT_KEYS and old in obj:
            return obj.replace(old, new), obj.count(old)
        return obj, 0
    if isinstance(obj, list):
        out, hits = [], 0
        for x in obj:
            y, h = replace(x, old, new, key)
            out.append(y)
            hits += h
        return out, hits
    if isinstance(obj, dict):
        out, hits = {}, 0
        for k, v in obj.items():
            y, h = replace(v, old, new, k)
            out[k] = y
            hits += h
        return out, hits
    return obj, 0


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    run_dir = sys.argv[1]
    drafts = []
    for p in sys.argv[2:]:
        drafts += json.load(open(os.path.join(run_dir, p), encoding="utf-8"))
    reviews = {r["name"]: r for r in json.load(open(os.path.join(run_dir, "drafts", "compliance.json"), encoding="utf-8"))}
    out, problems = [], []
    for v in drafts:
        r = reviews.get(v["name"])
        if not r:
            problems.append(f'no review for {v["name"]}')
            continue
        for e in r.get("edits") or []:
            v, hits = replace(v, e["old"], e["new"])
            if not hits:
                problems.append(f'{v["name"]}: edit not found → {e["old"][:80]}')
        v["compliance"] = {"verdict": r.get("verdict"), "issues": r.get("issues", []), "changes": r.get("changes", "")}
        out.append(v)
    with open(os.path.join(run_dir, "reviewed.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    for v in out:
        print(f'{v["compliance"]["verdict"]:>5}  {v["name"]}')
    if problems:
        print(f"\n⚠️ {len(problems)} problems:")
        for p in problems:
            print("  ", p)


if __name__ == "__main__":
    main()
