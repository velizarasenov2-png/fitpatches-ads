"""FitPatches native image ads in the style of the X-ray native ad (monitor + pills + caption).

Step 1: kie.ai Nano Banana Pro makes the photos (no text on them).
Step 2: compose.py puts the pills and the caption block on top (Oswald, Cyrillic).

    python3 generate.py            # all
    python3 generate.py xray       # one
The kie.ai key is injected by the session proxy; outside it, export KIE_API_KEY.
"""
import json, os, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

API = "https://api.kie.ai/api/v1/jobs"
MODEL = "nano-banana-pro"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw")
NO_TEXT = " Absolutely no text, letters, numbers, labels, logos or watermarks anywhere in the image."

# Style reference: a colour DEXA body-composition scan the user sent (uploaded to kie.ai temp storage).
DEXA_REF = "https://tempfile.redpandaai.co/kieai/1137735/images/fitpatches-native/dexa_ref.png"
DEXA_LOOK = (
    "Each scan is a full-body DEXA body-composition scan of a standing woman, front view, arms at her sides, on a "
    "black background, in the same false colours as the reference image: fat in yellow-orange, lean tissue in "
    "red-magenta, bones in blue-cyan. LEFT scan: an obese woman with a very wide body and a large bright "
    "yellow-orange mass of visceral fat filling the whole belly around the organs and wrapping the waist. RIGHT "
    "scan: a slim woman of the same height, mostly red-magenta lean tissue with only a thin yellow outline of fat "
    "and almost no fat inside the belly. "
)

JOBS = {
    "dexa_monitor": dict(refs=[DEXA_REF], prompt=(
        "Realistic stock photograph. Close view of a widescreen computer monitor with a black bezel on a desk in a "
        "bright modern medical office, the monitor fills most of the frame, a light grey wall behind it. The "
        "screen is split in two by a thin vertical light line, each half shows one scan. " + DEXA_LOOK +
        "Leave dark empty space above each head. A doctor's hand in a white coat sleeve comes in from the lower "
        "right and holds a slim silver ballpoint pen, its tip pointing at the belly of the left scan near the "
        "middle line. Soft neutral daylight, sharp focus, high detail." + NO_TEXT
    )),
    "dexa_flat": dict(refs=[DEXA_REF], prompt=(
        "Medical imaging software view, flat screenshot, two full-body DEXA scans side by side in two black "
        "panels with thin light grey borders and a thin divider between them, like the reference image. "
        + DEXA_LOOK + "Leave dark empty space above each head. Crisp, high detail. No colour bar, no grid lines, "
        "no measurement boxes." + NO_TEXT
    )),
}


def _call(url, data=None):
    req = urllib.request.Request(
        url, data=json.dumps(data).encode() if data is not None else None,
        headers={"Authorization": f"Bearer {os.environ.get('KIE_API_KEY', 'proxy-injected')}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def run(name, take=1):
    job = JOBS[name]
    inp = {"prompt": job["prompt"], "image_input": job.get("refs", []), "aspect_ratio": "1:1", "resolution": "2K", "output_format": "jpg"}
    j = _call(f"{API}/createTask", {"model": MODEL, "input": inp})
    if j.get("code") != 200:
        raise RuntimeError(f"{name}: {j}")
    tid = j["data"]["taskId"]
    t0 = time.time()
    while True:
        d = _call(f"{API}/recordInfo?taskId={tid}")["data"]
        if d["state"] in ("success", "fail"):
            break
        if time.time() - t0 > 900:
            raise TimeoutError(name)
        time.sleep(8)
    urls = json.loads(d.get("resultJson") or "{}").get("resultUrls", [])
    fn = f"{name}_{take}.jpg"
    if urls:
        urllib.request.urlretrieve(urls[0], os.path.join(OUT, fn))
    rec = {"name": name, "take": take, "taskId": tid, "state": d["state"], "fail": d.get("failMsg"), "urls": urls}
    with open(os.path.join(OUT, "results.jsonl"), "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    names = sys.argv[1:] or list(JOBS)
    tasks = [(n, t) for n in names for t in (1, 2)]  # two takes each, pick the better one
    with ThreadPoolExecutor(6) as ex:
        for r in ex.map(lambda a: run(*a), tasks):
            print(r["name"], r["take"], r["state"], r["fail"] or "")
