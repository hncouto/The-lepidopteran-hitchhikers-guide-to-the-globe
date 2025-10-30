# The Lepidopteran hitchhiker's guide to the globe
"The lepidopteran hitchhiker’s guide to the globe: the spread and dispersal of non-native Lepidoptera" code repository.
Original source:

# Invasion Drivers and Distribution Analysis of Lepidoptera

This project investigates the **drivers of invasion and establishment** for Lepidoptera (*moths* and *butterflies*) using statistical modeling in **R**, and provides complementary **visualizations and regional analyses** using **Python**.

---

## Project Structure

The repository includes 2 scripts:

| Language | File | Purpose |
|-----------|------|----------|
| **R** | `Model.R` | Model the drivers of invasion and establishment for *Total Lepidoptera*, *Moths*, and *Butterflies*. |
| **Python** | `TablesCirclize.py` | Extract visualizations and extract information on the prevalence of the species and affected regions. |

---

## R Script — Modeling of Invasion Drivers

### Requirements

#### Required Libraries
```r
glmmTMB
usdm
zoo
MuMIn
```

Install with:
```r
install.packages(c("glmmTMB", "usdm", "zoo", "MuMIn"))
```

#### Required Data
```
Appendix1_CountryData.csv
```
> ⚠️ This dataset must be in the same directory as the R script.

---

### Purpose

Identify the **drivers of invasion and establishment** for:
- Total Lepidoptera  
- Moths  
- Butterflies  

---

### Workflow Summary

#### [0] Imports
- Load all required libraries.
- Load all required data.

#### [1] Data Preparation
- Remove countries with missing values.  
- Create a binary presence/absence dataframe per country.  
- Prepare a dataframe with only predictors for **Variance Inflation Factor (VIF)** analysis.

#### [2] VIF Analysis
- Perform VIF analysis to ensure low correlation and multicollinearity among predictors.

#### [3] Models

| Target Group | Model Family Function | Objective |
|-------|------|----------|
| `Total Lepidoptera` | Negative binomial distribution: quadratic parameterization | Number of Establishments. |
| `Moths` | Negative binomial distribution: quadratic parameterization | Number of Establishments. |
| `Butterflies` | Binomial Distribution | Presence or Absence. |

Model Results can be seen on **[3.4]** 

---

## Python Script — Visual and Temporal Analysis

### Requirements

#### Required Libraries
```
pandas
pycirclize
matplotlib
numpy
plotly
```

Install them with:
```bash
pip install pandas pycirclize matplotlib numpy plotly
```

#### Required Data
```
Appendix2_DistributionData.xlsx
```
> ⚠️ Ensure this file is in the same directory as the Python script.

---

### Purpose

Extract **summaries** and **visual insights** on:
- Most affected regions  
- Most prevalent introduced Lepidoptera species
- Flows of invasion
- Temporal patterns of invasion and establishment  

---

### Workflow Summary

#### [0] Imports
- Import necessary libraries and data.

#### [1] Regions Analysis
- **[1.0]** Data preparation.  
- **[1.1]** Identify most prevalent species amongst:
  - Total Lepidoptera  
  - Moths  
  - Butterflies  
- **[1.2]** Identify most invaded regions for each group.

#### [2] Flow Analysis
- **[2.0]** Create pivot tables by group for flow analysis.  
- **[2.1]** Create the script for chord diagrams using `pycirclize`.  
- **[2.2]** Plot the invasion flows for each group.

#### [3] Temporal Analysis
- **[3.0]** Prepare tables for temporal study.  
- **[3.1]** Analyze global invasion trends for each group.
- **[3.2]** Perform continent-level temporal analysis.  

#### [4] Histograms
- Generate histograms summarizing the number of records per region for each group.

---

## Outputs

### R Script:
- Statistical models of establishment drivers  
- Model summaries and diagnostics  
- Tables of significant predictors  

### Python Script:
- Summary tables for species prevalence and invaded regions  
- Visualizations (e.g., chord diagrams, temporal trends and histograms)  

---

## Authors & Contact

- **Author(s):** *Henrique Couto 1*, *Rui Rebelo 1*, *José Grosso-Silva 2,3*, *Pedro Cardoso 1*, *César Capinha 4,5*  
- **Contact:** *[henriquenunocouto@gmail.com]*  
- **Institutions:**
  *1.	cE3c Centre for Ecology, Evolution and Environmental Changes & CHANGE - Global Change and Sustainability Institute, Faculdade de Ciências da Universidade de Lisboa, Lisboa, Portugal*
  *2.	Museu de História Natural e da Ciência da Universidade do Porto. Porto; Portugal*
  *3.	Faculdade de Ciências da Universidade do Porto. Porto; Portugal*
  *4.	Centre of Geographical Studies, Institute of Geography and Spatial Planning, Universidade de Lisboa, Lisboa, Portugal*
  *5.	Associate Laboratory TERRA, Portugal*  


---

## Acknowledgments


