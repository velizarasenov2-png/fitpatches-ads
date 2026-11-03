#!/usr/bin/env python3
"""Builds the still frames (product shots) and overlay PNGs for the FitPatches VSL.

Usage: python3 make_graphics.py <workdir>
Expects <workdir>/product/*.png (store photos from cdn.shopify.com) and the
Montserrat / Playfair Display TTFs in <workdir>/fonts/. Writes <workdir>/gfx/.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1920
WORK = sys.argv[1]
P = os.path.join(WORK, "product")
OUT = os.path.join(WORK, "gfx")
os.makedirs(OUT, exist_ok=True)
F_BOLD = os.path.join(WORK, "fonts", "f2.ttf")    # Montserrat Bold
F_XBOLD = os.path.join(WORK, "fonts", "f3.ttf")   # Montserrat ExtraBold
F_SERIF = os.path.join(WORK, "fonts", "f5.ttf")   # Playfair Display ExtraBold

PINK = (217, 79, 134)
GOLD = (232, 194, 79)


def load(name):
    return Image.open(os.path.join(P, name)).convert("RGB")


def cover(im, w, h, cx=0.5, cy=0.5):
    """Scale to cover w x h and crop around the (cx, cy) focus point."""
    s = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = min(max(0, round(im.width * cx - w / 2)), im.width - w)
    y = min(max(0, round(im.height * cy - h / 2)), im.height - h)
    return im.crop((x, y, x + w, y + h))


def on_canvas(piece, bg, width_frac=0.9, cy=0.5, size=(1296, 2304), sides=False):
    """Places a cropped piece on a flat background (stills are rendered 20% larger for the slow zoom).

    Products sit in the upper part of the frame so the captions (lower third) fall on plain background."""
    cw, ch = size
    canvas = Image.new("RGB", size, bg)
    pw = round(cw * width_frac)
    piece = piece.resize((pw, round(piece.height * pw / piece.width)), Image.LANCZOS)
    # feather the top and bottom edges so the crop blends into the flat background
    fade = min(160, piece.height // 4)
    mask = Image.new("L", piece.size, 255)
    md = ImageDraw.Draw(mask)
    for i in range(fade):
        a = round(255 * i / fade)
        md.line([(0, i), (piece.width, i)], fill=a)
        md.line([(0, piece.height - 1 - i), (piece.width, piece.height - 1 - i)], fill=a)
    if sides:
        side = Image.new("L", piece.size, 255)
        sd = ImageDraw.Draw(side)
        for i in range(fade):
            a = round(255 * i / fade)
            sd.line([(i, 0), (i, piece.height)], fill=a)
            sd.line([(piece.width - 1 - i, 0), (piece.width - 1 - i, piece.height)], fill=a)
        from PIL import ImageChops
        mask = ImageChops.multiply(mask, side)
    canvas.paste(piece, ((cw - pw) // 2, round(ch * cy - piece.height / 2)), mask)
    return canvas


def save(im, name):
    im.save(os.path.join(OUT, name))
    print("wrote", name, im.size)


# ---------- product stills (1296x2304, zoomed slowly to 1080x1920 at render) ----------
SW, SH = 1296, 2304

# Pouch on the pink panel. The store image carries a headline claim at the top, so it is cropped away.
hero = load("fp-slide-s1_hero_v2.png")
save(on_canvas(hero.crop((250, 700, 1540, 2180)), hero.getpixel((200, 1500)), width_frac=0.8, cy=0.33, sides=True),
     "still_hero.png")

# Pouch with pomegranate, cinnamon and leaves (no claims in frame).
pouch = load("fitpatches_2048_no_white_background.png")
save(on_canvas(pouch, pouch.getpixel((900, 2390)), width_frac=1.0, cy=0.36), "still_pouch.png")

# A single patch, close (the tile from the how-to card, without the text column).
howto = load("fp-detail-howto.png")
tile = howto.crop((70, 860, 905, 1830))
save(on_canvas(tile, howto.getpixel((10, 10)), width_frac=0.8, cy=0.36), "still_patch.png")

# Patch sheet (from the placement card, without heading or icons).
polza = load("polza_size.png")
sheet = polza.crop((120, 640, 1680, 1430))
bg = polza.getpixel((60, 700))
save(on_canvas(sheet, bg, width_frac=1.0, cy=0.37), "still_sheet.png")

# Patch on the wrist.
ruka = load("ruka_size_new_e633366f-b56d-4632-848c-4885ced7e166.png")
save(cover(ruka, SW, SH, cx=0.56, cy=0.55), "still_wrist.png")
save(cover(ruka, SW, SH, cx=0.56, cy=0.55).filter(ImageFilter.GaussianBlur(28)), "still_wrist_blur.png")

# Five pouches, two marked as the free ones (3+2). The pouch is cut from the hero image.
px0, py0, px1, py1 = 400, 780, 1400, 2140
cut = hero.crop((px0, py0, px1, py1))
# Background = panel pink, flood-filled from the corners so the pink circle on the pouch stays.
mask_src = cut.copy()
for corner in [(2, 2), (cut.width - 3, 2), (2, cut.height - 3), (cut.width - 3, cut.height - 3)]:
    ImageDraw.floodfill(mask_src, corner, (255, 0, 255), thresh=38)
mask = Image.new("L", cut.size, 255)
mp, mm = mask_src.load(), mask.load()
for y in range(cut.height):
    for x in range(cut.width):
        if mp[x, y] == (255, 0, 255):
            mm[x, y] = 0
mask = mask.filter(ImageFilter.GaussianBlur(1.2))
bbox = mask.getbbox()
cut, mask = cut.crop(bbox), mask.crop(bbox)
pouch_rgba = cut.copy()
pouch_rgba.putalpha(mask)

five = Image.new("RGB", (SW, SH), (250, 228, 236))
g = ImageDraw.Draw(five)
for i in range(SH):  # soft vertical gradient
    t = i / SH
    g.line([(0, i), (SW, i)], fill=(round(252 - 12 * t), round(236 - 22 * t), round(243 - 14 * t)))
pw = 480
ph = round(pouch_rgba.height * pw / pouch_rgba.width)
small = pouch_rgba.resize((pw, ph), Image.LANCZOS)
shadow = Image.new("RGBA", small.size, (90, 30, 60, 0))
shadow.putalpha(small.getchannel("A").point(lambda a: a * 0.35))
shadow = shadow.filter(ImageFilter.GaussianBlur(18))
# back row of 3, front row of 2 (the free ones)
positions = [(SW // 2 - 360 - pw // 2, 400), (SW // 2 - pw // 2, 340), (SW // 2 + 360 - pw // 2, 400),
             (SW // 2 - 200 - pw // 2, 400 + round(ph * 0.6)), (SW // 2 + 200 - pw // 2, 400 + round(ph * 0.6))]
f_rib = ImageFont.truetype(F_XBOLD, 44)
for k, (x, y) in enumerate(positions):
    five.paste(shadow, (x + 14, y + 26), shadow)
    five.paste(small, (x, y), small)
    if k >= 3:
        d = ImageDraw.Draw(five)
        rx0, ry0, rx1, ry1 = x - 10, y + ph - 120, x + pw + 10, y + ph - 40
        d.rounded_rectangle((rx0, ry0, rx1, ry1), radius=18, fill=PINK)
        d.text(((rx0 + rx1) / 2, (ry0 + ry1) / 2), "ПОДАРЪК", font=f_rib, fill="white", anchor="mm")
save(five, "still_five.png")


# ---------- overlays (1080x1920 RGBA) ----------
def overlay():
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def shadowed(im, radius=14, alpha=150):
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    sh.putalpha(im.getchannel("A").point(lambda a: min(alpha, a)))
    sh = sh.filter(ImageFilter.GaussianBlur(radius))
    out = overlay()
    out.alpha_composite(sh, (6, 10))
    out.alpha_composite(im)
    return out


# Red X (drawn over the "wrong" options).
im = overlay()
d = ImageDraw.Draw(im)
cx, cy, r, wd = W // 2, 760, 250, 64
d.line([(cx - r, cy - r), (cx + r, cy + r)], fill=(226, 38, 38, 255), width=wd)
d.line([(cx - r, cy + r), (cx + r, cy - r)], fill=(226, 38, 38, 255), width=wd)
for (x, y) in [(cx - r, cy - r), (cx + r, cy + r), (cx - r, cy + r), (cx + r, cy - r)]:
    d.ellipse((x - wd / 2, y - wd / 2, x + wd / 2, y + wd / 2), fill=(226, 38, 38, 255))
save(shadowed(im), "ov_x.png")


def boxes(checked):
    im = overlay()
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(F_XBOLD, 64)
    labels = ["Какво има вътре?", "Изследвано ли е?", "Плащане при получаване"] if checked else ["?", "?", "?"]
    panel = (90, 330, W - 90, 1010)
    d.rounded_rectangle(panel, radius=36, fill=(20, 20, 24, 170))
    for i in range(3):
        y = 380 + i * 205
        bx = 140
        d.rounded_rectangle((bx, y, bx + 150, y + 150), radius=26, outline=(255, 255, 255, 255), width=9,
                            fill=(255, 255, 255, 40))
        d.text((bx + 75, y + 75), str(i + 1), font=f, fill=(255, 255, 255, 120 if checked else 255), anchor="mm")
        if checked:
            d.line([(bx + 28, y + 80), (bx + 64, y + 118), (bx + 130, y + 30)], fill=(76, 201, 107, 255),
                   width=26, joint="curve")
            ft = ImageFont.truetype(F_BOLD, 44 if i < 2 else 38)
            d.text((bx + 190, y + 75), labels[i], font=ft, fill="white", anchor="lm")
        else:
            d.rounded_rectangle((bx + 190, y + 55, W - 160, y + 95), radius=20, fill=(255, 255, 255, 70))
    return shadowed(im)


save(boxes(False), "ov_boxes.png")
save(boxes(True), "ov_checks.png")

# "Cash on delivery" badge.
im = overlay()
d = ImageDraw.Draw(im)
f = ImageFont.truetype(F_XBOLD, 66)
text = "НАЛОЖЕН ПЛАТЕЖ"
tw = d.textlength(text, font=f)
x0, y0 = (W - tw) / 2 - 60, 420
d.rounded_rectangle((x0, y0, x0 + tw + 120, y0 + 140), radius=70, fill=(255, 255, 255, 245))
d.text((W / 2, y0 + 70), text, font=f, fill=PINK + (255,), anchor="mm")
save(shadowed(im), "ov_cod.png")

# Order button.
im = overlay()
d = ImageDraw.Draw(im)
f = ImageFont.truetype(F_XBOLD, 70)
text = "ПОРЪЧАЙ СЕГА  ›"
tw = d.textlength(text, font=f)
x0, y0 = (W - tw) / 2 - 70, 1540
d.rounded_rectangle((x0, y0, x0 + tw + 140, y0 + 160), radius=80, fill=PINK + (255,))
d.text((W / 2, y0 + 80), text, font=f, fill="white", anchor="mm")
f2 = ImageFont.truetype(F_BOLD, 40)
d.text((W / 2, y0 + 215), "Плащате при получаване", font=f2, fill="white", anchor="mm",
       stroke_width=3, stroke_fill=(0, 0, 0, 160))
save(shadowed(im), "ov_button.png")
