import unittest
import pandas as pd
from cityfynders.plotly_usmap import usmap

class usmapget(unittest.TestCase):

    # One shot test
    def test_usmap(self):
        runwell = True
        rank = pd.read_csv("../../data/rank_file.csv")
        usmap(rank)
        self.assertTrue(runwell)

if __name__ == '__main__':
    unittest.main()
