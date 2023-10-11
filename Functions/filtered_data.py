import pandas as pd
import numpy as np
# Prompt used in ChatGPT: I have some data showing wages for the years 2018-2022 and I would like to filter it so that I only have the wages for jobs impacted by tourism, how could I make a function for this?
def filter_jobs_impacted_by_tourism(data, tourism_keywords):
    """
    Filter a dataset to include only jobs impacted by tourism based on specified keywords.

    Parameters:
        data (DataFrame): The dataset containing wage data.
        tourism_keywords (list): A list of keywords or job titles related to tourism.

    Returns:
        DataFrame: A filtered DataFrame containing only rows corresponding to tourism-related jobs.
    """
    # Convert job titles to lowercase for case-insensitive matching
    data['NOC_Title'] = data['NOC_Title'].str.lower()

    # Filter the dataset based on tourism-related keywords
    filtered_data = data[data['NOC_Title'].str.contains('|'.join(tourism_keywords), case=False) & ~np.isnan(data['Median_Wage_Salaire_Median'])]
    # filtered_data = filtered_data[filtered_data['Average_Wage_Salaire_Moyen']]
    # filtered_data = [np.isnan(data) for data in filtered_data]
    return filtered_data
