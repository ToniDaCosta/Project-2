import pandas as pd
from pandas import json_normalize
import os
import src.extracting as ext
import src.visualization as viz


# Select df = file origin path, this file works for countries, change the country as needed.

df = ext.city_pop("https://worldpopulationreview.com/countries/cities/colombia")

# Use the viz. to visualize the data extracted from API

viz.counting_cities(df, "data/output_test.csv")

#This is for the top 5 countries

viz.top_5_countries()

#This is for the top 5 growing with percentage vs growing rate

viz.top_5_grow()

# Top 5 continents grow from 1990 to 2023

viz.top_5_continents()

# Area vs Density, India and China.

viz.china_vs_india()

# Use this one to extract the top 5 from the world dataframe,

ext.process_world_data()