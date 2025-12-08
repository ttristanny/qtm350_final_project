# Qtm350_final_project – Life Expectancy Analysis  
### **Branch:** [Sherry-Life-Expectancy](https://github.com/ttristanny/qtm350_final_project/tree/Sherry-Life-Expectancy)

This branch examines how life expectancy at birth has changed from 1999–2019 across five countries representing different world regions:

- Albania (Europe)  
- Azerbaijan (Asia)  
- Botswana (Africa)  
- Colombia (South America)  
- Fiji (Oceania)

## Indicator  
**Life expectancy at birth, total (years)** – Life expectancy at birth indicates the number of years a newborn infant would live if prevailing patterns of mortality at the time of its birth were to stay the same throughout its life.

## Visualizations
### 1. Life Expectancy Over Time (1999–2019)  
A line plot showing each country’s life expectancy trajectory across the 20-year period.  
This visualization helps identify:

- Broad upward trends in population health  
- Differences in starting life expectancy levels  
- Periods of acceleration or stagnation  
- Regional contrasts in long-term health outcomes  

It provides a clear, continuous view of how longevity has evolved over time.

### 2. Improvement from 1999 to 2019
A bar chart measuring the **total increase in life expectancy** over the dataset window for each country.  
This figure highlights:

- Which countries experienced the greatest improvement  
- Relative health gains across regions  
- Whether changes were modest or substantial  
- Long-term progress in population well-being  

This summary plot complements the time-series chart by focusing on net progress instead of annual variation.

## Files  
- `life_expectancy_analysis.py` – Python analysis  

## Author  
**Sherry Zhang** — QTM 350 Final Project
# qtm350_final_project – Education Analysis

This project is part of the QTM 350 final project and examines how **living standards** have changed over time for five countries, using indicators from three broad perspectives:

- **Economic** – e.g., GDP per capita, employment
- **Population/Health** – e.g., under-5 mortality, life expectancy
- **Education** – primary, secondary, and tertiary enrollment rates

The **Emily&Sally-education** branch focuses specifically on the **education dimension**:  
we study how education coverage has evolved over time in each country and how countries compare to one another.

## Countries studied

The project uses a balanced panel of five countries representing different world regions:

- **Albania** – Europe  
- **Azerbaijan** – Asia  
- **Botswana** – Africa  
- **Colombia** – South America  
- **Fiji** – Oceania  

For each country, we use annual data from **1999–2019**.

## Education indicators

Our education analysis uses three gross enrollment rates:

- `primary_enrollment_gross` – Primary school enrollment (% of relevant age group)  
- `secondary_enrollment_gross` – Secondary school enrollment (%)  
- `tertiary_enrollment_gross` – Tertiary (higher) education enrollment (%)  

These variables allow us to:

1. Track how **education coverage changes over time** within each country.
2. Compare **coverage levels across countries** at each education level.
3. Identify where progress has slowed, plateaued, or accelerated.

## Handling missing values (NAs)

To avoid misleading patterns while still being transparent about data gaps, we treat missing values as follows:

- If there is **only one isolated NA** for a country in a given series (a single missing year with valid values before and after),
  we **interpolate** that point (using the average of the neighboring years) so that the line stays connected.
- If there are **two or more consecutive NAs**, we **keep them as missing**, which creates a visible break in the line for that period.
- Missing values at the **beginning or end** of a country’s time series are also left as missing.

This rule ensures that short, likely-noisy gaps do not visually exaggerate discontinuities, while longer periods with no data remain clearly visible.

## Visualizations

The main education script on this branch (`qtm350final.py`) generates **three line plots**, one for each level of education:

1. **Primary Enrollment Plot** – 1999–2019  
2. **Secondary Enrollment Plot** – 1999–2019  
3. **Tertiary Enrollment Plot** – 1999–2019  

Each plot:

- Has **five lines**, one for each country.
- Uses the NA rules above to decide whether to connect lines or leave gaps.
- Allows us to visually compare **trends over time** (e.g., which countries expanded secondary or tertiary coverage, which stagnated, etc.).

These figures are used in the final report to discuss questions such as:

- Which countries have achieved the highest levels of education coverage?
- Do improvements in primary education translate into gains in secondary and tertiary education?
- Are there periods where progress in education coverage stalls or reverses?
## 📊 Under-5 Mortality Visualization Module  
**Author:** CL1234567890  
**Branch:** `CL's-Code`  
**Course:** QTM350 Final Project

This module contains the **first full version** of our under-5 mortality analysis using the World Bank *SH.DYN.MORT* dataset. It focuses on five GDP-comparable countries across different world regions:

- **Botswana** (Africa)  
- **Azerbaijan** (Asia)  
- **Albania** (Europe)  
- **Colombia** (South America)  
- **Fiji** (Oceania)

The goal is to compare **living standards** via **child mortality trends** from **1999 to 2019**, visualized through several high-quality statistical graphics.

---

## 📁 Included Script

### **`Fertality.py`**  
*(Note: despite the filename, the script performs mortality analysis, not fertility.)*

This script includes:

### **1. Data Loading & Preprocessing**
- Loads World Bank mortality data (`API_SH.DYN.MORT_DS2...csv`)  
- Filters by indicator `SH.DYN.MORT` (under-5 mortality per 1,000 live births)  
- Selects the five target countries  
- Converts data wide → long for visualization  

---

## 📈 Visualizations

### **1. Multi-Country Line Plot (1999–2019)**
- Viridis color palette  
- Highlights 1999 & 2019 mortality values  
- Shades 2008–2009 global financial crisis  

### **2. Faceted Country Panels**
- One plot per country  
- Allows quick comparison of slopes  

### **3. Heatmap (Country × Year)**
- Shows relative mortality levels over time  
- Helps identify structural differences  

---

## ▶️ How to Run the Script

Inside the project folder:

```bash
python Fertality.py

