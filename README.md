# Final-Project: Productivity and Working Hours Analysis

This repository provides tools for analysing the relationship between productivity and working hours, utilising datasets, statistical methods, and visualisation techniques. The goal is to explore how working hours impact productivity using various data preprocessing and analytical methods.

## Table of Contents
- [Repository Structure](#repository-structure)
- [Features](#features)
- [Datasets](#datasets)
- [Installation](#installation)
- [Usage](#usage)
- [Outputs](#outputs)
- [Continuous Integration](#continuous-integration)

---

## Repository Structure

```plaintext
FINAL-PROJECT/
├── __pycache__/                   # Cached Python files
├── .circleci/
│   └── config.yml                # CircleCI configuration file for CI/CD
├── Data/                          # Directory containing datasets
│   ├── annual-working-hours-per-worker.csv
│   ├── labor-productivity-per-hour-pennworld.csv
├── Images/                        # Generated visualisation files
│   ├── correlation_working_hours_productivity.png
│   ├── time_lag_scatter_plot.png
├── venv/                          # Python virtual environment
├── analysis.py                    # Main analysis module
├── README.md                      # Project documentation (this file)
├── requirements.txt               # Dependencies for the project
├── unit_testing.py                # Unit tests for the project
└── unit_tests_info.txt            # Detailed test descriptions

``` 

---

## Features

1. Data Preprocessing:

Load and merge datasets of working hours and productivity.
Filter data based on specific years or ranges.

2. Statistical Analysis:

Calculate correlation and regression statistics.
Add lagged variables for time-series analysis.

3. Visualisations:

Generate scatter plots and time-lag scatter plots.
Save plots to the Images/ directory.

4. Automated Testing:

Unit tests to ensure correctness of data handling, statistical analysis, and visualisation.

## Datasets

The Data folder contains the following datasets, which are used to create visualisations and analyse the relationship between productivity and working hours:

- annual-working-hours-per-worker.csv: Contains the average annual working hours per worker for various countries over multiple years.

- labor-productivity-per-hour-pennworld.csv: Provides productivity metrics (output per hour worked) for the same set of countries.

These datasets are preprocessed, merged, and analysed using the tools in the analysis.py module to generate insights and visualisations.

## Installation

Clone the repository:
git clone https://github.com/yourusername/final-project.git

Navigate into the project directory:
cd final-project

Set up a Python virtual environment:
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

## Usage

1. Run Analysis
The main analysis script is analysis.py. It includes functions to:

- Load data.
- Preprocess datasets.
- Generate scatter plots and statistical summaries.

To run the script: python analysis.py

2. Run Tests
The unit_testing.py file contains unit tests for all key functions. 

To execute the tests: python -m unittest unit_testing.py

## Outputs

### Visualisations

The following plots are generated and saved in the Images/ directory:

- correlation_working_hours_productivity.png: Correlation scatter plot between working hours and productivity.
- time_lag_scatter_plot.png: Scatter plot showing lagged effects of working hours on productivity.

### Statistical Summary
The analysis script outputs key metrics, including:

- Correlation coefficients.
- Regression line parameters (slope and intercept).

## Continuous Integration
This repository uses CircleCI for continuous integration. The .circleci/config.yml file defines the CI pipeline, ensuring that all tests pass before merging code.

