# [0] Imports

# [0.1] Packages and libs
import pandas as pd
from pycirclize import Circos
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from plotly.subplots import make_subplots
import numpy as np
import plotly

# [0.2] Data
Arrivals_df = pd.read_excel(r'Raw Data/Appendix2_DistributionData.xlsx', 2)
Departure_df = pd.read_excel(r'Raw Data/Appendix2_DistributionData.xlsx', 3)
Arrivals_df['First Record'] = Arrivals_df['First_Record']
Arrivals_df.drop('First_Record', axis=1, inplace=True)
ModelResults_df = pd.read_csv(r'Updated Data/models_data.csv')

# [1] Temporal Analysis
# [1.0] Tables Preparation
Arrivals_df_total = Arrivals_df.copy()
Arrivals_df_BF = Arrivals_df[Arrivals_df['Group'] == 'Butterfly'].copy()
Arrivals_df_Moth = Arrivals_df[Arrivals_df['Group'] != 'Butterfly'].copy()
Arrivals_df_MiMoth = Arrivals_df[Arrivals_df['Group'] == 'Micro-moth'].copy()
Arrivals_df_MaMoth = Arrivals_df[Arrivals_df['Group'] == 'Macro-moth'].copy()

# [1.1] Global
# [1.1.1] Total Lepidoptera
df_total = Arrivals_df_total.dropna(subset=["First Record"]).copy()
df_total['First Record'] = pd.to_numeric(df_total['First Record'])
first_record_counts_total = df_total['First Record'].value_counts().sort_index()
cumulative_counts_total = first_record_counts_total.cumsum()
x_min_total = df_total["First Record"].min()
end_year_total = df_total["First Record"].max()

fig_total = go.Figure()
fig_total.add_trace(go.Scatter(
    x=first_record_counts_total.index,
    y=first_record_counts_total.values,
    mode='markers',
    marker=dict(size=5, color='black'),
    name="First Record Rate"))
fig_total.add_trace(go.Scatter(
    x=cumulative_counts_total.index,
    y=cumulative_counts_total.values,
    mode='lines',
    line=dict(color='red', width=2),
    name="Cumulative Count",
    yaxis="y2"))
fig_total.update_layout(
    title="First Record Rate and Cumulative Count Over Time - Total Lepidoptera",
    xaxis=dict(title="Year", showgrid=False, range=[1500, None]),
    yaxis=dict(
        title="First Record Rate",
        showgrid=True,
        side="left"),
    yaxis2=dict(
        title="Cumulative Count",
        overlaying="y",
        side="right",
        showgrid=False),
    template="plotly_white",
    legend=dict(x=0.05, y=0.95))
fig_total.update_layout(showlegend=False)
fig_total.show()
fig_total.write_image(r"../FirstRecords_Total.png", width=1000, height=400, scale=2)

# [1.1.2] Butterflies
df_BF = Arrivals_df_BF.dropna(subset=["First Record"]).copy()
df_BF['First Record'] = pd.to_numeric(df_BF['First Record'])
first_record_counts_BF = df_BF['First Record'].value_counts().sort_index()
cumulative_counts_BF = first_record_counts_BF.cumsum()
x_min_BF = df_BF["First Record"].min()
end_year_BF = df_BF["First Record"].max()

fig_BF = go.Figure()
fig_BF.add_trace(go.Scatter(
    x=first_record_counts_BF.index,
    y=first_record_counts_BF.values,
    mode='markers',
    marker=dict(size=5, color='black'),
    name="First Record Rate"))
fig_BF.add_trace(go.Scatter(
    x=cumulative_counts_BF.index,
    y=cumulative_counts_BF.values,
    mode='lines',
    line=dict(color='red', width=2),
    name="Cumulative Count",
    yaxis="y2"))
fig_BF.update_layout(
    title="First Record Rate and Cumulative Count Over Time - Butterflies",
    xaxis=dict(title="Year", showgrid=False, range=[1500, None]),
    yaxis=dict(
        title="First Record Rate",
        showgrid=True,
        side="left"),
    yaxis2=dict(
        title="Cumulative Count",
        overlaying="y",
        side="right",
        showgrid=False),
    template="plotly_white",
    legend=dict(x=0.05, y=0.95))
fig_BF.update_layout(showlegend=False)
fig_BF.show()
fig_BF.write_image(r"../FirstRecords_Butterflies.png", width=1000, height=400, scale=2)

# [1.1.3] Moths
df_Moth = Arrivals_df_Moth.dropna(subset=["First Record"]).copy()
df_Moth['First Record'] = pd.to_numeric(df_Moth['First Record'])
first_record_counts_Moth = df_Moth['First Record'].value_counts().sort_index()
cumulative_counts_Moth = first_record_counts_Moth.cumsum()
x_min_Moth = df_Moth["First Record"].min()
end_year_Moth = df_Moth["First Record"].max()

fig_Moth = go.Figure()
fig_Moth.add_trace(go.Scatter(
    x=first_record_counts_Moth.index,
    y=first_record_counts_Moth.values,
    mode='markers',
    marker=dict(size=5, color='black'),
    name="First Record Rate"))
