import unittest
import pandas as pd
from cityfynders.UI_setup import layout_setup
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import plotly
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


class UI_setup_get(unittest.TestCase):

    """
    This is to test the UI_Setup.py and the function layout_setup.
    This function returns a 'Div' class so we test if it returns an none-null
    object

    """

    def test_uisetup(self):
        rank = pd.read_csv('../../data/rank_file.csv')
        available = list(rank.columns.values)
        for i in ['Unnamed: 0', 'City', 'State', 'Population',
                  'Natural_total_rank', 'Human_related_rank',
                  'Economy_rank', 'Tertiary_Rank', 'Latitude', 'Longitude']:
            available.remove(i)

        # Create a list of labels for dropdown
        labels = ['Air Quality', 'Water Quality', 'Fewer Toxics',
                  'Fewer Hazardous Particles', 'Green Coverage',
                  'Fewer Crimes', 'More Hospitals', 'Early Education Options',
                  'University Options', 'Employment Rate', 'Sales Revenue',
                  'Income', 'Tuition Affordability', 'Bars', 'Restaurants',
                  'Museums', 'Libraries', 'Parks', 'Top Restaurants']

        # Put available and labels in a two-dimensional list
        pairs = [available, labels]
        app = dash.Dash()
        output = 0
        output = layout_setup(pairs)
        self.assertTrue(output)


if __name__ == '__main__':
    unittest.main()
