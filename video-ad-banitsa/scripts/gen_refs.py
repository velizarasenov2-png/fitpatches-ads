"""Reference images for the banitsa ad (Nano Banana Pro on kie.ai)."""
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor

import kie

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "refs")

FIGURE = (
    "3D stylized female figure, around 50 years old, full body, soft rounded silhouette with a full belly and "
    "wide hips, made of semi-translucent frosted glass with a faint warm inner glow, wearing a simple loose "
    "knee-length dress made of the same frosted glass, smooth simplified mannequin-like form, smooth featureless "
    "face, hair shaped as a simple low bun, standing in a neutral relaxed pose, arms at her sides, centered, dark "
    "navy background, cinematic soft volumetric lighting, photorealistic 3D render, Octane quality. Reference "
    "character for a family-friendly medical animation."
)

JOBS = {
    "ref_figure": dict(image_input=[], prompt=FIGURE),
    "ref_figure_v2": dict(image_input=[], prompt=FIGURE),
    "ref_kitchen": dict(image_input=[], prompt=(
        "3D stylized kitchen interior of an ordinary apartment, soft morning light through a window with white "
        "net curtains, a wooden table, white square wall tiles, a wall cabinet with wooden doors, a white coffee "
        "cup with rising steam on the table, calm and warm, deep dark navy tones in the shadows, empty room, "
        "cinematic volumetric light, photorealistic 3D render, Octane quality, vertical 9:16 composition.")),
    "ref_banitsa": dict(image_input=[], prompt=(
        "3D photorealistic render of a square slice of Bulgarian banitsa on a white plate: many thin golden "
        "flaky phyllo pastry layers, crisp browned top, soft white cheese filling visible between the layers, "
        "a steaming white coffee cup beside it on a wooden table, warm morning light, dark navy shadows, "
        "shallow depth of field, Octane quality, vertical 9:16 composition.")),
}


def run(name):
    j = JOBS[name]
    tid = kie.create("nano-banana-pro", {"prompt": j["prompt"], "image_input": j["image_input"],
                                         "aspect_ratio": "9:16", "resolution": "2K", "output_format": "jpg"})
    d = kie.wait(tid, every=8)
    rec = {"name": name, "taskId": tid, "state": d["state"], "credits": d.get("creditsConsumed"),
           "urls": kie.result_urls(d)}
    if rec["urls"]:
        kie.download(rec["urls"][0], os.path.join(OUT, f"{name}.jpg"))
    print(json.dumps(rec, ensure_ascii=False), flush=True)
    with open(os.path.join(OUT, "refs_log.jsonl"), "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


if __name__ == "__main__":
    names = sys.argv[1:] or list(JOBS)
    with ThreadPoolExecutor(len(names)) as ex:
        list(ex.map(run, names))
