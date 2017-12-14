import pandas as pd
import numpy as np
import unittest
import geopy as gy
from geopy.geocoders import Nominatim

import cityfynders.data_processing as dp


class DataProcessingTest(unittest.TestCase):
    """
    Please run this test in cityfynders/ dir
    """

    def setUp(self):
        print('setUp...')

    # test for data_rank
    def test_data_rank(self):
        # [natural, human, economy, tertiary] = dp.read_data()
        natural1 = pd.read_csv('../data/Natural.csv')
        human1 = pd.read_csv('../data/human_related.csv')
        economy1 = pd.read_csv('../data/economy.csv')
        tertiary1 = pd.read_csv("../data/tertiary.csv")
        (natural, human, economy, tertiary) = \
            dp.data_rank(natural1, human1, economy1, tertiary1)
        self.assertTrue(np.isclose(human['Human_related_rank'][0], 27.0))

    # test for geopy
    def test_get_loc(self):
        geolocator = Nominatim()
        loc = geolocator.geocode('Beijing' + ' China')
        lat = loc.latitude
        lon = loc.longitude
        self.assertTrue(np.isclose(lat, 39.90596))

    # test for find_loc
    def test_find_loc(self):
        # [natural, human, economy, tertiary] = dp.read_data()
        human = pd.read_csv('../data/human_related.csv')
        (Lat, Lon) = dp.find_loc(human)
        self.assertTrue(np.isclose(Lat[0], 33.7490987))

    # test for create_rank
    def test_create_rank(self):
        # [natural, human, economy, tertiary] = dp.read_data()
        natural1 = pd.read_csv('../data/Natural.csv')
        human1 = pd.read_csv('../data/human_related.csv')
        economy1 = pd.read_csv('../data/economy.csv')
        tertiary1 = pd.read_csv("../data/tertiary.csv")
        (natural, human, economy, tertiary) = \
            dp.data_rank(natural1, human1, economy1, tertiary1)
        rank1 = pd.read_csv('../data/rank_file.csv')
        Lat = rank1['Latitude']
        Lon = rank1['Longitude']
        rank = dp.create_rank(natural, human, economy, tertiary, Lat, Lon)
        self.assertTrue(np.isclose(rank['Economy_rank'][0], 34.0))

    def tearDown(self):
        print('tearDown...')


if __name__ == '__main__':
    unittest.main()
