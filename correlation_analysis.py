
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import pearsonr

#Loads datasets from CSV files
def load_data(productivity_file, working_hours_file):
    return pd.read_csv(productivity_file), pd.read_csv(working_hours_file)

#Filters and merges the datasets for a specific year
def preprocess_data(productivity_data, working_hours_data, year):
    filtered_productivity_data = productivity_data[productivity_data['Year'] == year]
    filtered_working_hours_data = working_hours_data[working_hours_data['Year'] == year]

    merged_data = pd.merge(
        filtered_productivity_data, filtered_working_hours_data,
        on=['Entity', 'Code', 'Year']
    )

    return merged_data.rename(columns={
        'Productivity: output per hour worked': 'Productivity',
        'Average annual working hours per worker': 'Working Hours'
    })

#Creates and saves a scatter plot with a regression line
def create_scatter_plot(data, output_file):
    plt.figure(figsize=(10, 6))
    sns.regplot(
        x='Working Hours',
        y='Productivity',
        data=data,
        scatter_kws={'alpha': 0.7, 'color': 'orange'},
        line_kws={'color': 'orange'}
    )
    plt.title('Correlation Between Annual Working Hours and Productivity (2017)', fontsize=16)
    plt.xlabel('Annual Working Hours per Worker', fontsize=14)
    plt.ylabel('Productivity (Output per Hour Worked)', fontsize=14)
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
  
#Calculates summary statistics and correlation coefficient 
def calculate_statistics(data):
    """Calculate summary statistics and correlation coefficient."""
    # Summary statistics
    summary_stats = data[['Working Hours', 'Productivity']].describe()

    # Correlation coefficient
    correlation, p_value = pearsonr(data['Working Hours'], data['Productivity'])

    return summary_stats, correlation, p_value

#Filters and merges the datasets for a specific year range
def preprocess_data_range(productivity_data, working_hours_data, start_year, end_year):
    filtered_productivity_data = productivity_data[
        (productivity_data['Year'] >= start_year) & (productivity_data['Year'] <= end_year)
    ]
    filtered_working_hours_data = working_hours_data[
        (working_hours_data['Year'] >= start_year) & (working_hours_data['Year'] <= end_year)
    ]

    tl_merged_data = pd.merge(
        filtered_productivity_data, filtered_working_hours_data,
        on=['Entity', 'Code', 'Year']
    )

    return tl_merged_data.rename(columns={
        'Productivity: output per hour worked': 'Productivity',
        'Average annual working hours per worker': 'Working Hours'
    })

#Adds a lagged version of a specified column to the dataset
def add_lagged_variables(data, lag_column, lagged_column_name, lag=1):
    data = data.sort_values(by=["Entity", "Year"]).reset_index(drop=True)
    data[lagged_column_name] = data.groupby("Entity")[lag_column].shift(lag)
    return data

#Create time lag scatter plot
def create_time_lag_scatter_plot(data, output_file_2):
    # Determine the 10-year time period from the data
    time_period = "2008–2017"

    # Create the scatter plot with a regression line
    plt.figure(figsize=(10, 6))
    sns.regplot(
        x='Lagged_WorkingHours_1',  # Assuming the column name for lagged working hours
        y='Productivity',
        data=data,
        scatter_kws={'alpha': 0.5, 'color': 'blue'},  # Scatter points styling
        line_kws={'color': 'red', 'linewidth': 2.5}  # Regression line styling
    )
    # Title and labels
    plt.title('Relationship Between 1-Year Lagged Working Hours and Productivity (Last 10 Years)', fontsize=16)
    plt.xlabel('1-Year Lagged Working Hours', fontsize=14)
    plt.ylabel('Productivity (Output per Hour Worked)', fontsize=14)
    
    # Add annotation for the 10-year time period
    plt.annotate(
        f"Time Period: {time_period}",
        xy=(0.95, 0.95),  # Position at the far right, near the top
        xycoords="axes fraction",
        fontsize=12,
        ha="right",  # Right-align the text
        backgroundcolor="white",
        bbox=dict(boxstyle="round", facecolor="lightgrey", edgecolor="black"),
    )
    
    # Grid for readability
    plt.grid(alpha=0.3)

    # Save the figure to the specified output file
    plt.savefig(output_file_2, dpi=300, bbox_inches='tight')
    plt.close()

def main():
    productivity_file = 'Data/labor-productivity-per-hour-pennworldtable.csv'
    working_hours_file = 'Data/annual-working-hours-per-worker.csv'
    output_file = 'correlation_working_hours_productivity.png'
    output_file_2 = 'time_lag_scatter_plot.png'
    year = 2017

    productivity_data, working_hours_data = load_data(productivity_file, working_hours_file)
    merged_data = preprocess_data(productivity_data, working_hours_data, year)
    create_scatter_plot(merged_data, output_file)


    summary_stats, correlation, p_value = calculate_statistics(merged_data)
    print("Summary Statistics:\n", summary_stats)
    print("Correlation Coefficient:", correlation)
    print("P-value:", p_value)

     # Create scatter plot for the range 2008–2017
    start_year, end_year = 2008, 2017
    data_2008_2017 = preprocess_data_range(productivity_data, working_hours_data, start_year, end_year)
    data_2008_2017 = add_lagged_variables(data_2008_2017, lag_column="Working Hours", lagged_column_name="Lagged_WorkingHours_1")
    data_2008_2017 = data_2008_2017.dropna(subset=["Lagged_WorkingHours_1"])

    time_period = f"{start_year}–{end_year}"
    create_time_lag_scatter_plot(data_2008_2017, output_file_2)
    print(f"Scatter plot for 2008–2017 saved to {output_file_2}")


if __name__ == '__main__':
    main()
