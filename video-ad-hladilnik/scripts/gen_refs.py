"""References for the fridge ad (Nano Banana Pro on kie.ai)."""
import json, os, sys
from concurrent.futures import ThreadPoolExecutor
import kie
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "refs")
LOOK = "Photorealistic, natural, realistic skin texture, documentary look, vertical 9:16."
JOBS = {
 "ivaila_before": ([], "Full-body photo of a Bulgarian woman, 45 years old, 165 cm, around 85 kg, full round belly, full arms and full round face, shoulder-length chestnut brown hair, kind tired face, no makeup, wearing a soft faded pink home t-shirt and grey home trousers, standing in an ordinary Bulgarian apartment kitchen, soft evening lamp light. " + LOOK),
 "kitchen_fridge_pov": ([], "Point of view from inside an open refrigerator looking out into an ordinary Bulgarian panel-apartment kitchen at night: in the soft out-of-focus foreground the edges of glass fridge shelves with a jar of lyutenitsa, a block of yellow cheese, white feta in a box, a pot with a lid and a cake on a plate; beyond them the dark kitchen with white tiles, a wooden table with an oilcloth and an old gas stove, lit only by the warm fridge light spilling out. Empty, no people. " + LOOK),
}
def run(name):
    refs, prompt = JOBS[name]
    tid = kie.create("nano-banana-pro", {"prompt": prompt, "image_input": refs, "aspect_ratio": "9:16", "resolution": "2K", "output_format": "jpg"})
    d = kie.wait(tid, every=8)
    urls = kie.result_urls(d)
    if urls: kie.download(urls[0], os.path.join(OUT, name + ".jpg"))
    rec = {"name": name, "state": d["state"], "credits": d.get("creditsConsumed"), "urls": urls, "fail": d.get("failMsg")}
    print(json.dumps(rec, ensure_ascii=False), flush=True)
    open(os.path.join(OUT, "refs_log.jsonl"), "a").write(json.dumps(rec, ensure_ascii=False) + "\n")
if __name__ == "__main__":
    names = sys.argv[1:] or list(JOBS)
    with ThreadPoolExecutor(len(names)) as ex: list(ex.map(run, names))
