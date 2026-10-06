"""Shots for the banitsa 3D medical explainer (Gemini Omni 1.1 Flash on kie.ai).

Each voice paragraph (P01..P21) is covered by several short, dynamic shots so the cut can change
every few seconds. Prompts are positive-only (the user's rule). Usage: python3 gen_scenes.py 01a 02b ...
A ":tag" suffix makes a variant file, e.g. 01a:v2 -> clips/01a_v2.mp4.
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

REF = {
    "figure": "https://tempfile.aiquickdraw.com/workers/images/image_f0776be5a161e5d6cf0d9893d80aec00.jpg",
    "kitchen": "https://tempfile.aiquickdraw.com/workers/images/image_570bd7245c11b695923e87be049c88c2.jpg",
    "banitsa": "https://tempfile.aiquickdraw.com/workers/images/image_c6cf886c2543d7ee70b9a4275a831894.jpg",
    "patch": "https://tempfile.redpandaai.co/kieai/1137735/fitpatches/refs/patch_real_crop.jpg",
}

# The user's style prefix; "no text, no labels, no logos" is phrased positively.
PREFIX = (
    "Cinematic 3D medical animation, photorealistic render, Octane/Unreal quality, soft volumetric lighting, "
    "shallow depth of field, dark navy background, accent colors: warm amber for blood and energy, bright "
    "yellow for glucose, soft pink (#d64d87) for the patch and ingredients, cold blue for insulin, 9:16 "
    "vertical, clean imagery made only of 3D forms, light and particles. "
)
FIG = (
    "The translucent female figure from the reference image: a 3D stylized woman of about 50 with a soft "
    "rounded silhouette, made of semi-translucent frosted glass with a faint warm inner glow, wearing a simple "
    "loose knee-length dress of the same frosted glass, smooth featureless face, hair in a simple low bun. "
)
SOUND = " Sound: a soft deep cinematic ambience."


def shot(dur, refs, text):
    return dict(dur=str(dur), refs=refs, prompt=PREFIX + text + SOUND)


SHOTS = {
    # P01 8:00 — morning, banitsa and coffee
    "01a": shot(6, ["kitchen", "figure", "banitsa"],
                "Dynamic opening: the camera glides fast and smoothly through the 3D kitchen from the reference image "
                "in soft morning light, sweeping low over the wooden table and slowing down on a steaming coffee cup "
                "and a plate with a square slice of golden flaky banitsa like in the reference image. " + FIG +
                "She sits down at the table."),
    "01b": shot(6, ["kitchen", "figure", "banitsa"],
                FIG + "Close macro shot: her glass hand lifts the slice of golden flaky banitsa from the plate, thin "
                "phyllo flakes falling in slow motion through the morning light beams. The camera pushes in fast "
                "toward the crisp layered pastry until it fills the frame."),
    # P02 white flour -> sugar in minutes
    "02a": shot(6, ["banitsa"],
                "The camera flies like a drone through the inside of the golden flaky banitsa pastry: thin layers "
                "rise like glowing canyon walls, then peel apart and break up into thousands of small white "
                "starch crystals floating in dark navy space."),
    "02b": shot(6, [],
                "Extreme close-up of long chains of white starch molecules floating in dark navy space. The chains "
                "snap apart link by link in a fast chain reaction, and every released link ignites into a bright "
                "glowing yellow glucose particle. Quick orbit around the reaction."),
    "02c": shot(6, [],
                "Thousands of bright glowing yellow glucose particles swirl into a spiraling vortex in dark navy "
                "space, spinning faster and faster, light trails streaking, the camera rising up through the center "
                "of the vortex."),
    # P03 8:20 — the spike
    "03a": shot(6, [],
                "First-person flight forward inside a human blood vessel, red blood cells drifting calmly past the "
                "camera in warm amber light, soft rhythmic pulse of the vessel walls."),
    "03b": shot(6, [],
                "Inside a human blood vessel in warm amber light: suddenly a huge wave of bright glowing yellow "
                "glucose particles rushes in from behind the camera and floods the vessel, camera shake, chaotic "
                "swirl, the vessel walls flash alarm red."),
    # P04 pancreas, insulin
    "04a": shot(6, [],
                "Slow dramatic orbit around a human pancreas glowing softly and pulsing like a heartbeat, releasing "
                "streams of small cold blue insulin particles like a glowing swarm into a nearby blood vessel full of "
                "yellow glucose."),
    "04b": shot(6, [],
                "Macro on the surface of a body cell: cold blue insulin particles shaped like little keys dock onto "
                "glowing locks on the cell wall, the cell wall opens like a door and yellow glucose particles are "
                "pulled inside, the cell lights up from within as it fills."),
    "04c": shot(6, [],
                "A blood vessel flooded with more and more cold blue insulin particles pouring in from the pancreas, "
                "a dense blue storm, the camera pulling back fast to show the overwhelming amount."),
    # P05 the trap, 10:30
    "05a": shot(6, [],
                "The same blood vessel now empty of yellow particles, blue insulin particles still pulling, the light "
                "shifts to a cold dim blue, red blood cells move sluggishly, the camera drifts slowly, heavy quiet mood."),
    "05b": shot(6, ["kitchen", "figure"],
                FIG + "She stands in the kitchen from the reference image. In front of her floats a glowing pink line-graph "
                "hologram: the line rises into a sharp peak and then sinks below a faint glowing baseline. The camera "
                "pushes in slowly toward the hologram."),
    # P06 brain, hunger
    "06a": shot(6, [],
                "A human brain floating in dark navy space, slow orbit; deep in its center a small red point pulses "
                "faster and brighter, sending red shockwaves rippling outward through the brain."),
    "06b": shot(8, ["kitchen", "figure"],
                FIG + "In the kitchen from the reference image she opens the wall cabinet; the shelves glow warmly; she "
                "reaches in and takes a sweet pastry. Camera from the side, gentle dolly."),
    # P07 multiply: x3 a day, x10 years
    "07a": shot(6, [],
                "A wall calendar in dark navy space, its pages tearing off and flipping away rapidly, months and years "
                "flying past, light flickering between day and night."),
    "07b": shot(8, [],
                "A glowing pink jagged line of sharp peaks and drops races across dark navy space and repeats again "
                "and again; the camera pulls back fast to reveal thousands of these spike lines stacked into a "
                "gigantic glowing wall."),
    # P08 insulin resistance
    "08a": shot(6, [],
                "Close-up of muscle cells already packed full of glowing yellow particles. Cold blue insulin particles "
                "knock against the cell walls and bounce off; the cells stay sealed shut."),
    "08b": shot(8, [],
                "Inside a blood vessel a traffic jam builds: yellow glucose particles crowd and pile up while more and "
                "more cold blue insulin particles stream in, congestion growing, the camera pushing through the crowd."),
    # P09 storage hormone, visceral fat
    "09a": shot(8, [],
                "A glowing transparent 3D medical model of the human abdomen floating in dark navy space, the camera "
                "flying in through it: the liver glows softly, bright yellow particles stream into the liver and come "
                "out as yellow fat droplets."),
    "09b": shot(8, [],
                "Slow orbit around a transparent 3D medical model of the human abdomen: yellow fat droplets attach "
                "around the internal organs deep inside, the fat layer growing thicker with each pass, the middle "
                "becoming dense and firm."),
    # P10 the fat is a gland
    "10a": shot(8, [],
                "A transparent 3D medical model of the human abdomen in dark navy space: the thick visceral fat layer "
                "around the organs pulses faintly red like a living gland and releases fine red particles that travel to "
                "the heart and through the blood vessels; the vessels narrow slightly."),
    "10b": shot(8, ["kitchen", "figure"],
                FIG + "She sits slumped at the kitchen table from the reference image in flat afternoon light, her inner "
                "glow dimming slowly, heavy clinical mood. Slow push-in."),
    # P11 life shrinks
    "11a": shot(6, ["figure"],
                FIG + "A 3D living room in grey afternoon light: she lies on a sofa under a blanket holding a glowing "
                "phone, completely still, net curtains moving slightly. Wide static shot, muted and lonely."),
    "11b": shot(6, [],
                "A 3D shelf in a dim grey living room: the camera slides slowly past a framed photo of a sunny sea beach "
                "lying face down beside a closed swimsuit bag gathering dust, muted lonely mood."),
    # P12 the problem is speed; nature
    "12a": shot(6, [],
                "A single glowing pink line on dark navy space: a tall sharp peak slowly melts and reshapes into a "
                "soft gentle hill, smooth elegant motion, light glinting along the line."),
    "12b": shot(6, [],
                "3D rendered ancient forest, sunlight breaking through green leaves in golden beams, dust and pollen "
                "floating in the light, the camera gliding forward between the trees, warm and peaceful."),
    "12c": shot(6, [],
                "An old village kitchen with bunches of dried herbs hanging on a string by a small window, warm "
                "afternoon light, slow pan along the herbs, dust in the light."),
    # P13 berberine
    "12d": shot(6, [],
                "A fast highway of bright glowing yellow glucose particles racing past the camera through dark navy "
                "space with long motion-blur light trails, then the whole stream slows down smoothly into a calm, "
                "gentle flow."),
    "12e": shot(6, [],
                "Old wrinkled hands of a village herbalist grinding dried herbs and roots in a stone mortar by warm "
                "candle light, golden dust rising, slow cinematic push-in, timeless feeling."),
    "13a": shot(6, [],
                "3D macro of a Berberis vulgaris branch with bright red oval berries and sharp thorns, dew drops, "
                "dramatic orbit around the branch on a dark navy background."),
    "13b": shot(6, [],
                "Cross-section of a berberis root with glowing golden-yellow wood rings; one drop of bright yellow sap "
                "forms and falls in slow motion, catching the light."),
    "13c": shot(8, [],
                "A single muscle cell, sealed shut. Golden-yellow berberine particles arrive and light up a glowing "
                "enzyme core inside the cell; the cell wall softens and opens; yellow glucose particles flow inside and "
                "burst into small flashes of energy light as they are burned."),
    "13d": shot(6, [],
                "A glowing pink line graph on dark navy space beside a golden glow: a sharp tall peak deflates smoothly "
                "into a low rounded hill and then flows on calmly."),
    # P14 cinnamon
    "13e": shot(6, [],
                "Inside a muscle cell: a glowing golden enzyme core switches on like a power switch, energy waves ripple "
                "outward through the cell, and stored yellow glucose particles are drawn in and turned into bright "
                "sparks of energy. Dynamic orbit."),
    "14a": shot(6, [],
                "3D macro of cinnamon sticks on a dark surface; one stick breaks slowly in slow motion and fine "
                "cinnamon powder falls through warm light beams."),
    "14b": shot(8, [],
                "Inside a stomach: white starch particles being cut apart by small round enzyme shapes; warm "
                "cinnamon-colored particles arrive, the enzymes slow down, the starch stays whole longer and drifts "
                "out slowly in a thin calm stream."),
    "14c": shot(6, [],
                "A glass hourglass in dark navy space filled with glowing yellow glucose sand; the falling stream "
                "slows down to a thin calm trickle, the camera orbiting slowly around it."),
    # P15 pomegranate
    "14d": shot(6, [],
                "Two streams of glowing yellow glucose side by side in dark navy space: on the left a violent spiky "
                "torrent crashing down, on the right a slow calm thin golden stream flowing gently; the camera "
                "glides from left to right."),
    "15a": shot(8, [],
                "3D macro of a pomegranate breaking open in slow motion, ruby seeds spilling, one drop of juice falling, "
                "strong backlight on a dark navy background."),
    "15b": shot(8, [],
                "Inside a blood vessel whose walls glow irritated red; deep red pomegranate particles flow through and "
                "the irritation fades into a healthy pale pink glow. Calm forward camera flight."),
    # P16 three plants, one circle
    "15c": shot(6, [],
                "Macro on a blood vessel wall with fine glowing cracks; deep ruby pomegranate particles settle into the "
                "cracks and seal them with a soft pink light, the wall becoming smooth and healthy. Slow orbit."),
    "16a": shot(10, [],
                "3D still life on a dark navy background: a berberis branch with red berries, three cinnamon sticks "
                "and half a pomegranate side by side, dramatic side light, slow push-in. Three thin glowing pink lines "
                "rise from them, swirl together and merge into one glowing pink circle."),
    # P17 the pill problem
    "17a": shot(8, [],
                "A white capsule falls into a translucent stomach and dissolves; most of its particles turn into grey "
                "mist and fade inside the stomach and the liver, and only a thin stream reaches a red blood vessel. "
                "Cool clinical tones."),
    "17b": shot(6, ["figure"],
                FIG + "She stands at a medium distance with one hand resting on her stomach; a faint grey mist swirls "
                "inside her frosted glass dress at that spot; cool clinical light, slow gentle camera drift."),
    # P18 through the skin
    "17c": shot(6, [],
                "A handful of white capsules pouring in slow motion onto a dark glossy surface, bouncing and rolling, "
                "cold clinical light, the camera tracking low along them."),
    "17d": shot(6, [],
                "A glowing human liver in dark navy space: streams of golden particles enter it and are broken down "
                "into grey dust that drifts away, only a few golden particles pass through. Slow orbit."),
    "18a": shot(10, ["patch"],
                "Cross-section of human skin layers in cool blue tones; a small round translucent soft-pink patch like "
                "the reference image rests on the surface; tiny glowing pink particles drift slowly and evenly down "
                "through the epidermis and dermis into a red blood vessel, steady calm motion."),
    "18b": shot(6, [],
                "A glowing ring-shaped 24-hour dial in dark navy space with a steady soft pink light flowing evenly "
                "around it in one smooth continuous loop, beside it a pink line that stays perfectly flat and level."),
    # P19 FitPatches combines the three
    "18c": shot(8, ["figure", "patch"],
                FIG + "Seen in profile on a dark navy background, a small round translucent soft-pink patch like the patch "
                "reference glows steadily on her upper arm, while the light around her turns from morning to midday to "
                "evening to night in a smooth time-lapse; the soft pink glow stays even the whole time."),
    "19a": shot(6, ["patch"],
                "Three streams of glowing particles, golden-yellow, warm cinnamon-brown and deep ruby red, spiral "
                "together in dark navy space and condense into one round translucent soft-pink patch exactly like the "
                "reference image, which turns slowly toward the camera with a soft glow."),
    "19b": shot(8, ["kitchen", "figure", "patch"],
                FIG + "In the kitchen from the reference image in morning light she peels a small round translucent "
                "soft-pink patch like the patch reference from a white backing sheet and presses it onto her upper arm; "
                "the patch glows softly and a faint pink pulse travels into her arm and through her body. Slow push-in "
                "on the patch."),
    "19c": shot(6, ["kitchen", "figure", "banitsa"],
                FIG + "Sitting at the kitchen table from the reference image she picks up her coffee; the slice of "
                "banitsa from the reference image is on the plate in front of her; calm warm morning light; a small "
                "pink patch glows softly on her upper arm."),
    # P20 10:30, no crash
    "20a": shot(8, ["kitchen", "figure"],
                FIG + "The kitchen from the reference image in bright daylight: she sits at the table working on a "
                "laptop, half a cup of coffee beside her, the wall cabinet behind her closed. A small floating hologram "
                "of a calm flat pink line glows steadily above the table. Her attention stays on the laptop. Camera "
                "static."),
    "21a": shot(8, ["kitchen", "patch"],
                "Premium 3D product shot on the wooden table of the kitchen from the reference image in soft morning "
                "window light: three round translucent soft-pink patches exactly like the patch reference fanned out "
                "beside a steaming coffee cup, slow camera orbit, shallow depth of field, elegant highlights."),
}


def run(arg):
    name, _, var = arg.partition(":")
    s = SHOTS[name]
    inp = {"prompt": s["prompt"], "duration": s["dur"], "aspect_ratio": "9:16", "resolution": RES}
    if s["refs"]:
        inp["image_urls"] = [REF[r] for r in s["refs"]]
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
    names = sys.argv[1:] or list(SHOTS)
    with ThreadPoolExecutor(min(len(names), 8)) as ex:
        list(ex.map(run, names))
