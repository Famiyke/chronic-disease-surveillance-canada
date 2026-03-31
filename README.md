# Project 2: Canadian Chronic Disease Surveillance Analysis

**Domain:** Epidemiology / Public Health  
**Tools:** Python · SQL · Power BI  
**Real Data Source:** CCDSS Data Tool — Public Health Agency of Canada  
**Download:** https://health-infobase.canada.ca/ccdss/data-tool/  
(Free — use the tool to select conditions and export tables)

---

## Business Question
Which chronic conditions are growing fastest in Canada, which provinces carry the highest disease burden, and what does the data tell us about where prevention resources should go?

---

## How to Get the Real Data
1. Go to: https://health-infobase.canada.ca/ccdss/data-tool/
2. Select each condition (diabetes, hypertension, COPD, mood/anxiety, heart failure)
3. Set geography: All provinces, all years available
4. Click **Download data table** for each condition
5. Save files as `ccdss_diabetes.csv`, `ccdss_hypertension.csv`, etc.
6. Place all files in this project folder
7. `01_load_clean.py` will detect and combine them automatically

## How to Run (demo mode — no download needed)
```bash
pip install pandas numpy openpyxl
python simulate_ccdss_data.py   # creates ccdss_combined.csv
python 01_clean_explore.py      # data detective
python 02_analysis.py           # full analysis
```

---

## Analyst Roles

| Hat | What I Did |
|-----|-----------|
| Data Detective | Merged 5 condition files, standardised age groups, handled suppressed small-cell counts |
| SQL/Python Programmer | Queried prevalence trends, ranked provinces, identified fastest-growing conditions |
| Dashboard Architect | Built Power BI dashboard: condition trend lines + province map + age pyramid |
| Data Storyteller | Produced a plain-language public health brief |
| Strategic Consultant | Recommended prevention investment priorities by province and condition |

---

## Files

| File | Purpose |
|------|---------|
| `simulate_ccdss_data.py` | Builds representative dataset from published CCDSS figures |
| `01_clean_explore.py` | Load, merge, profile — Data Detective |
| `02_analysis.py` | Prevalence trends, rankings, burden analysis |
| `03_sql_queries.sql` | All key queries in SQL |
| `powerbi_spec.md` | Power BI dashboard build guide with DAX measures |
| `prevention_brief.md` | Plain-language brief for a public health director |
