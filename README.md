# Screen-to-Study Conversion Efficiency (SSCE) among university students
### Reproducible analysis pipeline
**Author:** Raheeb Sadman · BRAC University, Dhaka, Bangladesh

---

## About

This repository contains the data and analysis code for a study of how
university students in Bangladesh convert screen time into study time. It
lets anyone reproduce every statistic, table and figure in the manuscript.

The shared data contain only respondents who reported being in their second,
third, or fourth or later year of college or university and who chose a
college or university as their institution type (n = 171).

- **Excluded from the data:** all school-stage responses (Class 6 to
  Class 12), all first-year responses, and responses whose reported stage and
  institution conflicted. None of these are shared or analysed.
- **No identifiers:** the file contains no names, contact details, student
  IDs, institution names, timestamps or email addresses.

The study did not receive ethics committee review. The manuscript's
Statements and Declarations and its Limitations section report the consent
procedure and ethical basis in full.

---

## Repository structure

```
├── README.md
├── data/
│   └── SSCE_survey_university.csv   <- university Years 2-4+ (n = 171); last column
│                                       cluster_sensitivity_flag is not a survey item
├── docs/                            <- verification table and change reports
├── figures/university/              <- figures as they appear in the manuscript (PNG)
├── outputs/                         <- created when the script runs (not tracked)
└── scripts/
    └── university_analysis.py       <- reproduces every number and figure in the manuscript
```

---

## How to reproduce

### Requirements
```
Python >= 3.9
pip install pandas numpy scipy statsmodels scikit-learn matplotlib
```

### Command
Run from the repository root:

```bash
git clone https://github.com/Raheeb223/SSCE_repository.git
cd SSCE_repository
python scripts/university_analysis.py
```

Outputs:
- `outputs/university/`: `RESULTS.txt`, `summary.json`, tables (`table_*.csv`)
  and the coded open-text responses
- `figures/university/`: figures (300 dpi)

All random steps use seed `20260618`, so every run gives the same numbers.
`docs/verification_table.md` maps each statistic in the manuscript to its
`summary.json` key.

The manuscript describes how the analytic sample was drawn from the original
survey, and reports a comparison that includes first-year students. These
steps need the original survey file, which is not shared because it contains
responses from school-age participants. Without that file the script skips
them and reproduces all other results.

---

## License

MIT License. The survey data are shared here for academic reproducibility.
