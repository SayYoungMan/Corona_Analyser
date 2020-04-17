import os
import pandas as pd
import config
import dash
import dash_table

COUNTRY_DATA_PATH = "Data/Country"


def get_country_data():
    country_dict = {}
    n = 0
    for i in os.listdir(COUNTRY_DATA_PATH):
        country_dict[config.countries_codes[n]] = pd.read_csv(os.path.join(COUNTRY_DATA_PATH, i))
        n += 1
    return country_dict

def sort_today_data(country_dict):
    df = pd.DataFrame(columns=country_dict["KOR"].columns)
    n = 0
    for i in country_dict.values():
        df.loc[n] = i.iloc[-1, :]
        n += 1
    return df

country_dict = get_country_data()
today_data = sort_today_data(country_dict)

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id="today_table",
    columns=[{"name":i, "id":i} for i in today_data.columns],
    data=today_data.to_dict("records"),
)

if __name__ == '__main__':
    app.run_server(debug=True)