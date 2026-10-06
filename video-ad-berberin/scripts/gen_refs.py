"""Generate reference images (character B, portraits, environments) with Nano Banana Pro on kie.ai."""
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor

import kie

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "refs")
REF_A_BODY = "https://tempfile.redpandaai.co/kieai/1137735/fitpatches/refs/ref_A_body.jpg"

LOOK = (
    "Photorealistic documentary photo, natural available light only, muted grey-beige colour palette, "
    "realistic, no cinematic glow, no retouching."
)
APARTMENT = (
    "Ordinary Bulgarian prefab panel-block apartment built in the 1980s. Realistic, lived-in, slightly "
    "cluttered, nothing new or stylish. Soft grey daylight through white net curtains. No people."
)

JOBS = {
    "ref_A_portrait": dict(
        image_input=[REF_A_BODY],
        prompt=(
            "Head-and-shoulders portrait of the exact same woman from the reference photo. Keep her identity "
            "100% identical: same face shape, same eyes, nose, lips, same light wrinkles around the eyes, same "
            "skin tone and skin texture, same shoulder-length dark brown hair with visible grey at the roots "
            "tied in a low ponytail, no makeup, same navy blue linen blouse with small buttons. Bulgarian "
            "woman, 51 years old, full face, tired but kind expression, looking slightly off camera. Same plain "
            "grey concrete wall background, soft even daylight. Do not beautify, do not make her younger or "
            "slimmer. " + LOOK
        ),
    ),
    "ref_B_body": dict(
        image_input=[REF_A_BODY],
        prompt=(
            "Full-body photo of the exact same woman from the reference photo, same face, same hair, same navy "
            "blue linen blouse, same straight black trousers, same flat black shoes, but about 6 kg lighter: "
            "slightly slimmer face, less fullness under the chin, waist a little more defined, the blouse "
            "falls more loosely over the belly, shoulders pulled back, standing upright with good posture, "
            "arms relaxed at her sides, no handbag. Face relaxed, a hint of calm. She must be instantly "
            "recognisable as the same person and still look like a normal 51-year-old woman who is not slim: "
            "a subtle, realistic change only, not a transformation. Same plain grey concrete wall background "
            "and pavement, soft daylight, same framing as the reference. " + LOOK
        ),
    ),
    "ref_B_portrait": dict(
        image_input=[
            "https://tempfile.aiquickdraw.com/models/nano-banana-pro/1791270593813-7t40do1347g.jpg",
            "https://tempfile.aiquickdraw.com/models/nano-banana-pro/1791270597621-t4e16980gyn.jpg",
        ],
        prompt=(
            "Head-and-shoulders portrait of the same woman. Use image 1 for the exact framing and identity "
            "(same face, eyes, nose, lips, wrinkles, skin, hair with grey roots in a low ponytail, navy linen "
            "blouse, grey concrete background) and image 2 for her slightly lighter body: about 6 kg lighter, "
            "slightly slimmer face, less fullness under the chin, shoulders back, upright. Face relaxed, a "
            "hint of calm, eyes slightly off camera. Still clearly the same 51-year-old woman, subtle change "
            "only. Do not beautify, no makeup. " + LOOK
        ),
    ),
    "env_hallway": dict(
        image_input=[],
        prompt=(
            "Vertical photo of the narrow entry hallway of an apartment. " + APARTMENT + " On the side wall a "
            "tall full-length mirror with a simple dark wooden frame; next to it a wall coat-hook rail with a "
            "black leather handbag and a grey coat hanging. Faded beige patterned wallpaper, worn laminate "
            "floor, a small shoe rack with a few pairs of shoes, a brown padded front door with a metal "
            "handle at the far end of the hallway. Soft grey morning light falls in from the open kitchen door "
            "on the side. Shot from chest height. " + LOOK
        ),
    ),
    "env_kitchen": dict(
        image_input=[],
        prompt=(
            "Vertical photo of a small apartment kitchen. " + APARTMENT + " White square wall tiles, an old "
            "white enamel gas stove with four burners and a metal moka pot on it, a small wooden table covered "
            "with a floral oilcloth, two simple wooden chairs, a window with net curtains, upper wooden kitchen "
            "cabinets, a single plain ceiling lamp, a fridge with magnets. Shot from table height, slightly "
            "from the side. " + LOOK
        ),
    ),
    "env_livingroom": dict(
        image_input=[],
        prompt=(
            "Vertical photo of an apartment living room. " + APARTMENT + " A brown fabric three-seat sofa with "
            "a knitted throw, a low wooden coffee table, a dark-brown lacquered wall unit with glass doors "
            "holding dishes, books and a small TV, a patterned rug, and a glass balcony door with net curtains "
            "leading to a small balcony with a white plastic chair. Shot from the side at seated height. "
            + LOOK
        ),
    ),
    "env_balcony": dict(
        image_input=[],
        prompt=(
            "Vertical photo taken from inside an apartment room through an open glass balcony door with a net "
            "curtain pulled aside, looking onto a small open balcony of a Bulgarian prefab panel block: metal "
            "railing, a white plastic chair, a couple of potted plants, view over grey prefab panel apartment "
            "buildings in soft morning sun. Realistic, lived-in, nothing stylish. No people. " + LOOK
        ),
    ),
    "env_clinic": dict(
        image_input=[],
        prompt=(
            "Vertical photo of a long waiting corridor in an old Bulgarian public polyclinic: a row of blue "
            "plastic chairs fixed along one wall, walls painted pale green on the lower half and off-white "
            "above, fluorescent tube lights on the ceiling, worn grey linoleum floor, several white doors with "
            "small number plates, a notice board with a few papers. Empty, no people. Long corridor "
            "perspective, camera at the far end of the corridor. " + LOOK
        ),
    ),
}


def run(name):
    j = JOBS[name]
    tid = kie.create(
        "nano-banana-pro",
        {
            "prompt": j["prompt"],
            "image_input": j["image_input"],
            "aspect_ratio": "9:16",
            "resolution": "2K",
            "output_format": "jpg",
        },
    )
    print(name, "task", tid, flush=True)
    d = kie.wait(tid, every=8)
    rec = {"name": name, "taskId": tid, "state": d["state"], "credits": d.get("creditsConsumed"),
           "fail": d.get("failMsg"), "urls": kie.result_urls(d)}
    if rec["urls"]:
        kie.download(rec["urls"][0], f"{OUT}/{name}.jpg")
    print(json.dumps(rec, ensure_ascii=False), flush=True)
    return rec


if __name__ == "__main__":
    names = sys.argv[1:] or list(JOBS)
    with ThreadPoolExecutor(len(names)) as ex:
        recs = list(ex.map(run, names))
    with open(f"{OUT}/refs_log.jsonl", "a") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
