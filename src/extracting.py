import pandas as pd
from pandas import json_normalize
from urllib.request import urlopen
import requests 
import json
from bs4 import BeautifulSoup
import os
import sys
sys.path.append("../")
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# First : We downloaded the data from world population to base start with the project. We have selected this parameters but you can change them.

file_path = r'C:\Users\ateso\Desktop\Ironhack\Project-2\data\world_data.csv'

df = pd.read_csv(file_path)

df_grow = df[["rank", "country","1990 population", "2000 population", "2010 population", "2020 population"]]
df_grow.groupby("country")[["1990 population", "2000 population", "2010 population", "2020 population"]].mean()
df_india_china = df[df["country"].isin(["India", "China"])][["country","2023 population", "area (km²)", "density (km²)"]]
df_world = df[["country","world percentage","growth rate"]].head(5)

import pandas as pd

def process_world_data(file_path):
    
    df = pd.read_csv(file_path)

    df_grow = df[["rank", "country", "1990 population", "2000 population", "2010 population", "2020 population"]]
    df_grow_mean = df_grow.groupby("country")[["1990 population", "2000 population", "2010 population", "2020 population"]].mean()

    df_india_china = df[df["country"].isin(["India", "China"])][["country", "2023 population", "area (km²)", "density (km²)"]]

    df_world_top5 = df[["country", "world percentage", "growth rate"]].head(5)

    return df_grow_mean, df_india_china, df_world_top5


# Second : We have cleaned an API from the websites and created definitions for easy usage.

url = "https://worldpopulationreview.com/countries/cities/china"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")
# "DATA CLASS" <th class="sticky left-0 z-50 border bg-clip-padding px-2 py-0.5 text-left bg-gray-100">Beijing</th>
# "DATA CLASS" <th class="sticky left-0 z-50 border bg-clip-padding px-2 py-0.5 text-left bg-white">Shanghai</th>
list_cities = soup.find_all("th", class_=["sticky left-0 z-50 border bg-clip-padding px-2 py-0.5 text-left bg-gray-100", "sticky left-0 z-50 border bg-clip-padding px-2 py-0.5 text-left bg-white"])
cities = [i.getText().strip() for i in list_cities]
# "DATA CLASS" <td class="z-40 border px-2 py-0.5">22,315,474</td>
list_population = soup.find_all("td", {"class":"z-40 border px-2 py-0.5"})
population = [i.getText().strip().replace(",", ".") for i in list_population]
population = [number.replace('"', '') for number in population]


def city_pop (url):

    city  = url.split("/")[-1]
    
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    
    #City
    list_cities = soup.find_all("th", class_=["sticky left-0 z-50 border bg-clip-padding px-2 py-0.5 text-left bg-gray-100", "sticky left-0 z-50 border bg-clip-padding px-2 py-0.5 text-left bg-white"])
    cities = [i.getText().strip() for i in list_cities]
  
    
    #Population
    list_population = soup.find_all("td", {"class":"z-40 border px-2 py-0.5"})
    population = [i.getText().strip().replace(",", ".") for i in list_population]
    population = [number.replace('"', '') for number in population]


    dict_ = {
        "City": cities,
        "Population": population,
    }
    
    df = pd.DataFrame(dict_)
    df.to_csv(f'data/output_{city}.csv', index=False)
    
    return df

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
import os

def counting_cities(df, output_path="data/output.csv"):

   
    df['Population'] = df['Population'].astype(str).str.replace('.', '').astype(int)

    top_10_cities = df.nlargest(10, 'Population')

    sns.set(style="whitegrid")
    plt.figure(figsize=(12, 6))

    def population_formatter(x, pos):
        return '{:,}'.format(int(x))

    sns.barplot(x='City', y='Population', hue='City', data=top_10_cities, palette='gray', legend=False)
   
    plt.gca().yaxis.set_major_formatter(FuncFormatter(population_formatter))
    plt.xticks(rotation=45, ha='right') 
    plt.title('Top 10 Cities by Population')
    plt.ylabel('Population')
    plt.tight_layout()
    plt.show()
   
    top_10_cities.to_csv(output_path, index=False)