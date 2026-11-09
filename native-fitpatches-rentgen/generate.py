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

JOBS = {
    "skener": (
        "Realistic stock photograph. Close view of a widescreen computer monitor with a black bezel on a desk in a "
        "bright modern medical office, the monitor fills most of the frame, a light grey wall behind it. The screen "
        "shows two axial abdominal CT scan cross-sections side by side, left and right, separated by a thin vertical "
        "light line in the middle. Grayscale CT slices of the abdomen at waist level: spine, kidneys, intestines, "
        "and the fat tissue around the organs highlighted in semi-transparent yellow-orange, as in medical body-fat "
        "analysis software. The LEFT scan has a much larger yellow-orange fat area wrapped around the organs, the "
        "RIGHT scan has clearly less. Leave dark empty space at the top of each panel. A doctor's hand in a white "
        "coat sleeve comes in from the lower right and holds a slim silver ballpoint pen, its tip pointing at the "
        "yellow-orange area of the left scan near the middle line. Soft neutral daylight, sharp focus, high detail."
        + NO_TEXT
    ),
    "garderob": (
        "Realistic candid smartphone photo in an ordinary Bulgarian apartment bedroom in daylight. A woman around 45 "
        "with brown shoulder-length hair, ordinary figure with a soft belly, wearing a loose plain black long top "
        "and black leggings, stands at an open wooden wardrobe full of mostly black and dark grey clothes on "
        "hangers. She holds up in front of her, on its hanger, a bright coral-red summer dress and looks at it with "
        "a wistful, hopeful half-smile. Natural window light, slightly lived-in room, eye level, unposed, not a "
        "model, real-life feel, leave some empty space above the dress." + NO_TEXT
    ),
}


def _call(url, data=None):
    req = urllib.request.Request(
        url, data=json.dumps(data).encode() if data is not None else None,
        headers={"Authorization": f"Bearer {os.environ.get('KIE_API_KEY', 'proxy-injected')}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def run(name, take=1):
    inp = {"prompt": JOBS[name], "image_input": [], "aspect_ratio": "1:1", "resolution": "2K", "output_format": "jpg"}
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
