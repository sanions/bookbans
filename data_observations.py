import numpy as np
import pandas as pd
import warnings
import geopandas as gpd
import matplotlib.pyplot as plt
from chart_studio import plotly as py
import plotly.express as px
warnings.filterwarnings("ignore")

us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}

df_school_yr_1 = pd.read_csv("PEN_July_1_2021_June_30_2022.csv", sep=",")
df_school_yr_2 = pd.read_csv("PEN_July_1_2022_December_31_2022.csv", sep=",")


data = df_school_yr_1.append(df_school_yr_2)

print(len(data))
data.dropna(subset=['Title'], inplace=True)
duplicate_columns = ['Title', 'District']

# Remove duplicates
data.drop_duplicates(subset=duplicate_columns)

# Get top 10 most common school districts
top_10_districts = data[["District", "State"]].value_counts().head(10)
print(top_10_districts)

# Get the top 10 most common book bans
top_10_books = data[["Author", "Title"]].value_counts().head(10)
print(top_10_books)

# Create a map of states and frequencies
state_ban_counts = data.groupby('State')[["Title", "District"]].count().reset_index()
state_ban_counts["State_Abbrv"] = state_ban_counts["State"].map(us_state_to_abbrev)

print(data["District"])

fig = px.choropleth(state_ban_counts, 
                    locations=state_ban_counts["State_Abbrv"],  # Column containing state names
                    locationmode="USA-states",  # Set the location mode
                    color=state_ban_counts["District"], # Column for color scale
                    scope="usa")



# fig.show()
