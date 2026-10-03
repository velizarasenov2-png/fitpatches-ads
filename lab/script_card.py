#!/usr/bin/env python3
"""Full script cards (Markdown) for the owner: the whole script scene by scene, why it should
work and how it acts on the viewer, plus the lab numbers.

Usage:
  python3 lab/script_card.py team/lab/runs/<run_id> --top 3 [--codes V1 V7] [--out <file.md>]
  python3 lab/script_card.py --source team/lab/runs/<run>/reviewed_all.json --names "S2 · 30 сек" "W2" --out <file.md>

- Content comes from <run>/reviewed_all.json (or --source); numbers from <run>/results.json.
- `why` (защо ще работи) and `how` (как ще подейства) are read from the variant itself
  (fields `why` / `how`, written by creative-strategist / copywriter). Missing → a visible TODO,
  so a report never ships an angle without them.
"""
import argparse
import json
import os
import re


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def span(t):
    nums = [float(x) for x in re.findall(r"\d+(?:\.\d+)?", str(t))]
    return (nums[0], nums[1]) if len(nums) >= 2 else (nums[0], nums[0]) if nums else (0.0, 0.0)


def fmt_t(t):
    if not re.search(r"\d+(?:\.\d+)?\s*[-–]\s*\d", str(t)):
        return str(t)  # "карта 3", "статик"
    a, b = span(t)
    f = lambda x: f"{x:g}"
    return f"{f(a)}–{f(b)} с"


def voice_by_scene(v):
    scenes = v.get("scenes") or []
    lines = v.get("transcript") or []
    out = [[] for _ in scenes]
    for ln in lines:
        start = span(ln.get("t"))[0]
        idx = None
        for i, s in enumerate(scenes):
            a, b = span(s.get("t"))
            if a <= start < b or (i == len(scenes) - 1 and start >= a):
                idx = i
                break
        if idx is None:
            idx = len(scenes) - 1 if scenes else None
        if idx is not None:
            out[idx].append(ln.get("text", ""))
    return out


def tidy(v):
    """Owner-facing wording: lab codes for the control become the real ad names."""
    def fix(x):
        if isinstance(x, str):
            return x.replace("S2/C0", "S2").replace("от C0", "от ugc1").replace("C0", "ugc1")
        if isinstance(x, list):
            return [fix(i) for i in x]
        if isinstance(x, dict):
            return {k: fix(val) for k, val in x.items()}
        return x
    return fix(v)


def card(v, res=None):
    v = tidy(v)
    o = [f"## {v['name']}"]
    meta = [v.get("format", "")] + ([f"{v['length_s']} сек"] if v.get("length_s") else [])
    if res:
        icp = res.get("icp", {})
        ab = res.get("ab_vs_control")
        ci = res.get("ci90") or []
        meta.append(f"SIM {icp.get('composite')}" + (f" [{ci[0]}–{ci[1]}]" if len(ci) == 2 else ""))
        meta.append("контрола" if res.get("control") else (f"A/B {round(ab * 100)}% срещу контролата" if ab is not None else ""))
    o.append("*" + " · ".join(m for m in meta if m) + "*")
    o.append("")
    o.append(f"**Hook (думи):** {v.get('hook_words', '')}")
    o.append(f"**Hook (кадър):** {v.get('hook_visual', '')}")
    o.append("")
    o.append("### Скриптът, сцена по сцена")
    voices = voice_by_scene(v)
    for s, vo in zip(v.get("scenes") or [], voices):
        o.append(f"**{fmt_t(s.get('t'))} · {s.get('shot', '')}**")
        if vo:
            o.append("- 🎙 " + " ".join(vo))
        if s.get("on_screen_text"):
            o.append(f"- 🖊 {s['on_screen_text']}")
        if s.get("visual"):
            o.append(f"- 🎬 {s['visual']}")
        o.append("")
    pts = v.get("primary_texts") or []
    if pts:
        o.append("### Текстове под видеото")
        for i, p in enumerate(pts, 1):
            o.append(f"**Текст {i}:**")
            o.append("> " + p.replace("\n", "\n> "))
            o.append("")
    if v.get("headlines"):
        o.append("**Заглавия:** " + " · ".join(v["headlines"]))
    if v.get("cta"):
        o.append(f"**Бутон:** {v['cta']}")
    o.append("")
    o.append("### Защо ще работи")
    o.append(v.get("why") or "⚠️ TODO: липсва `why` във варианта")
    o.append("")
    o.append("### Как ще подейства на зрителката")
    o.append(v.get("how") or "⚠️ TODO: липсва `how` във варианта")
    if res:
        o.append("")
        o.append("### Какво каза панелът")
        for q in (res.get("top_quotes") or [])[:3]:
            o.append(f"> {q}" if isinstance(q, str) else f"> {q.get('name', q.get('persona', ''))}: {q.get('quote', '')}")
        obj = [x if isinstance(x, str) else x.get("objection", "") for x in (res.get("objections") or [])[:2]]
        if obj:
            o.append("")
            o.append("**Възражения:** " + " · ".join(obj))
        curve = res.get("retention_curve") or []
        if curve:
            o.append("")
            o.append("**Задържане по сцени (ICP):** " + " → ".join(f"{round(c * 100)}%" for c in curve))
    o.append("")
    return "\n".join(o)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_dir", nargs="?")
    ap.add_argument("--codes", nargs="*", default=[])
    ap.add_argument("--top", type=int, default=0)
    ap.add_argument("--source")
    ap.add_argument("--names", nargs="*", default=[])
    ap.add_argument("--notes", help="JSON {name: {why, how}} merged into the variants")
    ap.add_argument("--out")
    a = ap.parse_args()

    notes = load(a.notes) if a.notes else {}
    cards = []
    if a.run_dir:
        content = {v["name"]: v for v in load(os.path.join(a.run_dir, "reviewed_all.json"))}
        res = load(os.path.join(a.run_dir, "results.json"))["results"]
        picked = [r for r in res if r["code"] in a.codes]
        if a.top:
            picked += [r for r in res if not r.get("anchor") and r["name"] in content][: a.top]
        seen = set()
        for r in picked:
            if r["code"] in seen or r["name"] not in content:
                continue
            seen.add(r["code"])
            v = {**content[r["name"]], **notes.get(r["name"], {})}
            cards.append(card(v, r))
    if a.source:
        for v in load(a.source):
            if any(n in v["name"] for n in a.names):
                cards.append(card({**v, **notes.get(v["name"], {})}))
    text = "\n---\n\n".join(cards)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"{len(cards)} cards → {a.out}")
    else:
        print(text)


if __name__ == "__main__":
    main()
