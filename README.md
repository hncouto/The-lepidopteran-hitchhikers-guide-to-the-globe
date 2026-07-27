<a href="https://doi.org/10.5281/zenodo.21620831"><img src="https://zenodo.org/badge/1086422220.svg" alt="DOI"></a>

# The Lepidopteran hitchhiker's guide to the globe
"The lepidopteran hitchhiker’s guide to the globe: the spread and dispersal of non-native Lepidoptera" code repository.

Original source: Couto, H., Rebelo, R., Grosso-Silva, J., Cardoso, P., Capinha, C. (2026). The lepidopteran hitchhiker’s guide to the globe: the spread and dispersal of non-native moths and butterflies. Global Ecology and Biogeography. 

The data needed for this project can be obtained from the original source Supplementary Materials section.

# Invasion Drivers and Distribution Analysis of Lepidoptera

This project investigates the **drivers of invasion and establishment** for Lepidoptera (*moths* and *butterflies*) using statistical modeling in **R**, and provides complementary **visualizations and regional analyses** using **Python**.

---

## Project Structure

The repository includes 2 scripts:

| Language | File | Purpose |
|-----------|------|----------|
| **R** | `Model.R` | Model the drivers of invasion and establishment for *Total Lepidoptera*, *Moths*, and *Butterflies*. |
| **Python** | `Figures.py` | Extract visualizations and extract information on the prevalence of the species and affected regions. |

---

## R Script — Modeling of Invasion Drivers

### Requirements

#### Required Libraries
```r

broom.mixed
bruceR
dplyr
forcats
glmmTMB
usdm
zoo
MuMIn

```

Install with:
```r
install.packages(c("broom.mixed", "bruceR", "dplyr", "forcats", "glmmTMB", "usdm", "zoo", "MuMIn"))
```

#### Required Data
```
Appendix1_CountryData.csv
```
> ⚠️ This dataset can be found as well as a Supplementary Material of the paper in the original source.

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
| `Butterflies` | Binomial Distribution | Presence or Absence. |
| `Moths -  Total` | Negative binomial distribution: quadratic parameterization | Number of Establishments. |
| `Moths - Macro-moths` | Negative binomial distribution: quadratic parameterization | Number of Establishments. |
| `Moths - Micro-moths` | Negative binomial distribution: quadratic parameterization | Number of Establishments. |

Model Results can be seen on **[3.4]** 

Extration of Model Results for forest plot on **[3.5]**

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
models_data.csv
```
> ⚠️ Appendix2_DistributionData.xlsx dataset can be found as well as an Supplementary Material of the paper in the original source.
> ⚠️ models_data.csv dataset is extracted from Model.R


---

### Purpose

Extract **summaries** and **visual insights** on:
- Most affected regions  
- Most prevalent introduced Lepidoptera species
- Flows of invasion
- Temporal patterns of invasion and establishment
- Forest Plot for the model results  

---

### Workflow Summary

#### [0] Imports
- Import necessary libraries and data.

#### [1] Temporal Analysis
- **[1.0]** Prepare tables for temporal study.  
- **[1.1]** Analyze global invasion trends for each group.
- **[1.2]** Perform continent-level temporal analysis. 

#### [2] Regions Analysis
- **[2.0]** Data preparation.  
- **[2.1]** Identify most prevalent species amongst:
  - Total Lepidoptera    
  - Butterflies
  - All Moths
      - Macro-moths
      - Micro-moths  
- **[2.2]** Identify most invaded regions for each group.

#### [3] Histograms 
- Generate histograms summarizing the number of records per region for each group.

#### [4] Flow Analysis
- **[4.0]** Create pivot tables by group for flow analysis.  
- **[4.1]** Create the script for chord diagrams using `pycirclize`.  
- **[4.2]** Plot the invasion flows for each group.

#### [5] Histograms
- **[5.1]** Data Preparation
- **[5.2]** Plot the Forest Plot for the model results.


---

## Outputs

### R Script:
- Statistical models of establishment drivers  
- Model summaries and diagnostics  
- Tables of significant predictors  

### Python Script:
- Summary tables for species prevalence and invaded regions  
- Visualizations (e.g., chord diagrams, temporal trends, histograms and forest plots)  

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

We would like to thank André Calado, Claudia Gomes and João Neto for support during the data collection process, to Rebecca Pabst for assistance in data analysis, to Dr. Regan Early for making available the data on countries’ biological invasions’ detection capacity, to Dr. Michael Braby, Dr Carlos Lopez Vaamonde, Dr. Richard Mally, Dr. Yi-Bo Zhang and Peilin Wang for all the help on revising the data. CC acknowledges the support of the Portuguese Foundation for Science and Technology (FCT) through InvaSTOP project grant (https://doi.org/10.54499/2023.12533.PEX) and funds to CEG/IGOT Research Unit (UIDB/00295/2020 and UIDP/00295/2020). HC is funded by a grant (2022.14512.BD) financed by FCT (https://doi.org/10.54499/2022.14512.BD). This work received support from CE3C (https://doi.org/10.54499/UIDB/00329/2025), and CHANGE (https://doi.org/10.54499/la/p/0121/2020).

