"""Add the Bulgarian text to the generated images, dormo style (labels, stamps, 3-panel infographics).
Reads kie/raw/*-raw.jpg (from generate_images.py) and kie/screen/card.png, writes the final img/*.jpg."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "..", "img")
FD = "/usr/share/fonts/opentype/inter/"
NAVY, INK, GREY, RED, GREEN = (24, 36, 74), (28, 28, 30), (110, 110, 118), (208, 32, 46), (26, 127, 55)


def F(size, w="Bold"):
    return ImageFont.truetype(FD + f"Inter-{w}.otf", size)


def raw(name):
    return Image.open(os.path.join(HERE, "raw", f"{name}-raw.jpg")).convert("RGB")


def save(im, name, width=1600):
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(os.path.join(IMG, f"{name}.jpg"), quality=85)
    print(name, im.size)


def center_text(d, cx, y, text, font, fill, maxw=None, lh=1.2):
    """Centered text, wrapped to maxw; returns the y below the block."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if maxw and d.textlength(t, font=font) > maxw and cur:
            lines.append(cur); cur = w
        else:
            cur = t
    lines.append(cur)
    for ln in lines:
        d.text((cx - d.textlength(ln, font=font) / 2, y), ln, font=font, fill=fill)
        y += int(font.size * lh)
    return y


def label(d, text, tx, ty, px, py, font, fill=INK, anchor="l"):
    """Label at (tx,ty) with a thin leader line to the point (px,py) and a dot."""
    w = d.textlength(text, font=font)
    x = tx if anchor == "l" else tx - w
    d.text((x, ty), text, font=font, fill=fill)
    sx = x - 14 if anchor == "l" else x + w + 14
    d.line([(sx, ty + font.size * 0.6), (px, py)], fill=fill, width=4)
    d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=fill)


def stamp(base, text, cx, cy, size=110, angle=-8, color=RED):
    f = F(size, "ExtraBold")
    tmp = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    tw = tmp.textlength(text, font=f)
    w, h = int(tw + size * 0.9), int(size * 1.7)
    s = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(s)
    d.rounded_rectangle([20, 20, 20 + w, 20 + h], radius=18, fill=(255, 255, 255, 235), outline=color, width=12)
    bb = d.textbbox((0, 0), text, font=f)
    d.text((20 + (w - tw) / 2, 20 + (h - (bb[1] + bb[3])) / 2), text, font=f, fill=color)
    s = s.rotate(angle, expand=True, resample=Image.BICUBIC)
    base.paste(s, (int(cx - s.width / 2), int(cy - s.height / 2)), s)


def rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, im.width, im.height], r, fill=255)
    out = Image.new("RGBA", im.size); out.paste(im, (0, 0), m); return out


def fit_crop(im, w, h):
    s = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x, y = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))


def lungs():
    im = raw("lungs"); W, H = im.size
    stamp(im, "ДИША СВОБОДНО", W * 0.25, H * 0.80, angle=-7, color=GREEN)
    stamp(im, "ЗАДЪХВА СЕ", W * 0.75, H * 0.80, angle=-7)
    save(im, "lungs")


def vise():
    im = raw("vise"); d = ImageDraw.Draw(im); f = F(62, "SemiBold")
    label(d, "Бели дробове", 1900, 380, 1420, 470, f)
    label(d, "Избутана диафрагма", 1900, 760, 1560, 880, f, fill=RED)
    label(d, "Висцерална мазнина", 1900, 1140, 1690, 1180, f, fill=(176, 120, 0))
    save(im, "vise")


def second_door():
    im = raw("second_door"); d = ImageDraw.Draw(im); f = F(56, "SemiBold"); g = (120, 128, 140)
    label(d, "Лепенка", 1700, 150, 1420, 360, f, fill=(200, 60, 120))
    label(d, "Кожата: втората врата", 1700, 1390, 1400, 1180, f, fill=NAVY)
    d.text((140, 90), "Стомах — заобиколен", font=f, fill=g)
    d.text((80, 1180), "Черен дроб — заобиколен", font=f, fill=g)
    d.text((2020, 1300), "Черва — заобиколени", font=f, fill=g)
    save(im, "second-door")


