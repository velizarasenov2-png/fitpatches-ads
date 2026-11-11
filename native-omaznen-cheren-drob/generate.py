"""Native ad images: hyper-realistic fatty liver under an examination lamp (kie.ai Nano Banana Pro).

    python3 generate.py              # all
    python3 generate.py liver_lamp   # one
Raw output: raw/<name>-raw.jpg. The kie.ai key is injected by the session proxy; outside it, export KIE_API_KEY.
"""
import json, os, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

API = "https://api.kie.ai/api/v1/jobs"
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw")
NO_TEXT = " Absolutely no text, letters, numbers, labels, logos or watermarks anywhere in the image."
REAL = (" Hyper-realistic, looks like a real unedited photo taken on a phone in a real hospital, natural imperfections, "
        "macro-level texture detail, raw and slightly unsettling, a little gross to look at, but no blood and no gore.")

JOBS = {
    "liver_lamp": (
        "Candid photo in a hospital pathology lab: on a stainless steel dissection tray lies a real human liver that is "
        "visibly very fatty — swollen and enlarged, pale yellow-beige, greasy, with a waxy glistening surface, mottled "
        "yellow fat patches, rounded blunt edges and small beads of oily fat pooling on the steel around it. A doctor in "
        "a white coat, surgical cap and face mask, wearing blue nitrile gloves, leans over it and examines it closely "
        "through a round illuminated magnifying lamp positioned right above the liver; the cold white lamp light makes "
        "the greasy surface shine." + REAL + NO_TEXT, "4:5"),
    "liver_lamp_top": (
        "Overhead photo looking straight down onto a stainless steel tray under a bright round examination lamp: a real "
        "human fatty liver, enlarged, pale yellowish, greasy and waxy with an oily sheen, small fat droplets smeared on "
        "the tray, blunt rounded edges. Two blue-gloved doctor's hands: one lifts the edge with steel forceps to show the "
        "yellow greasy tissue, the other holds a small steel probe pointing at it. A steel ruler lies beside it for "
        "scale." + REAL + NO_TEXT, "4:5"),
    "liver_compare_lab": (
        "Photo in a hospital pathology lab: two real human livers lie side by side on one stainless steel tray under a "
        "bright examination lamp — on the left a normal healthy liver, deep reddish-brown, smooth and firm; on the right a "
        "much bigger fatty liver, swollen, pale yellow, greasy and waxy with glistening fat and oily smears on the steel. "
        "A doctor in a white coat and blue gloves leans in and points at the fatty one with a steel probe, his face mostly "
        "out of frame." + REAL + NO_TEXT, "4:5"),
}


def _call(url, data=None):
    req = urllib.request.Request(
        url, data=json.dumps(data).encode() if data is not None else None,
        headers={"Authorization": f"Bearer {os.environ.get('KIE_API_KEY', 'proxy-injected')}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def run(name):
    prompt, ar = JOBS[name]
    inp = {"prompt": prompt, "image_input": [], "aspect_ratio": ar, "resolution": "2K", "output_format": "jpg"}
    j = _call(f"{API}/createTask", {"model": "nano-banana-pro", "input": inp})
    if j.get("code") != 200:
        return name, "create-failed", j
    tid, t0 = j["data"]["taskId"], time.time()
    while True:
        d = _call(f"{API}/recordInfo?taskId={tid}")["data"]
        if d["state"] in ("success", "fail") or time.time() - t0 > 900:
            break
        time.sleep(8)
    urls = json.loads(d.get("resultJson") or "{}").get("resultUrls", [])
    if urls:
        urllib.request.urlretrieve(urls[0], os.path.join(RAW, f"{name}-raw.jpg"))
    return name, d["state"], d.get("failMsg")


if __name__ == "__main__":
    os.makedirs(RAW, exist_ok=True)
    with ThreadPoolExecutor(4) as ex:
        for r in ex.map(run, sys.argv[1:] or list(JOBS)):
            print(*r, flush=True)
