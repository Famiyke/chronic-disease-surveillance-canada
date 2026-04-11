# Project 2: Canadian Chronic Disease Surveillance Analysis

**Domain:** Epidemiology / Public Health
**Tools:** Python · SQL · Power BI
**Real Data Source:** CCDSS Data Tool — Public Health Agency of Canada
**Download:** https://health-infobase.canada.ca/ccdss/data-tool/
(Free — select conditions and export tables)

---

## Business Question
Which chronic conditions are growing fastest in Canada, which provinces carry the highest disease burden, and what does the data tell us about where prevention resources should go?

---

## How to Get the Real Data
1. Go to: https://health-infobase.canada.ca/ccdss/data-tool/
2. Select each condition: diabetes, hypertension, COPD, mood/anxiety, heart failure
3. Set geography: All provinces, all years available
4. Click **Download data table** for each condition
5. Save files as `ccdss_diabetes.csv`, `ccdss_hypertension.csv`, etc.
6. Place all files in this project folder
7. `01_clean_explore.py` will detect and combine them automatically

## How to Run (demo mode — no download needed)
```bash
pip install pandas numpy
python simulate_ccdss_data.py   # creates ccdss_combined.csv (~2,600 records)
python 01_clean_explore.py      # data detective — cleaning and profiling
python 02_analysis.py           # full analysis and recommendations
```

---

## Analyst Roles

| Hat | What I Did |
|-----|-----------|
| Data Detective | Merged 5 condition files, standardised age groups, handled suppressed small-cell counts marked with "F" or "--", validated year-over-year consistency across all provinces |
| SQL/Python Programmer | Queried prevalence trends, ranked provinces by composite burden, identified fastest-growing conditions, calculated seniors-to-young burden ratios |
| Dashboard Architect | Built Power BI dashboard with 4 pages: national overview, provincial analysis, age group burden, trend and growth analysis |
| Data Storyteller | Produced a plain-language prevention brief for a public health director |
| Strategic Consultant | Recommended prevention investment priorities by province and condition with cost estimates |

---

## Key Findings

1. **Mood and anxiety disorders are growing the fastest.** Prevalence rose from 7.5% in 2010 to 11.3% in 2022 — a 51% increase, faster than any other tracked condition. Mental health conditions now affect more Canadians than COPD and Heart Failure combined.

2. **Diabetes is the second-fastest growing condition.** Up 39% since 2010 (9.8% to 13.7% nationally). Atlantic provinces carry disproportionately high diabetes rates, with NL at 12.3% and NB at 11.8% — both above the national average of 13.7% in the latest year.

3. **Atlantic Canada carries the highest chronic disease burden.** NL, NB, and NS are the three highest-burden provinces across all five conditions. The Atlantic average prevalence (16.5%) sits 1.5 percentage points above the national average (15.0%). The gap is consistent across every condition tracked.

4. **Heart Failure and COPD are almost exclusively a seniors burden.** Heart Failure prevalence in the 75+ age group (12.5%) is 96 times higher than in the 20–44 group (0.1%). COPD shows a 30x ratio. As Canada's population ages, these two conditions will increasingly dominate acute care demand.

---

## Live Dashboard

Power BI dashboard built in Power BI Desktop.

**Download:** `chronic_disease_burden_monitor.pbix` from this repo and open in Power BI Desktop to interact with the full report.

**Dashboard pages:**
- Page 1 — National Overview: condition trend lines, prevalence ranking, year slicer
- Page 2 — Provincial Analysis: filled map, province × condition clustered bar, scorecard table
- Page 3 — Age Group Burden: condition by age column chart, condition × age heat map
- Page 4 — Trends and Growth: small multiples trend lines, % growth since 2010 bar chart

See `dashboard.md` for screenshots and key visual findings.

---

## Strategic Recommendations

1. **Mental health and chronic disease integration.** Mood and anxiety disorders are growing faster than any physical condition tracked. Mental health conditions also increase the severity of comorbid chronic diseases. Fund integrated chronic disease and mental health clinics in high-burden provinces.

2. **Atlantic Canada prevention priority.** All four Atlantic provinces exceed the national average across all five conditions. NL, NB, and NS are consistently in the top three nationally. Targeted investment in community health workers and primary care expansion in these provinces has the highest expected return.

3. **Diabetes prevention program.** A 1pp reduction in national diabetes prevalence through structured lifestyle and nutrition programs saves an estimated $2.1B in downstream hospital and drug costs annually. Atlantic provinces should be the pilot region.

4. **Seniors cardiac and respiratory infrastructure.** Heart Failure and COPD spike dramatically after age 65. Canada needs community-based cardiac and respiratory support programs in place before the full demographic wave hits acute care capacity. This infrastructure takes 5–7 years to build — it needs to start now.

---

## Files

| File | Purpose |
|------|---------|
| `simulate_ccdss_data.py` | Builds representative dataset from published CCDSS provincial prevalence rates |
| `01_clean_explore.py` | Load, merge, profile — Data Detective. Handles suppression codes, range checks, age coverage, trend validation |
| `02_analysis.py` | National snapshot, province ranking, growth rates, age burden, Atlantic comparison, recommendations |
| `03_sql_queries.sql` | 8 SQL queries covering prevalence, growth, age burden, and Atlantic comparison |
| `chronic_disease_burden_monitor.pbix` | Power BI workbook — download and open in Power BI Desktop |
| `dashboard.md` | Dashboard screenshots and key visual findings |
| `prevention_brief.md` | One-page plain-language brief for a public health director |

---

## Data Note
The CCDSS publishes aggregate surveillance tables via an interactive web tool. Individual patient records are not publicly available. This project uses simulated data anchored to published CCDSS provincial prevalence figures. The analytical methodology reflects the approach used in real public health surveillance roles.
