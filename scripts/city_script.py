import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import cityfynders.data_processing as dp
from cityfynders.plotly_usmap import usmap
import cityfynders.UI_setup as UI_setup


rank = pd.read_csv('../data/rank_file.csv')
#############################
######### Plot part #########

# Create a list of indicators
available = list(rank.columns.values)
for i in ['Unnamed: 0','City','State','Population','Natural_total_rank', 'Human_related_rank',
          'Economy_rank', 'Tertiary_Rank', 'Latitude', 'Longitude']:
    available.remove(i)

# Create a list of labels for dropdown
labels = ['Fewer Crimes','More Hospitals','Early Education Options',
          'University Options','Air Quality','Water Quality',
           'Fewer Toxics','Fewer Hazardous Particles','Green Coverage',
           'Employment Rate','Sales Revenue','Income','Tuition Affordability',
          'Bars','Restaurants','Museums','Libraries','Parks','Top Restaurants']

# Put available and labels in a two-dimensional list
pairs = [available,labels]

(natural, human, economy, tertiary) = dp.read_data()
alldata = human
for i in[natural, economy, tertiary]:
    factors = list(i.columns.values)
    for j in factors:
        alldata[j] = i[j]
imp = pd.DataFrame()
imp['City'] = alldata['City']
imp['Population'] = alldata['Population']
imp['Crime'] = alldata['Violent'] + alldata['Rape'] + alldata['Robbery']
imp['Colleges'] = alldata['Colleges']
imp['Hospitals'] = alldata['NumHospital']
imp['Air Score'] = alldata['Air']
imp['Water Score'] = alldata['Water_quality']
imp['Median Income'] = alldata['Median Income']
imp['Restaurants'] = alldata['Restaurant']
imp['Pro Sport team'] = alldata['Pro_sports_team']
f = list(imp.columns.values)
f.remove('City')
f.remove('Population')

if __name__ == '__main__':
    # Set up User Interface through dash
    app = dash.Dash()
    # Get DataFrame value
    app.layout = UI_setup.layout_setup(pairs, f)

    @app.callback(
        dash.dependencies.Output('graph-with-slider', 'figure'),
        [dash.dependencies.Input('factor', 'value')])
    def update_figure(factor):
        choose = f[factor]
        return {
            'data': [go.Scatter(
                x=imp['Population'],
                y=imp[choose],
                text=imp['City'],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 15,
                    'line': {'width': 0.5, 'color': 'white'}
                }
            )],
            'layout': go.Layout(
                xaxis={
                    'title': 'Population',
                    'type': 'linear'
                },
                yaxis={
                    'title': choose,
                    'type': 'linear'
                },
                margin={'l': 40, 'b': 30, 't': 10, 'r': 0},
                hovermode='closest'
            )
        }

    @app.callback(
        dash.dependencies.Output('Total-graphic', 'figure'),
        [dash.dependencies.Input('Total', 'n_clicks')]
    )
    def total_graph(Total):
        if(Total is None):
            return
        #Total general rank
        return {
               usmap(rank)
            }

    @app.callback(
        dash.dependencies.Output('Human-graphic', 'figure'),
        [dash.dependencies.Input('Hrank', 'n_clicks')]
    )
    def human_graph(Hrank):
        if(Hrank is None):
            return
        #Total general rank
        return {
               usmap(rank, 'human')
            }

    @app.callback(
        dash.dependencies.Output('Natural-graphic', 'figure'),
        [dash.dependencies.Input('Nrank', 'n_clicks')]
    )
    def natural_graph(Nrank):
        if(Nrank is None):
            return
        #Total general rank
        return {
               usmap(rank, 'natural')
            }

    @app.callback(
        dash.dependencies.Output('Economic-graphic', 'figure'),
        [dash.dependencies.Input('Erank', 'n_clicks')]
    )
    def economomic_graph(Erank):
        if(Erank is None):
            return
        #Total general rank
        return {
               usmap(rank, 'economy')
            }

    @app.callback(
        dash.dependencies.Output('Tertiary-graphic', 'figure'),
        [dash.dependencies.Input('Trank', 'n_clicks')]
    )
    def teritary_graph(Trank):
        if(Trank is None):
            return
        #Total general rank
        return {
               usmap(rank, 'tertiary')
            }
    @app.callback(
        dash.dependencies.Output('User-graphic', 'figure'),
        [dash.dependencies.Input('Search', 'n_clicks')],
        [dash.dependencies.State('First-care', 'value'),
         dash.dependencies.State('Second-care', 'value'),
         dash.dependencies.State('Third-care', 'value'),
         dash.dependencies.State('Fourth-care', 'value'),
         dash.dependencies.State('Fifth-care', 'value'),
        ]
    )

    def user_DIY_graph(Search, First_care, Second_care, Third_care, Fourth_care, Fifth_care):
        df = UI_setup.newdf(rank, First_care, Second_care, Third_care, Fourth_care, Fifth_care)

        limits = [(0,10),(10,20),(20,30),(30,40),(40,50)]
        colors = ["rgb(0,116,217)","rgb(255,65,54)","rgb(133,20,75)","rgb(255,133,27)","lightgrey"]
        cities = []


        for i in range(len(limits)):
            lim = limits[i]
            df_sub = df[lim[0]:lim[1]]
            city = dict(
                type = 'scattergeo',
                locationmode = 'USA-states',
                lon = df_sub['longitude'],
                lat = df_sub['latitude'],
                text = df_sub['text'],
                marker = dict(
                    size = df_sub['reverse_rank']*15,
                    color = colors[i],
                    line = dict(width=0.5, color='rgb(40,40,40)'),
                    sizemode = 'area'
                ),
                name = '{0} - {1}'.format(lim[0],lim[1]) )
            cities.append(city)

            layout = dict(
                title = 'Your Dream City Results',
                showlegend = True,
                geo = dict(
                    scope='usa',
                    projection=dict( type='albers usa' ),
                    showland = True,
                    landcolor = 'rgb(217, 217, 217)',
                    subunitwidth=1,
                    countrywidth=1,
                    subunitcolor="rgb(255, 255, 255)",
                    countrycolor="rgb(255, 255, 255)"
                ),
            )
            fig = dict( data=cities, layout=layout )

        return {
            plotly.offline.plot( fig, validate=False )
        }

if __name__ == '__main__':
    app.run_server(debug=True)
