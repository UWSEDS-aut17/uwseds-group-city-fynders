# Component Design

## 1. Rank the city for each criterion:

- What it does. This component will rank the city for each factors within the four categories, such as number of museums, crime rate, average household income.  The idea is to add up the rank number for the factors within a category or the factors that users choose and then give the total rank (small number first).
- Name: RankCity (Factors_list)
- Inputs: Factors_list: a list of factors that users care about; the length of the list is five because we will allow users to choose up to 5 factors
- Outputs: `csv` file that contains the ranking of the cities for each factor
- How it works
    + Ranking of all factors
    + Ranking of the five factors that the users choose

## 2. Correlation analysis:
- What it does: Analyze correlations of different factors, as well as correlations of four basic categories.
- Name: CorrelationAnalysis.
- Inputs: (`natural.csv, HumanRelated.csv, Economy.csv, tertiary.csv`) all change into a big DataFrame.Columns include (all float64), we need to change to array for correlation:
`'Jan_T', 'April_T', 'july_T', 'Oct_T', 'Prep_inch’,  'Prep_days', 'Snowfall_inch', 'Green_score', 'Air', 'Water_quality', 'Toxics', 'Hazardous', 'Sanitation'
'Percent unemployment', 'State sale tax rate', 'Local tax rate', 'Total rate', 'Median Income', 'AvgTuition', 'Rank_Unemployment', 'Rank_Sales', 'Rank_income', 'Rank_Tution', 'Sum', 'Economy_rank','Total_city_rank'`, etc.

- Outputs: Correlation coefficients and scatter plots of every two factors; correlations of four basic category rankings.
- How it works: (Pseudo code)
<pre><code>
	Def CorrelationAnalysis.py
		numpy.correlate(column_1, column_2, …, column_n)
        coefficient = numpy.corrcoef(column_1, column_2, …, column_n)
		For i < n
			For j < i
				subplot(column_i, column_j)
				Text show coefficient(i,j)
</code></pre>

## 3. Users choose ranking criteria and assign weight to each criterion
- What it does: User select five factors which mainly affect the city ranking from their viewpoint and give them score each, then get the city ranking results based on their choice.
- Name: UserDIYRanking
- Inputs:
	- Factors, score
- Outputs:
	- Sum of the score for each city
	- Results of ranking of the city
- How it works:
	- Import button_function
	- Import get_selected_factors
	- Import get_selected_score
	- Import results_output
	- get_selected_factors(factor)
	- get_selected_score(score)
	- data[‘sum_chosen_factors’] = (factor1 * score1 + factor2 * score2 + factor3 *      score3 + factor4 * score4 + factor5 * score5)      
    - data[‘DIY_ranking’] = data[‘sum_chosen_factors’]
    - result_output(data)

## 4. Visualization ranking results on the US map
- What it does: Present the ranking information on the United States map.
- Name: City and Layout
- Inputs:

    **City information from pandas dataframe**			
    + City: object
    + Longitude: float64
    + Latitude: float64
    + Four big category rank: float64

    **Default graph design**
    + Type: scatter geo
    + Location Mode: USA
    + Colors: rgb

- Outputs: a graph with all the rank information
- How it works:

<pre><code>
    city = dict(
            type = 'scattergeo',
            locationmode = 'USA-states',
            lon = df_sub['longitude'],
            lat = df_sub['latitude'],
            text = df_sub[['City','Human_related_rank']].apply(combine,axis=1),
            marker = dict(
                size = df_sub['Human_related_rank']\*10,
                color = colors[i],
                line = dict(width=0.5, color='rgb(40,40,40)'),
                sizemode = 'area'
            ),
            name = '{0} - {1}'.format(lim[0],lim[1]) )
        cities.append(city)

    layout = dict(
            title = 'The human related ranking of US big cities',
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
        )`
</code></pre>
