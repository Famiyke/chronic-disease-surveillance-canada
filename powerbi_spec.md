# Project 2 — Power BI Dashboard Spec
## "Canada Chronic Disease Burden Monitor"

### Data Connection
- Source: `ccdss_clean.csv`
- Load via: Get Data → Text/CSV
- Set `year` as whole number, `prevalence` and `incidence` as decimals
- Mark `province` as geographic data type: Province/State → Canada

---

### Page 1 — National Overview

**Visual 1 — Card row (3 cards)**
- Total Conditions Tracked: `DISTINCTCOUNT(ccdss[condition])`
- Latest Year: `MAX(ccdss[year])`
- Avg National Prevalence: `AVERAGE(ccdss[prevalence])` → format `0.0"%"`

**Visual 2 — Line chart: Prevalence trend over time**
- X-axis: `year`
- Y-axis: `AVERAGE(prevalence)`
- Legend: `condition`
- Title: "30-Year Chronic Disease Prevalence Trends"
- Add a constant line at national average

**Visual 3 — Bar chart: Condition ranking**
- Y-axis: `condition`
- X-axis: `AVERAGE(prevalence)` filtered to latest year
- Sort: descending
- Color: single accent — highlight top condition

**Page-level filter:** Year slicer (set default to latest year)

---

### Page 2 — Provincial Analysis

**Visual 1 — Filled Map**
- Location: `province`
- Color saturation: `AVERAGE(prevalence)` in latest year
- Color scale: light yellow → deep red
- Tooltip: Province, Avg Prevalence, Condition breakdown

**Visual 2 — Clustered bar: Province × Condition**
- Y-axis: `province`
- X-axis: `AVERAGE(prevalence)`
- Legend: `condition`
- Sort: by total prevalence descending

**DAX Measure — Atlantic Flag:**
```dax
Atlantic Flag =
IF(
    SELECTEDVALUE(ccdss[province]) IN {"NB","NS","PE","NL"},
    "Atlantic Province",
    "Other Province"
)
```

**Visual 3 — Table: Province scorecard**
Columns: Province, Diabetes%, Hypertension%, COPD%, Mood/Anxiety%, Heart Failure%
Use conditional formatting: green → red scale per column

---

### Page 3 — Age Group Burden

**Visual 1 — Clustered column: Condition by age group**
- X-axis: `age_group`
- Y-axis: `AVERAGE(prevalence)`
- Legend: `condition`
- Filter to latest year

**Visual 2 — Matrix: Condition × Age heatmap**
- Rows: `condition`
- Columns: `age_group`
- Values: `AVERAGE(prevalence)`
- Conditional formatting: data bars

**DAX Measure — Seniors Burden Ratio:**
```dax
Seniors Ratio =
DIVIDE(
    CALCULATE(AVERAGE(ccdss[prevalence]),
              ccdss[age_group] = "75+"),
    CALCULATE(AVERAGE(ccdss[prevalence]),
              ccdss[age_group] = "20-44")
)
```

---

### Page 4 — Trends & Growth

**Visual 1 — Line chart: Each condition trend**
- X-axis: `year`
- Y-axis: `AVERAGE(prevalence)`
- Small multiples by: `condition`

**Visual 2 — Bar chart: % Growth since earliest year**
Use DAX measure:
```dax
Growth Since Baseline =
VAR earliest_yr = MIN(ccdss[year])
VAR latest_yr   = MAX(ccdss[year])
RETURN
DIVIDE(
    CALCULATE(AVERAGE(ccdss[prevalence]),
              FILTER(ccdss, ccdss[year] = latest_yr))
  - CALCULATE(AVERAGE(ccdss[prevalence]),
              FILTER(ccdss, ccdss[year] = earliest_yr)),
    CALCULATE(AVERAGE(ccdss[prevalence]),
              FILTER(ccdss, ccdss[year] = earliest_yr))
) * 100
```

---

### Theme & Colours
| Element | Hex |
|---------|-----|
| Primary | `#1A5276` |
| Accent | `#E74C3C` |
| Positive trend | `#27AE60` |
| Warning | `#F39C12` |
| Background | `#FAFAFA` |
| Grid lines | `#E8E8E8` |
