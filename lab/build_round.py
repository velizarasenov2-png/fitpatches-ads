#!/usr/bin/env python3
"""Build the inputs of an Ad Lab A/B round: variants.json, variants_blind.json, pairs.json.

Usage:
  python3 lab/build_round.py team/lab/runs/<run_id> \
      --reviewed team/lab/runs/<run_id>/reviewed.json \
      --control-from team/lab/runs/<old_run_id> \
      --anchors-from team/lab/runs/<old_run_id> \
      --title "A/B: ..." [--seed 7] [--extra-pairs 2]

- reviewed.json: compliance output (list). Entries with compliance.verdict == "stop" are dropped.
  If it holds a variant with "control": true or mutated_gene "compliance_clean", that is the control;
  otherwise the control is copied from --control-from (same content, same code-free form).
- Anchors (real winner / loser) are copied from --anchors-from (variants.json + variants_blind.json).
- Blind copy: random order, codes V1..Vn, only ad content. Production notes that would reveal
  the control or the gene ("като родителя", "C0", "compliance", ...) are stripped and any
  leftover hit is printed so the operator can fix it by hand.
- Pairs: every variant vs the control (the A/B test), each new variant in `extra` more pairs
  (a ring), each anchor vs 3 variants, plus winner vs loser.
"""
import argparse
import json
import os
import random
import re

CONTENT = ["format", "hook_visual", "hook_words", "length_s", "scenes", "transcript",
           "primary_texts", "headlines", "cta", "offer"]
LEAK = re.compile(r"родител|контролата|compliance|комплайънс|\bC0\b|\bген\b|почистен|симулац|ugc1", re.I)
NOTE_FIELDS = {"hook_visual", "offer", "visual", "shot"}  # production notes; ad copy is never rewritten
NOTE_LEAK = re.compile(LEAK.pattern + r"|добавен|непровер|вместо|заменя|махна|премахн|сменен", re.I)


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def clean_text(s, note):
    # "като C0 …" / "като родителя …" are author shorthand; the panel must not see them.
    s = re.sub(r"\s*\bкато C0 \(джипът\)", ": „След това един с джип щеше да ме блъсне 😑😑“", s)
    s = re.sub(r"(?i)(^|\s)като (в |при )?(C0|родителя)\b[:,]?\s*", lambda m: m.group(1), s).strip()
    s = re.sub(r"\s+от (C0|родителя)\b", "", s)
    s = s[:1].upper() + s[1:] if note and s else s
    # Parenthesised production notes that name the control or the gene go everywhere.
    s = re.sub(r"\s*\([^()]*\)", lambda m: "" if LEAK.search(m.group(0)) else m.group(0), s)
    if not note:
        return s
    s = re.sub(r"(?i)като (при )?родителя[:,]?\s*", "", s)
    parts = re.split(r"(?<=[.!?])\s+", s)
    kept = [p for p in parts if not NOTE_LEAK.search(p)]
    return " ".join(kept).strip() if kept else s


def clean(obj, key=""):
    if isinstance(obj, str):
        return clean_text(obj, key in NOTE_FIELDS)
    if isinstance(obj, list):
        return [clean(x, key) for x in obj]
    if isinstance(obj, dict):
        return {k: clean(v, k) for k, v in obj.items()}
    return obj


