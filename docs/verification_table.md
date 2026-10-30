# Verification table: manuscript numbers vs script output (n = 171)

All values below come from `manuscript/SSCE_university.tex` and from the outputs
of `python scripts/university_analysis.py` (n = 171, seed 20260618):
`outputs/university/summary.json` and the `outputs/university/table_*.csv`
files written by the same run.

The `y1in_*` keys (the n = 211 comparison with first-year students included)
are produced only when the unshared original survey file is present locally.

## Part A. Key statistics, mapped by hand to their summary.json key

Each row gives a statistic stated in the manuscript, the exact `summary.json`
key it comes from, and the stored value. Two things are checked automatically:

- the stored value, rounded to the precision shown in the manuscript, equals
  the number shown;
- the quoted phrase occurs in the `.tex` file.

Result: **110 checks, 0 failures.**

A further scan looked for values whose 4-decimal printout ends in 5, where
rounding by hand can go wrong. It found five such errors, all now corrected:

| Statistic | Was | Corrected to |
|---|---|---|
| SSCE by year (ANOVA p) | .042 | .041 |
| SSCE gender equivalence (TOST p) | .139 | .138 |
| Count-based build p | .103 | .102 |
| Exposure r without the lowest band (p) | .161 | .160 |
| Device × year (p) | .107 | .106 |

No such error remains.

| Statement | Manuscript | summary.json key | Value in summary.json | Match |
|---|---|---|---|---|
| analytic n | 171 | `N` | 171 | yes |
| Year 2 n | 50 | `n_year_Uni Y2` | 50 | yes |
| Year 3 n | 91 | `n_year_Uni Y3` | 91 | yes |
| Year 4+ n | 30 | `n_year_Uni Y4+` | 30 | yes |
| male n | 94 | `n_gender_Male` | 94 | yes |
| female n | 70 | `n_gender_Female` | 70 | yes |
| Prefer not to say n | 7 | `n_gender_Prefer not to say` | 7 | yes |
| STEM n | 111 | `n_subject_STEM` | 111 | yes |
| full file rows | 430 | `full_rows` | 430 | yes |
| school-stage rows | 206 | `full_school` | 206 | yes |
| university-year rows | 218 | `full_uni` | 218 | yes |
| out-of-range rows | 6 | `full_out_of_range` | 6 | yes |
| school-institution excluded | 7 | `full_uni_school_institution` | 7 | yes |
| first-year excluded | 40 | `full_uni_year1_excluded` | 40 | yes |
| final analysed (funnel) | 171 | `full_analysed` | 171 | yes |
| focus-complete n | 169 | `reg_n` | 169 | yes |
| mean screen | 6.08 | `screen_mid_mean_all` | 6.07602 | yes |
| mean SSCE | 0.54 | `ssce_mean_all` | 0.539752 | yes |
| mean study | 3.17 | `study_hours_mean_all` | 3.16933 | yes |
| power r=.20 | .75 | `power_r20` | 0.747856 | yes |
| power r=.14 | .45 | `power_r14` | 0.447031 | yes |
| min r 80% | .21 | `min_r_80pct_power` | 0.213 | yes |
| CI .15 lo | .00 | `prec_this study_ci[0]` | -7.6847e-05 | yes |
| CI .15 hi | .29 | `prec_this study_ci[1]` | 0.293469 | yes |
| half-width | .15 | `prec_this study_halfwidth` | 0.146773 | yes |
| n needed r=.12 | 543 | `n_needed_r12_80pct` | 543 | yes |
| ratio | 3.2 | `n_needed_r12_80pct` | 3.17544 | yes |
| exp r | -.15 | `exp_r` | -0.15359 | yes |
| exp p | .045 | `exp_p` | 0.0448957 | yes |
| exp CI lo | -.30 | `exp_r_ci[0]` | -0.296823 | yes |
| exp CI hi | -.004 | `exp_r_ci[1]` | -0.00359746 | yes |
| slope | -0.022 | `exp_slope` | -0.0217638 | yes |
| slope CI lo | -0.044 | `exp_slope_ci[0]` | -0.0438239 | yes |
| slope CI hi | 0.001 | `exp_slope_ci[1]` | 0.00147264 | yes |
| linear R2 | .024 | `exp_r2_lin` | 0.0235898 | yes |
| quad p | .738 | `exp_p_quad` | 0.738286 | yes |
| r w/o lowest band | -.11 | `exp_r_without_lowest_band` | -0.110786 | yes |
| p w/o lowest band | .160 | `exp_p_without_lowest_band` | 0.160473 | yes |
| n w/o lowest band | 162 | `exp_n_without_lowest_band` | 162 | yes |
| screen ~ nonacad | +.38 | `exp_r_n_nonacademic` | 0.377694 | yes |
| screen ~ acad | +.13 | `exp_r_n_academic` | 0.131614 | yes |
| screen ~ acad p | .086 | `exp_p_n_academic` | 0.086175 | yes |
| workload ~ acad | +.01 | `r_workload_n_academic` | 0.00581499 | yes |
| workload ~ nonacad | -.23 | `r_workload_n_nonacademic` | -0.234625 | yes |
| SSCE year F | 3.24 | `ssce_anova_F` | 3.24386 | yes |
| SSCE year p | .041 | `ssce_anova_p` | 0.0414695 | yes |
| SSCE year KW p | .045 | `ssce_kw_p` | 0.0446941 | yes |
| study year p | .052 | `study_hours_anova_p` | 0.0516023 | yes |
| anova df2 | 168 | `ssce_anova_df[1]` | 168 | yes |
| r workload | +.245 | `r_workload` | 0.245366 | yes |
| p workload | .001 | `p_workload` | 0.00121797 | yes |
| Holm workload | .006 | `p_holm_workload` | 0.00608983 | yes |
| r control | +.128 | `r_control` | 0.127557 | yes |
| p control | .096 | `p_control` | 0.0963957 | yes |
| r switch | -.102 | `r_switch` | -0.102228 | yes |
| p switch | .183 | `p_switch` | 0.183357 | yes |
| switch CI lo | -.25 | `r_ci_switch[0]` | -0.248491 | yes |
| control CI lo | -.02 | `r_ci_control[0]` | -0.0229579 | yes |
| reg R2 | .10 | `reg_r2` | 0.102814 | yes |
| reg F | 4.70 | `reg_F` | 4.69846 | yes |
| reg p | .001 | `reg_pF` | 0.00129092 | yes |
| beta workload | +.271 | `beta_workload` | 0.270542 | yes |
| beta switch p | .088 | `pbeta_switch` | 0.0875659 | yes |
| beta control p | .299 | `pbeta_control` | 0.298923 | yes |
| uniq workload | .070 | `uniqueR2_workload` | 0.0700475 | yes |
| hier b1 R2 | .070 | `hier_b1_R2` | 0.0699239 | yes |
| hier b1 df | 161 | `hier_b1_df[1]` | 161 | yes |
| hier b2 R2 | .159 | `hier_b2_R2` | 0.159499 | yes |
| hier dR2 | .090 | `hier_dR2` | 0.0895752 | yes |
| hier p | .003 | `hier_pFch` | 0.00302021 | yes |
| med a | .26 | `med_a` | 0.263843 | yes |
| med b p | .402 | `med_b_p` | 0.401607 | yes |
| med indirect | -.017 | `med_indirect` | -0.0174985 | yes |
| med CI lo | -.064 | `med_ci_lo` | -0.0642939 | yes |
| med CI hi | .025 | `med_ci_hi` | 0.0252158 | yes |
| med direct p | .086 | `med_c_direct_p` | 0.0862781 | yes |
| Harman | 30.4 | `harman_first_pct` | 30.4216 | yes |
| TOST study p | .115 | `gender_study_hours_tost_p` | 0.114848 | yes |
| TOST ssce p | .138 | `gender_ssce_tost_p` | 0.138451 | yes |
| subject study p | .013 | `subject_study_hours_p` | 0.013313 | yes |
| device study p | .045 | `device_study_hours_p` | 0.0452466 | yes |
| device-year p | .106 | `device_year_p` | 0.106458 | yes |
| mod gender p | .652 | `mod_gender_p` | 0.651865 | yes |
| mod stem p | .991 | `mod_stem_p` | 0.991005 | yes |
| mod year p | .606 | `mod_year_p` | 0.606181 | yes |
| grid sel p min | .045 | `grid_9.0_selected_p` | 0.0448957 | yes |
| grid sel p max | .049 | `grid_11.0_selected_p` | 0.0487017 | yes |
| grid all p lo | .056 | `grid_11.0_all_p` | 0.0563304 | yes |
| grid all p hi | .102 | `grid_8.5_all_p` | 0.102467 | yes |
| split screen | 93.0 | `split_screen_mid_same_sign_pct` | 93 | yes |
| split switch | 80.6 | `split_switch_same_sign_pct` | 80.6 | yes |
| cluster flagged | 23 | `cluster_n_excluded` | 23 | yes |
| cluster n | 148 | `cluster_n` | 148 | yes |
| cluster r | -.25 | `cluster_r_screen_mid` | -0.245273 | yes |
| cluster reg R2 | .09 | `cluster_reg_r2` | 0.0911853 | yes |
| y1 n | 211 | `y1in_n` | 211 | yes |
| y1 exp r | -.14 | `y1in_exp_r` | -0.141302 | yes |
| y1 exp p | .040 | `y1in_exp_p` | 0.0403029 | yes |
| y1 workload | +.24 | `y1in_r_workload` | 0.239005 | yes |
| y1 switch p | .084 | `y1in_p_switch` | 0.0839141 | yes |
| y1 control r | +.18 | `y1in_r_control` | 0.17726 | yes |
| y1 control holm | .040 | `y1in_p_holm_control` | 0.0395176 | yes |
| y1 reg R2 | .12 | `y1in_reg_r2` | 0.116057 | yes |
| y1 reg n | 209 | `y1in_reg_n` | 209 | yes |
| text challenge n | 77 | `text_CHALLENGE_n` | 77 | yes |
| text distraction pct | 59.7 | `text_CHALLENGE_Distraction / task-switching_pct` | 59.7403 | yes |
| disclosure | 5 | `disclosure_unique_rows` | 5 | yes |
| this study CI width | .29 | `prec_this study_width` | 0.293546 | yes |
| Junco width | .09 | `prec_Junco & Cotten 2012_width` | 0.0893684 | yes |
| Giunchiglia width | .47 | `prec_Giunchiglia et al. 2018_width` | 0.470227 | yes |

## Part B. Every numeric token in the manuscript body

Every number in the body (abstract through Statements and Declarations,
excluding the bibliography) was extracted. Each one was matched against all
values in `summary.json` and the output tables, at the precision displayed.

Read this table with three cautions:

- **A match proves the number exists in the output, not that it is the right
  statistic.** Small integers and common values can match by coincidence; the
  half-rounding errors above were missed by this table and caught by Part A.
- **"design"** means a constant of the study design, not a result. Examples:
  dates, the seed, band midpoints, software and model versions, "95%" in
  "95% CI".
- **"cited source"** means a number reported by a cited study and verified
  against that study's abstract or full text. These numbers are not outputs of
  this analysis.

    Counter({'summary.json': 739, 'cited source': 27, 'design': 24, 'output table': 19})

