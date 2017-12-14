import unittest
import pandas as pd
from cityfynders.plotly_usmap import usmap, newdf

class usmapget(unittest.TestCase):

    # Smoke test
    def test_usmap(self):
        runwell = True
        rank = pd.read_csv("../../data/rank_file.csv")
        usmap(rank)
        self.assertTrue(runwell)

    # def test_usmap_single_point

if __name__ == '__main__':
    unittest.main()