def leaks(obj, where=""):
    out = []
    if isinstance(obj, str):
        if LEAK.search(obj):
            out.append((where, obj[:160]))
    elif isinstance(obj, list):
        for i, x in enumerate(obj):
            out += leaks(x, f"{where}[{i}]")
    elif isinstance(obj, dict):
        for k, v in obj.items():
            out += leaks(v, f"{where}.{k}")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_dir")
    ap.add_argument("--reviewed", required=True)
    ap.add_argument("--control-from")
    ap.add_argument("--anchors-from")
    ap.add_argument("--title", default="")
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--extra-pairs", type=int, default=2)
    a = ap.parse_args()
    rnd = random.Random(a.seed)

    reviewed = [v for v in load(a.reviewed) if (v.get("compliance") or {}).get("verdict") != "stop"]
    items = []  # (meta, content)
    control = [v for v in reviewed if v.get("control") or v.get("mutated_gene") == "compliance_clean"]
    new = [v for v in reviewed if v not in control]
    if not control and a.control_from:
        old = load(os.path.join(a.control_from, "variants.json"))
        oldb = {b["code"]: b for b in load(os.path.join(a.control_from, "variants_blind.json"))}
        for v in old:
            if v.get("control"):
                c = dict(oldb[v["code"]])
                c.update({k: v[k] for k in ("name", "parent", "mutated_gene", "gene_value")})
                control = [c]
    if len(control) != 1:
        raise SystemExit(f"need exactly one control, got {len(control)}")
    for v in new:
        items.append(({"name": v["name"], "parent": v.get("parent"), "mutated_gene": v.get("mutated_gene"),
                       "gene_value": v.get("gene_value"), "control": False, "anchor": None,
                       "verdict": (v.get("compliance") or {}).get("verdict")}, v))
    c = control[0]
    items.append(({"name": c["name"], "parent": c.get("parent"), "mutated_gene": c.get("mutated_gene"),
                   "gene_value": c.get("gene_value"), "control": True, "anchor": None}, c))
    if a.anchors_from:
        old = load(os.path.join(a.anchors_from, "variants.json"))
        oldb = {b["code"]: b for b in load(os.path.join(a.anchors_from, "variants_blind.json"))}
        for v in old:
            if v.get("anchor"):
                items.append(({"name": v["name"], "parent": v.get("parent"), "mutated_gene": None,
                               "gene_value": None, "control": False, "anchor": v["anchor"],
                               "real": v.get("real")}, oldb[v["code"]]))

    rnd.shuffle(items)
    variants, blind = [], []
    for i, (meta, content) in enumerate(items, 1):
        code = f"V{i}"
        m = {"code": code, **meta, "scenes": content.get("scenes"), "real": meta.get("real")}
        variants.append(m)
        b = {"code": code}
        for k in CONTENT:
            if k in content:
                b[k] = content[k] if k in ("length_s", "cta") else clean(content[k], k)
        blind.append(b)

    ctrl = next(v["code"] for v in variants if v["control"])
    newc = [v["code"] for v in variants if not v["control"] and not v["anchor"]]
    anch = {v["anchor"]: v["code"] for v in variants if v["anchor"]}
    pairs = set()
    for x in newc + list(anch.values()):
        pairs.add(tuple(sorted((x, ctrl), key=lambda s: int(s[1:]))))
    ring = newc[:]
    rnd.shuffle(ring)
    for step in range(1, a.extra_pairs // 2 + 1 + (a.extra_pairs % 2)):
        for i, x in enumerate(ring):
            y = ring[(i + step) % len(ring)]
            if x != y:
                pairs.add(tuple(sorted((x, y), key=lambda s: int(s[1:]))))
    for code in anch.values():
        for y in rnd.sample(newc, min(3, len(newc))):
            pairs.add(tuple(sorted((code, y), key=lambda s: int(s[1:]))))
    if "winner" in anch and "loser" in anch:
        pairs.add(tuple(sorted((anch["winner"], anch["loser"]), key=lambda s: int(s[1:]))))
    pairs = sorted(pairs, key=lambda p: (int(p[0][1:]), int(p[1][1:])))

    os.makedirs(a.run_dir, exist_ok=True)
    def dump(name, obj):
        with open(os.path.join(a.run_dir, name), "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=1)
    dump("variants.json", variants)
    dump("variants_blind.json", blind)
    dump("pairs.json", [list(p) for p in pairs])
    dump("meta.json", {"title": a.title, "mode": "active"})
    print(f"{len(variants)} ads (control {ctrl}, anchors {anch}), {len(pairs)} pairs")
    for v in variants:
        print(f'  {v["code"]:>4}  {v["name"]}')
    left = leaks(blind)
    if left:
        print(f"\n⚠️ {len(left)} possible leaks in the blind copy (fix by hand):")
        for w, s in left[:30]:
            print("  ", w, "→", s)


if __name__ == "__main__":
    main()
