import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

df_school_yr_1 = pd.read_csv("PEN_July_1_2021_June_30_2022.csv", sep=",")
df_school_yr_2 = pd.read_csv("PEN_July_1_2022_December_31_2022.csv", sep=",")

data = df_school_yr_1.append(df_school_yr_2)

print(len(df_school_yr_2))
data.dropna(subset=['Title'], inplace=True)
duplicate_columns = ['Title', 'District']

# Remove duplicates
data.drop_duplicates(subset=duplicate_columns)

print(len(df_school_yr_1))



