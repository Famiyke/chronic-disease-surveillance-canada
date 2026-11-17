# Project 2: Canadian Chronic Disease Surveillance Analysis

> **DATA PROVENANCE:** This portfolio project uses simulated records informed by named Canadian public sources. All generated statistics, rankings, demographic differences, and savings models are illustrative rather than verified official estimates. Recommendations are hypothetical scenarios, not observed effects.

**Domain:** Epidemiology / Public Health
**Tools:** Python · SQL · Power BI
**Public reference source (distinct from simulated analysis data):** CCDSS Data Tool — Public Health Agency of Canada
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

## Illustrative analytical outputs

This project's Python/SQL outputs illustrate data processing, comparisons, modeling and reporting using generated records. The specific rates, rankings, cost figures and trends in the demonstration are **not verified official findings**. See the analysis scripts for the computations and the data limitations section below for interpretation requirements.

## Live Dashboard

Power BI dashboard built in Power BI Desktop.

**Download:** `canada_chronic_disease_burden_monitor.pbix` from this repo and open in Power BI Desktop to interact with the full report.

**Dashboard pages:**
- Page 1 — National Overview: condition trend lines, prevalence ranking, year slicer
- Page 2 — Provincial Analysis: filled map, province × condition clustered bar, scorecard table
- Page 3 — Age Group Burden: condition by age column chart, condition × age heat map
- Page 4 — Trends and Growth: small multiples trend lines, % growth since 2010 bar chart

See `dashboard.md` for screenshots and key visual findings.

---

## Interpretation and real-world next steps

Use the simulated findings to demonstrate analytical methods, not to rank actual jurisdictions or recommend clinical or policy interventions. A real decision requires matched official data, documented definitions, relevant uncertainty, and clinical or operational stakeholder review. Financial scenarios must include assumptions, costs and sensitivity analysis.

## Files

| File | Purpose |
|------|---------|
| `simulate_ccdss_data.py` | Builds representative dataset from published CCDSS provincial prevalence rates |
| `01_clean_explore.py` | Load, merge, profile — Data Detective. Handles suppression codes, range checks, age coverage, trend validation |
| `02_analysis.py` | National snapshot, province ranking, growth rates, age burden, Atlantic comparison, recommendations |
| `03_sql_queries.sql` | 8 SQL queries covering prevalence, growth, age burden, and Atlantic comparison |
| `canada_chronic_disease_burden_monitor.pbix` | Power BI workbook — download and open in Power BI Desktop |
| `dashboard.md` | Dashboard screenshots and key visual findings |
| `prevention_brief.md` | One-page plain-language brief for a public health director |

---

## Data Provenance and Limitations

Check all numerator, denominator, year and age adjustment definitions before comparison. The stated 12.3% (NL) and 11.8% (NB) are below, not above, the stated 13.7% national diabetes rate. The mood/anxiety growth figures differ between the repository and homepage. Neither rate is independently verified. All rankings, model-generated prevalence changes and cost-savings claims are illustrative.

The CCDSS publishes aggregate surveillance tables via an interactive web tool. Individual patient records are not publicly available. This project uses simulated data anchored to published CCDSS provincial prevalence figures. The analytical methodology reflects the approach used in real public health surveillance roles.

---

## Screenshots

![Provincial Analysis](https://github.com/user-attachments/assets/3a370e0d-5462-4f0d-b3b6-049e6132380e)

![National Overview](https://github.com/user-attachments/assets/4f997be0-8a12-45e1-ad8d-eb92e6dbfd93)

![Age Group Burden](https://github.com/user-attachments/assets/9efd0c9b-6e9c-4b64-97ef-b3d9df7e194d)

![Trend and Analysis](https://github.com/user-attachments/assets/6b0a5aed-fbae-40f5-b209-fd8722c18b2a)

---

## Reproducibility and execution status

**Environment:** Python 3 with `pandas` and `numpy` installed. If working with the Excel files, install `openpyxl` as needed. Run the simulation script before the analysis commands shown above.

**Important:** The scripts are designed for the generated datasets and expected column names. Downloading a public government table does **not** guarantee that it will run with these scripts unchanged; a schema-mapping and validation step is required for authentic external data. The repository has undergone a static documentation and code-reference audit, but a fresh environment execution and independent reconciliation with official datasets have not yet been completed.

