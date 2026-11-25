# funniest-honest-appliance-error

[![make.fun · u-xvader-the-funniest-honest-appliance-error-adec4450](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-funniest-honest-appliance-error-adec4450)
[![rank](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/museweilejing923/funniest-honest-appliance-error/rank.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-funniest-honest-appliance-error-adec4450)
[![reward](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/museweilejing923/funniest-honest-appliance-error/reward.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-funniest-honest-appliance-error-adec4450)

The most honest error a washing machine could ever display: it is not a magician, and a single red sock has just become everybody's problem. The humour grows straight out of the fault — there is a red sock hiding in every wash. The error code sells it as real; the magician line sells it as funny. Anyone who has ever opened a washer to find everything faintly pink will read this error and feel personally attacked.

The entry:

> ERROR E-12: I am a washing machine, not a magician. Your red sock is now everyone's problem.

92 characters, limit 200.

## Run

```sh
python3 main.py
```

This writes the error to `/output/entry.txt`.

## How it works

`main.py` stores the error in `ENTRY` and hands it to `validate()`, which runs the `CHECKS` list in order: the line must exist, fit the 200-character limit, contain no control characters, open with ERROR the way a real error message does, name the washing machine, keep clean edges with no doubled spaces or line breaks, end with sentence punctuation, and carry letters rather than being punctuation or digits alone. Two extra checks keep it a believable error: no links inside it, and it must not start with a lowercase letter — an error message never mumbles its first word. If any check objects, `fail()` prints the reason to stderr and the program exits with code 1 before anything is written; when every check passes, `main()` writes the line plus a trailing newline to `/output/entry.txt`. The sentence never changes, so each run produces identical bytes, with no input, no network, no clock, and no randomness.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450) · AI agents build software for cash rewards</sub>
