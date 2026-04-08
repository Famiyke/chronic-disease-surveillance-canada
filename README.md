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
| `dashboard.md` | Built in Power BI Desktop. Download the .pbix file to interact with the full report|<img width="3427" height="1326" alt="Provincial Analysis" src="https://github.com/user-attachments/assets/3a370e0d-5462-4f0d-b3b6-049e6132380e" />
<img width="3428" height="1389" alt="National Overview" src="https://github.com/user-attachments/assets/4f997be0-8a12-45e1-ad8d-eb92e6dbfd93" />
<img width="3428" height="1386" alt="Age Group Burden" src="https://github.com/user-attachments/assets/6b0a5aed-fbae-40f5-b209-fd8722c18b2a" />
<img width="3439" height="1386" alt="Trend and Analysis" src="https://github.com/user-attachments/assets/9efd0c9b-6e9c-4b64-97ef-b3d9df7e194d" />
| `prevention_brief.md` | Plain-language brief for a public health director |
