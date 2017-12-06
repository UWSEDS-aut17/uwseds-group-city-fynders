import unittest
import numpy as np
import geopy as gy
from geopy.geocoders import Nominatim

class GeoInfoTest(unittest.TestCase):

    # One shot test
    def test_get_loc(self):
        geolocator = Nominatim()
        loc = geolocator.geocode('Beijing' + ' China')
        lat = loc.latitude
        lon = loc.longitude
        self.assertTrue(np.isclose(lat, 39.90596))

if __name__ == '__main__':
    unittest.main()
