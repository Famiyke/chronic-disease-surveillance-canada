# Real diabetes prevalence data: Nova Scotia, 2000–2022

This project uses **authentic aggregate CCDSS-derived administrative data published by the Government of Nova Scotia**. It is NOT the old synthetic national CCDSS simulation.

**Primary source:** https://data.novascotia.ca/datasets/cumi-sw99

**Source CSV:** https://data.novascotia.ca/api/views/cumi-sw99/rows.csv?accessType=DOWNLOAD

## Descriptive findings

| Metric | Value |
|---|---:|
| Published strata imported | 1,288 |
| Year coverage | 2000–2022 |
| Health zones | 4 |
| Sex groups | 2 |
| Age groups | Seven 10-year bands, age 20+ |
| Nova Scotia 2000 crude diabetes prevalence | 6.56% |
| Nova Scotia 2022 crude diabetes prevalence | 12.43% |
| Difference, 2022 minus 2000 | +5.87 percentage points |

## Computation and limitations

Each year-zone crude prevalence is derived as the sum of published prevalent diabetes cases divided by the sum of published population denominators for the seven mutually exclusive age groups and both sexes, multiplied by 100. Provincial values aggregate all four health zones. **Do not average published subgroup percentages**: aggregation is count-weighted. All 1,288 source-row rates were independently checked against count/population ratios to within 0.015 percentage points, allowing for the publisher's decimal rounding.

- These are **crude estimates**, not age-standardized rates. Changes over time may reflect population aging, case ascertainment and diagnosis patterns as well as disease burden.
- These are Nova Scotia-only records. **Do not treat them as national or cross-provincial findings**.
- The source has no individual patients, patient outcomes or causal variables.
- Differences between zones do not establish differences in healthcare quality or causes of diabetes.
- All source data remain attributed to the Government of Nova Scotia, which describes the dataset as derived from the Canadian Chronic Disease Surveillance System.

## Reproduction

```bash
python official_ns_diabetes.py
```

Outputs: `official_ns_diabetes_2000_2022.csv` and `official_ns_diabetes_zone_2000_2022.csv`. The old synthetic `simulate_ccdss_data.py` workflow is retained separately as an educational example.
