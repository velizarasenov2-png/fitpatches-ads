"""FitPatches: put the caption block and the pills on the raw photos -> final/*.jpg (1080x1350, Meta feed 4:5).

Style copied from the reference native ad: photo on top, black pill labels, white caption block
with bold condensed black text, centered, ending with a blue underlined "Прочети повече."
Needs Oswald (Google Fonts, Cyrillic) in FONT_DIR.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.environ.get("FONT_DIR", os.path.join(HERE, "fonts"))
W, H = 1080, 1350
INK, LINK, PILL = (17, 17, 17), (21, 94, 196), (14, 14, 14)
CTA = "Прочети повече."

ADS = {
    "A_skener": dict(
        raw="skener_2.jpg", crop_top=0.0,
        pills=[("ЯДЕ МАЛКО", 0.305, 0.150), ("ЯДЕ ВСИЧКО", 0.722, 0.150)],  # text, x centre, y centre (share of photo)
        lines=["Ядете като врабче, но коремът ви",
               "пак расте, а дънките стягат все повече?",
               "Ето истинската причина —",
               "и тя изобщо не се крие в чинията ви."],
    ),
    "B_garderob": dict(
        raw="garderob_1.jpg", crop_top=0.0,
        pills=[("ЧАКА ОТ 2019 Г.", 0.335, 0.085)],
        lines=["Искате пак да облечете роклята, която",
               "чака в гардероба от години — вместо черното?",
               "Ето истинската причина да не ви става —",
               "и тя изобщо не е в чинията ви."],
    ),
}


def font(size, weight=600):
    return ImageFont.truetype(os.path.join(FONT_DIR, f"Oswald-{weight}.ttf"), size)


def caption(lines, size):
    """Return the caption block image; CTA is appended to the last line in blue."""
    f = font(size)
    lh = int(size * 1.24)
    pad = int(size * 0.75)
    img = Image.new("RGB", (W, pad * 2 + lh * len(lines)), "white")
    d = ImageDraw.Draw(img)
    for i, ln in enumerate(lines):
        last = i == len(lines) - 1
        parts = [(ln, INK)] + ([(" " + CTA, LINK)] if last else [])
        total = sum(d.textlength(t, font=f) for t, _ in parts)
        x = (W - total) / 2
        y = pad + i * lh
        for t, col in parts:
            d.text((x, y), t, font=f, fill=col)
            if col == LINK:
                tw = d.textlength(t, font=f)
                lead = d.textlength(" ", font=f)
                asc, desc = f.getmetrics()
                uy = y + asc + int(desc * 0.30)  # just under the baseline
                d.rectangle([x + lead, uy, x + tw, uy + max(2, size // 18)], fill=LINK)
            x += d.textlength(t, font=f)
    return img


def fit_size(lines, start=48, margin=36):
    d = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    size = start
    while size > 30:
        f = font(size)
        widest = max(d.textlength(l + (" " + CTA if i == len(lines) - 1 else ""), font=f)
                     for i, l in enumerate(lines))
        if widest <= W - 2 * margin:
            return size
        size -= 1
    return size


def pill(d, text, cx, cy, size=46):
    f = font(size)
    tw = d.textlength(text, font=f)
    ph = int(size * 1.62)
    pw = int(tw + size * 1.25)
    x0, y0 = int(cx - pw / 2), int(cy - ph / 2)
    d.rounded_rectangle([x0, y0, x0 + pw, y0 + ph], radius=ph // 2, fill=PILL)
    bbox = d.textbbox((0, 0), text, font=f)
    d.text((cx - tw / 2, cy - (bbox[1] + bbox[3]) / 2), text, font=f, fill="white")


def build(name, ad):
    size = fit_size(ad["lines"])
    cap = caption(ad["lines"], size)
    ph = H - cap.height
    src = Image.open(os.path.join(HERE, "raw", ad["raw"])).convert("RGB").resize((W, W), Image.LANCZOS)
    top = int(ad["crop_top"] * (W - ph))  # 0 = keep the top, 1 = keep the bottom
    top = max(0, min(W - ph, top))
    photo = src.crop((0, top, W, top + ph))
    d = ImageDraw.Draw(photo)
    for text, fx, fy in ad["pills"]:
        pill(d, text, fx * W, fy * W - top)
    out = Image.new("RGB", (W, H), "white")
    out.paste(photo, (0, 0))
    out.paste(cap, (0, ph))
    os.makedirs(os.path.join(HERE, "final"), exist_ok=True)
    out.save(os.path.join(HERE, "final", f"{name}.jpg"), quality=93)
    print(name, "font", size, "photo h", ph, "crop top", top)


if __name__ == "__main__":
    for n, a in ADS.items():
        build(n, a)
