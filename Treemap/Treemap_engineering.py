import pandas as pd

price = pd.read_csv('../Data/price.csv')
whisky = pd.read_csv('../Data/whisky.csv')

label_count = price.groupby(['brand'])['label'].count()
df = pd.merge(pd.DataFrame(label_count), whisky,
              left_on='brand', right_on='Distillery', how='inner')
df = df[['Distillery','label','Region']]
results = df.groupby('Region')['label'].sum()
results = pd.DataFrame(results).reset_index()

results.columns = ['region','count']
results['text'] = results['region'].astype(str) + '\n' + results['count'].astype(str)

results.to_csv('../Data/whiksy_treemap_count.csv', index=False)