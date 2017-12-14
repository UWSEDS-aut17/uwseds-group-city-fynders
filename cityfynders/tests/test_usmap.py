import unittest
import pandas as pd
from cityfynders.plotly_usmap import usmap, newdf


class usmapget(unittest.TestCase):
    """
    This is to test the two funcions usmap and newdf in ploltly_usmap.py
    The frist test is a smoke test to see if the function can run
    The second test is done by giving a particular user imput (5 factors)
    and see if the newdf funcion returns a dataframe with the correct
    ranking of cities

    """

    # Smoke test
    def test_usmap(self):
        runwell = True
        rank = pd.read_csv("../../data/rank_file.csv")
        usmap(rank)
        self.assertTrue(runwell)

    # def test_usmap_single_point
    def test_newdf(self):
        rank = pd.read_csv("../../data/rank_file.csv")
        df = newdf(rank, 'Air', 'Water', 'Toxics',
                   'Hazardous', 'Green_score')
        for index, row in df.iterrows():
            if row['City'] == "Portland":
                target = row['Total']

        self.assertTrue(target == 1.0)


if __name__ == '__main__':
    unittest.main()