fig_Moth.add_trace(go.Scatter(
    x=cumulative_counts_Moth.index,
    y=cumulative_counts_Moth.values,
    mode='lines',
    line=dict(color='red', width=2),
    name="Cumulative Count",
    yaxis="y2"))
fig_Moth.update_layout(
    title="First Record Rate and Cumulative Count Over Time - Total Moths",
    xaxis=dict(title="Year", showgrid=False, range=[1500, None]),
    yaxis=dict(
        title="First Record Rate",
        showgrid=True,
        side="left"),
    yaxis2=dict(
        title="Cumulative Count",
        overlaying="y",
        side="right",
        showgrid=False),
    template="plotly_white",
    legend=dict(x=0.05, y=0.95))
fig_Moth.update_layout(showlegend=False)
fig_Moth.show()
fig_Moth.write_image(r"../FirstRecords_Moths.png", width=1000, height=400, scale=2)

# [1.1.3.1] Micro-moths
df_MiMoth = Arrivals_df_MiMoth.dropna(subset=["First Record"]).copy()
df_MiMoth['First Record'] = pd.to_numeric(df_Moth['First Record'])
first_record_counts_MiMoth = df_MiMoth['First Record'].value_counts().sort_index()
cumulative_counts_MiMoth = first_record_counts_MiMoth.cumsum()
x_min_MiMoth = df_MiMoth["First Record"].min()
end_year_MiMoth = df_MiMoth["First Record"].max()

fig_MiMoth = go.Figure()
fig_MiMoth.add_trace(go.Scatter(
    x=first_record_counts_MiMoth.index,
    y=first_record_counts_MiMoth.values,
    mode='markers',
    marker=dict(size=5, color='black'),
    name="First Record Rate"))
fig_MiMoth.add_trace(go.Scatter(
    x=cumulative_counts_MiMoth.index,
    y=cumulative_counts_MiMoth.values,
    mode='lines',
    line=dict(color='red', width=2),
    name="Cumulative Count",
    yaxis="y2"))
fig_MiMoth.update_layout(
    title="First Record Rate and Cumulative Count Over Time - Micro-moths",
    xaxis=dict(title="Year", showgrid=False, range=[1500, None]),
    yaxis=dict(
        title="First Record Rate",
        showgrid=True,
        side="left"),
    yaxis2=dict(
        title="Cumulative Count",
        overlaying="y",
        side="right",
        showgrid=False),
    template="plotly_white",
    legend=dict(x=0.05, y=0.95))
fig_MiMoth.update_layout(showlegend=False)
fig_MiMoth.show()
fig_MiMoth.write_image(r"../FirstRecords_MicroMoths.png", width=1000, height=400, scale=2)

# [1.1.3.2] Macro-moths
df_MaMoth = Arrivals_df_MaMoth.dropna(subset=["First Record"]).copy()
df_MaMoth['First Record'] = pd.to_numeric(df_Moth['First Record'])
first_record_counts_MaMoth = df_MaMoth['First Record'].value_counts().sort_index()
cumulative_counts_MaMoth = first_record_counts_MaMoth.cumsum()
x_min_MaMoth = df_MaMoth["First Record"].min()
end_year_MaMoth = df_MaMoth["First Record"].max()

fig_MaMoth = go.Figure()
fig_MaMoth.add_trace(go.Scatter(
    x=first_record_counts_MaMoth.index,
    y=first_record_counts_MaMoth.values,
    mode='markers',
    marker=dict(size=5, color='black'),
    name="First Record Rate"))
fig_MaMoth.add_trace(go.Scatter(
    x=cumulative_counts_MaMoth.index,
    y=cumulative_counts_MaMoth.values,
    mode='lines',
    line=dict(color='red', width=2),
    name="Cumulative Count",
    yaxis="y2"))
fig_MaMoth.update_layout(
    title="First Record Rate and Cumulative Count Over Time - Macro-moths",
    xaxis=dict(title="Year", showgrid=False, range=[1500, None]),
    yaxis=dict(
        title="First Record Rate",
        showgrid=True,
        side="left"),
    yaxis2=dict(
        title="Cumulative Count",
        overlaying="y",
        side="right",
        showgrid=False),
    template="plotly_white",
    legend=dict(x=0.05, y=0.95))
fig_MaMoth.update_layout(showlegend=False)
fig_MaMoth.show()
fig_MaMoth.write_image(r"../FirstRecords_MacroMoths.png", width=1000, height=400, scale=2)

# [1.1.4] Combined Figure

x_range = [1500, max(
    df_total["First Record"].max(),
    df_BF["First Record"].max(),
    df_Moth["First Record"].max(),
    df_MiMoth["First Record"].max(),
    df_MaMoth["First Record"].max())]

fig_combined = make_subplots(rows=5, cols=1, 
                    #column_widths=[0.90,0.10], 
                    shared_yaxes=False, 
                    subplot_titles=['Total Lepidoptera',
                                    'Butterflies',
                                    'Total Moths',
                                    'Macro-moths',
                                    'Micro-moths'],
                    specs=[[{"secondary_y": True}],[{"secondary_y": True}],[{"secondary_y": True}],[{"secondary_y": True}],[{"secondary_y": True}]]) 


