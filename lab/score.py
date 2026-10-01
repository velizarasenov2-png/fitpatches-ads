#!/usr/bin/env python3
"""Ad Lab scorer: aggregates audience-panel ratings into variant scores.

Usage:
  python3 lab/score.py team/lab/runs/<run_id>            # score a run
  python3 lab/score.py team/lab/runs/<run_id> --min-spend 30

Inputs in the run dir:
  variants.json      full variant list (code, name, genes, optional "real" metrics)
  panel-*.json       one file per audience-panel agent
Outputs in the run dir:
  results.json       machine-readable scores (also used for the dashboard)
  results.md         human-readable summary (Bulgarian)
Also upserts the run into team/lab/leaderboard.json.
Pure standard library on purpose: runs in any session without installs.
"""
import glob
import json
import math
import os
import random
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PERSONAS = os.path.join(ROOT, "team", "lab", "personas.json")
LEADERBOARD = os.path.join(ROOT, "team", "lab", "leaderboard.json")
METRICS = ["stop", "watch", "understanding", "relevance", "trust", "click", "buy", "pickup"]
OPTIONAL = {"understanding", "pickup"}  # kept for diagnostics, not in the composite
# Team goal (owner, 01.10): which angle/format stops the scroll, holds, gets the click and the sale.
# SIM composite on a 0-100 scale.
WEIGHTS = {"stop": 0.30, "watch": 0.25, "click": 0.25, "buy": 0.20}


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def wmean(pairs):
    tot = sum(w for _, w in pairs)
    return sum(v * w for v, w in pairs) / tot if tot else float("nan")


def composite(r):
    return 10 * sum(r[k] * w for k, w in WEIGHTS.items())


def ctr_index(r):
    # Probability-like funnel proxy: stops the scroll AND clicks.
    return 100 * (r["stop"] / 10) * (r["click"] / 10)


def qos(r):
    # "Angle power" index: stops the scroll, clicks AND buys. Uncalibrated proxy.
    return 1000 * (r["stop"] / 10) * (r["click"] / 10) * (r["buy"] / 10)


def ranks(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    rk = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        for k in range(i, j + 1):
            rk[order[k]] = (i + j) / 2 + 1
        i = j + 1
    return rk


def spearman(a, b):
    if len(a) < 3:
        return None
    ra, rb = ranks(a), ranks(b)
    ma, mb = sum(ra) / len(ra), sum(rb) / len(rb)
    num = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    den = math.sqrt(sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb))
    return num / den if den else None


