"""Claret Atelier Theme - icon candidates.

Code-drawn candidates (no AI images), a light/dark contact sheet and an inline
strip. Re-runnable: every mark is redrawn from scratch.

Run from the project root:  py -3 scripts/generate-icon-candidates.py
"""

import io
import math
import os

from PIL import Image, ImageDraw, ImageFont

S = 3
W = 1024

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "logo-candidates")

# palette (already de-collided from garnet-porcelain / coastal-cream)
WINE = (90, 15, 30, 255)        # #5A0F1E  deep claret
WINE2 = (138, 26, 44, 255)       # #8A1A2C  brighter claret
BRASS = (216, 188, 140, 255)     # #D8BC8C  warm brass
BRASS_D = (170, 138, 92, 255)    # #AA8A5C  shaded brass
PAPER = (250, 246, 238, 255)     # #FAF6EE  warm paper
BLUE = (159, 180, 198, 255)      # #9FB4C6  cool grey blue
INK = (58, 31, 38, 255)          # #3A1F26  outline

LIGHT_BG = (247, 243, 236, 255)
DARK_BG = (32, 20, 26, 255)
LIGHT_INK = (62, 34, 42, 255)
DARK_INK = (240, 226, 214, 255)

FONT_DIR = r"C:\Windows\Fonts"


def font(name, size):
    try:
        return ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    except Exception:
        return ImageFont.load_default()


def scr(p):
    return (p[0] * S, p[1] * S)


def wd(v):
    return max(1, int(round(v * S)))


def canvas():
    return Image.new("RGBA", (W * S, W * S), (0, 0, 0, 0))


def finish(img):
    return img.resize((W, W), Image.LANCZOS)


def bez(p0, p1, p2, n=64):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1.0 - t
        pts.append((u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
                    u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]))
    return pts


def poly(draw, pts, fill, outline=None, width=0):
    draw.polygon([scr(p) for p in pts], fill=fill,
                 outline=outline, width=wd(width) if width else 0)


def disc(draw, center, r, fill, outline=None, width=0):
    draw.ellipse([center[0] * S - r * S, center[1] * S - r * S,
                  center[0] * S + r * S, center[1] * S + r * S],
                 fill=fill, outline=outline, width=wd(width) if width else 0)


def rrect(draw, box, radius, fill, outline=None, width=0):
    draw.rounded_rectangle([box[0] * S, box[1] * S, box[2] * S, box[3] * S],
                           radius=radius * S, fill=fill, outline=outline,
                           width=wd(width) if width else 0)


def line(draw, pts, color, width, joint="curve"):
    draw.line([scr(p) for p in pts], fill=color, width=wd(width), joint=joint)


# ---------------------------------------------------------------- candidates

def cand_palette():
    """01 - painter's palette with paint dabs."""
    img = canvas()
    d = ImageDraw.Draw(img)

    disc(d, (512, 500), 300, PAPER, INK, 26)

    # thumb hole (punched out)
    disc(d, (648, 392), 62, (0, 0, 0, 0))
    disc(d, (648, 392), 62, None, INK, 18)

    # paint dabs along the lower rim
    disc(d, (352, 596), 72, WINE)
    disc(d, (470, 672), 64, BRASS)
    disc(d, (578, 690), 56, BLUE)
    disc(d, (268, 486), 46, WINE2)

    return finish(img)


