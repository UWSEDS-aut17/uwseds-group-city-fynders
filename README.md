![usa-cities-collage](https://user-images.githubusercontent.com/32344254/32299959-b57f7bf6-bf14-11e7-8c03-90c0a7e29d0a.jpg)

# Which city would you like to live in?

**City Fynders** *(Xiangyu Zhang, Wendan Yan, Yiran Zhang, Zhuochen Han)*

## What is CityFynders?
The most common question for people who decide to start a career or make a family is: where shall we live in the USA? `cityfynders` package helps people make choices for the city they want to live in through a webpage-based UI.


**Highlights:**
- Four Categories of indicators
- Customized  indicators
- Geographic Visualization on a map

## DATA
Four different categories of data are included:
1. Environmental-related: city annual weather, precipitation, air pollution, water quality, green index
2. Human related: Population, crime rate, unemployment rate, school and education quality
3. Economics related: cost of living, tax rates
4. Tertiary industry related: Restaurants, museums, bars
The detailed data resources are listed on `./doc/Data.md`. Sample links of the data:

https://www.infoplease.com/science-health/weather/climate-100-selected-us-cities
https://www.kaggle.com/sogun3/uspollution/data


## Potential usage
The interacted webpag-based tool is designed for two main usages:

1. Normal uses: get general result and used-DIY result based on their preferences of factors.

2. Research uses: get general results and make check the correlations of different factors.

## installing and use guidance
1. For mac, navigate (`cd`) to the location you would like to copy the `cityfynders` package; for Windows, we recommend you to install [Anaconda](https://www.anaconda.com/download/#macos) `cd` through the terminal in the conda.

2. Clone the `cityfynders` by typing the following code in terminal:

<pre><code>
git clone https://github.com/UWSEDS-aut17/uwseds-group-city-fynders.git
</code></pre>

3. In the `uwseds-group-city-fynders` directory, initiate the setup (it will automatically install the packages if you do not have them):

<pre><code>
python setup.py develop --user
</code></pre>

4. Run the script to generate webpage-based UI server:

<pre><code>
python ./scripts/city_script.py
</code></pre>

5. Copy the following url in the browser:

<pre><code>
http://127.0.0.1:8050/
</code></pre>

If your terminal shows the different url, copy that one.

6. Choose your factor and get the city you want!!!
