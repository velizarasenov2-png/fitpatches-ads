"""Generate the ad scenes with Gemini Omni 1.1 Flash on kie.ai.

Usage: python3 gen_scenes.py S01 S02 ...   (no args = all scenes)
Prompts are written positively only (the user's rule: models read negatives as positives).
"""
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor

import kie

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CLIPS = os.path.join(ROOT, "clips")
MODEL = "google/gemini-omni-flash-1-1"
RES = os.environ.get("RES", "720p")

CHAR = json.load(open(os.path.join(ROOT, "refs", "characters.json")))
A = CHAR["A"]["characterId"]  # before
B = CHAR["B"]["characterId"]  # one month later

ENV = {
    "hallway": "https://tempfile.aiquickdraw.com/models/nano-banana-pro/1791270683581-sa1hawp89xr.jpg",
    "kitchen": "https://tempfile.aiquickdraw.com/models/nano-banana-pro/1791270682659-nhe54fl4ff.jpg",
    "livingroom": "https://tempfile.aiquickdraw.com/models/nano-banana-pro/1791270696913-rbvora26958.jpg",
    "balcony": "https://tempfile.aiquickdraw.com/models/nano-banana-pro/1791270684456-qm0azh325s.jpg",
    "clinic": "https://tempfile.aiquickdraw.com/models/nano-banana-pro/1791270808406-aibmumzoc.jpg",
    "patch": "https://tempfile.aiquickdraw.com/models/nano-banana-pro/1791272822219-fmcta3fkoc.jpg",
    "s07b_frame": "https://tempfile.redpandaai.co/kieai/1137735/fitpatches/refs/s07b_lastframe.jpg",
}

STYLE = (
    " Observational documentary style. A fixed, locked-off shot: the frame stays perfectly still for the "
    "entire shot. She is unaware of the camera; her attention stays on what she is doing. Natural "
    "available light only, muted grey-beige colour palette, realistic flat look of real unedited documentary "
    "footage, everything moves at natural real-time speed. Vertical 9:16."
)
SOUND = " Sound: quiet natural room tone and the small real sounds of her movements; she stays silent."
ANIM = (
    " Clean minimal 2D medical illustration animation on a warm cream background, thin dark-grey line drawing, "
    "flat soft colours, slow smooth motion, the frame holds steady. The illustration consists only of lines, "
    "simple icons, shapes and colours. Vertical 9:16. Sound: a very soft, calm ambient piano pad."
)
WOMAN_A = (
    "The woman is the character from the character reference: a 51-year-old Bulgarian woman, 168 cm and "
    "heavy-set, about 88 kg: a soft round belly that visibly pushes the blouse outward, a thick waist, wide "
    "hips, full heavy upper arms, a full round face with a soft double chin. Dark brown hair with grey roots "
    "in a low ponytail, navy blue linen blouse, black trousers, flat black shoes. "
)
WOMAN_B = (
    "The woman is the character from the character reference, one month later: the same 51-year-old Bulgarian "
    "woman, still a full-figured, heavy-set woman of about 82 kg with a soft belly, but a little lighter than "
    "before: the face slightly slimmer, the chin a little more defined, the waist a little more visible, "
    "standing upright with her shoulders back and a calmer face. Dark brown hair with grey roots in a low "
    "ponytail, navy blue linen blouse, black trousers, flat black shoes. "
)
PATCH = (
    "a small round patch about 3.5 cm wide, a perfect circle of soft matte non-woven fabric like thin felt, "
    "dusty blush-pink, with a thin ring of tiny dark-grey dots along its edge, exactly like the patch in the "
    "patch reference image"
)

