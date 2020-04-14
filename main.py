
import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = os.path.join(os.getcwd(), "Data\COVID-19-geographic-disbtribution-worldwide.xlsx")

def data_preprocess(df):
    """
    :param df:
    :return drop all the columns from the dataframe except the needed ones:
    """
    return df.filter(["dateRep", "cases", "deaths", "countryterritoryCode", "popData2018"])

def get_country(country_code):
    """
    :param country_code:
    :return all the rows with that code:
    """
    return df.loc[df["countryterritoryCode"] == country_code]

def cumulative_data(ds):
    """
    :param ds:
    :return the new dataset with two columns added:
        1. Cumulative cases till the day
        2. Cumulative deaths till the day:
    """
    ds["cum_cases"] = ds["cases"].cumsum()
    ds["cum_deaths"] = ds["deaths"].cumsum()
    return ds

def time_process(ds):
    """
    converts dateRep column into datetime object and sort it according to the date
    :param ds:
    :return new dataset:
    """
    ds["dateRep"] = pd.to_datetime(ds.dateRep)
    ds = ds.sort_values(by="dateRep")
    return ds

def process_by_country(country_code):
    country_ds = get_country(country_code)
    country_ds = time_process(country_ds)
    country_ds = cumulative_data(country_ds)
    return country_ds


df = data_preprocess(pd.read_excel(DATA_PATH))

kor = process_by_country("KOR")
print(kor)