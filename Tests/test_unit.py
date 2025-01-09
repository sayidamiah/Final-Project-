import unittest
import pandas as pd
from io import BytesIO
from unittest.mock import patch
from Plots.correlation_analysis import load_data, preprocess_data, create_scatter_plot

class TestCorrelationAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Simulated datasets for testing
        cls.productivity_data = pd.DataFrame({
            'Entity': ['Country A', 'Country B'],
            'Code': ['A', 'B'],
            'Year': [2017, 2017],
            'Productivity: output per hour worked': [50, 40]
        })

        cls.working_hours_data = pd.DataFrame({
            'Entity': ['Country A', 'Country B'],
            'Code': ['A', 'B'],
            'Year': [2017, 2017],
            'Average annual working hours per worker': [1800, 2000]
        })

        cls.expected_merged_data = pd.DataFrame({
            'Entity': ['Country A', 'Country B'],
            'Code': ['A', 'B'],
            'Year': [2017, 2017],
            'Productivity': [50, 40],
            'Working Hours': [1800, 2000]
        })

    def test_load_data(self):
        #Verify the data loading function
        with patch('pandas.read_csv', side_effect=[self.productivity_data, self.working_hours_data]):
            prod_data, work_data = load_data('mock_prod.csv', 'mock_work.csv')
            pd.testing.assert_frame_equal(prod_data, self.productivity_data)
            pd.testing.assert_frame_equal(work_data, self.working_hours_data)


# Run the tests
if __name__ == "__main__":
    unittest.main()