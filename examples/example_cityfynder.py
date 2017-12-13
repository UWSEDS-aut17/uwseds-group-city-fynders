# Which city would like to live?
# Created by City Fynders - University of Washington

import pandas as pd
import numpy as np
import geopy as gy
from geopy.geocoders import Nominatim

import cityfynders.data_processing as dp
from cityfynders.plotly_usmap import usmap



# import data
(natural, human, economy, tertiary) = dp.read_data()


# Add ranks in the DataFrame
(natural, human, economy, tertiary) = dp.data_rank(natural, human, economy, tertiary)


# Get location information
(Lat, Lon) = dp.find_loc(human)


# Create a rank DataFrame and save as csv file
rank = dp.create_rank(natural, human, economy, tertiary, Lat, Lon)


# Plot US city general ranking usmap
usmap(rank)
