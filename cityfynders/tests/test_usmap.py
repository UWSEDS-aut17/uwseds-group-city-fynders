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
    def test_newdf(self):
        rank = pd.read_csv("../../data/rank_file.csv")
        df = newdf(rank,'Air','Water','Toxics',
         'Hazardous','Green_score')

        for index, row in df.iterrows():
            if row['City']=="Portland":
                target = row['Total']

        self.assertTrue(target == 1.0)

if __name__ == '__main__':
    unittest.main()
