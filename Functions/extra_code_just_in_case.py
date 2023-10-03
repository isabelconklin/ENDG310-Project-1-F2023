# import pandas as pd

# # Make a function to define seasons
# def map_to_season(month):
#     if 3 <= month <= 5:
#         return 'Spring'
#     elif 6 <= month <= 8:
#         return 'Summer'
#     elif 9 <= month <= 11:
#         return 'Fall'
#     else:
#         return 'Winter'

# import pandas as pd
# #import numpy as np

# def seasons_sort(file_path, date_column, data_columns):
#     """
#     Extract data for each year from a CSV file with a date column.

#     Parameters:
#         file_path (str): Path to the CSV file.
#         date_column (str): Name of the column containing the date.
#         data_columns (list): List of column names to extract data from.

#     Returns:
#         dict: A dictionary where keys are seasons, and values are arrays of data for each season.
#     """
#     data_by_season = {}

#     # Read the CSV file
#     df = pd.read_csv(file_path, encoding='ISO-8859-1')

#     # Convert the date column to a datetime object
#     df[date_column] = pd.to_datetime(df[date_column])

#     # Extract the year from the date column and store it in a new column
#     df['Month'] = df[date_column].dt.month

#     # Iterate through unique months
#     unique_months = df['Month'].unique()

#     # Sort months by season using map_to_season function
#     for month in unique_months:
#         # Assign seasons to the data
#         season_data['season'] = season_data['month'].apply(map_to_season)

#         # Filter the DataFrame for the current year
#         season_data = df[df['season'] == year][data_columns]

#         # Convert the filtered DataFrame to a NumPy array
#         season_data_array = season_data.to_numpy()

#         # Store the data array in the dictionary with the year as the key
#         data_by_season[season] = season_data_array

#     return data_by_season

# def seasons_sort(df, date_column):
#     """
#     Sort data by season based on a date column.

#     Parameters:
#         df (pd.DataFrame): The DataFrame containing the data.
#         date_column (str): The name of the date column.

#     Returns:
#         dict: A dictionary where keys are seasons and values are DataFrames with data for each season.
#     """


#     # Mapping of months to seasons
#     #season_mapping = {

#         # 1: 'Winter',
#         # 2: 'Winter',
#         # 3: 'Spring',
#         # 4: 'Spring',
#         # 5: 'Spring',
#         # 6: 'Summer',
#         # 7: 'Summer',
#         # 8: 'Summer',
#         # 9: 'Fall',
#         # 10: 'Fall',
#         # 11: 'Fall',
#         # 12: 'Winter'
#     #}

#     # Convert the date column to a datetime object
#     print ('Date Column: ',(date_column))
#     print ('df: ', (df))
#     print ('df[date_column]: ', (df[date_column]))
#     #print (pd.to_datetime(df[date_column]))
#     df[date_column] = pd.to_datetime(df[date_column])

#     # Extract the month from the date column
#     df['Month'] = df[date_column].dt.month

#     # Apply the season mapping to create a 'Season' column
#     df['Season'] = map_to_season(df['Month'])
#     #df['Season'] = df['Month'].map(season_mapping)

#     # Sort the DataFrame by 'Season' and 'Date'
#     df = df.sort_values(by=['Season', date_column])

#     # Split the DataFrame into separate DataFrames for each season
#     seasons_data = {}
#     for season, season_df in df.groupby('Season'):
#         seasons_data[season] = season_df.drop(['Month', 'Season'], axis=1)

#     return seasons_data