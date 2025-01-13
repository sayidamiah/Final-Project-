import unittest
import pandas as pd
from io import BytesIO
from scipy.stats import linregress
from unittest.mock import patch
from analysis import load_data, preprocess_data, create_scatter_plot, calculate_statistics,preprocess_data_range, add_lagged_variables, create_time_lag_scatter_plot

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

    def test_calculate_statistics(self):
        # Use the expected merged dataset
        summary_stats, correlation, p_value = calculate_statistics(self.expected_merged_data)

        # Expected summary statistics and correlation values (calculated manually or separately)
        expected_correlation = -1.0
        expected_p_value = 0.0

        # Assert correlation and p-value
        self.assertAlmostEqual(correlation, expected_correlation, places=2, msg="Correlation coefficient mismatch.")
        self.assertTrue(p_value > 0, "P-value should be greater than 0.")
    
    def test_preprocess_data_range(self):
        # Test for correct filtering and merging for a year range
        merged_data = preprocess_data_range(self.productivity_data, self.working_hours_data, 2008, 2017)
        expected_data = self.expected_merged_data
        pd.testing.assert_frame_equal(merged_data, expected_data)
    
    def test_add_lagged_variables(self):
        # Test the creation of lagged variables
        data = pd.DataFrame({
            'Entity': ['Country A', 'Country A', 'Country A'],
            'Year': [2008, 2009, 2010],
            'Working Hours': [1800, 1700, 1600]
        })
        result = add_lagged_variables(data, lag_column="Working Hours", lagged_column_name="Lagged_WorkingHours_1")
        expected = pd.DataFrame({
            'Entity': ['Country A', 'Country A', 'Country A'],
            'Year': [2008, 2009, 2010],
            'Working Hours': [1800, 1700, 1600],
            'Lagged_WorkingHours_1': [None, 1800, 1700]
        })
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))
    
    def test_create_time_lag_scatter_plot(self):
        # Test time lag scatter plot creation
        data = add_lagged_variables(self.expected_merged_data, lag_column="Working Hours", lagged_column_name="Lagged_WorkingHours_1")
        buf = BytesIO()
        create_time_lag_scatter_plot(data, output_file_2=buf)


# Run the tests
if __name__ == "__main__":
    unittest.main()

