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

HOOK = ["Пиете всякакви добавки, но всеки ден",
        "се задъхвате по стълбите и се чувствате,",
        "сякаш сте тичали маратон?",
        "Ето истинската причина —",
        "и тя изобщо не се крие в навиците ви."]

# pills: (text, x, y) as a share of the SOURCE image; layout "cover" = fill the width and crop,
# "fit" = whole image scaled into the photo area on a grey software-style frame.
ADS = {
    "A_dexa_monitor": dict(raw="dexa_monitor_2.jpg", layout="cover", crop_top=0.0,
                           pills=[("ЗАДЪХВА СЕ", 0.322, 0.165), ("НЕ СЕ ЗАДЪХВА", 0.700, 0.165)], lines=HOOK),
    "B_dexa_flat": dict(raw="dexa_flat_1.jpg", layout="fit", crop_top=0.0,
                        pills=[("ЗАДЪХВА СЕ", 0.252, 0.992), ("НЕ СЕ ЗАДЪХВА", 0.748, 0.992)], lines=HOOK),
}
FRAME = (205, 205, 205)


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
    raw = Image.open(os.path.join(HERE, "raw", ad["raw"])).convert("RGB")
    if ad["layout"] == "cover":
        src = raw.resize((W, W), Image.LANCZOS)
        top = max(0, min(W - ph, int(ad["crop_top"] * (W - ph))))
        photo = src.crop((0, top, W, top + ph))
        to_xy = lambda fx, fy: (fx * W, fy * W - top)
    else:
        band = 56  # frame below the scans, where the pills sit
        s = ph - band - 18
        photo = Image.new("RGB", (W, ph), FRAME)
        ox, oy = (W - s) // 2, 18
        photo.paste(raw.resize((s, s), Image.LANCZOS), (ox, oy))
        to_xy = lambda fx, fy: (ox + fx * s, oy + fy * s)
    d = ImageDraw.Draw(photo)
    for text, fx, fy in ad["pills"]:
        pill(d, text, *to_xy(fx, fy))
    out = Image.new("RGB", (W, H), "white")
    out.paste(photo, (0, 0))
    out.paste(cap, (0, ph))
    os.makedirs(os.path.join(HERE, "final"), exist_ok=True)
    out.save(os.path.join(HERE, "final", f"{name}.jpg"), quality=93)
    print(name, "font", size, "photo h", ph)

if __name__ == "__main__":
    for n, a in ADS.items():
        build(n, a)
