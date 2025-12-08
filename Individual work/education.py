import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def fill_isolated_nans(s: pd.Series) -> pd.Series:
    """
    For a 1D series:
    - If there is exactly ONE NaN between two non-NaNs, replace it
      with the average of its neighbors.
    - If there are 2+ consecutive NaNs, leave them as NaN.
    - NaNs at the start or end are left as NaN.
    """
    s = s.copy()
    values = s.values
    isnan = pd.isna(values)
    n = len(values)

    i = 0
    while i < n:
        if isnan[i]:
            start = i
            # find end of this NaN run
            while i + 1 < n and isnan[i + 1]:
                i += 1
            end = i
            length = end - start + 1

            # isolated single NaN, not at edges, neighbors are non-NaN
            if (
                length == 1
                and start > 0
                and end < n - 1
                and not isnan[start - 1]
                and not isnan[end + 1]
            ):
                values[start] = (values[start - 1] + values[end + 1]) / 2.0
                isnan[start] = False  # now filled

        i += 1

    return pd.Series(values, index=s.index)

df = pd.read_csv("living_standards_5countries_1999_2019.csv")

countries = ["Botswana", "Azerbaijan", "Albania", "Colombia", "Fiji"]
df = df[df["Country Name"].isin(countries)]

df = df.sort_values(["Country Name", "Year"])

enrollment_cols = {
    "primary_enrollment_gross": "Primary School Enrollment (% gross)",
    "secondary_enrollment_gross": "Secondary School Enrollment (% gross)",
    "tertiary_enrollment_gross": "Tertiary School Enrollment (% gross)",
}

for col in enrollment_cols.keys():
    for country in countries:
        mask = df["Country Name"] == country
        df.loc[mask, col] = fill_isolated_nans(df.loc[mask, col])

for col, title in enrollment_cols.items():
    plt.figure(figsize=(8, 5))

    for country in countries:
        temp = df[df["Country Name"] == country]
        plt.plot(
            temp["Year"],
            temp[col],
            marker="o",
            label=country,
        )

    plt.title(title + " (1999–2019)")
    plt.xlabel("Year")
    plt.ylabel("Gross enrollment (%)")
    plt.legend(title="Country")
    plt.tight_layout()
    plt.show()