fig_total.update_layout(showlegend=False)
fig_BF.update_layout(showlegend=False)
              
fig_combined.add_trace(go.Scatter(
    x=first_record_counts_total.index,
    y=first_record_counts_total.values,
    mode='markers',
    marker=dict(size=5, color='black'),
    name="First Records",
    showlegend=False), 
              row=1, col=1)

fig_combined.add_trace(go.Scatter(
    x=cumulative_counts_total.index,
    y=cumulative_counts_total.values,
    mode='lines',
    line=dict(color='red', width=2),
    name="Cumulative Count",
    yaxis="y2",
    showlegend=False), 
              row=1, col=1, secondary_y=True)

fig_combined.update_yaxes(row=1, col=1, secondary_y=False)
fig_combined.update_yaxes(row=1, col=1, secondary_y=True)
fig_combined.update_yaxes(automargin=False, row=1, col=1, secondary_y=True)
fig_combined.update_xaxes(range=x_range, row=1, col=1)



fig_combined.add_trace(go.Scatter(
    x=first_record_counts_BF.index,
    y=first_record_counts_BF.values,
    mode='markers',
    marker=dict(size=5, color='black'),
    name="First Records",
    showlegend=False), 
              row=2, col=1)

fig_combined.add_trace(go.Scatter(
    x=cumulative_counts_BF.index,
    y=cumulative_counts_BF.values,
    mode='lines',
    line=dict(color='red', width=2),
    name="Cumulative Count",
    yaxis="y2",
    showlegend=False), 
              row=2, col=1, secondary_y=True)

fig_combined.update_yaxes(row=2, col=1, secondary_y=False)
fig_combined.update_yaxes(row=2, col=1, secondary_y=True)
fig_combined.update_yaxes(automargin=False, row=2, col=1, secondary_y=True)
fig_combined.update_xaxes(range=x_range, row=2, col=1)

fig_combined.add_trace(go.Scatter(
    x=first_record_counts_Moth.index,
    y=first_record_counts_Moth.values,
    mode='markers',
    marker=dict(size=5, color='black'),
    name="First Records",
    showlegend=False), 
              row=3, col=1)

fig_combined.add_trace(go.Scatter(
    x=cumulative_counts_Moth.index,
    y=cumulative_counts_Moth.values,
    mode='lines',
    line=dict(color='red', width=2),
    name="Cumulative Count",
    yaxis="y2",
    showlegend=False), 
              row=3, col=1, secondary_y=True)
fig_combined.update_yaxes(title_text="First Record Rate", row=3, col=1, secondary_y=False)
fig_combined.update_yaxes(title_text="Cumulative Count", row=3, col=1, secondary_y=True)
fig_combined.update_yaxes(automargin=False, row=3, col=1, secondary_y=True)
fig_combined.update_xaxes(range=x_range, row=3, col=1)



fig_combined.add_trace(go.Scatter(
    x=first_record_counts_MaMoth.index,
    y=first_record_counts_MaMoth.values,
    mode='markers',
    marker=dict(size=5, color='black'),
    name="First Records",
    showlegend=False), 
              row=4, col=1)

fig_combined.add_trace(go.Scatter(
    x=cumulative_counts_MaMoth.index,
    y=cumulative_counts_MaMoth.values,
    mode='lines',
    line=dict(color='red', width=2),
    name="Cumulative Count",
    yaxis="y2",
    showlegend=False), 
              row=4, col=1, secondary_y=True)

fig_combined.update_yaxes(row=4, col=1, secondary_y=False)
fig_combined.update_yaxes(row=4, col=1, secondary_y=True)
fig_combined.update_yaxes(automargin=False, row=4, col=1, secondary_y=True)
fig_combined.update_xaxes(range=x_range, row=4, col=1)





fig_combined.add_trace(go.Scatter(
    x=first_record_counts_MiMoth.index,
    y=first_record_counts_MiMoth.values,
    mode='markers',
    marker=dict(size=5, color='black'),
    name="First Records"), 
              row=5, col=1)

fig_combined.add_trace(go.Scatter(
    x=cumulative_counts_MiMoth.index,
    y=cumulative_counts_MiMoth.values,
    mode='lines',
    line=dict(color='red', width=2),
    name="Cumulative Count",
    yaxis="y2"), 
              row=5, col=1, secondary_y=True)

fig_combined.update_yaxes(row=5, col=1, secondary_y=False)
fig_combined.update_yaxes(row=5, col=1, secondary_y=True)
fig_combined.update_yaxes(automargin=False, row=5, col=1, secondary_y=True)
fig_combined.update_xaxes(range=x_range, row=5, col=1)

fig_combined.update_layout(showlegend=True,
                           height=900, width=1000, 
                           template="plotly_white",
                           legend=dict(x=0.05, y=-0.15))

fig_combined.show()
fig_combined.write_image(r"Figures/FirstRecords_Combined.png", width=1000, height=900, scale=2)

# [1.2] By Continent
df_africa = Arrivals_df.dropna(subset=["First Record"]).copy()
df_africa = df_africa[df_africa["Continent"] == "Africa"].copy()
df_africa["First Record"] = pd.to_numeric(df_africa["First Record"])
first_record_counts_africa = df_africa["First Record"].value_counts().sort_index()
cumulative_counts_africa = first_record_counts_africa.cumsum()

