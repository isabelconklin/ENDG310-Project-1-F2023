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

def seasons_sort(df, date_column):
    """
    Sort data by season based on a date column.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        date_column (str): The name of the date column.

    Returns:
        dict: A dictionary where keys are seasons and values are DataFrames with data for each season.
    """


    # Mapping of months to seasons
    #season_mapping = {

        # 1: 'Winter',
        # 2: 'Winter',
        # 3: 'Spring',
        # 4: 'Spring',
        # 5: 'Spring',
        # 6: 'Summer',
        # 7: 'Summer',
        # 8: 'Summer',
        # 9: 'Fall',
        # 10: 'Fall',
        # 11: 'Fall',
        # 12: 'Winter'
    #}

    # Convert the date column to a datetime object
    print ('Date Column: ',(date_column))
    print ('df: ', (df))
    print ('df[date_column]: ', (df[date_column]))
    #print (pd.to_datetime(df[date_column]))
    df[date_column] = pd.to_datetime(df[date_column])

    # Extract the month from the date column
    df['Month'] = df[date_column].dt.month

    # Apply the season mapping to create a 'Season' column
    df['Season'] = map_to_season(df['Month'])
    #df['Season'] = df['Month'].map(season_mapping)

    # Sort the DataFrame by 'Season' and 'Date'
    df = df.sort_values(by=['Season', date_column])

    # Split the DataFrame into separate DataFrames for each season
    seasons_data = {}
    for season, season_df in df.groupby('Season'):
        seasons_data[season] = season_df.drop(['Month', 'Season'], axis=1)

    return seasons_data
