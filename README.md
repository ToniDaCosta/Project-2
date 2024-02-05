

# Project-2

 Welcome to the project to visualize world population and most populated cities in the countries, the project has been devided in steps for easy understanding and quick usage.

 # File names :

    - data --> output
    - Images
    - Scrapping
    - src
    - Visualizations

# Documents :

    - .env
    - Jupyter Example
    - Main
    - README

We will explain how to use and the origin of each file so you can follow the process.

# Data :

In this file you have the data obtained from the web sites and cleaned files, You can also find the "output" file with documents from the returned data.

# Images : 

Containing images downloaded from internet.

# Scrapping: 

Containing .ipnyb files where functions and cleaning processed were followed.

# src : 

This file contains all the .py functions cleaned and separated in several steps : "extracting", "CodeRunner", "transforming", "visualization".

# Visualizations :

Containing the visualizations process followed, later resumed in one function for the "Scrapping process".

# How to use the "Main file".

- Select df = file origin path, this file works for countries, change the country as needed.

    "df = ext.city_pop("https://worldpopulationreview.com/countries/cities/colombia")"

- Use the viz. to visualize the data extracted.

    "viz.counting_cities(df, "data/output_test.csv")"

EXAMPLES: you might want to look at "jupiter_example" for a better understanding of the functions.


