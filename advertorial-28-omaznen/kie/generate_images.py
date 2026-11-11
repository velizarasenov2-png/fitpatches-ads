"""Images for advertorial-28-omaznen on kie.ai (Nano Banana Pro). Raw output: kie/raw/<name>-raw.jpg

    python3 kie/generate_images.py              # all
    python3 kie/generate_images.py jeans        # one
The kie.ai key is injected by the session proxy; outside it, export KIE_API_KEY.
"""
import json, os, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

API = "https://api.kie.ai/api/v1/jobs"
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw")
NO_TEXT = " Absolutely no text, letters, numbers, labels, logos or watermarks anywhere in the image."
PATCH = "https://cdn.shopify.com/s/files/1/1019/0929/9545/files/fp-patch-real.png?v=1785852731"
PATCH_LOOK = (" The patch must look exactly like the reference photo: a thin round translucent dusty-pink patch the size "
              "of a coin with a thin ring of tiny print around its edge.")
ILLU = " Clean semi-realistic medical illustration in a bright educational health-magazine infographic style."

JOBS = {
    "jeans": (
        "Realistic close-up candid phone photo, shot from slightly above, of a Bulgarian woman around 50 standing in "
        "her bedroom trying to button her blue jeans: both hands pull the waistband together but the metal button "
        "stays about four centimetres away from the buttonhole and cannot reach, her soft round belly pushes forward "
        "under a pale knitted sweater that is lifted a little. Behind her an unmade bed covered with a pile of "
        "tried-on clothes. Soft grey morning window light, real life, unposed, slightly frustrated mood." + NO_TEXT,
        "4:3", []),
    "fitting_room": (
        "Realistic candid photo inside a small shopping-mall fitting room with a large mirror and harsh overhead "
        "fluorescent light. A Bulgarian woman around 50 with a full figure and a round belly, short dark-blonde hair, "
        "is trying on an elegant dark-red evening dress that will not zip up: the zipper at her back gapes open in a "
        "wide V. She holds the dress at her waist with both hands and looks at her reflection with tired, teary eyes. "
        "Two more dresses hang on hooks on the wall, her winter coat and handbag lie on a small stool. Emotional, "
        "real life, shot on a phone." + NO_TEXT, "4:3", []),
    "closet_tags": (
        "Realistic photo of an open wardrobe in a Bulgarian bedroom. On the left side hangs a row of beautiful "
        "fitted clothes that were never worn: a fitted dress, slim jeans, a tailored blazer, a silk blouse, many "
        "still with blank paper price tags dangling from them. On the right side hang a few large dark shapeless "
        "tunics and stretchy black trousers that are clearly worn every day. A rolled measuring tape lies on the "
        "shelf. Soft daylight, quiet, slightly sad mood." + NO_TEXT, "4:3", []),
    "failed_grid": (
        "A 3x2 photo collage with thin white borders between the six equal panels, bright realistic stock "
        "photography. Panel 1: a beige shapewear body shaper laid flat on a bed. Panel 2: a protein shake shaker "
        "and a powder tub with a scoop on a kitchen counter. Panel 3: a glass cup of herbal detox tea with loose "
        "tea bags. Panel 4: a plain jar of slimming cream next to a roll of plastic cling film on a bathroom shelf. "
        "Panel 5: an open hand holding colourful diet capsules spilling from an orange pharmacy bottle. Panel 6: an "
        "empty gym with treadmills and a lonely membership card on a bench." + NO_TEXT, "3:2", []),
    "fat_muscle": (
        "Realistic educational studio photo of two anatomical replica models used by dietitians, side by side on a "
        "clean white table: on the left a large lumpy pale-yellow model of one kilogram of human body fat, on the "
        "right a much smaller, compact, dark-red model of one kilogram of muscle with visible fibres. They weigh the "
        "same, but the fat model is clearly much bigger in volume. A yellow measuring tape lies curled in front of "
        "them. Plain light grey background, soft studio light, high detail." + NO_TEXT, "16:9", []),
    "pear_apple": (
        "Two side-by-side front-view female body figures on a light beige background, separated by a thin vertical "
        "line." + ILLU + " LEFT: a woman around 35 with a pear-shaped figure, her body fat shown as a soft yellow "
        "overlay mainly on the hips, buttocks and thighs, the waist narrow. RIGHT: the same woman around 52, about "
        "the same overall size, but the yellow fat has moved to the belly and deep inside the abdomen around the "
        "organs, the waist now wide and round like an apple, the hips slightly smaller. Both wear simple grey "
        "underwear, neutral friendly faces. Leave empty space in the bottom fifth for labels." + NO_TEXT, "16:9", []),
    "nye_finale": (
        "Realistic warm candid photo of a New Year's Eve family celebration in a Bulgarian living room with a "
        "decorated Christmas tree and warm string lights. A happy, confident woman around 50 with a full but healthy "
        "figure, wearing an elegant fitted emerald-green dress, laughs while dancing hand in hand with her husband; "
        "family members clap around them, a teenage granddaughter holds a sparkler, a festive table in the "
        "background. Joyful, real life, shot on a phone." + NO_TEXT, "4:3", []),
    "dress_door": (
        "Realistic calm morning photo in a Bulgarian bedroom: an elegant emerald-green dress on a hanger hooked on "
        "the open door of a wardrobe, soft sunlight through sheer curtains. On the wooden dresser below: a cup of "
        "coffee, a rolled measuring tape and a single round translucent dusty-pink skin patch lying on its backing "
        "film. Hopeful, quiet mood." + PATCH_LOOK + NO_TEXT, "4:3", [PATCH]),
    "liver_hero": (
        "Photorealistic medical 3D render, dramatic studio lighting on a dark charcoal background: two human livers "
        "side by side. LEFT: a healthy liver, smooth glossy deep reddish-brown, normal size, sharp edges. RIGHT: a "
        "fatty liver, visibly swollen and enlarged with rounded blunt edges, pale yellow-beige greasy surface with "
        "yellow fat patches and a mottled texture. Both seen from the front at the same angle and scale, high "
        "detail, educational and striking." + NO_TEXT, "16:9", []),
    "ultrasound_visit": (
        "Realistic candid photo in a Bulgarian doctor's office: an overweight woman around 51 with a round belly, a "
        "full face and short chestnut hair, in a beige cardigan, sits at the desk and holds a folded white A4 paper "
        "medical report in both hands, looking down, ashamed and worried, eyes wet. On the desk in front of her lies "
        "a small grey-scale ultrasound image of an adult liver (a wedge-shaped organ, clearly not a baby). Across "
        "the desk only the forearms of a doctor in a white coat are visible. Cold daylight, simple clinic interior, "
        "emotional real-life moment, shot on a phone. The papers are blank or blurred." + NO_TEXT, "4:3", []),
    "ultrasound_screen": (
        "Realistic close-up photo of a medical ultrasound machine monitor in a dim exam room showing a grey-scale "
        "abdominal ultrasound of a fatty liver: the liver tissue looks unusually bright white and grainy, blurring "
        "the vessels, next to a darker kidney. A gloved hand holds the probe with gel at the bottom of the frame. "
        "Blue-grey light from the screen." + NO_TEXT, "4:3", []),
    "liver_grid": (
        "A 3x2 photo collage with thin white borders between the six equal panels, bright realistic stock "
        "photography. Panel 1: blister packs of brown liver-support capsules on a pharmacy counter. Panel 2: purple "
        "milk thistle flowers with a cup of herbal tea and seeds. Panel 3: a glass of warm water with a lemon slice "
        "on a kitchen table in the morning. Panel 4: a row of green and orange detox juice bottles. Panel 5: an "
        "open hand holding yellow herbal capsules. Panel 6: a tiny salad portion on a plate next to a kitchen "
        "scale." + NO_TEXT, "3:2", []),
    "liver_cells": (
        "Microscopic close-up medical illustration of human liver cells (hepatocytes) in a tissue section:" + ILLU +
        " LEFT half: healthy pink-purple polygonal liver cells with round nuclei. RIGHT half: the same cells packed "
        "and swollen with large round glossy yellow fat droplets that push the nuclei to the side. Soft depth of "
        "field." + NO_TEXT, "16:9", []),
    "portal": (
        "Front view anatomical illustration of a woman's abdomen with see-through skin:" + ILLU + " thick yellow "
        "visceral fat wraps the intestines; bright yellow arrows flow upward from this belly fat through a large "
        "blue portal vein straight into the liver, which looks swollen and pale yellow. The heart and lungs are "
        "faint above. Light beige background, high detail." + NO_TEXT, "16:9", []),
    "desk_liver": (
        "Realistic moody photo of a doctor's office desk late at night, no person in frame: a green banker's desk "
        "lamp lighting open medical textbooks with liver anatomy pages, printed research papers with highlighted "
        "lines, a stack of grey-scale abdominal ultrasound printouts, a laptop showing a liver ultrasound, a "
        "stethoscope and a cold cup of coffee. Dark window with city lights. Cinematic warm light." + NO_TEXT,
        "4:3", []),
    "walk_finale": (
        "Realistic warm candid photo on a sunny late-autumn day in a Bulgarian mountain park with golden trees: a "
        "smiling energetic woman around 52 with a healthy full figure, in a light puffer jacket and sneakers, walks "
        "briskly uphill on a trail, laughing and holding hands with her granddaughter of about 7; her husband "
        "follows with a thermos. Joyful, real life, shot on a phone." + NO_TEXT, "4:3", []),

}


def _call(url, data=None):
    req = urllib.request.Request(
        url, data=json.dumps(data).encode() if data is not None else None,
        headers={"Authorization": f"Bearer {os.environ.get('KIE_API_KEY', 'proxy-injected')}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def run(name):
    prompt, ar, refs = JOBS[name]
    inp = {"prompt": prompt, "image_input": refs, "aspect_ratio": ar, "resolution": "2K", "output_format": "jpg"}
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
    with ThreadPoolExecutor(8) as ex:
        for r in ex.map(run, sys.argv[1:] or list(JOBS)):
            print(*r, flush=True)
