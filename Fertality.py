import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use("TkAgg")

sns.set_theme(style="whitegrid", context="talk")
plt.rcParams["figure.figsize"] = (12, 7)
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.titleweight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"

FILE = "/Users/liuchang/Downloads/API_SH/API_SH.DYN.MORT_DS2_en_csv_v2_6199.csv"

df_raw = pd.read_csv(FILE, skiprows=4)

INDICATOR = "SH.DYN.MORT"

df = df_raw[df_raw["Indicator Code"] == INDICATOR].copy()

countries = ["Botswana", "Azerbaijan", "Albania", "Colombia", "Fiji"]

years = [str(y) for y in range(1999, 2019+1)]

df = df[df["Country Name"].isin(countries)]

df = df[["Country Name"] + years]

df_long = df.melt(
    id_vars="Country Name",
    value_vars=years,
    var_name="Year",
    value_name="Mortality"
)

df_long["Year"] = df_long["Year"].astype(int)
df_long = df_long.dropna()

palette = sns.color_palette("viridis", n_colors=len(countries))

fig, ax = plt.subplots(figsize=(15, 8))

for i, (country, group) in enumerate(df_long.groupby("Country Name")):
    group = group.sort_values("Year")

    ax.plot(
        group["Year"], group["Mortality"],
        label=country,
        linewidth=2.5,
        marker="o",
        markersize=6,
        alpha=0.9,
        color=palette[i]
    )

    # Highlight start (1999) + end (2019)
    start = group[group["Year"] == 1999]["Mortality"].iloc[0]
    end = group[group["Year"] == 2019]["Mortality"].iloc[0]

    ax.text(1999 - 0.2, start + 1, f"{start:.1f}", color=palette[i])
    ax.text(2019 + 0.2, end + 1, f"{end:.1f}", color=palette[i])

# Shade 2008–2009 global recession
ax.axvspan(2008, 2009, color="grey", alpha=0.15)

ax.set_title("Under-5 Mortality Rate (per 1,000 live births)\n1999–2019", fontsize=20)
ax.set_xlabel("Year")
ax.set_ylabel("Mortality per 1,000 live births")

ax.legend(title="Country", bbox_to_anchor=(1.04, 1), loc="upper left")

plt.tight_layout()
plt.show()

g = sns.FacetGrid(
    df_long,
    col="Country Name",
    col_wrap=3,
    sharey=True,
    height=4,
    aspect=1.3
)

g.map_dataframe(
    sns.lineplot,
    x="Year",
    y="Mortality",
    marker="o"
)

g.fig.suptitle("Under-5 Mortality Trends by Country (1999–2019)", y=1.05, fontsize=18)

plt.show()

heat_df = df_long.pivot(index="Country Name", columns="Year", values="Mortality")

plt.figure(figsize=(18, 5))
sns.heatmap(
    heat_df,
    cmap="magma_r",
    linewidths=0.5,
    linecolor="white",
    cbar_kws={"label": "Mortality (per 1,000 live births)"},
)

plt.title("Heatmap of Under-5 Mortality Rate (1999–2019)", fontsize=18, pad=15)
plt.xlabel("Year")
plt.ylabel("Country")

plt.tight_layout()
plt.show()
