import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv("data/living_standards_5countries_1999_2019.csv")

# List of countries directly from dataset
countries = df["Country Name"].unique()

# Line Plot of Life Expectancy Over Time for Each Country
plt.figure(figsize=(10, 6))

for country in countries:
    temp = df[df["Country Name"] == country]
    plt.plot(
        temp["Year"],
        temp["life_expectancy_years"],
        marker="o",
        label=country
    )

plt.title("Life Expectancy at Birth (1999–2019)")
plt.xlabel("Year")
plt.ylabel("Life Expectancy (Years)")
plt.legend(title="Country")
plt.tight_layout()
plt.show()

# Bar Plot: Improvement from 1999 to 2019
improvement_df = (
    df[df["Year"].isin([1999, 2019])]
    .pivot(index="Country Name", columns="Year", values="life_expectancy_years")
    .reset_index()
)

# Calculate improvement
improvement_df["Improvement"] = improvement_df[2019] - improvement_df[1999]

plt.figure(figsize=(10, 6))
plt.bar(improvement_df["Country Name"], improvement_df["Improvement"], color="skyblue")
plt.title("Improvement in Life Expectancy (1999–2019)")
plt.xlabel("Country")
plt.ylabel("Years of Life Expectancy Gained")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()