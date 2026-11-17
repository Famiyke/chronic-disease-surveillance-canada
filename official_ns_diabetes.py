"""Build official Nova Scotia diabetes surveillance summary from published data.

Source: Government of Nova Scotia Open Data, CCDSS-derived diabetes crude prevalence.
Socrata dataset ID: cumi-sw99.
https://data.novascotia.ca/datasets/cumi-sw99

This is REAL aggregated administrative surveillance data for NOVA SCOTIA only.
Age scope is 20 years and older. Rates are crude, not age-standardized.
It does not contain confidential records or fictional simulation parameters.
"""
import csv
import io
from collections import defaultdict
from pathlib import Path
from urllib.request import Request, urlopen

URL = "https://data.novascotia.ca/api/views/cumi-sw99/rows.csv?accessType=DOWNLOAD"
ZONE_OUT = Path("official_ns_diabetes_zone_2000_2022.csv")
PROVINCE_OUT = Path("official_ns_diabetes_2000_2022.csv")
REPORT = Path("OFFICIAL_NS_DIABETES_FINDINGS.md")
AGE_BANDS = ["20 to 29", "30 to 39", "40 to 49", "50 to 59",
             "60 to 69", "70 to 79", "80 +"]


def write_table(path, items):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(items[0]))
        writer.writeheader()
        writer.writerows(items)


def main():
    request = Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=50) as response:
        raw = response.read()
    records = list(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))))
    expected_cols = {"Year", "Zone", "Sex", "Agegroup", "Population",
                     "Prevalence", "Crude Prevalence Rate"}
    assert records and expected_cols.issubset(records[0]), "Source schema changed"
    assert len(records) == 23 * 4 * 2 * 7, "Expected full 2000–2022 zone-sex-age cube"
    unique = set()
    zone_counts = defaultdict(lambda: [0, 0])
    province_counts = defaultdict(lambda: [0, 0])
    for row in records:
        year = int(row["Year"])
        zone = row["Zone"]
        sex = row["Sex"]
        age = row["Agegroup"]
        key = (year, zone, sex, age)
        assert key not in unique, f"Duplicate published stratum: {key}"
        unique.add(key)
        assert 2000 <= year <= 2022
        assert sex in ("F", "M") and age in AGE_BANDS
        population = int(row["Population"].replace(",", ""))
        count = int(row["Prevalence"].replace(",", ""))
        rate = float(row["Crude Prevalence Rate"])
        assert population > 0 and 0 <= count <= population
        assert abs(100 * count / population - rate) <= 0.015, key
        zone_counts[(year, zone)][0] += count
        zone_counts[(year, zone)][1] += population
        province_counts[year][0] += count
        province_counts[year][1] += population

    assert sorted(province_counts) == list(range(2000, 2023))
    assert len(zone_counts) == 23 * 4
    zone_rows = []
    for (year, zone), (count, pop) in sorted(zone_counts.items()):
        zone_rows.append({
            "year": year, "health_zone": zone, "age_scope": "20+",
            "diabetes_prevalent_count": count, "population": pop,
            "crude_diabetes_prevalence_percent": round(100 * count / pop, 4),
            "source_dataset": "Nova Scotia Open Data cumi-sw99 / CCDSS",
            "source_url": URL
        })
    province_rows = []
    for year, (count, pop) in sorted(province_counts.items()):
        province_rows.append({
            "year": year, "geography": "Nova Scotia", "age_scope": "20+",
            "diabetes_prevalent_count": count, "population": pop,
            "crude_diabetes_prevalence_percent": round(100 * count / pop, 4),
            "source_dataset": "Nova Scotia Open Data cumi-sw99 / CCDSS",
            "source_url": URL
        })
    write_table(ZONE_OUT, zone_rows)
    write_table(PROVINCE_OUT, province_rows)
    first, last = province_rows[0], province_rows[-1]
    report = f"""# Real diabetes prevalence data: Nova Scotia, 2000–2022

This project uses **authentic aggregate CCDSS-derived administrative data published by the Government of Nova Scotia**. It is NOT the old synthetic national CCDSS simulation.

**Primary source:** https://data.novascotia.ca/datasets/cumi-sw99

**Source CSV:** {URL}

## Descriptive findings

| Metric | Value |
|---|---:|
| Published strata imported | {len(records):,} |
| Year coverage | 2000–2022 |
| Health zones | 4 |
| Sex groups | 2 |
| Age groups | Seven 10-year bands, age 20+ |
| Nova Scotia 2000 crude diabetes prevalence | {first['crude_diabetes_prevalence_percent']:.2f}% |
| Nova Scotia 2022 crude diabetes prevalence | {last['crude_diabetes_prevalence_percent']:.2f}% |
| Difference, 2022 minus 2000 | {last['crude_diabetes_prevalence_percent']-first['crude_diabetes_prevalence_percent']:+.2f} percentage points |

## Computation and limitations

Each year-zone crude prevalence is derived as the sum of published prevalent diabetes cases divided by the sum of published population denominators for the seven mutually exclusive age groups and both sexes, multiplied by 100. Provincial values aggregate all four health zones. **Do not average published subgroup percentages**: aggregation is count-weighted. All {len(records):,} source-row rates were independently checked against count/population ratios to within 0.015 percentage points, allowing for the publisher's decimal rounding.

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
"""
    REPORT.write_text(report, encoding="utf-8")
    print(f"PASS: {len(records)} official source strata and {len(zone_rows)} zone-years")
    print(f"Nova Scotia crude prevalence 2000: {first['crude_diabetes_prevalence_percent']:.2f}%")
    print(f"Nova Scotia crude prevalence 2022: {last['crude_diabetes_prevalence_percent']:.2f}%")
    print(f"Wrote {PROVINCE_OUT}, {ZONE_OUT} and {REPORT}")


if __name__ == "__main__":
    main()
