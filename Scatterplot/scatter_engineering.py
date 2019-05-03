import pandas as pd

price = pd.read_csv('../Data/price.csv')
whisky = pd.read_csv('../Data/whisky.csv')

result = price.groupby(['brand'])['price'].agg(['min','max']).reset_index()
df = pd.merge(result, whisky, left_on='brand', right_on='Distillery', how='inner')
df = df.loc[df['min'] != df['max']]
data_scatter = df[['brand','min','max','Sweetness','Smoky','Region']]

data_scatter.to_csv('../Data/data_scatter.csv', index=False)
