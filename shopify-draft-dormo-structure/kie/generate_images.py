"""Generate the images for the new FitPatches draft-theme sections on kie.ai (Nano Banana Pro).

Usage:
    export KIE_API_KEY=...          # set it in the environment, never commit it
    python3 generate_images.py              # all images
    python3 generate_images.py layers vs_capsules   # only some

Every finished image is downloaded to ./out/<name>.jpg and its kie.ai result URL is
appended to ./out/results.jsonl (that URL is what gets imported into Shopify Files).
"""
import json
import os
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

API = "https://api.kie.ai/api/v1/jobs"
MODEL = "nano-banana-pro"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")

# Real product photos from the store, used as references so the patch looks like the real one.
PATCH = "https://cdn.shopify.com/s/files/1/1019/0929/9545/files/fp-patch-real.png?v=1785852731"
PACK = "https://cdn.shopify.com/s/files/1/1048/3269/6657/files/fitpatches_2048_no_white_background.png"
WRIST = "https://cdn.shopify.com/s/files/1/1048/3269/6657/files/ruka_size_new_e633366f-b56d-4632-848c-4885ced7e166.png"

PATCH_LOOK = (
    "The patch must look exactly like the reference photo: a thin round translucent pink patch about the size "
    "of a coin, with the word 'FitPatches' printed in a ring around its edge. Do not invent other logos or text."
)

JOBS = {
    # fpx-layers: exploded view of the patch layers
    "layers": dict(
        aspect_ratio="1:1",
        refs=[PATCH],
        prompt=(
            "Clean 3D product render, exploded view of one round skin patch separated into four thin stacked "
            "layers floating above each other with small gaps: a matte breathable top layer, a translucent pink "
            "active layer with tiny visible plant-extract particles, a soft clear adhesive layer, and a peel-off "
            "protective liner slightly curled at one edge. Soft pastel pink background (#faf0f4), soft studio "
            "light, gentle shadows, premium skincare advertising style, no text, no labels. " + PATCH_LOOK
        ),
    ),
    # fpx-nostomach: patch instead of capsules
    "nostomach": dict(
        aspect_ratio="1:1",
        refs=[PATCH, WRIST],
        prompt=(
            "Bright lifestyle photo in a calm Bulgarian apartment kitchen in the morning: a relaxed smiling woman "
            "around 40 sits at a light wooden table with a cup of tea, one small round pink patch on the inside "
            "of her forearm clearly visible. On the table in front of her an amber supplement bottle lies "
            "closed and pushed aside. Natural window light, warm neutral tones with soft pink accents, shallow "
            "depth of field, realistic skin texture, candid feel, no text. " + PATCH_LOOK
        ),
    ),
    # fpx-timeline: the patch worn day to day
    "timeline": dict(
        aspect_ratio="4:5",
        refs=[PATCH, WRIST],
        prompt=(
            "Realistic close-up photo of a woman's upper arm in a soft white t-shirt sleeve with one small round "
            "pink patch applied to clean skin, morning sunlight from a window, she holds a phone with a calendar "
            "app slightly out of focus in the background, warm and hopeful mood, soft pink and cream color "
            "palette, natural skin texture, no text overlays. " + PATCH_LOOK
        ),
    ),
    # fpx-vs: the two comparison cards
    "vs_patch": dict(
        aspect_ratio="1:1",
        refs=[PATCH],
        prompt=(
            "Product photo of a single round pink skin patch lying on a soft pastel pink surface, top-down, "
            "soft diffused studio light, gentle shadow, minimal and clean, no text besides the print on the "
            "patch. " + PATCH_LOOK
        ),
    ),
    "vs_capsules": dict(
        aspect_ratio="1:1",
        refs=[],
        prompt=(
            "Product photo of a generic amber supplement bottle tipped over with large yellow-brown herbal "
            "capsules spilling onto a light grey surface, top-down, soft diffused studio light, minimal and "
            "clean, no brand, no label text, neutral cool tones."
        ),
    ),
}


def _call(url, data=None):
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode() if data is not None else None,
        headers={"Authorization": f"Bearer {os.environ['KIE_API_KEY']}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def run(name):
    job = JOBS[name]
    inp = {"prompt": job["prompt"], "image_input": job["refs"], "aspect_ratio": job["aspect_ratio"],
           "resolution": "2K", "output_format": "jpg"}
    j = _call(f"{API}/createTask", {"model": MODEL, "input": inp})
    if j.get("code") != 200:
        raise RuntimeError(f"{name}: createTask failed: {j}")
    task_id = j["data"]["taskId"]
    t0 = time.time()
    while True:
        d = _call(f"{API}/recordInfo?taskId={task_id}")["data"]
        if d["state"] in ("success", "fail"):
            break
        if time.time() - t0 > 900:
            raise TimeoutError(f"{name}: {task_id}")
        time.sleep(8)
    urls = json.loads(d.get("resultJson") or "{}").get("resultUrls", [])
    rec = {"name": name, "taskId": task_id, "state": d["state"], "fail": d.get("failMsg"), "urls": urls}
    if urls:
        urllib.request.urlretrieve(urls[0], os.path.join(OUT, f"{name}.jpg"))
    with open(os.path.join(OUT, "results.jsonl"), "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(json.dumps(rec, ensure_ascii=False), flush=True)
    return rec


if __name__ == "__main__":
    if not os.environ.get("KIE_API_KEY"):
        sys.exit("KIE_API_KEY is not set")
    os.makedirs(OUT, exist_ok=True)
    names = sys.argv[1:] or list(JOBS)
    with ThreadPoolExecutor(len(names)) as ex:
        list(ex.map(run, names))
