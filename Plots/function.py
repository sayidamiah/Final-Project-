import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

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

# Filter datasets for the overlapping year (2017)
filtered_productivity_data = productivity_data[productivity_data['Year'] == 2017]
filtered_working_hours_data = working_hours_data[working_hours_data['Year'] == 2017]

# Merge the filtered datasets
merged_data = pd.merge(filtered_productivity_data, filtered_working_hours_data, on=['Entity', 'Code', 'Year'])

# Rename columns for better readability
merged_data.rename(columns={
    'Productivity: output per hour worked': 'Productivity',
    'Average annual working hours per worker': 'Working Hours'
}, inplace=True)

#Filter datasets for the overlapping year (2017)
filtered_productivity_data = productivity_data[productivity_data['Year'] == 2017]
filtered_working_hours_data = working_hours_data[working_hours_data['Year'] == 2017]

#Merge the filtered datasets
merged_data_2017 = pd.merge(filtered_productivity_data, filtered_working_hours_data, on=['Entity', 'Code', 'Year'])

#Rename columns for better readability
merged_data_2017.rename(columns={
    'Productivity: output per hour worked': 'Productivity',
    'Average annual working hours per worker': 'Working Hours'
}, inplace=True)


#Scatter plot
plt.figure(figsize=(10, 6))
sns.regplot(
    x='Working Hours', 
    y='Productivity', 
    data=merged_data, 
    scatter_kws={'alpha': 0.7, 'color': 'orange'}, 
    line_kws={'color': 'orange'}
)

#Adding titles and labels to scatter plot
plt.title('Correlation Between Annual Working Hours and Productivity (2017)', fontsize=16)
plt.xlabel('Annual Working Hours per Worker', fontsize=14)
plt.ylabel('Productivity (Output per Hour Worked)', fontsize=14)

plt.savefig('correlation_working_hours_productivity.png', dpi=300, bbox_inches='tight')