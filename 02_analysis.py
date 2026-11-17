"""
Project 2 – 02_analysis.py
PROGRAMMER + STORYTELLER + CONSULTANT HATS
Chronic disease burden analysis: prevalence rankings,
fastest-growing conditions, age burden, provincial gaps.
"""

# PORTFOLIO DATA NOTICE: All computed findings below use simulated/generated
# analytical records, not verified official Canadian statistics. Numeric outputs
# illustrate methods only; any program recommendations require source validation.

import pandas as pd
import numpy as np

df  = pd.read_csv("ccdss_clean.csv")
sep = "=" * 62

print(f"\n{sep}")
print("  PROJECT 2 — CANADIAN CHRONIC DISEASE SURVEILLANCE")
print(f"{sep}\n")

latest_yr = df["year"].max()
early_yr  = df["year"].min()
n_cond    = df["condition"].nunique()
n_prov    = df["province"].nunique()

print(f"  Dataset spans:     {early_yr} – {latest_yr}")
print(f"  Conditions tracked:{n_cond}")
print(f"  Provinces:         {n_prov}")

# ── Latest Year Snapshot ──────────────────────────────────────────────────────
print(f"\n{'─'*62}")
print(f"NATIONAL PREVALENCE SNAPSHOT — {latest_yr}")
print(f"{'─'*62}")

latest = df[df["year"] == latest_yr]
nat = (latest.groupby("condition")["prevalence"]
             .mean().sort_values(ascending=False).reset_index())

print(f"\n  {'Condition':<22} {'Prevalence':>12}")
print(f"  {'─'*22} {'─'*12}")
for _, r in nat.iterrows():
    print(f"  {r['condition']:<22} {r['prevalence']:>11.1f}%")

# ── Province Burden Ranking ───────────────────────────────────────────────────
print(f"\n{'─'*62}")
print(f"PROVINCE BURDEN RANKING — {latest_yr} (avg across conditions)")
print(f"{'─'*62}")

prov = (latest.groupby("province")["prevalence"]
              .mean().sort_values(ascending=False).reset_index())
nat_avg = prov["prevalence"].mean()

print(f"\n  {'Province':>10} {'Avg Prevalence':>16} {'vs National':>13}")
print(f"  {'─'*10} {'─'*16} {'─'*13}")
for _, r in prov.iterrows():
    diff = r["prevalence"] - nat_avg
    flag = " ◄ ABOVE AVG" if diff > 0 else ""
    print(f"  {r['province']:>10} {r['prevalence']:>15.1f}% {diff:>+12.1f}pp{flag}")

# ── Fastest Growing Conditions ────────────────────────────────────────────────
print(f"\n{'─'*62}")
print(f"FASTEST-GROWING CONDITIONS ({early_yr}–{latest_yr})")
print(f"{'─'*62}")

growth = []
for cond in df["condition"].unique():
    sub  = df[df["condition"] == cond]
    r_e  = sub[sub["year"] == early_yr]["prevalence"].mean()
    r_l  = sub[sub["year"] == latest_yr]["prevalence"].mean()
    pct  = (r_l - r_e) / r_e * 100
    pp   = r_l - r_e
    growth.append({"condition": cond, "from": r_e, "to": r_l,
                   "pp_change": pp, "pct_change": pct})

growth_df = pd.DataFrame(growth).sort_values("pct_change", ascending=False)

print(f"\n  {'Condition':<22} {str(early_yr):>6} {str(latest_yr):>6} {'pp Change':>10} {'% Growth':>10}")
print(f"  {'─'*22} {'─'*6} {'─'*6} {'─'*10} {'─'*10}")
for _, r in growth_df.iterrows():
    print(f"  {r['condition']:<22} {r['from']:>5.1f}% {r['to']:>5.1f}%"
          f" {r['pp_change']:>+9.1f}pp {r['pct_change']:>+9.0f}%")

# ── Age Group Burden ──────────────────────────────────────────────────────────
print(f"\n{'─'*62}")
print(f"AGE GROUP BURDEN — {latest_yr}")
print(f"{'─'*62}")

age = (latest.groupby(["condition","age_group"])["prevalence"]
             .mean().unstack().reset_index())

print(f"\n  {'Condition':<22}", end="")
for ag in sorted(df["age_group"].unique()):
    print(f" {ag:>9}", end="")
print()
print(f"  {'─'*22}", end="")
for _ in sorted(df["age_group"].unique()):
    print(f" {'─'*9}", end="")
print()

for _, r in age.iterrows():
    print(f"  {r['condition']:<22}", end="")
    for ag in sorted(df["age_group"].unique()):
        val = r.get(ag, np.nan)
        print(f" {val:>8.1f}%", end="")
    print()

# ── Atlantic vs. National ─────────────────────────────────────────────────────
print(f"\n{'─'*62}")
print("ATLANTIC PROVINCES vs NATIONAL — Chronic Disease Gap")
print(f"{'─'*62}")

atlantic  = ["NB","NS","PE","NL"]
atl_prev  = latest[latest["province"].isin(atlantic)]["prevalence"].mean()
can_prev  = latest["prevalence"].mean()

print(f"\n  Atlantic average prevalence:  {atl_prev:.1f}%")
print(f"  National average:             {can_prev:.1f}%")
print(f"  Atlantic premium:             {atl_prev - can_prev:+.1f} percentage points")

print(f"\n  By condition:")
for cond in sorted(df["condition"].unique()):
    sub    = latest[latest["condition"] == cond]
    atl_c  = sub[sub["province"].isin(atlantic)]["prevalence"].mean()
    can_c  = sub["prevalence"].mean()
    print(f"  {cond:<22} Atlantic {atl_c:.1f}%  National {can_c:.1f}%  gap {atl_c-can_c:+.1f}pp")

# ── Strategic Recommendations ─────────────────────────────────────────────────
print("\\nILLUSTRATIVE INTERPRETATION AND NEXT STEPS")
print("-" * 62)
print("""
These results come from a generated portfolio dataset. They are not
verified Canadian population or health-system estimates.

Potential next steps for a real-world study:
1. Obtain and validate authoritative source data and definitions.
2. Recalculate differences, including denominators and uncertainty.
3. Work with clinical, community or operational partners to assess
   feasibility and avoid treating associations as causal effects.
4. Treat cost differences and savings as sensitivity-tested scenarios,
   not realized outcomes or established policy recommendations.
""")
