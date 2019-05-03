import pandas as pd


whisky = pd.read_csv('../Data/whisky.csv')
results = whisky.groupby(['Region','Body'])['Winey'].mean().reset_index()
results.to_csv('../Data/whisky_heatmap.csv', index=False)