def bradley_terry(codes, games, iters=200):
    """games: list of (winner, loser, weight). Returns strength per code (mean 1)."""
    p = {c: 1.0 for c in codes}
    wins = defaultdict(float)
    n = defaultdict(float)
    for w, l, wt in games:
        wins[w] += wt
        n[(w, l)] += wt
        n[(l, w)] += wt
    for _ in range(iters):
        newp = {}
        for i in codes:
            den = sum(n[(i, j)] / (p[i] + p[j]) for j in codes if j != i and n[(i, j)])
            newp[i] = (wins[i] + 0.5) / den if den else p[i]  # +0.5 prior avoids zero strength
        s = sum(newp.values()) / len(newp)
        p = {k: v / s for k, v in newp.items()}
    return p


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    run_dir = sys.argv[1]
    min_spend = 30.0
    if "--min-spend" in sys.argv:
        min_spend = float(sys.argv[sys.argv.index("--min-spend") + 1])

    personas = {p["id"]: p for p in load_json(PERSONAS)["personas"]}
    variants = load_json(os.path.join(run_dir, "variants.json"))
    vmap = {v["code"]: v for v in variants}
    panels = [load_json(f) for f in sorted(glob.glob(os.path.join(run_dir, "panel-*.json")))]
    if not panels:
        sys.exit("no panel-*.json files in " + run_dir)

    ratings, pairwise, warnings = [], [], []
    for pnl in panels:
        for r in pnl.get("ratings", []):
            if r.get("variant") not in vmap or r.get("persona") not in personas:
                warnings.append(f"unknown variant/persona in panel {pnl.get('panel_id')}: {r.get('persona')}/{r.get('variant')}")
                continue
            if "pickup" not in r and "refusal_risk" in r:  # older panel files
                r["pickup"] = 10 - float(r["refusal_risk"])
            for m in OPTIONAL:
                r.setdefault(m, 0)
            try:
                for m in METRICS:
                    r[m] = max(0, min(10, float(r[m])))
            except (KeyError, TypeError, ValueError):
                warnings.append(f"bad metrics for {r.get('persona')}/{r.get('variant')}")
                continue
            ratings.append(r)
        pairwise.extend(pnl.get("pairwise", []))

    # Completeness and flat-rater checks
    seen = {(r["persona"], r["variant"]) for r in ratings}
    used_personas = sorted({r["persona"] for r in ratings})
    missing = [(p, c) for p in used_personas for c in vmap if (p, c) not in seen]
    if missing:
        warnings.append(f"{len(missing)} missing persona×variant ratings, e.g. {missing[:3]}")
    for pid in used_personas:
        comps = [composite(r) for r in ratings if r["persona"] == pid]
        if len(comps) > 2 and (max(comps) - min(comps)) < 8:
            warnings.append(f"{pid} rated everything almost the same (spread {max(comps)-min(comps):.1f}/100)")

    by_var = defaultdict(list)
    for r in ratings:
        by_var[r["variant"]].append(r)

    def agg(rs, icp):
        sub = [r for r in rs if personas[r["persona"]]["icp"] == icp]
        if not sub:
            return None
        out = {m: round(wmean([(r[m], personas[r["persona"]]["weight"]) for r in sub]), 2) for m in METRICS}
        out["composite"] = round(wmean([(composite(r), 1) for r in sub]), 1)
        out["ctr_index"] = round(wmean([(ctr_index(r), 1) for r in sub]), 1)
        out["qos"] = round(wmean([(qos(r), 1) for r in sub]), 1)
        out["n"] = len(sub)
        return out

    # Bootstrap CI over ICP personas for the composite
    rng = random.Random(42)
    icp_ids = [p for p in used_personas if personas[p]["icp"]]

    def boot_ci(code, b=1000):
        per = {r["persona"]: composite(r) for r in by_var[code] if personas[r["persona"]]["icp"]}
        ids = [p for p in icp_ids if p in per]
        if len(ids) < 3:
            return None
        means = sorted(sum(per[rng.choice(ids)] for _ in ids) / len(ids) for _ in range(b))
        return [round(means[int(0.05 * b)], 1), round(means[int(0.95 * b)], 1)]

    # Bradley-Terry on pairwise picks (weighted by persona weight; weak picks count half)
    games = []
    for g in pairwise:
        a, b_, w = g.get("a"), g.get("b"), g.get("winner")
        if a in vmap and b_ in vmap and w in (a, b_) and g.get("persona") in personas:
            loser = b_ if w == a else a
            wt = personas[g["persona"]]["weight"] * (0.5 if g.get("weak") else 1.0)
            games.append((w, loser, wt))
    bt = bradley_terry(list(vmap), games) if games else {}

    # Simple A/B: head-to-head share of personas picking the variant over the control
    controls = [c for c, v in vmap.items() if v.get("control")]
    ab = {}
    for c in controls:
        for w, l, wt in games:
            if c in (w, l):
                other = l if w == c else w
                won = wt if w == other else 0.0
                tot = ab.setdefault(other, [0.0, 0.0])
                tot[0] += won
                tot[1] += wt

    results = []
    for code, v in vmap.items():
        icp = agg(by_var[code], True)
        other = agg(by_var[code], False)
        quotes = [f'{personas[r["persona"]]["name"]} ({r["persona"]}): {r.get("quote","")}'
                  for r in sorted(by_var[code], key=lambda r: -composite(r))[:2]]
        objections = [r.get("objection", "") for r in by_var[code] if personas[r["persona"]]["icp"] and r.get("objection")]
        door = [r.get("door_doubt", "") for r in by_var[code] if personas[r["persona"]]["icp"] and r.get("door_doubt")]
        learned = [r.get("learned", "") for r in by_var[code] if personas[r["persona"]]["icp"] and r.get("learned")]
        # Retention curve: share of ICP personas still watching after each scene (left_at 0 = watched to the end)
        icp_rs = [r for r in by_var[code] if personas[r["persona"]]["icp"]]
        n_sc = max([int(r.get("left_at") or 0) for r in icp_rs] + [len(v.get("scenes") or [])] + [0])
        curve = None
        if icp_rs and n_sc:
            curve = []
            for k in range(1, n_sc + 1):
                still = sum(1 for r in icp_rs if not r.get("left_at") or int(r["left_at"]) > k)
                curve.append(round(still / len(icp_rs), 2))
        results.append({
            "code": code, "name": v.get("name", code), "parent": v.get("parent"),
            "mutated_gene": v.get("mutated_gene"), "gene_value": v.get("gene_value"),
            "icp": icp, "others": other, "ci90": boot_ci(code),
            "bt_strength": round(bt.get(code, float("nan")), 3) if bt else None,
            "ab_vs_control": round(ab[code][0] / ab[code][1], 2) if code in ab and ab[code][1] else None,
            "control": bool(v.get("control")),
            "top_quotes": quotes, "objections": objections[:5], "door_doubts": door[:5], "learned": learned[:3],
            "retention_curve": curve, "real": v.get("real"),
        })
    results.sort(key=lambda x: -(x["icp"]["composite"] if x["icp"] else -1))
    for i, r in enumerate(results, 1):
        r["rank"] = i

    # Calibration against real Meta results (only variants with enough spend)
    calib = None
    real = [r for r in results if r.get("real") and (r["real"].get("spend") or 0) >= min_spend and r["icp"]]
    if len(real) >= 3:
        def series(key):
            return [x["real"].get(key) for x in real]
        comp = [x["icp"]["composite"] for x in real]
        ctri = [x["icp"]["ctr_index"] for x in real]
        btv = [x["bt_strength"] or 0 for x in real]
        calib = {"n_ads": len(real), "min_spend": min_spend}
        if all(v is not None for v in series("link_ctr")):
            calib["spearman_ctrindex_vs_real_ctr"] = spearman(ctri, series("link_ctr"))
        holds = [(x["icp"]["watch"], x["real"].get("hold_rate")) for x in real if x["real"].get("hold_rate") is not None]
        if len(holds) >= 3:
            calib["spearman_watch_vs_real_hold"] = spearman([a for a, _ in holds], [b for _, b in holds])
        picks = [(x["icp"]["pickup"], x["real"].get("pickup_rate")) for x in real if x["real"].get("pickup_rate") is not None]
        if len(picks) >= 3:
            calib["spearman_pickup_vs_real_pickup"] = spearman([a for a, _ in picks], [b for _, b in picks])
        cpas = series("cpa")
        if all(v is not None for v in cpas):
            inv = [-c for c in cpas]
            calib["spearman_composite_vs_real_cpa"] = spearman(comp, inv)
            calib["spearman_qos_vs_real_cpa"] = spearman([x["icp"]["qos"] for x in real], inv)
            calib["spearman_bt_vs_real_cpa"] = spearman(btv, inv)
            agree = total = 0
            for i in range(len(real)):
                for j in range(i + 1, len(real)):
                    ci, cj = cpas[i], cpas[j]
                    if abs(ci - cj) / min(ci, cj) < 0.2:
                        continue  # too close to call in reality
                    total += 1
                    real_better_i = ci < cj
                    sim_better_i = comp[i] > comp[j]
                    agree += real_better_i == sim_better_i
            calib["pairwise_agreement_cpa"] = f"{agree}/{total}" if total else None
        for k, v in list(calib.items()):
            if isinstance(v, float):
                calib[k] = round(v, 2)

    # Gene effects: mean ICP composite per mutated gene value vs its parent
    genes = defaultdict(list)
    parent_score = {r["name"]: r["icp"]["composite"] for r in results if r["icp"]}
    for r in results:
        if r.get("mutated_gene") and r["icp"]:
            base = parent_score.get(r.get("parent"))
            genes[r["mutated_gene"]].append({
                "value": r.get("gene_value"), "code": r["code"], "composite": r["icp"]["composite"],
                "delta_vs_parent": round(r["icp"]["composite"] - base, 1) if base is not None else None,
            })

    out = {
        "run_id": os.path.basename(os.path.normpath(run_dir)),
        "n_panels": len(panels), "n_ratings": len(ratings), "n_pairwise": len(games),
        "personas_used": used_personas, "weights": WEIGHTS,
        "results": results, "calibration": calib, "gene_effects": genes, "warnings": warnings,
    }
    with open(os.path.join(run_dir, "results.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    # Markdown summary
    lines = [f"# Резултати от симулацията: {out['run_id']}", "",
             f"Панели: {len(panels)} · оценки: {len(ratings)} · двойки: {len(games)} · персони: {len(used_personas)}", "",
             "| # | Код | Вариант | SIM (ICP) | 90% интервал | A/B срещу контролата | Спира | Задържа | Клик | Купува | Сила на ъгъла | BT | Външни: клик |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in results:
        i, o = r["icp"] or {}, r["others"] or {}
        abv = "контрола" if r["control"] else (f"{int(r['ab_vs_control']*100)}%" if r["ab_vs_control"] is not None else "–")
        lines.append(f"| {r['rank']} | {r['code']} | {r['name']} | **{i.get('composite','–')}** | {r['ci90'] or '–'} | {abv} | "
                     f"{i.get('stop','–')} | {i.get('watch','–')} | {i.get('click','–')} | {i.get('buy','–')} | "
                     f"{i.get('qos','–')} | {r['bt_strength'] if r['bt_strength'] is not None else '–'} | {o.get('click','–')} |")
    if calib:
        lines += ["", "## Калибрация спрямо реалните резултати в Meta", "```", json.dumps(calib, ensure_ascii=False, indent=2), "```",
                  "Spearman е от −1 до 1: над 0.5 значи, че симулацията подрежда рекламите горе-долу като реалността; около 0 значи, че не ги подрежда."]
    if genes:
        lines += ["", "## Ефект по „гени“ (спрямо родителската реклама)"]
        for g, vals in genes.items():
            for v in sorted(vals, key=lambda x: -(x["composite"])):
                lines.append(f"- **{g}** · {v['code']} · {v['value']} → {v['composite']} (Δ {v['delta_vs_parent']})")
    lines += ["", "## Какво казват персоните (топ 3)"]
    for r in results[:3]:
        lines.append(f"**{r['code']} {r['name']}**")
        lines += [f"> {q}" for q in r["top_quotes"]]
        if r.get("retention_curve"):
            lines.append("Задържане по сцени (дял ICP, които още гледат): " + " → ".join(f"{int(x*100)}%" for x in r["retention_curve"]))

    if warnings:
        lines += ["", "## ⚠️ Предупреждения", *[f"- {w}" for w in warnings]]
    with open(os.path.join(run_dir, "results.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    # Leaderboard upsert
    lb = load_json(LEADERBOARD) if os.path.exists(LEADERBOARD) else {"runs": []}
    lb["runs"] = [x for x in lb["runs"] if x["run_id"] != out["run_id"]]
    lb["runs"].append({
        "run_id": out["run_id"], "calibration": calib,
        "top": [{"code": r["code"], "name": r["name"], "composite": r["icp"]["composite"] if r["icp"] else None,
                 "ci90": r["ci90"], "real": r.get("real")} for r in results],
    })
    with open(LEADERBOARD, "w", encoding="utf-8") as f:
        json.dump(lb, f, ensure_ascii=False, indent=2)

    print("\n".join(lines[:len(results) + 6]))
    if calib:
        print("calibration:", json.dumps(calib, ensure_ascii=False))
    for w in warnings:
        print("WARN:", w)


if __name__ == "__main__":
    main()
