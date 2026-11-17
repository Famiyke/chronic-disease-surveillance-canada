# Power BI dashboard correction specification

**Status: Report pages exist and the PBIX passes container checks, but no visible simulated-data disclosure was found in the report layout.**

## Required corrections in Power BI Desktop

1. Add a high-contrast top banner to each of the four report pages: **SIMULATED DATA — DEMONSTRATION ONLY. NOT VERIFIED PHAC CCDSS ESTIMATES.**
2. Label visual figures and trends as generated, including province comparisons, condition prevalence, growth rate and composite scores.
3. The demonstration data uses age groups that differ from standard CCDSS aggregation. Do not label simulated 20–44/45–64/65–74/75+ comparisons as PHAC's official age-group estimates.
4. Confirm whether each rate is age-standardized, crude or modeled. Include numerators, denominators and time periods in tooltips.
5. Review suppression and small-cell handling. PHAC does not release estimates with small underlying counts according to its methodology.
6. Verify all DAX measures, slicer interactions, filters, report-level relationships, and missing-value treatments.
7. Save, reopen and take screenshots of all four updated pages. The corrected PBIX should replace the GitHub file only after a successful Power BI Desktop open test.

## Validation boundary

Structural inspection found four pages with 6, 3, 2 and 2 visual containers. No simulation-disclosure phrase was found in the serialized report-page layout. This is not an assessment of the report's visual design or numerical validity.
