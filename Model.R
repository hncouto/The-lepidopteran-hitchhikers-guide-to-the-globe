# [0] Imports
library(broom.mixed)
library(bruceR)
library(dplyr)
library(DHARMa)
library(forcats)
library(glmmTMB)
library(MuMIn)
library(usdm)
library(zoo)

Appendix1_CountryData <- read.csv("Raw Data/Appendix1_CountryData.csv", sep =",")

# [1] Data Preparation
FinalData <- Appendix1_CountryData
FinalData_clean <- FinalData[!is.na(FinalData$InvBias_SC), ]
FinalData_clean <- na.omit(FinalData_clean)

FinalData_clear <- data.frame(
  TotalIntroducedSpecies = FinalData_clean$TotalIntroducedSpecies,
  ButterflyIntSp = FinalData_clean$ButterflyIntSp,
  MothsIntSp = FinalData_clean$MothsIntSp,
  Micro.MothsIntSp = FinalData_clean$Micro.MothsIntSp,
  Macro.MothsIntSp = FinalData_clean$Macro.MothsIntSp,
  Island = FinalData_clean$Island,
  GDP_AVG5Y = scaler(FinalData_clean$GDP_AVG5Y),
  Area_SqKms = scaler(FinalData_clean$Area_SqKms),
  DensPop = scaler(FinalData_clean$DensPop),
  AgricultureCultivated_Area_100 = FinalData_clean$AgricultureCultivated_Area_100/100,
  Urban_Area_100 = FinalData_clean$Urban_Area_100/100,
  Forest_Area_100 = FinalData_clean$Forest_Area_100/100,
  MeanAnnualTemperature = scaler(FinalData_clean$MeanAnnualTemperature),
  AnnualPrecipitation = scaler(FinalData_clean$AnnualPrecipitation),
  InvBias_SC = scaler(FinalData_clean$InvBias_SC),
  Region = FinalData_clean$RegionName,
  Continent = FinalData_clean$Continent,
  Country = FinalData_clean$Country)



FinalData_clear_bin <- FinalData_clear
FinalData_clear_bin$ButterflyIntSp[FinalData_clear_bin$ButterflyIntSp != 0] <- 1


new_dataframe <- cbind(FinalData_clear$Island,
                       FinalData_clear$GDP_AVG5Y, 
                       FinalData_clear$Area_SqKms,
                       FinalData_clear$DensPop,
                       FinalData_clear$AgricultureCultivated_Area_100 , 
                       FinalData_clear$Urban_Area_100,
                       FinalData_clear$Forest_Area_100 ,
                       FinalData_clear$MeanAnnualTemperature ,
                       FinalData_clear$AnnualPrecipitation ,
                       FinalData_clear$InvBias_SC)

# [2] VIF Analysis
vif_results <- vifstep(
  new_dataframe, th=5)
vif_results

# [3] Models
# [3.1] Total Lepidoptera
GLMM_FULL_MinMax <- glmmTMB(TotalIntroducedSpecies ~ Island +
                    GDP_AVG5Y +
                    Area_SqKms +
                    DensPop  +
                    AgricultureCultivated_Area_100 + 
                    Urban_Area_100 + 
                    Forest_Area_100 + 
                    MeanAnnualTemperature + 
                    AnnualPrecipitation + 
                    InvBias_SC +
                    (1|Continent), 
                    data = FinalData_clear,
                    family = nbinom2)

# [3.2] Butterflies 
GLMMBF_MinMax_bin <- glmmTMB(ButterflyIntSp ~ Island +
                             GDP_AVG5Y +
                             Area_SqKms +
                             DensPop +
                             AgricultureCultivated_Area_100 + 
                             Urban_Area_100 + 
                             Forest_Area_100 + 
                             MeanAnnualTemperature + 
                             AnnualPrecipitation + 
                             InvBias_SC +
                             (1|Continent) , 
                           data = FinalData_clear_bin,
                           family = binomial)


# [3.3] Moths - Total
GLMMMoth_MinMax <- glmmTMB(MothsIntSp ~ Island +
                                GDP_AVG5Y +
                                Area_SqKms +
                                DensPop +
                                AgricultureCultivated_Area_100 + 
                                Urban_Area_100 + 
                                Forest_Area_100 + 
                                MeanAnnualTemperature + 
                                AnnualPrecipitation + 
                                InvBias_SC +
                                (1|Continent), 
                              data = FinalData_clear,
                              family = nbinom2)


# [3.3.1] Moths - Micro-moths
GLMMMaMoth_MinMax <- glmmTMB(Macro.MothsIntSp ~ Island +
                                GDP_AVG5Y +
                                Area_SqKms +
                                DensPop +
                                AgricultureCultivated_Area_100 + 
                                Urban_Area_100 + 
                                Forest_Area_100  + 
                                MeanAnnualTemperature + 
                                AnnualPrecipitation + 
                                InvBias_SC +
                                (1|Continent), 
                              data = FinalData_clear,
                              family = nbinom2)

# [3.3.2] Moths - Macro-Moths
GLMMMiMoth_MinMax <- glmmTMB(Micro.MothsIntSp ~ Island +
                               GDP_AVG5Y +
                               Area_SqKms +
                               DensPop +
                               AgricultureCultivated_Area_100 + 
                               Urban_Area_100 + 
                               Forest_Area_100 + 
                               MeanAnnualTemperature + 
                               AnnualPrecipitation + 
                               InvBias_SC +
                               (1|Continent), 
                             data = FinalData_clear,
                             family = nbinom2)


# [3.4] Show Results
summary(GLMM_FULL_MinMax)
simulationOutput_FULL <- simulateResiduals(fittedModel = GLMM_FULL_MinMax, plot = F)
plot(simulationOutput_FULL)
performance::check_collinearity(GLMM_FULL_MinMax)

summary(GLMMBF_MinMax_bin)
simulationOutput_BF <- simulateResiduals(fittedModel = GLMMBF_MinMax_bin, plot = F)
plot(simulationOutput_BF)
performance::check_collinearity(GLMMBF_MinMax_bin)

summary(GLMMMoth_MinMax)
simulationOutput_Moth <- simulateResiduals(fittedModel = GLMMMoth_MinMax, plot = F)
plot(simulationOutput_Moth)
performance::check_collinearity(GLMMMoth_MinMax)

summary(GLMMMaMoth_MinMax)
simulationOutput_MaMoth <- simulateResiduals(fittedModel = GLMMMaMoth_MinMax, plot = F)
plot(simulationOutput_MaMoth)
performance::check_collinearity(simulationOutput_MaMoth)

summary(GLMMMiMoth_MinMax)
simulationOutput_MiMoth <- simulateResiduals(fittedModel = GLMMMiMoth_MinMax, plot = F)
plot(simulationOutput_MiMoth)
performance::check_collinearity(simulationOutput_MiMoth)


# [3.5] Extract Model Results with 95% CI

models <- list(GLMM_FULL_MinMax,GLMMBF_MinMax_bin,GLMMMoth_MinMax,GLMMMaMoth_MinMax,GLMMMiMoth_MinMax)
model_names <- c("Total Lepidoptera","Butterflies Presence","Total Moths","Macro-moths","Micro-moths")

get_models_data <- function(model, model_name) {
  tidy_df <- tidy(model, effects = "fixed", conf.int = TRUE)
  tidy_df$model <- model_name
  tidy_df}

models_data <- bind_rows(mapply(get_models_data, models, model_names, SIMPLIFY = FALSE))
models_data$term <- fct_rev(factor(models_data$term, levels = unique(models_data$term)))
write.csv(models_data, "Updated Data/models_data.csv", row.names = FALSE)
