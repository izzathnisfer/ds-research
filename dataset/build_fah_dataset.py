from pathlib import Path

import pandas as pd

# Paths relative to this script
DATA_DIR = Path(__file__).resolve().parent


def load_fire(path: Path) -> pd.DataFrame:
    fire = pd.read_csv(path)
    fire['nearest_district'] = fire['nearest_district'].str.strip()
    fire['year_month'] = fire['year_month'].str.strip()

    fire_agg = (
        fire.groupby(['nearest_district', 'year_month'])
        .agg(
            fire_point_count=('brightness', 'count'),
            fire_brightness_mean=('brightness', 'mean'),
            fire_confidence_mean=('confidence', 'mean'),
            fire_frp_mean=('frp', 'mean'),
        )
        .reset_index()
        .rename(columns={'nearest_district': 'district'})
    )
    return fire_agg


def load_ndvi(path: Path) -> pd.DataFrame:
    ndvi = pd.read_csv(path)
    ndvi['district'] = ndvi['district'].str.strip()
    ndvi['year_month'] = ndvi['year_month'].astype(str)

    keep_cols = [
        'year_month',
        'month_name',
        'district',
        'province',
        'adm_level',
        'adm_id',
        'PCODE',
        'n_pixels',
        'vim',
        'vim_avg',
        'viq',
    ]
    return ndvi[keep_cols]


def load_resp(path: Path) -> pd.DataFrame:
    resp = pd.read_csv(path)
    resp['district'] = resp['district'].str.strip()
    resp['year_month'] = (
        resp['year'].astype(int).astype(str)
        + '-'
        + resp['month'].astype(int).astype(str).str.zfill(2)
    )
    return resp[['year_month', 'district', 'respiratory_cases', 'deaths']]


def load_population(path: Path) -> pd.DataFrame:
    pop = pd.read_csv(path)
    pop['district'] = pop['District'].str.strip()
    pop['year_month'] = (
        pop['Year'].astype(int).astype(str)
        + '-'
        + pop['Month'].astype(int).astype(str).str.zfill(2)
    )
    pop['population'] = pop['Population_Thousands'] * 1000
    return pop[['year_month', 'district', 'population']]


def build_panel(data_dir: Path = DATA_DIR) -> Path:
    fire_path = data_dir / 'fire_monthly_district_full_columns_averaged.csv'
    ndvi_path = data_dir / 'MODIS_NDVI_monthly_district_full_columns_averaged.csv'
    resp_path = data_dir / 'respiratory_monthly_pm25_weighted_integer_counts.csv'
    pop_path = data_dir / 'sri_lanka_population_interpolated_2014_2024.csv'

    ndvi = load_ndvi(ndvi_path)
    fire = load_fire(fire_path)
    resp = load_resp(resp_path)
    pop = load_population(pop_path)

    panel = ndvi.merge(fire, how='left', on=['district', 'year_month'])
    panel = panel.merge(resp, how='left', on=['district', 'year_month'])
    panel = panel.merge(pop, how='left', on=['district', 'year_month'])

    panel['year'] = panel['year_month'].str.slice(0, 4).astype(int)
    panel['month'] = panel['year_month'].str.slice(5, 7).astype(int)

    panel['resp_cases_per_100k'] = (
        panel['respiratory_cases'] / panel['population'] * 1e5
    ).round(2)

    numeric_cols = [
        'fire_point_count',
        'fire_brightness_mean',
        'fire_confidence_mean',
        'fire_frp_mean',
        'respiratory_cases',
        'deaths',
        'population',
        'resp_cases_per_100k',
    ]
    for col in numeric_cols:
        panel[col] = panel[col].astype(float)

    panel = panel.sort_values(['district', 'year', 'month'])

    output_path = data_dir / 'fah_panel_2001_2024.csv'
    panel.to_csv(output_path, index=False)
    return output_path


def preview(path: Path, n: int = 5) -> pd.DataFrame:
    return pd.read_csv(path).head(n)


if __name__ == '__main__':
    output = build_panel()
    print(f'Wrote unified panel to: {output}')
    print(preview(output))
