"""Compose advertorial-28 images: labels, red-X grid, risk card. Input kie/raw, output img/ (1200px wide)."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..")
RAW = os.path.join(ROOT, "kie", "raw"); OUT = os.path.join(ROOT, "img")
INTER = "/usr/share/fonts/opentype/inter/Inter-{}.otf"
OSW = os.path.join(ROOT, "..", "native-fitpatches-rentgen", "fonts", "Oswald-{}.ttf")
F = lambda w, s: ImageFont.truetype(INTER.format(w), s)
O = lambda w, s: ImageFont.truetype(OSW.format(w), s)
RED = (215, 30, 45); NAVY = (24, 34, 70); W = 1200


def raw(n):
    im = Image.open(os.path.join(RAW, f"{n}-raw.jpg")).convert("RGB")
    return im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)


def save(im, name):
    im.save(os.path.join(OUT, name), quality=86); print(name, im.size)


def pill(d, xy, text, font, fill, fg="white", pad=(18, 10), anchor="mm"):
    x, y = xy; b = d.textbbox((x, y), text, font=font, anchor=anchor)
    iw = d.im.size[0]; shift = max(0, 14 + pad[0] - b[0]) - max(0, b[2] + pad[0] + 14 - iw)
    if shift:
        x += shift; b = d.textbbox((x, y), text, font=font, anchor=anchor)
    d.rounded_rectangle((b[0] - pad[0], b[1] - pad[1], b[2] + pad[0], b[3] + pad[1]), 12, fill=fill)
    d.text((x, y), text, font=font, fill=fg, anchor=anchor)
    return b


def liver_hero():
    im = raw("liver_hero"); d = ImageDraw.Draw(im); h = im.height
    f = O("700", 46)
    pill(d, (int(W * 0.29), int(h * 0.86)), "ЗДРАВ ЧЕРЕН ДРОБ", f, (35, 120, 60))
    pill(d, (int(W * 0.72), int(h * 0.86)), "ОМАЗНЕН ЧЕРЕН ДРОБ", f, RED)
    save(im, "liver-hero.jpg")


def red_x_grid():
    im = raw("liver_grid"); a = np.asarray(im).astype(int)
    white = (a.min(axis=2) > 235)
    cols = np.where(white.mean(axis=0) > 0.97)[0]; rows = np.where(white.mean(axis=1) > 0.97)[0]

    def spans(idx, n):
        cuts = [0] + [int(i) for i in idx] + [n]; out = []; s = 0
        for c in cuts[1:]:
            if c - s > 40: out.append((s, c))
            s = c + 1
        return out
    xs, ys = spans(cols, im.width), spans(rows, im.height)
    d = ImageDraw.Draw(im)
    for x0, x1 in xs:
        for y0, y1 in ys:
            m = 0.22; lw = 16
            ax, ay, bx, by = x0 + (x1 - x0) * m, y0 + (y1 - y0) * m, x1 - (x1 - x0) * m, y1 - (y1 - y0) * m
            d.line((ax, ay, bx, by), fill=RED, width=lw); d.line((ax, by, bx, ay), fill=RED, width=lw)
    print("grid", xs, ys); save(im, "liver-grid.jpg")


def band_labels(name, out, left, right, colors=((35, 120, 60), RED), fill_bottom=False):
    im = raw(name); d = ImageDraw.Draw(im); h = im.height; f = F("ExtraBold", 34)
    if fill_bottom:
        bg = im.getpixel((20, int(h * 0.5))); d.rectangle((0, int(h * 0.80), W, h), fill=bg)
    pill(d, (int(W * 0.25), int(h * 0.9)), left, f, colors[0])
    pill(d, (int(W * 0.75), int(h * 0.9)), right, f, colors[1])
    save(im, out)


def arrow_label(d, text, at, to, font, fill):
    b = pill(d, at, text, font, fill)
    sx = b[2] + 18 if to[0] > b[2] else (b[0] - 18 if to[0] < b[0] else at[0])
    sy = at[1] if sx != at[0] else (b[3] + 10 if to[1] > b[3] else b[1] - 10)
    d.line((sx, sy, to[0], to[1]), fill=fill, width=6)
    d.ellipse((to[0] - 10, to[1] - 10, to[0] + 10, to[1] + 10), fill=fill)


def portal():
    im = raw("portal"); d = ImageDraw.Draw(im); h = im.height; f = F("ExtraBold", 32)
    arrow_label(d, "ЧЕРЕН ДРОБ", (int(W * 0.15), int(h * 0.22)), (int(W * 0.33), int(h * 0.33)), f, RED)
    arrow_label(d, "ПОРТАЛНА ВЕНА", (int(W * 0.80), int(h * 0.30)), (int(W * 0.52), int(h * 0.48)), f, (30, 80, 160))
    arrow_label(d, "МАЗНИНА ОКОЛО ЧЕРВАТА", (int(W * 0.22), int(h * 0.88)), (int(W * 0.40), int(h * 0.72)), f, (190, 130, 0))
    save(im, "portal.jpg")


def ultrasound():
    im = raw("ultrasound_screen"); d = ImageDraw.Draw(im); h = im.height
    arrow_label(d, "„СВЕТЪЛ“ ЧЕРЕН ДРОБ", (int(W * 0.30), int(h * 0.10)), (int(W * 0.30), int(h * 0.42)), F("ExtraBold", 34), RED)
    arrow_label(d, "бъбрек", (int(W * 0.82), int(h * 0.20)), (int(W * 0.62), int(h * 0.30)), F("Bold", 28), (60, 60, 60))
    save(im, "ultrasound-screen.jpg")


def risk_card():
    w, h = 1000, 1360; im = Image.new("RGB", (w, h), (246, 242, 236)); d = ImageDraw.Draw(im)
    d.text((w // 2, 70), "ОМАЗНЕНИЯТ ЧЕРЕН ДРОБ", font=F("Black", 60), fill=NAVY, anchor="mm")
    d.text((w // 2, 140), "В ЧИСЛА", font=F("Black", 60), fill=NAVY, anchor="mm")
    d.text((w // 2, 210), "Какво показват големите проучвания", font=F("Medium", 32), fill=(120, 120, 130), anchor="mm")
    tiles = [("7 от 10", "души с наднормено\nтегло го имат", "151 проучвания, 101 028 души"),
             ("+64%", "риск от инфаркт\nи инсулт", "16 проучвания, 34 043 души"),
             ("1 на 5", "вече има белези\n(фиброза) в черния дроб", "при наднормено тегло"),
             ("×4", "повече сърдечни,\nотколкото чернодробни\nсмъртни случаи", "над 9 млн. души")]
    for i, (big, txt, src) in enumerate(tiles):
        x0 = 30 + (i % 2) * 485; y0 = 270 + (i // 2) * 470; x1, y1 = x0 + 455, y0 + 445
        d.rounded_rectangle((x0, y0, x1, y1), 28, fill="white", outline=(230, 222, 212), width=3)
        cx = (x0 + x1) // 2
        d.text((cx, y0 + 105), big, font=F("Black", 96 if len(big) < 5 else 84), fill=RED, anchor="mm")
        d.multiline_text((cx, y0 + 255), txt, font=F("Bold", 32), fill=(30, 30, 30), anchor="mm", align="center", spacing=8)
        d.text((cx, y1 - 45), src, font=F("Medium", 27), fill=(120, 120, 130), anchor="mm")
    d.text((w // 2, 1260), "1 на всеки 3 възрастни по света", font=F("ExtraBold", 44), fill=NAVY, anchor="mm")
    d.text((w // 2, 1315), "Източниците са под текста", font=F("Medium", 28), fill=(120, 120, 130), anchor="mm")
    save(im, "liver-risks.jpg")


def pack_sky():
    im = raw("pack_sky"); d = ImageDraw.Draw(im); h = im.height
    cx, cy, r = int(W * 0.84), int(h * 0.17), 118                      # red sale circle
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=RED)
    d.text((cx, cy - 20), "−50%", font=F("Black", 62), fill="white", anchor="mm")
    d.text((cx, cy + 42), "ДНЕС", font=F("ExtraBold", 34), fill="white", anchor="mm")
    cx, cy, r = int(W * 0.15), int(h * 0.80), 112                      # gold seal
    gold, dark = (214, 168, 52), (120, 82, 10)
    import math                                                        # starburst edge
    d.polygon([(cx + (r + (14 if k % 2 else 2)) * math.cos(math.pi * k / 30),
                cy + (r + (14 if k % 2 else 2)) * math.sin(math.pi * k / 30)) for k in range(60)], fill=gold)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=gold, outline=dark, width=5)
    d.ellipse((cx - r + 14, cy - r + 14, cx + r - 14, cy + r - 14), outline=(250, 230, 160), width=3)
    for i, (t, sz) in enumerate((("ПЛАЩАТЕ", 25), ("ПРИ", 23), ("ПОЛУЧАВАНЕ", 19))):
        d.text((cx, cy - 30 + i * 30), t, font=F("Black", sz), fill=dark, anchor="mm")
    save(im, "pack-sky.jpg")


def plain(name, out):
    save(raw(name), out)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    liver_hero(); red_x_grid(); portal(); ultrasound(); risk_card()
    band_labels("liver_cells", "liver-cells.jpg", "ЗДРАВИ КЛЕТКИ", "КЛЕТКИ, ПЪЛНИ С МАЗНИНА")
    band_labels("pear_apple", "pear-apple.jpg", "ДО 40: ПО ХАНША", "СЛЕД 40: В КОРЕМА", ((60, 90, 160), RED), fill_bottom=True)
    pack_sky(); plain("desk_liver", "desk-liver.jpg"); plain("walk_finale", "walk-finale.jpg")
    if os.path.exists(os.path.join(RAW, "ultrasound_visit-raw.jpg")):
        plain("ultrasound_visit", "ultrasound-visit.jpg")
