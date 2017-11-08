# Functional specification

Problem Statements
1. Select criteria for city ranking in the four categories
2. Data collection and joint
3. General analysis for four categories
4. Create tools for user interface for selecting factors and visualizing result

## User profile

  The computational environments the user should be familiar with are listed as:
  - Python
  - Jupyter notebook

Also, users need to be willing to choose the criteria as well as allocate weight value to each selected factors themselves to score city.

## Elements

### Research part
 - General analysis on the top environmental-friendly (social, developed or culturally important) cities
 -  Correlations of those factors and possible causality through PCA analysis.

### Tool part
- Welcome Page with default research result
- Create an interactive User Interface to select ranking criteria
- Visualization ranking results on the US map.

### Notes
- There will be four main categories for users to choose in the database: Environment, Society, Economy and Tertiary Industry
- Many cities may only have partial information, so we will only use the information for big cities which have enough data to do the analysis

## Use Case

**Welcome Page with default research result**
- Run `main.py` file to prompt up the Welcome Page
- Present the general research results of the top cities of the four categories																																																																
**Users choose ranking criteria and assign weight to each criterion**
- From all the factors, users pick 5 top criteria they care about and rank them from 1 to 5
- Calculate the score of each city (Score1* 5 +Score2*4 + Score3 * 3 + Score4*2 + Score5*1) and return the top 3 cities

**Visualization ranking results on the US map**
- Import a certain US map package showing all the city information
- Click on a  city to show the rankings of four main categories and top 3 ranking for all the factors
- Present the top 10 cities on the map with information according to the user ranking criteria
