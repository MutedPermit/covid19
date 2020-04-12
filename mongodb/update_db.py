from pymongo import MongoClient
import pandas as pd

CASE = "deaths" #Please select the collection to update (confirmed, deaths, recovered)

cases = {
    "confirmed": "time_series_covid19_confirmed_global.csv",
    "deaths": "time_series_covid19_deaths_global.csv",
    "recovered": "time_series_covid19_recovered_global.csv"
}

#Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client["covid19"]

collection = db[CASE]

df = pd.read_csv('COVID-19/csse_covid_19_data/csse_covid_19_time_series/' + cases[CASE])

# Preprocessing
df = df.reset_index().groupby("Country/Region").sum()
df = df.drop(["index", "Lat", "Long"], axis=1)
df = df.transpose()
df.index.names = ['Date']

df.reset_index(inplace=True)
data_dict = df.to_dict("records")

#Push data to db
collection.insert_many(data_dict)
