import numpy as np
import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *
# To initiate ploty to run offline
init_notebook_mode(connected=True)

price = pd.read_csv('../Data/whisky.csv')

region_size = price.groupby('Region').size()
region_size = pd.DataFrame(region_size,columns=['count'])
region_size.reset_index(level=0, inplace=True)
region_size = region_size.sort_values(by='count')
region = region_size['Region'].tolist()
count = region_size['count'].tolist()
count_text = [str(num) for num in count]

bar = [go.Bar(x=region,
	           y=count, text=count_text,
	           textposition='auto')]

layout = go.Layout(
    title='Distillery Count of Scotch Whisky by Region',
    xaxis=dict(title='Region of Scotland'),
    yaxis=dict(title='Count'))
fig = go.Figure(data=bar, layout=layout)

plotly.offline.plot(fig, filename='whisky_barchart.html')
