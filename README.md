# Forest-Air-Health Data Science Project: Dataset Guide

Welcome to the data repository for our CS3121 project: **"Forest Degradation, Air Quality, and Respiratory Health in Sri Lanka: A District-Level Data Science Analysis"**.

This folder contains all the raw data and reports we have gathered so far. Our goal is to build a unified **district × year panel dataset (2001–2024)** that links environmental degradation to respiratory disease burden across all 25 districts in Sri Lanka.

## 📂 Directory Structure

Our data is grouped into five main pillars:

### 1. `forest_cover/` (Forest Degradation)
- **Hansen Global Forest Change (GFC) v1.12**: Annual tree cover loss (hectares) and gross CO₂ emissions for all 25 districts (2001–2024). This is our primary variable for deforestation.
- **MODIS NDVI**: Normalised Difference Vegetation Index data (2002–2026). Used to calculate 3-year rolling greenness anomalies to capture gradual forest degradation (not just total loss).

### 2. `air_quality/` & `fire_hotspots/` (Air Pollution & Burning)
- **NASA MERRA-2**: 44-year time series of surface PM2.5 concentrations. We will aggregate this gridded data to the district level.
- **Sentinel-5P TROPOMI**: High-resolution (5.5 km) data for NO₂, SO₂, CO, and Aerosol Optical Depth (2018–2024).
- **NASA FIRMS**: Active fire hotspot records (MODIS/VIIRS) from 2000. Used to calculate an annual "fire intensity index" (fire count × estimated burned area) per district.
- *Note: Historical ground-station PM2.5 data for Colombo (Battaramulla/US Embassy) is also available via AQICN.*

### 3. `health_data/` (Respiratory Impacts)
- **MoH Indoor Morbidity and Mortality Reports (IMMR)**: District-level inpatient admissions for 2019, 2020, and 2021 (Excel format).
- Focus areas: Acute respiratory infections, COPD, asthma, and pneumonia admissions per 100,000 population.

### 4. `vehicles_energy/` (Transport & Fossil Fuels)
*We added these to differentiate biomass burning emissions from fossil fuel emissions.*
- **SLSEA Energy Balance Reports (2021–2022)**: Contains a crucial "Demand for Petroleum by District" table (approx. page 65). This gives us district-level petrol/diesel consumption as a proxy for vehicle density.
- **DMT Vehicle Statistics**: National vehicle population and new registrations by fuel type (2010–2025).
- **World Bank Data**: Time series for national CO₂ from transport and fossil fuel electricity generation % (1960–2021).

### 5. `population/` & `admin_boundaries/` (Controls)
- **WorldPop**: 100m gridded population data (2020) for aggregating rates.
- **Household Income and Expenditure Survey (HIES) 2019**: Poverty headcount and firewood usage (important confounders).
- District shapefiles (GADM ADM1) for mapping and joining all data layers.

---

## 🚀 Next Steps for the Group

1. **Extraction**: We need to extract the district-level data from the SLSEA PDFs and MoH IMMR Excel sheets into a clean CSV format.
2. **Harmonisation**: Join all these disparate datasets using the **District ID (GADM ADM1)** and **Year** as the common keys.
3. **Modeling Phase**: Once the single panel tabular dataset is ready, we can begin the XGBoost and Panel Regression modeling as outlined in our Phase 1 proposal (`proposal_forest.tex`).

If you add new data, please ensure it can be aggregated to the **District + Year** level so it fits our panel structure!
