import pandas as pd 
import matplotlib as plt 

#Loading datasets
working_hours_data = pd.read_csv('Data/annual-working-hours-per-worker.csv')
productivity_data = pd.read_csv('Data/labor-productivity-per-hour-pennworldtable.csv')

#Merging datasets
merged_data = pd.merge(productivity_data, working_hours_data, on=['Entity', 'Year'])

#Renaming the datasets
merged_data.rename(columns={
    'Productivity: output per hour worked': 'Productivity',
    'Average annual working hours per worker': 'Working Hours'
}, inplace=True)