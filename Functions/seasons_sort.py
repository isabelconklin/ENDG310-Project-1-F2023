import pandas as pd

# Make a function to define seasons
def map_to_season(month):
    if 3 <= month <= 5:
        return 'Spring'
    elif 6 <= month <= 8:
        return 'Summer'
    elif 9 <= month <= 11:
        return 'Fall'
    else:
        return 'Winter'

def seasons_sort(file_path, date_column, data_columns):
    """
    Extract data for each season from a CSV file with a date column.

    Parameters:
        file_path (str): Path to the CSV file.
        date_column (str): Name of the column containing the date.
        data_columns (list): List of column names to extract data from.

    Returns:
        dict: A dictionary where keys are seasons, and values are arrays of data for each season.
    """
    data_by_season = {}

    # Read the CSV file
    df = pd.read_csv(file_path, encoding='ISO-8859-1')

    # Convert the date column to a datetime object
    df[date_column] = pd.to_datetime(df[date_column])

    # Extract the month from the date column and store it in a new column 'Month'
    df['Month'] = df[date_column].dt.month

    # Iterate through unique months
    unique_months = df['Month'].unique()

    # Sort months by season using map_to_season function
    for month in unique_months:
        # Assign seasons to the data
        season = map_to_season(month)

        # Filter the DataFrame for the current season
        season_data = df[df['Month'] == month][data_columns]

        # Convert the filtered DataFrame to a NumPy array
        season_data_array = season_data.to_numpy()

        # Store the data array in the dictionary with the season as the key
        data_by_season[season] = season_data_array

    return data_by_season
