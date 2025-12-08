import pandas as pd
import matplotlib.pyplot as plt

# Import the dataset
df = pd.read_csv('data/data.csv')

# Print the dataset
print(df)

# Filter data for years 1999-2019
df_filtered = df[(df['Year'] >= 1999) & (df['Year'] <= 2019)]

# Get unique countries
countries = df_filtered['Country Name'].unique()

# Create the plot
plt.figure(figsize=(10, 6))

for country in countries:
    country_data = df_filtered[df_filtered['Country Name'] == country]
    # Sort by year to ensure correct line plotting
    country_data = country_data.sort_values('Year')
    plt.plot(country_data['Year'], country_data['employment_rate_percent'], label=country, marker='o')

# Add title and labels
plt.title('Employment Rate (1999-2019) for 5 Countries')
plt.xlabel('Year')
plt.ylabel('Employment Rate (%)')

# Add legend
plt.legend()

# Set x-axis ticks to ensure integer years are shown clearly
plt.xticks(sorted(df_filtered['Year'].unique()), rotation=45)

# Add grid
plt.grid(True)

# Save the plot
plt.tight_layout()
plt.savefig('employment_rate_line_chart.png')