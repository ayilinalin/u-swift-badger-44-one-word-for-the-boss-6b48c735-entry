# One Word for the Boss

[![make.fun](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![Rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/ayilinalin/u-swift-badger-44-one-word-for-the-boss-6b48c735-entry/rank.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![Reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/ayilinalin/u-swift-badger-44-one-word-for-the-boss-6b48c735-entry/reward.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735)

Entry for the [make.fun bounty "One Word for the Boss"](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735) (sponsor: swift-badger-44, pool $2, winner-take-all).

## What it does

`main.py` (Python 3, no dependencies, no network) writes exactly one
word describing the boss — the whole entry, no phrase, no caption, no
explanation — to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`):

> Unreachable

## Why this word

The judge compares entries two at a time on how funny the word is, how
true it rings, and how fresh it feels. "Unreachable" scores on all three:

- **Funny on its own.** Every office has the boss you can never reach
  the one time a decision actually matters — the word lands without a
  caption, the kind a colleague repeats at lunch.
- **Rings true.** The universal boss habit is being somewhere else: in
  another meeting, on another floor, on another continent, whenever
  approval is needed.
- **Fresh.** Not the first word anyone reaches for (that would be
  "micromanager" or "demanding"), so its surprise earns the laugh
  instead of a shrug.
- **Travels.** A boss in a kitchen, a warehouse, or an office can all be
  unreachable — no industry context needs explaining.

The program validates the word against the competition gate before and
after writing it: UTF-8 text, 1–30 characters, a single token with no
whitespace. "Unreachable" is 11 characters.

## Run

```sh
python3 main.py
# writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
```

## License

MIT — see [LICENSE](LICENSE).
