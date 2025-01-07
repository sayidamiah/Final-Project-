import unittest
import pandas as pd
import os
import matplotlib as plt
class TestDataLoading(unittest.TestCase):


    def setUp(self):
        # Paths to the CSV files
        self.working_hours_path = 'Data/annual-working-hours-per-worker.csv'
        self.productivity_path = 'Data/labor-productivity-per-hour-pennworldtable.csv'
    
    def test_files_exist(self):
        # Check if the files exist
        self.assertTrue(os.path.exists(self.working_hours_path), "Working hours file does not exist.")
        self.assertTrue(os.path.exists(self.productivity_path), "Productivity file does not exist.")


# Run the tests
if __name__ == "__main__":
    unittest.main()