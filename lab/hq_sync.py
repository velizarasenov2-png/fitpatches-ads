#!/usr/bin/env python3
"""Build FitPatches HQ (game dashboard) documents from lab outputs.

Usage:
  python3 lab/hq_sync.py arena team/lab/runs/<run_id>   # arena from results.json
  python3 lab/hq_sync.py radar                           # radar from team/lab/intel/latest.json

Writes one JSON file per document to lab/out/hq/ and prints the `writes` list
for an ArtifactData "batch" call (add each document's current `if_version`
from a prior "list"/"get" before sending; new documents need none).
Dashboard: https://claude.ai/artifact/AzfuqaQVNWi6gkeD7SGVRZ
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "lab", "out", "hq")


def write_doc(collection, doc_id, data):
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f"{collection}__{doc_id}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    return {"op": "set", "collection": collection, "doc_id": doc_id, "file_path": path}


def arena(run_dir):
    res = json.load(open(os.path.join(run_dir, "results.json"), encoding="utf-8"))
    variants = {v["code"]: v for v in json.load(open(os.path.join(run_dir, "variants.json"), encoding="utf-8"))}
    fighters = []
    for r in res["results"]:
        icp = r.get("icp") or {}
        v = variants.get(r["code"], {})
        quote = ""
        if r.get("top_quotes"):
            quote = r["top_quotes"][0].split(": ", 1)[-1][:140]
        real = r.get("real") or {}
        gene = None
        if r.get("mutated_gene"):
            gene = f'{r["mutated_gene"]}: {str(r.get("gene_value") or "")[:40]}'
        fighters.append({
            "code": r["code"], "name": r["name"], "score": icp.get("composite"), "ci": r.get("ci90"),
            "stop": icp.get("stop"), "watch": icp.get("watch"), "understanding": icp.get("understanding"),
            "click": icp.get("click"), "buy": icp.get("buy"), "pickup": icp.get("pickup"), "qos": icp.get("qos"),
            "curve": r.get("retention_curve"), "door_doubt": (r.get("door_doubts") or [None])[0],
            "anchor": v.get("anchor"), "gene": gene, "quote": quote,
            "ab": r.get("ab_vs_control"), "control": r.get("control"),
            "real": {k: real.get(k) for k in ("cpa", "link_ctr", "spend", "hold_rate", "pickup_rate") if real.get(k) is not None} or None,
        })
    meta = {}
    meta_path = os.path.join(run_dir, "meta.json")
    if os.path.exists(meta_path):
        meta = json.load(open(meta_path, encoding="utf-8"))
    doc = {"run_id": res["run_id"], "title": meta.get("title", ""), "calibration": res.get("calibration"),
           "fighters": fighters[:16], "warnings": res.get("warnings", [])[:5]}
    return [write_doc("hq", "arena", doc)]


def radar():
    latest = json.load(open(os.path.join(ROOT, "team", "lab", "intel", "latest.json"), encoding="utf-8"))
    # World formats first in the HQ idea list: they feed the next lab shift
    wf = [{"cb": f.get("id"), "title": f'{f.get("name", "")} · {", ".join(f.get("countries", [])[:4])}'}
          for f in latest.get("world_formats", [])]
    latest["ideas"] = (wf + latest.get("ideas", []))[:8]
    latest.pop("world_formats", None)
    return [write_doc("hq", "radar", latest)]


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("arena", "radar"):
        sys.exit(__doc__)
    writes = arena(sys.argv[2]) if sys.argv[1] == "arena" else radar()
    print(json.dumps(writes, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
