"""Phone-first versions of the text-heavy images (1000 px wide, vertical, large type).
Overwrites img/steps.jpg, phases.jpg, risks.jpg, absorption.jpg, vise.jpg, second-door.jpg."""
import os
from PIL import Image, ImageDraw
import compose_images as C

F, NAVY, INK, GREY, RED = C.F, C.NAVY, C.INK, C.GREY, C.RED
GREEN = (22, 128, 60)
raw = C.raw


def wrap(d, text, font, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) > maxw and cur:
            lines.append(cur); cur = w
        else:
            cur = t
    return lines + [cur]


def block(d, x, y, text, font, fill, maxw, lh=1.28, center=False):
    for ln in wrap(d, text, font, maxw):
        xx = x + (maxw - d.textlength(ln, font=font)) / 2 if center else x
        d.text((xx, y), ln, font=font, fill=fill); y += int(font.size * lh)
    return y


def circle_num(d, cx, cy, n, color, r=34):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    C.center_text(d, cx, cy - 23, str(n), F(36, "ExtraBold"), "white")


def finish(can, used_h, name):
    C.save(can.crop((0, 0, can.width, used_h)), name, width=1000)


def steps_m():
    W = 1000; can = Image.new("RGB", (W, 2000), (238, 241, 244)); d = ImageDraw.Draw(can)
    y = block(d, 40, 40, "ТРИТЕ СТЪПКИ", F(58, "ExtraBold"), NAVY, 920, center=True) + 20
    rows = [("Заобиколи стомаха", "Кожата е втората врата — без подуване и тежест."),
            ("Подавай постепенно, целия ден", "По малко и равномерно — като капково напояване."),
            ("Дай на тялото берберин", "Изследва се заради метаболитния превключвател AMPK.")]
    for i, (t, c) in enumerate(rows):
        p = C.rounded(C.fit_crop(raw(f"step{i + 1}"), 380, 440), 22); can.paste(p, (40, y), p)
        circle_num(d, 470, y + 40, i + 1, NAVY)
        yy = block(d, 520, y + 14, t, F(44, "ExtraBold"), INK, 440)
        block(d, 450, yy + 16, c, F(36, "Medium"), GREY, 510)
        y += 480
    finish(can, y + 10, "steps")


def phases_m():
    W = 1000; can = Image.new("RGB", (W, 2200), "white"); d = ImageDraw.Draw(can)
    f = F(52, "ExtraBold"); t = "ВАШИЯТ ДЕН С FITPATCHES"; tw = d.textlength(t, font=f)
    d.rounded_rectangle([(W - tw) / 2 - 36, 36, (W + tw) / 2 + 36, 126], radius=45, fill=(244, 236, 241))
    C.center_text(d, W / 2, 50, t, f, NAVY)
    y = 170
    rows = [("Сутрин", "Залепвате — 30 секунди."), ("През деня", "Тихо подаване, без да мислите за нея."),
            ("На следващата сутрин", "Нова лепенка, на ново място.")]
    for i, (t, c) in enumerate(rows):
        p = C.rounded(C.fit_crop(raw(f"phase{i + 1}"), 400, 500), 22); can.paste(p, (40, y), p)
        d.rounded_rectangle([470, y + 20, 960, y + 20 + 74], radius=37, fill=NAVY)
        C.center_text(d, 715, y + 36, t, F(36, "ExtraBold"), "white")
        block(d, 470, y + 130, c, F(40, "SemiBold"), INK, 490)
        y += 540
    finish(can, y, "phases")


