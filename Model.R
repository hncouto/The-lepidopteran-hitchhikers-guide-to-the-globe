# [0] Imports
library(glmmTMB)
library(usdm)
library(zoo)
library(MuMIn)
Appendix1_CountryData <- read.csv("Appendix1_CountryData.csv", sep =";")

# [1] Data Preparation
FinalData <- Appendix1_CountryData
FinalData_clear <- FinalData[!is.na(FinalData$InvBias_SC), ]
FinalData_clear <- na.omit(FinalData_clear)

FinalData_clear_bin <- FinalData_clear
FinalData_clear_bin$NonButterflyIntSp[FinalData_clear_bin$NonButterflyIntSp != 0] <- 1
FinalData_clear_bin$ButterflyIntSp[FinalData_clear_bin$ButterflyIntSp != 0] <- 1
FinalData_clear_bin$TotalIntroducedSpecies[FinalData_clear_bin$TotalIntroducedSpecies != 0] <- 1

new_dataframe <- cbind(FinalData_clear$Island,
                       log(FinalData_clear$GDP_AVG5Y) , 
                       log(FinalData_clear$Area_SqKms),
                       FinalData_clear$DensPop,
                       FinalData_clear$AgricultureCultivated_Area_100 , 
                       FinalData_clear$Urban_Area_100,
                       FinalData_clear$ClosedForest_Area_100 ,
                       FinalData_clear$OpenForest_Area_100  ,
                       FinalData_clear$MeanAnnualTemperature ,
                       FinalData_clear$AnnualPrecipitation ,
                       FinalData_clear$InvBias_SC)

# [2] VIF Analysis
vif_results <- vifstep(
  new_dataframe, th=5)
vif_results

# [3] Models
# [3.1] Total Lepidoptera - Number of Establishments
GLMM_FULL_NoScaler <- glmmTMB(TotalIntroducedSpecies ~ Island +
                    log(GDP_AVG5Y) +
                    log(Area_SqKms) +
                    DensPop  +
                    AgricultureCultivated_Area_100 + 
                    Urban_Area_100 + 
                    ClosedForest_Area_100 + 
                    OpenForest_Area_100  + 
                    MeanAnnualTemperature + 
                    AnnualPrecipitation + 
                    InvBias_SC +
                    (1|Continent), 
                    data = FinalData_clear,
                    family = nbinom2)

# [3.2] Moths - Number of Establishments
GLMMNonBF_NoScaler <- glmmTMB(NonButterflyIntSp ~ Island +
                              log(GDP_AVG5Y) +
                              log(Area_SqKms) +
                              DensPop +
                              AgricultureCultivated_Area_100 + 
                              Urban_Area_100 + 
                              ClosedForest_Area_100 + 
                              OpenForest_Area_100  + 
                              MeanAnnualTemperature + 
                              AnnualPrecipitation + 
                              InvBias_SC +
                              (1|Continent), 
                            data = FinalData_clear,
                            family = nbinom2)


# [3.3] Butterflies - Regions with records
GLMMBF_NoScaler_bin <- glmmTMB(ButterflyIntSp ~ Island +
                             log(GDP_AVG5Y) +
                             log(Area_SqKms) +
                             DensPop +
                             AgricultureCultivated_Area_100 + 
                             Urban_Area_100 + 
                             ClosedForest_Area_100 + 
                             OpenForest_Area_100  + 
                             MeanAnnualTemperature + 
                             AnnualPrecipitation + 
                             InvBias_SC +
                             (1|Continent) , 
                           data = FinalData_clear_bin,
                           family = binomial)

# [3.4] Show Results
summary(GLMM_FULL_NoScaler)
summary(GLMMNonBF_NoScaler)
summary(GLMMBF_NoScaler_bin)