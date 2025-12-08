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

FILE = "data/living_standards_5countries_1999_2019.csv"

df_full = pd.read_csv(FILE)
countries = ["Botswana", "Azerbaijan", "Albania", "Colombia", "Fiji"]
df_full = df_full[df_full["Country Name"].isin(countries)].copy()

df_long = df_full[["Country Name", "Year", "under5_mortality_per_1000"]].rename(
    columns={"under5_mortality_per_1000": "Mortality"}
)

df_long = df_long.dropna(subset=["Mortality"])
df_long["Year"] = df_long["Year"].astype(int)

countries = df_long["Country Name"].unique().tolist()
years = sorted(df_long["Year"].unique())

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

    start_year = group["Year"].min()
    end_year = group["Year"].max()
    start_val = group.loc[group["Year"] == start_year, "Mortality"].iloc[0]
    end_val = group.loc[group["Year"] == end_year, "Mortality"].iloc[0]

    ax.text(start_year - 0.2, start_val + 1, f"{start_val:.1f}", color=palette[i])
    ax.text(end_year + 0.2, end_val + 1, f"{end_val:.1f}", color=palette[i])

if 2008 in years and 2009 in years:
    ax.axvspan(2008, 2009, color="grey", alpha=0.15)

ax.set_title("Under-5 Mortality Rate (per 1,000 live births) 1999–2019", fontsize=20)
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
    cbar_kws={"label": "Mortality (per 1,000 live births)"}
)

plt.title("Heatmap of Under-5 Mortality Rate (1999–2019)", fontsize=18, pad=15)
plt.xlabel("Year")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

