import os
import pandas as pd
import matplotlib.pyplot as plt
import config
import time
import urllib.request
from bs4 import BeautifulSoup

COUNTRY_DATA = os.path.join(os.getcwd(), "Data/Country")
DATABASE_URL = "https://data.europa.eu/euodp/en/data/dataset/covid-19-coronavirus-data"
DATA_PATH = os.path.join(os.getcwd(), "Data/COVID-19-geographic-disbtribution-worldwide.xlsx")

def data_preprocess(df):
    """
    :param df:
    :return drop all the columns from the dataframe except the needed ones:
    """
    return df.filter(["dateRep", "cases", "deaths", "countriesAndTerritories", "countryterritoryCode", "popData2018"])

def get_country(df, country_code):
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

def save_as_csv(ds, path):
    """
    saves dataset as csv in the path
    :param ds:
    :param path:
    """
    ds.to_csv(path, index=False)

def process_by_country(df, country_code):
    country_ds = get_country(df, country_code)
    country_ds = time_process(country_ds)
    country_ds = cumulative_data(country_ds)
    file_name = country_ds.iloc[0]["countriesAndTerritories"] + ".csv"
    save_as_csv(country_ds, os.path.join(COUNTRY_DATA, file_name))

def download(url, location):
    print("Beginning File Download...")
    urllib.request.urlretrieve(url, location)
    print("Downloaded Successfully.")

def get_database_url(page):
    print("Fetching url of the data file...")
    page = urllib.request.urlopen(page)
    soup = BeautifulSoup(page, "lxml")
    url = soup.find("ul", class_="resource-list unstyled").find_all("li")[1].a["href"]
    print("File Fetched Successfully.")
    return url

def update():
    # Fetch latest database via HTTP
    url = get_database_url(DATABASE_URL)
    download(url, DATA_PATH)

    # Load the main data frame
    df = data_preprocess(pd.read_excel(DATA_PATH))

    # Load Country Data
    for country in config.countries_codes:
        country = process_by_country(df, country)