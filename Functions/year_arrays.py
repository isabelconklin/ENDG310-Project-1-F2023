import pandas as pd
#import numpy as np

def make_year_arrays(file_path, date_column, data_columns):
    """
    Extract data for each year from a CSV file with a date column.

    Parameters:
        file_path (str): Path to the CSV file.
        date_column (str): Name of the column containing the date.
        data_columns (list): List of column names to extract data from.

    Returns:
        dict: A dictionary where keys are years, and values are arrays of data for each year.
    """
    data_by_year = {}

    # Read the CSV file
    df = pd.read_csv(file_path, encoding='ISO-8859-1')

    # Convert the date column to a datetime object
    df[date_column] = pd.to_datetime(df[date_column])

    # Extract the year from the date column and store it in a new column
    df['Year'] = df[date_column].dt.year

    # Iterate through unique years
    unique_years = df['Year'].unique()
    for year in unique_years:
        # Filter the DataFrame for the current year
        year_data = df[df['Year'] == year][data_columns]

        # Convert the filtered DataFrame to a NumPy array
        year_data_array = year_data.to_numpy()

        # Store the data array in the dictionary with the year as the key
        data_by_year[year] = year_data_array

    return data_by_year
