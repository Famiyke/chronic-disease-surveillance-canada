"""
Project 2 – simulate_ccdss_data.py
Builds a representative chronic disease dataset
from published CCDSS prevalence figures (2010–2022).
Real data: https://health-infobase.canada.ca/ccdss/data-tool/
"""

import pandas as pd
import numpy as np

np.random.seed(2)

PROVINCES = ["BC","AB","SK","MB","ON","QC","NB","NS","PE","NL"]

# Published CCDSS prevalence rates (%) by condition — latest year available
# Source: PHAC CCDSS data tool, 2022 estimates
BASE_PREVALENCE = {
    "Diabetes":          {"BC":9.1,"AB":9.8,"SK":10.6,"MB":11.2,"ON":9.6,
                          "QC":8.4,"NB":11.8,"NS":11.4,"PE":11.1,"NL":12.3},
    "Hypertension":      {"BC":20.1,"AB":19.4,"SK":21.8,"MB":22.3,"ON":20.8,
                          "QC":18.6,"NB":23.4,"NS":23.1,"PE":22.8,"NL":24.6},
    "COPD":              {"BC":5.8,"AB":5.4,"SK":6.2,"MB":6.4,"ON":5.9,
                          "QC":5.1,"NB":7.1,"NS":7.4,"PE":6.8,"NL":8.1},
    "Mood/Anxiety":      {"BC":14.2,"AB":13.8,"SK":13.1,"MB":14.6,"ON":14.0,
                          "QC":13.4,"NB":15.8,"NS":15.6,"PE":14.9,"NL":16.2},
    "Heart Failure":     {"BC":2.1,"AB":2.0,"SK":2.3,"MB":2.5,"ON":2.2,
                          "QC":1.9,"NB":2.8,"NS":2.9,"PE":2.6,"NL":3.1},
}

# Annual growth rates by condition (%) — from CCDSS trend reports
ANNUAL_GROWTH = {
    "Diabetes":      0.028,
    "Hypertension":  0.018,
    "COPD":          0.012,
    "Mood/Anxiety":  0.035,
    "Heart Failure": 0.022,
}

AGE_GROUPS = ["20-44","45-64","65-74","75+"]
AGE_MULT = {
    "Diabetes":      [0.30, 1.00, 1.80, 2.10],
    "Hypertension":  [0.20, 1.00, 2.20, 2.80],
    "COPD":          [0.10, 1.00, 2.50, 3.00],
    "Mood/Anxiety":  [0.80, 1.00, 0.70, 0.60],
    "Heart Failure": [0.05, 1.00, 3.20, 5.10],
}

YEARS = list(range(2010, 2023))

rows = []
for condition in BASE_PREVALENCE:
    growth = ANNUAL_GROWTH[condition]
    for prov in PROVINCES:
        base_2022 = BASE_PREVALENCE[condition][prov]
        for i, year in enumerate(YEARS):
            # Back-calculate from 2022 base
            years_back = 2022 - year
            prev_rate  = base_2022 / ((1 + growth) ** years_back)
            prev_rate += np.random.normal(0, 0.08)
            prev_rate  = max(0.5, round(prev_rate, 2))

            for j, age in enumerate(AGE_GROUPS):
                age_prev = round(prev_rate * AGE_MULT[condition][j]
                                 + np.random.normal(0, 0.05), 2)
                rows.append({
                    "year":        year,
                    "province":    prov,
                    "condition":   condition,
                    "age_group":   age,
                    "prevalence":  max(0.1, age_prev),
                    "incidence":   round(age_prev * 0.12 + np.random.normal(0, 0.03), 2),
                })

df = pd.DataFrame(rows)
df.to_csv("ccdss_combined.csv", index=False)
print(f"Created ccdss_combined.csv  —  {len(df):,} rows")
print(f"Conditions: {sorted(df['condition'].unique())}")
print(f"Provinces:  {sorted(df['province'].unique())}")
print(f"Years:      {df['year'].min()}–{df['year'].max()}")
