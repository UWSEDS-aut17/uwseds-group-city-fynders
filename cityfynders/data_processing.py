import pandas as pd
import numpy as np
import geopy as gy
from geopy.geocoders import Nominatim


def read_data():
    """
    Read data from Github repository. The file is small, so we upload it in the Github.
    """
    # Read data from github
    natural = pd.read_csv('../data/Natural.csv')
    human = pd.read_csv('../data/human_related.csv')
    economy = pd.read_csv('../data/economy.csv')
    tertiary = pd.read_csv("../data/tertiary.csv")

    return natural, human, economy, tertiary


def data_rank(natural, human, economy, tertiary):
    """
    Get data ranks for four different categories related to city choices.

    natural, human, economy, tertiary: all in DataFrame format.
    """

    #natural
    natural['Air'] = natural['Air'].rank(ascending=0)
    natural['Water_quality'] = natural['Water_quality'].rank(ascending=0)
    natural['Toxics'] = natural['Toxics'].rank(ascending=0)
    natural['Hazardous'] = natural['Hazardous'].rank(ascending=0)
    natural['Green_score_rank'] = natural['Green_score'].rank(ascending=1)
    natural['Green_score_rank'].fillna(natural['Green_score_rank'].max()+1, inplace=True)
    natural['Sanitation'].fillna(natural['Sanitation'].max()+1, inplace=True)
    natural['Natural_total_score'] = (natural['Air'] + natural['Water_quality'] + natural['Toxics']
                                      + natural['Hazardous'] + natural['Green_score_rank'])
    natural['Natural_total_rank'] = natural['Natural_total_score'].rank(ascending=1)

    #human related
    human['total crime'] = human['Violent'] + human['Rape'] + human['Robbery']
    human['crime_rank'] = human['total crime'].rank(ascending=1)
    # Fill the NaN data to the max ranking + 1 with non-NaN data.
    human['crime_rank'].fillna(human['crime_rank'].max() + 1,inplace=True)

    human['hospital_rank']= human['NumHospital'].rank(ascending=0)
    human['hospital_rank'].fillna(human['hospital_rank'].max() + 1,inplace=True)

    human['early_education_rank'] = human['AvgSATScore'].rank(ascending=0)
    human['early_education_rank'].fillna(human['early_education_rank'].max() + 1,inplace=True)

    human['Population'] = pd.to_numeric(human['Population'], errors ='coerce')
    a = np.multiply(human['Percent_graduate_degree'], human['Population'])
    a = a.rank(ascending=0)
    b = human['Colleges'].rank(ascending=0)
    human['advanced_education_rank'] = (a + b).rank(ascending=1)
    human['advanced_education_rank'].fillna(human['advanced_education_rank'].max() + 1,inplace=True)

    human['Human_related_rank'] = (human['crime_rank'] + human['hospital_rank'] + human['early_education_rank'] +\
                                   human['advanced_education_rank']).rank(ascending=1)

    #economy
    economy['Rank_Unemployment'] = economy['Percent unemployment'].rank(ascending = 1)
    economy['Rank_Sales'] = economy['Local tax rate'].rank(ascending = 1)
    economy['Rank_Income'] = economy['Median Income'].rank(ascending = 0)
    economy['Rank_Tuition'] = economy['AvgTuition'].rank(ascending = 1)
    economy['Rank_Unemployment'].fillna(economy['Rank_Unemployment'].max() + 1, inplace=True)
    economy['Rank_Sales'].fillna(economy['Rank_Sales'].max() + 1, inplace=True)
    economy['Rank_Income'].fillna(economy['Rank_Income'].max() + 1, inplace=True)
    economy['Rank_Tuition'].fillna(economy['Rank_Tuition'].max() + 1, inplace=True)
    economy['Sum'] = (economy['Rank_Unemployment'] + economy['Rank_Sales'] +
                      economy['Rank_Income'] + economy['Rank_Tuition'])
    economy['Economy_rank'] = economy['Sum'].rank(ascending = 1)

    #tertiary
    tertiary['Bar_Rank'] = tertiary['Bars'].rank(ascending = 0)
    tertiary['Restaurant_Rank'] = tertiary['Restaurant'].rank(ascending = 0)
    tertiary['Museums_Rank'] = tertiary['Museums'].rank(ascending = 0)
    tertiary['Libraries_Rank'] = tertiary['Libraries'].rank(ascending = 0)
    tertiary['Park_Rank'] = tertiary['Park_acres_per_1000_residents'].rank(ascending = 0)
    tertiary['TopRes_Rank'] = tertiary['NumTop200Restau'].rank(ascending = 0)
    tertiary['Bar_Rank'].fillna(tertiary['Bar_Rank'].max() + 1,inplace=True)
    tertiary['Restaurant_Rank'].fillna(tertiary['Restaurant_Rank'].max() + 1,inplace=True)
    tertiary['Museums_Rank'].fillna(tertiary['Museums_Rank'].max() + 1,inplace=True)
    tertiary['Libraries_Rank'].fillna(tertiary['Libraries_Rank'].max()+1,inplace=True)
    tertiary['Park_Rank'].fillna(tertiary['Park_Rank'].max() + 1,inplace=True)
    tertiary['TopRes_Rank'].fillna(tertiary['TopRes_Rank'].max() + 1,inplace=True)
    tertiary['Total_Rank'] = tertiary['Bar_Rank'] + tertiary['Restaurant_Rank'] + tertiary['Museums_Rank'] +\
                            tertiary['Libraries_Rank'] + tertiary['Park_Rank'] + tertiary['TopRes_Rank']
    tertiary['Tertiary_Rank'] = tertiary['Total_Rank'].rank(ascending = 1)

    return natural, human, economy, tertiary


