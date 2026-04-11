# Canada Chronic Disease Burden Monitor — Power BI Dashboard

**File:** `chronic_disease_burden_monitor.pbix`
**Tool:** Power BI Desktop (free download at microsoft.com/powerbi)
**Data:** `ccdss_clean.csv` — 2,600 records, 5 conditions, 10 provinces, 4 age groups, 2010–2022

## How to Open
1. Download `chronic_disease_burden_monitor.pbix` from this repo
2. Open Power BI Desktop
3. File → Open → select the .pbix file
4. The dashboard loads with all 4 pages ready to explore

---

## Dashboard Pages

### Page 1 — National Overview
Three KPI cards showing conditions tracked, latest data year, and average national prevalence. A line chart shows 30-year prevalence trends for all five conditions simultaneously, making the Mood/Anxiety growth curve immediately visible against the others. A bar chart ranks conditions by latest-year prevalence. Year slicer filters all visuals.

### Page 2 — Provincial Analysis
A filled map of Canada colour-coded by average chronic disease prevalence — Atlantic provinces appear darker. A clustered bar chart breaks down each province by condition. A province scorecard table uses conditional formatting (green to red) to show at a glance which provinces are above or below national benchmarks on each condition.

### Page 3 — Age Group Burden
A clustered column chart shows how each condition distributes across the four age groups. The Heart Failure and COPD columns show near-zero values for 20–44 and then a dramatic spike at 75+. A condition × age heat map uses data bars to encode the same pattern in matrix form.

### Page 4 — Trends and Growth
Small multiples line chart shows each condition's trend line independently, making individual growth patterns clearer than the overlapping lines on Page 1. A bar chart ranks conditions by percentage growth since 2010 — Mood/Anxiety and Diabetes are the standout bars.

---

## Key Visual Findings

- The Mood/Anxiety trend line on Page 1 is steeper than any other condition since 2015
- Atlantic provinces are visibly darker on the Page 2 map — the geographic pattern is immediately clear
- The Heart Failure 75+ column on Page 3 towers over all other age groups — a 96x ratio
- The Page 4 growth bar chart shows Mood/Anxiety (51%) and Diabetes (39%) clearly separated from the other three conditions

---

## Screenshots

![Provincial Analysis](https://github.com/user-attachments/assets/3a370e0d-5462-4f0d-b3b6-049e6132380e)

![National Overview](https://github.com/user-attachments/assets/4f997be0-8a12-45e1-ad8d-eb92e6dbfd93)

![Age Group Burden](https://github.com/user-attachments/assets/9efd0c9b-6e9c-4b64-97ef-b3d9df7e194d)

![Trend and Analysis](https://github.com/user-attachments/assets/6b0a5aed-fbae-40f5-b209-fd8722c18b2a)
