import pandas as pd
from pandas import json_normalize
import os
import src.extracting as ext
import src.visualization as viz


# Select df = file origin path, this file works for countries, change the country as needed.

df = ext.city_pop("https://worldpopulationreview.com/countries/cities/colombia")

# Use the viz. to visualize the data extracted.

viz.counting_cities(df, "data/output_test.csv")




