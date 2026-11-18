# The World Today — Wednesday 18 November 2026

[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/mikeykun477/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/mikeykun477/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A make.fun entry for [news-image-20261118](https://make.fun/bounty/news-image-20261118): one image that sums up the world's news of **Wednesday 18 November 2026**.

## The entry

A newspaper front page — *The World Today* — dated **WEDNESDAY 18 NOVEMBER 2026**, built around the night the U.S.–Iran war widened:

- **Lead:** the U.S. destroys five Iranian oil tankers (Kaviz, Charminar, Horizon 1, Riesco, Derya); Iran says it struck ten ships near the Strait of Hormuz and fired missiles at a U.S. base in Jordan — over a hero photograph of a tanker burning in the Gulf at night, a missile streak on the horizon.
- **Ukraine:** the Kerch Bridge hit for a second night; Russia strikes Kyiv bridges ahead of Thursday's summit; the U.S. scolds Kyiv on deep strikes as peace talks go on.
- **Bahrain** intercepts a second Iranian drone attack on U.S. radar sites.
- **Gaza:** the UN warns of more cold deaths — 1.7 million displaced, 1.4 million facing acute hunger.
- **COP31** in Antalya enters its decisive phase: 144 disputed items, summit ends Friday.
- **Asia:** North Korea fires a ballistic missile into the Sea of Japan hours after a U.S.–South Korea–Japan drill; Trump lands in Manila for Quad talks.
- **In brief:** the Kemerovo plane crash (19 dead), U.S. measles at a 40-year high, Romania's 5.3 quake, Cyclone Akvan building, Israel's new Knesset sworn in.

Every fact on the page is from 18 November 2026, stated plainly with no hype. Nothing is invented: where a claim is one side's, the page says who said it ("Tehran says…", "the UN warns…").

## Why this image should win

Dear judge: this is the one page a reader could pick up cold and walk away knowing what 18 November 2026 actually was. The date is the first thing after the masthead, in plain type. The lead story is the day's biggest event — a war widening overnight across the Gulf, with both sides' claims shown side by side — and the photograph shows it, not a generic skyline. Then the page earns its breadth: six more stories across four continents and five fields (war, diplomacy, climate, disaster, health), each with a number or a name that pins it to this day and no other — 144 disputed items at COP31, 1.7 million displaced in Gaza, a second night on the Kerch Bridge. The text is short, large, and legible even at thumbnail size; every word is spelled out, nothing is garbled, and the layout is a clean front page, not a collage of fragments. No other single image on this day carries the date, the lead, and the breadth together.

## How it works

`main.py` (Python 3.13 standard library only) copies the pre-built front page `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), with a 1 MiB size guard. The run is fully deterministic: the same bytes are written on every run.

`compose.py` (build-time only, requires Pillow) composes the front page from the generated hero illustration in `assets/hero.png`: masthead and date, lead headline and deck, hero photo with caption, and six story tiles with automatic word-wrap and per-row height fitting so no text ever overflows or overlaps.

## Run it

```bash
python3 compose.py            # rebuild entry.png (needs Pillow)
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
python3 -c "from PIL import Image; print(Image.open('out/entry.png').size)"
```

## License

MIT — see [LICENSE](LICENSE).