df_asia = Arrivals_df.dropna(subset=["First Record"]).copy()
df_asia = df_asia[df_asia["Continent"] == "Asia"].copy()
df_asia["First Record"] = pd.to_numeric(df_asia["First Record"])
first_record_counts_asia = df_asia["First Record"].value_counts().sort_index()
cumulative_counts_asia = first_record_counts_asia.cumsum()

df_Australia = Arrivals_df.dropna(subset=["First Record"]).copy()
df_Australia = df_Australia[df_Australia["Continent"] == "Australia"].copy()
df_Australia["First Record"] = pd.to_numeric(df_Australia["First Record"])
first_record_counts_Australia = df_Australia["First Record"].value_counts().sort_index()
cumulative_counts_Australia = first_record_counts_Australia.cumsum()

df_Oceania = Arrivals_df.dropna(subset=["First Record"]).copy()
df_Oceania = df_Oceania[df_Oceania["Continent"] == "Oceania"].copy()
df_Oceania["First Record"] = pd.to_numeric(df_Oceania["First Record"])
first_record_counts_Oceania = df_Oceania["First Record"].value_counts().sort_index()
cumulative_counts_Oceania = first_record_counts_Oceania.cumsum()

df_Europe = Arrivals_df.dropna(subset=["First Record"]).copy()
df_Europe = df_Europe[df_Europe["Continent"] == "Europe"].copy()
df_Europe["First Record"] = pd.to_numeric(df_Europe["First Record"])
first_record_counts_Europe = df_Europe["First Record"].value_counts().sort_index()
cumulative_counts_Europe = first_record_counts_Europe.cumsum()

df_North_America = Arrivals_df.dropna(subset=["First Record"]).copy()
df_North_America = df_North_America[df_North_America["Continent"] == "North America"].copy()
df_North_America["First Record"] = pd.to_numeric(df_North_America["First Record"])
first_record_counts_North_America = df_North_America["First Record"].value_counts().sort_index()
cumulative_counts_North_America = first_record_counts_North_America.cumsum()

df_South_America = Arrivals_df.dropna(subset=["First Record"]).copy()
df_South_America = df_South_America[df_South_America["Continent"] == "South America"].copy()
df_South_America["First Record"] = pd.to_numeric(df_South_America["First Record"])
first_record_counts_South_America = df_South_America["First Record"].value_counts().sort_index()
cumulative_counts_South_America = first_record_counts_South_America.cumsum()

fig_continents_cumulative = go.Figure()
fig_continents_cumulative.add_trace(go.Scatter(
    x=cumulative_counts_africa.index,
    y=cumulative_counts_africa.values,
    mode='lines',
    line=dict(color='#1f77b4', width=2),
    name="Africa",
    yaxis="y2"))
fig_continents_cumulative.add_trace(go.Scatter(
    x=cumulative_counts_asia.index,
    y=cumulative_counts_asia.values,
    mode='lines',
    line=dict(color='#ff7f0e', width=2),
    name="Asia",
    yaxis="y2"))
fig_continents_cumulative.add_trace(go.Scatter(
    x=cumulative_counts_Australia.index,
    y=cumulative_counts_Australia.values,
    mode='lines',
    line=dict(color='#d62728', width=2),
    name="Australia",
    yaxis="y2"))
fig_continents_cumulative.add_trace(go.Scatter(
    x=cumulative_counts_Oceania.index,
    y=cumulative_counts_Oceania.values,
    mode='lines',
    line=dict(color='#bcbd22', width=2),
    name="Oceania",
    yaxis="y2"))
fig_continents_cumulative.add_trace(go.Scatter(
    x=cumulative_counts_Europe.index,
    y=cumulative_counts_Europe.values,
    mode='lines',
    line=dict(color='#8c564b', width=2),
    name="Europe",
    yaxis="y2"))
fig_continents_cumulative.add_trace(go.Scatter(
    x=cumulative_counts_North_America.index,
    y=cumulative_counts_North_America.values,
    mode='lines',
    line=dict(color='#e377c2', width=2),
    name="North America",
    yaxis="y2"))
fig_continents_cumulative.add_trace(go.Scatter(
    x=cumulative_counts_South_America.index,
    y=cumulative_counts_South_America.values,
    mode='lines',
    line=dict(color='#17becf', width=2),
    name="South America",
    yaxis="y2"))
fig_continents_cumulative.update_layout(
    title="First Record Rate and Cumulative Count Over Time",
    xaxis=dict(title="Year", showgrid=False, range=[1500, None]),
    yaxis=dict(title="Cumulative Count", overlaying="y", side="left", showgrid=False),
    template="plotly_white",
    legend=dict(x=0.05, y=0.95))
fig_continents_cumulative.show()
fig_continents_cumulative.write_image(r"Figures/FirstRecords_Continents.png", width=1000, height=400, scale=2)