def create_rank(natural, human, economy, tertiary, Lat, Lon):
    """
    make all rank into one Dataframe and save as csv file.

    All inputs are in DataFrame format.
    """

    rank = pd.DataFrame()

    # get natural-relate rank
    rank['Air'] = natural['Air']
    rank['Water'] = natural['Water_quality']
    rank['Toxics'] = natural['Toxics']
    rank['Hazardous'] = natural['Hazardous']
    rank['Green_score'] = natural['Green_score_rank']
    rank['Natural_total_rank'] = natural['Natural_total_rank']

    # get human-relate rank
    rank['City'] = human['City']
    rank['State'] = human['State']
    rank['Population'] = human['Population']
    rank['Crime_rank'] = human['crime_rank']
    rank['Hospital_rank'] = human['hospital_rank']
    rank['Early_education_rank'] = human['early_education_rank']
    rank['University_education_rank'] = human['advanced_education_rank']
    rank['Human_related_rank'] = human['Human_related_rank']

    # get economy-relate rank
    rank['Rank_unemployment'] = economy['Rank_Unemployment']
    rank['Rank_sale_rate'] = economy['Rank_Sales']
    rank['Rank_Income'] = economy['Rank_Income']
    rank['Rank_Tuition'] = economy['Rank_Tuition']
    rank['Economy_rank'] = economy['Economy_rank']

    # get tertiary-relate rank
    rank['Bar_Rank'] = tertiary['Bar_Rank']
    rank['Restaurant_Rank'] = tertiary['Restaurant_Rank']
    rank['Museums_Rank'] = tertiary['Museums_Rank']
    rank['Libraries_Rank'] = tertiary['Libraries_Rank']
    rank['Park_Rank'] = tertiary['Park_Rank']
    rank['TopRes_Rank'] = tertiary['TopRes_Rank']
    rank['Tertiary_Rank'] = tertiary['Tertiary_Rank']

    # get location information
    rank['Latitude'] = Lat
    rank['Longitude'] = Lon

    rank.to_csv("../data/rank_file.csv")

    return rank


def find_loc(dataframe):
    """
    Find latitude and longitude using geopy package.
    Returnn latitude and longitude.
    """
    
    geolocator = Nominatim()
    lat = []
    lon = []
    for index, row in dataframe.iterrows():
        loc = geolocator.geocode(row['City'] + ' ' + row['State'] + ' United States')
        lat.append(loc.latitude)
        lon.append(loc.longitude)
    return lat, lon
