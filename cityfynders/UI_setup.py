import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

def layout_setup(pairs, f):
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
                                style={'color': 'lavender', 'fontFamily': 'Helvetica', 'fontSize': 50}),
                       ),
            html.Center(html.P("Powerd by City Fynders",
                               style={'color': 'black','fontFamily':'Helvetica', 'fontSize': 20}),
                       ),
            html.Br(),
            html.Br()],
                style={'backgroundColor': 'FireBrick', 'margin': 0,'padding': 0}),
            html.Br(),
            html.Br(),

        html.Center(html.Div([
            html.P(INFORMATION, style={'color': 'black','fontFamily':'Helvetica', 'fontSize': 15, 'width': '70%'}),
            html.Img(src="http://travelquaz.com/wp-content/uploads/2015/09/photo-travel-holidays-to-the-usa-america-visit-usa-images.jpg",
                        style={'width': '70%'})
        ])),

        html.Br(),
        html.Br(),

        html.Div([
           html.Center(html.Button('Total General Rank', id='Total',
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

        html.Center(html.Div([
            dcc.Graph(id='graph-with-slider'),
            dcc.Slider(
                id='factor',
                min=0,
                max=7,
                value=4,
                step=None,
                marks={i: f[i] for i in range(8)})
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

def newdf(rank, First_care, Second_care, Third_care, Fourth_care, Fifth_care):
    """
    This function returns a new data frame from user choices

    rank: pandas data frame
    First_care: the first care column name chose from rank
    Second_care: the second care column name chose from rank
    Third_care: the third care column name chose from rank
    Fourth_care: the fourth care column name chose from rank
    Fifth_care: the fifth care column name chose from rank
    """

    df = pd.DataFrame()
    df['City'] = rank['City']
    df['First'] = rank[First_care]
    df['Second'] = rank[Second_care]
    df['Third'] = rank[Third_care]
    df['Fourth'] = rank[Fourth_care]
    df['Fifth'] = rank[Fifth_care]
    df['Total'] = (df['First']*5+df['Second']*4+df['Third']*3+df['Fourth']*2+df['Fifth']*1).rank(ascending=1)
    df = df.sort_values('Total', ascending=1)
    df['reverse_rank'] = df['Total'].rank(ascending=0)
    df['longitude'] = rank['Longitude']
    df['latitude'] = rank['Latitude']
    df['text'] = df['City'] + '<br># Final Rank ' + ': ' + (df['Total']).astype(str) +\
    '<br># ' + First_care + ': ' + (df['First']).astype(str)+ '<br># ' + Second_care +\
    ': ' + (df['Second']).astype(str) + '<br># ' + Third_care + ': ' + (df['Third']).astype(str)+\
    '<br># ' + Fourth_care + ': ' + (df['Fourth']).astype(str) + '<br># '+ Fifth_care +\
    ': ' + (df['Fifth']).astype(str)
    return df
