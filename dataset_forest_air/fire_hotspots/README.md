# Fire Hotspots Data — README

Collected by: Ahamed M.U.A.
Department of Computer Science and Engineering, University of Moratuwa
Date: March 2026
Task: Forest Cover & Fire Hotspots — Data Collection

---

## Overview

This folder contains fire hotspot detection data for Sri Lanka from 2001 to 2026,
collected from NASA FIRMS using the MODIS Collection 6.1 sensor.
Each row represents one fire detection event with its location, date, and intensity.
These datasets provide the direct link between slash-and-burn deforestation
and PM2.5 air quality spikes in the FAH Risk Index.

---

## Dataset 4 — NASA FIRMS Fire Hotspots

**Files:**
- `FIRMS_MODIS_C61_SriLanka_2001_2025.csv` — Standard quality archive
- `FIRMS_MODIS_C61_NRT_SriLanka_2026.csv` — Near Real-Time recent data

**Source:** NASA FIRMS (Fire Information for Resource Management System)
**URL:** https://firms.modaps.eosdis.nasa.gov
**Sensor:** MODIS Collection 6.1 (Terra + Aqua satellites)
**Format:** CSV
**Total rows:** 28,414 fire detections (28,348 archive + 66 NRT)
**Coverage:** 2001-03-05 to 2026-03-15

---

## File 1 — FIRMS Archive (Standard Quality)

**File:** `FIRMS_MODIS_C61_SriLanka_2001_2025.csv`
**Rows:** 28,348
**Coverage:** 2001-03-05 to 2025-12-25
**Quality:** Fully verified standard quality data
**Processed by:** University of Maryland with ~3 month lag

---

## File 2 — FIRMS NRT (Near Real-Time)

**File:** `FIRMS_MODIS_C61_NRT_SriLanka_2026.csv`
**Rows:** 66
**Coverage:** 2026-01-04 to 2026-03-15
**Quality:** Near Real-Time — not yet fully verified
**Note:** Will be replaced by standard quality data after ~3 months

---

## Columns (Both Files)

| Column | Description |
|--------|-------------|
| `latitude` | Latitude of fire detection |
| `longitude` | Longitude of fire detection |
| `brightness` | Fire brightness temperature in Kelvin |
| `scan` | Scan pixel size (km) |
| `track` | Track pixel size (km) |
| `acq_date` | Date fire was detected (YYYY-MM-DD) |
| `acq_time` | Time of detection (HHMM UTC) |
| `satellite` | Satellite that detected it (Terra or Aqua) |
| `instrument` | Sensor used (MODIS) |
| `confidence` | Detection confidence (0–100) |
| `version` | MODIS collection version |
| `bright_t31` | Background brightness temperature |
| `frp` | Fire Radiative Power — fire intensity (MW) |
| `daynight` | D = daytime detection, N = nighttime |
| `type` | Fire type (0=presumed vegetation, 1=active volcano, 2=other, 3=offshore) |

*Note: NRT file does not have the `type` column*

---

## Confidence Score Guide

| Confidence | Meaning |
|------------|---------|
| 0 – 30 | Low confidence — possible false alarm |
| 31 – 79 | Nominal confidence — likely fire |
| 80 – 100 | High confidence — confirmed fire |

- Total high confidence fires (80+): **5,070** out of 28,348
- Recommended: use confidence >= 50 for analysis

---

## Fire Radiative Power (FRP) Guide

| FRP (MW) | Fire Intensity |
|----------|---------------|
| 0 – 10 | Low intensity (small fires) |
| 10 – 50 | Moderate intensity |
| 50 – 100 | High intensity |
| 100+ | Extreme intensity (large burns) |

---

## Important Notes on Data Quality

From NASA FIRMS README:
- Some data missing from end of June to July 2001
- 2002 has some missing data throughout
- 2007 has missing data from mid August
- Data missing for 21–22 April 2009
- These gaps should be noted in the methodology section

---

## How This Data Will Be Used in Processing Phase

Currently the data is raw fire point locations (lat/lon). During processing:

```
Step 1: Load fire CSV + Sri Lanka district boundary shapefile
Step 2: Spatial join — assign each fire point to a district
Step 3: Group by district + year → count fires per district per year
Step 4: Calculate total FRP per district per year (fire intensity)
Step 5: Output: 25 districts x 24 years = 600 rows
        Columns: district, year, fire_count, total_frp, burned_area
```

This produces the `fire_intensity_index` feature used in the FAH Risk Index.

---

## How Dataset 4 Connects to Other Datasets

```
Dataset 1 (Forest Loss) ──→ Where trees were cut
Dataset 4 (Fire Hotspots) ─→ Where fires burned (slash-and-burn confirmation)
Dataset 3 (NDVI) ──────────→ Vegetation health dropped after fires

Fire locations overlapping forest loss areas = confirmed slash-and-burn events
These events directly cause PM2.5 spikes → respiratory hospital admissions
```

---

## Key Statistics

- Total fire detections: 28,414
- Coverage: Sri Lanka entire country
- Date range: 2001 to 2026 (25 years)
- Peak fire season: typically June to September (dry zone)
- Highest risk districts: Anuradhapura, Vavuniya, Kurunegala, Moneragala
