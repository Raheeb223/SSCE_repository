#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Screen-to-study conversion efficiency among university students
University students in Years 2 to 4 and above (n = 171)
================================================================================
Reproduces every number and figure in the university-only manuscript from
data/SSCE_survey_university.csv. Variable construction, codings, seed
(20260618) and statistical methods are identical to those of the original
full-survey analysis; only the sample differs. Respondents who chose a university year but named a
school as their institution, and all first-year respondents, are excluded (see
LOAD). Models that include ease
of focus use the focus-complete subset; every other model uses all respondents.
Analyses that need school stages (Class 11-12 contrast,
specification curve, permutation and leave-one-out tests on that contrast,
AR(1) persistence, school/university moderation) are not run.

USAGE (from the repository root):  python scripts/university_analysis.py
       optional:                    python scripts/university_analysis.py <csv>
OUTPUT: outputs/university/  (RESULTS.txt, summary.json, table_*.csv,
                              opentext_coded_university.csv)
        figures/university/  (figures, 300 dpi, no titles; captions in manuscript)
================================================================================
"""
import os, sys, re, json, math, glob, platform, warnings
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
from sklearn.decomposition import PCA
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
SEED = 20260618
RNG = np.random.default_rng(SEED)
N_BOOT = 10000

MID_HIGH = 9.0          # midpoint for the ">8 hours" band (as 01_main_analysis.py)
PROP_MODE = "selected"  # canonical denominator (as 01_main_analysis.py)
N_PURPOSE_OPTIONS = 7   # used only by the 'all' robustness builds

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "data", "SSCE_survey_university.csv")
if not os.path.isfile(DATA):
    sys.exit(f"Survey CSV not found: {DATA}")
OUTDIR = os.path.join(ROOT, "outputs", "university")
FIGDIR = os.path.join(ROOT, "figures", "university")
os.makedirs(OUTDIR, exist_ok=True); os.makedirs(FIGDIR, exist_ok=True)

LOG = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); LOG.append(s)

RES = {}   # every reported value, saved to summary.json
def rec(key, value):
    RES[key] = float(value) if isinstance(value, (np.floating, np.integer)) else value
    return value

plt.rcParams.update({
    "figure.dpi": 110, "savefig.dpi": 300, "font.size": 11,
    "axes.titlesize": 12, "axes.titleweight": "bold", "axes.spines.top": False,
    "axes.spines.right": False, "axes.grid": True, "grid.alpha": 0.25,
    "axes.axisbelow": True, "figure.autolayout": True,
})
C1, C2, C3 = "#2c5f8a", "#c0504d", "#7f7f7f"
# five-slot categorical palette for the device chart (passes the CVD and
# normal-vision separation checks; the 01 script's five-colour set does not)
DEV_COLS = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]

# ============================================================ CONSTRUCTION ===
# identical to build() in 01_main_analysis.py
STAGE_MAP = {"Class 6": 1, "Class 7": 2, "Class 8": 3, "Class 9": 4, "Class 10": 5,
             "Class 11": 6, "Class 12": 7, "1st Year College/University": 8,
             "2nd Year College/University": 9, "3rd Year College/University": 10,
             "4th Year or above College/University": 11}
YEARS = [9, 10, 11]                      # Year 1 (stage 8) is excluded; see LOAD
YEAR_LABELS = ["Uni Y2", "Uni Y3", "Uni Y4+"]
SCREEN_BASE = {"Less than 2 hours": 1.0, "2 to 4 hours": 3.0, "4 to 6 hours": 5.0, "6 to 8 hours": 7.0}
STUDY_KEYS = ["attending online classes", "doing homework", "researching for projects",
              "reading digital textbooks", "watching educational videos"]
FLAG = "cluster_sensitivity_flag"

def split_multi(cell):
    """';' (Forms export) or ', ' (de-identified file); commas inside
    '(Instagram, Facebook, ...)' belong to the option label."""
    return [p.strip() for p in re.split(r";|,\s+(?![^()]*\))", str(cell)) if p.strip()]

def resolve(df, *kw):
    for c in df.columns:
        if all(k.lower() in c.lower() for k in kw):
            return c
    raise KeyError(f"No column matching {kw}")

def build(df_raw, mid_high=MID_HIGH, prop_mode=PROP_MODE):
    df = df_raw.copy()
    COL = {"gender": resolve(df, "gender"), "grade": resolve(df, "grade"),
           "subject": resolve(df, "main area"), "screen": resolve(df, "total", "hours"),
           "purpose": resolve(df, "screen time mainly for"), "device": resolve(df, "MOST for studying")}
    df["stage"] = df[COL["grade"]].apply(lambda v: STAGE_MAP.get(str(v).strip(), np.nan))
    df = df.dropna(subset=["stage"]).copy(); df["stage"] = df["stage"].astype(int)
    mid = dict(SCREEN_BASE); mid["More than 8 hours"] = mid_high
    df["screen_mid"] = df[COL["screen"]].map(mid)
    def prop(cell):
        if pd.isna(cell): return np.nan
        parts = split_multi(cell)
        if not parts: return np.nan
        n_study = sum(any(k in p.lower() for k in STUDY_KEYS) for p in parts)
        denom = len(parts) if prop_mode == "selected" else N_PURPOSE_OPTIONS
        return n_study / denom
    df["study_prop"] = df[COL["purpose"]].apply(prop)
    df["study_hours"] = df["screen_mid"] * df["study_prop"]
    df = df.dropna(subset=["study_hours"]).copy()
    df["ssce"] = df["study_prop"]
    def _focus(v):
        m = re.match(r"\s*(\d)", str(v)); return int(m.group(1)) if m else np.nan
    df["focus"] = df[resolve(df, "easy is it for you to focus")].apply(_focus)
    df["control"] = pd.to_numeric(df[resolve(df, "feel in control")], errors="coerce")
    _SW = {"rarely": 1, "occasionally": 2, "very often": 4, "often": 3}
    df["switch"] = df[resolve(df, "switch tasks")].apply(
        lambda v: next((_SW[k] for k in _SW if k in str(v).lower()), np.nan))
    _WL = {"light": 1, "moderate": 2, "very heavy": 4, "heavy": 3}
    df["workload"] = df[resolve(df, "academic workload")].apply(
        lambda v: next((_WL[k] for k in _WL if k in str(v).lower()), np.nan))
    _TH = {"very distracting": 1, "somewhat distracting": 2, "neutral": 3,
           "somewhat helpful": 4, "very helpful": 5}
    df["tech_helps"] = df[resolve(df, "helps your learning")].apply(
        lambda v: next((_TH[k] for k in _TH if k in str(v).lower()), np.nan))
    df["gender"] = df[COL["gender"]].apply(
        lambda x: "Male" if str(x).strip().lower().startswith("male")
        else "Female" if str(x).strip().lower().startswith("female")
        else "Prefer not to say")         # the form's third option, verbatim
    def subj(x):
        s = str(x).lower()
        if any(k in s for k in ["science", "engineering", "math"]): return "STEM"
        if any(k in s for k in ["commerce", "business", "econom"]): return "Commerce"
        if any(k in s for k in ["arts", "humanities", "language", "history", "philosophy"]): return "Arts"
        return "Other"
    df["subject"] = df[COL["subject"]].apply(subj)
    df["stem"] = (df["subject"] == "STEM").astype(int)
    def dev(x):
        s = str(x).lower()
        if "tablet" in s and "without" not in s: return "Tablet"
        if "laptop" in s or "desktop" in s: return "Mixed" if "phone" in s else "Laptop/Desktop"
        if "smartphone" in s or s.strip() == "phone": return "Smartphone"
        if "all equally" in s: return "Mixed"
        return "Other"
    df["device"] = df[COL["device"]].apply(dev)
    return df

# ============================================================ STATS HELPERS ==
def holm(pvals):
    p = np.asarray(pvals, float); m = len(p); order = np.argsort(p)
    adj = np.empty(m); run = 0.0
    for i, idx in enumerate(order):
        run = max(run, (m - i) * p[idx]); adj[idx] = min(run, 1.0)
    return adj

def benjamini_hochberg(pvals):
    p = np.asarray(pvals, float); m = len(p); order = np.argsort(p)
    adj = np.empty(m); run = 1.0
    for rank in range(m, 0, -1):
        idx = order[rank - 1]; run = min(run, p[idx] * m / rank); adj[idx] = run
    return adj

def cohens_d(a, b):
    na, nb = len(a), len(b)
    if na < 2 or nb < 2: return np.nan
    sp = np.sqrt(((na-1)*a.var(ddof=1) + (nb-1)*b.var(ddof=1)) / (na+nb-2))
    return (b.mean() - a.mean()) / sp if sp > 0 else np.nan

def welch_ci(a, b):
    sa, sb, na, nb = a.var(ddof=1), b.var(ddof=1), len(a), len(b)
    se = np.sqrt(sa/na + sb/nb)
    dfree = (sa/na + sb/nb)**2 / ((sa/na)**2/(na-1) + (sb/nb)**2/(nb-1))
    t = stats.t.ppf(0.975, dfree); diff = b.mean() - a.mean()
    return diff - t*se, diff + t*se

def boot_ci(func, *arrays, n=N_BOOT, lo=2.5, hi=97.5):
    out = np.empty(n)
    for i in range(n):
        res = [RNG.choice(a, len(a), replace=True) for a in arrays]
        out[i] = func(*res)
    return np.percentile(out, [lo, hi])

def ols_standardized(Xraw, y, names):
    cols = [np.ones(len(y))]
    for i in range(Xraw.shape[1]):
        xi = Xraw[:, i]
        cols.append((xi - xi.mean()) / xi.std(ddof=0))
    X = np.column_stack(cols)
    yz = (y - y.mean()) / y.std(ddof=0)
    n, k = X.shape
    beta = np.linalg.lstsq(X, yz, rcond=None)[0]
    res = yz - X @ beta
    dof = n - k
    se = np.sqrt(np.diag((res @ res / dof) * np.linalg.inv(X.T @ X)))
    t = beta / se
    p = 2 * stats.t.sf(np.abs(t), dof)
    r2 = 1 - (res @ res) / ((yz - yz.mean()) ** 2).sum()
    adj = 1 - (1 - r2) * (n - 1) / dof
    F = (r2 / (k - 1)) / ((1 - r2) / dof)
    pF = stats.f.sf(F, k - 1, dof)
    return dict(names=names, beta=beta[1:], se=se[1:], p=p[1:],
                r2=r2, adj=adj, F=F, pF=pF, n=n, dof=dof)

def r_ci(r, n):
    """Fisher-z 95% CI for a Pearson r."""
    z, se = np.arctanh(r), 1 / np.sqrt(n - 3)
    return np.tanh(z - 1.96 * se), np.tanh(z + 1.96 * se)

def power_r(r, n, alpha=0.05):
    """Two-tailed power for a correlation, Fisher-z approximation."""
    zc = stats.norm.ppf(1 - alpha / 2); zr = np.arctanh(r) * np.sqrt(n - 3)
    return stats.norm.cdf(zr - zc) + stats.norm.cdf(-zr - zc)

def fmt_p(p):
    """'p < .001' or 'p = .028'."""
    return "p < .001" if p < .001 else f"p = {p:.3f}".replace("0.", ".")

# ============================================================ LOAD ============
raw = pd.read_csv(DATA)
if FLAG not in raw.columns:
    raise KeyError(f"Required column not found: {FLAG}")
say(f"Loaded {os.path.basename(DATA)}: {len(raw)} rows, {raw.shape[1]} columns")
# Exclude respondents who chose a university year but named a secondary or
# higher-secondary school as their institution. Their stage is contradictory,
# and they may be school pupils under 18, who took part without parental consent
# or ethics review and must not be analysed. The shared file already omits them;
# the filter is kept so the script enforces the rule on any input.
INST = resolve(raw, "type of institution")
school_inst = ~raw[INST].astype(str).str.strip().str.startswith("College/University")
rec("n_input_rows", len(raw)); rec("n_excluded_school_institution", int(school_inst.sum()))
say(f"Excluded {int(school_inst.sum())} row(s) whose institution is a school "
    f"(records {[int(i) + 2 for i in raw.index[school_inst]]})")
raw = raw[~school_inst]
# Exclude first-year respondents. Age was not recorded, and first-year students
# are the only university group in which respondents under 18 are plausible (a
# pupil who started Class 1 at five could begin university at 17). Students in
# Year 2 or later have completed at least a year of university and would
# normally be 18 or older. The shared file already omits Year 1; the filter is
# kept so the script enforces the rule on any input.
GRADE = resolve(raw, "grade")
year1 = raw[GRADE].astype(str).str.strip().eq("1st Year College/University")
rec("n_excluded_year1", int(year1.sum()))
say(f"Excluded {int(year1.sum())} first-year row(s)")
raw = raw[~year1]
flags = raw[FLAG]
raw_items = raw.drop(columns=[FLAG])
df = build(raw_items)
df[FLAG] = flags.loc[df.index].values
if not set(df.stage.unique()) <= set(YEARS):
    sys.exit("Input contains non-university stages; this script analyses university years only.")
df["year"] = df.stage.map(dict(zip(YEARS, YEAR_LABELS)))
N = rec("N", len(df))
say(f"Analytic n = {N}  (dropped: {len(raw) - N}; construction MID_HIGH={MID_HIGH}, PROP_MODE='{PROP_MODE}')\n")

# where the university subset sits in the full survey file (only if that file is present)
FULL = os.path.join(ROOT, "data", "SSCE_survey.csv")
if os.path.isfile(FULL):
    _full = pd.read_csv(FULL)
    _lab = _full[resolve(raw, "grade")].astype(str).str.strip()
    _st = _lab.map(STAGE_MAP)
    _sch = ~_full[INST].astype(str).str.strip().str.startswith("College/University")
    n_full, n_school = len(_st), int(_st.between(1, 7).sum())
    n_uni, n_out = int(_st.between(8, 11).sum()), int(_st.isna().sum())
    _bad = _st.between(8, 11) & _sch
    n_bad = int(_bad.sum())
    for k, v in [("full_rows", n_full), ("full_school", n_school), ("full_uni", n_uni),
                 ("full_out_of_range", n_out), ("full_uni_school_institution", n_bad),
                 ("full_uni_university_institution", n_uni - n_bad)]:
        rec(k, v)
    rec("full_uni_school_institution_records", [int(i) + 2 for i in _full.index[_bad]])
    say(f"Full survey file: {n_full} rows = {n_school} school-stage (Class 6-12, excluded) + "
        f"{n_uni} university Years 1-4 + {n_out} outside the listed stages (excluded)")
    say(f"  outside the listed stages: {dict(_lab[_st.isna()].value_counts())}")
    say(f"  of the {n_uni} university-year rows, {n_bad} name a school as institution (excluded; "
        f"full-file records {[int(i) + 2 for i in _full.index[_bad]]}) -> {n_uni - n_bad} analysed")
    say(f"  their institution: {dict(_full.loc[_bad, INST].value_counts())}; "
        f"their year: {dict(_lab[_bad].value_counts())}")
    _y1 = _st.eq(8) & ~_sch
    rec("full_uni_year1_excluded", int(_y1.sum())); rec("full_analysed", n_uni - n_bad - int(_y1.sum()))
    say(f"  of the {n_uni - n_bad} remaining, {int(_y1.sum())} are first-year students (excluded) -> "
        f"{n_uni - n_bad - int(_y1.sum())} analysed\n")

# ============================================================ 1. SAMPLE =======
say("="*80); say("1. SAMPLE DESCRIPTION"); say("="*80)
samp = []
for var, order in [("year", YEAR_LABELS), ("gender", ["Male", "Female", "Prefer not to say"]),
                   ("subject", ["STEM", "Commerce", "Arts", "Other"]),
                   ("device", ["Laptop/Desktop", "Smartphone", "Mixed", "Tablet", "Other"])]:
    vc = df[var].value_counts()
    for cat in order:
        n = int(vc.get(cat, 0))
        samp.append(dict(variable=var, category=cat, n=n, pct=100 * n / N))
        rec(f"n_{var}_{cat}", n); rec(f"pct_{var}_{cat}", round(100 * n / N, 1))
        say(f"  {var:8s} {cat:15s} n={n:4d}  ({100*n/N:5.1f}%)")
SAMP = pd.DataFrame(samp)
DEVYR = pd.crosstab(df.year, df.device).reindex(index=YEAR_LABELS)
say("\nDevice by university year (counts):")
say(DEVYR.to_string())
say("")

# power for the correlations at this n
pw20, pw14 = power_r(0.20, N), power_r(0.14, N)
r80 = next(r / 1000 for r in range(1, 1000) if power_r(r / 1000, N) >= 0.80)
rec("power_r20", pw20); rec("power_r14", pw14); rec("min_r_80pct_power", r80)
say(f"Power (two-tailed alpha=.05, Fisher z, n={N}): r=.20 -> {pw20:.3f}; r=.14 -> {pw14:.3f}; "
    f"smallest r with 80% power = {r80:.3f}")
# precision: Fisher-z 95% CI around r = .15 at this n and at the sample sizes of
# the comparison studies (N from the sources: Junco & Cotten 2012; Lepp et al.
# 2015; Bjerre-Nielsen et al. 2020; Rosen et al. 2013; Lukram et al. 2026;
# Giunchiglia et al. 2018, analysed n)
PREC = []
for lab, n_ in [("this study", N), ("Junco & Cotten 2012", 1839), ("Lepp et al. 2015", 536),
                ("Bjerre-Nielsen et al. 2020", 470), ("Rosen et al. 2013", 263),
                ("Lukram et al. 2026", 102), ("Giunchiglia et al. 2018", 67)]:
    lo, hi = r_ci(0.15, n_)
    r80_ = next(x / 1000 for x in range(1, 1000) if power_r(x / 1000, n_) >= 0.80)
    PREC.append(dict(study=lab, n=n_, ci_lo=lo, ci_hi=hi, width=hi - lo, min_r_80=r80_))
    rec(f"prec_{lab}_n", n_); rec(f"prec_{lab}_ci", [lo, hi]); rec(f"prec_{lab}_width", hi - lo)
    rec(f"prec_{lab}_halfwidth", (hi - lo) / 2); rec(f"prec_{lab}_min_r_80", r80_)
PREC = pd.DataFrame(PREC)
# sample size needed for 80% power at the size of the task-switching estimate (|r| = .12)
n_r12 = next(n_ for n_ in range(10, 100000) if power_r(0.12, n_) >= 0.80)
rec("n_needed_r12_80pct", n_r12)
say(f"n needed for 80% power at r = .12: {n_r12} ({n_r12 / N:.1f} times this sample)")
say("95% CI around r = .15 (Fisher z) and smallest r with 80% power, by sample size:")
say(PREC.round(3).to_string(index=False)); say("")

# ============================================================ 2. BY YEAR ======
say("="*80); say("2. STUDY TIME, SCREEN TIME AND SSCE BY UNIVERSITY YEAR (95% t-intervals)"); say("="*80)
rows = []
for k, lab in zip(YEARS, YEAR_LABELS):
    sub = df[df.stage == k]
    row = dict(year=lab, n=len(sub))
    for v in ["study_hours", "ssce", "screen_mid"]:
        x = sub[v].values; n = len(x); mu = x.mean(); sd = x.std(ddof=1)
        h = stats.t.ppf(0.975, n - 1) * sd / np.sqrt(n)
        row.update({f"{v}_mean": mu, f"{v}_sd": sd, f"{v}_ci_lo": mu - h, f"{v}_ci_hi": mu + h})
        rec(f"{v}_mean_{lab}", mu); rec(f"{v}_sd_{lab}", sd)
        rec(f"{v}_ci_{lab}", [mu - h, mu + h])
    rows.append(row)
YR = pd.DataFrame(rows)
say(YR.round(3).to_string(index=False))
for v, lab in [("study_hours", "study time"), ("ssce", "SSCE"), ("screen_mid", "screen time")]:
    rec(f"{v}_mean_all", df[v].mean()); rec(f"{v}_sd_all", df[v].std(ddof=1))
    say(f"overall {lab}: mean={df[v].mean():.4f} (SD {df[v].std(ddof=1):.4f})")
say("")
for v, lab in [("study_hours", "study time"), ("ssce", "SSCE")]:
    groups = [df.loc[df.stage == k, v].values for k in YEARS]
    F, pA = stats.f_oneway(*groups); H, pK = stats.kruskal(*groups)
    grand = df[v].mean()
    eta2 = sum(len(g)*(g.mean()-grand)**2 for g in groups) / ((df[v]-grand)**2).sum()
    for key, val in [("anova_F", F), ("anova_p", pA), ("eta2", eta2), ("kw_H", H), ("kw_p", pK)]:
        rec(f"{v}_{key}", val)
    rec(f"{v}_anova_df", [len(YEARS) - 1, N - len(YEARS)])
    say(f"{lab:10s} by year: ANOVA F({len(YEARS)-1},{N-len(YEARS)})={F:.3f}, p={pA:.4f}, eta^2={eta2:.4f}; "
        f"Kruskal-Wallis H({len(YEARS)-1})={H:.3f}, p={pK:.4f}")
say("")

say("Adjacent-year differences in study time (ETG), Welch CI, Cohen's d (bootstrap CI),")
say(f"Holm and Benjamini-Hochberg adjustment across the {len(YEARS) - 1} comparisons:")
rows = []
for i in range(len(YEARS) - 1):
    a = df.loc[df.stage == YEARS[i], "study_hours"].values
    b = df.loc[df.stage == YEARS[i+1], "study_hours"].values
    t, p = stats.ttest_ind(b, a, equal_var=False)
    lo, hi = welch_ci(a, b); d = cohens_d(a, b); d_lo, d_hi = boot_ci(cohens_d, a, b)
    rows.append(dict(transition=f"{YEAR_LABELS[i]}->{YEAR_LABELS[i+1]}", n_a=len(a), n_b=len(b),
                     etg=b.mean()-a.mean(), ci_lo=lo, ci_hi=hi, welch_t=t, p_raw=p,
                     cohen_d=d, d_lo=d_lo, d_hi=d_hi))
ETG = pd.DataFrame(rows)
ETG["p_holm"] = holm(ETG.p_raw.values); ETG["p_bh"] = benjamini_hochberg(ETG.p_raw.values)
say(ETG.round(3).to_string(index=False))
for r in ETG.itertuples():
    for c in ["etg", "ci_lo", "ci_hi", "welch_t", "p_raw", "cohen_d", "d_lo", "d_hi", "p_holm", "p_bh"]:
        rec(f"etg_{r.transition}_{c}", getattr(r, c))
say(f">> {int((ETG.p_bh < .05).sum())}/{len(ETG)} adjacent-year differences significant after BH correction\n")

# ============================================================ 3. EXPOSURE =====
say("="*80); say("3. EXPOSURE-EFFICIENCY: SSCE vs SCREEN-TIME BAND"); say("="*80)
sc = df.screen_mid.values; ef = df.ssce.values
r_se, p_se = stats.pearsonr(sc, ef)
bl = np.polyfit(sc, ef, 1); r2_lin = 1 - ((ef - np.polyval(bl, sc))**2).sum() / ((ef-ef.mean())**2).sum()
bq = np.polyfit(sc, ef, 2); r2_quad = 1 - ((ef - np.polyval(bq, sc))**2).sum() / ((ef-ef.mean())**2).sum()
_bs = np.array([np.polyfit(sc[ix], ef[ix], 1)[0] for ix in (RNG.integers(0, N, N) for _ in range(N_BOOT))])
slope_ci = np.percentile(_bs, [2.5, 97.5])   # paired bootstrap, as 01_main_analysis.py
_q = smf.ols("ssce ~ screen_mid + I(screen_mid**2)", data=df).fit()
p_quad = _q.pvalues["I(screen_mid ** 2)"]
rec("exp_r", r_se); rec("exp_p", p_se); rec("exp_r_ci", list(r_ci(r_se, N)))
rec("exp_slope", bl[0]); rec("exp_slope_ci", list(slope_ci))
rec("exp_r2_lin", r2_lin); rec("exp_r2_quad", r2_quad); rec("exp_r2_gain", r2_quad - r2_lin); rec("exp_p_quad", p_quad)
say(f"r={r_se:.4f}, p={p_se:.4f}, Fisher-z 95% CI [{r_ci(r_se,N)[0]:.3f}, {r_ci(r_se,N)[1]:.3f}]  (n={N})")
say(f"slope={bl[0]:+.4f} per h, paired-bootstrap 95% CI [{slope_ci[0]:+.4f}, {slope_ci[1]:+.4f}]")
say(f"linear R^2={r2_lin:.4f}, quadratic R^2={r2_quad:.4f}, gain={r2_quad-r2_lin:.4f}, "
    f"quadratic-term p={p_quad:.4f}")
BAND = df.groupby("screen_mid")["ssce"].agg(["count", "mean", "std"]).reset_index()
BAND["se"] = BAND["std"] / np.sqrt(BAND["count"])
say("per-band SSCE:"); say(BAND.round(3).to_string(index=False))
# what the share is made of: purposes selected, by kind, against screen time
_parts = raw_items.loc[df.index, resolve(raw_items, "screen time mainly for")].apply(split_multi)
df["n_purposes"] = _parts.apply(len)
df["n_academic"] = _parts.apply(lambda ps: sum(any(k in p.lower() for k in STUDY_KEYS) for p in ps))
df["n_nonacademic"] = df.n_purposes - df.n_academic
for v in ["n_purposes", "n_academic", "n_nonacademic"]:
    rr, pp = stats.pearsonr(df.screen_mid, df[v]); rec(f"exp_r_{v}", rr); rec(f"exp_p_{v}", pp)
    rec(f"mean_{v}", df[v].mean())
    say(f"screen band ~ {v:13s}: r={rr:+.4f}, p={pp:.4f}  (mean {df[v].mean():.3f})")
_no_low = df[df.screen_mid > 1.0]
rr, pp = stats.pearsonr(_no_low.screen_mid, _no_low.ssce)
rec("exp_r_without_lowest_band", rr); rec("exp_p_without_lowest_band", pp); rec("exp_n_without_lowest_band", len(_no_low))
say(f"SSCE ~ screen band without the '<2 h' band: r={rr:+.4f}, p={pp:.4f} (n={len(_no_low)})")
rr, pp = stats.pearsonr(df.workload, df.n_academic); rec("r_workload_n_academic", rr); rec("p_workload_n_academic", pp)
rr2, pp2 = stats.pearsonr(df.workload, df.n_nonacademic); rec("r_workload_n_nonacademic", rr2); rec("p_workload_n_nonacademic", pp2)
say(f"workload ~ n_academic: r={rr:+.4f}, p={pp:.4f}; workload ~ n_nonacademic: r={rr2:+.4f}, p={pp2:.4f}")
say("")

# ============================================================ 4. CONVERGENT ===
say("="*80); say("4. CONVERGENT CORRELATIONS WITH SSCE"); say("="*80)
val = []
for v, lab in [("switch", "task-switching"), ("workload", "workload"), ("focus", "focus ease"),
               ("control", "perceived control"), ("tech_helps", "tech helpfulness")]:
    d = df.dropna(subset=[v]); rr, pp = stats.pearsonr(d[v], d.ssce)
    lo, hi = r_ci(rr, len(d))
    val.append(dict(item=lab, r=rr, ci_lo=lo, ci_hi=hi, p=pp, n=len(d)))
    rec(f"r_{v}", rr); rec(f"p_{v}", pp); rec(f"n_{v}", len(d)); rec(f"r_ci_{v}", [lo, hi])
    say(f"  SSCE ~ {lab:18s}: r={rr:+.4f} [{lo:+.3f}, {hi:+.3f}], p={pp:.4f}  (n={len(d)})")
VAL = pd.DataFrame(val)
VAL["p_holm"] = holm(VAL.p.values); VAL["p_bh"] = benjamini_hochberg(VAL.p.values)
for r in VAL.itertuples():
    rec(f"p_holm_{r.item}", r.p_holm); rec(f"p_bh_{r.item}", r.p_bh)
say("adjusted across the five correlations:")
say(VAL[["item", "r", "p", "p_holm", "p_bh"]].round(4).to_string(index=False)); say("")

# ============================================================ 5. MODEL ========
say("="*80); say("5. STANDARDISED REGRESSION: SSCE ~ focus + control + task-switching + workload"); say("="*80)
preds = ["focus", "control", "switch", "workload"]
mreg = df.dropna(subset=preds + ["ssce"]).copy()
REG = ols_standardized(mreg[preds].values, mreg["ssce"].values, preds)
for key in ["n", "r2", "adj", "F", "pF", "dof"]:
    rec(f"reg_{key}", REG[key])
say(f"n={REG['n']}: R^2={REG['r2']:.4f}, adj R^2={REG['adj']:.4f}, "
    f"F(4,{REG['dof']})={REG['F']:.3f}, p={REG['pF']:.4g}")
REGT = pd.DataFrame(dict(predictor=preds, std_beta=REG["beta"], se=REG["se"], p=REG["p"]))
for v, b, s, p in zip(preds, REG["beta"], REG["se"], REG["p"]):
    rec(f"beta_{v}", b); rec(f"se_{v}", s); rec(f"pbeta_{v}", p)
# relative importance (unique R^2), as verify_section411.py
z = mreg.copy()
for v in preds + ["ssce"]:
    z[f"z{v}"] = (z[v] - z[v].mean()) / z[v].std(ddof=1)
full = smf.ols("zssce ~ zfocus + zcontrol + zswitch + zworkload", data=z).fit()
uniq = []
for v in preds:
    red = smf.ols("zssce ~ " + " + ".join(f"z{o}" for o in preds if o != v), data=z).fit()
    uniq.append(full.rsquared - red.rsquared); rec(f"uniqueR2_{v}", full.rsquared - red.rsquared)
REGT["unique_r2"] = uniq
say(REGT.round(4).to_string(index=False)); say("")

# ============================================================ 6. HIERARCHICAL =
say("="*80); say("6. HIERARCHICAL REGRESSION: demographics -> + self-regulation"); say("="*80)
# Block 1 = gender, subject and university year (dummies, drop_first). The
# full-sample model's school/university dummy is constant here and is replaced
# by university-year dummies.
m49 = df.dropna(subset=["focus", "control", "switch", "workload", "ssce", "gender", "subject"]).copy()
for v in ["focus", "control", "switch", "workload", "ssce", "screen_mid"]:
    m49[f"z_{v}"] = (m49[v] - m49[v].mean()) / m49[v].std(ddof=1)
m49["yr"] = m49["year"].str.replace("Uni ", "").str.replace("+", "plus")
m49d = pd.get_dummies(m49, columns=["gender", "subject", "yr"], drop_first=True)
m49d.columns = [c.replace(" ", "_") for c in m49d.columns]   # "Prefer not to say" -> formula-safe
demo = [c for c in m49d.columns if c.startswith(("gender_", "subject_", "yr_"))]
for c in demo: m49d[c] = m49d[c].astype(float)
b1 = smf.ols("z_ssce ~ " + " + ".join(demo), data=m49d).fit()
b2 = smf.ols("z_ssce ~ " + " + ".join(demo) + " + z_focus + z_control + z_switch + z_workload", data=m49d).fit()
dR2 = b2.rsquared - b1.rsquared; df1 = b2.df_model - b1.df_model; df2 = b2.df_resid
Fch = (dR2 / df1) / ((1 - b2.rsquared) / df2); pFch = stats.f.sf(Fch, df1, df2)
for key, v in [("n", len(m49d)), ("b1_R2", b1.rsquared), ("b1_F", b1.fvalue), ("b1_p", b1.f_pvalue),
               ("b1_df", [int(b1.df_model), int(b1.df_resid)]), ("b2_R2", b2.rsquared), ("dR2", dR2), ("df1", df1), ("df2", df2), ("Fch", Fch), ("pFch", pFch)]:
    rec(f"hier_{key}", v)
say(f"n={len(m49d)}; Block 1 terms: {demo}")
say(f"  Block 1 demographics       R^2={b1.rsquared:.4f} (F({int(b1.df_model)},{int(b1.df_resid)})={b1.fvalue:.3f}, p={b1.f_pvalue:.4f})")
say(f"  Block 2 + self-regulation  R^2={b2.rsquared:.4f}")
say(f"  Delta R^2={dR2:.4f}, F-change({int(df1)},{int(df2)})={Fch:.3f}, p={pFch:.4g}\n")

# ============================================================ 7. MEDIATION ====
say("="*80); say("7. MEDIATION: screen exposure -> task-switching -> SSCE (10,000 bootstrap)"); say("="*80)
_rng = np.random.default_rng(SEED)          # separate generator, as 01_main_analysis.py
# focus is not in this model, so it uses every respondent (z-scores over all N)
dz = df.copy()
for v in ["screen_mid", "switch", "ssce"]:
    dz[f"z_{v}"] = (dz[v] - dz[v].mean()) / dz[v].std(ddof=1)
med = dz.dropna(subset=["z_screen_mid", "z_switch", "z_ssce"]).copy()
a_r = smf.ols("z_switch ~ z_screen_mid", data=med).fit()
b_r = smf.ols("z_ssce ~ z_switch + z_screen_mid", data=med).fit()
c_r = smf.ols("z_ssce ~ z_screen_mid", data=med).fit()
a_c, b_c = a_r.params["z_screen_mid"], b_r.params["z_switch"]
ind = a_c * b_c
X = med[["z_screen_mid", "z_switch", "z_ssce"]].values
boot = []
for _ in range(10000):
    s = X[_rng.integers(0, len(X), len(X))]
    aa = np.polyfit(s[:, 0], s[:, 1], 1)[0]
    A = np.column_stack([np.ones(len(s)), s[:, 1], s[:, 0]])
    boot.append(aa * np.linalg.lstsq(A, s[:, 2], rcond=None)[0][1])
m_lo, m_hi = np.percentile(boot, [2.5, 97.5])
for key, v in [("n", len(med)), ("a", a_c), ("a_p", a_r.pvalues["z_screen_mid"]),
               ("b", b_c), ("b_p", b_r.pvalues["z_switch"]),
               ("c_total", c_r.params["z_screen_mid"]), ("c_total_p", c_r.pvalues["z_screen_mid"]),
               ("c_direct", b_r.params["z_screen_mid"]), ("c_direct_p", b_r.pvalues["z_screen_mid"]),
               ("indirect", ind), ("ci_lo", m_lo), ("ci_hi", m_hi)]:
    rec(f"med_{key}", v)
med_sig = m_lo * m_hi > 0; rec("med_significant", bool(med_sig))
say(f"n={len(med)}")
say(f"  a  (exposure -> switch)          = {a_c:.4f}, p={a_r.pvalues['z_screen_mid']:.4f}")
say(f"  b  (switch -> SSCE | exposure)   = {b_c:.4f}, p={b_r.pvalues['z_switch']:.4f}")
say(f"  c  (total, exposure -> SSCE)     = {c_r.params['z_screen_mid']:.4f}, p={c_r.pvalues['z_screen_mid']:.4f}")
say(f"  c' (direct, exposure | switch)   = {b_r.params['z_screen_mid']:.4f}, p={b_r.pvalues['z_screen_mid']:.4f}")
say(f"  indirect a*b = {ind:.4f}, 95% bootstrap CI [{m_lo:.4f}, {m_hi:.4f}] -> "
    f"{'SIGNIFICANT' if med_sig else 'NOT significant (CI includes zero)'}\n")

# ============================================================ 8. HARMAN =======
say("="*80); say("8. HARMAN'S SINGLE-FACTOR TEST"); say("="*80)
items = m49[["z_focus", "z_control", "z_switch", "z_workload", "z_ssce"]].dropna()
ev = PCA().fit(items).explained_variance_ratio_
rec("harman_first_pct", ev[0] * 100); rec("harman_n", len(items))
say(f"{len(items)} obs, 5 items: " + ", ".join(f"F{i+1}={e*100:.1f}%" for i, e in enumerate(ev)))
say(f"first factor = {ev[0]*100:.1f}% ({'< 50%' if ev[0] < .5 else '>= 50%'})\n")

# ============================================================ 9. ROBUSTNESS ===
say("="*80); say("9a. ROBUSTNESS: exposure-efficiency r across the eight builds"); say("="*80)
grid = []
for mh in [8.5, 9.0, 10.0, 11.0]:
    for pm in ["selected", "all"]:
        d2 = build(raw_items, mid_high=mh, prop_mode=pm)
        rr, pp = stats.pearsonr(d2.screen_mid, d2.ssce); lo, hi = r_ci(rr, len(d2))
        grid.append(dict(mid_high=mh, prop_mode=pm, n=len(d2), mean_study_h=d2.study_hours.mean(),
                         r=rr, r_ci_lo=lo, r_ci_hi=hi, p=pp))
GRID = pd.DataFrame(grid)
say(GRID.round(4).to_string(index=False))
rec("grid_r_min", GRID.r.min()); rec("grid_r_max", GRID.r.max())
rec("grid_p_max", GRID.p.max()); rec("grid_n_sig", int((GRID.p < .05).sum()))
rec("grid_mean_min", GRID.mean_study_h.min()); rec("grid_mean_max", GRID.mean_study_h.max())
for g in GRID.itertuples():
    rec(f"grid_{g.mid_high}_{g.prop_mode}_r", g.r); rec(f"grid_{g.mid_high}_{g.prop_mode}_p", g.p)
say(f">> r ranges {GRID.r.min():.3f} to {GRID.r.max():.3f}; p < .05 in {int((GRID.p<.05).sum())}/8 builds\n")

say("="*80); say("9b. SPLIT-HALF REPLICATION (1,000 random splits)"); say("="*80)
np.random.seed(SEED)                        # legacy generator, as verify_section411.py
def corr(d, a, b):
    s = d.dropna(subset=[a, b]); return stats.pearsonr(s[a], s[b])[0]
split = []
for v in ["screen_mid", "switch", "workload", "control"]:
    out = []
    for _ in range(1000):
        idx = np.random.permutation(N)
        out.append((corr(df.iloc[idx[:N//2]], v, "ssce"), corr(df.iloc[idx[N//2:]], v, "ssce")))
    a = np.array(out); ss = np.mean(np.sign(a[:, 0]) == np.sign(a[:, 1]))
    split.append(dict(item=v, median_r_half1=np.median(a[:, 0]), median_r_half2=np.median(a[:, 1]),
                      same_sign_pct=ss * 100))
    rec(f"split_{v}_same_sign_pct", ss * 100)
    rec(f"split_{v}_median_r", [float(np.median(a[:, 0])), float(np.median(a[:, 1]))])
    say(f"  {v}-SSCE: median r={np.median(a[:,0]):.3f}/{np.median(a[:,1]):.3f}, same sign in {ss*100:.1f}% of splits")
SPLIT = pd.DataFrame(split); say("")

say("="*80); say(f"9c. CLUSTER SENSITIVITY (exclude {FLAG} == 1)"); say("="*80)
cl = df[df[FLAG] != 1].copy()
rec("cluster_n_excluded", int((df[FLAG] == 1).sum())); rec("cluster_n", len(cl))
say(f"excluded {int((df[FLAG]==1).sum())} flagged responses -> n={len(cl)}")
for k, lab in zip(YEARS, YEAR_LABELS):
    rec(f"cluster_n_{lab}", int((cl.stage == k).sum())); say(f"  {lab:8s} n={int((cl.stage==k).sum())}")
clu = []
for v in ["screen_mid", "switch", "workload", "control", "focus", "tech_helps"]:
    s = cl.dropna(subset=[v]); rr, pp = stats.pearsonr(s[v], s.ssce)
    clu.append(dict(item=v, r=rr, p=pp, n=len(s))); rec(f"cluster_r_{v}", rr); rec(f"cluster_p_{v}", pp)
    say(f"  SSCE ~ {v:10s}: r={rr:+.4f}, p={pp:.4f} (n={len(s)})")
creg_d = cl.dropna(subset=preds + ["ssce"])
CREG = ols_standardized(creg_d[preds].values, creg_d["ssce"].values, preds)
rec("cluster_reg_r2", CREG["r2"]); rec("cluster_reg_dof", CREG["dof"]); rec("cluster_reg_F", CREG["F"]); rec("cluster_reg_p", CREG["pF"]); rec("cluster_reg_n", CREG["n"])
say(f"  regression: n={CREG['n']}, R^2={CREG['r2']:.4f}, F(4,{CREG['dof']})={CREG['F']:.3f}, p={CREG['pF']:.4g}")
for v, b, p in zip(preds, CREG["beta"], CREG["p"]):
    rec(f"cluster_beta_{v}", b); rec(f"cluster_pbeta_{v}", p)
    say(f"     beta {v:9s} = {b:+.4f}, p={p:.4f}")
CLU = pd.DataFrame(clu); say("")

say("="*80); say("9d. COMPARISON WITH FIRST-YEAR STUDENTS INCLUDED (n = 211)"); say("="*80)
# First-year responses are not shared, so this comparison runs only where the
# original survey file is available locally. It is reported so that readers can
# see how the restriction to Years 2-4+ changes the results.
Y1 = None
if os.path.isfile(FULL):
    _f = pd.read_csv(FULL)
    _keep = (_f[GRADE].astype(str).str.strip().map(STAGE_MAP).between(8, 11)
             & _f[INST].astype(str).str.strip().str.startswith("College/University"))
    _f = _f[_keep]
    y1 = build(_f.drop(columns=[FLAG]))
    rec("y1in_n", len(y1)); say(f"n = {len(y1)} (Years 1-4+, university institution)")
    rr, pp = stats.pearsonr(y1.screen_mid, y1.ssce); lo, hi = r_ci(rr, len(y1))
    rec("y1in_exp_r", rr); rec("y1in_exp_p", pp); rec("y1in_exp_ci", [lo, hi])
    say(f"  SSCE ~ screen band: r={rr:+.4f} [{lo:+.3f}, {hi:+.3f}], p={pp:.4f}")
    _yv = []
    for v in ["switch", "workload", "focus", "control", "tech_helps"]:
        d_ = y1.dropna(subset=[v]); rr, pp = stats.pearsonr(d_[v], d_.ssce)
        _yv.append((v, rr, pp, len(d_)))
    _hp = holm([x[2] for x in _yv])
    for (v, rr, pp, n_), ph in zip(_yv, _hp):
        rec(f"y1in_r_{v}", rr); rec(f"y1in_p_{v}", pp); rec(f"y1in_p_holm_{v}", ph); rec(f"y1in_n_{v}", n_)
        say(f"  SSCE ~ {v:10s}: r={rr:+.4f}, p={pp:.4f}, Holm (5 tests) p={ph:.4f} (n={n_})")
    _yr = y1.dropna(subset=preds + ["ssce"])
    Y1 = ols_standardized(_yr[preds].values, _yr["ssce"].values, preds)
    for key in ["n", "r2", "F", "pF", "dof"]:
        rec(f"y1in_reg_{key}", Y1[key])
    say(f"  regression: n={Y1['n']}, R^2={Y1['r2']:.4f}, F(4,{Y1['dof']})={Y1['F']:.3f}, p={Y1['pF']:.4g}")
    for v, b_, p_ in zip(preds, Y1["beta"], Y1["p"]):
        rec(f"y1in_beta_{v}", b_); rec(f"y1in_pbeta_{v}", p_)
        say(f"     beta {v:9s} = {b_:+.4f}, p={p_:.4f}")
else:
    say("original survey file not present; comparison not run")
say("")

# ============================================================ 10. GROUPS ======
say("="*80); say("10. GROUP CHECKS (gender, subject, device) AND DISCRIMINANT CORRELATIONS"); say("="*80)
grp = []
for v, lab in [("study_hours", "study time"), ("ssce", "SSCE")]:
    m = df.loc[df.gender == "Male", v]; f = df.loc[df.gender == "Female", v]
    tg, pg = stats.ttest_ind(m, f, equal_var=False)
    dg = cohens_d(f.values, m.values)                         # male minus female
    diff = m.mean() - f.mean(); se = math.sqrt(m.var(ddof=1)/len(m) + f.var(ddof=1)/len(f))
    bound = 0.3 * df[v].std(ddof=1); dft = len(m) + len(f) - 2
    p_tost = max(1 - stats.t.cdf((diff + bound) / se, dft), stats.t.cdf((diff - bound) / se, dft))
    for key, val_ in [("t", tg), ("p", pg), ("d", dg), ("diff", diff), ("bound", bound), ("tost_p", p_tost)]:
        rec(f"gender_{v}_{key}", val_)
    say(f"{lab:10s} male (n={len(m)}) vs female (n={len(f)}): diff={diff:+.4f}, Welch t={tg:.3f}, p={pg:.4f}, "
        f"d={dg:.3f}; TOST +-{bound:.4f} (0.3 SD): p={p_tost:.4f} -> "
        f"{'EQUIVALENT' if p_tost < .05 else 'equivalence NOT shown'}")
    for gv in ["subject", "device"]:
        gs = [g[v].values for _, g in df.groupby(gv)]
        Fs, ps = stats.f_oneway(*gs); Hs, pks = stats.kruskal(*gs)
        rec(f"{gv}_{v}_F", Fs); rec(f"{gv}_{v}_p", ps); rec(f"{gv}_{v}_kw_p", pks)
        rec(f"{gv}_{v}_df", [len(gs) - 1, N - len(gs)])
        say(f"{lab:10s} by {gv:7s}: ANOVA F({len(gs)-1},{N-len(gs)})={Fs:.3f}, p={ps:.4f}; KW p={pks:.4f}")
        gm = df.groupby(gv)[v].agg(["count", "mean", "std"])
        for cat, row in gm.iterrows():
            rec(f"{gv}_{v}_mean_{cat}", row["mean"]); rec(f"{gv}_{v}_sd_{cat}", row["std"])
        say("      " + "; ".join(f"{cat} n={int(r_['count'])} M={r_['mean']:.3f} (SD {r_['std']:.3f})"
                                for cat, r_ in gm.iterrows()))
    grp.append(dict(outcome=v, male_minus_female=diff, welch_t=tg, p=pg, d=dg, tost_bound=bound, tost_p=p_tost))
chi2, pdev, dofd, expct = stats.chi2_contingency(DEVYR)
rec("device_year_chi2", chi2); rec("device_year_df", dofd); rec("device_year_p", pdev)
rec("device_year_min_expected", expct.min()); rec("device_year_pct_cells_lt5", 100 * (expct < 5).mean())
say(f"device x year: chi2({dofd})={chi2:.3f}, p={pdev:.4f}; min expected count={expct.min():.2f}, "
    f"{100*(expct<5).mean():.0f}% of cells expected < 5 (chi-square approximation unreliable)")
df["gender_bin"] = (df.gender == "Male").astype(int)
for v, lab in [("gender_bin", "gender (male vs not male)"), ("stem", "STEM vs non-STEM")]:
    rr, pp = stats.pointbiserialr(df[v], df.ssce)
    rec(f"discr_r_{v}", rr); rec(f"discr_p_{v}", pp)
    say(f"discriminant SSCE x {lab}: r={rr:+.4f}, p={pp:.4f}")
# invariance of the exposure-efficiency association (moderation, as 4.9d method)
# focus is not in these models, so they use every respondent (dz, n = N)
dz["yr"] = dz["year"].str.replace("Uni ", "").str.replace("+", "plus")
mm = dz[dz.gender.isin(["Male", "Female"])].copy(); mm["male"] = (mm.gender == "Male").astype(float)
p_int_g = smf.ols("z_ssce ~ z_screen_mid * male", data=mm).fit().pvalues["z_screen_mid:male"]
p_int_s = smf.ols("z_ssce ~ z_screen_mid * stem", data=dz).fit().pvalues["z_screen_mid:stem"]
_r0 = smf.ols("z_ssce ~ z_screen_mid + C(yr)", data=dz).fit()
_r1 = smf.ols("z_ssce ~ z_screen_mid * C(yr)", data=dz).fit()
_av = anova_lm(_r0, _r1); p_int_y = _av["Pr(>F)"].iloc[1]
rec("mod_gender_p", p_int_g); rec("mod_gender_n", len(mm)); rec("mod_stem_p", p_int_s)
rec("mod_year_F", _av["F"].iloc[1]); rec("mod_year_p", p_int_y); rec("mod_n", len(dz))
rec("mod_year_df", [int(_av["df_diff"].iloc[1]), int(_r1.df_resid)])
say(f"moderation of exposure-efficiency: x gender (M/F, n={len(mm)}) p={p_int_g:.4f}; "
    f"x STEM (n={len(dz)}) p={p_int_s:.4f}; x year (n={len(dz)}, joint F({int(_av['df_diff'].iloc[1])},{int(_r1.df_resid)})="
    f"{_av['F'].iloc[1]:.3f}) p={p_int_y:.4f}")
GRP = pd.DataFrame(grp); say("")

# ============================================================ 11. OPEN TEXT ===
say("="*80); say("11. OPEN-TEXT CODING (Section 4.10 method, 02_opentext_coding.py)"); say("="*80)
# dictionaries and filler rule copied unchanged from 02_opentext_coding.py
FILLER = {"nan","","na","n/a","none","no","nothing","-",".","none.","no.","nil",
          "nope","i have no idea","idk","no idea","not really","n.a"}
def usable(s):
    s = str(s).strip().lower(); return (s not in FILLER) and (len(s) >= 4)
THEMES_CHALLENGE = {
 "Distraction / task-switching": r"distract|social ?media|instagram|facebook|whats ?app|tiktok|scroll|switch|procrastinat|off.?task|lose (?:focus|track|time)|attention|tempt|addict|notif|reels|short video|sidetrack|wast(?:e|ing) time",
 "Notifications (sub-set)":       r"notif|ping|message pop|alert|pop.?up",
 "Entertainment pull":            r"\bgame|gaming|youtube|netflix|video.?game|entertainment|movie",
 "Connectivity / technical":      r"internet|wi.?fi|\bdata\b|connection|slow|network|load.?shed|electricity|buffer|server|power cut",
 "Eye strain / health / fatigue": r"eye|headache|tired|fatigue|strain|sleep|health|pain|exhaust",
 "Access / cost":                 r"expensive|cost|afford|price|money|data pack|subscription",
 "Info overload / reliability":   r"too much|overwhelm|reliab|fake|accura|misinform|find (?:the )?right|overload|confus",
}
THEMES_POSITIVE = {
 "Access to resources/materials": r"resource|youtube|tutorial|video|pdf|material|website|find|google|article|lecture",
 "Concept understanding/clarity": r"understand|concept|clear|explain|learn|visuali|grasp|easier to|comprehen|deep",
 "Convenience/flexibility":       r"anytime|anywhere|fast|quick|easy|convenien|flexib|instant|accessib|time.?sav",
 "Collaboration/communication":   r"group|friend|discuss|share|whats ?app|collaborat|peer|note",
 "Practice/exam prep":            r"quiz|practice|test|exam|mock|revis|prepar",
}
THEMES_SUGGESTIONS = {
 "Focus/distraction controls":    r"block|focus|limit|control|distract|mute|notif|discipline|self.?control",
 "Infrastructure/connectivity":   r"internet|wi.?fi|infrastructur|device|access|\bdata\b|network|electricity",
 "Institutional tools/platform":  r"institution|\bapp\b|platform|lms|portal|system|software|tool",
 "Content quality/curation":      r"reliab|curat|verif|quality|accura|trust|official|credible",
 "Training/guidance":             r"train|teach|guid|literac|aware|workshop|how to",
}
otext = raw_items.loc[df.index]     # the analysed university respondents only
coded_all = []
for colkey, themes, label in [("challenge", THEMES_CHALLENGE, "CHALLENGE"),
                              ("positive experience", THEMES_POSITIVE, "POSITIVE"),
                              ("suggestions", THEMES_SUGGESTIONS, "SUGGESTIONS")]:
    col = resolve(otext, colkey)
    s = otext[col][otext[col].apply(usable)].astype(str)
    rows = []
    for rid, txt in s.items():
        low = txt.lower(); assigned = [t for t, pat in themes.items() if re.search(pat, low)]
        rows.append({"column": label, "source_row": rid + 2, "text": txt,
                     **{t: int(t in assigned) for t in themes}, "n_themes": len(assigned)})
    coded = pd.DataFrame(rows); n_use = len(coded)
    rec(f"text_{label}_n", n_use)
    say(f"{label}: {n_use} usable responses")
    for t in themes:
        n = int(coded[t].sum()); rec(f"text_{label}_{t}_n", n); rec(f"text_{label}_{t}_pct", 100 * n / n_use)
        say(f"   {t:32s} {n:3d}  ({n/n_use*100:4.1f}%)")
    unc = int((coded.n_themes == 0).sum()); rec(f"text_{label}_uncoded_n", unc)
    say(f"   {'(uncoded)':32s} {unc:3d}  ({unc/n_use*100:4.1f}%)")
    coded_all.append(coded)
# responses that repeat the questionnaire's own example text (case/space-insensitive)
EXAMPLES = {"CHALLENGE": "social notifications constantly interrupt my focus",
            "POSITIVE": "youtube tutorials helped me understand difficult math concepts"}
for c in coded_all:
    label = c.column.iloc[0]
    if label in EXAMPLES:
        norm = c.text.str.lower().str.replace(r"[^a-z ]", "", regex=True).str.split().str.join(" ")
        n_ex = int((norm == EXAMPLES[label]).sum()); rec(f"text_{label}_example_copies", n_ex)
        say(f"{label}: {n_ex} response(s) repeat the questionnaire's example wording verbatim")
OT = pd.concat(coded_all, ignore_index=True)
OT.insert(0, "response_id", range(1, len(OT) + 1)); OT["second_coder_distraction"] = ""
OT.to_csv(os.path.join(OUTDIR, "opentext_coded_university.csv"), index=False)
say(f"(source_row = record number of the respondent in {os.path.basename(DATA)}, counting the header as 1; "
    f"coded responses in opentext_coded_university.csv)\n")

# ============================================================ 12. DISCLOSURE ==
say("="*80); say("12. DISCLOSURE CHECK: respondents unique on year x gender x subject"); say("="*80)
cells = df.groupby(["year", "gender", "subject"]).size()
n_unique = int((cells == 1).sum()); rec("disclosure_unique_rows", n_unique)
rec("disclosure_cells_lt3", int((cells < 3).sum()))
say(f"{n_unique} respondents are unique on year x gender x subject (coded categories); "
    f"{int((cells < 3).sum())} cells have fewer than 3 respondents\n")

# ============================================================ FIGURES =========
def save(name):
    plt.savefig(os.path.join(FIGDIR, name), bbox_inches="tight"); plt.close()
xs = np.arange(len(YEARS))

# U1 sample by year
plt.figure(figsize=(6, 4))
plt.bar(xs, YR.n, color=C1, width=0.6)
for i, v in enumerate(YR.n): plt.text(i, v + 1.5, str(int(v)), ha="center")
plt.xticks(xs, YEAR_LABELS); plt.ylabel("Respondents"); save("figU1_sample_year.png")

# U2 study time by year (95% t-intervals); points not joined: different students per year
plt.figure(figsize=(6, 4.2))
plt.errorbar(xs, YR.study_hours_mean, yerr=[YR.study_hours_mean - YR.study_hours_ci_lo,
             YR.study_hours_ci_hi - YR.study_hours_mean], fmt="o", ms=8, color=C1, capsize=4, lw=2)
plt.axhline(df.study_hours.mean(), ls="--", color=C3, lw=1, label=f"overall mean = {df.study_hours.mean():.2f} h")
plt.xticks(xs, YEAR_LABELS); plt.ylabel("Study time proxy (h/day)"); plt.xlim(-0.5, len(YEARS) - 0.5)
plt.legend(frameon=False); save("figU2_studytime_year.png")

# U3 SSCE vs screen-time band (per-band means +- SE, linear fit)
plt.figure(figsize=(6.5, 4.2))
plt.errorbar(BAND.screen_mid, BAND["mean"], yerr=BAND.se, fmt="o", ms=8, color=C1, capsize=4)
for r in BAND.itertuples():
    plt.text(r.screen_mid, r.mean + r.se + 0.02, f"n={int(r.count)}", ha="center", fontsize=8, color="#52514e")
xx = np.linspace(BAND.screen_mid.min(), BAND.screen_mid.max(), 50)
plt.plot(xx, np.polyval(bl, xx), color=C2, lw=2, label=f"linear fit: slope {bl[0]:+.3f}/h, r = {r_se:.2f}")
plt.xticks(BAND.screen_mid, ["<2", "2-4", "4-6", "6-8", ">8"][:len(BAND)])
plt.xlabel("Total screen time yesterday (h, band)"); plt.ylabel("SSCE (study share of screen time)")
plt.legend(frameon=False); save("figU3_ssce_exposure.png")

# U4 SSCE by year (95% t-intervals)
plt.figure(figsize=(6, 4.2))
plt.errorbar(xs, YR.ssce_mean, yerr=[YR.ssce_mean - YR.ssce_ci_lo, YR.ssce_ci_hi - YR.ssce_mean],
             fmt="o", ms=8, color=C1, capsize=4, lw=2)
plt.axhline(df.ssce.mean(), ls="--", color=C3, lw=1, label=f"overall mean = {df.ssce.mean():.2f}")
plt.xticks(xs, YEAR_LABELS); plt.ylabel("SSCE (study share of screen time)"); plt.xlim(-0.5, len(YEARS) - 0.5)
plt.legend(frameon=False); save("figU4_ssce_year.png")

# U5 standardised coefficients (95% CI)
plt.figure(figsize=(6.5, 4))
ypos = np.arange(len(preds)); ci95 = 1.96 * REG["se"]
plt.errorbar(REG["beta"], ypos, xerr=ci95, fmt="o", color="k", capsize=3, zorder=3)
for yp, b, pv in zip(ypos, REG["beta"], REG["p"]):
    plt.plot([0, b], [yp, yp], color=C2 if pv < .05 else C3, lw=4, alpha=.5, zorder=2)
plt.axvline(0, color="k", lw=.8)
plt.yticks(ypos, ["focus ease", "perceived control", "task-switching", "workload"])
plt.xlabel("Standardised coefficient (outcome: SSCE)"); save("figU5_selfreg_coef.png")

# U6 device by year (shares; 2px white gaps between segments)
dev_order = ["Laptop/Desktop", "Smartphone", "Mixed", "Tablet", "Other"]
prop = DEVYR.reindex(columns=dev_order).fillna(0); prop = prop.div(prop.sum(axis=1), axis=0)
plt.figure(figsize=(7, 4.6)); bottom = np.zeros(len(YEARS))
for c, col in zip(dev_order, DEV_COLS):
    plt.bar(xs, prop[c].values, bottom=bottom, color=col, width=0.6, label=c, edgecolor="white", linewidth=2)
    bottom += prop[c].values
plt.xticks(xs, [f"{l}\n(n={int(n)})" for l, n in zip(YEAR_LABELS, YR.n)]); plt.ylabel("Share of respondents")
plt.grid(axis="x", visible=False)
plt.legend(fontsize=8, ncol=5, loc="lower center", bbox_to_anchor=(0.5, 1.01), frameon=False)
save("figU6_device_year.png")

# U7 robustness: exposure-efficiency r (Fisher-z 95% CI) across the eight builds
plt.figure(figsize=(7, 4.2))
mh_vals = sorted(GRID.mid_high.unique())
for j, (pm, col, mk, name) in enumerate([("selected", C1, "o", "denominator = purposes selected (used)"),
                                         ("all", C2, "s", "denominator = all 7 purposes")]):
    g = GRID[GRID.prop_mode == pm]; xpos = np.arange(len(g)) + (j - 0.5) * 0.18
    plt.errorbar(xpos, g.r, yerr=[g.r - g.r_ci_lo, g.r_ci_hi - g.r], fmt=mk, ms=8,
                 color=col, capsize=4, label=name)
plt.axhline(0, color="k", lw=.8)
plt.xticks(np.arange(len(mh_vals)), [f"{v:g}" for v in mh_vals])
plt.xlabel("Value assigned to the '>8 h' band (h)"); plt.ylabel("r (SSCE, screen time), 95% CI")
plt.legend(frameon=False, fontsize=9, ncol=2, loc="lower center", bbox_to_anchor=(0.5, 1.0))
save("figU7_robustness.png")

# ============================================================ SAVE ============
SAMP.to_csv(os.path.join(OUTDIR, "table_sample.csv"), index=False)
DEVYR.to_csv(os.path.join(OUTDIR, "table_device_by_year.csv"))
YR.to_csv(os.path.join(OUTDIR, "table_by_year.csv"), index=False)
ETG.to_csv(os.path.join(OUTDIR, "table_etg_years.csv"), index=False)
BAND.to_csv(os.path.join(OUTDIR, "table_ssce_by_band.csv"), index=False)
VAL.to_csv(os.path.join(OUTDIR, "table_convergent.csv"), index=False)
REGT.to_csv(os.path.join(OUTDIR, "table_selfreg_model.csv"), index=False)
GRID.to_csv(os.path.join(OUTDIR, "table_builds.csv"), index=False)
SPLIT.to_csv(os.path.join(OUTDIR, "table_splithalf.csv"), index=False)
CLU.to_csv(os.path.join(OUTDIR, "table_cluster_sensitivity.csv"), index=False)
PREC.to_csv(os.path.join(OUTDIR, "table_precision.csv"), index=False)
GRP.to_csv(os.path.join(OUTDIR, "table_gender.csv"), index=False)
with open(os.path.join(OUTDIR, "summary.json"), "w") as f:
    json.dump(dict(seed=SEED, data=os.path.basename(DATA), results=RES), f, indent=1, default=float)
with open(os.path.join(OUTDIR, "sessioninfo.txt"), "w") as f:
    f.write(f"python {platform.python_version()}\nnumpy {np.__version__}\npandas {pd.__version__}\n"
            f"statsmodels {statsmodels.__version__}\nseed {SEED}\n")

# ============================================================ SUMMARY =========
say("="*80); say("SUMMARY (n per model in brackets)"); say("="*80)
summary = [
    ("n", f"{N}"),
    ("SSCE vs screen band", f"r = {r_se:+.3f}, {fmt_p(p_se)} [n = {N}]"),
    ("SSCE vs task-switching", f"r = {RES['r_switch']:+.3f}, {fmt_p(RES['p_switch'])}, Holm {fmt_p(RES['p_holm_task-switching'])} [n = {RES['n_switch']}]"),
    ("SSCE vs workload", f"r = {RES['r_workload']:+.3f}, {fmt_p(RES['p_workload'])} [n = {RES['n_workload']}]"),
    ("SSCE vs control", f"r = {RES['r_control']:+.3f}, {fmt_p(RES['p_control'])}, Holm {fmt_p(RES['p_holm_perceived control'])} [n = {RES['n_control']}]"),
    ("SSCE vs focus", f"r = {RES['r_focus']:+.3f}, {fmt_p(RES['p_focus'])} [n = {RES['n_focus']}]"),
    ("SSCE vs tech helpfulness", f"r = {RES['r_tech_helps']:+.3f}, {fmt_p(RES['p_tech_helps'])} [n = {RES['n_tech_helps']}]"),
    ("regression R^2", f"{REG['r2']:.3f} (F(4,{REG['dof']}) = {REG['F']:.2f}, {fmt_p(REG['pF'])}) [n = {REG['n']}]"),
    ("hierarchical delta R^2", f"{dR2:.3f} (F({int(df1)},{int(df2)}) = {Fch:.2f}, {fmt_p(pFch)}) [n = {len(m49d)}]"),
    ("mediation indirect", f"{ind:+.3f} [{m_lo:+.3f}, {m_hi:+.3f}] {'sig.' if med_sig else 'n.s.'} [n = {len(med)}]"),
    ("moderation p (gender/STEM/year)", f"{p_int_g:.3f} / {p_int_s:.3f} / {p_int_y:.3f} [n = {len(mm)} / {len(dz)} / {len(dz)}]"),
    ("Harman first factor", f"{ev[0]*100:.1f}% [n = {len(items)}]"),
    ("builds: exposure r range", f"{GRID.r.min():+.3f} to {GRID.r.max():+.3f} ({int((GRID.p<.05).sum())}/8 p<.05)"),
    ("cluster-excluded exposure r", f"{RES['cluster_r_screen_mid']:+.3f} (n = {len(cl)}, {fmt_p(RES['cluster_p_screen_mid'])})"),
    ("with Year 1 (n = 211): exposure r", f"{RES['y1in_exp_r']:+.3f} ({fmt_p(RES['y1in_exp_p'])})" if Y1 else "not run"),
    ("with Year 1: regression R^2", f"{Y1['r2']:.3f} (F(4,{Y1['dof']}) = {Y1['F']:.2f}) [n = {Y1['n']}]" if Y1 else "not run"),
    ("smallest r at 80% power", f"{r80:.3f} [n = {N}]"),
]
w = max(len(s[0]) for s in summary)
for k, v in summary:
    say(f"  {k:{w}s}  {v}")
say(f"\nOutputs: {OUTDIR}\nFigures: {FIGDIR} ({len(glob.glob(os.path.join(FIGDIR, '*.png')))} files)")

with open(os.path.join(OUTDIR, "RESULTS.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(LOG) + "\n")
