import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import cityfynders.data_processing as dp
from cityfynders.plotly_usmap import usmap, newdf, usmap_choose
import cityfynders.UI_setup as UI_setup


rank = pd.read_csv('../data/rank_file.csv')

# Create a list of indicators
available = list(rank.columns.values)
for i in ['Unnamed: 0', 'City', 'State', 'Population', 'Natural_total_rank',
          'Human_related_rank', 'Economy_rank', 'Tertiary_Rank', 'Latitude',
          'Longitude']:
    available.remove(i)

# Create a list of labels for dropdown
labels = ['Air Quality', 'Water Quality', 'Fewer Toxics',
          'Fewer Hazardous Particles', 'Green Coverage',
          'Fewer Crimes', 'More Hospitals', 'Early Education Options',
          'University Options', 'Employment Rate', 'Sales Revenue',
          'Income', 'Tuition Affordability', 'Bars', 'Restaurants',
          'Museums', 'Libraries', 'Parks', 'Top Restaurants']

# Put available and labels in a two-dimensional list
pairs = [available, labels]


if __name__ == '__main__':
    app = dash.Dash()
    # Get DataFrame value
    app.layout = UI_setup.layout_setup(pairs)

    @app.callback(
        dash.dependencies.Output('Total-graphic', 'figure'),
        [dash.dependencies.Input('Total', 'n_clicks')]
    )
    def total_graph(Total):
        if(Total is None):
            return
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
        return {
           usmap(rank, 'human')
        }

    @app.callback(
        dash.dependencies.Output('Natural-graphic', 'figure'),
        [dash.dependencies.Input('Nrank', 'n_clicks')]
    )
    def environment_graph(Nrank):
        if(Nrank is None):
            return
        return {
           usmap(rank, 'natural')
        }

    @app.callback(
        dash.dependencies.Output('Economic-graphic', 'figure'),
        [dash.dependencies.Input('Erank', 'n_clicks')]
    )
    def economy_graph(Erank):
        if(Erank is None):
            return
        return {
           usmap(rank, 'economy')
        }

    @app.callback(
        dash.dependencies.Output('Tertiary-graphic', 'figure'),
        [dash.dependencies.Input('Trank', 'n_clicks')]
    )
    def entertainment_graph(Trank):
        if(Trank is None):
            return
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
         dash.dependencies.State('Fifth-care', 'value'), ]
    )
    def user_DIY_graph(Search, First_care, Second_care, Third_care,
                       Fourth_care, Fifth_care):
        df = newdf(rank, First_care, Second_care, Third_care,
                   Fourth_care, Fifth_care)
        return {
            usmap_choose(df)
        }

if __name__ == '__main__':
    app.run_server(debug=True)