def steps():
    W, H = 1600, 930
    can = Image.new("RGB", (W, H), (238, 241, 244)); d = ImageDraw.Draw(can)
    xs = [267, 800, 1333]
    d.line([(xs[0], 62), (xs[2], 62)], fill=(170, 176, 186), width=4)
    titles = ["Заобиколи стомаха", "Подавай постепенно, целия ден", "Дай на тялото берберин"]
    caps = ["Кожата е втората врата — без подуване и тежест",
            "По малко и равномерно — като капково напояване",
            "Изследва се заради метаболитния превключвател AMPK"]
    for i, cx in enumerate(xs):
        d.ellipse([cx - 30, 32, cx + 30, 92], fill="white", outline=NAVY, width=5)
        center_text(d, cx, 44, str(i + 1), F(32, "ExtraBold"), NAVY)
        center_text(d, cx, 112, titles[i], F(34, "Bold"), INK, maxw=440)
        p = rounded(fit_crop(raw(f"step{i + 1}"), 460, 560), 22)
        can.paste(p, (cx - 230, 200), p)
        center_text(d, cx, 785, caps[i], F(26, "Medium"), GREY, maxw=430, lh=1.3)
    save(can, "steps")


def phases():
    W, H = 1600, 1300
    can = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(can)
    t = "ВАШИЯТ ДЕН С FITPATCHES"; f = F(46, "ExtraBold"); tw = d.textlength(t, font=f)
    d.rounded_rectangle([(W - tw) / 2 - 40, 34, (W + tw) / 2 + 40, 124], radius=45, fill=(244, 236, 241))
    center_text(d, W / 2, 52, t, f, NAVY)
    heads = [("Сутрин", "Залепвате — 30 секунди"), ("През деня", "Тихо подаване, без да мислите"),
             ("На следващата сутрин", "Нова лепенка, ново място")]
    for i in range(3):
        x0 = 50 + i * 510
        d.rounded_rectangle([x0, 160, x0 + 480, 1150], radius=24, fill=NAVY)
        center_text(d, x0 + 240, 182, heads[i][0], F(38, "ExtraBold"), "white")
        center_text(d, x0 + 240, 236, heads[i][1], F(27, "Medium"), (210, 216, 236), maxw=440)
        p = rounded(fit_crop(raw(f"phase{i + 1}"), 452, 840), 18)
        can.paste(p, (x0 + 14, 296), p)
    d.line([(90, 1220), (1500, 1220)], fill=(190, 196, 210), width=5)
    d.polygon([(1500, 1204), (1530, 1220), (1500, 1236)], fill=(190, 196, 210))
    for i in range(3):
        cx = 290 + i * 510
        d.ellipse([cx - 14, 1206, cx + 14, 1234], fill=NAVY)
    save(can, "phases")


def cost():
    im = raw("cost"); d = ImageDraw.Draw(im)
    center_text(d, 677, 1360, "1 000+ € на година", F(84, "ExtraBold"), RED)
    center_text(d, 2088, 760, "0,27 €", F(110, "ExtraBold"), INK)
    center_text(d, 2088, 900, "на ден", F(60, "SemiBold"), GREY)
    save(im, "cost-compare")


def seal():
    coin = raw("seal").crop((300, 170, 2460, 1500))
    W, H = 1600, 760
    can = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(can)
    c = coin.resize((round(coin.width * 560 / coin.height), 560), Image.LANCZOS)
    can.paste(c, (10, 100))
    x = 20 + c.width + 20
    f1, f2 = F(64, "ExtraBold"), F(32, "Medium")
    y = 250
    for ln in ["ПЛАЩАТЕ", "ПРИ ПОЛУЧАВАНЕ"]:
        d.text((x, y), ln, font=f1, fill=(150, 108, 20)); y += 78
    d.text((x, y + 16), "Без предплащане · Без абонамент", font=f2, fill=GREY)
    save(can, "seal")


def tablet():
    im = raw("tablet")
    card = Image.open(os.path.join(HERE, "screen", "card.png")).convert("RGB")
    dst = [(543, 722), (1443, 727), (1450, 1347), (522, 1337)]  # TL, TR, BR, BL of the blank screen
    w, h = card.size
    src = [(0, 0), (w, 0), (w, h), (0, h)]
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):  # map output (x,y) -> card (u,v)
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]; B += [u, v]
    coef = np.linalg.solve(np.array(A, float), np.array(B, float))
    warped = card.transform(im.size, Image.PERSPECTIVE, tuple(coef), Image.BICUBIC)
    mask = Image.new("L", im.size, 0); ImageDraw.Draw(mask).polygon(dst, fill=255)
    im.paste(warped, (0, 0), mask)
    save(im, "tablet-cta", 1200)


def plain(name, out):
    save(raw(name), out)


if __name__ == "__main__":
    lungs(); vise(); second_door(); steps(); phases(); cost(); seal(); tablet()
    plain("methods", "methods")
