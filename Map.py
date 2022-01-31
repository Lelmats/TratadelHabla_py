import plotly.graph_objects as go

fig = go.Figure(go.Choroplethmapbox(name='Mexico', geojson=mx_regions_geo, ids=df['estado'], z=df['percentage'],
                                  locations=df['estado'], featureidkey='properties.name', colorscale='reds',
                                  marker=dict(line=dict(color='black'), opacity=0.6)))
fig.update_layout(mapbox_style='open-street-map',
                  mapbox_zoom=4, 
                  mapbox_center = {'lat': 25, 'lon': -99}
                 )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()