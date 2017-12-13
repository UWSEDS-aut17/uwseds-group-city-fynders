import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

def layout_setup(pairs):
    """
    This function returns a layout of the user interface

    pairs: pairs is a two_dimensional list. The first is the columns from pandas data frame,
           the second is the relative name for each column in the dropdown choices
    """

    INFORMATION = """
    City information is always an interesting topic in people’s daily life. Many websites
    have their own ranking results based on unique preference. However, it is hard to say
    which city is the best choice for everyone. We created a tool for people to choose the
    factors matter to them instead of ranking with some information they don’t care about.
    We divided the factors into four main parts: human related (Population, Crime, College,
    Hospital, etc), economy (Income, Percent Unemployment, etc), natural (Green
    Score, Air, Water, etc) and tertiary (Restaurant, Museum, Library, etc). We
    combined our data from many different sources like former ranking websites and some
    departments collected data. We provide some buttons below to help you make your own choice.
    """

    lay = html.Div([

        html.Div([
            html.Br(),
            html.Br(),
            html.Center(html.H1("Find Your Dream City to Live in the US",
                                style={ 'color': 'lavender', 'fontFamily': 'Helvetica', 'fontSize': 50}),
                       ),
            html.Center(html.P("Powerd by City Fynders",
                               style={'color': 'black','fontFamily':'Helvetica', 'fontSize': 20}),
                       ),
            html.Br(),
            html.Br()],
                style={'class':'l-r','backgroundColor': 'FireBrick', 'margin': 0,'padding': 0}),

        html.Div([
            html.Br(),
            html.Br(),
            html.Div(html.P(INFORMATION,
                              style={'margin-left': '10%','float':'left','width': '500px','height': '500px','color':'black','fontFamily':'Helvetica', 'fontSize': 20 }),
                       ),
            html.Center(html.Img(src="http://travelquaz.com/wp-content/uploads/2015/09/photo-travel-holidays-to-the-usa-america-visit-usa-images.jpg"),
                       style={'margin-right': '10%','float':'right'})
        ]),


        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Div([
           html.Center(html.Button('Total Rank', id='Total',
                                style={'width': 200, 'color': 'white', 'backgroundColor': 'FireBrick', 'height': 70,'fontSize': 15})),
        ]),

        html.Br(),
        html.Br(),
        html.Center(html.Div([
                html.Button('Human Related Rank', id='Hrank',
                                style={'width': 200, 'color': 'black', 'backgroundColor': 'lightblue', 'height': 70,'fontSize': 15,'marginRight':100}),
                html.Button('Natural Rank', id='Nrank',
                                style={'width': 200, 'color': 'black', 'backgroundColor': 'lightblue', 'height': 70,'fontSize': 15,'marginRight':100}),
                html.Button('Economy Rank', id='Erank',
                                style={'width': 200, 'color': 'black', 'backgroundColor': 'lightblue', 'height': 70,'fontSize': 15,'marginRight':100}),
                html.Button('Teritary Industry Rank', id='Trank',
                                style={'width': 200, 'color': 'black', 'backgroundColor': 'lightblue', 'height': 70,'fontSize': 15}),
        ])),

        html.Br(),
        html.Br(),
        html.Center(html.Div([
            html.Center(html.H1("Factor Correlation Graph",
                    style={ 'color': 'black', 'fontFamily': 'Helvetica', 'fontSize': 20}),
                       ),
            html.Center(html.Img(src="https://user-images.githubusercontent.com/32367015/33920542-67cd1d80-df73-11e7-9dc5-48cdc7a5c81e.png"),
                       )
        ])),
        html.Br(),
        html.Br(),
        html.Center(html.Div([
            html.P("Now choose factors you care about",
                style={'color': 'black','fontFamily':'Helvetica', 'fontSize': 20}),
        ])),
        # First important factor
        html.Div([
            html.P('Important No.1'),
            dcc.Dropdown(
                id='First-care',
                options=[ {'label': pairs[1][i],'value': pairs[0][i]} for i in range(19)],
            )
        ],
            style={'width': '20%', 'fontFamily':'Helvetica','display': 'inline-block'}),
        # Second important factor
        html.Div([
            html.P('Important No.2'),
            dcc.Dropdown(
                id='Second-care',
                options=[{'label': pairs[1][i],'value': pairs[0][i]} for i in range(19)],
            )
        ],
            style={'width': '20%','fontFamily':'Helvetica', 'display': 'inline-block'}),
        # Third important factor
        html.Div([
            html.P('Important No.3'),
            dcc.Dropdown(
                id='Third-care',
                options=[{'label': pairs[1][i],'value': pairs[0][i]} for i in range(19)],
            )
        ],
            style={'width': '20%','fontFamily':'Helvetica', 'display': 'inline-block'}),
        # Fourth important factor
        html.Div([
            html.P('Important No.4'),
            dcc.Dropdown(
                id='Fourth-care',
                options=[{'label': pairs[1][i],'value': pairs[0][i]} for i in range(19)],
            )
        ],
            style={'width': '20%','fontFamily':'Helvetica', 'display': 'inline-block'}),
        # Fifth important factor
        html.Div([
            html.P('Important No.5'),
            dcc.Dropdown(
                id='Fifth-care',
                options=[{'label': pairs[1][i],'value': pairs[0][i]} for i in range(19)],
            )
        ],
            style={'width': '20%', 'fontFamily':'Helvetica','display': 'inline-block'}),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Center(html.Button('Go Searching!', id='Search',
            style={'width': 200, 'color': 'white', 'backgroundColor': 'FireBrick', 'height': 70,'fontSize': 20})),
        html.Div(dcc.Graph(id='User-graphic')),
        html.Div(dcc.Graph(id='Total-graphic')),
        html.Div(dcc.Graph(id='Human-graphic')),
        html.Div(dcc.Graph(id='Natural-graphic')),
        html.Div(dcc.Graph(id='Economic-graphic')),
        html.Div(dcc.Graph(id='Tertiary-graphic'))
    ])
    return lay
