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

PATCH = "https://cdn.shopify.com/s/files/1/1019/0929/9545/files/fp-patch-real.png?v=1785852731"
WRIST = "https://cdn.shopify.com/s/files/1/1048/3269/6657/files/ruka_size_new_e633366f-b56d-4632-848c-4885ced7e166.png"
PATCH_LOOK = (" The patch must look exactly like the reference photo: a thin round translucent dusty-pink patch the size "
              "of a coin with a thin ring of tiny print around its edge.")
ILLU = " Clean semi-realistic medical illustration in a bright educational health-magazine infographic style."

# name: (prompt, aspect ratio, reference images). Text is added later in compose_images.py.
JOBS = {
    # first batch (photos)
    "stairs": (
        "Realistic candid phone photo in the stairwell of an old Bulgarian panel apartment block: worn terrazzo "
        "steps, pale green painted walls, a metal railing, a small dusty window. A woman around 50, ordinary "
        "figure with a round belly, in a dark winter coat, has stopped on the landing between floors, one hand "
        "gripping the railing and the other pressed to her chest, catching her breath with her eyes closed and "
        "mouth slightly open. Two full plastic supermarket bags rest on the step beside her. Cold fluorescent "
        "light mixed with grey daylight, real life, unposed." + NO_TEXT, "4:3", []),
    "supplements": (
        "Realistic photo of a Bulgarian kitchen counter crowded with the clutter of years of trying: many plain "
        "unlabeled supplement bottles and jars in different colours, boxes of herbal detox tea without print, a "
        "protein shaker, opened blister packs, a coiled measuring tape, a crumpled printed diet plan with a pen, "
        "a half-eaten bowl of salad. Morning window light, slightly messy, real life." + NO_TEXT, "4:3", []),
    "finale": (
        "Realistic warm candid photo in a bright Bulgarian apartment block stairwell: a smiling woman around 50 "
        "in a light spring coat climbs the last steps to the top-floor landing easily, laughing, holding the hand "
        "of her granddaughter of about 6 who runs ahead of her up the stairs. Sunlight through the window, joyful "
        "real-life family moment, shot on a phone." + NO_TEXT, "4:3", []),

    # second batch: dormo-style illustrations and infographics
    "methods": (
        "A 2x2 photo collage with thin white borders on a light turquoise background, magazine infographic style. "
        "Top left: protein shake tubs, a shaker and a powder scoop on a kitchen counter. Top right: a cup of herbal "
        "detox tea with tea bags and plain tea boxes. Bottom left: a hand holding a pile of colourful diet pills "
        "and capsules spilling from an orange pharmacy bottle. Bottom right: an empty gym with treadmills and a "
        "lonely membership card on a bench. Bright realistic stock photography." + NO_TEXT, "16:9", []),
    "lungs": (
        "Two side-by-side medical illustrations separated by a thin vertical dark line, on a soft beige "
        "background." + ILLU + " LEFT panel: front view of a woman's torso with see-through skin showing large pink "
        "fully expanded healthy lungs, a low relaxed diaphragm and a slim abdomen with very little yellow fat. "
        "RIGHT panel: the same torso view but the abdomen is packed with thick yellow visceral fat around the "
        "organs that pushes the diaphragm high up, the lungs are visibly smaller and squeezed, with small red "
        "irritated glows on them. Leave empty space in the lower third of each panel." + NO_TEXT, "16:9", []),
    "vise": (
        "Side view cross-section of an adult woman's torso on a light grey-white background:" + ILLU + " Pink "
        "lungs in the chest, the dome-shaped diaphragm under them, and the abdominal organs packed in thick "
        "yellow visceral fat. Two large bold red arrows point upward from the fat into the diaphragm, showing "
        "the fat pushing the diaphragm up and squeezing the lungs. Soft lighting, high detail." + NO_TEXT, "16:9", []),
    "second_door": (
        "Pale light-blue medical textbook illustration with delicate line work. In the centre a large 3D "
        "cross-section block of human skin layers (epidermis, dermis with tiny red blood capillaries, a fat "
        "layer) with a thin round pink patch on top, from which tiny glowing yellow particles move down into the "
        "skin and enter the capillaries. On the left side, faded and greyed out: the stomach and the liver. On "
        "the right side, faded and greyed out: the intestines, showing that they are bypassed. High detail."
        + NO_TEXT, "16:9", []),
    "step1": (
        "Square-ish medical illustration on a light grey background:" + ILLU + " A cross-section of skin with a "
        "round pink patch on top and tiny yellow particles entering the skin, while in the background a faded "
        "stomach full of yellow capsules is crossed out with a soft red X." + NO_TEXT, "3:4", []),
    "step2": (
        "Square-ish medical illustration on a light grey background:" + ILLU + " A round pink patch on a "
        "cross-section of skin releasing a slow, steady stream of tiny golden droplets into the skin layers, like "
        "drip irrigation, under a soft arc from a small sun on the left to a small moon on the right showing the "
        "whole day." + NO_TEXT, "3:4", []),
    "step3": (
        "Square-ish illustration on a light grey background:" + ILLU + " A branch of the common barberry shrub "
        "with small green leaves, thorns and red oblong berries, its freshly cut root showing bright lemon-yellow "
        "wood, next to a glowing stylised human cell with a small golden switch lever turned on." + NO_TEXT,
        "3:4", []),
    "phase1": (
        "Bright realistic close-up photo: a woman's hand applying one small round pink patch to the clean skin of "
        "her outer upper arm, soft morning sunlight from a window, bedroom softly blurred behind."
        + PATCH_LOOK + NO_TEXT, "3:4", [PATCH]),
    "phase2": (
        "Realistic candid photo: a smiling woman around 45 at a sunny open-air vegetable market choosing "
        "tomatoes, her sleeve pushed up so one small round pink patch is visible on her forearm, busy daytime."
        + PATCH_LOOK + NO_TEXT, "3:4", [PATCH, WRIST]),
    "phase3": (
        "Realistic close-up photo: fingers peeling a used round pink patch off the skin of a forearm, a fresh new "
        "pink patch still on its clear liner lies next to a cup of coffee on a wooden bedside table, soft early "
        "morning light." + PATCH_LOOK + NO_TEXT, "3:4", [PATCH]),
    "cost": (
        "Clean infographic on a light grey-white background: on the left a long crumpled paper shop receipt with "
        "many faint printed lines and a big bold red diagonal cross over it; in the middle a dark navy circle "
        "with a small white arrow; on the right a white cardboard price tag on a string with a green circle "
        "check mark. Leave clean empty space on the lower part of the receipt and in the middle of the tag."
        + NO_TEXT, "16:9", []),
    "seal": (
        "A shiny embossed gold medal seal on a pure white background, 3D render, thick raised rim with a laurel "
        "pattern and in the centre a raised embossed icon of a delivery van with a hand holding banknotes. "
        "Premium, high detail, soft shadow." + NO_TEXT, "16:9", []),
    "tablet": (
        "Realistic photo: two hands holding a white tablet in front of a softly blurred cosy living room with a "
        "sofa and bookshelves. The tablet screen is completely plain, flat white and blank, facing the camera "
        "straight on with almost no perspective, filling the centre of the frame. Soft daylight." + NO_TEXT,
        "1:1", []),
    "abs_capsule": (
        "Clean semi-realistic medical illustration on a plain very light grey background, front view of a "
        "semi-transparent woman's torso from the mouth to the hips showing the oesophagus, the stomach, the small "
        "intestine and the liver in soft natural colours. A yellow capsule is dissolving inside the stomach and "
        "tiny yellow particles travel on into the intestine and the liver, getting fewer and fainter along the "
        "way, with only a couple of particles reaching a red blood vessel. Educational health infographic style, "
        "high detail." + NO_TEXT, "3:4", []),
    "abs_patch": (
        "Clean semi-realistic medical illustration on a plain very light grey background: a large 3D cross-section "
        "of human skin (epidermis, dermis with a dense network of small red capillaries, fat layer) with a thin "
        "round dusty-pink patch on top. Many tiny glowing golden particles move evenly and steadily from the patch "
        "down through the skin layers and into the capillaries, like a slow drip. Educational health infographic "
        "style, high detail." + NO_TEXT, "3:4", []),
    "hormones": (
        "Realistic candid photo at night in a Bulgarian bedroom lit by a dim bedside lamp: a woman around 50 sits up "
        "in bed, awake, fanning herself with a folded magazine, slightly flushed face, tired eyes, the duvet pushed "
        "aside, a glass of water on the nightstand. Warm low light, real life, unposed." + NO_TEXT, "4:3", []),
    "stress": (
        "Realistic candid photo late in the evening in an ordinary Bulgarian kitchen: a woman around 47 sits at the "
        "table with a laptop, a pile of unopened envelopes and a cold cup of tea, one hand on her forehead, "
        "exhausted, the window dark behind her. Cool overhead light mixed with the warm glow of the laptop, real "
        "life." + NO_TEXT, "4:3", []),
    "map": (
        "Clean stylised flat illustration of the map of Bulgaria in soft white on a pale pink background, with many "
        "small glowing dusty-pink location pins spread across the country (Sofia, Plovdiv, Varna, Burgas, Pleven, "
        "Stara Zagora, Haskovo, Kyustendil, Vratsa, Pazardzhik, Silistra region and smaller towns), a few thin pink "
        "lines connecting them, modern infographic style, lots of air around the map." + NO_TEXT, "16:9", []),
    "courier": (
        "Realistic warm photo at the open door of a Bulgarian apartment: a courier in a plain dark jacket without "
        "any logo hands a small cardboard parcel to a smiling woman around 50 in a cardigan, who holds a few "
        "banknotes in her other hand to pay. Bright hallway, friendly moment, real life, shot on a phone."
        + NO_TEXT, "4:3", []),
    "ingredients": (
        "Bright top-down flat-lay product photo on a soft pale pink marble surface: in the centre one round "
        "translucent dusty-pink skin patch, surrounded by a small barberry branch with red berries and pieces of "
        "bright yellow barberry root, cinnamon sticks, a halved pomegranate with glistening seeds, and a small "
        "ceramic bowl of fine white powder. Soft daylight, gentle shadows, clean premium health style."
        + PATCH_LOOK + NO_TEXT, "4:3", [PATCH]),
    "walk": (
        "Realistic candid photo in a Bulgarian city park in golden autumn: a smiling woman around 50 in a light "
        "jacket, jeans and sneakers walks briskly along a path with fallen yellow leaves, swinging her arms, "
        "breathing easily, morning sun. Real life, shot on a phone." + NO_TEXT, "4:3", []),
    "holiday": (
        "Realistic warm photo of a festive Bulgarian winter holiday table at home, seen from above at an angle: a "
        "whole baked carp on a platter, a pot of stuffed cabbage rolls (sarmi), a round banitsa pastry, a sweet "
        "braided kozunak bread, red wine, candles, a white embroidered tablecloth and several hands reaching for "
        "the food. Cosy candle light, abundance." + NO_TEXT, "4:3", []),
    "measure": (
        "Realistic close-up photo in a bright bathroom: a woman's hands wrapping a soft yellow measuring tape around "
        "her waist over a plain grey t-shirt, at belly-button level, neutral and calm, only the torso and hands in "
        "frame, natural morning light." + NO_TEXT, "4:3", []),
    "doc_selfie": (
        "Realistic casual smartphone photo taken by a male doctor in his own office, point of view: his left forearm "
        "in a rolled-up white doctor's coat sleeve is held up close to the camera, showing one small round "
        "dusty-pink patch stuck on the inside of the forearm. Behind it, slightly out of focus: a framed medical "
        "diploma on the wall with no readable writing, a bookshelf of thick medical books, a desk with a "
        "stethoscope and papers, and a computer monitor that clearly shows a colourful full-body DEXA "
        "body-composition scan split in two (an obese body with lots of yellow fat on the left, a slim body on "
        "the right) like the second reference image. Daylight from a window, ordinary clinic, real life, "
        "slightly imperfect phone framing." + PATCH_LOOK + NO_TEXT, "1:1",
        [PATCH, "https://raw.githubusercontent.com/velizarasenov2-png/fitpatches-ads/4aadeb89539d02ed1ea64869ab8ead8484038b88/advertorial-26-zadahvane/img/hero-dexa.jpg"]),
}


def _call(url, data=None):
    req = urllib.request.Request(
        url, data=json.dumps(data).encode() if data is not None else None,
        headers={"Authorization": f"Bearer {os.environ.get('KIE_API_KEY', 'proxy-injected')}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def run(name, take=1):
    prompt, ar, refs = JOBS[name]
    inp = {"prompt": prompt, "image_input": refs, "aspect_ratio": ar, "resolution": "2K", "output_format": "jpg"}
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
        urllib.request.urlretrieve(urls[0], os.path.join(OUT, "..", "kie", "raw", f"{name}-raw.jpg" if take == 1 else f"{name}-{take}-raw.jpg"))
    return name, d["state"], d.get("failMsg")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    with ThreadPoolExecutor(8) as ex:
        for r in ex.map(run, sys.argv[1:] or list(JOBS)):
            print(*r)
