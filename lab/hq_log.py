#!/usr/bin/env python3
"""Prepend entries to a FitPatches HQ day log document.

Usage:
  python3 lab/hq_log.py <current_log.json|-> <day YYYY-MM-DD> "HH:MM|agent|text" ["HH:MM|agent|text" ...]

<current_log.json> is the document saved by an ArtifactData get with out_dir
(or "-" when the day has no document yet). Writes lab/out/hq/log__<day>.json
with the new entries first (max 60) and prints it; send it with ArtifactData
update/set (file_path) and the version you read.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    src, day, raw = sys.argv[1], sys.argv[2], sys.argv[3:]
    entries = []
    if src != "-":
        doc = json.load(open(src, encoding="utf-8"))
        doc = doc.get("data", doc)
        entries = doc.get("entries", [])
    new = []
    for r in raw:
        t, agent, text = r.split("|", 2)
        new.append({"t": t, "agent": agent, "text": text})
    out = {"day": day, "entries": (new + entries)[:60]}
    os.makedirs(os.path.join(ROOT, "lab", "out", "hq"), exist_ok=True)
    path = os.path.join(ROOT, "lab", "out", "hq", f"log__{day}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(path)


if __name__ == "__main__":
    main()