# [2] Regions Analysis
# [2.0] Tables Preparation
Arrivals_df.rename(columns={'First_Observation': 'First Record'}, inplace=True)
Arrivals_no_nulls_regions = Arrivals_df.dropna(subset=['Region']).copy()
Departure_df.dropna(subset=['Continent'], inplace=True)

# [2.1] Most Prevalent Species
# [2.1.1] Total Lepidoptera
print("Top 10 most prevalent Lepidopteran",Arrivals_no_nulls_regions.value_counts('Species')[Arrivals_no_nulls_regions.value_counts('Species')>(Arrivals_no_nulls_regions.value_counts('Species').head(10).values[-1])-1])
print("Total number of introduced established Lepidopteran species:",len(Arrivals_no_nulls_regions['Species'].value_counts()))
print("Total number of introduced established Lepidopteran species in 10 or more regions:",len(Arrivals_no_nulls_regions.value_counts('Species')[Arrivals_no_nulls_regions.value_counts('Species')>9]))

# [2.1.2] Butterflies
print("Top 10 most prevalent Butterfly",Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] == 'Butterfly', 'Species'].value_counts()[Arrivals_no_nulls_regions.value_counts('Species')>(Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] == 'Butterfly', 'Species'].value_counts().head(10).values[-1])-1])
print("Total number of introduced established Butterfly species:", len(Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] == 'Butterfly', 'Species'].value_counts()))

# [2.1.3] Moths
print("Top 10 most prevalent Moth",Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] != 'Butterfly', 'Species'].value_counts()[Arrivals_no_nulls_regions.value_counts('Species')>(Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] != 'Butterfly', 'Species'].value_counts().head(10).values[-1])-1])
print("Total number of introduced established Moth species:", len(Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] != 'Butterfly', 'Species'].value_counts()))

# [2.1.3.1] Macro-moths
print("Top 10 most prevalent Macro-moth",Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] == 'Macro-moth', 'Species'].value_counts()[Arrivals_no_nulls_regions.value_counts('Species')>(Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] == 'Macro-moth', 'Species'].value_counts().head(10).values[-1])-1])
print("Total number of introduced established Macro-moth species:", len(Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] == 'Macro-moth', 'Species'].value_counts()))

# [2.1.3.2] Micro-moths
print("Top 10 most prevalent Micro-moth",Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] == 'Micro-moth', 'Species'].value_counts()[Arrivals_no_nulls_regions.value_counts('Species')>(Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] == 'Micro-moth', 'Species'].value_counts().head(10).values[-1])-1])
print("Total number of introduced established Micro-moth species:", len(Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] == 'Micro-moth', 'Species'].value_counts()))


# [2.2] Most Invaded Regions
# [2.2.1] Total Lepidoptera
print("Top 10 most invaded regions - Lepidoptera",Arrivals_no_nulls_regions.value_counts('Region').head(10))
print("Regions with more than 65 recorded Lepidoptera species", Arrivals_no_nulls_regions.value_counts('Region')[Arrivals_no_nulls_regions.value_counts('Region')>65])
print("Total number of invaded regions",len(Arrivals_no_nulls_regions.value_counts('Region')))
print("Total number of invaded regions with more than 9 species",len(Arrivals_no_nulls_regions.value_counts('Region')[Arrivals_no_nulls_regions.value_counts('Region')>9]))

# [2.2.2] Butterflies
print("Top 10 most invaded regions - Butterlies", Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] == 'Butterfly', 'Region'].value_counts().head(10))
print("Regions with more than 2 recorded Butterfly species", Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] == 'Butterfly', 'Region'].value_counts().loc[lambda x: x >= 3])
print("Total number of Regions with Butterfly species", len(Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] == 'Butterfly', 'Region'].value_counts()))

# [2.2.3] Moths
print("Top 10 most invaded regions - Moths", Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] != 'Butterfly', 'Region'].value_counts().head(10))
print("Regions with more than 65 recorded Moth species", Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] != 'Butterfly', 'Region'].value_counts().loc[lambda x: x >= 65])
print("Total number of Regions with Moth species", len(Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] != 'Butterfly', 'Region'].value_counts()))

# [2.2.3.1] Macro-moths
print("Top 10 most invaded regions - Macro-moths", Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] == 'Macro-moth', 'Region'].value_counts().head(10))
print("Regions with more than 65 recorded Macro-moth species", Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] == 'Macro-moth', 'Region'].value_counts().loc[lambda x: x >= 65])
print("Total number of Regions with Macro-moth species", len(Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] == 'Macro-moth', 'Region'].value_counts()))


