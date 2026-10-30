# Changes from the n = 218 analysis to the n = 211 analysis

> **Historical.** This file documents the n = 218 → n = 211 step. The current analysis is n = 171 (Years 2–4+); see `changes_from_n211.md`. The n = 218 and n = 211 analyses were internal working stages and were never submitted; the previously submitted manuscript analysed the full survey (N = 424).

**What changed in the sample.** Seven respondents chose a university year but
named a school as their institution:

- 4 named a Higher Secondary School (Classes 11–12);
- 3 named a Secondary School (Classes 6–10).

Their stage is contradictory, and they may be school pupils under 18, so they
are now excluded.

- **Record numbers in the original full survey file** (header = record 1): 100,
  153, 288, 295, 308, 324, 428.
- **Record numbers in the former 218-row university file:** 26, 64, 138, 143,
  154, 162, 217.
- **Their reported years:**
  - Year 1: 3
  - Year 2: 1
  - Year 3: 2
  - Year 4+: 1
- **Their gender:** 6 male, 1 female.

Five other changes besides the sample:

- **Models now run on all respondents:** the mediation and the gender, STEM and
  year interaction tests use all 211 rows. Before, they used the 216
  focus-complete rows.
- **Models that still use the focus-complete subset (n = 209):** the
  self-regulation regression, the hierarchical regression and Harman's test.
- **New analyses added:**
  - an age-sensitivity check (Years 2–4+, n = 171);
  - CIs for the convergent correlations;
  - a precision table (CI around r = .15 at each comparison study's N);
  - the sample size needed for r = .12.
- **Gender label:** "Other" is now "Prefer not to say", the form's exact wording.
- **Unchanged:** the seed (20260618) and all codings.

Old values come from `outputs/university/summary.json` produced by the n = 218
script at commit 55bbf79. New values come from the current `summary.json`.

## Results that crossed p = .05

| Result | n = 218 | n = 211 | Direction |
|---|---|---|---|
| SSCE vs task-switching, raw p (H2) | r = −.139, p = .041 | r = −.119, p = .084 | **significant → not significant** |
| Task-switching β in the self-regulation regression | β = −.165, p = .020 (n = 216) | β = −.141, p = .051 (n = 209) | **significant → not significant** |
| Perceived control, Holm-adjusted p (5 tests) | .064 | .040 | **not significant → significant** (BH: .040 → .025, significant in both) |
| Exposure–efficiency r, build with open band = 10 h, selected denominator | r = −.140, p = .040 | r = −.131, p = .057 | **significant → not significant**; share-based builds significant: 3 of 4 → 2 of 4 |
| Cluster-excluded SSCE vs task-switching | r = −.15, p = .037 (n = 188) | r = −.13, p = .077 (n = 181) | **significant → not significant** |
| Study time by subject, Kruskal–Wallis p | .080 | .033 | **not significant → significant** (ANOVA p .043 → .015, significant in both) |

No result moved from significant to not significant *after* Holm or BH
correction. Among the convergent correlations, the only correction-level change
is perceived control, which became significant under Holm. Task-switching was
already not significant after correction (Holm .122, BH .068) and remains so
(Holm .252, BH .140).

## Other notable changes (no change in significance)

| Result | n = 218 | n = 211 | Note |
|---|---|---|---|
| Exposure–efficiency r (H1) | −.149, p = .028, CI [−.28, −.02] | −.141, p = .040, CI [−.27, −.01] | Weaker; still p < .05 |
| Exposure–efficiency slope, bootstrap 95% CI | [−0.041, −0.001] | [−0.040, +0.0001] | **Now reaches zero**: the bootstrap CI includes 0, but the Fisher CI for r does not |
| r without the lowest band | −.06, p = .370 (n = 205; 13 students < 2 h) | −.07, p = .338 (n = 199; 12 students) | Unchanged conclusion |
| Mediation total effect c | −.134, p = .0496 (n = 216) | −.141, p = .040 (n = 211) | Different n; was reported as ".050" |
| Mediation b path | −.11, p = .118 | −.08, p = .250 | Weaker |
| Mediation indirect | −.036 [−.089, .010] | −.026 [−.076, .021] | Still not significant |
| Year differences (ANOVA) | study p = .055, SSCE p = .054 | study p = .105, SSCE p = .108 | Further from significance |
| Perceived control r | +.163, p = .016 | +.177, p = .010 | Stronger |
| Workload r | +.243 | +.239 | Unchanged |
| Ease of focus r | +.068, p = .321 | +.108, p = .120 | Still not significant |
| Regression R², F | .117, F(4, 211) = 7.00 | .116, F(4, 204) = 6.70 | Unchanged |
| Control β | +.132, p = .071 | +.142, p = .058 | Still not significant |
| Hierarchical ΔR² | .104, F(4, 203) = 6.34 | .105, F(4, 196) = 6.19 | Unchanged |
| Harman first factor | 32.2% | 33.0% | Unchanged |
| STEM discriminant r | +.11, p = .114 | +.12, p = .084 | Still not significant |
| Gender TOST, study time | p = .021 | p = .039 | Still equivalent |
| Cluster-excluded exposure r | −.225 (n = 188) | −.222 (n = 181) | Unchanged |
| Smallest r at 80% power | .189 | .192 | ≈ .19 in both |

## New results (n = 211 only)

- **Age sensitivity, Years 2–4+ (n = 171):**
  - Exposure r = −.15, 95% CI [−.30, −.004], p = .045; Holm (4 tests) p = .135.
  - Workload r = +.25, p = .001.
  - Control r = +.13, p = .096.
  - Task-switching r = −.10, p = .183.
  - Regression (n = 169): R² = .10, F(4, 164) = 4.70, p = .001. Only workload
    is significant: β = +.27, p < .001.
- **Task-switching r 95% CI:** [−.25, .02].
- **Precision:** the CI around r = .15 at n = 211 is [.02, .28], a half-width of
  .13. Detecting r = .12 with 80% power needs n = 543.

## How the manuscript narrative changed

- **H2:** now "supported for workload and perceived control, not for
  task-switching". Before, task-switching was described as a significant
  correlate.
- **Regression:** workload is now the only significant predictor. Before,
  workload and task-switching were both significant, and Figure U5's caption
  said so.
- **H1:**
  - It is now described as the weakest main finding, not the clearest.
  - It is significant in 2 of 4 builds.
  - The slope bootstrap CI reaches zero.
- **Abstract, plain-language summary, Discussion, Limitations and Conclusion:**
  rewritten to match the points above.

## Full key-by-key diff

The complete list of every changed `summary.json` value (428 keys) is in
`docs/changes_from_n218_allkeys.md`. It was generated by comparing the two
`summary.json` files. Keys that exist in only one run are marked.
