# Pandas Eğitimi: Design

Date: 2026-11-15. Status: draft, awaiting approval. Language of all course material: **Turkish**. This document is in English.

## Intent
A 1.5-2 hour hands-on training for beginners (know Python basics, nothing about numpy/pandas). Everyone codes along on their own laptop. One story runs through the session: a class of randomly generated students (ID, name, midterm, final) ends up with letter grades AA-FF via Turkish *bağıl değerlendirme* (curve grading). The statistics behind it are explained, not just coded.

## Goals
- Students leave able to: create/use numpy arrays and random numbers; build and inspect a DataFrame; select, filter, add columns; use `describe`, `value_counts`, `sort_values`, `apply`/`np.select`; plot a histogram.
- Students understand mean, standard deviation, normal distribution (bell curve), z-score, T-score, and why curve grading uses them.
- Students end with a letter-grade column they computed themselves.

## Non-goals
- No groupby/merge/time series, no advanced stats, no installing Marp on student machines.
- Not a reference manual; breadth is limited to what the story needs.

## Anti-goals
- A session where students paste code they don't understand, or where numbers differ per laptop so the instructor can't help.
- Statistics presented as a black box.

## Constraints
- Students have Python, VS Code, Git Bash. They install `numpy pandas matplotlib` via pip.
- **Students type everything from scratch** (decided): no starter file with TODO gaps.
- Shared seed (`np.random.seed(42)` / `default_rng(42)`) so all laptops produce identical data.

## Decided with the instructor
- Data: ID, name, midterm, final; weighted average 40% midterm / 60% final (weights are an adjustable constant; my default).
- Curve grading with this table (default, cutoffs are named constants):

| T-score | Letter |
|---|---|
| ≥ 60 | AA |
| 55-59.99 | BA |
| 50-54.99 | BB |
| 45-49.99 | CB |
| 40-44.99 | CC |
| 35-39.99 | DC |
| 30-34.99 | DD |
| 25-29.99 | FD |
| < 25 | FF |

- Statistics to explain with slides + small examples: mean, variance/standard deviation, normal distribution, z = (x − mean)/std, T = 50 + 10·z, why ~68% fall within ±1 std.

## Deliverables (my calls unless marked)
1. `slides/egitim.md`: Marp deck, Turkish, short segments, each ending with the code students type. Exported to HTML/PDF by the instructor.
2. `atolye/atolye-rehberi.md`: step-by-step workshop guide with tasks and 2-3 open challenges (e.g. who failed, top 5, grade distribution). No code gaps; shows expected output so students can self-check.
3. `cozum/cozum.py`: complete instructor solution, runnable end to end.
4. `README.md`: instructor notes: setup, pip command, timing, how to export slides.

## Planned flow and timing (my guess, ~110 min)
1. Setup and check imports (10)
2. numpy: arrays, mean/std, random generation (15)
3. Statistics concepts: mean, std, bell curve (10)
4. pandas: DataFrame, head/info/describe, select/filter/new column (25)
5. Weighted average and sorting (10)
6. Histogram and bell curve with matplotlib (10)
7. z-score and T-score (10)
8. Letter grades with `np.select`/`pd.cut`, auto-FF rule (final < 45), `value_counts` (15)
9. Wrap-up and challenges (5+)

## Left to the builder
Turkish name pool for random names, number of students (~100 suggested so the curve looks bell-shaped), exact slide styling, clip scores to 0-100, exact wording of exercises.

## Open assumptions to confirm
- Auto-FF rule: final < 45 → FF (my default, common practice; easy to change or drop).
- Jupyter is not used; plain `.py` files in VS Code (my call, avoids kernel setup problems).

## Amendments after review (2026-11-15, my calls)
- **Sync safety:** data generation is one block students type verbatim in a single step; the guide shows the expected `df.head()` output so they can check they match. `veri/ogrenciler.csv` ships as a fallback (`pd.read_csv`). "From scratch" still holds: no TODO gaps.
- **One random API everywhere:** `rng = np.random.default_rng(42)`. Scores: `rng.normal(loc=60, scale=15)` for midterm and final, clipped to 0-100, then rounded. Never mix with `np.random.seed`.
- **Std convention:** population std, `ddof=0`, passed explicitly in numpy and pandas (the class is the whole population). One slide explains numpy vs pandas defaults.
- **Statistics teaching:** anchor z/T on one named student; overlay a hand-computed normal pdf on the histogram (no scipy); show the 68% rule via a pandas filter.
- **Auto-FF** is applied after the curve (curve computed on all students); simpler for teaching.
- **Cuttable steps** are marked in the guide so the histogram and letter grades always happen.
- **Tooling:** README uses `python -m pip install`; slides previewed/exported with the "Marp for VS Code" extension. `pd.cut(..., right=False)`; z computed on the unrounded weighted average.
- **Auto-FF threshold changed to final < 35** (was 45): with these data 45 failed 17/100 students, too skewed for a demo. Named constant `ALT_FINAL`.
- **Data creation removed from the course (instructor request):** students receive `ogrenciler.csv` and load it with `pd.read_csv`; the generator lives in `veri/uret.py` for the instructor only. This supersedes the 'verbatim data block' sync-safety item and the 'generate from scratch' constraint for data. The numpy section still shows `default_rng(42)` as a short demo.
