import unittest
import pandas as pd
import matplotlib as plt
class TestDataLoading(unittest.TestCase):


    def setUp(self):
        # Paths to the CSV files
        self.working_hours_path = 'annual-working-hours-per-worker.csv'
        self.productivity_path = 'labor-productivity-per-hour-pennworldtable.csv'

# Run the tests
if __name__ == "__main__":
    unittest.main()