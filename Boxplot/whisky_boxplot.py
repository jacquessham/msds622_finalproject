import numpy as np
import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *
# To initiate ploty to run offline
init_notebook_mode(connected=True)

price = pd.read_csv('../Data/price.csv')
regions = ['Lowland','Islay & Islands','Highland','Speyside']
data = []
for region in regions:
    prices = price.loc[price['region'] == region]['price'].tolist()
    prices = [float(p) for p in prices if float(p) < 400]
    data.append(go.Box(y = prices,name = region))

layout = go.Layout(
    title='Scotch Whisky Price Statistic by Region')
fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='whisky_boxplot.html')