def risks_m():
    W = 1000; can = Image.new("RGB", (W, 1600), (246, 243, 238)); d = ImageDraw.Draw(can)
    y = block(d, 40, 36, "МАЗНИНАТА В КОРЕМА И РИСКОВЕТЕ", F(54, "ExtraBold"), NAVY, 920, center=True)
    y = block(d, 40, y + 6, "Какво показват големите проучвания при жени с най-голяма талия", F(32, "Medium"), GREY, 920, center=True) + 24
    tiles = [("×2", "риск от смърт от сърдечно-съдово заболяване", "44 636 жени, 16 г."),
             ("×3", "сърдечен риск при НОРМАЛНО тегло, но талия 88+ см", "44 636 жени, 16 г."),
             ("×5", "риск от диабет тип 2, независимо от теглото", "43 581 жени"),
             ("×3", "риск от деменция десетилетия по-късно", "6 583 души, 30+ г.")]
    for i, (big, lbl, src) in enumerate(tiles):
        x0 = 30 + (i % 2) * 480; y0 = y + (i // 2) * 470
        d.rounded_rectangle([x0, y0, x0 + 460, y0 + 450], radius=26, fill="white", outline=(228, 222, 212), width=3)
        C.center_text(d, x0 + 230, y0 + 18, big, F(130, "ExtraBold"), RED)
        block(d, x0 + 25, y0 + 190, lbl, F(36, "Bold"), INK, 410, lh=1.22, center=True)
        C.center_text(d, x0 + 230, y0 + 390, src, F(28, "Medium"), GREY)
    y += 2 * 470 + 10
    y = block(d, 40, y, "+63% риск от смърт от рак", F(40, "ExtraBold"), NAVY, 920, center=True)
    y = block(d, 40, y + 4, "Източниците са под текста", F(28, "Medium"), GREY, 920, center=True)
    finish(can, y + 30, "risks")


def absorption_m():
    W = 1000; can = Image.new("RGB", (W, 4200), (246, 243, 238)); d = ImageDraw.Draw(can)
    y = block(d, 40, 36, "КАПСУЛА СРЕЩУ ЛЕПЕНКА", F(62, "ExtraBold"), NAVY, 920, center=True)
    y = block(d, 40, y + 4, "Пътят на съставките до кръвта", F(36, "Medium"), GREY, 920, center=True) + 30
    secs = [
        dict(color=RED, head="КАПСУЛА: 3 БАРИЕРИ", raw="abs_capsule", crop=(0, 860, 1792, 2204),
             marks=[(1, 1180, 1250), (2, 905, 1700), (3, 640, 1180)],
             steps=[("Стомахът", "Киселина и дразнене: тежест, подуване, запек или разстройство."),
                    ("Червата", "Усвоява се трудно, а „помпите“ в чревната стена връщат голяма част обратно."),
                    ("Черният дроб", "Разгражда голяма част още при първото преминаване.")],
             result="×  До кръвта стига под 1%*", tint=(252, 228, 230)),
        dict(color=GREEN, head="ЛЕПЕНКА: ВТОРАТА ВРАТА", raw="abs_patch", crop=(0, 520, 1792, 2200),
             marks=[(1, 1100, 900), (2, 760, 1330)],
             steps=[("Кожата", "Нищо не се гълта — стомахът изобщо не участва."),
                    ("Малките съдове под кожата", "Към кръвта, без червата и без първото преминаване през черния дроб."),
                    ("През целия ден", "Бавно и равномерно, като капково напояване — без пикове и спадове.")],
             result="✓  Постепенно, целия ден", tint=(222, 244, 228)),
    ]
    splits = []
    for s in secs:
        splits.append(y - 20)
        f = F(44, "ExtraBold"); tw = d.textlength(s["head"], font=f)
        d.rounded_rectangle([(W - tw) / 2 - 34, y, (W + tw) / 2 + 34, y + 80], radius=40, fill=s["color"])
        C.center_text(d, W / 2, y + 13, s["head"], f, "white"); y += 104
        x0, y0, x1, y1 = s["crop"]; S = 920 / (x1 - x0)
        img = raw(s["raw"]).crop(s["crop"]).resize((920, round((y1 - y0) * S)), Image.LANCZOS)
        cd = ImageDraw.Draw(img)
        for n, ox, oy in s["marks"]:
            mx, my = (ox - x0) * S, (oy - y0) * S
            cd.ellipse([mx - 34, my - 34, mx + 34, my + 34], fill=s["color"], outline="white", width=5)
            C.center_text(cd, mx, my - 24, str(n), F(38, "ExtraBold"), "white")
        img = C.rounded(img, 26); can.paste(img, (40, y), img); y += img.height + 34
        for i, (t, desc) in enumerate(s["steps"]):
            circle_num(d, 80, y + 30, i + 1, s["color"])
            d.text((136, y + 4), t, font=F(42, "ExtraBold"), fill=INK)
            y = block(d, 136, y + 60, desc, F(36, "Medium"), GREY, 820) + 22
        d.rounded_rectangle([40, y, 960, y + 110], radius=24, fill=s["tint"], outline=s["color"], width=4)
        C.center_text(d, W / 2, y + 30, s["result"], F(44, "ExtraBold"), s["color"]); y += 160
    y = block(d, 40, y, "* при берберин на капсули (Liu и съавт., Fitoterapia, 2016).", F(30, "Medium"), GREY, 920, center=True)
    y = block(d, 40, y + 4, "Лепенката е създадена да заобиколи трите бариери на капсулата.", F(32, "SemiBold"), NAVY, 920, center=True)
    finish(can, y + 30, "absorption")
    cut = splits[1]
    C.save(can.crop((0, 0, W, cut)), "absorption-1", width=1000)
    C.save(can.crop((0, cut, W, y + 30)), "absorption-2", width=1000)


def label2(d, lines, tx, ty, px, py, font, fill):
    """Multi-line label with a leader line from the first line to the point."""
    y = ty
    for ln in lines:
        d.text((tx, y), ln, font=font, fill=fill); y += int(font.size * 1.15)
    d.line([(tx - 16, ty + font.size * 0.6), (px, py)], fill=fill, width=6)
    d.ellipse([px - 12, py - 12, px + 12, py + 12], fill=fill)


def vise_m():
    im = raw("vise"); d = ImageDraw.Draw(im); f = F(96, "Bold")
    label2(d, ["Бели дробове"], 1820, 330, 1420, 470, f, INK)
    label2(d, ["Избутана", "диафрагма"], 1820, 700, 1560, 880, f, RED)
    label2(d, ["Висцерална", "мазнина"], 1820, 1110, 1690, 1180, f, (176, 120, 0))
    C.save(im, "vise", width=1400)


def second_door_m():
    im = raw("second_door"); d = ImageDraw.Draw(im); f = F(86, "Bold"); g = (110, 118, 130)
    label2(d, ["Лепенка"], 1720, 110, 1420, 360, f, (200, 60, 120))
    t = "Кожата: втората врата"; tw = d.textlength(t, font=f)
    d.text((1376 - tw / 2, 1410), t, font=f, fill=NAVY)
    d.line([(1376, 1405), (1400, 1190)], fill=NAVY, width=6)
    d.ellipse([1388, 1178, 1412, 1202], fill=NAVY)
    for lines, x, y in [(["Стомах", "заобиколен"], 110, 50), (["Черен дроб", "заобиколен"], 60, 1240),
                        (["Черва", "заобиколени"], 2160, 1300)]:
        for k, ln in enumerate(lines):
            d.text((x, y + k * 100), ln, font=f, fill=g)
    C.save(im, "second-door", width=1400)


if __name__ == "__main__":
    steps_m(); phases_m(); risks_m(); absorption_m(); vise_m(); second_door_m()
