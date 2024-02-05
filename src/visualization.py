import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
import os

# These are the plots used in the WORLD DATA file.

""" World Percentage and Growth Rate for Top 5 Countries """

df_world = pd.DataFrame({
    "country": ["India", "China", "United States", "Indonesia", "Pakistan"],
    "world percentage": [17.85, 17.81, 4.25, 3.47, 3.00],
    "growth rate": [0.81, -0.02, 0.50, 0.74, 1.98]
})

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(df_world["country"], df_world["world percentage"], label="Ocupation Percentage", color="blue")
ax.plot(df_world["growth rate"], df_world["country"], label="Growth Rate", color="pink")

plt.xlabel("Percentage / Growth Rate")
plt.title("World Percentage and Growth Rate for Top 5 Countries")
plt.legend();

""" Top 5 Countries with the Largest Mean Population Over Years """

result = df_grow.groupby("country")[["1990 population", "2000 population", "2010 population", "2020 population"]].mean()

sorted_result = result.sort_values(by="2020 population", ascending=False)
top5 = sorted_result.head(5)


top5.plot(kind='bar', figsize=(10, 6), title='Top 5 Countries with the Largest Mean Population Over Years', colormap="bwr")


plt.xlabel('Country')
plt.ylabel('Population')
plt.legend(title='Year');

""" Top 5 Continents by 2023 and 1990 Population """


continents = ["Asia", "North America", "Europe", "Africa", "South America"]
df_cont = df[df['continent'].isin(continents)]

continent_population = df_cont.groupby("continent")[["2023 population", "1990 population"]].sum().reset_index()
continent_population = continent_population.sort_values(by='2023 population', ascending=True)
top_5_continents = continent_population.head(5)

plt.figure(figsize=(10, 6))

sns.barplot(x='continent', y='2023 population', data=top_5_continents, color='red', label='2023 Population')
sns.barplot(x='continent', y='1990 population', data=top_5_continents, color='blue', label='1990 Population')

plt.title('Top 5 Continents by 2023 and 1990 Population')
plt.xlabel('Continent')
plt.ylabel('Population')
plt.legend()
plt.tight_layout();


""" Comparison of Area and Density for India and China """

df = pd.DataFrame({
    'country': ['India', 'China'],
    '2023 population': [1428627663, 1425671352],
    'area (km²)': [3287590.0, 9706961.0],
    'density (km²)': [481, 151]
})


df_bars = df[["country", "area (km²)", "density (km²)"]]
df_mixed = pd.melt(df_bars, id_vars = "country", var_name = "Variable", value_name="Value")
plt.figure(figsize=(12, 6))

sns.barplot(x = "Variable", y = "Value", hue = "country", data = df_mixed[df_mixed["Variable"] == "area (km²)"])
plt.legend(loc="upper left")
plt.xlabel("Country Size vs Density", fontsize=16)
plt.ylabel("Countries Size")


ax2 = plt.twinx()
sns.barplot(x="country", y="Value", hue="Variable", data=df_mixed[df_mixed["Variable"] == "density (km²)"], ax=ax2)
ax2.legend(loc='upper right')


plt.title("Comparison of Area and Density for India and China")
plt.ylabel("Countries Density");



# This is the plot definition for the cleaned API called "counting_cities".


def counting_cities(df, output_path="data/output.csv"):

   
    df['Population'] = df['Population'].astype(str).str.replace('.', '').astype(int)

    top_10_cities = df.nlargest(10, 'Population')

    sns.set(style="whitegrid")
    plt.figure(figsize=(12, 6))

    def population_formatter(x, pos):
        return '{:,}'.format(int(x))

    sns.barplot(x='City', y='Population', hue='City', data=top_10_cities, palette='gray')
   
    plt.gca().yaxis.set_major_formatter(FuncFormatter(population_formatter))
    plt.xticks(rotation=45, ha='right') 
    plt.title('Top 10 Cities by Population')
    plt.ylabel('Population')
    plt.tight_layout()
    plt.show()
   
    top_10_cities.to_csv(output_path, index=False)
