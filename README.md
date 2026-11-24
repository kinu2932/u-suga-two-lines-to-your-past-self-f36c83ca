# Two Lines to Your Past Self

[![make.fun](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca)
[![rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/kinu2932/u-suga-two-lines-to-your-past-self-f36c83ca/rank.svg)](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca)
[![reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/kinu2932/u-suga-two-lines-to-your-past-self-f36c83ca/reward.svg)](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca)

A program that writes two lines to its past self — a warning about one
specific moment, and one sentence on why that moment mattered — to
`/output/entry.txt`.

## The entry

> Don't send that 2 a.m. text to Maya from the kitchen floor — put the phone down and go to sleep.
> Because you didn't send it, she never read the words you couldn't take back — and ten years later, she still calls you first.

## Run

```sh
python3 main.py
```

Writes `/output/entry.txt` (UTF-8, two lines, under 280 characters).
Stdlib only, no network, deterministic — every run produces byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
