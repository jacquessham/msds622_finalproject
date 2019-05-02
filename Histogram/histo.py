import numpy as np
import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *
# To initiate ploty to run offline
init_notebook_mode(connected=True)

price = pd.read_csv('../Data/price.csv')

price_tag = price['price'].tolist()
"""
print(type(price_tag))
print(price_tag)
print(type(price_tag[0]))
"""
price_tag = [float(p) for p in price_tag if float(p) < 400]

his = [go.Histogram(x=price_tag,
	                marker=dict(color='#884C63'))]
layout = go.Layout(title='Price of Scotch Whisky Available in TotalWine',
	               xaxis=dict(title='Price ($)'),
	               yaxis=dict(title='Count'))
fig = go.Figure(data=his, layout=layout)
plotly.offline.plot(fig, filename='whisky_histogram.html')