| tex line | number | context | source | summary.json key(s) |
|---|---|---|---|---|
| 39 | 171 | …demic, in a cross-sectional online survey of 171 university students in B… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 39 | 18 | …university group in which respondents under 18 are plausible, were excl… | summary.json | `pct_year_Uni Y4+`, `n_device_Tablet`, `prec_Bjerre-Nielsen et al. 2020_width` (+8) |
| 39 | -.15 | …day reported a smaller academic share (r = -.15, p = .045, 95\% CI [… | summary.json | `exp_r`, `med_c_total`, `grid_r_min` (+10) |
| 39 | .045 | …d a smaller academic share (r = -.15, p = .045, 95\% CI [-.30, -.004]… | summary.json | `prec_Junco & Cotten 2012_halfwidth`, `ssce_kw_p`, `exp_p` (+7) |
| 39 | 95 | …ller academic share (r = -.15, p = .045, 95\% CI [-.30, -.004]). T… | design | — |
| 39 | -.30 | …mic share (r = -.15, p = .045, 95\% CI [-.30, -.004]). This associat… | summary.json | `exp_r_ci[0]`, `table_builds.csv[0].r_ci_lo`, `table_builds.csv[0].r_ci_hi` (+2) |
| 39 | -.004 | …are (r = -.15, p = .045, 95\% CI [-.30, -.004]). This association is… | summary.json | `exp_r_ci[1]`, `table_builds.csv[2].r_ci_hi`, `table_builds.csv[7].r_ci_lo` |
| 39 | .21 | …ation the sample could reliably detect (r .21 at 80\% power), the boo… | summary.json | `min_r_80pct_power`, `prec_this study_min_r_80`, `table_precision.csv[0].min_r_80` |
| 39 | 80 | …e sample could reliably detect (r .21 at 80\% power), the bootstrap… | summary.json | `n_device_Laptop/Desktop`, `table_sample.csv[10].n` |
| 39 | 9 | …t weakened and lost significance without the 9 students in the lowest s… | summary.json | `prec_Junco & Cotten 2012_width`, `prec_Bjerre-Nielsen et al. 2020_halfwidth`, `prec_Giunchiglia et al. 2018_ci[0]` (+19) |
| 39 | -.11 | …tudents in the lowest screen-time band (r = -.11, p = .160); it held a… | summary.json | `exp_r_without_lowest_band` |
| 39 | .160 | …he lowest screen-time band (r = -.11, p = .160); it held across all fo… | summary.json | `exp_p_without_lowest_band`, `split_screen_mid_median_r[0]`, `table_splithalf.csv[0].median_r_half1` |
| 39 | 8 | …four values assigned to the open ``more than 8 hours'' band and was str… | summary.json | `prec_Lepp et al. 2015_halfwidth`, `study_hours_kw_p`, `reg_adj` (+18) |
| 39 | +.25 | …ated positively with academic workload (r = +.25, p = .001), which rem… | summary.json | `r_workload`, `split_workload_median_r[0]`, `split_workload_median_r[1]` (+7) |
| 39 | .001 | …ely with academic workload (r = +.25, p = .001), which remained signif… | summary.json | `exp_slope_ci[1]`, `exp_r2_gain`, `exp_p_n_purposes` (+5) |
| 39 | +.13 | …ts correlations with perceived control (r = +.13, p = .096) and task-s… | summary.json | `prec_Bjerre-Nielsen et al. 2020_min_r_80`, `exp_r_n_academic`, `r_control` (+11) |
| 39 | .096 | …ons with perceived control (r = +.13, p = .096) and task-switching (r… | summary.json | `p_control`, `gender_ssce_bound`, `table_convergent.csv[3].p` (+1) |
| 39 | -.10 | …+.13, p = .096) and task-switching (r = -.10, p = .183) were not s… | summary.json | `r_switch`, `split_switch_median_r[0]`, `split_switch_median_r[1]` (+5) |
| 39 | .183 | ….096) and task-switching (r = -.10, p = .183) were not significant.… | summary.json | `p_switch`, `table_convergent.csv[0].p` |
| 39 | 10 | …elf-regulation indicators together explained 10\% of the variance in SSC… | summary.json | `pct_device_Tablet`, `r_switch`, `r_ci_workload[0]` (+24) |
| 39 | 2 | …r explained 10\% of the variance in SSCE (R^2 = .10, F(4, 164) = 4.7… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 39 | .10 | …plained 10\% of the variance in SSCE (R^2 = .10, F(4, 164) = 4.70, p… | summary.json | `r_switch`, `r_ci_workload[0]`, `p_control` (+18) |
| 39 | 4 | …0\% of the variance in SSCE (R^2 = .10, F(4, 164) = 4.70, p = .001… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 39 | 164 | …of the variance in SSCE (R^2 = .10, F(4, 164) = 4.70, p = .001), c… | summary.json | `reg_dof`, `mod_gender_n` |
| 39 | 4.70 | …variance in SSCE (R^2 = .10, F(4, 164) = 4.70, p = .001), carried b… | summary.json | `study_hours_ci_Uni Y4+[1]`, `reg_F`, `table_by_year.csv[2].study_hours_ci_hi` |
| 39 | .001 | …SSCE (R^2 = .10, F(4, 164) = 4.70, p = .001), carried by workload,… | summary.json | `exp_slope_ci[1]`, `exp_r2_gain`, `exp_p_n_purposes` (+5) |
| 39 | 2 | …nd gender, subject and university year ( R^2 = .09, p = .003). Scr… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 39 | .09 | …ender, subject and university year ( R^2 = .09, p = .003). Screen ex… | summary.json | `prec_Junco & Cotten 2012_width`, `prec_Bjerre-Nielsen et al. 2020_halfwidth`, `prec_Giunchiglia et al. 2018_ci[0]` (+14) |
| 39 | .003 | …ect and university year ( R^2 = .09, p = .003). Screen exposure was a… | summary.json | `hier_pFch`, `cluster_p_screen_mid`, `table_builds.csv[0].r_ci_hi` (+2) |
| 45 | 171 | …e did not ask for ages, we analysed only the 171 students in their second… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 45 | 18 | …second year or later, who would normally be 18 or older. Students who r… | summary.json | `pct_year_Uni Y4+`, `n_device_Tablet`, `prec_Bjerre-Nielsen et al. 2020_width` (+8) |
| 45 | 9 | …weak and depended partly on a small group of 9 students with under two… | summary.json | `prec_Junco & Cotten 2012_width`, `prec_Bjerre-Nielsen et al. 2020_halfwidth`, `prec_Giunchiglia et al. 2018_ci[0]` (+19) |
| 45 | 171 | …sers study a smaller share of the time. With 171 students, the study can… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 51 | 171 | …in high-income countries. This paper surveys 171 university students in B… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 53 | 1 | …{(1) A fully reproducible, o… | summary.json | `pct_device_Other`, `power_r20`, `ssce_ci_Uni Y2[1]` (+91) |
| 55 | 2 | …{(2) An exploratory efficien… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 57 | 3 | …{(3) A setting rarely repres… | summary.json | `prec_Rosen et al. 2013_ci[0]`, `study_hours_mean_Uni Y2`, `study_hours_ci_Uni Y2[1]` (+38) |
| 59 | 171 | …e exploratory rather than confirmatory. With 171 respondents the study is… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 82 | 3 | …box/.style={draw, rounded corners=3pt, align=center, minimum… | summary.json | `prec_Rosen et al. 2013_ci[0]`, `study_hours_mean_Uni Y2`, `study_hours_ci_Uni Y2[1]` (+38) |
| 82 | 1.1 | …ed corners=3pt, align=center, minimum height=1.1cm, text width=3.4cm, fon… | summary.json | `etg_Uni Y3->Uni Y4+_welch_t`, `table_etg_years.csv[1].welch_t` |
| 82 | 3.4 | …ign=center, minimum height=1.1cm, text width=3.4cm, font= },… | summary.json | `grid_mean_max`, `device_study_hours_mean_Laptop/Desktop`, `table_builds.csv[6].mean_study_h` |
| 83 | 2.5 | …arr/.style={-{Latex[length=2.5mm]}, thick},… | summary.json | `med_ci_hi`, `device_study_hours_F`, `device_study_hours_mean_Smartphone` (+1) |
| 84 | 1.5 | …lab/.style={font= , fill=white, inner sep=1.5pt}]… | summary.json | `etg_Uni Y3->Uni Y4+_ci_hi`, `table_etg_years.csv[1].ci_hi` |
| 101 | 4 | …Data were collected between 4 and 11 February 2026 thr… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 101 | 11 | …Data were collected between 4 and 11 February 2026 through an… | summary.json | `pct_subject_Arts`, `prec_Junco & Cotten 2012_ci[0]`, `exp_r_without_lowest_band` (+13) |
| 101 | 2026 | …ata were collected between 4 and 11 February 2026 through an anonymous Goo… | design | — |
| 101 | 6 | …naire was distributed to students from Class 6 to university: the link… | summary.json | `full_out_of_range`, `n_subject_Other`, `prec_Bjerre-Nielsen et al. 2020_ci[0]` (+29) |
| 103 | 6 | …School-stage responses (Class 6 to Class 12) are exclude… | summary.json | `full_out_of_range`, `n_subject_Other`, `prec_Bjerre-Nielsen et al. 2020_ci[0]` (+29) |
| 103 | 12 | …School-stage responses (Class 6 to Class 12) are excluded from this… | summary.json | `prec_Lepp et al. 2015_min_r_80`, `prec_Rosen et al. 2013_halfwidth`, `etg_Uni Y2->Uni Y3_p_holm` (+12) |
| 103 | 18 | …d from this paper because participants under 18 took part without parent… | summary.json | `pct_year_Uni Y4+`, `n_device_Tablet`, `prec_Bjerre-Nielsen et al. 2020_width` (+8) |
| 103 | 171 | …ethics review. This paper analyses only the 171 respondents who reported… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 103 | 94 | …this subset in advance. The sample comprised 94 male and 70 female stude… | summary.json | `n_gender_Male`, `p_workload_n_academic`, `table_sample.csv[3].n` |
| 103 | 70 | …in advance. The sample comprised 94 male and 70 female students and 7 wh… | summary.json | `n_gender_Female`, `table_sample.csv[4].n`, `table_ssce_by_band.csv[0].mean` |
| 103 | 7 | …comprised 94 male and 70 female students and 7 who chose ``Prefer not t… | summary.json | `full_uni_school_institution`, `n_gender_Prefer not to say`, `prec_Junco & Cotten 2012_min_r_80` (+19) |
| 103 | 111 | …`Prefer not to say'' for gender; by subject, 111 were STEM, 35 Commerce,… | summary.json | `n_subject_STEM`, `table_sample.csv[6].n` |
| 103 | 35 | …say'' for gender; by subject, 111 were STEM, 35 Commerce, 19 Arts and 6… | summary.json | `n_subject_Commerce`, `subject_ssce_sd_Commerce`, `device_year_min_expected` (+1) |
| 103 | 19 | …der; by subject, 111 were STEM, 35 Commerce, 19 Arts and 6 Other ( ). T… | summary.json | `n_subject_Arts`, `prec_Junco & Cotten 2012_ci[1]`, `prec_Lukram et al. 2026_halfwidth` (+4) |
| 103 | 6 | …ect, 111 were STEM, 35 Commerce, 19 Arts and 6 Other ( ). This is a co… | summary.json | `full_out_of_range`, `n_subject_Other`, `prec_Bjerre-Nielsen et al. 2020_ci[0]` (+29) |
| 105 | 18 | …son generally attains majority on completing 18 years , and every perso… | summary.json | `pct_year_Uni Y4+`, `n_device_Tablet`, `prec_Bjerre-Nielsen et al. 2020_width` (+8) |
| 105 | 18 | …ompleting 18 years , and every person up to 18 is treated as a child fo… | summary.json | `pct_year_Uni Y4+`, `n_device_Tablet`, `prec_Bjerre-Nielsen et al. 2020_width` (+8) |
| 105 | 1 | …lished . The official age of entry to Grade 1 is 6, and late entry is… | summary.json | `pct_device_Other`, `power_r20`, `ssce_ci_Uni Y2[1]` (+91) |
| 105 | 6 | …d . The official age of entry to Grade 1 is 6, and late entry is far mo… | summary.json | `full_out_of_range`, `n_subject_Other`, `prec_Bjerre-Nielsen et al. 2020_ci[0]` (+29) |
| 105 | 400 | …ore common than early entry ; in a study of 400 first-year students at a… | summary.json | `hier_df1`, `grid_n_sig`, `device_study_hours_df[0]` (+3) |
| 105 | 18 | …o age criterion for inclusion, all were aged 18 to 23 . On the usual pa… | summary.json | `pct_year_Uni Y4+`, `n_device_Tablet`, `prec_Bjerre-Nielsen et al. 2020_width` (+8) |
| 105 | 23 | …criterion for inclusion, all were aged 18 to 23 . On the usual path, th… | summary.json | `prec_Lepp et al. 2015_ci[1]`, `etg_Uni Y3->Uni Y4+_cohen_d`, `r_workload_n_nonacademic` (+6) |
| 105 | 18 | …herefore, students begin university at about 18, and those in their secon… | summary.json | `pct_year_Uni Y4+`, `n_device_Tablet`, `prec_Bjerre-Nielsen et al. 2020_width` (+8) |
| 105 | 18 | …no admission rule that sets a minimum age of 18, however, and a pupil who… | summary.json | `pct_year_Uni Y4+`, `n_device_Tablet`, `prec_Bjerre-Nielsen et al. 2020_width` (+8) |
| 105 | 17 | …arted school early could begin university at 17. First-year students are… | summary.json | `prec_Lepp et al. 2015_width`, `prec_Rosen et al. 2013_min_r_80`, `table_precision.csv[2].width` (+1) |
| 105 | 18 | …university group in which a respondent under 18 is most plausible, so al… | summary.json | `pct_year_Uni Y4+`, `n_device_Tablet`, `prec_Bjerre-Nielsen et al. 2020_width` (+8) |
| 105 | 40 | …espondent under 18 is most plausible, so all 40 first-year respondents w… | summary.json | `full_uni_year1_excluded`, `med_b_p` |
| 105 | 211 | …riction was decided after an analysis of all 211 university respondents h… | summary.json | `full_uni_university_institution`, `y1in_n`, `y1in_n_switch` (+3) |
| 105 | 211 | …to show its effect, the main results for all 211 are reported in .… | summary.json | `full_uni_university_institution`, `y1in_n`, `y1in_n_switch` (+3) |
| 108 | 19 | …The 19-item questionnaire recor… | summary.json | `n_subject_Arts`, `prec_Junco & Cotten 2012_ci[1]`, `prec_Lukram et al. 2026_halfwidth` (+4) |
| 108 | 1 | …ion and context items covered ease of focus (1 – 5), perceived control… | summary.json | `pct_device_Other`, `power_r20`, `ssce_ci_Uni Y2[1]` (+91) |
| 108 | 5 | …and context items covered ease of focus (1 – 5), perceived control over… | summary.json | `prec_Lukram et al. 2026_ci[0]`, `screen_mid_ci_Uni Y2[0]`, `study_hours_ci_Uni Y4+[1]` (+24) |
| 108 | 1 | …ived control over technology while studying (1 – 5), frequency of task-… | summary.json | `pct_device_Other`, `power_r20`, `ssce_ci_Uni Y2[1]` (+91) |
| 108 | 5 | …control over technology while studying (1 – 5), frequency of task-swit… | summary.json | `prec_Lukram et al. 2026_ci[0]`, `screen_mid_ci_Uni Y2[0]`, `study_hours_ci_Uni Y4+[1]` (+24) |
| 115 | 2 | …of screen use. The bands map as: ``Less than 2 h'' 1.0, ``2 – 4 h''… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 115 | 1.0 | …use. The bands map as: ``Less than 2 h'' 1.0, ``2 – 4 h'' 3.0, ``… | summary.json | `y1in_p_control`, `device_ssce_F`, `mod_stem_p` (+5) |
| 115 | 2 | …e bands map as: ``Less than 2 h'' 1.0, ``2 – 4 h'' 3.0, ``4 – 6… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 115 | 4 | …nds map as: ``Less than 2 h'' 1.0, ``2 – 4 h'' 3.0, ``4 – 6 h''… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 115 | 3.0 | …: ``Less than 2 h'' 1.0, ``2 – 4 h'' 3.0, ``4 – 6 h'' 5.0, ``… | summary.json | `prec_Rosen et al. 2013_ci[0]`, `study_hours_anova_F`, `etg_Uni Y2->Uni Y3_ci_lo` (+8) |
| 115 | 4 | …s than 2 h'' 1.0, ``2 – 4 h'' 3.0, ``4 – 6 h'' 5.0, ``6 – 8… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 115 | 6 | …an 2 h'' 1.0, ``2 – 4 h'' 3.0, ``4 – 6 h'' 5.0, ``6 – 8 h''… | summary.json | `full_out_of_range`, `n_subject_Other`, `prec_Bjerre-Nielsen et al. 2020_ci[0]` (+29) |
| 115 | 5.0 | …1.0, ``2 – 4 h'' 3.0, ``4 – 6 h'' 5.0, ``6 – 8 h'' 7.0, an… | summary.json | `study_hours_kw_H`, `disclosure_unique_rows`, `table_device_by_year.csv[2].Mixed` (+1) |
| 115 | 6 | …``2 – 4 h'' 3.0, ``4 – 6 h'' 5.0, ``6 – 8 h'' 7.0, and the… | summary.json | `full_out_of_range`, `n_subject_Other`, `prec_Bjerre-Nielsen et al. 2020_ci[0]` (+29) |
| 115 | 8 | …– 4 h'' 3.0, ``4 – 6 h'' 5.0, ``6 – 8 h'' 7.0, and the ope… | summary.json | `prec_Lepp et al. 2015_halfwidth`, `study_hours_kw_p`, `reg_adj` (+18) |
| 115 | 7.0 | …3.0, ``4 – 6 h'' 5.0, ``6 – 8 h'' 7.0, and the open band ``Mor… | summary.json | `full_uni_school_institution`, `n_gender_Prefer not to say`, `uniqueR2_workload` (+6) |
| 115 | 8 | …8 h'' 7.0, and the open band ``More than 8 h'' 9.0 (a bounded,… | summary.json | `prec_Lepp et al. 2015_halfwidth`, `study_hours_kw_p`, `reg_adj` (+18) |
| 115 | 9.0 | …7.0, and the open band ``More than 8 h'' 9.0 (a bounded, conservative… | summary.json | `hier_dR2`, `text_SUGGESTIONS_Focus/distraction controls_n`, `table_builds.csv[2].mid_high` (+3) |
| 119 | 1 | …items were coded as ordered numbers: focus (1 – 5), control (1 – 5), t… | summary.json | `pct_device_Other`, `power_r20`, `ssce_ci_Uni Y2[1]` (+91) |
| 119 | 5 | …ms were coded as ordered numbers: focus (1 – 5), control (1 – 5), task-… | summary.json | `prec_Lukram et al. 2026_ci[0]`, `screen_mid_ci_Uni Y2[0]`, `study_hours_ci_Uni Y4+[1]` (+24) |
| 119 | 1 | …as ordered numbers: focus (1 – 5), control (1 – 5), task-switching (1… | summary.json | `pct_device_Other`, `power_r20`, `ssce_ci_Uni Y2[1]` (+91) |
| 119 | 5 | …ordered numbers: focus (1 – 5), control (1 – 5), task-switching (1 – 4,… | summary.json | `prec_Lukram et al. 2026_ci[0]`, `screen_mid_ci_Uni Y2[0]`, `study_hours_ci_Uni Y4+[1]` (+24) |
| 119 | 1 | …us (1 – 5), control (1 – 5), task-switching (1 – 4, higher = more switc… | summary.json | `pct_device_Other`, `power_r20`, `ssce_ci_Uni Y2[1]` (+91) |
| 119 | 4 | …1 – 5), control (1 – 5), task-switching (1 – 4, higher = more switching)… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 119 | 1 | …(1 – 4, higher = more switching), workload (1 – 4, higher = heavier) a… | summary.json | `pct_device_Other`, `power_r20`, `ssce_ci_Uni Y2[1]` (+91) |
| 119 | 4 | …– 4, higher = more switching), workload (1 – 4, higher = heavier) and te… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 119 | 1 | …igher = heavier) and technology helpfulness (1 – 5, higher = more helpf… | summary.json | `pct_device_Other`, `power_r20`, `ssce_ci_Uni Y2[1]` (+91) |
| 119 | 5 | …r = heavier) and technology helpfulness (1 – 5, higher = more helpful).… | summary.json | `prec_Lukram et al. 2026_ci[0]`, `screen_mid_ci_Uni Y2[0]`, `study_hours_ci_Uni Y4+[1]` (+24) |
| 121 | 0.5 | …and two non-academic purposes has an SSCE of 0.5 regardless of how the ho… | summary.json | `prec_Giunchiglia et al. 2018_width`, `ssce_mean_Uni Y2`, `ssce_mean_Uni Y3` (+28) |
| 124 | 430 | …The original survey file contains 430 responses: 206 from scho… | summary.json | `full_rows` |
| 124 | 206 | …original survey file contains 430 responses: 206 from school stages (Clas… | summary.json | `full_school` |
| 124 | 6 | …430 responses: 206 from school stages (Class 6 to Class 12), 218 from t… | summary.json | `full_out_of_range`, `n_subject_Other`, `prec_Bjerre-Nielsen et al. 2020_ci[0]` (+29) |
| 124 | 12 | …es: 206 from school stages (Class 6 to Class 12), 218 from the four univ… | summary.json | `prec_Lepp et al. 2015_min_r_80`, `prec_Rosen et al. 2013_halfwidth`, `etg_Uni Y2->Uni Y3_p_holm` (+12) |
| 124 | 218 | …06 from school stages (Class 6 to Class 12), 218 from the four university… | summary.json | `full_uni` |
| 124 | 6 | …rom the four university-year categories, and 6 that reported a stage ou… | summary.json | `full_out_of_range`, `n_subject_Other`, `prec_Bjerre-Nielsen et al. 2020_ci[0]` (+29) |
| 124 | 218 | …ginal analysis and are excluded here. Of the 218 university-year response… | summary.json | `full_uni` |
| 124 | 7 | …here. Of the 218 university-year responses, 7 named a school as their… | summary.json | `full_uni_school_institution`, `n_gender_Prefer not to say`, `prec_Junco & Cotten 2012_min_r_80` (+19) |
| 124 | 4 | …nses, 7 named a school as their institution (4 a higher secondary schoo… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 124 | 11 | …tution (4 a higher secondary school, Classes 11 – 12, and 3 a secondary… | summary.json | `pct_subject_Arts`, `prec_Junco & Cotten 2012_ci[0]`, `exp_r_without_lowest_band` (+13) |
| 124 | 12 | …n (4 a higher secondary school, Classes 11 – 12, and 3 a secondary school… | summary.json | `prec_Lepp et al. 2015_min_r_80`, `prec_Rosen et al. 2013_halfwidth`, `etg_Uni Y2->Uni Y3_p_holm` (+12) |
| 124 | 3 | …igher secondary school, Classes 11 – 12, and 3 a secondary school, Clas… | summary.json | `prec_Rosen et al. 2013_ci[0]`, `study_hours_mean_Uni Y2`, `study_hours_ci_Uni Y2[1]` (+38) |
| 124 | 6 | …s 11 – 12, and 3 a secondary school, Classes 6 – 10); their reported st… | summary.json | `full_out_of_range`, `n_subject_Other`, `prec_Bjerre-Nielsen et al. 2020_ci[0]` (+29) |
| 124 | 10 | …– 12, and 3 a secondary school, Classes 6 – 10); their reported stage i… | summary.json | `pct_device_Tablet`, `r_switch`, `r_ci_workload[0]` (+24) |
| 124 | 18 | …dictory, and they may be school pupils under 18, so they were excluded. O… | summary.json | `pct_year_Uni Y4+`, `n_device_Tablet`, `prec_Bjerre-Nielsen et al. 2020_width` (+8) |
| 124 | 211 | …18, so they were excluded. Of the remaining 211, the 40 first-year studen… | summary.json | `full_uni_university_institution`, `y1in_n`, `y1in_n_switch` (+3) |
| 124 | 40 | …hey were excluded. Of the remaining 211, the 40 first-year students were… | summary.json | `full_uni_year1_excluded`, `med_b_p` |
| 124 | 171 | …en above, leaving an analytic sample of n = 171. All 171 had a screen-t… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 124 | 171 | …leaving an analytic sample of n = 171. All 171 had a screen-time band a… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 124 | 2 | …t one purpose. Ease of focus was missing for 2 respondents, so the mode… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 124 | 169 | …hical regression and Harman's test) use n = 169; every other analysis,… | summary.json | `n_focus`, `reg_n`, `hier_n` (+2) |
| 124 | 171 | …he mediation and interaction tests, uses all 171.… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 126 | 171 | …The shared dataset contains only these 171 responses. The original… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 131 | 1 | …{ETG}_k = {x}_{k+1} - {x}_k… | summary.json | `pct_device_Other`, `power_r20`, `ssce_ci_Uni Y2[1]` (+91) |
| 135 | 1 | …{ {x}_2 - {x}_1}{s_p}, s_p = { {(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{… | summary.json | `pct_device_Other`, `power_r20`, `ssce_ci_Uni Y2[1]` (+91) |
| 135 | 2 | …}_2 - {x}_1}{s_p}, s_p = { {(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 +… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 135 | 1 | …1}{s_p}, s_p = { {(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}}… | summary.json | `pct_device_Other`, `power_r20`, `ssce_ci_Uni Y2[1]` (+91) |
| 135 | 2 | …}, s_p = { {(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}}… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 135 | 2 | …(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}}… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 138 | 2 | …t = { {x}_2 - {x}_1}{ {s_1^2/n_1 + s_2^2/n_2}}… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 138 | 2 | …t = { {x}_2 - {x}_1}{ {s_1^2/n_1 + s_2^2/n_2}}… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 142 | 2 | …^2 = SS_ {between} / SS_ {t… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 144 | 10,000 | …and the mediation effect use the bootstrap (10,000 resamples) ; intervals… | summary.json | `full_uni_school_institution_records[0]` |
| 146 | 2 | …(x_i - {x})(y_i - {y})}{ { (x_i - {x})^2 (y_i - {y})^2}}… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 146 | 2 | …i - {y})}{ { (x_i - {x})^2 (y_i - {y})^2}}… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 152 | 2 | …ned variance into each predictor's unique R^2 (the drop in R^2 when… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 152 | 2 | …ach predictor's unique R^2 (the drop in R^2 when that predictor is… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 154 | 1 | …(gender, subject and university year; Block 1) and then on the four se… | summary.json | `pct_device_Other`, `power_r20`, `ssce_ci_Uni Y2[1]` (+91) |
| 154 | 2 | …n the four self-regulation indicators (Block 2), with the change in R^… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 154 | 2 | …indicators (Block 2), with the change in R^2 tested by an F-change… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 154 | 95 | …g to SSCE controlling for exposure, with the 95\% interval bracketed by… | design | — |
| 154 | 10,000 | …osure, with the 95\% interval bracketed by a 10,000-sample bootstrap. To gau… | summary.json | `full_uni_school_institution_records[0]` |
| 154 | 50 | …st unrotated factor accounting for less than 50\% of variance indicates… | summary.json | `n_year_Uni Y2`, `device_study_hours_mean_Other`, `device_ssce_mean_Other` (+4) |
| 156 | 20260618 | …All random steps used a fixed seed (20260618). Analyses ran in Python… | design | — |
| 156 | 3.14 | …ixed seed (20260618). Analyses ran in Python 3.14 with NumPy 2.4, pandas 3… | design | — |
| 156 | 2.4 | …618). Analyses ran in Python 3.14 with NumPy 2.4, pandas 3.0, SciPy, stat… | summary.json | `study_hours_sd_Uni Y4+`, `screen_mid_sd_Uni Y4+`, `exp_r2_lin` (+5) |
| 156 | 3.0 | …es ran in Python 3.14 with NumPy 2.4, pandas 3.0, SciPy, statsmodels and… | summary.json | `prec_Rosen et al. 2013_ci[0]`, `study_hours_anova_F`, `etg_Uni Y2->Uni Y3_ci_lo` (+8) |
| 158 | 171 | …{Sample size and power.} With n = 171, a two-tailed correlati… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 158 | .05 | …171, a two-tailed correlation test at = .05 had .75 power to detect… | summary.json | `prec_Lukram et al. 2026_ci[0]`, `study_hours_anova_p`, `exp_p_n_purposes` (+18) |
| 158 | .75 | …two-tailed correlation test at = .05 had .75 power to detect r = .20… | summary.json | `power_r20` |
| 158 | .20 | …st at = .05 had .75 power to detect r = .20 and .45 power to detect… | summary.json | `p_workload_n_nonacademic`, `p_bh_focus ease`, `p_bh_perceived control` (+6) |
| 158 | .45 | …= .05 had .75 power to detect r = .20 and .45 power to detect r = .14… | summary.json | `power_r14`, `cluster_p_tech_helps`, `cluster_pbeta_control` (+1) |
| 158 | .14 | …etect r = .20 and .45 power to detect r = .14; the smallest correlati… | summary.json | `r_ci_tech_helps[0]`, `beta_switch`, `med_c_direct` (+13) |
| 158 | 80 | …4; the smallest correlation detectable with 80\% power was r .21. M… | summary.json | `n_device_Laptop/Desktop`, `table_sample.csv[10].n` |
| 158 | .21 | …relation detectable with 80\% power was r .21. Most of the correlatio… | summary.json | `min_r_80pct_power`, `prec_this study_min_r_80`, `table_precision.csv[0].min_r_80` |
| 173 | 2 | …ent i's reported screen-time band (e.g., ``2 – 4 h'' maps to 3.0 h) \… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 173 | 4 | …i's reported screen-time band (e.g., ``2 – 4 h'' maps to 3.0 h) \\… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 173 | 3.0 | …screen-time band (e.g., ``2 – 4 h'' maps to 3.0 h) \\… | summary.json | `prec_Rosen et al. 2013_ci[0]`, `study_hours_anova_F`, `etg_Uni Y2->Uni Y3_ci_lo` (+8) |
| 178 | 1 | …n mean study time between university year k+1 and year k (a between… | summary.json | `pct_device_Other`, `power_r20`, `ssce_ci_Uni Y2[1]` (+91) |
| 185 | 2 | …^2 & Eta-squared: proporti… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 191 | 0 | …ormation: each variable standardised to mean 0, SD 1 \\… | summary.json | `n_excluded_school_institution`, `n_excluded_year1`, `power_r14` (+414) |
| 191 | 1 | …on: each variable standardised to mean 0, SD 1 \\… | summary.json | `pct_device_Other`, `power_r20`, `ssce_ci_Uni Y2[1]` (+91) |
| 201 | 6.08 | …Students reported 6.08 h of total screen time o… | summary.json | `screen_mid_mean_all` |
| 201 | 2.26 | …reen time on the previous day on average (SD 2.26), of which an average sh… | summary.json | `screen_mid_sd_all` |
| 201 | 0.54 | …rage (SD 2.26), of which an average share of 0.54 was academic (SSCE; SD 0… | summary.json | `ssce_mean_Uni Y3`, `ssce_mean_all`, `subject_ssce_F` (+2) |
| 201 | 0.32 | …average share of 0.54 was academic (SSCE; SD 0.32), giving a mean study-ti… | summary.json | `ssce_sd_all` |
| 201 | 3.17 | …SD 0.32), giving a mean study-time proxy of 3.17 h/day (SD 2.20). The sam… | summary.json | `study_hours_mean_all`, `table_builds.csv[2].mean_study_h` |
| 201 | 2.20 | …ng a mean study-time proxy of 3.17 h/day (SD 2.20). The sample leaned male… | summary.json | `study_hours_sd_all`, `subject_study_hours_sd_STEM` |
| 201 | 55 | ….17 h/day (SD 2.20). The sample leaned male (55\%) and STEM (65\%), and… | summary.json | `pct_gender_Male`, `ssce_ci_Uni Y2[1]`, `device_ssce_mean_Laptop/Desktop` (+3) |
| 201 | 65 | …20). The sample leaned male (55\%) and STEM (65\%), and the third year w… | summary.json | `pct_subject_STEM`, `ssce_mean_Uni Y4+`, `y1in_p_tech_helps` (+4) |
| 212 | 2 | …University year & Year 2 & 50 & 29.2 \\… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 212 | 50 | …University year & Year 2 & 50 & 29.2 \\… | summary.json | `n_year_Uni Y2`, `device_study_hours_mean_Other`, `device_ssce_mean_Other` (+4) |
| 212 | 29.2 | …University year & Year 2 & 50 & 29.2 \\… | summary.json | `pct_year_Uni Y2`, `table_sample.csv[0].pct` |
| 213 | 3 | …& Year 3 & 91 & 53.2 \\… | summary.json | `prec_Rosen et al. 2013_ci[0]`, `study_hours_mean_Uni Y2`, `study_hours_ci_Uni Y2[1]` (+38) |
| 213 | 91 | …& Year 3 & 91 & 53.2 \\… | summary.json | `n_year_Uni Y3`, `table_by_year.csv[1].n`, `table_etg_years.csv[0].n_b` (+2) |
| 213 | 53.2 | …& Year 3 & 91 & 53.2 \\… | summary.json | `pct_year_Uni Y3`, `etg_Uni Y3->Uni Y4+_etg`, `table_etg_years.csv[1].etg` (+2) |
| 214 | 4 | …& Year 4 or above & 30 & 17.5 \\… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 214 | 30 | …& Year 4 or above & 30 & 17.5 \\… | summary.json | `n_year_Uni Y4+`, `ssce_sd_Uni Y2`, `exp_r_ci[0]` (+12) |
| 214 | 17.5 | …& Year 4 or above & 30 & 17.5 \\… | summary.json | `pct_year_Uni Y4+`, `etg_Uni Y3->Uni Y4+_d_lo`, `table_etg_years.csv[1].d_lo` (+1) |
| 216 | 94 | …Gender & Male & 94 & 55.0 \\… | summary.json | `n_gender_Male`, `p_workload_n_academic`, `table_sample.csv[3].n` |
| 216 | 55.0 | …Gender & Male & 94 & 55.0 \\… | summary.json | `pct_gender_Male`, `table_sample.csv[3].pct` |
| 217 | 70 | …& Female & 70 & 40.9 \\… | summary.json | `n_gender_Female`, `table_sample.csv[4].n`, `table_ssce_by_band.csv[0].mean` |
| 217 | 40.9 | …& Female & 70 & 40.9 \\… | summary.json | `pct_gender_Female`, `table_sample.csv[4].pct` |
| 218 | 7 | …& Prefer not to say & 7 & 4.1 \\… | summary.json | `full_uni_school_institution`, `n_gender_Prefer not to say`, `prec_Junco & Cotten 2012_min_r_80` (+19) |
| 218 | 4.1 | …& Prefer not to say & 7 & 4.1 \\… | summary.json | `pct_gender_Prefer not to say`, `ssce_anova_p`, `table_sample.csv[5].pct` (+1) |
| 220 | 111 | …Subject & STEM & 111 & 64.9 \\… | summary.json | `n_subject_STEM`, `table_sample.csv[6].n` |
| 220 | 64.9 | …Subject & STEM & 111 & 64.9 \\… | summary.json | `pct_subject_STEM`, `table_sample.csv[6].pct` |
| 221 | 35 | …& Commerce & 35 & 20.5 \\… | summary.json | `n_subject_Commerce`, `subject_ssce_sd_Commerce`, `device_year_min_expected` (+1) |
| 221 | 20.5 | …& Commerce & 35 & 20.5 \\… | summary.json | `pct_subject_Commerce`, `cluster_p_switch`, `table_cluster_sensitivity.csv[1].p` (+1) |
| 222 | 19 | …& Arts & 19 & 11.1 \\… | summary.json | `n_subject_Arts`, `prec_Junco & Cotten 2012_ci[1]`, `prec_Lukram et al. 2026_halfwidth` (+4) |
| 222 | 11.1 | …& Arts & 19 & 11.1 \\… | summary.json | `pct_subject_Arts`, `exp_r_without_lowest_band`, `table_sample.csv[8].pct` |
| 223 | 6 | …& Other & 6 & 3.5 \\… | summary.json | `full_out_of_range`, `n_subject_Other`, `prec_Bjerre-Nielsen et al. 2020_ci[0]` (+29) |
| 223 | 3.5 | …& Other & 6 & 3.5 \\… | summary.json | `pct_subject_Other`, `study_hours_eta2`, `cluster_reg_F` (+3) |
| 225 | 80 | …Study device & Laptop/Desktop & 80 & 46.8 \\… | summary.json | `n_device_Laptop/Desktop`, `table_sample.csv[10].n` |
| 225 | 46.8 | …Study device & Laptop/Desktop & 80 & 46.8 \\… | summary.json | `pct_device_Laptop/Desktop`, `table_sample.csv[10].pct` |
| 226 | 46 | …& Smartphone & 46 & 26.9 \\… | summary.json | `n_device_Smartphone`, `text_CHALLENGE_Distraction / task-switching_n`, `table_device_by_year.csv[1].Laptop/Desktop` (+2) |
| 226 | 26.9 | …& Smartphone & 46 & 26.9 \\… | summary.json | `pct_device_Smartphone`, `table_sample.csv[11].pct` |
| 227 | 25 | …& Mixed & 25 & 14.6 \\… | summary.json | `n_device_Mixed`, `r_ci_switch[0]`, `r_workload` (+14) |
| 227 | 14.6 | …& Mixed & 25 & 14.6 \\… | summary.json | `pct_device_Mixed`, `grid_r_max`, `grid_11.0_all_r` (+2) |
| 228 | 18 | …& & 18 & 10.5 \\… | summary.json | `pct_year_Uni Y4+`, `n_device_Tablet`, `prec_Bjerre-Nielsen et al. 2020_width` (+8) |
| 228 | 10.5 | …& & 18 & 10.5 \\… | summary.json | `pct_device_Tablet`, `prec_Junco & Cotten 2012_ci[0]`, `split_switch_median_r[1]` (+5) |
| 229 | 2 | …& Other & 2 & 1.2 \\… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 229 | 1.2 | …& Other & 2 & 1.2 \\… | summary.json | `pct_device_Other`, `table_sample.csv[14].pct` |
| 242 | 2 | …s the three university-year groups (ANOVA F(2, 168) = 3.24, p = .041… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 242 | 168 | …he three university-year groups (ANOVA F(2, 168) = 3.24, p = .041,… | summary.json | `study_hours_anova_df[1]`, `ssce_anova_df[1]` |
| 242 | 3.24 | …e university-year groups (ANOVA F(2, 168) = 3.24, p = .041, ^2 = .03… | summary.json | `ssce_anova_F` |
| 242 | .041 | …-year groups (ANOVA F(2, 168) = 3.24, p = .041, ^2 = .037; Kruskal… | summary.json | `ssce_anova_p`, `table_ssce_by_band.csv[2].se` |
| 242 | 2 | …ps (ANOVA F(2, 168) = 3.24, p = .041, ^2 = .037; Kruskal – Walli… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 242 | .037 | …ANOVA F(2, 168) = 3.24, p = .041, ^2 = .037; Kruskal – Wallis H(2)… | summary.json | `ssce_eta2` |
| 242 | 2 | …p = .041, ^2 = .037; Kruskal – Wallis H(2) = 6.22, p = .045), r… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 242 | 6.22 | …041, ^2 = .037; Kruskal – Wallis H(2) = 6.22, p = .045), rising fr… | summary.json | `ssce_kw_H` |
| 242 | .045 | ….037; Kruskal – Wallis H(2) = 6.22, p = .045), rising from .47 in Ye… | summary.json | `prec_Junco & Cotten 2012_halfwidth`, `ssce_kw_p`, `exp_p` (+7) |
| 242 | .47 | …llis H(2) = 6.22, p = .045), rising from .47 in Year 2 to .54 in Year… | summary.json | `prec_Giunchiglia et al. 2018_width`, `ssce_mean_Uni Y2`, `gender_study_hours_p` (+5) |
| 242 | 2 | …6.22, p = .045), rising from .47 in Year 2 to .54 in Year 3 and .65… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 242 | .54 | …, p = .045), rising from .47 in Year 2 to .54 in Year 3 and .65 in Yea… | summary.json | `ssce_mean_Uni Y3`, `ssce_mean_all`, `subject_ssce_F` (+2) |
| 242 | 3 | …), rising from .47 in Year 2 to .54 in Year 3 and .65 in Year 4 and ab… | summary.json | `prec_Rosen et al. 2013_ci[0]`, `study_hours_mean_Uni Y2`, `study_hours_ci_Uni Y2[1]` (+38) |
| 242 | .65 | …sing from .47 in Year 2 to .54 in Year 3 and .65 in Year 4 and above; stu… | summary.json | `ssce_mean_Uni Y4+`, `etg_Uni Y2->Uni Y3_d_lo`, `y1in_p_tech_helps` (+4) |
| 242 | 4 | …7 in Year 2 to .54 in Year 3 and .65 in Year 4 and above; study time sh… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 242 | 2 | …pattern but did not differ significantly (F(2, 168) = 3.02, p = .052… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 242 | 168 | …tern but did not differ significantly (F(2, 168) = 3.02, p = .052,… | summary.json | `study_hours_anova_df[1]`, `ssce_anova_df[1]` |
| 242 | 3.02 | …t did not differ significantly (F(2, 168) = 3.02, p = .052, ^2 = .03… | summary.json | `study_hours_anova_F` |
| 242 | .052 | …ffer significantly (F(2, 168) = 3.02, p = .052, ^2 = .035; H(2) =… | summary.json | `study_hours_anova_p` |
| 242 | 2 | …ficantly (F(2, 168) = 3.02, p = .052, ^2 = .035; H(2) = 4.96,… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 242 | .035 | …ntly (F(2, 168) = 3.02, p = .052, ^2 = .035; H(2) = 4.96, p = .0… | summary.json | `study_hours_eta2`, `cluster_beta_focus` |
| 242 | 2 | …, 168) = 3.02, p = .052, ^2 = .035; H(2) = 4.96, p = .084) (… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 242 | 4.96 | …) = 3.02, p = .052, ^2 = .035; H(2) = 4.96, p = .084) ( ; an… | summary.json | `study_hours_kw_H` |
| 242 | .084 | …p = .052, ^2 = .035; H(2) = 4.96, p = .084) ( ; and~ ). Neithe… | summary.json | `study_hours_kw_p`, `y1in_p_switch` |
| 242 | 5.76 | …treated as exploratory. Mean screen time was 5.76 h in Year 2, 6.21 h in Y… | summary.json | `screen_mid_mean_Uni Y2`, `table_by_year.csv[0].screen_mid_mean` |
| 242 | 2 | …oratory. Mean screen time was 5.76 h in Year 2, 6.21 h in Year 3 and 6.2… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 242 | 6.21 | …tory. Mean screen time was 5.76 h in Year 2, 6.21 h in Year 3 and 6.20 h i… | summary.json | `screen_mid_mean_Uni Y3`, `table_by_year.csv[1].screen_mid_mean` |
| 242 | 3 | …en time was 5.76 h in Year 2, 6.21 h in Year 3 and 6.20 h in Year 4 and… | summary.json | `prec_Rosen et al. 2013_ci[0]`, `study_hours_mean_Uni Y2`, `study_hours_ci_Uni Y2[1]` (+38) |
| 242 | 6.20 | …e was 5.76 h in Year 2, 6.21 h in Year 3 and 6.20 h in Year 4 and above. B… | summary.json | `screen_mid_mean_Uni Y4+`, `table_by_year.csv[2].screen_mid_mean` |
| 242 | 4 | …Year 2, 6.21 h in Year 3 and 6.20 h in Year 4 and above. Because diffe… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 251 | 3 | …& & {3}{c}{Study time (h/day)}… | summary.json | `prec_Rosen et al. 2013_ci[0]`, `study_hours_mean_Uni Y2`, `study_hours_ci_Uni Y2[1]` (+38) |
| 251 | 3 | …& & {3}{c}{Study time (h/day)} & {3}{c}{SSCE} \\… | summary.json | `prec_Rosen et al. 2013_ci[0]`, `study_hours_mean_Uni Y2`, `study_hours_ci_Uni Y2[1]` (+38) |
| 252 | 3 | …(lr){3-5} (l){6-8}… | summary.json | `prec_Rosen et al. 2013_ci[0]`, `study_hours_mean_Uni Y2`, `study_hours_ci_Uni Y2[1]` (+38) |
| 252 | 5 | …(lr){3-5} (l){6-8}… | summary.json | `prec_Lukram et al. 2026_ci[0]`, `screen_mid_ci_Uni Y2[0]`, `study_hours_ci_Uni Y4+[1]` (+24) |
| 252 | 6 | …(lr){3-5} (l){6-8}… | summary.json | `full_out_of_range`, `n_subject_Other`, `prec_Bjerre-Nielsen et al. 2020_ci[0]` (+29) |
| 252 | 8 | …(lr){3-5} (l){6-8}… | summary.json | `prec_Lepp et al. 2015_halfwidth`, `study_hours_kw_p`, `reg_adj` (+18) |
| 253 | 95 | …Year & n & Mean & SD & 95\% CI & Mean & SD & 95\%… | design | — |
| 253 | 95 | …ar & n & Mean & SD & 95\% CI & Mean & SD & 95\% CI \\… | design | — |
| 255 | 2 | …Year 2 & 50 & 2.61 & 1.79 & 2.1… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 255 | 50 | …Year 2 & 50 & 2.61 & 1.79 & 2.10 – 3… | summary.json | `n_year_Uni Y2`, `device_study_hours_mean_Other`, `device_ssce_mean_Other` (+4) |
| 255 | 2.61 | …Year 2 & 50 & 2.61 & 1.79 & 2.10 – 3.12 & .… | summary.json | `study_hours_mean_Uni Y2`, `table_by_year.csv[0].study_hours_mean` |
| 255 | 1.79 | …Year 2 & 50 & 2.61 & 1.79 & 2.10 – 3.12 & .469 & .… | summary.json | `study_hours_sd_Uni Y2`, `table_by_year.csv[0].study_hours_sd` |
| 255 | 2.10 | …Year 2 & 50 & 2.61 & 1.79 & 2.10 – 3.12 & .469 & .303 & .… | summary.json | `study_hours_ci_Uni Y2[0]`, `table_by_year.csv[0].study_hours_ci_lo` |
| 255 | 3.12 | …Year 2 & 50 & 2.61 & 1.79 & 2.10 – 3.12 & .469 & .303 & .383 – .… | summary.json | `study_hours_ci_Uni Y2[1]`, `y1in_r_tech_helps`, `table_builds.csv[0].mean_study_h` (+1) |
| 255 | .469 | …Year 2 & 50 & 2.61 & 1.79 & 2.10 – 3.12 & .469 & .303 & .383 – .555 \\… | summary.json | `ssce_mean_Uni Y2`, `table_by_year.csv[0].ssce_mean` |
| 255 | .303 | …2 & 50 & 2.61 & 1.79 & 2.10 – 3.12 & .469 & .303 & .383 – .555 \\… | summary.json | `ssce_sd_Uni Y2`, `table_by_year.csv[0].ssce_sd` |
| 255 | .383 | …& 2.61 & 1.79 & 2.10 – 3.12 & .469 & .303 & .383 – .555 \\… | summary.json | `ssce_ci_Uni Y2[0]`, `table_by_year.csv[0].ssce_ci_lo` |
| 255 | .555 | …& 1.79 & 2.10 – 3.12 & .469 & .303 & .383 – .555 \\… | summary.json | `ssce_ci_Uni Y2[1]`, `table_by_year.csv[0].ssce_ci_hi` |
| 256 | 3 | …Year 3 & 91 & 3.27 & 2.28 & 2.7… | summary.json | `prec_Rosen et al. 2013_ci[0]`, `study_hours_mean_Uni Y2`, `study_hours_ci_Uni Y2[1]` (+38) |
| 256 | 91 | …Year 3 & 91 & 3.27 & 2.28 & 2.79 – 3… | summary.json | `n_year_Uni Y3`, `table_by_year.csv[1].n`, `table_etg_years.csv[0].n_b` (+2) |
| 256 | 3.27 | …Year 3 & 91 & 3.27 & 2.28 & 2.79 – 3.74 & .… | summary.json | `study_hours_mean_Uni Y3`, `table_builds.csv[4].mean_study_h`, `table_by_year.csv[1].study_hours_mean` |
| 256 | 2.28 | …Year 3 & 91 & 3.27 & 2.28 & 2.79 – 3.74 & .541 & .… | summary.json | `study_hours_sd_Uni Y3`, `table_by_year.csv[1].study_hours_sd` |
| 256 | 2.79 | …Year 3 & 91 & 3.27 & 2.28 & 2.79 – 3.74 & .541 & .313 & .… | summary.json | `study_hours_ci_Uni Y3[0]`, `table_by_year.csv[1].study_hours_ci_lo` |
| 256 | 3.74 | …Year 3 & 91 & 3.27 & 2.28 & 2.79 – 3.74 & .541 & .313 & .476 – .… | summary.json | `study_hours_ci_Uni Y3[1]`, `table_by_year.csv[1].study_hours_ci_hi` |
| 256 | .541 | …Year 3 & 91 & 3.27 & 2.28 & 2.79 – 3.74 & .541 & .313 & .476 – .606 \\… | summary.json | `ssce_mean_Uni Y3`, `table_by_year.csv[1].ssce_mean` |
| 256 | .313 | …3 & 91 & 3.27 & 2.28 & 2.79 – 3.74 & .541 & .313 & .476 – .606 \\… | summary.json | `ssce_sd_Uni Y3`, `table_by_year.csv[1].ssce_sd` |
| 256 | .476 | …& 3.27 & 2.28 & 2.79 – 3.74 & .541 & .313 & .476 – .606 \\… | summary.json | `ssce_ci_Uni Y3[0]`, `etg_Uni Y3->Uni Y4+_ci_lo`, `table_by_year.csv[1].ssce_ci_lo` (+1) |
| 256 | .606 | …& 2.28 & 2.79 – 3.74 & .541 & .313 & .476 – .606 \\… | summary.json | `ssce_ci_Uni Y3[1]`, `mod_year_p`, `table_by_year.csv[1].ssce_ci_hi` |
| 257 | 4 | …Year 4+ & 30 & 3.80 & 2.41 & 2.… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 257 | 30 | …Year 4+ & 30 & 3.80 & 2.41 & 2.90 – 4… | summary.json | `n_year_Uni Y4+`, `ssce_sd_Uni Y2`, `exp_r_ci[0]` (+12) |
| 257 | 3.80 | …Year 4+ & 30 & 3.80 & 2.41 & 2.90 – 4.70 & .… | summary.json | `study_hours_mean_Uni Y4+`, `table_by_year.csv[2].study_hours_mean` |
| 257 | 2.41 | …Year 4+ & 30 & 3.80 & 2.41 & 2.90 – 4.70 & .654 & .… | summary.json | `study_hours_sd_Uni Y4+`, `table_by_year.csv[2].study_hours_sd` |
| 257 | 2.90 | …Year 4+ & 30 & 3.80 & 2.41 & 2.90 – 4.70 & .654 & .343 & .… | summary.json | `study_hours_ci_Uni Y4+[0]`, `table_by_year.csv[2].study_hours_ci_lo` |
| 257 | 4.70 | …Year 4+ & 30 & 3.80 & 2.41 & 2.90 – 4.70 & .654 & .343 & .526 – .… | summary.json | `study_hours_ci_Uni Y4+[1]`, `reg_F`, `table_by_year.csv[2].study_hours_ci_hi` |
| 257 | .654 | …Year 4+ & 30 & 3.80 & 2.41 & 2.90 – 4.70 & .654 & .343 & .526 – .782 \\… | summary.json | `ssce_mean_Uni Y4+`, `table_by_year.csv[2].ssce_mean` |
| 257 | .343 | …4+ & 30 & 3.80 & 2.41 & 2.90 – 4.70 & .654 & .343 & .526 – .782 \\… | summary.json | `ssce_sd_Uni Y4+`, `table_by_year.csv[2].ssce_sd` |
| 257 | .526 | …& 3.80 & 2.41 & 2.90 – 4.70 & .654 & .343 & .526 – .782 \\… | summary.json | `ssce_ci_Uni Y4+[0]`, `table_by_year.csv[2].ssce_ci_lo` |
| 257 | .782 | …& 2.41 & 2.90 – 4.70 & .654 & .343 & .526 – .782 \\… | summary.json | `ssce_ci_Uni Y4+[1]`, `table_by_year.csv[2].ssce_ci_hi` |
| 259 | 171 | …All & 171 & 3.17 & 2.20 & & .540 &… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 259 | 3.17 | …All & 171 & 3.17 & 2.20 & & .540 & .320 &… | summary.json | `study_hours_mean_all`, `table_builds.csv[2].mean_study_h` |
| 259 | 2.20 | …All & 171 & 3.17 & 2.20 & & .540 & .320 & \\… | summary.json | `study_hours_sd_all`, `subject_study_hours_sd_STEM` |
| 259 | .540 | …All & 171 & 3.17 & 2.20 & & .540 & .320 & \\… | summary.json | `ssce_mean_all` |
| 259 | .320 | …All & 171 & 3.17 & 2.20 & & .540 & .320 & \\… | summary.json | `ssce_sd_all` |
| 278 | 95 | …Years compared & ETG (h) & 95\% CI & d [95\% bootstr… | design | — |
| 278 | 95 | …Years compared & ETG (h) & 95\% CI & d [95\% bootstrap CI] & p (r… | design | — |
| 280 | +0.66 | …Y2 Y3 & +0.66 & [-0.03, 1.35] & 0.… | summary.json | `etg_Uni Y2->Uni Y3_etg`, `etg_Uni Y3->Uni Y4+_d_hi`, `gender_study_hours_bound` (+4) |
| 280 | -0.03 | …Y2 Y3 & +0.66 & [-0.03, 1.35] & 0.31 [-0.01… | summary.json | `etg_Uni Y2->Uni Y3_ci_lo`, `r_ci_focus[0]`, `y1in_r_tech_helps` (+3) |
| 280 | 1.35 | …Y2 Y3 & +0.66 & [-0.03, 1.35] & 0.31 [-0.01, 0.64… | summary.json | `etg_Uni Y2->Uni Y3_ci_hi`, `mean_n_nonacademic`, `table_etg_years.csv[0].ci_hi` |
| 280 | 0.31 | …Y2 Y3 & +0.66 & [-0.03, 1.35] & 0.31 [-0.01, 0.64] & .061… | summary.json | `ssce_sd_Uni Y3`, `etg_Uni Y2->Uni Y3_cohen_d`, `table_by_year.csv[1].ssce_sd` (+1) |
| 280 | -0.01 | …Y3 & +0.66 & [-0.03, 1.35] & 0.31 [-0.01, 0.64] & .061 & .121 &… | summary.json | `prec_this study_ci[0]`, `etg_Uni Y2->Uni Y3_d_lo`, `y1in_exp_ci[1]` (+3) |
| 280 | 0.64 | …+0.66 & [-0.03, 1.35] & 0.31 [-0.01, 0.64] & .061 & .121 & .121 \… | summary.json | `etg_Uni Y2->Uni Y3_d_hi`, `y1in_exp_ci[1]`, `device_ssce_mean_Tablet` (+1) |
| 280 | .061 | …& [-0.03, 1.35] & 0.31 [-0.01, 0.64] & .061 & .121 & .121 \\… | summary.json | `etg_Uni Y2->Uni Y3_p_raw`, `table_etg_years.csv[0].p_raw` |
| 280 | .121 | …03, 1.35] & 0.31 [-0.01, 0.64] & .061 & .121 & .121 \\… | summary.json | `prec_Lepp et al. 2015_min_r_80`, `etg_Uni Y2->Uni Y3_p_holm`, `etg_Uni Y2->Uni Y3_p_bh` (+3) |
| 280 | .121 | …5] & 0.31 [-0.01, 0.64] & .061 & .121 & .121 \\… | summary.json | `prec_Lepp et al. 2015_min_r_80`, `etg_Uni Y2->Uni Y3_p_holm`, `etg_Uni Y2->Uni Y3_p_bh` (+3) |
| 281 | +0.53 | …Y3 Y4+ & +0.53 & [-0.48, 1.54] & 0.… | summary.json | `ssce_ci_Uni Y4+[0]`, `etg_Uni Y3->Uni Y4+_etg`, `subject_ssce_mean_Other` (+3) |
| 281 | -0.48 | …Y3 Y4+ & +0.53 & [-0.48, 1.54] & 0.23 [-0.18… | summary.json | `etg_Uni Y3->Uni Y4+_ci_lo`, `table_etg_years.csv[1].ci_lo` |
| 281 | 1.54 | …Y3 Y4+ & +0.53 & [-0.48, 1.54] & 0.23 [-0.18, 0.66… | summary.json | `etg_Uni Y3->Uni Y4+_ci_hi`, `table_etg_years.csv[1].ci_hi` |
| 281 | 0.23 | …Y3 Y4+ & +0.53 & [-0.48, 1.54] & 0.23 [-0.18, 0.66] & .294… | summary.json | `prec_Lepp et al. 2015_ci[1]`, `etg_Uni Y3->Uni Y4+_cohen_d`, `r_workload_n_nonacademic` (+5) |
| 281 | -0.18 | …Y4+ & +0.53 & [-0.48, 1.54] & 0.23 [-0.18, 0.66] & .294 & .294 &… | summary.json | `etg_Uni Y3->Uni Y4+_d_lo`, `table_etg_years.csv[1].d_lo` |
| 281 | 0.66 | …+0.53 & [-0.48, 1.54] & 0.23 [-0.18, 0.66] & .294 & .294 & .294 \… | summary.json | `etg_Uni Y2->Uni Y3_etg`, `etg_Uni Y3->Uni Y4+_d_hi`, `gender_study_hours_bound` (+4) |
| 281 | .294 | …& [-0.48, 1.54] & 0.23 [-0.18, 0.66] & .294 & .294 & .294 \\… | summary.json | `prec_this study_width`, `etg_Uni Y3->Uni Y4+_p_raw`, `etg_Uni Y3->Uni Y4+_p_holm` (+6) |
| 281 | .294 | …48, 1.54] & 0.23 [-0.18, 0.66] & .294 & .294 & .294 \\… | summary.json | `prec_this study_width`, `etg_Uni Y3->Uni Y4+_p_raw`, `etg_Uni Y3->Uni Y4+_p_holm` (+6) |
| 281 | .294 | …4] & 0.23 [-0.18, 0.66] & .294 & .294 & .294 \\… | summary.json | `prec_this study_width`, `etg_Uni Y3->Uni Y4+_p_raw`, `etg_Uni Y3->Uni Y4+_p_holm` (+6) |
| 287 | -.15 | …eported a smaller academic share of it (r = -.15, p = .045, 95\% CI [… | summary.json | `exp_r`, `med_c_total`, `grid_r_min` (+10) |
| 287 | .045 | …aller academic share of it (r = -.15, p = .045, 95\% CI [-.30, -.004]… | summary.json | `prec_Junco & Cotten 2012_halfwidth`, `ssce_kw_p`, `exp_p` (+7) |
| 287 | 95 | …cademic share of it (r = -.15, p = .045, 95\% CI [-.30, -.004];… | design | — |
| 287 | -.30 | …are of it (r = -.15, p = .045, 95\% CI [-.30, -.004]; ). The slope… | summary.json | `exp_r_ci[0]`, `table_builds.csv[0].r_ci_lo`, `table_builds.csv[0].r_ci_hi` (+2) |
| 287 | -.004 | …it (r = -.15, p = .045, 95\% CI [-.30, -.004]; ). The slope was -… | summary.json | `exp_r_ci[1]`, `table_builds.csv[2].r_ci_hi`, `table_builds.csv[7].r_ci_lo` |
| 287 | -0.022 | …95\% CI [-.30, -.004]; ). The slope was -0.022 per hour, but its 95\%… | summary.json | `exp_slope` |
| 287 | 95 | …). The slope was -0.022 per hour, but its 95\% bootstrap interval inc… | design | — |
| 287 | -0.044 | …its 95\% bootstrap interval included zero ([-0.044, 0.001]), so the eviden… | summary.json | `exp_slope_ci[0]` |
| 287 | 0.001 | …bootstrap interval included zero ([-0.044, 0.001]), so the evidence for… | summary.json | `exp_slope_ci[1]`, `exp_r2_gain`, `exp_p_n_purposes` (+5) |
| 287 | 2 | …on is small: screen time accounted for about 2\% of the variance in SSC… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 287 | 2 | …about 2\% of the variance in SSCE (linear R^2 = .024). Adding a squar… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 287 | .024 | …t 2\% of the variance in SSCE (linear R^2 = .024). Adding a squared term… | summary.json | `exp_r2_lin`, `exp_r2_quad` |
| 287 | 2 | …^2 = .024). Adding a squared term raised R^2 by less than .001 (p =… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 287 | .001 | …ing a squared term raised R^2 by less than .001 (p = .738), so there i… | summary.json | `exp_slope_ci[1]`, `exp_r2_gain`, `exp_p_n_purposes` (+5) |
| 287 | .738 | …ed term raised R^2 by less than .001 (p = .738), so there is no eviden… | summary.json | `exp_p_quad` |
| 287 | .70 | …no evidence of curvature. The mean SSCE was .70 in the lowest band (unde… | output table | `table_ssce_by_band.csv[0].mean` |
| 287 | 2 | …mean SSCE was .70 in the lowest band (under 2 h, n = 9), .59 at 2 –… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 287 | 9 | …was .70 in the lowest band (under 2 h, n = 9), .59 at 2 – 4 h, .55 a… | summary.json | `prec_Junco & Cotten 2012_width`, `prec_Bjerre-Nielsen et al. 2020_halfwidth`, `prec_Giunchiglia et al. 2018_ci[0]` (+19) |
| 287 | .59 | ….70 in the lowest band (under 2 h, n = 9), .59 at 2 – 4 h, .55 at 4 – 6… | summary.json | `uniqueR2_control`, `table_selfreg_model.csv[1].unique_r2`, `table_ssce_by_band.csv[1].mean` |
| 287 | 2 | …the lowest band (under 2 h, n = 9), .59 at 2 – 4 h, .55 at 4 – 6 h, .… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 287 | 4 | …lowest band (under 2 h, n = 9), .59 at 2 – 4 h, .55 at 4 – 6 h, .53 a… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 287 | .55 | …t band (under 2 h, n = 9), .59 at 2 – 4 h, .55 at 4 – 6 h, .53 at 6 – 8… | summary.json | `ssce_ci_Uni Y2[1]`, `device_ssce_mean_Laptop/Desktop`, `table_by_year.csv[0].ssce_ci_hi` (+1) |
| 287 | 4 | …(under 2 h, n = 9), .59 at 2 – 4 h, .55 at 4 – 6 h, .53 at 6 – 8 h an… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 287 | 6 | …er 2 h, n = 9), .59 at 2 – 4 h, .55 at 4 – 6 h, .53 at 6 – 8 h and .4… | summary.json | `full_out_of_range`, `n_subject_Other`, `prec_Bjerre-Nielsen et al. 2020_ci[0]` (+29) |
| 287 | .53 | …h, n = 9), .59 at 2 – 4 h, .55 at 4 – 6 h, .53 at 6 – 8 h and .47 above… | summary.json | `ssce_ci_Uni Y4+[0]`, `etg_Uni Y3->Uni Y4+_etg`, `subject_ssce_mean_Other` (+3) |
| 287 | 6 | …9), .59 at 2 – 4 h, .55 at 4 – 6 h, .53 at 6 – 8 h and .47 above 8 h,… | summary.json | `full_out_of_range`, `n_subject_Other`, `prec_Bjerre-Nielsen et al. 2020_ci[0]` (+29) |
| 287 | 8 | …, .59 at 2 – 4 h, .55 at 4 – 6 h, .53 at 6 – 8 h and .47 above 8 h, a d… | summary.json | `prec_Lepp et al. 2015_halfwidth`, `study_hours_kw_p`, `reg_adj` (+18) |
| 287 | .47 | …2 – 4 h, .55 at 4 – 6 h, .53 at 6 – 8 h and .47 above 8 h, a decline acr… | summary.json | `prec_Giunchiglia et al. 2018_width`, `ssce_mean_Uni Y2`, `gender_study_hours_p` (+5) |
| 287 | 8 | ….55 at 4 – 6 h, .53 at 6 – 8 h and .47 above 8 h, a decline across the… | summary.json | `prec_Lepp et al. 2015_halfwidth`, `study_hours_kw_p`, `reg_adj` (+18) |
| 287 | 9 | …rests on the small lowest band: without its 9 students the correlation… | summary.json | `prec_Junco & Cotten 2012_width`, `prec_Bjerre-Nielsen et al. 2020_halfwidth`, `prec_Giunchiglia et al. 2018_ci[0]` (+19) |
| 287 | -.11 | …elation was weaker and not significant (r = -.11, p = .160, n = 162)… | summary.json | `exp_r_without_lowest_band` |
| 287 | .160 | …weaker and not significant (r = -.11, p = .160, n = 162). H1 is ther… | summary.json | `exp_p_without_lowest_band`, `split_screen_mid_median_r[0]`, `table_splithalf.csv[0].median_r_half1` |
| 287 | 162 | …ot significant (r = -.11, p = .160, n = 162). H1 is therefore only… | summary.json | `exp_n_without_lowest_band` |
| 304 | +.25 | …kload reported a larger academic share (r = +.25, p = .001), and this… | summary.json | `r_workload`, `split_workload_median_r[0]`, `split_workload_median_r[1]` (+7) |
| 304 | .001 | …ed a larger academic share (r = +.25, p = .001), and this remained sig… | summary.json | `exp_slope_ci[1]`, `exp_r2_gain`, `exp_p_n_purposes` (+5) |
| 304 | .006 | …ests under both procedures (Holm and BH p = .006). Perceived control (r… | summary.json | `r_workload_n_academic`, `p_holm_workload`, `p_bh_workload` (+6) |
| 304 | +.13 | …and BH p = .006). Perceived control (r = +.13, p = .096) and task-s… | summary.json | `prec_Bjerre-Nielsen et al. 2020_min_r_80`, `exp_r_n_academic`, `r_control` (+11) |
| 304 | .096 | ….006). Perceived control (r = +.13, p = .096) and task-switching (r… | summary.json | `p_control`, `gender_ssce_bound`, `table_convergent.csv[3].p` (+1) |
| 304 | -.10 | …+.13, p = .096) and task-switching (r = -.10, p = .183) were in th… | summary.json | `r_switch`, `split_switch_median_r[0]`, `split_switch_median_r[1]` (+5) |
| 304 | .183 | ….096) and task-switching (r = -.10, p = .183) were in the expected d… | summary.json | `p_switch`, `table_convergent.csv[0].p` |
| 304 | +.12 | …ficant, and neither were ease of focus (r = +.12, p = .122) or perceiv… | summary.json | `prec_Lepp et al. 2015_min_r_80`, `prec_Rosen et al. 2013_halfwidth`, `etg_Uni Y2->Uni Y3_p_holm` (+12) |
| 304 | .122 | …neither were ease of focus (r = +.12, p = .122) or perceived helpfulne… | summary.json | `p_workload`, `p_focus`, `table_convergent.csv[1].p` (+1) |
| 304 | +.01 | …or perceived helpfulness of technology (r = +.01, p = .851). H2 is the… | summary.json | `r_workload_n_academic`, `r_tech_helps`, `p_holm_workload` (+12) |
| 304 | .851 | …helpfulness of technology (r = +.01, p = .851). H2 is therefore suppo… | summary.json | `p_tech_helps`, `p_holm_tech helpfulness`, `p_bh_tech helpfulness` (+3) |
| 313 | 95 | …Item & r with SSCE & 95\% CI & p & p (Holm)… | design | — |
| 315 | +.245 | …Academic workload & +.245 & [.099, .381] & .001… | summary.json | `r_workload`, `table_convergent.csv[1].r` |
| 315 | .099 | …Academic workload & +.245 & [.099, .381] & .001 & .006 &… | summary.json | `r_ci_workload[0]`, `table_convergent.csv[1].ci_lo` |
| 315 | .381 | …Academic workload & +.245 & [.099, .381] & .001 & .006 & .006 &… | summary.json | `prec_Lukram et al. 2026_width`, `r_ci_workload[1]`, `table_convergent.csv[1].ci_hi` (+1) |
| 315 | .001 | …ademic workload & +.245 & [.099, .381] & .001 & .006 & .006 & 171 \\… | summary.json | `exp_slope_ci[1]`, `exp_r2_gain`, `exp_p_n_purposes` (+5) |
| 315 | .006 | …workload & +.245 & [.099, .381] & .001 & .006 & .006 & 171 \\… | summary.json | `r_workload_n_academic`, `p_holm_workload`, `p_bh_workload` (+6) |
| 315 | .006 | …d & +.245 & [.099, .381] & .001 & .006 & .006 & 171 \\… | summary.json | `r_workload_n_academic`, `p_holm_workload`, `p_bh_workload` (+6) |
| 315 | 171 | …245 & [.099, .381] & .001 & .006 & .006 & 171 \\… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 316 | +.128 | …Perceived control & +.128 & [-.023, .272] & .09… | summary.json | `r_control`, `split_control_median_r[0]`, `split_control_median_r[1]` (+3) |
| 316 | -.023 | …Perceived control & +.128 & [-.023, .272] & .096 & .386 &… | summary.json | `r_ci_control[0]`, `table_convergent.csv[3].ci_lo` |
| 316 | .272 | …Perceived control & +.128 & [-.023, .272] & .096 & .386 & .203 &… | summary.json | `r_ci_control[1]`, `table_convergent.csv[3].ci_hi` |
| 316 | .096 | …ceived control & +.128 & [-.023, .272] & .096 & .386 & .203 & 171 \\… | summary.json | `p_control`, `gender_ssce_bound`, `table_convergent.csv[3].p` (+1) |
| 316 | .386 | …control & +.128 & [-.023, .272] & .096 & .386 & .203 & 171 \\… | summary.json | `p_holm_task-switching`, `p_holm_focus ease`, `p_holm_perceived control` (+3) |
| 316 | .203 | …& +.128 & [-.023, .272] & .096 & .386 & .203 & 171 \\… | summary.json | `p_bh_focus ease`, `p_bh_perceived control`, `table_convergent.csv[2].p_bh` (+1) |
| 316 | 171 | …28 & [-.023, .272] & .096 & .386 & .203 & 171 \\… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 317 | +.120 | …Ease of focus & +.120 & [-.032, .266] & .12… | summary.json | `r_focus`, `y1in_p_focus`, `table_convergent.csv[2].r` |
| 317 | -.032 | …Ease of focus & +.120 & [-.032, .266] & .122 & .386 &… | summary.json | `r_ci_focus[0]`, `table_convergent.csv[2].ci_lo` |
| 317 | .266 | …Ease of focus & +.120 & [-.032, .266] & .122 & .386 & .203 &… | summary.json | `prec_Rosen et al. 2013_ci[1]`, `r_ci_focus[1]`, `cluster_p_screen_mid` (+3) |
| 317 | .122 | …Ease of focus & +.120 & [-.032, .266] & .122 & .386 & .203 & 169 \\… | summary.json | `p_workload`, `p_focus`, `table_convergent.csv[1].p` (+1) |
| 317 | .386 | …f focus & +.120 & [-.032, .266] & .122 & .386 & .203 & 169 \\… | summary.json | `p_holm_task-switching`, `p_holm_focus ease`, `p_holm_perceived control` (+3) |
| 317 | .203 | …& +.120 & [-.032, .266] & .122 & .386 & .203 & 169 \\… | summary.json | `p_bh_focus ease`, `p_bh_perceived control`, `table_convergent.csv[2].p_bh` (+1) |
| 317 | 169 | …20 & [-.032, .266] & .122 & .386 & .203 & 169 \\… | summary.json | `n_focus`, `reg_n`, `hier_n` (+2) |
| 318 | -.102 | …Task-switching & -.102 & [-.248, .049] & .18… | summary.json | `r_switch`, `table_convergent.csv[0].r` |
| 318 | -.248 | …Task-switching & -.102 & [-.248, .049] & .183 & .386 &… | summary.json | `r_ci_switch[0]`, `table_convergent.csv[0].ci_lo` |
| 318 | .049 | …Task-switching & -.102 & [-.248, .049] & .183 & .386 & .229 &… | summary.json | `r_ci_switch[1]`, `med_a_p`, `grid_11.0_selected_p` (+2) |
| 318 | .183 | …Task-switching & -.102 & [-.248, .049] & .183 & .386 & .229 & 171 \\… | summary.json | `p_switch`, `table_convergent.csv[0].p` |
| 318 | .386 | …itching & -.102 & [-.248, .049] & .183 & .386 & .229 & 171 \\… | summary.json | `p_holm_task-switching`, `p_holm_focus ease`, `p_holm_perceived control` (+3) |
| 318 | .229 | …& -.102 & [-.248, .049] & .183 & .386 & .229 & 171 \\… | summary.json | `p_bh_task-switching`, `table_convergent.csv[0].p_bh` |
| 318 | 171 | …02 & [-.248, .049] & .183 & .386 & .229 & 171 \\… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 319 | +.014 | …Technology helpfulness & +.014 & [-.136, .164] & .85… | summary.json | `r_tech_helps`, `table_convergent.csv[4].r` |
| 319 | -.136 | …Technology helpfulness & +.014 & [-.136, .164] & .851 & .851 &… | summary.json | `r_ci_tech_helps[0]`, `beta_switch`, `med_c_direct` (+2) |
| 319 | .164 | …Technology helpfulness & +.014 & [-.136, .164] & .851 & .851 & .851 &… | summary.json | `r_ci_tech_helps[1]`, `table_convergent.csv[4].ci_hi` |
| 319 | .851 | …gy helpfulness & +.014 & [-.136, .164] & .851 & .851 & .851 & 171 \\… | summary.json | `p_tech_helps`, `p_holm_tech helpfulness`, `p_bh_tech helpfulness` (+3) |
| 319 | .851 | …fulness & +.014 & [-.136, .164] & .851 & .851 & .851 & 171 \\… | summary.json | `p_tech_helps`, `p_holm_tech helpfulness`, `p_bh_tech helpfulness` (+3) |
| 319 | .851 | …& +.014 & [-.136, .164] & .851 & .851 & .851 & 171 \\… | summary.json | `p_tech_helps`, `p_holm_tech helpfulness`, `p_bh_tech helpfulness` (+3) |
| 319 | 171 | …14 & [-.136, .164] & .851 & .851 & .851 & 171 \\… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 324 | 169 | …, control, task-switching and workload (n = 169) was significant overal… | summary.json | `n_focus`, `reg_n`, `hier_n` (+2) |
| 324 | 4 | …load (n = 169) was significant overall (F(4, 164) = 4.70, p = .001… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 324 | 164 | …d (n = 169) was significant overall (F(4, 164) = 4.70, p = .001, R… | summary.json | `reg_dof`, `mod_gender_n` |
| 324 | 4.70 | …169) was significant overall (F(4, 164) = 4.70, p = .001, R^2 = .10… | summary.json | `study_hours_ci_Uni Y4+[1]`, `reg_F`, `table_by_year.csv[2].study_hours_ci_hi` |
| 324 | .001 | …ignificant overall (F(4, 164) = 4.70, p = .001, R^2 = .10, adjusted… | summary.json | `exp_slope_ci[1]`, `exp_r2_gain`, `exp_p_n_purposes` (+5) |
| 324 | 2 | …overall (F(4, 164) = 4.70, p = .001, R^2 = .10, adjusted R^2 =… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 324 | .10 | …rall (F(4, 164) = 4.70, p = .001, R^2 = .10, adjusted R^2 = .08;… | summary.json | `r_switch`, `r_ci_workload[0]`, `p_control` (+18) |
| 324 | 2 | …4.70, p = .001, R^2 = .10, adjusted R^2 = .08; ; ). Against… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 324 | .08 | …0, p = .001, R^2 = .10, adjusted R^2 = .08; ; ). Against Cohen… | summary.json | `prec_Lepp et al. 2015_halfwidth`, `study_hours_kw_p`, `reg_adj` (+12) |
| 324 | 2 | …; ). Against Cohen's benchmarks, where R^2 values near .02, .13 an… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 324 | .02 | …Cohen's benchmarks, where R^2 values near .02, .13 and .26 correspond… | summary.json | `exp_slope`, `exp_r2_lin`, `exp_r2_quad` (+7) |
| 324 | .13 | …n's benchmarks, where R^2 values near .02, .13 and .26 correspond to sm… | summary.json | `prec_Bjerre-Nielsen et al. 2020_min_r_80`, `exp_r_n_academic`, `r_control` (+11) |
| 324 | .26 | …hmarks, where R^2 values near .02, .13 and .26 correspond to small, med… | summary.json | `exp_r_n_purposes`, `med_a`, `cluster_r_workload` (+3) |
| 324 | +.27 | …oad was the only significant predictor ( = +.27, p < .001); task-swit… | summary.json | `prec_Rosen et al. 2013_ci[1]`, `r_ci_focus[1]`, `r_ci_control[1]` (+9) |
| 324 | .001 | …only significant predictor ( = +.27, p < .001); task-switching ( =… | summary.json | `exp_slope_ci[1]`, `exp_r2_gain`, `exp_p_n_purposes` (+5) |
| 324 | -.14 | …= +.27, p < .001); task-switching ( = -.14, p = .088), focus (… | summary.json | `r_ci_tech_helps[0]`, `beta_switch`, `med_c_direct` (+5) |
| 324 | .088 | …p < .001); task-switching ( = -.14, p = .088), focus ( = +.10, p… | summary.json | `prec_Bjerre-Nielsen et al. 2020_halfwidth`, `pbeta_switch`, `table_selfreg_model.csv[2].p` |
| 324 | +.10 | …tching ( = -.14, p = .088), focus ( = +.10, p = .197) and contro… | summary.json | `r_ci_workload[0]`, `p_control`, `reg_r2` (+10) |
| 324 | .197 | …-.14, p = .088), focus ( = +.10, p = .197) and control ( = +.08… | summary.json | `pbeta_focus`, `table_selfreg_model.csv[0].p` |
| 324 | +.08 | …s ( = +.10, p = .197) and control ( = +.08, p = .299) were not.… | summary.json | `prec_Lepp et al. 2015_halfwidth`, `study_hours_kw_p`, `reg_adj` (+12) |
| 324 | .299 | …, p = .197) and control ( = +.08, p = .299) were not. The unique… | summary.json | `pbeta_control`, `table_selfreg_model.csv[1].p` |
| 324 | 2 | …= +.08, p = .299) were not. The unique R^2 of each predictor tells… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 324 | .070 | …ach predictor tells the same story: workload .070, task-switching .016, fo… | summary.json | `uniqueR2_workload`, `hier_b1_R2`, `table_selfreg_model.csv[3].unique_r2` |
| 324 | .016 | …he same story: workload .070, task-switching .016, focus .009 and control… | summary.json | `uniqueR2_switch`, `table_selfreg_model.csv[2].unique_r2` |
| 324 | .009 | …y: workload .070, task-switching .016, focus .009 and control .006. The wo… | summary.json | `uniqueR2_focus`, `cluster_reg_p`, `table_selfreg_model.csv[0].unique_r2` |
| 324 | .006 | …task-switching .016, focus .009 and control .006. The workload associatio… | summary.json | `r_workload_n_academic`, `p_holm_workload`, `p_bh_workload` (+6) |
| 324 | +.01 | …rkload and number of academic purposes: r = +.01, p = .940); instead,… | summary.json | `r_workload_n_academic`, `r_tech_helps`, `p_holm_workload` (+12) |
| 324 | .940 | …umber of academic purposes: r = +.01, p = .940); instead, they listed… | summary.json | `p_workload_n_academic` |
| 324 | -.23 | …hey listed fewer non-academic purposes (r = -.23, p = .002). Because S… | summary.json | `r_workload_n_nonacademic` |
| 324 | .002 | …ewer non-academic purposes (r = -.23, p = .002). Because SSCE is a sha… | summary.json | `p_workload_n_nonacademic`, `cluster_p_workload`, `y1in_p_holm_workload` (+1) |
| 333 | 2 | …Predictor & Std. & SE & p & Unique R^2 \\… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 335 | +.271 | …Academic workload & +.271 & .076 & < .001 & .07… | summary.json | `beta_workload`, `cluster_beta_workload`, `table_selfreg_model.csv[3].std_beta` |
| 335 | .076 | …Academic workload & +.271 & .076 & < .001 & .070 \\… | summary.json | `se_workload`, `table_selfreg_model.csv[3].se` |
| 335 | .001 | …Academic workload & +.271 & .076 & < .001 & .070 \\… | summary.json | `exp_slope_ci[1]`, `exp_r2_gain`, `exp_p_n_purposes` (+5) |
| 335 | .070 | …demic workload & +.271 & .076 & < .001 & .070 \\… | summary.json | `uniqueR2_workload`, `hier_b1_R2`, `table_selfreg_model.csv[3].unique_r2` |
| 336 | -.136 | …Task-switching & -.136 & .079 & .088 & .016 \\… | summary.json | `r_ci_tech_helps[0]`, `beta_switch`, `med_c_direct` (+2) |
| 336 | .079 | …Task-switching & -.136 & .079 & .088 & .016 \\… | summary.json | `se_switch`, `table_selfreg_model.csv[2].se`, `table_ssce_by_band.csv[1].se` |
| 336 | .088 | …Task-switching & -.136 & .079 & .088 & .016 \\… | summary.json | `prec_Bjerre-Nielsen et al. 2020_halfwidth`, `pbeta_switch`, `table_selfreg_model.csv[2].p` |
| 336 | .016 | …Task-switching & -.136 & .079 & .088 & .016 \\… | summary.json | `uniqueR2_switch`, `table_selfreg_model.csv[2].unique_r2` |
| 337 | +.101 | …Ease of focus & +.101 & .078 & .197 & .009 \\… | summary.json | `beta_focus`, `table_selfreg_model.csv[0].std_beta` |
| 337 | .078 | …Ease of focus & +.101 & .078 & .197 & .009 \\… | summary.json | `se_focus`, `table_selfreg_model.csv[0].se` |
| 337 | .197 | …Ease of focus & +.101 & .078 & .197 & .009 \\… | summary.json | `pbeta_focus`, `table_selfreg_model.csv[0].p` |
| 337 | .009 | …Ease of focus & +.101 & .078 & .197 & .009 \\… | summary.json | `uniqueR2_focus`, `cluster_reg_p`, `table_selfreg_model.csv[0].unique_r2` |
| 338 | +.085 | …Perceived control & +.085 & .081 & .299 & .006 \\… | summary.json | `beta_control`, `table_selfreg_model.csv[1].std_beta` |
| 338 | .081 | …Perceived control & +.085 & .081 & .299 & .006 \\… | summary.json | `reg_adj`, `se_control`, `table_selfreg_model.csv[1].se` |
| 338 | .299 | …Perceived control & +.085 & .081 & .299 & .006 \\… | summary.json | `pbeta_control`, `table_selfreg_model.csv[1].p` |
| 338 | .006 | …Perceived control & +.085 & .081 & .299 & .006 \\… | summary.json | `r_workload_n_academic`, `p_holm_workload`, `p_bh_workload` (+6) |
| 351 | 2 | …r, subject and university year) explained R^2 = .070 of the variance… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 351 | .070 | …ubject and university year) explained R^2 = .070 of the variance in SSCE… | summary.json | `uniqueR2_workload`, `hier_b1_R2`, `table_selfreg_model.csv[3].unique_r2` |
| 351 | 7 | …iance in SSCE, which was not significant (F(7, 161) = 1.73, p = .106… | summary.json | `full_uni_school_institution`, `n_gender_Prefer not to say`, `prec_Junco & Cotten 2012_min_r_80` (+19) |
| 351 | 161 | …ce in SSCE, which was not significant (F(7, 161) = 1.73, p = .106); a… | summary.json | `hier_b1_df[1]` |
| 351 | 1.73 | …SCE, which was not significant (F(7, 161) = 1.73, p = .106); adding th… | summary.json | `hier_b1_F`, `grid_mean_min`, `table_builds.csv[1].mean_study_h` |
| 351 | .106 | …as not significant (F(7, 161) = 1.73, p = .106); adding the four self-… | summary.json | `hier_b1_p`, `device_year_p` |
| 351 | 2 | …self-regulation indicators raised this to R^2 = .159, a significant i… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 351 | .159 | …-regulation indicators raised this to R^2 = .159, a significant incremen… | summary.json | `hier_b2_R2` |
| 351 | 2 | …R^2 = .159, a significant increment ( R^2 = .090; F-change(4,… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 351 | .090 | …2 = .159, a significant increment ( R^2 = .090; F-change(4, 157) =… | summary.json | `hier_dR2` |
| 351 | 4 | …icant increment ( R^2 = .090; F-change(4, 157) = 4.18, p = .003… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 351 | 157 | …nt increment ( R^2 = .090; F-change(4, 157) = 4.18, p = .003; n… | summary.json | `hier_df2` |
| 351 | 4.18 | …ement ( R^2 = .090; F-change(4, 157) = 4.18, p = .003; n = 169)… | summary.json | `hier_Fch` |
| 351 | .003 | …2 = .090; F-change(4, 157) = 4.18, p = .003; n = 169). Self-regul… | summary.json | `hier_pFch`, `cluster_p_screen_mid`, `table_builds.csv[0].r_ci_hi` (+2) |
| 351 | 169 | …F-change(4, 157) = 4.18, p = .003; n = 169). Self-regulation, chie… | summary.json | `n_focus`, `reg_n`, `hier_n` (+2) |
| 353 | 171 | …The mediation analysis (n = 171) supported H3a but not… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 353 | .26 | …as associated with more task-switching (a = .26, p < .001). Controlli… | summary.json | `exp_r_n_purposes`, `med_a`, `cluster_r_workload` (+3) |
| 353 | .001 | …ed with more task-switching (a = .26, p < .001). Controlling for expos… | summary.json | `exp_slope_ci[1]`, `exp_r2_gain`, `exp_p_n_purposes` (+5) |
| 353 | -.07 | …not significantly associated with SSCE (b = -.07, p = .402), and the i… | summary.json | `med_b` |
| 353 | .402 | …antly associated with SSCE (b = -.07, p = .402), and the indirect effe… | summary.json | `med_b_p` |
| 353 | -.017 | …rect effect was not significant (indirect = -.017, 95\% bootstrap CI [-.… | summary.json | `med_indirect` |
| 353 | 95 | …ect was not significant (indirect = -.017, 95\% bootstrap CI [-.064,… | design | — |
| 353 | -.064 | …ant (indirect = -.017, 95\% bootstrap CI [-.064, .025], which includes… | summary.json | `med_ci_lo` |
| 353 | .025 | …direct = -.017, 95\% bootstrap CI [-.064, .025], which includes zero).… | summary.json | `med_ci_hi`, `table_builds.csv[1].r_ci_lo` |
| 353 | -.15 | …l association between exposure and SSCE was -.15 (p = .045) and the di… | summary.json | `exp_r`, `med_c_total`, `grid_r_min` (+10) |
| 353 | .045 | …n between exposure and SSCE was -.15 (p = .045) and the direct associa… | summary.json | `prec_Junco & Cotten 2012_halfwidth`, `ssce_kw_p`, `exp_p` (+7) |
| 353 | -.14 | …ion after accounting for task-switching was -.14 (p = .086). We theref… | summary.json | `r_ci_tech_helps[0]`, `beta_switch`, `med_c_direct` (+5) |
| 353 | .086 | …counting for task-switching was -.14 (p = .086). We therefore find no… | summary.json | `exp_p_n_academic`, `med_c_direct_p`, `grid_9.0_all_p` (+1) |
| 355 | 169 | …Harman's single-factor test (n = 169) returned a first unrot… | summary.json | `n_focus`, `reg_n`, `hier_n` (+2) |
| 355 | 30.4 | …returned a first unrotated factor explaining 30.4\% of variance, below 50\… | summary.json | `harman_first_pct` |
| 355 | 50 | …factor explaining 30.4\% of variance, below 50\%, so shared method vari… | summary.json | `n_year_Uni Y2`, `device_study_hours_mean_Other`, `device_ssce_mean_Other` (+4) |
| 358 | 0.72 | …antly between male and female students (t = 0.72, p = .472, d = 0.11… | summary.json | `gender_study_hours_t`, `table_gender.csv[0].welch_t` |
| 358 | .472 | …n male and female students (t = 0.72, p = .472, d = 0.11), but equiv… | summary.json | `gender_study_hours_p`, `table_gender.csv[0].p` |
| 358 | 0.11 | …emale students (t = 0.72, p = .472, d = 0.11), but equivalence withi… | summary.json | `prec_Junco & Cotten 2012_ci[0]`, `exp_r_without_lowest_band`, `hier_b1_p` (+8) |
| 358 | 0.3 | …472, d = 0.11), but equivalence within 0.3 SD ( 0.66 h) could n… | summary.json | `prec_this study_ci[1]`, `prec_this study_width`, `prec_Rosen et al. 2013_ci[1]` (+66) |
| 358 | 0.66 | ….11), but equivalence within 0.3 SD ( 0.66 h) could not be shown (… | summary.json | `etg_Uni Y2->Uni Y3_etg`, `etg_Uni Y3->Uni Y4+_d_hi`, `gender_study_hours_bound` (+4) |
| 358 | .115 | ….3 SD ( 0.66 h) could not be shown (p = .115). SSCE also did not dif… | summary.json | `gender_study_hours_tost_p`, `table_gender.csv[0].tost_p` |
| 358 | 0.86 | …did not differ significantly by gender (t = 0.86, p = .389, d = 0.14… | summary.json | `gender_ssce_t`, `table_gender.csv[1].welch_t` |
| 358 | .389 | …er significantly by gender (t = 0.86, p = .389, d = 0.14), and equiv… | summary.json | `gender_ssce_p`, `table_gender.csv[1].p` |
| 358 | 0.14 | …ntly by gender (t = 0.86, p = .389, d = 0.14), and equivalence withi… | summary.json | `r_ci_tech_helps[0]`, `beta_switch`, `med_c_direct` (+13) |
| 358 | 0.3 | …389, d = 0.14), and equivalence within 0.3 SD ( 0.10) could not… | summary.json | `prec_this study_ci[1]`, `prec_this study_width`, `prec_Rosen et al. 2013_ci[1]` (+66) |
| 358 | 0.10 | ….14), and equivalence within 0.3 SD ( 0.10) could not be shown eit… | summary.json | `r_switch`, `r_ci_workload[0]`, `p_control` (+18) |
| 358 | .138 | …D ( 0.10) could not be shown either (p = .138), so small gender diffe… | summary.json | `gender_ssce_tost_p`, `table_gender.csv[1].tost_p` |
| 358 | 3 | …ut. Study time differed by subject (ANOVA F(3, 167) = 3.68, p = .013… | summary.json | `prec_Rosen et al. 2013_ci[0]`, `study_hours_mean_Uni Y2`, `study_hours_ci_Uni Y2[1]` (+38) |
| 358 | 167 | …Study time differed by subject (ANOVA F(3, 167) = 3.68, p = .013; Kr… | summary.json | `subject_study_hours_df[1]`, `subject_study_hours_sd_Other`, `subject_ssce_df[1]` |
| 358 | 3.68 | …time differed by subject (ANOVA F(3, 167) = 3.68, p = .013; Kruskal –… | summary.json | `subject_study_hours_F` |
| 358 | .013 | …d by subject (ANOVA F(3, 167) = 3.68, p = .013; Kruskal – Wallis p =… | summary.json | `subject_study_hours_p` |
| 358 | .023 | …) = 3.68, p = .013; Kruskal – Wallis p = .023; highest among STEM stu… | summary.json | `r_ci_control[0]`, `subject_study_hours_kw_p`, `table_convergent.csv[3].ci_lo` |
| 358 | 3.52 | …lis p = .023; highest among STEM students, 3.52 h, and lowest among Comm… | summary.json | `subject_study_hours_mean_STEM` |
| 358 | 2.14 | …3.52 h, and lowest among Commerce students, 2.14 h) and, in the ANOVA onl… | summary.json | `subject_study_hours_mean_Commerce` |
| 358 | 4 | …in the ANOVA only, by main study device (F(4, 166) = 2.49, p = .045… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 358 | 166 | …the ANOVA only, by main study device (F(4, 166) = 2.49, p = .045; Kr… | summary.json | `device_study_hours_df[1]`, `device_ssce_df[1]` |
| 358 | 2.49 | …OVA only, by main study device (F(4, 166) = 2.49, p = .045; Kruskal –… | summary.json | `device_study_hours_F` |
| 358 | .045 | …main study device (F(4, 166) = 2.49, p = .045; Kruskal – Wallis p =… | summary.json | `prec_Junco & Cotten 2012_halfwidth`, `ssce_kw_p`, `exp_p` (+7) |
| 358 | .051 | …) = 2.49, p = .045; Kruskal – Wallis p = .051); these unadjusted, exp… | summary.json | `y1in_pbeta_switch`, `device_study_hours_kw_p` |
| 358 | 3 | …ver-read. SSCE did not differ by subject (F(3, 167) = 0.54, p = .657… | summary.json | `prec_Rosen et al. 2013_ci[0]`, `study_hours_mean_Uni Y2`, `study_hours_ci_Uni Y2[1]` (+38) |
| 358 | 167 | …-read. SSCE did not differ by subject (F(3, 167) = 0.54, p = .657) or… | summary.json | `subject_study_hours_df[1]`, `subject_study_hours_sd_Other`, `subject_ssce_df[1]` |
| 358 | 0.54 | …SSCE did not differ by subject (F(3, 167) = 0.54, p = .657) or device… | summary.json | `ssce_mean_Uni Y3`, `ssce_mean_all`, `subject_ssce_F` (+2) |
| 358 | .657 | …differ by subject (F(3, 167) = 0.54, p = .657) or device (F(4, 166)… | summary.json | `subject_ssce_p` |
| 358 | 4 | …F(3, 167) = 0.54, p = .657) or device (F(4, 166) = 1.05, p = .384… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 358 | 166 | …, 167) = 0.54, p = .657) or device (F(4, 166) = 1.05, p = .384). T… | summary.json | `device_study_hours_df[1]`, `device_ssce_df[1]` |
| 358 | 1.05 | …= 0.54, p = .657) or device (F(4, 166) = 1.05, p = .384). The mix o… | summary.json | `device_ssce_F` |
| 358 | .384 | …= .657) or device (F(4, 166) = 1.05, p = .384). The mix of study devi… | summary.json | `device_ssce_p` |
| 358 | 2 | …s did not differ detectably across years ( ^2(8) = 13.16, p = .106;… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 358 | 8 | …did not differ detectably across years ( ^2(8) = 13.16, p = .106;… | summary.json | `prec_Lepp et al. 2015_halfwidth`, `study_hours_kw_p`, `reg_adj` (+18) |
| 358 | 13.16 | …ot differ detectably across years ( ^2(8) = 13.16, p = .106; ), but 3… | summary.json | `exp_r_n_academic`, `grid_9.0_all_r`, `device_year_chi2` (+1) |
| 358 | .106 | …ectably across years ( ^2(8) = 13.16, p = .106; ), but 33\% of the c… | summary.json | `hier_b1_p`, `device_year_p` |
| 358 | 33 | …ears ( ^2(8) = 13.16, p = .106; ), but 33\% of the cells had expec… | summary.json | `prec_Lukram et al. 2026_ci[1]`, `device_year_pct_cells_lt5`, `table_precision.csv[5].ci_hi` (+1) |
| 358 | 5 | …33\% of the cells had expected counts below 5, so this test is unreliab… | summary.json | `prec_Lukram et al. 2026_ci[0]`, `screen_mid_ci_Uni Y2[0]`, `study_hours_ci_Uni Y4+[1]` (+24) |
| 360 | +.05 | …der (male versus all other respondents; r = +.05, p = .538) or to stud… | summary.json | `study_hours_anova_p`, `exp_p_n_purposes`, `r_ci_switch[1]` (+16) |
| 360 | .538 | …rsus all other respondents; r = +.05, p = .538) or to studying a STEM… | summary.json | `subject_ssce_F`, `discr_p_gender_bin` |
| 360 | +.09 | …= .538) or to studying a STEM subject (r = +.09, p = .219). The expos… | summary.json | `prec_Junco & Cotten 2012_width`, `prec_Bjerre-Nielsen et al. 2020_halfwidth`, `exp_p_n_academic` (+11) |
| 360 | .219 | …to studying a STEM subject (r = +.09, p = .219). The exposure – effici… | summary.json | `discr_p_stem` |
| 360 | .652 | …iffer detectably by gender (interaction p = .652, male and female respon… | summary.json | `etg_Uni Y2->Uni Y3_d_lo`, `y1in_p_tech_helps`, `y1in_p_holm_tech_helps` (+2) |
| 360 | 164 | …p = .652, male and female respondents, n = 164), subject (STEM versus… | summary.json | `reg_dof`, `mod_gender_n` |
| 360 | .991 | …n = 164), subject (STEM versus other, p = .991, n = 171) or universi… | summary.json | `mod_stem_p` |
| 360 | 171 | …subject (STEM versus other, p = .991, n = 171) or university year (F… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 360 | 2 | …p = .991, n = 171) or university year (F(2, 165) = 0.50, p = .606… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 360 | 165 | ….991, n = 171) or university year (F(2, 165) = 0.50, p = .606, n… | summary.json | `mod_year_df[1]` |
| 360 | 0.50 | …n = 171) or university year (F(2, 165) = 0.50, p = .606, n = 171)… | summary.json | `device_study_hours_mean_Other`, `device_ssce_mean_Other`, `mod_year_F` |
| 360 | .606 | …or university year (F(2, 165) = 0.50, p = .606, n = 171), consistent… | summary.json | `ssce_ci_Uni Y3[1]`, `mod_year_p`, `table_by_year.csv[1].ssce_ci_hi` |
| 360 | 171 | …y year (F(2, 165) = 0.50, p = .606, n = 171), consistent with H4; w… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 370 | 8 | …rossing four values for the open ``more than 8 hours'' band (8.5, 9, 10… | summary.json | `prec_Lepp et al. 2015_halfwidth`, `study_hours_kw_p`, `reg_adj` (+18) |
| 370 | 8.5 | …ues for the open ``more than 8 hours'' band (8.5, 9, 10 and 11 h) with tw… | summary.json | `beta_control`, `table_builds.csv[0].mid_high`, `table_builds.csv[1].mid_high` (+1) |
| 370 | 9 | …or the open ``more than 8 hours'' band (8.5, 9, 10 and 11 h) with two de… | summary.json | `prec_Junco & Cotten 2012_width`, `prec_Bjerre-Nielsen et al. 2020_halfwidth`, `prec_Giunchiglia et al. 2018_ci[0]` (+19) |
| 370 | 10 | …the open ``more than 8 hours'' band (8.5, 9, 10 and 11 h) with two denom… | summary.json | `pct_device_Tablet`, `r_switch`, `r_ci_workload[0]` (+24) |
| 370 | 11 | …n ``more than 8 hours'' band (8.5, 9, 10 and 11 h) with two denominators… | summary.json | `pct_subject_Arts`, `prec_Junco & Cotten 2012_ci[0]`, `exp_r_without_lowest_band` (+13) |
| 370 | -.15 | …re – efficiency correlation was stable (r = -.15 in every build) and sig… | summary.json | `exp_r`, `med_c_total`, `grid_r_min` (+10) |
| 370 | .045 | …t in all four builds, though only just (p = .045 to .049). With the fi… | summary.json | `prec_Junco & Cotten 2012_halfwidth`, `ssce_kw_p`, `exp_p` (+7) |
| 370 | .049 | …our builds, though only just (p = .045 to .049). With the fixed-seven… | summary.json | `r_ci_switch[1]`, `med_a_p`, `grid_11.0_selected_p` (+2) |
| 370 | +.13 | …or it was positive but not significant (r = +.13 to +.15, p = .056 t… | summary.json | `prec_Bjerre-Nielsen et al. 2020_min_r_80`, `exp_r_n_academic`, `r_control` (+11) |
| 370 | +.15 | …positive but not significant (r = +.13 to +.15, p = .056 to .102;… | summary.json | `prec_this study_halfwidth`, `exp_slope_ci[1]`, `grid_r_max` (+2) |
| 370 | .056 | …not significant (r = +.13 to +.15, p = .056 to .102; ; ). The… | summary.json | `grid_11.0_all_p`, `table_builds.csv[7].p` |
| 370 | .102 | …ficant (r = +.13 to +.15, p = .056 to .102; ; ). The reason is… | summary.json | `r_switch`, `grid_p_max`, `grid_8.5_all_p` (+3) |
| 370 | +.38 | …me selected more non-academic purposes (r = +.38, p < .001) and, non-s… | summary.json | `prec_Lukram et al. 2026_width`, `prec_Giunchiglia et al. 2018_ci[1]`, `ssce_ci_Uni Y2[0]` (+7) |
| 370 | .001 | …more non-academic purposes (r = +.38, p < .001) and, non-significantly… | summary.json | `exp_slope_ci[1]`, `exp_r2_gain`, `exp_p_n_purposes` (+5) |
| 370 | +.13 | …non-significantly, more academic ones (r = +.13, p = .086). H1 is the… | summary.json | `prec_Bjerre-Nielsen et al. 2020_min_r_80`, `exp_r_n_academic`, `r_control` (+11) |
| 370 | .086 | …cantly, more academic ones (r = +.13, p = .086). H1 is therefore suppo… | summary.json | `exp_p_n_academic`, `med_c_direct_p`, `grid_9.0_all_p` (+1) |
| 370 | 1.73 | …iency. The mean study-time proxy ranged from 1.73 to 3.38 h across builds,… | summary.json | `hier_b1_F`, `grid_mean_min`, `table_builds.csv[1].mean_study_h` |
| 370 | 3.38 | …he mean study-time proxy ranged from 1.73 to 3.38 h across builds, so its… | summary.json | `grid_mean_max`, `table_builds.csv[6].mean_study_h` |
| 379 | 95 | …) & Denominator & Mean study time (h) & r [95\% CI] & p \\… | design | — |
| 381 | 8.5 | …8.5 & selected & 3.12 & -.1… | summary.json | `beta_control`, `table_builds.csv[0].mid_high`, `table_builds.csv[1].mid_high` (+1) |
| 381 | 3.12 | …8.5 & selected & 3.12 & -.153 [-.296, -.003… | summary.json | `study_hours_ci_Uni Y2[1]`, `y1in_r_tech_helps`, `table_builds.csv[0].mean_study_h` (+1) |
| 381 | -.153 | …8.5 & selected & 3.12 & -.153 [-.296, -.003] & .046… | summary.json | `grid_8.5_selected_r`, `grid_10.0_selected_r`, `table_builds.csv[0].r` (+1) |
| 381 | -.296 | …8.5 & selected & 3.12 & -.153 [-.296, -.003] & .046 \\… | output table | `table_builds.csv[0].r_ci_lo`, `table_builds.csv[4].r_ci_lo` |
| 381 | -.003 | …8.5 & selected & 3.12 & -.153 [-.296, -.003] & .046 \\… | output table | `table_builds.csv[0].r_ci_hi`, `table_builds.csv[4].r_ci_hi` |
| 381 | .046 | …selected & 3.12 & -.153 [-.296, -.003] & .046 \\… | summary.json | `prec_Lukram et al. 2026_ci[0]`, `grid_8.5_selected_p`, `grid_10.0_selected_p` (+5) |
| 382 | 8.5 | …8.5 & all & 1.73 & +.125… | summary.json | `beta_control`, `table_builds.csv[0].mid_high`, `table_builds.csv[1].mid_high` (+1) |
| 382 | 1.73 | …8.5 & all & 1.73 & +.125 [-.025, .270]… | summary.json | `hier_b1_F`, `grid_mean_min`, `table_builds.csv[1].mean_study_h` |
| 382 | +.125 | …8.5 & all & 1.73 & +.125 [-.025, .270] & .102… | summary.json | `grid_8.5_all_r`, `table_builds.csv[1].r` |
| 382 | -.025 | …8.5 & all & 1.73 & +.125 [-.025, .270] & .102 \\… | output table | `table_builds.csv[1].r_ci_lo` |
| 382 | .270 | …8.5 & all & 1.73 & +.125 [-.025, .270] & .102 \\… | output table | `table_builds.csv[1].r_ci_hi` |
| 382 | .102 | …8.5 & all & 1.73 & +.125 [-.025, .270] & .102 \\… | summary.json | `r_switch`, `grid_p_max`, `grid_8.5_all_p` (+3) |
| 383 | 9.0 | …9.0 (used) & selected & 3.17… | summary.json | `hier_dR2`, `text_SUGGESTIONS_Focus/distraction controls_n`, `table_builds.csv[2].mid_high` (+3) |
| 383 | 3.17 | …9.0 (used) & selected & 3.17 & -.154 [-.297, -.004… | summary.json | `study_hours_mean_all`, `table_builds.csv[2].mean_study_h` |
| 383 | -.154 | …9.0 (used) & selected & 3.17 & -.154 [-.297, -.004] & .045… | summary.json | `exp_r`, `med_c_total`, `grid_r_min` (+2) |
| 383 | -.297 | …9.0 (used) & selected & 3.17 & -.154 [-.297, -.004] & .045 \\… | summary.json | `exp_r_ci[0]`, `table_builds.csv[2].r_ci_lo` |
| 383 | -.004 | …(used) & selected & 3.17 & -.154 [-.297, -.004] & .045 \\… | summary.json | `exp_r_ci[1]`, `table_builds.csv[2].r_ci_hi`, `table_builds.csv[7].r_ci_lo` |
| 383 | .045 | …selected & 3.17 & -.154 [-.297, -.004] & .045 \\… | summary.json | `prec_Junco & Cotten 2012_halfwidth`, `ssce_kw_p`, `exp_p` (+7) |
| 384 | 9.0 | …9.0 & all & 1.77 & +.132… | summary.json | `hier_dR2`, `text_SUGGESTIONS_Focus/distraction controls_n`, `table_builds.csv[2].mid_high` (+3) |
| 384 | 1.77 | …9.0 & all & 1.77 & +.132 [-.019, .276]… | output table | `table_builds.csv[3].mean_study_h` |
| 384 | +.132 | …9.0 & all & 1.77 & +.132 [-.019, .276] & .086… | summary.json | `exp_r_n_academic`, `grid_9.0_all_r`, `table_builds.csv[3].r` |
| 384 | -.019 | …9.0 & all & 1.77 & +.132 [-.019, .276] & .086 \\… | output table | `table_builds.csv[3].r_ci_lo` |
| 384 | .276 | …9.0 & all & 1.77 & +.132 [-.019, .276] & .086 \\… | output table | `table_builds.csv[3].r_ci_hi` |
| 384 | .086 | …9.0 & all & 1.77 & +.132 [-.019, .276] & .086 \\… | summary.json | `exp_p_n_academic`, `med_c_direct_p`, `grid_9.0_all_p` (+1) |
| 385 | 10.0 | …10.0 & selected & 3.27 & -.1… | summary.json | `split_switch_median_r[0]`, `table_builds.csv[4].mid_high`, `table_builds.csv[5].mid_high` (+4) |
| 385 | 3.27 | …10.0 & selected & 3.27 & -.153 [-.296, -.003… | summary.json | `study_hours_mean_Uni Y3`, `table_builds.csv[4].mean_study_h`, `table_by_year.csv[1].study_hours_mean` |
| 385 | -.153 | …10.0 & selected & 3.27 & -.153 [-.296, -.003] & .046… | summary.json | `grid_8.5_selected_r`, `grid_10.0_selected_r`, `table_builds.csv[0].r` (+1) |
| 385 | -.296 | …10.0 & selected & 3.27 & -.153 [-.296, -.003] & .046 \\… | output table | `table_builds.csv[0].r_ci_lo`, `table_builds.csv[4].r_ci_lo` |
| 385 | -.003 | …10.0 & selected & 3.27 & -.153 [-.296, -.003] & .046 \\… | output table | `table_builds.csv[0].r_ci_hi`, `table_builds.csv[4].r_ci_hi` |
| 385 | .046 | …selected & 3.27 & -.153 [-.296, -.003] & .046 \\… | summary.json | `prec_Lukram et al. 2026_ci[0]`, `grid_8.5_selected_p`, `grid_10.0_selected_p` (+5) |
| 386 | 10.0 | …10.0 & all & 1.84 & +.141… | summary.json | `split_switch_median_r[0]`, `table_builds.csv[4].mid_high`, `table_builds.csv[5].mid_high` (+4) |
| 386 | 1.84 | …10.0 & all & 1.84 & +.141 [-.010, .285]… | output table | `table_builds.csv[5].mean_study_h` |
| 386 | +.141 | …10.0 & all & 1.84 & +.141 [-.010, .285] & .067… | summary.json | `grid_10.0_all_r`, `table_builds.csv[5].r`, `table_ssce_by_band.csv[0].se` |
| 386 | -.010 | …10.0 & all & 1.84 & +.141 [-.010, .285] & .067 \\… | output table | `table_builds.csv[5].r_ci_lo` |
| 386 | .285 | …10.0 & all & 1.84 & +.141 [-.010, .285] & .067 \\… | output table | `table_builds.csv[5].r_ci_hi` |
| 386 | .067 | …0.0 & all & 1.84 & +.141 [-.010, .285] & .067 \\… | summary.json | `grid_10.0_all_p`, `table_builds.csv[5].p` |
| 387 | 11.0 | …11.0 & selected & 3.38 & -.1… | summary.json | `disclosure_cells_lt3`, `table_builds.csv[6].mid_high`, `table_builds.csv[7].mid_high` |
| 387 | 3.38 | …11.0 & selected & 3.38 & -.151 [-.294, -.001… | summary.json | `grid_mean_max`, `table_builds.csv[6].mean_study_h` |
| 387 | -.151 | …11.0 & selected & 3.38 & -.151 [-.294, -.001] & .049… | summary.json | `grid_11.0_selected_r`, `table_builds.csv[6].r` |
| 387 | -.294 | …11.0 & selected & 3.38 & -.151 [-.294, -.001] & .049 \\… | output table | `table_builds.csv[6].r_ci_lo` |
| 387 | -.001 | …11.0 & selected & 3.38 & -.151 [-.294, -.001] & .049 \\… | output table | `table_builds.csv[6].r_ci_hi` |
| 387 | .049 | …selected & 3.38 & -.151 [-.294, -.001] & .049 \\… | summary.json | `r_ci_switch[1]`, `med_a_p`, `grid_11.0_selected_p` (+2) |
| 388 | 11.0 | …11.0 & all & 1.92 & +.146… | summary.json | `disclosure_cells_lt3`, `table_builds.csv[6].mid_high`, `table_builds.csv[7].mid_high` |
| 388 | 1.92 | …11.0 & all & 1.92 & +.146 [-.004, .290]… | output table | `table_builds.csv[7].mean_study_h` |
| 388 | +.146 | …11.0 & all & 1.92 & +.146 [-.004, .290] & .056… | summary.json | `grid_r_max`, `grid_11.0_all_r`, `table_builds.csv[7].r` |
| 388 | -.004 | …11.0 & all & 1.92 & +.146 [-.004, .290] & .056 \\… | summary.json | `exp_r_ci[1]`, `table_builds.csv[2].r_ci_hi`, `table_builds.csv[7].r_ci_lo` |
| 388 | .290 | …11.0 & all & 1.92 & +.146 [-.004, .290] & .056 \\… | output table | `table_builds.csv[7].r_ci_hi` |
| 388 | .056 | …1.0 & all & 1.92 & +.146 [-.004, .290] & .056 \\… | summary.json | `grid_11.0_all_p`, `table_builds.csv[7].p` |
| 400 | 1,000 | …{Split-half replication.} Across 1,000 random splits of the sam… | output table | `table_builds.csv[4].mid_high`, `table_builds.csv[5].mid_high`, `table_device_by_year.csv[0].Mixed` (+2) |
| 400 | 93.0 | …lations kept the same sign in both halves in 93.0\% of splits for screen e… | summary.json | `split_screen_mid_same_sign_pct`, `table_splithalf.csv[0].same_sign_pct` |
| 400 | -.16 | ….0\% of splits for screen exposure (medians -.16 and -.15), 99.8\% for… | summary.json | `split_screen_mid_median_r[0]`, `table_splithalf.csv[0].median_r_half1` |
| 400 | -.15 | …its for screen exposure (medians -.16 and -.15), 99.8\% for workload (… | summary.json | `exp_r`, `med_c_total`, `grid_r_min` (+10) |
| 400 | 99.8 | …screen exposure (medians -.16 and -.15), 99.8\% for workload (medians… | summary.json | `split_workload_same_sign_pct`, `table_splithalf.csv[2].same_sign_pct` |
| 400 | +.25 | …and -.15), 99.8\% for workload (medians +.25), 85.5\% for perceived… | summary.json | `r_workload`, `split_workload_median_r[0]`, `split_workload_median_r[1]` (+7) |
| 400 | 85.5 | ….15), 99.8\% for workload (medians +.25), 85.5\% for perceived control… | summary.json | `split_control_same_sign_pct`, `table_splithalf.csv[3].same_sign_pct` |
| 400 | +.13 | …25), 85.5\% for perceived control (medians +.13) and 80.6\% for task-sw… | summary.json | `prec_Bjerre-Nielsen et al. 2020_min_r_80`, `exp_r_n_academic`, `r_control` (+11) |
| 400 | 80.6 | …% for perceived control (medians +.13) and 80.6\% for task-switching (me… | summary.json | `split_switch_same_sign_pct`, `table_splithalf.csv[1].same_sign_pct` |
| 400 | -.10 | …13) and 80.6\% for task-switching (medians -.10). Keeping the same sign… | summary.json | `r_switch`, `split_switch_median_r[0]`, `split_switch_median_r[1]` (+5) |
| 402 | 10 | …hich together defined three short periods on 10 – 11 February 2026; the… | summary.json | `pct_device_Tablet`, `r_switch`, `r_ci_workload[0]` (+24) |
| 402 | 11 | …together defined three short periods on 10 – 11 February 2026; the share… | summary.json | `pct_subject_Arts`, `prec_Junco & Cotten 2012_ci[0]`, `exp_r_without_lowest_band` (+13) |
| 402 | 2026 | …ined three short periods on 10 – 11 February 2026; the shared dataset incl… | design | — |
| 402 | 171 | …times are not released. Twenty-three of the 171 responses are flagged. E… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 402 | 148 | …responses are flagged. Excluding them (n = 148) gave a stronger exposu… | summary.json | `cluster_n`, `table_cluster_sensitivity.csv[0].n`, `table_cluster_sensitivity.csv[1].n` (+3) |
| 402 | -.25 | …nger exposure – efficiency association (r = -.25, p = .003) and a simi… | summary.json | `r_ci_switch[0]`, `cluster_r_screen_mid`, `table_cluster_sensitivity.csv[0].r` (+1) |
| 402 | .003 | …e – efficiency association (r = -.25, p = .003) and a similar correlat… | summary.json | `hier_pFch`, `cluster_p_screen_mid`, `table_builds.csv[0].r_ci_hi` (+2) |
| 402 | +.26 | …nd a similar correlation with workload (r = +.26, p = .002); the corre… | summary.json | `exp_r_n_purposes`, `med_a`, `cluster_r_workload` (+3) |
| 402 | .002 | …correlation with workload (r = +.26, p = .002); the correlations with… | summary.json | `p_workload_n_nonacademic`, `cluster_p_workload`, `y1in_p_holm_workload` (+1) |
| 402 | +.09 | …he correlations with perceived control (r = +.09, p = .256) and task-s… | summary.json | `prec_Junco & Cotten 2012_width`, `prec_Bjerre-Nielsen et al. 2020_halfwidth`, `exp_p_n_academic` (+11) |
| 402 | .256 | …ons with perceived control (r = +.09, p = .256) and task-switching (r… | summary.json | `cluster_p_control`, `table_cluster_sensitivity.csv[3].p` |
| 402 | -.10 | …+.09, p = .256) and task-switching (r = -.10, p = .205) were again… | summary.json | `r_switch`, `split_switch_median_r[0]`, `split_switch_median_r[1]` (+5) |
| 402 | .205 | ….256) and task-switching (r = -.10, p = .205) were again not signifi… | summary.json | `cluster_p_switch`, `table_cluster_sensitivity.csv[1].p` |
| 402 | 2 | …lf-regulation model remained significant (R^2 = .09, F(4, 141) = 3.5… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 402 | .09 | …egulation model remained significant (R^2 = .09, F(4, 141) = 3.54, p… | summary.json | `prec_Junco & Cotten 2012_width`, `prec_Bjerre-Nielsen et al. 2020_halfwidth`, `prec_Giunchiglia et al. 2018_ci[0]` (+14) |
| 402 | 4 | …model remained significant (R^2 = .09, F(4, 141) = 3.54, p = .009… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 402 | 141 | …del remained significant (R^2 = .09, F(4, 141) = 3.54, p = .009, n… | summary.json | `cluster_reg_dof` |
| 402 | 3.54 | …ained significant (R^2 = .09, F(4, 141) = 3.54, p = .009, n = 146)… | summary.json | `cluster_reg_F` |
| 402 | .009 | …icant (R^2 = .09, F(4, 141) = 3.54, p = .009, n = 146).… | summary.json | `uniqueR2_focus`, `cluster_reg_p`, `table_selfreg_model.csv[0].unique_r2` |
| 402 | 146 | …= .09, F(4, 141) = 3.54, p = .009, n = 146).… | summary.json | `cluster_reg_n`, `table_cluster_sensitivity.csv[4].n` |
| 404 | 211 | …ncluded.} Repeating the main analyses on all 211 university respondents,… | summary.json | `full_uni_university_institution`, `y1in_n`, `y1in_n_switch` (+3) |
| 404 | 40 | …ll 211 university respondents, including the 40 first-year students, gav… | summary.json | `full_uni_year1_excluded`, `med_b_p` |
| 404 | -.14 | …e exposure – efficiency correlation was r = -.14 (p = .040), workload… | summary.json | `r_ci_tech_helps[0]`, `beta_switch`, `med_c_direct` (+5) |
| 404 | .040 | …efficiency correlation was r = -.14 (p = .040), workload remained the… | summary.json | `cluster_r_focus`, `y1in_exp_p`, `y1in_p_holm_control` (+1) |
| 404 | +.24 | …rkload remained the clearest correlate (r = +.24, p < .001), task-swit… | summary.json | `prec_Bjerre-Nielsen et al. 2020_ci[1]`, `prec_Rosen et al. 2013_width`, `prec_Giunchiglia et al. 2018_halfwidth` (+3) |
| 404 | .001 | …ned the clearest correlate (r = +.24, p < .001), task-switching was ag… | summary.json | `exp_slope_ci[1]`, `exp_r2_gain`, `exp_p_n_purposes` (+5) |
| 404 | -.12 | …sk-switching was again not significant (r = -.12, p = .084), and the s… | summary.json | `y1in_r_switch` |
| 404 | .084 | …was again not significant (r = -.12, p = .084), and the self-regulati… | summary.json | `study_hours_kw_p`, `y1in_p_switch` |
| 404 | 2 | …el explained a similar share of variance (R^2 = .12, F(4, 204) = 6.7… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 404 | .12 | …xplained a similar share of variance (R^2 = .12, F(4, 204) = 6.70, p… | summary.json | `prec_Lepp et al. 2015_min_r_80`, `prec_Rosen et al. 2013_halfwidth`, `etg_Uni Y2->Uni Y3_p_holm` (+13) |
| 404 | 4 | …a similar share of variance (R^2 = .12, F(4, 204) = 6.70, p < .001… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 404 | 204 | …imilar share of variance (R^2 = .12, F(4, 204) = 6.70, p < .001, n… | summary.json | `y1in_reg_dof` |
| 404 | 6.70 | …share of variance (R^2 = .12, F(4, 204) = 6.70, p < .001, n = 209)… | summary.json | `y1in_reg_F` |
| 404 | .001 | …iance (R^2 = .12, F(4, 204) = 6.70, p < .001, n = 209), with workl… | summary.json | `exp_slope_ci[1]`, `exp_r2_gain`, `exp_p_n_purposes` (+5) |
| 404 | 209 | …= .12, F(4, 204) = 6.70, p < .001, n = 209), with workload again t… | summary.json | `y1in_n_focus`, `y1in_reg_n` |
| 404 | +.18 | …ociated with SSCE in the larger sample (r = +.18, p = .010; Holm p =… | summary.json | `prec_Bjerre-Nielsen et al. 2020_width`, `p_switch`, `y1in_r_control` (+2) |
| 404 | .010 | …SSCE in the larger sample (r = +.18, p = .010; Holm p = .040) but n… | summary.json | `y1in_p_control`, `table_builds.csv[5].r_ci_lo` |
| 404 | .040 | …er sample (r = +.18, p = .010; Holm p = .040) but not among students… | summary.json | `cluster_r_focus`, `y1in_exp_p`, `y1in_p_holm_control` (+1) |
| 404 | 2 | …p = .040) but not among students in Years 2 to 4 and above. Because… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 404 | 4 | ….040) but not among students in Years 2 to 4 and above. Because first… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 407 | 171 | …l survey to the three open-text items of the 171 respondents; the scheme… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 407 | 77 | …output are in the public repository. Of the 77 usable challenge respons… | summary.json | `text_CHALLENGE_n` |
| 407 | 46 | …itory. Of the 77 usable challenge responses, 46 (59.7\%) referred to dis… | summary.json | `n_device_Smartphone`, `text_CHALLENGE_Distraction / task-switching_n`, `table_device_by_year.csv[1].Laptop/Desktop` (+2) |
| 407 | 59.7 | …y. Of the 77 usable challenge responses, 46 (59.7\%) referred to distracti… | summary.json | `text_CHALLENGE_Distraction / task-switching_pct` |
| 407 | 21 | …interruption, by far the most common theme; 21 (27.3\%) mentioned notif… | summary.json | `min_r_80pct_power`, `prec_this study_min_r_80`, `text_CHALLENGE_Notifications (sub-set)_n` (+3) |
| 407 | 27.3 | …erruption, by far the most common theme; 21 (27.3\%) mentioned notificatio… | summary.json | `text_CHALLENGE_Notifications (sub-set)_pct` |
| 407 | 6 | …ctivity and technical problems accounted for 6 (7.8\%). Representative… | summary.json | `full_out_of_range`, `n_subject_Other`, `prec_Bjerre-Nielsen et al. 2020_ci[0]` (+29) |
| 407 | 7.8 | …vity and technical problems accounted for 6 (7.8\%). Representative respo… | summary.json | `se_focus`, `text_CHALLENGE_Connectivity / technical_pct`, `table_selfreg_model.csv[0].se` |
| 407 | 85 | …s time and reduces productivity.'' Among the 85 positive-experience resp… | summary.json | `p_tech_helps`, `p_holm_tech helpfulness`, `p_bh_tech helpfulness` (+4) |
| 407 | 36 | …e-experience responses, access to resources (36, 42.4\%) and improved con… | summary.json | `y1in_pbeta_focus`, `device_ssce_sd_Tablet`, `text_POSITIVE_Access to resources/materials_n` |
| 407 | 42.4 | …perience responses, access to resources (36, 42.4\%) and improved conceptu… | summary.json | `text_POSITIVE_Access to resources/materials_pct` |
| 407 | 19 | ….4\%) and improved conceptual understanding (19, 22.4\%) dominated. Among… | summary.json | `n_subject_Arts`, `prec_Junco & Cotten 2012_ci[1]`, `prec_Lukram et al. 2026_halfwidth` (+4) |
| 407 | 22.4 | …) and improved conceptual understanding (19, 22.4\%) dominated. Among the… | summary.json | `text_POSITIVE_Concept understanding/clarity_pct` |
| 407 | 47 | …erstanding (19, 22.4\%) dominated. Among the 47 suggestion responses, in… | summary.json | `pct_device_Laptop/Desktop`, `prec_Giunchiglia et al. 2018_width`, `ssce_mean_Uni Y2` (+8) |
| 407 | 12 | …responses, institutional tools or platforms (12, 25.5\%), focus and distr… | summary.json | `prec_Lepp et al. 2015_min_r_80`, `prec_Rosen et al. 2013_halfwidth`, `etg_Uni Y2->Uni Y3_p_holm` (+12) |
| 407 | 25.5 | …onses, institutional tools or platforms (12, 25.5\%), focus and distractio… | summary.json | `text_SUGGESTIONS_Institutional tools/platform_pct` |
| 407 | 9 | …12, 25.5\%), focus and distraction controls (9, 19.1\%) and infrastructu… | summary.json | `prec_Junco & Cotten 2012_width`, `prec_Bjerre-Nielsen et al. 2020_halfwidth`, `prec_Giunchiglia et al. 2018_ci[0]` (+19) |
| 407 | 19.1 | …25.5\%), focus and distraction controls (9, 19.1\%) and infrastructure or… | summary.json | `text_SUGGESTIONS_Focus/distraction controls_pct` |
| 407 | 6 | …19.1\%) and infrastructure or connectivity (6, 12.8\%) were the most fr… | summary.json | `full_out_of_range`, `n_subject_Other`, `prec_Bjerre-Nielsen et al. 2020_ci[0]` (+29) |
| 407 | 12.8 | ….1\%) and infrastructure or connectivity (6, 12.8\%) were the most frequen… | summary.json | `r_control`, `split_control_median_r[0]`, `split_control_median_r[1]` (+4) |
| 409 | 3 | …ers that deny being distracted. In addition, 3 challenge responses and… | summary.json | `prec_Rosen et al. 2013_ci[0]`, `study_hours_mean_Uni Y2`, `study_hours_ci_Uni Y2[1]` (+38) |
| 409 | 2 | …cted. In addition, 3 challenge responses and 2 positive-experience resp… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 420 | +.25 | …& SSCE relates to related items & Workload +.25 (survives Holm correcti… | summary.json | `r_workload`, `split_workload_median_r[0]`, `split_workload_median_r[1]` (+7) |
| 420 | +.13 | …+.25 (survives Holm correction); control +.13 and task-switching -.1… | summary.json | `prec_Bjerre-Nielsen et al. 2020_min_r_80`, `exp_r_n_academic`, `r_control` (+11) |
| 420 | -.10 | …rection); control +.13 and task-switching -.10 (not significant) \\… | summary.json | `r_switch`, `split_switch_median_r[0]`, `split_switch_median_r[1]` (+5) |
| 421 | +.05 | …unrelated to off-target variables & Gender +.05 (p = .538), STEM +.0… | summary.json | `study_hours_anova_p`, `exp_p_n_purposes`, `r_ci_switch[1]` (+16) |
| 421 | .538 | …o off-target variables & Gender +.05 (p = .538), STEM +.09 (p = .21… | summary.json | `subject_ssce_F`, `discr_p_gender_bin` |
| 421 | +.09 | …ariables & Gender +.05 (p = .538), STEM +.09 (p = .219) \\… | summary.json | `prec_Junco & Cotten 2012_width`, `prec_Bjerre-Nielsen et al. 2020_halfwidth`, `exp_p_n_academic` (+11) |
| 421 | .219 | …ender +.05 (p = .538), STEM +.09 (p = .219) \\… | summary.json | `discr_p_stem` |
| 422 | 2 | …l validity & SSCE beyond demographics & R^2 = .090, F(4, 157) = 4.… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 422 | .090 | …lidity & SSCE beyond demographics & R^2 = .090, F(4, 157) = 4.18, p… | summary.json | `hier_dR2` |
| 422 | 4 | …SCE beyond demographics & R^2 = .090, F(4, 157) = 4.18, p = .003… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 422 | 157 | …beyond demographics & R^2 = .090, F(4, 157) = 4.18, p = .003 \\… | summary.json | `hier_df2` |
| 422 | 4.18 | …demographics & R^2 = .090, F(4, 157) = 4.18, p = .003 \\… | summary.json | `hier_Fch` |
| 422 | .003 | …s & R^2 = .090, F(4, 157) = 4.18, p = .003 \\… | summary.json | `hier_pFch`, `cluster_p_screen_mid`, `table_builds.csv[0].r_ci_hi` (+2) |
| 423 | -.017 | …path via task-switching & Not significant: -.017, 95\% CI [-.064, .025]… | summary.json | `med_indirect` |
| 423 | 95 | …a task-switching & Not significant: -.017, 95\% CI [-.064, .025] \\… | design | — |
| 423 | -.064 | …tching & Not significant: -.017, 95\% CI [-.064, .025] \\… | summary.json | `med_ci_lo` |
| 423 | .025 | …& Not significant: -.017, 95\% CI [-.064, .025] \\… | summary.json | `med_ci_hi`, `table_builds.csv[1].r_ci_lo` |
| 424 | 8 | …ve builds & Exposure – efficiency r across 8 builds & Negative with s… | summary.json | `prec_Lepp et al. 2015_halfwidth`, `study_hours_kw_p`, `reg_adj` (+18) |
| 424 | -.15 | …8 builds & Negative with share denominator (-.15, 4 of 4 significant); p… | summary.json | `exp_r`, `med_c_total`, `grid_r_min` (+10) |
| 424 | 4 | …s & Negative with share denominator (-.15, 4 of 4 significant); posit… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 424 | 4 | …egative with share denominator (-.15, 4 of 4 significant); positive,… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 425 | 9 | …band & Exposure – efficiency r without the 9 students under 2 h & r… | summary.json | `prec_Junco & Cotten 2012_width`, `prec_Bjerre-Nielsen et al. 2020_halfwidth`, `prec_Giunchiglia et al. 2018_ci[0]` (+19) |
| 425 | 2 | …efficiency r without the 9 students under 2 h & r = -.11, p = .16… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 425 | -.11 | …r without the 9 students under 2 h & r = -.11, p = .160 (n = 162)… | summary.json | `exp_r_without_lowest_band` |
| 425 | .160 | …the 9 students under 2 h & r = -.11, p = .160 (n = 162) \\… | summary.json | `exp_p_without_lowest_band`, `split_screen_mid_median_r[0]`, `table_splithalf.csv[0].median_r_half1` |
| 425 | 162 | …nts under 2 h & r = -.11, p = .160 (n = 162) \\… | summary.json | `exp_n_without_lowest_band` |
| 426 | 81 | …irection across random halves & Same sign in 81 – 100\% of 1,000 splits… | summary.json | `split_switch_same_sign_pct`, `table_splithalf.csv[1].same_sign_pct` |
| 426 | 100 | …ion across random halves & Same sign in 81 – 100\% of 1,000 splits \\… | summary.json | `full_uni_school_institution_records[0]`, `split_workload_same_sign_pct`, `text_CHALLENGE_Entertainment pull_n` (+4) |
| 426 | 1,000 | …s random halves & Same sign in 81 – 100\% of 1,000 splits \\… | output table | `table_builds.csv[4].mid_high`, `table_builds.csv[5].mid_high`, `table_device_by_year.csv[0].Mixed` (+2) |
| 427 | -.25 | …milar responses & Exposure – efficiency r = -.25 (n = 148) \\… | summary.json | `r_ci_switch[0]`, `cluster_r_screen_mid`, `table_cluster_sensitivity.csv[0].r` (+1) |
| 427 | 148 | …ses & Exposure – efficiency r = -.25 (n = 148) \\… | summary.json | `cluster_n`, `table_cluster_sensitivity.csv[0].n`, `table_cluster_sensitivity.csv[1].n` (+3) |
| 428 | -.14 | …sed restriction & Exposure – efficiency r = -.14; workload +.24; contr… | summary.json | `r_ci_tech_helps[0]`, `beta_switch`, `med_c_direct` (+5) |
| 428 | +.24 | …Exposure – efficiency r = -.14; workload +.24; control significant (… | summary.json | `prec_Bjerre-Nielsen et al. 2020_ci[1]`, `prec_Rosen et al. 2013_width`, `prec_Giunchiglia et al. 2018_halfwidth` (+3) |
| 428 | +.18 | ….14; workload +.24; control significant (+.18) (n = 211) \\… | summary.json | `prec_Bjerre-Nielsen et al. 2020_width`, `p_switch`, `y1in_r_control` (+2) |
| 428 | 211 | …d +.24; control significant (+.18) (n = 211) \\… | summary.json | `full_uni_university_institution`, `y1in_n`, `y1in_n_switch` (+3) |
| 429 | 0.3 | …& Gender invariance & Equivalence within 0.3 SD not shown for study… | summary.json | `prec_this study_ci[1]`, `prec_this study_width`, `prec_Rosen et al. 2013_ci[1]` (+66) |
| 429 | .115 | …in 0.3 SD not shown for study time (p = .115) or SSCE (p = .138) \… | summary.json | `gender_study_hours_tost_p`, `table_gender.csv[0].tost_p` |
| 429 | .138 | …wn for study time (p = .115) or SSCE (p = .138) \\… | summary.json | `gender_ssce_tost_p`, `table_gender.csv[1].tost_p` |
| 431 | 30.4 | …hared-method inflation & Harman first factor 30.4\% (< 50\%) \\… | summary.json | `harman_first_pct` |
| 431 | 50 | …d inflation & Harman first factor 30.4\% (< 50\%) \\… | summary.json | `n_year_Uni Y2`, `device_study_hours_mean_Other`, `device_ssce_mean_Other` (+4) |
| 438 | 2 | …n time, but the association was small (about 2\% of the variance), belo… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 438 | 9 | …t weakened and lost significance without the 9 students in the lowest s… | summary.json | `prec_Junco & Cotten 2012_width`, `prec_Bjerre-Nielsen et al. 2020_halfwidth`, `prec_Giunchiglia et al. 2018_ci[0]` (+19) |
| 440 | 95 | …s are inconclusive rather than negative: the 95\% intervals for the cont… | design | — |
| 440 | +.13 | …ve: the 95\% intervals for the control (r = +.13, [-.02, .27]) and tas… | summary.json | `prec_Bjerre-Nielsen et al. 2020_min_r_80`, `exp_r_n_academic`, `r_control` (+11) |
| 440 | -.02 | …5\% intervals for the control (r = +.13, [-.02, .27]) and task-switchi… | summary.json | `exp_slope`, `r_ci_control[0]`, `med_indirect` (+2) |
| 440 | .27 | …tervals for the control (r = +.13, [-.02, .27]) and task-switching (… | summary.json | `prec_Rosen et al. 2013_ci[1]`, `r_ci_focus[1]`, `r_ci_control[1]` (+10) |
| 440 | -.10 | …13, [-.02, .27]) and task-switching (r = -.10, [-.25, .05]) correla… | summary.json | `r_switch`, `split_switch_median_r[0]`, `split_switch_median_r[1]` (+5) |
| 440 | -.25 | …02, .27]) and task-switching (r = -.10, [-.25, .05]) correlations inc… | summary.json | `r_ci_switch[0]`, `cluster_r_screen_mid`, `table_cluster_sensitivity.csv[0].r` (+1) |
| 440 | .05 | …7]) and task-switching (r = -.10, [-.25, .05]) correlations include… | summary.json | `prec_Lukram et al. 2026_ci[0]`, `study_hours_anova_p`, `exp_p_n_purposes` (+18) |
| 440 | 10 | …r time. Together the four indicators explain 10\% of the variance in SSC… | summary.json | `pct_device_Tablet`, `r_switch`, `r_ci_workload[0]` (+24) |
| 450 | 171 | …{What a sample of 171 can show, and comparison… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 451 | 171 | …A sample of 171 supports only coarse con… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 451 | .15 | …tions of the size reported here. Around r = .15, the 95\% confidence in… | summary.json | `prec_this study_halfwidth`, `exp_r`, `exp_slope_ci[1]` (+15) |
| 451 | 95 | …he size reported here. Around r = .15, the 95\% confidence interval ru… | design | — |
| 451 | .00 | …the 95\% confidence interval runs from about .00 to .29 (a half-width of… | summary.json | `n_excluded_school_institution`, `n_excluded_year1`, `prec_this study_ci[0]` (+32) |
| 451 | .29 | …% confidence interval runs from about .00 to .29 (a half-width of about .… | summary.json | `prec_this study_ci[1]`, `prec_this study_width`, `etg_Uni Y3->Uni Y4+_p_raw` (+10) |
| 451 | .15 | …from about .00 to .29 (a half-width of about .15), so an estimate of this… | summary.json | `prec_this study_halfwidth`, `exp_r`, `exp_slope_ci[1]` (+15) |
| 451 | 80 | …est correlation the sample could detect with 80\% power is about .21, an… | summary.json | `n_device_Laptop/Desktop`, `table_sample.csv[10].n` |
| 451 | .21 | …sample could detect with 80\% power is about .21, and its power to detect… | summary.json | `min_r_80pct_power`, `prec_this study_min_r_80`, `table_precision.csv[0].min_r_80` |
| 451 | .14 | …r is about .21, and its power to detect r = .14 was only .45. Two conse… | summary.json | `r_ci_tech_helps[0]`, `beta_switch`, `med_c_direct` (+13) |
| 451 | .45 | …, and its power to detect r = .14 was only .45. Two consequences follow… | summary.json | `power_r14`, `cluster_p_tech_helps`, `cluster_pbeta_control` (+1) |
| 451 | .15 | …uences follow. Significant correlations near .15, such as the exposure –… | summary.json | `prec_this study_halfwidth`, `exp_r`, `exp_slope_ci[1]` (+15) |
| 451 | .05 | …ges in coding or sample move them across the .05 threshold. And non-signi… | summary.json | `prec_Lukram et al. 2026_ci[0]`, `study_hours_anova_p`, `exp_p_n_purposes` (+18) |
| 451 | 211 | …pted this loss of precision, relative to the 211 university respondents,… | summary.json | `full_uni_university_institution`, `y1in_n`, `y1in_n_switch` (+3) |
| 453 | 95 | …ch primary study, the approximate width of a 95\% confidence interval ar… | design | — |
| 453 | .15 | …th of a 95\% confidence interval around r = .15 at that sample size; it… | summary.json | `prec_this study_halfwidth`, `exp_r`, `exp_slope_ci[1]` (+15) |
| 453 | 1839 | …ach study reported. Junco and Cotten , with 1839 students, could estimate… | summary.json | `prec_Junco & Cotten 2012_n`, `table_precision.csv[1].n` |
| 453 | 40 | …jerre-Nielsen et al.\ give intervals about 40\% narrower. Two meta-ana… | summary.json | `full_uni_year1_excluded`, `med_b_p` |
| 453 | -.12 | …one use, and academic outcomes at about r = -.12 to -.16, the same ord… | summary.json | `y1in_r_switch` |
| 453 | -.16 | …nd academic outcomes at about r = -.12 to -.16, the same order of magn… | summary.json | `split_screen_mid_median_r[0]`, `table_splithalf.csv[0].median_r_half1` |
| 453 | 102 | …le. At the other end, Lukram et al.\ (N = 102) and Giunchiglia et al.… | summary.json | `prec_Lukram et al. 2026_n`, `table_precision.csv[5].n` |
| 453 | 67 | …(N = 102) and Giunchiglia et al.\ (n = 67 analysed) are smaller a… | summary.json | `prec_Giunchiglia et al. 2018_n`, `table_precision.csv[6].n` |
| 455 | -.32 | …d in-class smartphone use and grades of r = -.32 shrank to a standardise… | cited source | — |
| 455 | -.045 | …32 shrank to a standardised coefficient of -.045 once stable student cha… | cited source | — |
| 466 | 2012 | …Junco \& Cotten (2012) & One university; col… | cited source | — |
| 466 | 1839 | …2012) & One university; college students & 1839 & Cross-sectional web su… | summary.json | `prec_Junco & Cotten 2012_n`, `table_precision.csv[1].n` |
| 466 | .09 | …ression (coefficients not in the abstract) & .09 & Much larger sample; GP… | summary.json | `prec_Junco & Cotten 2012_width`, `prec_Bjerre-Nielsen et al. 2020_halfwidth`, `prec_Giunchiglia et al. 2018_ci[0]` (+14) |
| 467 | 2015 | …Lepp et al.\ (2015) & One large public US… | cited source | — |
| 467 | 536 | …large public US university; undergraduates & 536 & Cross-sectional survey… | summary.json | `prec_Lepp et al. 2015_n`, `table_precision.csv[2].n` |
| 467 | -.164 | …PA & Survey measure of cell phone use & = -.164, p < .001, after cont… | cited source | — |
| 467 | .001 | …easure of cell phone use & = -.164, p < .001, after controlling for… | summary.json | `exp_slope_ci[1]`, `exp_r2_gain`, `exp_p_n_purposes` (+5) |
| 467 | 2 | …self-efficacy and high-school GPA (model R^2 = .449) & .17 & Actual… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 467 | .449 | …f-efficacy and high-school GPA (model R^2 = .449) & .17 & Actual GPA; co… | cited source | — |
| 467 | .17 | …y and high-school GPA (model R^2 = .449) & .17 & Actual GPA; controls f… | summary.json | `prec_Lepp et al. 2015_width`, `prec_Rosen et al. 2013_min_r_80`, `table_precision.csv[2].width` (+1) |
| 468 | 2020 | …Bjerre-Nielsen et al.\ (2020) & Technical Universit… | cited source | — |
| 468 | 470 | …(2020) & Technical University of Denmark & 470 & Two-year panel & App-l… | summary.json | `prec_Bjerre-Nielsen et al. 2020_n`, `study_hours_ci_Uni Y4+[1]`, `reg_F` (+2) |
| 468 | -.32 | …-class smartphone use & Cross-sectional r = -.32 [-.40, -.24]; within-… | cited source | — |
| 468 | -.40 | …martphone use & Cross-sectional r = -.32 [-.40, -.24]; within-student… | cited source | — |
| 468 | -.24 | …one use & Cross-sectional r = -.32 [-.40, -.24]; within-student standa… | cited source | — |
| 468 | -.045 | …40, -.24]; within-student standardised = -.045 & .18 & Objective loggi… | cited source | — |
| 468 | .18 | …; within-student standardised = -.045 & .18 & Objective logging; sho… | summary.json | `prec_Bjerre-Nielsen et al. 2020_width`, `etg_Uni Y3->Uni Y4+_d_lo`, `p_switch` (+4) |
| 469 | 2013 | …Rosen et al.\ (2013) & Students' homes; mi… | cited source | — |
| 469 | 263 | …middle school, high school and university & 263 & 15-min direct observat… | summary.json | `prec_Rosen et al. 2013_n`, `table_precision.csv[4].n` |
| 469 | 15 | …e school, high school and university & 263 & 15-min direct observation p… | summary.json | `pct_device_Mixed`, `prec_this study_halfwidth`, `exp_r` (+17) |
| 469 | 6 | …observed on- and off-task behaviour & Under 6 min on task before switc… | summary.json | `full_out_of_range`, `n_subject_Other`, `prec_Bjerre-Nielsen et al. 2020_ci[0]` (+29) |
| 469 | .24 | …wer GPAs (no coefficients in the abstract) & .24 & Direct behavioural obs… | summary.json | `prec_Bjerre-Nielsen et al. 2020_ci[1]`, `prec_Rosen et al. 2013_width`, `prec_Giunchiglia et al. 2018_halfwidth` (+3) |
| 470 | 2 | …This study & Bangladesh; university Years 2 – 4+ & 171 & Cross-secti… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 470 | 4 | …his study & Bangladesh; university Years 2 – 4+ & 171 & Cross-sectional… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 470 | 171 | …tudy & Bangladesh; university Years 2 – 4+ & 171 & Cross-sectional online… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 470 | -.15 | …purposes (SSCE) & Screen time with SSCE r = -.15 [-.30, -.004] & .29 &… | summary.json | `exp_r`, `med_c_total`, `grid_r_min` (+10) |
| 470 | -.30 | …(SSCE) & Screen time with SSCE r = -.15 [-.30, -.004] & .29 & Explora… | summary.json | `exp_r_ci[0]`, `table_builds.csv[0].r_ci_lo`, `table_builds.csv[0].r_ci_hi` (+2) |
| 470 | -.004 | …) & Screen time with SSCE r = -.15 [-.30, -.004] & .29 & Exploratory ef… | summary.json | `exp_r_ci[1]`, `table_builds.csv[2].r_ci_hi`, `table_builds.csv[7].r_ci_lo` |
| 470 | .29 | …time with SSCE r = -.15 [-.30, -.004] & .29 & Exploratory efficiency… | summary.json | `prec_this study_ci[1]`, `prec_this study_width`, `etg_Uni Y3->Uni Y4+_p_raw` (+10) |
| 471 | 2026 | …Lukram et al.\ (2026) & Medical college, no… | design | — |
| 471 | 102 | …college, north-east India; first-year MBBS & 102 & Prospective, 4 weeks &… | summary.json | `prec_Lukram et al. 2026_n`, `table_precision.csv[5].n` |
| 471 | 4 | …India; first-year MBBS & 102 & Prospective, 4 weeks & Device-recorded… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 471 | .541 | …to academic and non-academic & Academic = .541; non-academic = -.57… | summary.json | `ssce_mean_Uni Y3`, `table_by_year.csv[1].ssce_mean` |
| 471 | -.575 | …mic & Academic = .541; non-academic = -.575; total = -.091 (p… | cited source | — |
| 471 | -.091 | ….541; non-academic = -.575; total = -.091 (p = .364) with marks… | cited source | — |
| 471 | .364 | …cademic = -.575; total = -.091 (p = .364) with marks & .38 & Dev… | cited source | — |
| 471 | .38 | …total = -.091 (p = .364) with marks & .38 & Device records; achiev… | summary.json | `prec_Lukram et al. 2026_width`, `prec_Giunchiglia et al. 2018_ci[1]`, `ssce_ci_Uni Y2[0]` (+7) |
| 472 | 2018 | …Giunchiglia et al.\ (2018) & University of Trent… | cited source | — |
| 472 | 67 | …l.\ (2018) & University of Trento, Italy & 67 & Two-week app logging w… | summary.json | `prec_Giunchiglia et al. 2018_n`, `table_precision.csv[6].n` |
| 472 | -.26 | ….\ social-network sessions with credits r = -.26, p < .05 & .47 & Fine… | cited source | — |
| 472 | .05 | …twork sessions with credits r = -.26, p < .05 & .47 & Fine-grained lo… | summary.json | `prec_Lukram et al. 2026_ci[0]`, `study_hours_anova_p`, `exp_p_n_purposes` (+18) |
| 472 | .47 | …essions with credits r = -.26, p < .05 & .47 & Fine-grained logs; lin… | summary.json | `prec_Giunchiglia et al. 2018_width`, `ssce_mean_Uni Y2`, `gender_study_hours_p` (+5) |
| 473 | 2018 | …Kates et al.\ (2018) & Meta-analysis of st… | cited source | — |
| 473 | 2008 | …l.\ (2018) & Meta-analysis of studies from 2008 to 2017 & – & Meta-ana… | cited source | — |
| 473 | 2017 | …8) & Meta-analysis of studies from 2008 to 2017 & – & Meta-analysis &… | cited source | — |
| 473 | -.162 | …ny measure of mobile phone use & Pooled r = -.162 [-.196, -.128] & –… | cited source | — |
| 473 | -.196 | …e of mobile phone use & Pooled r = -.162 [-.196, -.128] & – & Field-w… | cited source | — |
| 473 | -.128 | …bile phone use & Pooled r = -.162 [-.196, -.128] & – & Field-wide ave… | cited source | — |
| 474 | 2021 | …Sunday et al.\ (2021) & Meta-analysis; 44 s… | cited source | — |
| 474 | 44 | …Sunday et al.\ (2021) & Meta-analysis; 44 studies, 16 countries &… | cited source | — |
| 474 | 16 | …t al.\ (2021) & Meta-analysis; 44 studies, 16 countries & 147,943 & Me… | summary.json | `exp_p_without_lowest_band`, `r_ci_tech_helps[1]`, `hier_b2_R2` (+3) |
| 474 | 147,943 | …& Meta-analysis; 44 studies, 16 countries & 147,943 & Meta-analysis & Smartp… | cited source | — |
| 474 | -.12 | …Smartphone addiction measures & Pooled r = -.12 & – & Very large pool… | summary.json | `y1in_r_switch` |
| 481 | 2 | …easons, and the further restriction to Years 2 to 4 and above was decid… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 481 | 4 | …s, and the further restriction to Years 2 to 4 and above was decided af… | summary.json | `pct_gender_Prefer not to say`, `pct_subject_Other`, `prec_Junco & Cotten 2012_halfwidth` (+34) |
| 481 | 211 | …above was decided after the results for all 211 university respondents h… | summary.json | `full_uni_university_institution`, `y1in_n`, `y1in_n_switch` (+3) |
| 483 | 171 | …Statistical power is limited. With n = 171, the smallest correlati… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 483 | 80 | …1, the smallest correlation detectable with 80\% power is about .21, an… | summary.json | `n_device_Laptop/Desktop`, `table_sample.csv[10].n` |
| 483 | .21 | …relation detectable with 80\% power is about .21, and all correlations ex… | summary.json | `min_r_80pct_power`, `prec_this study_min_r_80`, `table_precision.csv[0].min_r_80` |
| 483 | .15 | …workload are smaller than that; around r = .15 the 95\% interval has a… | summary.json | `prec_this study_halfwidth`, `exp_r`, `exp_slope_ci[1]` (+15) |
| 483 | 95 | …are smaller than that; around r = .15 the 95\% interval has a half-wi… | design | — |
| 483 | .15 | …the 95\% interval has a half-width of about .15 ( ). The exposure – eff… | summary.json | `prec_this study_halfwidth`, `exp_r`, `exp_slope_ci[1]` (+15) |
| 483 | 9 | …nd it is weaker and not significant once the 9 students in the lowest s… | summary.json | `prec_Junco & Cotten 2012_width`, `prec_Bjerre-Nielsen et al. 2020_halfwidth`, `prec_Giunchiglia et al. 2018_ci[0]` (+19) |
| 485 | .63 | …es correlate strongly (in the region of r .63 to .67) with multi-it… | summary.json | `cluster_p_focus`, `table_cluster_sensitivity.csv[4].p` |
| 485 | .67 | …ate strongly (in the region of r .63 to .67) with multi-item scales… | cited source | — |
| 489 | 6 | …naire was distributed to students from Class 6 upward, and school-age p… | summary.json | `full_out_of_range`, `n_subject_Other`, `prec_Bjerre-Nielsen et al. 2020_ci[0]` (+29) |
| 489 | 18 | …6 upward, and school-age participants under 18 took part without parent… | summary.json | `pct_year_Uni Y4+`, `n_device_Tablet`, `prec_Bjerre-Nielsen et al. 2020_width` (+8) |
| 489 | 7 | …the shared dataset, as are the responses of 7 respondents who chose a… | summary.json | `full_uni_school_institution`, `n_gender_Prefer not to say`, `prec_Junco & Cotten 2012_min_r_80` (+19) |
| 489 | 18 | …their second year or later would normally be 18 or older ( ), but this… | summary.json | `pct_year_Uni Y4+`, `n_device_Tablet`, `prec_Bjerre-Nielsen et al. 2020_width` (+8) |
| 494 | .12 | …ns reported here: detecting a correlation of .12 with 80\% power would ne… | summary.json | `prec_Lepp et al. 2015_min_r_80`, `prec_Rosen et al. 2013_halfwidth`, `etg_Uni Y2->Uni Y3_p_holm` (+13) |
| 494 | 80 | …ed here: detecting a correlation of .12 with 80\% power would need about… | summary.json | `n_device_Laptop/Desktop`, `table_sample.csv[10].n` |
| 494 | 543 | …tion of .12 with 80\% power would need about 543 respondents, 3.2 times t… | summary.json | `n_needed_r12_80pct` |
| 494 | 3.2 | …80\% power would need about 543 respondents, 3.2 times the present sample… | summary.json | `study_hours_mean_all`, `ssce_anova_F`, `r_ci_focus[0]` (+2) |
| 497 | 171 | …Among 171 university students in B… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 500 | 20260618 | …scripts/university\_analysis.py}, fixed seed 20260618) that reproduces every f… | design | — |
| 500 | 171 | …taset ( {data/SSCE\_survey\_university.csv}, 171 rows), except the compar… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 500 | 171 | …itory}. The shared dataset contains only the 171 responses analysed here;… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 503 | 32 | …ijheel Ideal School and College, Dhaka, with 32 years of dedicated servi… | summary.json | `ssce_sd_all` |
| 511 | 6 | …naire was distributed to students from Class 6 to university, and schoo… | summary.json | `full_out_of_range`, `n_subject_Other`, `prec_Bjerre-Nielsen et al. 2020_ci[0]` (+29) |
| 511 | 18 | …niversity, and school-age participants under 18 took part without parent… | summary.json | `pct_year_Uni Y4+`, `n_device_Tablet`, `prec_Bjerre-Nielsen et al. 2020_width` (+8) |
| 511 | 7 | …all school-stage responses, the responses of 7 respondents who chose a… | summary.json | `full_uni_school_institution`, `n_gender_Prefer not to say`, `prec_Junco & Cotten 2012_min_r_80` (+19) |
| 513 | 2 | …collected, that the survey would take about 2 – 3 minutes, and that pa… | summary.json | `n_device_Other`, `study_hours_sd_Uni Y2`, `study_hours_ci_Uni Y2[0]` (+51) |
| 513 | 3 | …lected, that the survey would take about 2 – 3 minutes, and that partic… | summary.json | `prec_Rosen et al. 2013_ci[0]`, `study_hours_mean_Uni Y2`, `study_hours_ci_Uni Y2[1]` (+38) |
| 513 | 12 | …espondents confirmed they were students aged 12 years or older (or had p… | summary.json | `prec_Lepp et al. 2015_min_r_80`, `prec_Rosen et al. 2013_halfwidth`, `etg_Uni Y2->Uni Y3_p_holm` (+12) |
| 513 | 18 | …as their institution. They would normally be 18 or older and able to giv… | summary.json | `pct_year_Uni Y4+`, `n_device_Tablet`, `prec_Bjerre-Nielsen et al. 2020_width` (+8) |
| 517 | 171 | …de availability.} The de-identified dataset (171 rows) and the complete r… | summary.json | `n_input_rows`, `N`, `full_analysed` (+20) |
| 517 | 23 | …state were redacted. A flag column marks the 23 responses excluded in th… | summary.json | `prec_Lepp et al. 2015_ci[1]`, `etg_Uni Y3->Uni Y4+_cohen_d`, `r_workload_n_nonacademic` (+6) |
| 517 | 5 | …der and subject are needed for the analyses, 5 respondents remain uniqu… | summary.json | `prec_Lukram et al. 2026_ci[0]`, `screen_mid_ci_Uni Y2[0]`, `study_hours_ci_Uni Y4+[1]` (+24) |
| 519 | 5.5 | …and AI-assisted technologies.} Claude Sonnet 5.5 (Anthropic) was used to… | design | — |
| 519 | 5.5 | …iginal study. For this revision, Claude Opus 5.5 (Anthropic) was used to… | design | — |
