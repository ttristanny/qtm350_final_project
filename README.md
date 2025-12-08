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

