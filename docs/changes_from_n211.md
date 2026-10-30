# Changes from the n = 211 analysis to the n = 171 analysis

> The n = 218 and n = 211 analyses were internal working stages and were never submitted. The previously submitted manuscript analysed the full survey (N = 424).

**What changed in the sample.** All 40 first-year respondents are excluded from
the analysis and from the shared dataset.

- **Why:** age was not recorded, and first-year students are the only
  university group in which respondents under 18 are plausible.
- **When it was decided:** after the n = 211 results, including the Years 2–4+
  check, had been seen. The manuscript says so.
- **How the comparison is kept:** the n = 211 results are still reported, as a
  comparison (`y1in_*` keys). That comparison can run only where the unshared
  original file is present.

**Unchanged:**

- the exclusion of the 7 school-institution rows;
- the seed (20260618) and all codings;
- the rule that models including ease of focus use the focus-complete subset
  (now n = 169);
- the rule that every other model uses all 171 rows.

Old values come from `summary.json` produced by the n = 211 script (commit
7c7b1f2). New values come from the current run.

## Results that crossed p = .05

| Result | n = 211 | n = 171 | Direction |
|---|---|---|---|
| **Perceived control r (H2)** | +.177, p = .010; Holm .040, BH .025 | +.128, p = .096; Holm .386, BH .203 | **significant → not significant, raw and after Holm/BH correction** |
| SSCE by university year, ANOVA | p = .108 (4 groups) | p = .041 (3 groups) | **not significant → significant** (exploratory, unadjusted) |
| SSCE by university year, Kruskal–Wallis | p = .103 | p = .045 | **not significant → significant** |
| Exposure–efficiency r, builds with open band = 10 h and 11 h, selected denominator | p = .057, .078 | p = .046, .049 | **not significant → significant**; share-based builds significant: 2 of 4 → 4 of 4 |
| Exposure–efficiency r, all four count-based ("all 7") builds | +.142 to +.176, all p < .05 | +.125 to +.146, p = .056 to .102 | **significant → not significant** (the positive count-based association is no longer significant) |
| Screen time vs number of academic purposes | r = +.15, p = .027 | r = +.13, p = .086 | **significant → not significant** |
| Gender TOST, study time (equivalence within ±0.3 SD) | p = .039 (equivalent) | p = .115 | **equivalence shown → not shown** |
| Study time by device, ANOVA | p = .303 | p = .045 | **not significant → significant** (Kruskal–Wallis p = .051, not significant) |
| Cluster-excluded control r | p = .023 | p = .256 | **significant → not significant** |
| Cluster-excluded task-switching β | p = .040 | p = .102 | **significant → not significant** |

**Only change after Holm/BH correction.** Among the five convergent correlations,
the only change is perceived control, which moved from significant to not
significant. Workload remains significant after correction (Holm .002 → .006).

## Other notable changes

| Result | n = 211 | n = 171 |
|---|---|---|
| Exposure–efficiency r (H1) | −.141, p = .040, CI [−.27, −.01] | −.154, p = .045, CI [−.30, −.004] |
| Slope bootstrap CI | [−0.040, +0.0001] | [−0.044, +0.001]; includes zero in both |
| r without the lowest band | −.07, p = .338 (n = 199) | −.11, p = .160 (n = 162); still not significant, but less close to zero |
| Workload r | +.239, p < .001 | +.245, p = .001 |
| Task-switching r | −.119, p = .084 | −.102, p = .183 |
| Task-switching β in the regression | −.141, p = .051 | −.136, p = .088 |
| Regression R² | .116, F(4, 204) = 6.70 | .103, F(4, 164) = 4.70, p = .001 |
| Hierarchical ΔR² | .105, p < .001 | .090, p = .003 |
| Mediation indirect | −.026 [−.076, .021] | −.017 [−.064, .025]; not significant in both |
| Harman first factor | 33.0% | 30.4% |
| Cluster-excluded exposure r | −.222 (n = 181) | −.245 (n = 148) |
| Smallest r at 80% power | .192 | .213 |
| CI around r = .15 | [.015, .279] | [−.000, .293] |
| Respondents unique on year × gender × subject | 7 | 5 |

## How the manuscript narrative changed

- **H2:** now supported for workload only. Perceived control is reported as not
  significant, and as significant only when first-year students are included.
- **H1:** described as small, fragile and marginal:
  - significant in all 4 share-based builds, but only just (p = .045 to .049);
  - the bootstrap slope interval includes zero.
- **Count-based builds:** the "reversal in sign" is now described as positive
  but not significant.
- **Year differences:** SSCE differs across years, reported as exploratory and
  unadjusted.
- **Participants section:** a new subsection, "Why first-year students are
  excluded", cites five sources, each checked against the source:
  - the Majority Act 1875, s.3;
  - the Children Act 2013, s.4;
  - The Business Standard (2020) on the UGC rule;
  - CREATE Policy Brief 5 (2011);
  - Islam et al. (2022).
- **Limitations, Ethics and Consent:** now say the following.
  - The Year 2+ restriction was chosen after the n = 211 results were seen.
  - Year-2+ students would normally be 18 or older, but this cannot be verified
    for every individual.
  - The exclusions do not make the original data collection compliant.

## Full key-by-key diff

`docs/changes_from_n211_allkeys.md` lists every changed `summary.json` value.
