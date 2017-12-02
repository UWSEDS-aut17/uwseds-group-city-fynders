import plotly
import plotly.plotly as py

def usmap(df, category='total'):
    """
    This function returns a dotted us map based on the rank DataFrame, and layout category.

    df: rank DataFrame
    category: can choose total, natural, human, economy, tertiary as value, the default is total
    """

    if category == 'natural':
        df = df.sort_values('Natural_total_rank', ascending=1)
        df['reverse_rank'] = df['Natural_total_rank'].rank(ascending=0)

        df['text'] = df['City'] + '<br># Final Rank ' + (df['Natural_total_rank']).astype(str) +\
                '<br># Air Rank ' + (df['Air']).astype(str)+ '<br># Water_rank ' +\
            (df['Water']).astype(str)+'<br># Toxics rank ' + (df['Toxics']).astype(str)+\
            '<br># Hazardous rank ' + (df['Hazardous']).astype(str) + '<br># Green score rank ' + (df['Green_score']).astype(str)
        layout_title = 'The natural ranking of US big cities'
        layout_filename = 'natural-ranking-map.html'

    elif category == 'human':
        df = df.sort_values('Human_related_rank', ascending=1)
        df['reverse_rank'] = df['Human_related_rank'].rank(ascending=0)

        df['text'] = df['City'] + '<br># Final Rank ' + (df['Human_related_rank']).astype(str) +\
                '<br># Crime rank ' + (df['Crime_rank']).astype(str)+ '<br># Hospital rank ' +\
            (df['Hospital_rank']).astype(str)+'<br># Early education rank ' + (df['Early_education_rank']).astype(str)+\
            '<br># University education rank ' + (df['University_education_rank']).astype(str)
        layout_title = 'The human related ranking of US big cities'
        layout_filename = 'human-related-ranking-map.html'

    elif category == 'economy':
        df = df.sort_values('Economy_rank', ascending=1)
        df['reverse_rank'] = df['Economy_rank'].rank(ascending=0)

        df['text'] = df['City'] + '<br># Final Rank ' + (df['Economy_rank']).astype(str) +\
                '<br># Percent unemployment rank ' + (df['Rank_unemployment']).astype(str)+ '<br># Sale rate rank' +\
            (df['Rank_sale_rate']).astype(str)+'<br># Income rank ' + (df['Rank_Income']).astype(str)+\
            '<br># Tuition rank ' + (df['Rank_Tuition']).astype(str)
        layout_title = 'The economy ranking of US big cities'
        layout_filename = 'economy-ranking-map.html'

    elif category == 'tertiary':
        df = df.sort_values('Tertiary_Rank', ascending=1)
        df['reverse_rank'] = df['Tertiary_Rank'].rank(ascending=0)

        df['text'] = df['City'] + '<br># Final Rank ' + (df['Tertiary_Rank']).astype(str) +\
                '<br># Total bar rank' + (df['Bar_Rank']).astype(str)+ '<br># Total restaurant_Rank' +\
            (df['Restaurant_Rank']).astype(str) + '<br># Museums rank ' + (df['Museums_Rank']).astype(str)+\
            '<br># Libraries rank ' + (df['Libraries_Rank']).astype(str) + '<br># Park rank' +\
            (df['Park_Rank']).astype(str) + '<br># Top200 Restaurant rank ' + (df['TopRes_Rank']).astype(str)
        layout_title = 'The tertiary industry ranking of US big cities'
        layout_filename = 'tertiary-ranking-map.html'

    elif category == 'total':
        df['Final rank'] = df['Human_related_rank'] + df['Natural_total_rank'] + df['Economy_rank'] + df['Tertiary_Rank']
        df['Final rank'] = df['Final rank'].rank(ascending = 1)
        df = df.sort_values('Final rank', ascending=1)
        df['reverse_rank'] = df['Final rank'].rank(ascending=0)

        df['text'] = df['City'] + '<br># Final Rank ' + (df['Final rank']).astype(str) +\
                '<br># Human related rank ' + (df['Human_related_rank']).astype(str)+ '<br># Natural total rank ' +\
            (df['Natural_total_rank']).astype(str) + '<br># Economy rank ' + (df['Economy_rank']).astype(str)+\
            '<br># Tertiary rank ' + (df['Tertiary_Rank']).astype(str)
        layout_title = 'The general ranking of US big cities'
        layout_filename = 'general-ranking-map.html'

    limits = [(0,10),(10,20),(20,30),(30,40),(40,50)]
    colors = ["rgb(0,116,217)","rgb(255,65,54)","rgb(133,20,75)","rgb(255,133,27)","lightgrey"]
    cities = []


    for i in range(len(limits)):
        lim = limits[i]
        df_sub = df[lim[0]:lim[1]]
        city = dict(
            type = 'scattergeo',
            locationmode = 'USA-states',
            lon = df_sub['Longitude'],
            lat = df_sub['Latitude'],
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
            title = layout_title,
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
    return plotly.offline.plot(fig, validate=False, filename=layout_filename)
