'''
TO DO: import database and divide by countries
'''

import os
import pandas as pd

DATA_PATH = os.path.join(os.getcwd(), "Data\COVID-19-geographic-disbtribution-worldwide.xlsx")

def data_preprocess(df):
    """
    :param df:
    :return drop all the columns from the dataframe except the needed ones:
    """
    return df.filter(["dateRep", "cases", "deaths", "countriesAndTerritories", "popData2018"])

def get_country(country_code):
    """
    :param country_code:
    :return all the rows with that code:
    """
    return df.loc[df["countryterritoryCode"] == country_code]

df = pd.read_excel(DATA_PATH)
df = data_preprocess(df)
print(df.head())