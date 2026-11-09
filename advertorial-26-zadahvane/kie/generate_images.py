"""Images for advertorial-26-zadahvane on kie.ai (Nano Banana Pro). Output: ../img/<name>.jpg

    python3 kie/generate_images.py              # all
    python3 kie/generate_images.py stairs       # one
The kie.ai key is injected by the session proxy; outside it, export KIE_API_KEY.
"""
import json, os, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

API = "https://api.kie.ai/api/v1/jobs"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "img")
NO_TEXT = " Absolutely no text, letters, numbers, labels, logos or watermarks anywhere in the image."

JOBS = {
    "stairs": (
        "Realistic candid phone photo in the stairwell of an old Bulgarian panel apartment block: worn terrazzo "
        "steps, pale green painted walls, a metal railing, a small dusty window. A woman around 50, ordinary "
        "figure with a round belly, in a dark winter coat, has stopped on the landing between floors, one hand "
        "gripping the railing and the other pressed to her chest, catching her breath with her eyes closed and "
        "mouth slightly open. Two full plastic supermarket bags rest on the step beside her. Cold fluorescent "
        "light mixed with grey daylight, real life, unposed." + NO_TEXT
    ),
    "diaphragm": (
        "Clean 3D medical illustration, side view cross-section of an adult woman's torso on a dark navy "
        "background: pink lungs in the chest, the dome-shaped diaphragm muscle under them, and below it the "
        "abdominal organs (liver, stomach, intestines) wrapped and tightly packed in thick glowing yellow "
        "visceral fat that pushes the diaphragm upward and leaves the lungs visibly squeezed and smaller. "
        "Educational anatomy style, soft rim lighting, high detail." + NO_TEXT
    ),
    "supplements": (
        "Realistic photo of a Bulgarian kitchen counter crowded with the clutter of years of trying: many plain "
        "unlabeled supplement bottles and jars in different colours, boxes of herbal detox tea without print, a "
        "protein shaker, opened blister packs, a coiled measuring tape, a crumpled printed diet plan with a pen, "
        "a half-eaten bowl of salad. Morning window light, slightly messy, real life." + NO_TEXT
    ),
    "finale": (
        "Realistic warm candid photo in a bright Bulgarian apartment block stairwell: a smiling woman around 50 "
        "in a light spring coat climbs the last steps to the top-floor landing easily, laughing, holding the hand "
        "of her granddaughter of about 6 who runs ahead of her up the stairs. Sunlight through the window, joyful "
        "real-life family moment, shot on a phone." + NO_TEXT
    ),
}


def _call(url, data=None):
    req = urllib.request.Request(
        url, data=json.dumps(data).encode() if data is not None else None,
        headers={"Authorization": f"Bearer {os.environ.get('KIE_API_KEY', 'proxy-injected')}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def run(name):
    inp = {"prompt": JOBS[name], "image_input": [], "aspect_ratio": "4:3", "resolution": "2K", "output_format": "jpg"}
    j = _call(f"{API}/createTask", {"model": "nano-banana-pro", "input": inp})
    if j.get("code") != 200:
        raise RuntimeError(f"{name}: {j}")
    tid, t0 = j["data"]["taskId"], time.time()
    while True:
        d = _call(f"{API}/recordInfo?taskId={tid}")["data"]
        if d["state"] in ("success", "fail") or time.time() - t0 > 900:
            break
        time.sleep(8)
    urls = json.loads(d.get("resultJson") or "{}").get("resultUrls", [])
    if urls:
        urllib.request.urlretrieve(urls[0], os.path.join(OUT, f"{name}-raw.jpg"))
    return name, d["state"], d.get("failMsg")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    with ThreadPoolExecutor(4) as ex:
        for r in ex.map(run, sys.argv[1:] or list(JOBS)):
            print(*r)