# [2.2.3.2] Micro-moths
print("Top 10 most invaded regions - Micro-moths", Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] == 'Micro-moth', 'Region'].value_counts().head(10))
print("Regions with more than 65 recorded Micro-moth species", Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] == 'Micro-moth', 'Region'].value_counts().loc[lambda x: x >= 65])
print("Total number of Regions with Micro-moth species", len(Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Group'] == 'Micro-moth', 'Region'].value_counts()))


# [3] Histograms
species_regions = (Arrivals_df.groupby(['Species', 'Group'])['Region'].nunique().reset_index().sort_values(by='Region', ascending=False))
species_regions['Region'] = pd.to_numeric(species_regions['Region'], errors='coerce')

bin_edges = [0, 1, 3, 7, 15, 31, np.inf]
bin_labels = ['1', '2–3', '4–7', '8-15', '16–31', '>31']
bin_edges_bf = [0, 1, 3, 7, 15, np.inf]
bin_labels_bf = ['1', '2–3', '4–7', '8-15', '>15']

species_regions['Region_Bin'] = pd.cut(species_regions['Region'],bins=bin_edges,labels=bin_labels,right=True)
total_counts = (species_regions['Region_Bin'].value_counts().reindex(bin_labels, fill_value=0))

bf_data = species_regions[species_regions['Group'] == 'Butterfly'].copy()
bf_data['Region_Bin_BF'] = pd.cut(bf_data['Region'], bins=bin_edges_bf, labels=bin_labels_bf, right=True)
bf_counts = (bf_data['Region_Bin_BF'].value_counts().reindex(bin_labels_bf, fill_value=0))

moth_data = species_regions[species_regions['Group'] != 'Butterfly']
macro_moth = moth_data[moth_data['Group'] == 'Macro-moth']
micro_moth = moth_data[moth_data['Group'] == 'Micro-moth']
macro_counts = (macro_moth['Region_Bin'].value_counts().reindex(bin_labels, fill_value=0))
micro_counts = (micro_moth['Region_Bin'].value_counts().reindex(bin_labels, fill_value=0))


hists = make_subplots(
    rows=1,
    cols=3,
    subplot_titles=("Total Lepidoptera", "Butterflies", "Moths"))

hists.add_trace(
    go.Bar(x=bin_labels,
        y=total_counts.values,
        name='Total Lepidoptera',
        marker_color='#880808'),
    row=1, col=1)

hists.add_trace(
    go.Bar(x=bin_labels_bf,
        y=bf_counts.values,
        name='Butterflies',
        marker_color='#EE4B2B'),
    row=1, col=2)

hists.add_trace(
    go.Bar(x=bin_labels,
        y=micro_counts.values,
        name='Micro-moth',
        marker_color='#AA4A44'),
    row=1, col=3)

hists.add_trace(
    go.Bar(x=bin_labels,
        y=macro_counts.values,
        name='Macro-moth',
        marker_color='#FF7F7F'),
    row=1, col=3)

hists.update_layout(
    barmode='stack',
    showlegend=True,
    height=400,
    width=1000,
    bargap=0.2,
    template="plotly_white",
    font=dict(family="Arial, sans-serif"),
    annotations=[
        dict(text="<b>Total Lepidoptera</b>", x=0.16, y=1.08, xref="paper", yref="paper", showarrow=False, font=dict(size=16)),
        dict(text="<b>Butterflies</b>", x=0.5, y=1.08, xref="paper", yref="paper", showarrow=False, font=dict(size=16)),
        dict(text="<b>Moths</b>", x=0.84, y=1.08, xref="paper", yref="paper", showarrow=False, font=dict(size=16))])

hists.update_xaxes(title_text="Number of Regions", row=1, col=1)
hists.update_xaxes(title_text="Number of Regions", row=1, col=2)
hists.update_xaxes(title_text="Number of Regions", row=1, col=3)
hists.update_yaxes(title_text="Number of Species", row=1, col=1)
hists.show()
hists.write_image(r"Figures/Histograms.png", width=900, height=400, scale=2)


# [4] Flow Analysis
# [4.0] Pivot Tables
# [4.0.1] Total Lepidoptera
entry_continents_total = Arrivals_df[['Species', 'Continent']].drop_duplicates().copy()
outs_continents_total = Departure_df[['Species', 'Continent']].drop_duplicates().copy()
merged_continents_total = pd.merge( outs_continents_total, entry_continents_total, on='Species', suffixes=('_outs', '_entry'))
pivot_table_continents_total = merged_continents_total.pivot_table(
    index='Continent_outs',
    columns='Continent_entry',
    values='Species',
    aggfunc='nunique',  
    fill_value=0)

# [4.0.2] Butterflies
entry_continents_BF = Arrivals_df[['Species', 'Continent', 'Group']].drop_duplicates().copy()
entry_continents_BF = entry_continents_BF[entry_continents_BF['Group'] == 'Butterfly']
entry_continents_BF = entry_continents_BF[['Species', 'Continent']].drop_duplicates()
outs_continents_BF = Departure_df[['Species', 'Continent']].drop_duplicates()
merged_continents_BF = pd.merge( outs_continents_BF, entry_continents_BF, on='Species', suffixes=('_outs', '_entry'))
pivot_table_continents_BF = merged_continents_BF.pivot_table(
    index='Continent_outs',
    columns='Continent_entry',
    values='Species',
    aggfunc='nunique',  
    fill_value=0)

# [4.0.3] Moths
entry_continents_Moth = Arrivals_df[['Species', 'Continent', 'Group']].drop_duplicates().copy()
entry_continents_Moth = entry_continents_Moth[entry_continents_Moth['Group'] != 'Butterfly']
entry_continents_Moth = entry_continents_Moth[['Species', 'Continent']].drop_duplicates()
outs_continents_Moth = Departure_df[['Species', 'Continent']].drop_duplicates()
merged_continents_Moth = pd.merge( outs_continents_Moth, entry_continents_Moth, on='Species', suffixes=('_outs', '_entry'))
pivot_table_continents_Moth = merged_continents_Moth.pivot_table(
    index='Continent_outs',
    columns='Continent_entry',
    values='Species',
    aggfunc='nunique',  
    fill_value=0)

# [4.0.3.1] Micro-moths
entry_continents_MiMoth = Arrivals_df[['Species', 'Continent', 'Group']].drop_duplicates().copy()
entry_continents_MiMoth = entry_continents_MiMoth[entry_continents_MiMoth['Group'] == 'Micro-moth']
entry_continents_MiMoth = entry_continents_MiMoth[['Species', 'Continent']].drop_duplicates()
outs_continents_MiMoth = Departure_df[['Species', 'Continent']].drop_duplicates()
merged_continents_MiMoth = pd.merge( outs_continents_MiMoth, entry_continents_MiMoth, on='Species', suffixes=('_outs', '_entry'))
pivot_table_continents_MiMoth = merged_continents_MiMoth.pivot_table(
    index='Continent_outs',
    columns='Continent_entry',
    values='Species',
    aggfunc='nunique',  
    fill_value=0)

# [4.0.3.2] Macro-moths
entry_continents_MaMoth = Arrivals_df[['Species', 'Continent', 'Group']].drop_duplicates().copy()
entry_continents_MaMoth = entry_continents_MaMoth[entry_continents_MaMoth['Group'] == 'Macro-moth']
entry_continents_MaMoth = entry_continents_MaMoth[['Species', 'Continent']].drop_duplicates()
outs_continents_MaMoth = Departure_df[['Species', 'Continent']].drop_duplicates()
merged_continents_MaMoth = pd.merge( outs_continents_MaMoth, entry_continents_MaMoth, on='Species', suffixes=('_outs', '_entry'))
pivot_table_continents_MaMoth = merged_continents_MaMoth.pivot_table(
    index='Continent_outs',
    columns='Continent_entry',
    values='Species',
    aggfunc='nunique',  
    fill_value=0)

# [4.1] Circlize Preparation
def link_kws_handler(from_label: str, to_label: str):
    if from_label in ("C", "G"):
        return dict(alpha=0.7, zorder=1.0)
    else:
        return dict(alpha=0.7, zorder=0)

colordic = {
    "Africa": '#1f77b4',
    "Asia": '#ff7f0e',
    "Australia": '#d62728',
    "Europe": '#8c564b',
    "North America": '#e377c2',
    "Oceania": '#bcbd22',
    "South America": '#17becf',}

# [4.2] Continents Analysis
# [4.2.1] Total Lepidoptera
circos_continental_directional_total = Circos.initialize_from_matrix(
    pivot_table_continents_total,
    space=5,
    cmap=colordic,
    label_kws=dict(size=16, family="sans-serif", weight="bold"),
    link_kws=dict(direction=1, ec="white", lw=1, alpha = 2, arrow_length_ratio = 0.07),
    link_kws_handler=link_kws_handler,
    order = "asc",)
circos_continental_directional_total.plotfig()
plt.title("Total Lepidoptera", fontsize=18, weight="bold", pad=20)
plt.show()
circos_continental_directional_total.savefig("Figures/Circos_continental_directional_total.png", dpi=300)

# [4.2.2] Butterflies
circos_continental_directional_BF = Circos.initialize_from_matrix(
    pivot_table_continents_BF,
    space=5,
    cmap=colordic,
    label_kws=dict(size=16, family="sans-serif", weight="bold"), 
    link_kws=dict(direction=1, ec="white", lw=1, alpha = 2, arrow_length_ratio = 0.07),
    link_kws_handler=link_kws_handler,
    order = "asc",)
circos_continental_directional_BF.plotfig()
plt.title("Butterflies", fontsize=18, weight="bold", pad=20)
plt.show()
circos_continental_directional_BF.savefig("Figures/Circos_continental_directional_BF.png", dpi=300)

# [4.2.3] Moths
circos_continental_directional_Moth = Circos.initialize_from_matrix(
    pivot_table_continents_Moth,
    space=5,
    cmap=colordic,
    label_kws=dict(size=16, family="sans-serif", weight="bold"),
    link_kws=dict(direction=1, ec="white", lw=1, alpha = 2, arrow_length_ratio = 0.07),
    link_kws_handler=link_kws_handler,
    order = "asc",)
circos_continental_directional_Moth.plotfig()
plt.title("Moths", fontsize=18, weight="bold", pad=20)
plt.show()
circos_continental_directional_Moth.savefig("Figures/Circos_continental_directional_Moth.png", dpi=300)

# [4.2.3.1] Micro-moths
circos_continental_directional_MiMoth = Circos.initialize_from_matrix(
    pivot_table_continents_MiMoth,
    space=5,
    cmap=colordic,
    label_kws=dict(size=16, family="sans-serif", weight="bold"),
    link_kws=dict(direction=1, ec="white", lw=1, alpha = 2, arrow_length_ratio = 0.07),
    link_kws_handler=link_kws_handler,
    order = "asc",)
circos_continental_directional_MiMoth.plotfig()
plt.title("Micro-moths", fontsize=18, weight="bold", pad=20)
plt.show()
circos_continental_directional_MiMoth.savefig("Figures/Circos_continental_directional_MiMoth.png", dpi=300)

# [4.2.3.2] Macro-moths
circos_continental_directional_MaMoth = Circos.initialize_from_matrix(
    pivot_table_continents_MaMoth,
    space=5,
    cmap=colordic,
    label_kws=dict(size=16, family="sans-serif", weight="bold"),
    link_kws=dict(direction=1, ec="white", lw=1, alpha = 2, arrow_length_ratio = 0.07),
    link_kws_handler=link_kws_handler,
    order = "asc",)
circos_continental_directional_MaMoth.plotfig()
plt.title("Macro-moths", fontsize=18, weight="bold", pad=20)
plt.show()
circos_continental_directional_MaMoth.savefig("Figures/Circos_continental_directional_MaMoth.png", dpi=300)


# [5] Model Forest Plots

# [5.1] Data Preparation
ModelResults_df_no_intercept = ModelResults_df[ModelResults_df['term'] != '(Intercept)'].copy()
ModelResults_df_no_intercept['term'] = ModelResults_df_no_intercept['term'].replace(
    {'InvBias_SC': 'Invasion Bias Score',
     'AnnualPrecipitation': 'Annual Precipitation',
     'MeanAnnualTemperature': 'Mean Annual Temperature',
     'Forest_Area_100': 'Forest Area',
     'Urban_Area_100': 'Urban Area',
     'AgricultureCultivated_Area_100': 'Cropland Area',
     'DensPop': 'Population Density',
     'Area_SqKms': 'Area',
     'GDP_AVG5Y': 'GDP'})

order = ['Island', 
         'Area', 
         'GDP', 
         'Population Density', 
         'Cropland Area', 
         'Urban Area', 
         'Forest Area', 
         'Mean Annual Temperature', 
         'Annual Precipitation', 
         'Invasion Bias Score']
reverse_order = order[::-1]

ModelResults_df_no_intercept['term'] = pd.Categorical(ModelResults_df_no_intercept['term'], categories=reverse_order, ordered=True)
ModelResults_df_no_intercept = ModelResults_df_no_intercept.sort_values('term')

def split_significant(df):
    significant = df[~((df['conf.low'] <= 0) & (df['conf.high'] >= 0))].copy()
    nonsignificant = df[(df['conf.low'] <= 0) & (df['conf.high'] >= 0)].copy()
    
    significant['term'] = pd.Categorical(significant['term'], categories=reverse_order, ordered=True)
    nonsignificant['term'] = pd.Categorical(nonsignificant['term'], categories=reverse_order, ordered=True)
    
    return significant, nonsignificant

models_color_map = [("Total Lepidoptera", "#880808"), ("Butterflies Presence", "#EE4B2B"), ("Total Moths", "#EEA236"), ("Macro-moths", "#AA4A44"), ("Micro-moths", "#FF7F7F")]

def get_colors(df, color):
    return [
        'lightgrey' if (low <= 0 <= high) else color
        for low, high in zip(df['conf.low'], df['conf.high'])]

# [5.2] Forest Plot
forest_plot = make_subplots(
    rows=1,
    cols=5,
    subplot_titles=("Total Lepidoptera", "Butterflies", "Total Moths", "Macro-moths", "Micro-Moths"),
    shared_yaxes=True)

        
# [5.2.1] Model Loop for Forest Plot

for i, (model_name, color) in enumerate(models_color_map, start=1):

    models_df = ModelResults_df_no_intercept[ModelResults_df_no_intercept['model'] == model_name].copy()
    significant, nonsignificant = split_significant(models_df)

    forest_plot.add_trace(go.Scatter(
        x=nonsignificant['estimate'],
        y=nonsignificant['term'],
        error_x=dict(
            type='data',
            symmetric=False,
            array=nonsignificant['conf.high'] - nonsignificant['estimate'],
            arrayminus=nonsignificant['estimate'] - nonsignificant['conf.low'],
            color='lightgrey'),
        mode='markers',
        marker=dict(color='lightgrey'),
        showlegend=False), row=1, col=i)

    forest_plot.add_trace(go.Scatter(
        x=significant['estimate'],
        y=significant['term'],
        error_x=dict(
            type='data',
            symmetric=False,
            array=significant['conf.high'] - significant['estimate'],
            arrayminus=significant['estimate'] - significant['conf.low'],
            color=color),
        mode='markers',
        marker=dict(color=color),
        showlegend=False), row=1, col=i)

    forest_plot.add_vline(
        x=0,
        line=dict(color='gray', dash='dash'),
        row=1,
        col=i)
    
forest_plot.update_yaxes(
    categoryorder='array',
    categoryarray=reverse_order)    
    
forest_plot.update_layout(
    width=1000, height=400,
    title="Model Results",
    title_x=0.5,
    margin=dict(l=50, r=50, t=100, b=50),
    yaxis=dict(title="Predictors"),
    #template="plotly_white", 
    font=dict(family="Arial, sans-serif"))

forest_plot.show()
forest_plot.write_image("Figures/ForestPlot.png", width=1000, height=400, scale=2)
