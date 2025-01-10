import unittest
import pandas as pd
from io import BytesIO
from scipy.stats import linregress
from unittest.mock import patch
from correlation_analysis import load_data, preprocess_data, create_scatter_plot

class TestAnalysis(unittest.TestCase):

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

    def test_preprocess_data(self):
        #Test the preprocessing function
        merged_data = preprocess_data(self.productivity_data, self.working_hours_data, 2017)
        pd.testing.assert_frame_equal(merged_data, self.expected_merged_data)
    
    def test_create_scatter_plot(self):
        # Test plot creation
        buf = BytesIO()
        create_scatter_plot(
            data=self.expected_merged_data,
            output_file=buf
        )

    def test_line_fitting(self):
        # Test the slope and intercept of the regression line
        merged_data = self.expected_merged_data

        # Calculate the regression line
        slope, intercept, _, _, _ = linregress(merged_data['Working Hours'], merged_data['Productivity'])

        # Expected slope and intercept (calculated manually)
        expected_slope = -0.05  
        expected_intercept = 140

        # Assert the slope and intercept are correct
        self.assertAlmostEqual(slope, expected_slope, places=2, msg="Slope does not match the expected value.")
        self.assertAlmostEqual(intercept, expected_intercept, places=2, msg="Intercept does not match the expected value.")


# Run the tests
if __name__ == "__main__":
    unittest.main()

