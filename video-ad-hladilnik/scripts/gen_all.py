"""Fridge ad 'Аз съм хладилникът на Ивайла': Nano Banana Pro refs -> Gemini Omni 1.1 Flash shots (kie.ai).
Positive-only prompts. Usage: python3 gen_all.py [refs] [shots names...]"""
import json, os, sys
from concurrent.futures import ThreadPoolExecutor
import kie

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
REFS, CLIPS = os.path.join(ROOT, "refs"), os.path.join(ROOT, "clips")
REFJSON = os.path.join(REFS, "refs.json")
PATCH = "https://tempfile.redpandaai.co/kieai/1137735/fitpatches/refs/patch.jpg"

IVAILA = ("a Bulgarian woman of 45 with a full, heavy figure (around 85 kg), round soft face, chestnut "
          "shoulder-length hair, kind brown eyes, wearing a faded pink cotton home t-shirt and grey home trousers")
REF_JOBS = {
    "ivaila_before": ([], f"Realistic candid photo of {IVAILA}, standing in an ordinary Bulgarian panel-block "
        "apartment kitchen in the evening, warm tungsten light, natural skin texture, documentary style, "
        "medium full-body shot, vertical 9:16."),
    "kitchen_pov": ([], "Realistic photo taken from inside an open old white refrigerator looking out into a "
        "small Bulgarian panel-block apartment kitchen at night: in the foreground the fridge shelves with a jar "
        "of lutenitsa, a block of yellow kashkaval, white sirene cheese in a box, a cooking pot and a chocolate "
        "cake on a plate; beyond the open door a dim kitchen with beige tiles, a wooden table and an oven with a "
        "glowing clock; cold white fridge light spilling into the dark room, cinematic, vertical 9:16."),
}

def nb(prompt, imgs):
    tid = kie.create("nano-banana-pro", {"prompt": prompt, "image_input": imgs, "aspect_ratio": "9:16",
                                         "resolution": "2K", "output_format": "jpg"})
    d = kie.wait(tid, every=8)
    u = kie.result_urls(d)
    if not u: raise RuntimeError(f"ref failed {d.get('failMsg')}")
    return u[0]

def make_refs():
    refs = json.load(open(REFJSON)) if os.path.exists(REFJSON) else {}
    with ThreadPoolExecutor(2) as ex:
        futs = {n: ex.submit(nb, p, i) for n, (i, p) in REF_JOBS.items() if n not in refs}
        for n, f in futs.items(): refs[n] = f.result(); print("ref", n, refs[n], flush=True)
    if "ivaila_after" not in refs:
        refs["ivaila_after"] = nb("The same woman from the reference image, same face, same hair colour, a few "
            "months later: visibly slimmer, about 15 kg lighter, a clearly slimmer face with a defined jawline, "
            "slimmer arms, a narrower waist and a flatter belly, healthy glowing skin, calm confident smile, hair neatly "
            "tied back, wearing a fitted light-blue cotton t-shirt tucked into dark slim trousers, the same kitchen in "
            "soft morning daylight, realistic candid photo, vertical 9:16.",
            [refs["ivaila_before"]]); print("ref ivaila_after", refs["ivaila_after"], flush=True)
    refs["patch"] = PATCH
    json.dump(refs, open(REFJSON, "w"), indent=1)
    for n, u in refs.items():
        p = os.path.join(REFS, n + ".jpg")
        if not os.path.exists(p): kie.download(u, p)
    return refs

LOOK = ("Realistic cinematic footage, natural film look, 9:16 vertical. The camera is inside the refrigerator, "
        "looking out through the open door between the shelves of food, like the reference kitchen image. ")
BEFORE = f"The woman is Ivaila from the reference image: {IVAILA}. "
AFTER = ("The woman is Ivaila from the reference image: visibly slimmer than before, slim face, slim arms, narrow "
         "waist, calm and confident, hair neatly tied back, fitted light-blue cotton t-shirt tucked into dark slim trousers. ")
