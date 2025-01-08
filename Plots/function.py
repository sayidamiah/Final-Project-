import pandas as pd 
import matplotlib as plt 

# Load datasets
working_hours_data = pd.read_csv('Data/annual-working-hours-per-worker.csv')
productivity_data = pd.read_csv('Data/labor-productivity-per-hour-pennworldtable.csv')

# Merge datasets
merged_data = pd.merge(productivity_data, working_hours_data, on=['Entity', 'Year'])
