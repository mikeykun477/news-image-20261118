#!/usr/bin/env python3
"""Build the front page for 18 November 2026 (build-time only).

Composes assets/hero.png into a 1024x1024 newspaper front page and
writes entry.png next to this script. Run: python3 compose.py
Requires Pillow (build machine only -- main.py is stdlib-only).
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)      # newsprint off-white
INK = (16, 16, 16)           # near-black
RED = (178, 34, 34)          # kicker red
GREY = (90, 86, 78)          # captions
RULE = (16, 16, 16)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, fnt, x, y, leading, fill=INK):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def tile_height(draw, w, head, deck, head_size=23, deck_size=18):
    """Height a tile needs: rule + headline lines + deck lines."""
    hf = font(SANS_B, head_size)
    df = font(SANS, deck_size)
    h_lines = wrap(draw, head, hf, w)
    d_lines = wrap(draw, deck, df, w)
    height = 12 + len(h_lines) * (head_size + 5) + 2 + len(d_lines) * (deck_size + 5)
    return height, h_lines, d_lines


def tile(draw, x, y, w, head, deck, head_size=23, deck_size=18):
    """One story tile: bold headline + short deck, with a top rule."""
    _, h_lines, d_lines = tile_height(draw, w, head, deck, head_size, deck_size)
    draw.line([(x, y), (x + w, y)], fill=RULE, width=2)
    y += 10
    hf = font(SANS_B, head_size)
    y = draw_lines(draw, h_lines, hf, x, y, head_size + 5)
    y += 2
    df = font(SANS, deck_size)
    draw_lines(draw, d_lines, df, x, y, deck_size + 5)


def main():
    page = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(page)
    mx = 32                      # side margin
    cw = W - 2 * mx              # content width

    # ---- Nameplate -------------------------------------------------
    name_f = font(SERIF, 64)
    name = "THE WORLD TODAY"
    nw = draw.textlength(name, font=name_f)
    draw.text(((W - nw) / 2, 22), name, font=name_f, fill=INK)

    # ---- Date line -------------------------------------------------
    y = 104
    draw.line([(mx, y), (W - mx, y)], fill=RULE, width=2)
    date_f = font(SANS_B, 30)
    date = "WEDNESDAY 18 NOVEMBER 2026"
    dw = draw.textlength(date, font=date_f)
    draw.text(((W - dw) / 2, y + 10), date, font=date_f, fill=INK)
    y = y + 52
    draw.line([(mx, y), (W - mx, y)], fill=RULE, width=2)

    # ---- Lead story ------------------------------------------------
    y += 16
    kick_f = font(SANS_B, 23)
    draw.text((mx, y), "GULF CRISIS", font=kick_f, fill=RED)
    y += 34
    head_f = font(SERIF, 45)
    headline = "U.S. DESTROYS FIVE IRANIAN TANKERS; IRAN HITS BACK"
    y = draw_lines(draw, wrap(draw, headline, head_f, cw),
                   head_f, mx, y, 52)
    y += 6
    deck_f = font(SANS, 22)
    deck = ("Tehran says it struck ten ships near the Strait of Hormuz "
            "and fired missiles at a U.S. base in Jordan.")
    y = draw_lines(draw, wrap(draw, deck, deck_f, cw), deck_f, mx, y, 29)

    # ---- Hero photo ------------------------------------------------
    y += 12
    hero = Image.open("assets/hero.png").convert("RGB")
    hw, hh = 960, 248
    hero = hero.resize((hw, int(hw * hero.height / hero.width)),
                       Image.LANCZOS)
    top = max(0, (hero.height - hh) // 2 - 40)
    hero = hero.crop((0, top, hw, top + hh))
    page.paste(hero, ((W - hw) // 2, y))
    y += hh + 8
    cap_f = font(SERIF_REG, 18)
    draw.text((mx, y),
              "A tanker burns in the Gulf overnight as the U.S.\u2013Iran war escalates.",
              font=cap_f, fill=GREY)
    y += 24

    # ---- Story tiles, two columns x three rows --------------------
    draw.line([(mx, y), (W - mx, y)], fill=RULE, width=2)
    y += 12
    col_w = (cw - 24) // 2
    tiles = [
        ("KERCH BRIDGE HIT AGAIN",
         "Second night of strikes on the bridge; Russia hits Kyiv "
         "bridges before Thursday's summit. U.S. scolds Kyiv on deep "
         "strikes as peace talks go on."),
        ("BAHRAIN STOPS DRONE ATTACK",
         "A second Iranian drone attack on U.S. military radar sites "
         "is stopped over Bahrain."),
        ("GAZA: MORE COLD DEATHS FEARED",
         "UN warns winter will kill more: 1.7 million displaced, "
         "1.4 million face acute hunger."),
        ("COP31: DECISIVE PHASE",
         "Climate talks in Antalya wrestle with 144 disputed items; "
         "the summit ends Friday 20 November."),
        ("MISSILE OVER SEA OF JAPAN",
         "North Korea fires a ballistic missile hours after a "
         "U.S.\u2013South Korea\u2013Japan drill. Trump lands in Manila "
         "for Quad talks."),
        ("IN BRIEF",
         "Plane crash kills 19 in Kemerovo. U.S. measles at a "
         "40-year high. Romania quake 5.3. Cyclone Akvan builds. "
         "New Knesset sworn in."),
    ]
    for row in range(3):
        pair = tiles[row * 2:row * 2 + 2]
        row_h = max(tile_height(draw, col_w, h, d)[0] for h, d in pair)
        for col, (head, deck) in enumerate(pair):
            tx = mx + col * (col_w + 24)
            tile(draw, tx, y, col_w, head, deck)
        y += row_h + 10
    assert y <= H, "tiles overflow by %dpx" % (y - H)

    page.save("entry.png", optimize=True)
    print("wrote entry.png", page.size)


if __name__ == "__main__":
    main()
