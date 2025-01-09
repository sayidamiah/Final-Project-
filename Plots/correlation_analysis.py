
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def load_data(productivity_file, working_hours_file):
    """Load datasets from CSV files."""
    return pd.read_csv(productivity_file), pd.read_csv(working_hours_file)

def preprocess_data(productivity_data, working_hours_data, year):
    """Filter and merge the datasets for a specific year."""
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

def create_scatter_plot(data, output_file):
    """Create and save a scatter plot with a regression line."""
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

def main():
    productivity_file = 'Data/labor-productivity-per-hour-pennworldtable.csv'
    working_hours_file = 'Data/annual-working-hours-per-worker.csv'
    output_file = 'correlation_working_hours_productivity.png'
    year = 2017

    productivity_data, working_hours_data = load_data(productivity_file, working_hours_file)
    merged_data = preprocess_data(productivity_data, working_hours_data, year)
    create_scatter_plot(merged_data, output_file)

if __name__ == '__main__':
    main()