SCENES = {
    "S01": dict(dur="6", chars=[A], envs=["hallway"], prompt=(
        "Location: the entry hallway from the reference image, with the tall wooden-framed mirror, the coat "
        "hooks and the beige wallpaper; grey morning light comes in from the kitchen door. " + WOMAN_A +
        "Camera 3 metres behind her at chest height, slightly to the side, so we see her back and her face in "
        "the mirror's reflection. She stands facing the tall mirror. She pulls the hem of her navy blouse down "
        "over her belly, lets go, then pulls it down again. She looks at her reflection for one second with a "
        "flat, neutral expression. Then she takes the black handbag off the coat hook, puts it on her shoulder "
        "and turns toward the front door." + STYLE + SOUND)),
    "S02": dict(dur="8", chars=[A], envs=[], prompt=(
        "Location: a city bus stop in an ordinary Bulgarian residential neighbourhood on an overcast day, grey "
        "prefab panel apartment blocks behind, a simple metal bus shelter with a bench. " + WOMAN_A +
        "Camera static on the opposite side of the street, wide shot at chest height. She stands at the stop "
        "and holds her black handbag firmly with both hands in front of her stomach for the whole shot. Two "
        "other people wait at the stop, each lost in their own thoughts, looking down the road. In the middle of "
        "the shot a younger slim woman in jeans walks past along the pavement right in front of her, clearly "
        "visible, from left to right. The woman's eyes follow the younger woman for half a second, then she "
        "lowers her gaze to the pavement and stays still, still holding the handbag with both hands." + STYLE +
        " Sound: quiet street ambience, distant traffic, footsteps; everyone stays silent.")),
    "S03a": dict(dur="6", chars=[A], envs=["clinic"], prompt=(
        "Location: the polyclinic waiting corridor from the reference image: blue plastic chairs along a pale "
        "green wall, fluorescent ceiling light. " + WOMAN_A + "Camera static at the far end of the corridor, "
        "wide shot. She sits alone on one of the blue plastic chairs with a beige cardboard folder on her lap, "
        "hands folded on top of it, looking down at the floor. She stays almost motionless, only breathing."
        + STYLE + " Sound: the low hum of fluorescent lights and a quiet echoing corridor; she stays silent.")),
    "S03b": dict(dur="6", chars=[A], envs=["clinic"], prompt=(
        "Location: the same polyclinic corridor from the reference image, blue plastic chairs, pale green "
        "walls, fluorescent light. " + WOMAN_A + "Camera static, far away, at a side angle. A white door with a "
        "number plate opens and she walks out holding a single sheet of paper and a beige cardboard folder. "
        "She stops two steps from the door, looks at the paper, exhales slowly, and slowly puts the paper into "
        "the folder. She stands still for a moment." + STYLE +
        " Sound: the low hum of fluorescent lights, a door closing softly; she stays silent.")),
    "S04a": dict(dur="4", chars=[A], envs=[], prompt=(
        "Location: a small old bathroom of a Bulgarian panel apartment with white square tiles, a washing "
        "machine and a towel on a hook. " + WOMAN_A + "Camera static from the side at hip height. She steps onto "
        "a simple white bathroom scale and stands still for one second with her eyes fixed straight ahead on "
        "the tiled wall, then steps off." + STYLE + SOUND)),
    "S04b": dict(dur="4", chars=[A], envs=["kitchen"], prompt=(
        "Location: the kitchen from the reference image, at the small table with the floral oilcloth. "
        + WOMAN_A + "Close side shot at table height framing only her hands, forearms and navy sleeves: a white "
        "bowl of plain green lettuce salad. Her hand slowly pushes the lettuce around the bowl with a fork, the "
        "fork staying down in the bowl. Her other hand rests flat on the table." + STYLE + SOUND)),
    "S04c": dict(dur="4", chars=[A], envs=[], prompt=(
        "Location: a small bedroom of a Bulgarian panel apartment in soft window light. In the foreground a "
        "wooden chair with a zipped grey gym bag on it, covered with a thin visible layer of dust. " + WOMAN_A +
        "Camera static. In the background she walks past from left to right, her eyes on the doorway ahead, "
        "and leaves the frame. The gym bag stays in sharp focus in the foreground." + STYLE + SOUND)),
    "S04d": dict(dur="4", chars=[A], envs=["kitchen"], prompt=(
        "Location: the kitchen from the reference image. Side angle on an open upper wooden kitchen cabinet: a "
        "shelf with glass jars and a plain white box of supplement capsules. " + WOMAN_A + "Her hand pushes the "
        "white box to the back of the shelf, then she closes the cabinet door." + STYLE + SOUND)),
    "S05": dict(dur="10", chars=[A], envs=["livingroom"], prompt=(
        "Location: the living room from the reference image, late at night: black windows, every lamp switched "
        "off, the room in deep darkness; the only light is the cool glow of the phone she holds in her own hands, "
        "lighting her face. " + WOMAN_A + "She sits in the corner of the brown sofa "
        "with her legs tucked under her, scrolling slowly with her thumb. Camera static from the side; the "
        "screen faces her and we see only the back of the phone. Her thumb stops. She brings the phone closer "
        "to her face, her eyebrows rise slightly, and she keeps reading, absorbed." + STYLE +
        " Sound: a quiet night room, a faint clock ticking; she stays silent.")),
    "S06a": dict(dur="6", chars=[A], envs=["livingroom"], prompt=(
        "Location: the same living room from the reference image late at night: every lamp switched off, the "
        "room dim and shadowy, lit only by orange street lights and the dark night sky through the net curtains "
        "and the glass balcony door. " + WOMAN_A + "Camera static from the side. She puts the phone face down on "
        "the coffee table, lets out a short dismissive breath through her nose, almost a laugh, and shakes her "
        "head once. She stands up, walks to the glass balcony door and stands there with her back to the "
        "camera, looking out at the dark panel blocks." + STYLE +
        " Sound: a quiet night room, her short breath through the nose, soft footsteps.")),
    "S06b": dict(dur="6", chars=[A], envs=["livingroom"], prompt=(
        "Location: the same living room from the reference image at night, dim street light through the net "
        "curtains. " + WOMAN_A + "Camera static from the side. She walks back from the balcony door to the sofa, "
        "hesitates for a moment standing beside it, then picks up the phone from the coffee table, turns it "
        "over so the screen lights her face, and sits down, reading." + STYLE +
        " Sound: a quiet night room, soft footsteps; she stays silent.")),
    "S07a": dict(dur="6", chars=[], envs=[], prompt=(
        "Cross-section of human skin showing its layers, drawn in thin lines. A small round pale dusty-pink "
        "patch is placed gently on top of the skin. Tiny soft pink dots slowly travel from the patch down "
        "through the skin layers into a red blood vessel at the bottom and drift along with the blood flow."
        + ANIM)),
    "S07b": dict(dur="6", chars=[], envs=[], prompt=(
        "A simple diagram from left to right: a plate icon on the left, an arrow pointing to a line graph whose "
        "curve rises steeply into a tall sharp peak, then an arrow pointing to a small simple outline of a human "
        "body on the right. Slow animation: the curve rises into its sharp peak, and as it does, the belly area "
        "of the body outline gradually fills with soft yellow." + ANIM)),
    "S07c": dict(dur="4", chars=[], envs=["s07b_frame"], prompt=(
        "Use the reference image for the exact layout, size and drawing style: the same row in the middle of "
        "the frame with an icon on the left, an arrow, the graph axes, an arrow and the human body outline on "
        "the right. In this version the icon on the left is a small round pale dusty-pink patch. The curve in "
        "the graph slowly draws itself as a low, flat, gentle wave along the bottom of the axes. The belly area "
        "of the body outline is clean and empty, the same plain cream as the background, and stays that way. "
        "Gentle, calm, slow animation." + ANIM)),
    "S08": dict(dur="6", chars=[A], envs=["kitchen"], prompt=(
        "Location: the kitchen from the reference image, late evening, dark outside the window, warm light from "
        "the single ceiling lamp. " + WOMAN_A + "Camera static from the side at table height. She sits at the "
        "table with the floral oilcloth holding her phone, typing slowly with one finger. She pauses, gives a "
        "very small shrug with one shoulder, taps the screen once, puts the phone down on the table and rests "
        "both hands flat on the table. She sits still." + STYLE + SOUND)),
    "S09a": dict(dur="6", chars=[B], envs=["hallway"], prompt=(
        "Location: the same entry hallway from the reference image with the tall wooden-framed mirror and the "
        "coat hooks, the same grey morning light from the kitchen door. " + WOMAN_B + "Camera 3 metres behind "
        "her at chest height, slightly to the side; we see her back and her face in the mirror. She stands "
        "facing the mirror, pulling the navy blouse over her head and down. The blouse falls loosely over her "
        "body and she leaves it as it is. She pauses and looks at herself in the mirror for two seconds, her "
        "face neutral but softer. Then she takes the black handbag from the coat hook." + STYLE + SOUND)),
    "S09b": dict(dur="6", chars=[B], envs=["kitchen", "patch"], prompt=(
        "Location: the kitchen from the reference image in the morning, natural daylight through the net "
        "curtains. " + WOMAN_B + "Camera static from the side. She stands upright with her shoulders back next "
        "to the gas stove. She holds a white cup in her left hand, the inside of her bare left forearm turned "
        "toward the camera, and pours coffee into it from a metal moka pot held in her right hand. On the inside "
        "of her left forearm, below the rolled sleeve, sits " + PATCH + ": small, softly focused, quietly "
        "noticeable as she pours." + STYLE + " Sound: coffee pouring, quiet morning kitchen; she stays silent.")),
    "S09c": dict(dur="6", chars=[B], envs=["balcony"], prompt=(
        "Location: the balcony from the reference image, morning sun. " + WOMAN_B + "Camera static inside the "
        "room, looking out through the open balcony door. She stands at the railing holding a coffee cup with "
        "both hands, looking out over the panel buildings; we see her back and her profile. She is calm and "
        "still, takes a slow breath and a small sip." + STYLE +
        " Sound: soft morning city ambience, distant birds; she stays silent.")),
    "S10": dict(dur="8", chars=[B], envs=["hallway"], prompt=(
        "Location: the entry hallway from the reference image with the brown front door at the far end. "
        + WOMAN_B + "Camera static at the other end of the hallway at chest height. The shot opens with her "
        "inside the apartment, standing at the closed front door with her back to the camera and her black "
        "handbag on her shoulder. She opens the door outward and steps into the doorway. She stops, turns her "
        "head back over her shoulder and looks directly into the camera for one second with a small "
        "closed-mouth smile, then steps out of the apartment and the door closes behind her. The hallway stays still and empty. Observational documentary style, fixed "
        "locked-off shot, natural available light, muted grey-beige palette, realistic unedited footage, "
        "natural real-time speed, vertical 9:16." + " Sound: the door opening and closing, quiet hallway; she "
        "stays silent.")),
}


def run(arg):
    name, _, var = arg.partition(":")
    s = SCENES[name]
    inp = {
        "prompt": s["prompt"],
        "duration": s["dur"],
        "aspect_ratio": "9:16",
        "resolution": RES,
    }
    if s["chars"]:
        inp["character_ids"] = s["chars"]
    if s["envs"]:
        inp["image_urls"] = [ENV[e] for e in s["envs"]]
    tid = kie.create(MODEL, inp)
    print(arg, "task", tid, flush=True)
    d = kie.wait(tid, every=15, timeout=3600)
    rec = {"name": arg, "taskId": tid, "state": d["state"], "credits": d.get("creditsConsumed"),
           "fail": d.get("failMsg"), "urls": kie.result_urls(d)}
    if rec["urls"]:
        kie.download(rec["urls"][0], os.path.join(CLIPS, f"{name}_{var}.mp4" if var else f"{name}.mp4"))
    print(json.dumps(rec, ensure_ascii=False), flush=True)
    with open(os.path.join(CLIPS, "clips_log.jsonl"), "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


if __name__ == "__main__":
    names = sys.argv[1:] or list(SCENES)
    with ThreadPoolExecutor(min(len(names), 8)) as ex:
        list(ex.map(run, names))
