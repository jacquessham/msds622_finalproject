import pandas as pd

export = pd.read_csv('../Data/export.csv')
max_year = max(export['year'].tolist())
export2017 = export[(export['year']==max_year) & (export['country']!='Rest of world')]
cities = ['Bourges', 'Nottingham', 'Mexico City', 'Athlone',
          'Winnipeg', 'Orebro', 'Amsterdam', 'Florence']
lat = [47.08, 52.95, 19.43, 53.42, 49.90, 59.28, 52.37, 43.77]
lon = [2.40, 1.16, -99.13, -7.94, -97.14, 15.21, 4.90, 11.26]
export2017['cities'] = cities
export2017['lat'] = lat
export2017['lon'] = lon
export2017 = export2017.drop(columns='year')
export2017.to_csv('../Data/export2017.csv', index=False)