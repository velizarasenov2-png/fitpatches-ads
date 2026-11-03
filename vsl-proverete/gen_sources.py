#!/usr/bin/env python3
"""Writes sources.md (clip → library, page, licence) from shots.json and <workdir>/replacements.json."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = sys.argv[1]
shots = json.load(open(os.path.join(HERE, "shots.json"), encoding="utf-8"))
repl = {str(r["n"]): r for r in json.load(open(os.path.join(WORK, "replacements.json"), encoding="utf-8"))}
by_src = {}
for s in shots:
    if s.get("page"):
        by_src.setdefault(s["src"], s)

LIC = {
    "MIXKIT": "Mixkit Free License: търговска употреба, без указване на автор",
    "COVERR": "Coverr License: безплатно, търговска употреба, без указване на автор",
    "ПРОДУКТ": "собствени снимки на FitPatches (fitpatches.net)",
}
rows = []
for s in shots:
    src = s["src"]
    if src.startswith("REPL"):
        n = src.split(":")[1] if ":" in src else s["n"]
        r = repl.get(str(n), {})
        lib, page = r.get("source", "?"), r.get("page_url", "")
        what = r.get("what_it_shows_bg", r.get("what_it_shows", ""))
        if ":" in src:
            what = f"повторение на кадър {n}, черно-бяло и забавено"
    elif src.startswith("still_"):
        lib, page, what = "ПРОДУКТ", "", f"{src} (make_graphics.py)"
    else:
        ref = by_src.get(src, s)
        lib, page, what = ref.get("library", "?").split()[0], ref.get("page", ""), s.get("desc", "")
        if src in by_src and by_src[src]["n"] != s["n"]:
            what = f"повторение на кадър {by_src[src]['n']}, друг отрязък"
    rows.append(f"| {s['n']} | {s['vo']} | {what} | {lib} | {page} |")

with open(os.path.join(HERE, "sources.md"), "w", encoding="utf-8") as f:
    f.write("# Източници на кадрите\n\n")
    f.write("Всички клипове са свалени от страницата им и проверени визуално. Лицензи:\n\n")
    for k, v in LIC.items():
        f.write(f"- **{k}**: {v}\n")
    f.write("- **Музика**: Mixkit, пиано, тракове 168 (до появата на продукта) и 601 (след нея), assets.mixkit.co/music/168/168.mp3 и /601/601.mp3, Mixkit Free License\n\n")
    f.write("| № | Глас | Кадър | Библиотека | Страница |\n|---|---|---|---|---|\n")
    f.write("\n".join(rows) + "\n")
print("wrote sources.md", len(rows))
