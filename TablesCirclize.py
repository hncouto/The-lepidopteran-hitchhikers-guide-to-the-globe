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
Arrivals_df = pd.read_excel(r'Appendix2_DistributionData.xlsx', 1)
Departure_df = pd.read_excel(r'Appendix2_DistributionData.xlsx', 2)


# [1] Regions Analysis
# [1.0] Tables Preparation
Arrivals_df.rename(columns={'First_Observation': 'First Record'}, inplace=True)
Arrivals_no_nulls_regions = Arrivals_df.dropna(subset=['Region']).copy()

# [1.1] Most Prevalent Species
# [1.1.1] Total Lepidoptera
print("Top 10 most prevalent Lepidopteran",Arrivals_no_nulls_regions.value_counts('Species')[Arrivals_no_nulls_regions.value_counts('Species')>(Arrivals_no_nulls_regions.value_counts('Species').head(10).values[-1])-1])
print("Total number of introduced established Lepidopteran species:",len(Arrivals_no_nulls_regions['Species'].value_counts()))
print("Total number of introduced established Lepidopteran species in 10 or more regions:",len(Arrivals_no_nulls_regions.value_counts('Species')[Arrivals_no_nulls_regions.value_counts('Species')>9]))

# [1.1.2] Moths
print("Top 10 most prevalent Moth",Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Butterfly'] == 0, 'Species'].value_counts()[Arrivals_no_nulls_regions.value_counts('Species')>(Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Butterfly'] == 0, 'Species'].value_counts().head(10).values[-1])-1])
print("Total number of introduced established Moth species:", len(Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Butterfly'] == 0, 'Species'].value_counts()))

# [1.1.3] Butterflies
print("Top 10 most prevalent Butterfly",Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Butterfly'] == 1, 'Species'].value_counts()[Arrivals_no_nulls_regions.value_counts('Species')>(Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Butterfly'] == 1, 'Species'].value_counts().head(10).values[-1])-1])
print("Total number of introduced established Butterfly species:", len(Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Butterfly'] == 1, 'Species'].value_counts()))


# [1.2] Most Invaded Regions
# [1.2.1] Total Lepidoptera
print("Top 10 most invaded regions - Lepidoptera",Arrivals_no_nulls_regions.value_counts('Region').head(10))
print("Regions with more than 65 recorded Lepidoptera species", Arrivals_no_nulls_regions.value_counts('Region')[Arrivals_no_nulls_regions.value_counts('Region')>65])
print("Total number of invaded regions",len(Arrivals_no_nulls_regions.value_counts('Region')))
print("Total number of invaded regions with more than 9 species",len(Arrivals_no_nulls_regions.value_counts('Region')[Arrivals_no_nulls_regions.value_counts('Region')>9]))

# [1.2.2] Moths
print("Top 10 most invaded regions - Moths", Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Butterfly'] == 0, 'Region'].value_counts().head(10))
print("Regions with more than 65 recorded Moth species", Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Butterfly'] == 0, 'Region'].value_counts().loc[lambda x: x >= 65])
print("Total number of Regions with Moth species", len(Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Butterfly'] == 0, 'Region'].value_counts()))

# [1.2.3] Butterflies
print("Top 10 most invaded regions - Butterlies", Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Butterfly'] == 1, 'Region'].value_counts().head(10))
print("Regions with more than 2 recorded Butterfly species", Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Butterfly'] == 1, 'Region'].value_counts().loc[lambda x: x >= 3])
print("Total number of Regions with Butterfly species", len(Arrivals_no_nulls_regions.loc[Arrivals_no_nulls_regions['Butterfly'] == 1, 'Region'].value_counts()))


# [2] Flow Analysis
# [2.0] Pivot Tables
# [2.0.1] Total Lepidoptera
entry_continents_total = Arrivals_df[['Species', 'Continent']].drop_duplicates().copy()
outs_continents_total = Departure_df[['Species', 'Continent']].drop_duplicates().copy()
merged_continents_total = pd.merge( outs_continents_total, entry_continents_total, on='Species', suffixes=('_outs', '_entry'))
pivot_table_continents_total = merged_continents_total.pivot_table(
    index='Continent_outs',
    columns='Continent_entry',
    values='Species',
    aggfunc='nunique',  
    fill_value=0)

# [2.0.2] Moths
entry_continents_NonBF = Arrivals_df[['Species', 'Continent', 'Butterfly']].drop_duplicates().copy()
entry_continents_NonBF = entry_continents_NonBF[entry_continents_NonBF['Butterfly'] == 0]
entry_continents_NonBF = entry_continents_NonBF[['Species', 'Continent']].drop_duplicates()
outs_continents_NonBF = Departure_df[['Species', 'Continent']].drop_duplicates()
merged_continents_NonBF = pd.merge( outs_continents_NonBF, entry_continents_NonBF, on='Species', suffixes=('_outs', '_entry'))
pivot_table_continents_NonBF = merged_continents_NonBF.pivot_table(
    index='Continent_outs',
    columns='Continent_entry',
    values='Species',
    aggfunc='nunique',  
    fill_value=0)

# [2.0.3] Butterflies
entry_continents_BF = Arrivals_df[['Species', 'Continent', 'Butterfly']].drop_duplicates().copy()
entry_continents_BF = entry_continents_BF[entry_continents_BF['Butterfly'] == 1]
entry_continents_BF = entry_continents_BF[['Species', 'Continent']].drop_duplicates()
outs_continents_BF = Departure_df[['Species', 'Continent']].drop_duplicates()
merged_continents_BF = pd.merge( outs_continents_BF, entry_continents_BF, on='Species', suffixes=('_outs', '_entry'))
pivot_table_continents_BF = merged_continents_BF.pivot_table(
    index='Continent_outs',
    columns='Continent_entry',
    values='Species',
    aggfunc='nunique',  
    fill_value=0)

# [2.1] Circlize Preparation
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

# [2.2] Continents Analysis
# [2.2.1] Total Lepidoptera
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

# [2.2.2] Moths
circos_continental_directional_NonBF = Circos.initialize_from_matrix(
    pivot_table_continents_NonBF,
    space=5,
    cmap=colordic,
    label_kws=dict(size=16, family="sans-serif", weight="bold"),
    link_kws=dict(direction=1, ec="white", lw=1, alpha = 2, arrow_length_ratio = 0.07),
    link_kws_handler=link_kws_handler,
    order = "asc",)
circos_continental_directional_NonBF.plotfig()
plt.title("Moths", fontsize=18, weight="bold", pad=20)
plt.show()

# [2.2.3] Butterflies
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


# [3] Temporal Analysis
# [3.0] Tables Preparation
Arrivals_df_total = Arrivals_df.copy()
Arrivals_df_NonBF = Arrivals_df[Arrivals_df['Butterfly'] == 0].copy()
Arrivals_df_BF = Arrivals_df[Arrivals_df['Butterfly'] == 1].copy()

# [3.1] Global
# [3.1.1] Total Lepidoptera
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
fig_total.show()

# [3.1.2] Moths
df_NonBF = Arrivals_df_NonBF.dropna(subset=["First Record"]).copy()
df_NonBF['First Record'] = pd.to_numeric(df_NonBF['First Record'])
first_record_counts_NonBF = df_NonBF['First Record'].value_counts().sort_index()
cumulative_counts_NonBF = first_record_counts_NonBF.cumsum()
x_min_NonBF = df_NonBF["First Record"].min()
end_year_NonBF = df_NonBF["First Record"].max()

fig_NonBF = go.Figure()
fig_NonBF.add_trace(go.Scatter(
    x=first_record_counts_NonBF.index,
    y=first_record_counts_NonBF.values,
    mode='markers',
    marker=dict(size=5, color='black'),
    name="First Record Rate"))
fig_NonBF.add_trace(go.Scatter(
    x=cumulative_counts_NonBF.index,
    y=cumulative_counts_NonBF.values,
    mode='lines',
    line=dict(color='red', width=2),
    name="Cumulative Count",
    yaxis="y2"))
fig_NonBF.update_layout(
    title="First Record Rate and Cumulative Count Over Time - Moths",
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
fig_NonBF.show()


# [3.1.3] Butterflies
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
fig_BF.show()



# [3.2] By Continent
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


# [4] Histograms
species_regions = (Arrivals_df.groupby(['Species', 'Butterfly'])['Region'].nunique().reset_index().rename(columns={'Region': 'Regions'}).sort_values(by='Regions', ascending=False))

species_regions['Regions'] = pd.to_numeric(species_regions['Regions'], errors='coerce')
bin_edges = [0, 1, 3, 7, 15, 31, np.inf]
bin_labels = ['1', '2–3', '4–7', '8-15','16–31', '>31']

species_regions['Region_Bin'] = pd.cut(species_regions['Regions'], bins=bin_edges, labels=bin_labels, right=True)
total_counts = species_regions['Region_Bin'].value_counts().reindex(bin_labels, fill_value=0)
moth_data = species_regions[species_regions['Butterfly'] == 0]
moth_counts = moth_data['Region_Bin'].value_counts().reindex(bin_labels, fill_value=0)

bin_edges_bf = [0, 1, 3, 7, 15, np.inf]
bin_labels_bf = ['1', '2–3', '4–7', '8-15','>15']
bf_data = species_regions[species_regions['Butterfly'] == 1].copy()
bf_data['Region_Bin_BF'] = pd.cut(bf_data['Regions'], bins=bin_edges_bf, labels=bin_labels_bf, right=True)
bf_counts = bf_data['Region_Bin_BF'].value_counts().reindex(bin_labels_bf, fill_value=0)

hists = make_subplots(rows=1, cols=3, subplot_titles=("Total Lepidoptera", "Moths", "Butterflies"))
hists.add_trace(
    go.Bar(x=bin_labels, y=total_counts.values, name='Total Lepidoptera', marker_color='#880808'),
    row=1, col=1)
hists.add_trace(
    go.Bar(x=bin_labels, y=moth_counts.values, name='Moths', marker_color='#AA4A44'),
    row=1, col=2)
hists.add_trace(
    go.Bar(x=bin_labels_bf, y=bf_counts.values, name='Butterflies', marker_color='#EE4B2B'),
    row=1, col=3)

hists.update_layout(
    showlegend=False,
    height=400,
    width=1000,
    bargap=0.2,
    template="plotly_white",
    font=dict(
        family="Arial, sans-serif",),
    annotations=[
        dict(
            text="<b>Total Lepidoptera</b>",
            x=0.16, y=1.08, xref="paper", yref="paper",
            showarrow=False, font=dict(size=16)),
        dict(
            text="<b>Moths</b>",
            x=0.5, y=1.08, xref="paper", yref="paper",
            showarrow=False, font=dict(size=16)),
        dict(
            text="<b>Butterflies</b>",
            x=0.84, y=1.08, xref="paper", yref="paper",
            showarrow=False, font=dict(size=16))])

hists.update_xaxes(title_text="Number of Regions", row=1, col=1)
hists.update_xaxes(title_text="Number of Regions", row=1, col=2)
hists.update_xaxes(title_text="Number of Regions", row=1, col=3)
hists.update_yaxes(title_text="Number of Species", row=1, col=1)

hists.show()

