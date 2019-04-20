import numpy as np
import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.offline import *
# To initiate ploty to run offline
init_notebook_mode(connected=True)

pop = pd.read_csv('uspop.csv')
f = open('total_uspop.txt','r')
total_uspop = int(f.read())
pop['pop_prct'] = pop['population']*1.0/total_uspop
pop['text'] = 'The population of '+ pop['state'] +\
              ' is ' + pop['population'].astype(str)

heatmap_color = [
    'rgb(193, 193, 193)',
    'rgb(239, 239, 239)',
    'rgb(195, 196, 222)',
    'rgb(144,148,194)',
    'rgb(101,104,168)',
    'rgb(65, 53, 132)'
]

endpts = [i*1.0/10000 for i in range(20, 1600, 256)]

scl = [(endpts[i], heatmap_color[i]) for i in range(6)]

data = [go.Choropleth(colorscale = scl,
                      autocolorscale = False,
                      locations = pop['state_abb'],
                      z = pop['pop_prct'].astype(float),
                      locationmode = 'USA-states',
                      text = pop['text'],
                      marker = go.choropleth.Marker(
                      line = go.choropleth.marker.Line(
                             color = 'rgb(255,255,255)',
                             width = 2)),
                      colorbar = go.choropleth.ColorBar(
                      title = "Porportion (Percentage)"))]

layout = go.Layout(
    title = go.layout.Title(
        text = '2018 Poputlation of State which Allows Alochol Shipments'
    ),
    geo = go.layout.Geo(
        scope = 'usa',
        projection = go.layout.geo.Projection(type = 'albers usa'),
        showlakes = True,
        lakecolor = 'rgb(255, 255, 255)'),
)

fig = go.Figure(data = data, layout = layout)
plotly.offline.plot(fig, filename='state_pop_alcohol.html')