def cand_brush():
    """02 - slanted paint brush with a claret tip."""
    layer = canvas()
    d = ImageDraw.Draw(layer)

    # handle
    rrect(d, (432, 176, 592, 556), 64, WINE, INK, 28)
    rrect(d, (468, 214, 496, 520), 12, (120, 34, 48, 255))

    # ferrule
    rrect(d, (418, 548, 606, 668), 22, BRASS, INK, 26)
    for x in (472, 512, 552, 592):
        line(d, [(x, 566), (x, 646)], BRASS_D, 11)

    # bristles
    poly(d, [(438, 656), (586, 656), (512, 862)], PAPER, INK, 22)

    # paint tip
    poly(d, [(478, 792), (546, 792), (512, 918)], WINE2)
    disc(d, (512, 910), 36, WINE)

    rot = layer.rotate(-32, resample=Image.BICUBIC, expand=True)
    out = canvas()
    out.alpha_composite(rot, ((W * S - rot.width) // 2, (W * S - rot.height) // 2))
    return finish(out)


def cand_tube():
    """03 - squeezed paint tube with a claret drop."""
    img = canvas()
    d = ImageDraw.Draw(img)

    # crimped tail
    rrect(d, (296, 150, 728, 232), 18, BRASS_D, INK, 22)
    for x in range(348, 700, 56):
        line(d, [(x, 162), (x, 230)], BRASS, 12)

    # metal body
    poly(d, [(320, 232), (704, 232), (632, 648), (392, 648)], BLUE, INK, 24)
    line(d, [(392, 268), (430, 610)], (198, 214, 226, 255), 22)

    # shoulder + nozzle
    poly(d, [(392, 648), (632, 648), (584, 738), (440, 738)], INK)
    rrect(d, (466, 738, 558, 798), 14, WINE, INK, 18)

    # drop
    poly(d, [(468, 832), (556, 832), (512, 932)], WINE)

    return finish(img)


def cand_easel():
    """04 - canvas on a claret easel with a brass stroke."""
    img = canvas()
    d = ImageDraw.Draw(img)

    # easel legs
    line(d, [(512, 560), (318, 872)], WINE, 34)
    line(d, [(512, 560), (706, 872)], WINE, 34)
    line(d, [(368, 762), (656, 762)], WINE, 24)
    line(d, [(318, 872), (256, 872)], WINE, 22)
    line(d, [(706, 872), (768, 872)], WINE, 22)

    # canvas
    rrect(d, (298, 236, 726, 600), 18, PAPER, INK, 26)

    # single brass brush stroke
    stroke = bez((360, 520), (470, 322), (664, 430))
    line(d, stroke, BRASS, 40)
    disc(d, (664, 430), 22, WINE2)

    return finish(img)


def cand_drop():
    """05 - claret paint drop inside a brass ring."""
    img = canvas()
    d = ImageDraw.Draw(img)

    # ring
    disc(d, (512, 512), 300, None, BRASS, 24)

    # drop body
    poly(d, [(388, 500), (636, 500), (512, 246)], WINE)
    disc(d, (512, 520), 128, WINE)

    # highlight
    disc(d, (466, 470), 34, (250, 246, 238, 190))

    # splatter
    disc(d, (766, 636), 26, WINE2)
    disc(d, (300, 700), 18, WINE2)

    return finish(img)


def cand_jar():
    """06 - pigment jar with a brush resting in it."""
    img = canvas()
    d = ImageDraw.Draw(img)

    # brush leaning out of the jar
    line(d, [(596, 420), (712, 176)], INK, 26)
    poly(d, [(676, 236), (752, 168), (700, 148), (640, 210)], WINE2)

    # lid
    rrect(d, (296, 336, 728, 428), 22, BRASS, INK, 24)

    # jar body
    rrect(d, (318, 430, 706, 824), 34, PAPER, INK, 26)

    # pigment pool
    d.rounded_rectangle([330 * S, 606 * S, 694 * S, 812 * S],
                        radius=28 * S, fill=WINE)

    # glass highlight
    rrect(d, (360, 476, 404, 590), 12, (255, 255, 255, 150))

    return finish(img)


CANDIDATES = [
    ("01", "palette", cand_palette),
    ("02", "brush", cand_brush),
    ("03", "paint-tube", cand_tube),
    ("04", "easel-canvas", cand_easel),
    ("05", "paint-drop", cand_drop),
    ("06", "pigment-jar", cand_jar),
]


# ---------------------------------------------------------------- sheet bits

def centered_text(d, center, text, fnt, fill):
    b = d.textbbox((0, 0), text, font=fnt)
    x = center[0] - (b[2] - b[0]) / 2 - b[0]
    y = center[1] - (b[3] - b[1]) / 2 - b[1]
    d.text((x, y), text, font=fnt, fill=fill)


def contact_sheet(icons, bg, ink, path):
    cell_w, cell_h = 420, 540
    margin, gap = 40, 26
    head = 118
    sheet_w = margin * 2 + cell_w * 3 + gap * 2
    sheet_h = margin + head + cell_h * 2 + gap + margin

    sheet = Image.new("RGBA", (sheet_w, sheet_h), bg)
    d = ImageDraw.Draw(sheet)

    f_title = font("segoeuib.ttf", 40)
    f_num = font("segoeuib.ttf", 30)
    f_name = font("segoeui.ttf", 26)
    f_small = font("segoeui.ttf", 20)

    centered_text(d, (sheet_w / 2, margin + 34), "CLARET ATELIER THEME", f_title, ink)
    centered_text(d, (sheet_w / 2, margin + 82), "icon candidates", f_small, ink)

    for idx, (num, name, icon) in enumerate(icons):
        row, col = divmod(idx, 3)
        gx = margin + col * (cell_w + gap)
        gy = margin + head + row * (cell_h + gap)

        sheet.alpha_composite(icon.resize((260, 260), Image.LANCZOS),
                              (gx + (cell_w - 260) // 2, gy + 30))

        centered_text(d, (gx + cell_w / 2, gy + 330), num, f_num, ink)
        centered_text(d, (gx + cell_w / 2, gy + 372), name, f_name, ink)
        centered_text(d, (gx + cell_w / 2, gy + 404), "1024 x 1024  PNG", f_small, ink)

        thumb = icon.resize((32, 32), Image.LANCZOS)
        tx, ty = gx + cell_w - 32 - 22, gy + cell_h - 32 - 22
        d.rectangle([tx - 10, ty - 10, tx + 42, ty + 42],
                    outline=(ink[0], ink[1], ink[2], 70), width=1)
        sheet.alpha_composite(thumb, (tx, ty))

    save_png(sheet.convert("RGB"), path)


def inline_strip(icons, path):
    size, gap, margin = 150, 18, 30
    strip_w = margin * 2 + size * len(icons) + gap * (len(icons) - 1)
    strip_h = margin * 2 + size + 34
    strip = Image.new("RGBA", (strip_w, strip_h), LIGHT_BG)
    d = ImageDraw.Draw(strip)
    f_num = font("segoeuib.ttf", 20)

    for idx, (num, _name, icon) in enumerate(icons):
        x = margin + idx * (size + gap)
        strip.alpha_composite(icon.resize((size, size), Image.LANCZOS), (x, margin))
        centered_text(d, (x + size / 2, margin + size + 16), num, f_num, LIGHT_INK)

    save_png(strip.convert("RGB"), path)


def save_png(img, path):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(buf.getvalue())


def main():
    os.makedirs(OUT, exist_ok=True)

    icons = []
    for num, name, fn in CANDIDATES:
        icon = fn()
        box = icon.getbbox()
        if box is None:
            raise AssertionError("%s rendered empty" % name)
        left, top, right, bottom = box
        lo, hi = 70, 954
        if left < lo or top < lo or right > hi or bottom > hi:
            raise AssertionError("%s out of safe area: %s" % (name, box))
        path = os.path.join(OUT, "%s-%s.png" % (num, name))
        save_png(icon, path)
        print("wrote", os.path.relpath(path, ROOT), box)
        icons.append((num, name, icon))

    contact_sheet(icons, LIGHT_BG, LIGHT_INK, os.path.join(OUT, "contact-light.png"))
    contact_sheet(icons, DARK_BG, DARK_INK, os.path.join(OUT, "contact-dark.png"))
    inline_strip(icons, os.path.join(OUT, "inline-strip.png"))
    print("wrote contact-light.png / contact-dark.png / inline-strip.png")


if __name__ == "__main__":
    main()
