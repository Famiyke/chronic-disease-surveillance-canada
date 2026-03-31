"""
Project 2 – 01_clean_explore.py
DATA DETECTIVE HAT
Load CCDSS data, profile it, validate age groups,
flag suppressed values, and save a clean file.
"""

import pandas as pd
import numpy as np

FILE = "ccdss_combined.csv"
sep  = "=" * 62

df = pd.read_csv(FILE)

print(f"\n{sep}")
print("  STEP 1: SHAPE AND STRUCTURE")
print(f"{sep}")
print(f"  Rows:       {len(df):,}")
print(f"  Columns:    {list(df.columns)}")

print(f"\n  Conditions: {sorted(df['condition'].unique())}")
print(f"  Provinces:  {sorted(df['province'].unique())}")
print(f"  Age groups: {sorted(df['age_group'].unique())}")
print(f"  Years:      {df['year'].min()} – {df['year'].max()}")

# ── Missing Values ────────────────────────────────────────────────────────────
print(f"\n{sep}")
print("  STEP 2: MISSING VALUES")
print(f"{sep}")

for col in ["prevalence","incidence"]:
    df[col] = pd.to_numeric(
        df[col].astype(str).str.replace("--","").str.replace("F","").str.strip(),
        errors="coerce"
    )

nulls = df.isnull().sum()
if nulls.sum() == 0:
    print("  No missing values.")
else:
    for col, n in nulls[nulls > 0].items():
        print(f"  {col}: {n} missing — suppressed small-cell counts, excluded from analysis")
    df = df.dropna(subset=["prevalence"])

# ── Range Checks ──────────────────────────────────────────────────────────────
print(f"\n{sep}")
print("  STEP 3: RANGE CHECKS")
print(f"{sep}")

for cond in df["condition"].unique():
    sub  = df[df["condition"] == cond]
    lo   = sub["prevalence"].min()
    hi   = sub["prevalence"].max()
    mean = sub["prevalence"].mean()
    print(f"  {cond:<20}  prevalence {lo:.1f}% – {hi:.1f}%  (mean {mean:.1f}%)")

# ── Age Group Coverage ────────────────────────────────────────────────────────
print(f"\n{sep}")
print("  STEP 4: AGE GROUP COVERAGE CHECK")
print(f"{sep}")

expected_ages = {"20-44","45-64","65-74","75+"}
actual_ages   = set(df["age_group"].unique())
missing_ages  = expected_ages - actual_ages
if missing_ages:
    print(f"  Missing age groups: {missing_ages}")
else:
    print("  All age groups present.")

# ── Trend Direction Check ─────────────────────────────────────────────────────
print(f"\n{sep}")
print("  STEP 5: TREND DIRECTION (2010 vs 2022)")
print(f"{sep}")

for cond in sorted(df["condition"].unique()):
    sub = df[df["condition"] == cond]
    r10 = sub[sub["year"] == sub["year"].min()]["prevalence"].mean()
    r22 = sub[sub["year"] == sub["year"].max()]["prevalence"].mean()
    chg = (r22 - r10) / r10 * 100
    arrow = "↑" if chg > 0 else "↓"
    print(f"  {cond:<20}  {r10:.1f}% → {r22:.1f}%  ({arrow} {abs(chg):.0f}%)")

df.to_csv("ccdss_clean.csv", index=False)
print(f"\n  Saved: ccdss_clean.csv  ({len(df):,} rows)")
print(sep)
