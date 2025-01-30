import pandas as pd


movies = pd.read_csv('movies.csv', encoding='ISO-8859-1')

summary_statistics = movies.describe()

data_info = movies.info()

print(summary_statistics)

print(data_info)