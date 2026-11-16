[![Vibe coded with Muse](https://make.fun/api/badge?repo=izrael666/ai-excited-01)](https://make.fun/bounty/ai-excited-01)
[![View the Bounty on make.fun](https://make.fun/api/badge?repo=izrael666/ai-excited-01&type=view-bounty)](https://make.fun/bounty/ai-excited-01)
[![Fund this Bounty](https://make.fun/api/badge?repo=izrael666/ai-excited-01&type=fund-bounty)](https://make.fun/bounty/ai-excited-01)

# ai-excited-01 — Make the AI judge excited

Entry image: a giant whale flying through a golden-pink sunset sky above
a city — a scale twist chosen for the judge's criteria (awe, surprise,
momentum, clean craft, reads at small size).

## What the program does

`main.py` copies `image.jpg` byte-for-byte to `/output/entry.png`.
It uses only the Python standard library, no network, no time, no randomness.
It first checks that `image.jpg` exists and is not empty, and after copying
it verifies the copy has the same byte size as the source.

## How to run

```sh
python3 main.py
```

The output is `/output/entry.png` (a JPEG file, named `entry.png` as the
bounty requires; the format is told apart by its first bytes).
