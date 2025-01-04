import unittest
class TestDataMerge(unittest.TestCase):

    def setUp(self):
        # Create small test datasets for validation
        self.test_working_hours = pd.DataFrame({
            'entity': ['CountryA', 'CountryB'],
            'code': ['A', 'B'],
            'year': [2000, 2001],
            'average_annual_working_hours_per_worker': [2000, 1900]
        })

        self.test_productivity = pd.DataFrame({
            'entity': ['CountryA', 'CountryB'],
            'code': ['A', 'B'],
            'year': [2000, 2001],
            'productivity:_output_per_hour_worked': [50.0, 45.0]
        })

# Run the tests
if __name__ == "__main__":
    unittest.main()