-- Project 2: Canadian Chronic Disease Surveillance Analysis
-- 03_sql_queries.sql  —  SQL Programmer Hat
-- Load ccdss_clean.csv as table: ccdss

-- ── 1. National prevalence snapshot, latest year ──────────────────────────────
SELECT
    condition,
    ROUND(AVG(prevalence), 1)       AS avg_prevalence_pct,
    ROUND(AVG(incidence), 1)        AS avg_incidence_pct
FROM ccdss
WHERE year = (SELECT MAX(year) FROM ccdss)
GROUP BY condition
ORDER BY avg_prevalence_pct DESC;

-- ── 2. Province burden ranking ────────────────────────────────────────────────
SELECT
    province,
    ROUND(AVG(prevalence), 1)       AS avg_all_conditions,
    COUNT(DISTINCT condition)       AS conditions_tracked
FROM ccdss
WHERE year = (SELECT MAX(year) FROM ccdss)
GROUP BY province
ORDER BY avg_all_conditions DESC;

-- ── 3. Condition trend over time ──────────────────────────────────────────────
SELECT
    year,
    condition,
    ROUND(AVG(prevalence), 1)       AS national_avg_prevalence
FROM ccdss
GROUP BY year, condition
ORDER BY condition, year;

-- ── 4. Fastest-growing conditions ────────────────────────────────────────────
SELECT
    condition,
    ROUND(AVG(CASE WHEN year = (SELECT MIN(year) FROM ccdss)
                   THEN prevalence END), 1)  AS earliest_prevalence,
    ROUND(AVG(CASE WHEN year = (SELECT MAX(year) FROM ccdss)
                   THEN prevalence END), 1)  AS latest_prevalence,
    ROUND(
        (AVG(CASE WHEN year = (SELECT MAX(year) FROM ccdss)
                  THEN prevalence END)
       - AVG(CASE WHEN year = (SELECT MIN(year) FROM ccdss)
                  THEN prevalence END))
       / AVG(CASE WHEN year = (SELECT MIN(year) FROM ccdss)
                  THEN prevalence END) * 100
    , 1)                                     AS pct_growth
FROM ccdss
GROUP BY condition
ORDER BY pct_growth DESC;

-- ── 5. Age group burden ───────────────────────────────────────────────────────
SELECT
    condition,
    age_group,
    ROUND(AVG(prevalence), 1)        AS avg_prevalence
FROM ccdss
WHERE year = (SELECT MAX(year) FROM ccdss)
GROUP BY condition, age_group
ORDER BY condition, age_group;

-- ── 6. Atlantic vs. Rest of Canada ───────────────────────────────────────────
SELECT
    condition,
    CASE WHEN province IN ('NB','NS','PE','NL')
         THEN 'Atlantic' ELSE 'Rest of Canada' END  AS region,
    ROUND(AVG(prevalence), 1)                       AS avg_prevalence
FROM ccdss
WHERE year = (SELECT MAX(year) FROM ccdss)
GROUP BY condition, region
ORDER BY condition, region;

-- ── 7. Province × condition matrix ───────────────────────────────────────────
SELECT
    province,
    condition,
    ROUND(AVG(prevalence), 1)        AS avg_prevalence
FROM ccdss
WHERE year = (SELECT MAX(year) FROM ccdss)
GROUP BY province, condition
ORDER BY province, condition;

-- ── 8. Seniors burden — conditions spiking in 75+ ────────────────────────────
SELECT
    condition,
    ROUND(AVG(CASE WHEN age_group = '20-44' THEN prevalence END), 1) AS age_20_44,
    ROUND(AVG(CASE WHEN age_group = '45-64' THEN prevalence END), 1) AS age_45_64,
    ROUND(AVG(CASE WHEN age_group = '65-74' THEN prevalence END), 1) AS age_65_74,
    ROUND(AVG(CASE WHEN age_group = '75+'   THEN prevalence END), 1) AS age_75plus,
    ROUND(
        AVG(CASE WHEN age_group = '75+'   THEN prevalence END)
      / AVG(CASE WHEN age_group = '20-44' THEN prevalence END), 1
    )                                                                  AS seniors_vs_young_ratio
FROM ccdss
WHERE year = (SELECT MAX(year) FROM ccdss)
GROUP BY condition
ORDER BY seniors_vs_young_ratio DESC;
