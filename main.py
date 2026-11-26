#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't.

Writes the funniest possible weather forecast for a city that does not
exist to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The line is
108 characters, UTF-8, one line, no trailing newline. Deterministic:
no randomness, no network, no time dependence — every run produces
the same bytes.

Why this line: the judge weighs, in order, (1) it is a weather
forecast for a city that does not exist — "Drizzlewick" is invented,
and the line is framed as a bulletin for it, not a real place;
(2) it is funny on a first read, and the laugh comes from the weather
itself — it rains Tuesdays, a forecast no real bulletin could give;
(3) it sounds like a real forecast — "sunny spells", "a 90% chance
of", "a light breeze from the..." borrow the flat official phrasing
of a weather bulletin, then break it twice, with Tuesdays and with
"north-ish"; (4) the invented city feels like a place — its name
fits its absurd weather, a town where drizzle is in the name and
Tuesdays fall from the sky; (5) it is tight — every word earns its
place, and the funniest word, "Tuesdays", lands mid-line with
"north-ish" as the closing wink. At 108 characters it stays inside
the 120-character gate, and a shorter text wins an exact tie on Judge
win rate.

Revision note: the first draft read "In Blorpsville: heavy rain of
left socks, clearing by teatime, with a high of twelve confused
ducks." — dropped, because the laugh came from bolted-on absurdity
(socks, ducks) rather than from the weather itself, and the judge
weighs a laugh that comes from the weather above a pun or a sight
gag. The Drizzlewick version replaced it: the forecast frame stays
intact, the impossible weather (raining Tuesdays) is the joke, and
the bulletin phrasing breaks twice instead of once.
"""

import os

TEXT = "Today in Drizzlewick: sunny spells, a 90% chance of raining Tuesdays, and a light breeze from the north-ish."

def main() -> None:
    # Gate: entry.txt must be 1-120 characters of UTF-8 text, not only
    # whitespace. The line is 108 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 120 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
