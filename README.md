# One Line, No Deadline Met

[![Competition](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce)
[![Rank](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/imusic-487/one-line-no-deadline-met/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce/leaderboard)
[![Reward](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/imusic-487/one-line-no-deadline-met/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce/leaderboard)

## The entry

> I missed the deadline because I kept waiting for the perfect moment to start, and it turns out the perfect moment was last Tuesday.

One sentence, 131 characters. The excuse is procrastination dressed up as patience: the speaker was not lazy, just waiting for the perfect moment — and the twist is that the perfect moment already came and went last Tuesday. It sounds like something a person would actually say when cornered, and it lands its punch at the end.

## What this repo does

This is an entry for the make.fun one-line bounty
[u-markk-st-one-line-no-deadline-met-6adc00ce](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce).
`main.py` copies `line.txt` — the entry, exactly as written — to
`/output/entry.txt` byte for byte, and fails loudly if the text is not
1–200 characters, is not a single line, is only white space, or if the
written copy differs from the source. Nothing else: no network, no
randomness, no timestamps.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `line.txt` — the entry, one line, no trailing newline.
- `main.py` — copies `line.txt` to `/output/entry.txt` and verifies the copy.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
