# Project 2: Canadian Chronic Disease Surveillance Analysis

> **PROJECT VALIDATION STATUS:** The Python demonstration workflow has passed GitHub Actions. Generated model parameters and subgroup comparisons are synthetic. No synthetic values should be described as verified official health-system statistics. See [SOURCE_VALIDATION.md](SOURCE_VALIDATION.md) for the evidence boundary.\n\n
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
7. Build a separate schema-mapping/import script for authentic PHAC files. `01_clean_explore.py` reads the synthetic `ccdss_combined.csv` output and does not automatically combine official exports.

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
| Data Detective | Cleaned simulated condition data, checked generated age groups and reviewed missing-value handling |
| SQL/Python Programmer | Queried prevalence trends, ranked provinces by composite burden, identified fastest-growing conditions, calculated seniors-to-young burden ratios |
| Dashboard Architect | Built Power BI dashboard with 4 pages: national overview, provincial analysis, age group burden, trend and growth analysis |
| Data Storyteller | Produced a plain-language prevention brief for a public health director |
| Scenario interpretation | Discussed illustrative planning questions without treating model estimates as actual provincial priorities |

---

## Illustrative analytical outputs

This project's Python/SQL outputs illustrate data processing, comparisons, modeling and reporting using generated records. The specific rates, rankings, cost figures and trends in the demonstration are **not verified official findings**. See the analysis scripts for the computations and the data limitations section below for interpretation requirements.

## Power BI demonstration status

The `canada_chronic_disease_burden_monitor.pbix` file is an **archived synthetic-data demonstration**. The present four report pages do not yet display prominent simulated-data labels. Do not use the numbers to evaluate actual Canadian disease rates. The corrected code and validation notes remain available.

See [DASHBOARD_CORRECTION_GUIDE.md](DASHBOARD_CORRECTION_GUIDE.md) for the required Power BI Desktop changes before publication. Historical dashboard screenshots are preserved for issue tracking but are not promoted as validated reporting.

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

## Historical screenshots

Older screenshot links have been removed from the public README until the PBIX carries explicit simulated-data labels and its calculations have been reviewed.

---

## Reproducibility and execution status

**Environment:** Python 3 with `pandas` and `numpy` installed. If working with the Excel files, install `openpyxl` as needed. Run the simulation script before the analysis commands shown above.

**Important:** The scripts are designed for the generated datasets and expected column names. Downloading a public government table does **not** guarantee that it will run with these scripts unchanged; a schema-mapping and validation step is required for authentic external data. The generated-data Python workflow passed a clean GitHub Actions execution test. Independent reconciliation against authoritative population or healthcare source files remains incomplete.

