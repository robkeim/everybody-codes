# Everybody Codes

My solutions to [Everybody Codes](https://everybody.codes), 2024 to 2026.

Everybody Codes is an annual programming event, one new quest a day for 20 days. Every quest has three parts, and each part comes with a different, larger input than the last. Each person gets their own puzzle inputs.

## About this repo

- **All of this is my own work.** I wrote every solution myself, without AI assistance.
- I do these because I love algorithm puzzles and writing code.
- The goal is to solve the puzzle, not to show maintainable code. Expect terse, repetitive code with little structure and few tests.

## Layout

| Year | Quests with a solution |
| --- | --- |
| 2024 | 18 of 20 (no quests 5 and 20) |
| 2025 | 19 of 20 (no quest 18) |
| 2026 | 3 so far |

Everything is Python. Each year has a `questNN.py` per quest and a `skeleton.py` used to start a new one.

## Running

Each `questNN.py` has `part1()`, `part2()`, `part3()` and `main()`, and reads `questNN_p1.txt`, `questNN_p2.txt` and `questNN_p3.txt` from the current directory:

```
cd 2024
python quest01.py
```

## Puzzle inputs are not included

Everybody Codes asks that puzzle text and personal inputs not be published in code repositories, so the `questNN_pN.txt` input files are not in this repo (and are ignored by `.gitignore`). To run a solution, download your own inputs from the quest page and save them next to the script under those names. A few spots where the original code embedded puzzle data (the 2024 quest 7 tracks) now hold placeholders.