SHOTS = {  # name: (seconds, refs, prompt) — line of the voice it plays under
    "s01": (6, ["kitchen_pov", "ivaila_before"], LOOK + BEFORE + "Morning: darkness inside the fridge, then the "
        "door swings open and cold light floods the shelves. Ivaila, sleepy, in the morning light of the kitchen, "
        "leans in, looks over the shelves with a warm familiar smile and takes the jar of milk. Sound: fridge hum, "
        "the soft suck of the door seal."),  # Аз съм хладилникът… Петнайсет години… Сутрин
    "s02": (6, ["kitchen_pov", "ivaila_before"], LOOK + BEFORE + "Evening, warm kitchen light behind her: Ivaila "
        "opens the door, takes out the cooking pot with both hands, then grabs a block of kashkaval too and closes "
        "the door with her hip. Sound: fridge hum, kitchen clatter."),  # На обед. Вечер.
    "s03": (8, ["kitchen_pov", "ivaila_before"], LOOK + BEFORE + "Late night, the kitchen dark, only the oven clock "
        "glowing 23:00. The door opens and the fridge light falls on Ivaila in a long cotton home robe. She smiles "
        "like meeting an old friend, takes the chocolate cake, cuts a piece with a spoon right there and eats it "
        "with pleasure, eyes half closed. Sound: quiet night, fridge hum."),  # ритуал… и два пъти
    "s04": (6, ["kitchen_pov", "ivaila_before", "patch"], LOOK + BEFORE + "Morning daylight. Ivaila opens the door "
        "and reaches for the yogurt on the top shelf; her short sleeve slides up and on her upper arm there is one "
        "round translucent soft-pink patch exactly like the patch reference, clearly visible in the fridge light. "
        "She takes the yogurt and closes the door. Sound: fridge hum."),  # Една сутрин… на ръката ѝ
    "s05": (10, ["kitchen_pov"], "Realistic cinematic footage, 9:16 vertical. A small Bulgarian panel-block kitchen "
        "at night seen from the fridge, like the reference image, the fridge door closed and the room in deep blue "
        "darkness. The glowing oven clock reads 23:00, then 23:15, then 23:45. Time passes: moonlight from the window "
        "slides slowly across the empty table and the floor. The kitchen stays still and quiet. Sound: a clock "
        "ticking, distant city night."),  # Онази вечер я чаках… Нищо. И на другата…
    "s06": (10, ["ivaila_before", "patch"], "Realistic cinematic footage, 9:16 vertical, soft morning window light in "
        "a Bulgarian apartment kitchen. Close-up: Ivaila from the reference image presses one round translucent "
        "soft-pink patch with a clear frosted rim and the curved text 'Fit Patches *' printed in dark pink around its "
        "edge, exactly like the patch reference, onto her upper arm, smooths it with two fingers and "
        "smiles to herself. Slow push-in on the patch on her skin. Sound: quiet morning room tone."),  # Слага си лепенки…
    "s07": (8, ["kitchen_pov", "ivaila_after"], "Realistic cinematic footage, 9:16 vertical. Evening in the small "
        "Bulgarian kitchen from the reference image. " + AFTER + "She finishes a small plate of salad at the table, "
        "relaxed, glances at the fridge for a moment, smiles calmly, switches off the kitchen light and walks out of "
        "the room. Sound: quiet evening room tone."),  # яде по-малко… не я тегли към мен
    "s08": (8, ["kitchen_pov", "ivaila_after"], LOOK + AFTER + "Bright morning sunlight in the kitchen. The door "
        "opens, Ivaila leans in with a light, rested face and a calm smile, takes a small bowl of yogurt with "
        "berries, and the camera lingers on her relaxed, lighter look. Sound: fridge hum, birds outside."),  # Сега идва… По-лека.
    "s09": (6, ["kitchen_pov", "ivaila_after"], LOOK + AFTER + "Evening. Ivaila takes a bottle of water, gives the "
        "shelves a soft, almost tender look, and gently closes the door. The view goes dark; the fridge light "
        "blinks once softly in the darkness. Sound: the soft thud of the door, a quiet hum."),  # Липсва ми… радвам се
    "s10": (4, ["patch"], "Realistic premium product footage, 9:16 vertical: round translucent soft-pink patches "
        "with a clear frosted rim and the curved text 'Fit Patches *' printed in dark pink around the edge, exactly like the patch reference, lying on a light wooden kitchen counter next to cinnamon sticks, a halved "
        "red pomegranate with glossy seeds and a small bowl of yellow barberry roots, soft morning light, slow "
        "camera push-in. Sound: soft warm ambience."),  # ФитПачес. Берберин, канела и нар.
}

def shot(name, refs):
    sec, r, prompt = SHOTS[name]
    inp = {"prompt": prompt, "duration": str(sec), "aspect_ratio": "9:16", "resolution": "720p",
           "image_urls": [refs[x] for x in r]}
    tid = kie.create("google/gemini-omni-flash-1-1", inp); print(name, "task", tid, flush=True)
    d = kie.wait(tid, every=15, timeout=3600)
    rec = {"name": name, "taskId": tid, "state": d["state"], "credits": d.get("creditsConsumed"),
           "fail": d.get("failMsg"), "urls": kie.result_urls(d)}
    if rec["urls"]: kie.download(rec["urls"][0], os.path.join(CLIPS, name + ".mp4"))
    print(json.dumps(rec, ensure_ascii=False), flush=True)
    with open(os.path.join(CLIPS, "clips_log.jsonl"), "a") as f: f.write(json.dumps(rec, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    refs = make_refs()
    names = [a for a in sys.argv[1:] if a != "refs"] or list(SHOTS)
    if sys.argv[1:] == ["refs"]: sys.exit()
    with ThreadPoolExecutor(len(names)) as ex: list(ex.map(lambda n: shot(n, refs), names))
