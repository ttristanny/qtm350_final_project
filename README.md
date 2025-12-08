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

## How to reproduce the education plots

1. Clone the repository and switch to the `Emily&Sally-education` branch.
2. Make sure you have Python (3.8+) with `pandas` and `matplotlib` installed:
   ```bash
   pip install pandas matplotlib

