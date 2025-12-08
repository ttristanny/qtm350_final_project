import pandas as pd
import os

# ========= CONFIG: file paths (using your actual locations) =========
PRIMARY_FILE   = "/Users/liuchang/Downloads/API_SE/API_SE.PRM.ENRR_DS2_en_csv_v2_4680.csv"
SECONDARY_FILE = "/Users/liuchang/Downloads/API_SE-2/API_SE.SEC.ENRR_DS2_en_csv_v2_4735.csv"
TERTIARY_FILE  = "/Users/liuchang/Downloads/API_SE-3/API_SE.TER.ENRR_DS2_en_csv_v2_3421.csv"

MORTALITY_FILE = "/Users/liuchang/Downloads/API_SH/API_SH.DYN.MORT_DS2_en_csv_v2_6199.csv"

LIFEEXP_FILE   = "/Users/liuchang/Downloads/API_SP/API_SP.DYN.LE00.IN_DS2_en_csv_v2_2505.csv"

GDP_PC_FILE    = "/Users/liuchang/Downloads/API_NY/API_NY.GDP.PCAP.KD_DS2_en_csv_v2_2624.csv"
EMP_RATE_FILE  = "/Users/liuchang/Downloads/API_SL/API_SL.EMP.TOTL.SP.ZS_DS2_en_csv_v2_4653.csv"

OUTPUT_DIR  = "data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "living_standards_5countries_1999_2019.csv")

START_YEAR = 1999
END_YEAR   = 2019
YEAR_COLS  = [str(y) for y in range(START_YEAR, END_YEAR + 1)]

# Restrict to your 5 project countries
TARGET_COUNTRIES = ["Botswana", "Azerbaijan", "Albania", "Colombia", "Fiji"]


def load_and_melt(path: str, value_name: str) -> pd.DataFrame:
    """
    Load a World Bank CSV (single indicator), keep 1999–2019,
    and return a long DataFrame with:

    Country Name, Country Code, Year, <value_name>
    """
    df = pd.read_csv(path, skiprows=4)
    cols = ["Country Name", "Country Code"] + YEAR_COLS
    df = df[cols].copy()

    # Restrict to the 5 target countries as early as possible
    df = df[df["Country Name"].isin(TARGET_COUNTRIES)].copy()

    long_df = df.melt(
        id_vars=["Country Name", "Country Code"],
        value_vars=YEAR_COLS,
        var_name="Year",
        value_name=value_name
    )
    long_df["Year"] = long_df["Year"].astype(int)
    return long_df


def main():
    # ----- Load each indicator for the 5 countries -----
    primary_long   = load_and_melt(PRIMARY_FILE,   "primary_enrollment_gross")
    secondary_long = load_and_melt(SECONDARY_FILE, "secondary_enrollment_gross")
    tertiary_long  = load_and_melt(TERTIARY_FILE,  "tertiary_enrollment_gross")

    mortality_long = load_and_melt(MORTALITY_FILE, "under5_mortality_per_1000")
    lifeexp_long   = load_and_melt(LIFEEXP_FILE,   "life_expectancy_years")

    gdp_pc_long    = load_and_melt(GDP_PC_FILE,    "gdp_per_capita_constant_2015usd")
    emp_rate_long  = load_and_melt(EMP_RATE_FILE,  "employment_rate_percent")

    # ----- Merge into one panel (5 countries × 1999–2019) -----
    merged = (
        primary_long
        .merge(secondary_long, on=["Country Name", "Country Code", "Year"], how="outer")
        .merge(tertiary_long,  on=["Country Name", "Country Code", "Year"], how="outer")
        .merge(mortality_long, on=["Country Name", "Country Code", "Year"], how="outer")
        .merge(lifeexp_long,   on=["Country Name", "Country Code", "Year"], how="outer")
        .merge(gdp_pc_long,    on=["Country Name", "Country Code", "Year"], how="outer")
        .merge(emp_rate_long,  on=["Country Name", "Country Code", "Year"], how="outer")
        .sort_values(["Country Name", "Year"])
        .reset_index(drop=True)
    )

    # Safety: enforce filter again in case any extra slipped through
    merged = merged[merged["Country Name"].isin(TARGET_COUNTRIES)].copy()

    # ----- Save -----
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    merged.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved merged 5-country dataset to: {OUTPUT_FILE}")
    print(f"Shape: {merged.shape}")
    print(merged.head())


if __name__ == "__main__":
    main()
