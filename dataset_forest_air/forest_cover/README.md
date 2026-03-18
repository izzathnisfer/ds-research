# Forest Cover Data — README

Collected by: Ahamed M.U.A.
Department of Computer Science and Engineering, University of Moratuwa
Date: March 2026
Task: Forest Cover & Fire Hotspots — Data Collection

---

## Overview

This folder contains 3 datasets related to forest cover loss, tree cover extent,
and vegetation health across all 25 Sri Lankan districts from 2001 to 2026.
These datasets form the "forest side" of the FAH (Forest-Air-Health) Risk Index.

---

## Dataset 1 — GFW District Forest Loss

**File:** `GFW_SriLanka_DistrictForestLoss_2001_2024.csv`
**Source:** Global Forest Watch (globalforestwatch.org)
**Format:** CSV
**Rows:** 25 (one per district)
**Coverage:** 2001 to 2024

### Columns

| Column | Description |
|--------|-------------|
| `country` | Country name (Sri Lanka) |
| `subnational1` | District name (e.g. Anuradhapura) |
| `threshold` | Tree canopy threshold used (30%) |
| `area_ha` | Total area of district in hectares |
| `extent_2000_ha` | Forest extent in year 2000 (baseline) |
| `extent_2010_ha` | Forest extent in year 2010 |
| `gain_2000-2012_ha` | Forest gained between 2000 and 2012 |
| `tc_loss_ha_2001` to `tc_loss_ha_2024` | Tree cover loss in hectares per year |

### Purpose
- Provides annual forest loss per district for 24 years
- Used to calculate cumulative forest loss fraction feature
- Core input variable for panel regression and XGBoost models
- Identifies highest-loss districts: Anuradhapura (35,510 ha), Kurunegala (21,963 ha)

### Sample Data (Anuradhapura)
- 2001 loss: 390 ha
- 2009 loss: 4,935 ha (peak — slash-and-burn spike)
- 2024 loss: 1,835 ha
- Total area: 720,607 ha

---

## Dataset 2 — GFW District Carbon Data

**File:** `GFW_SriLanka_DistrictCarbonData_2001_2024.csv`
**Source:** Global Forest Watch (globalforestwatch.org)
**Format:** CSV
**Rows:** 25 (one per district)
**Coverage:** 2001 to 2024

### Columns

| Column | Description |
|--------|-------------|
| `country` | Country name |
| `subnational1` | District name |
| `umd_tree_cover_extent_2000__ha` | Forest area baseline in 2000 |
| `gfw_aboveground_carbon_stocks_2000__Mg_C` | Total carbon stored in 2000 |
| `avg_gfw_aboveground_carbon_stocks_2000__Mg_C_ha-1` | Average carbon per hectare |
| `gfw_forest_carbon_gross_emissions__Mg_CO2e_yr-1` | Annual gross CO2 emissions |
| `gfw_forest_carbon_gross_removals__Mg_CO2_yr-1` | Annual carbon removals (regrowth) |
| `gfw_forest_carbon_net_flux__Mg_CO2e_yr-1` | Net carbon flux per year |
| `gfw_forest_carbon_gross_emissions_2001__Mg_CO2e` to `_2024` | CO2 emissions per year |

### Purpose
- Quantifies CO2 released from deforestation per district per year
- Links forest loss directly to atmospheric emissions
- Used as proxy for biomass burning contribution to PM2.5
- Key feature for the FAH Risk Index emission-source attribution

### Sample Data (Anuradhapura)
- Carbon stocks 2000: 17.5 million Mg C
- 2009 CO2 emissions: 1.3 million Mg CO2e (peak year)
- Net flux: -512,702 Mg CO2e/yr (net carbon loss)
- Average carbon density: 187 Mg C/ha

---

## Dataset 3 — MODIS NDVI Vegetation Health

**File:** `MODIS_NDVI_SriLanka_Subnational_2002_2026.csv`
**Source:** OCHA Humanitarian Data Exchange (data.humdata.org)
**Satellite:** MODIS Terra and Aqua (NASA)
**Format:** CSV
**Rows:** 28,968
**Coverage:** July 2002 to February 2026 (every 10 days)

### Columns

| Column | Description |
|--------|-------------|
| `date` | Date of reading (every 10 days) |
| `adm_level` | Administrative level (1=province, 2=district) |
| `adm_id` | Internal administrative ID |
| `PCODE` | District code (LK11=Colombo, LK21=Kandy etc.) |
| `n_pixels` | Number of satellite pixels covering the area |
| `vim` | NDVI score — vegetation health (main variable) |
| `vim_avg` | Smoothed average NDVI |
| `viq` | Data quality score (higher = more reliable) |

### NDVI Score Interpretation

| Score | Meaning |
|-------|---------|
| 0.6 – 1.0 | Dense healthy forest |
| 0.3 – 0.6 | Moderate vegetation |
| 0.1 – 0.3 | Sparse or degraded vegetation |
| Below 0.1 | Bare land or burned area |

### PCODE Reference (Districts only — use adm_level=2)
LK11=Colombo, LK12=Gampaha, LK13=Kalutara,
LK21=Kandy, LK22=Matale, LK23=Nuwara Eliya,
LK31=Galle, LK32=Matara, LK33=Hambantota,
LK41=Jaffna, LK42=Mannar, LK43=Vavuniya, LK44=Mullaitivu, LK45=Kilinochchi,
LK51=Batticaloa, LK52=Ampara, LK53=Trincomalee,
LK61=Kurunegala, LK62=Puttalam,
LK71=Anuradhapura, LK72=Polonnaruwa,
LK81=Badulla, LK82=Moneragala,
LK91=Ratnapura, LK92=Kegalle

### Purpose
- Tracks ongoing vegetation health every 10 days
- Detects degradation between major deforestation events
- Used to derive: vegetation degradation rate and greenness anomaly features
- Complements Hansen GFC — captures slow degradation not visible as full loss
- NDVI drop after fire event confirms fire damage to vegetation

### Notes
- Use only rows where `adm_level = 2` for district-level analysis
- Rows where `adm_level = 1` are province-level summaries
- Missing data in some periods — check `viq` column for quality

---

## How These 3 Datasets Connect

```
Dataset 1 (Forest Loss) ──→ How much forest was cut
Dataset 2 (Carbon Data) ──→ How much CO2 was released
Dataset 3 (NDVI)        ──→ How healthy the vegetation is over time

All three together ──→ Complete picture of forest degradation
                   ──→ Input to FAH Risk Index and ML model
```

---

## Original Source Files

The original Excel file with all 7 sheets is also kept in this folder:
- `GFW_SriLanka_DistrictForestLoss_2001_2024.xlsx`

Sheets included:
1. Read_Me
2. Country tree cover loss
3. Country carbon data
4. Subnational 1 tree cover loss ← source of Dataset 1
5. Subnational 1 carbon data ← source of Dataset 2
6. Subnational 2 tree cover loss (sub-district level)
7. Subnational 2 carbon data (sub-district level)
