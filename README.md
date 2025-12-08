# QTM 350 Final Project: Life Quality Across Five Countries

Group Members(Emory ID): Chang Liu(2579008), Emily Liu(2550121), Sally Shen(2549393), Tristan Yang (2592886), Sherry Zhang(2593324)

This project analyzes how **quality of life** has evolved from **1999–2019** in five countries that had **similar GDP per capita** around 1999 but are located on different continents:

- **Albania** (Europe)  
- **Azerbaijan** (Asia)  
- **Botswana** (Africa)  
- **Colombia** (South America)  
- **Fiji** (Oceania)  

Using World Bank World Development Indicators, we compare these countries on two main dimensions:

- **Economic & health outcomes**
  - Employment rate  
  - Life expectancy at birth  
  - Under-5 mortality rate  

- **Education coverage**
  - Primary school gross enrollment  
  - Secondary school gross enrollment  
  - Tertiary school gross enrollment  

Our analysis uses Python for cleaning, NA handling, and visualisation. The final Quarto report and notebook discuss trends over time and compare how life quality diverges across countries that started with similar income levels.

---

## How to run the project

### 1. Clone the repository and move into it
git clone https://github.com/ttristanny/qtm350_final_project.git
cd qtm350_final_project

### 2. Install required Python packages
pip install pandas matplotlib numpy jupyter

### 3. Rebuild the cleaned 5-country panel dataset (1999–2019)
python Preprocessing.py

### 4. Run the analysis scripts and generate figures
python Fertality.py                # fertility / population analysis
python life_expectancy_analysis.py # life expectancy & mortality analysis
python qtm350final.py              # education enrollment (primary/secondary/tertiary) plots

### 5. Open the notebook for full analysis
jupyter notebook finalproject.ipynb
