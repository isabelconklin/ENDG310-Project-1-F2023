import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Prompt used in ChatGPT: I would like to create a function to plot a graph which will have 2 datasets. One will be the tourism dataset and the other will be the wages dataset. What kind of graph should I use? 

def wages_tourism_graph(tourism_data, wage_data):
    """
    Create a grouped bar chart to compare tourism and wage datasets over the years.

    Parameters:
        tourism_data (Dictionary): The tourism-related dataset containing 'Year' and the data to be compared.
        wage_data (Dictionary): The wage dataset containing 'Year' and the data to be compared.

    Returns:
        None (displays the grouped bar chart).
    """
    # Extract the years from the dataframes
    years = list(tourism_data.keys())
    
    # Define the width of each bar
    bar_width = 0.35
    
    # Calculate the positions for bars
    x = np.arange(len(years))
    
    # Create a figure
    plt.figure(figsize=(10, 6))

    # Get values for bar graph
    # Filter the tourism data to match the years in wage data
    common_years = set(tourism_data.keys()).intersection(wage_data.keys())
    total_people = [np.sum(tourism_data[year] / 1e6) for year in common_years]
    average_wage_by_year = [np.mean(wage_data[year]) for year in common_years]
    
    # Create the grouped bar chart
    plt.bar(x - bar_width/2, total_people, bar_width, label='Tourism', alpha=0.7)
    plt.bar(x + bar_width/2, average_wage_by_year, bar_width, label='Wages', alpha=0.7)
    
    # Customize the plot labels and title
    plt.xlabel('Year')
    plt.ylabel('Values (Million)')
    plt.title('Comparison of Tourism and Wage Data Over the Years')
    
    # Set the x-axis labels to be the years
    plt.xticks(x, common_years)
    
    # Add a legend
    plt.legend()
    
    # Show the plot
    plt.show()


# # Example usage:
# tourism_data = {
#     2020: [1000000, 1200000, 1100000],
#     2021: [1100000, 1300000, 1200000],
#     2022: [1200000, 1400000, 1300000],
#     2023: [1300000, 1500000, 1400000]
# }

# wage_data = {
#     2020: [50000, 52000, 53000],
#     2021: [52000, 54000, 55000],
#     2022: [54000, 56000, 57000]
# }

# wages_tourism_graph(tourism_data, wage_data)


# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# def wages_tourism_graph(tourism_data, wage_data):
#     """
#     Create a grouped bar chart to compare tourism and wage datasets over the years.

#     Parameters:
#         tourism_data (Dictionary): The tourism-related dataset containing 'Year' and the data to be compared.
#         wage_data (Dicctionary): The wage dataset containing 'Year' and the data to be compared.

#     Returns:
#         None (displays the grouped bar chart).
#     """
#     import pandas as pd

#     # Assuming your tourism_data and wage_data are dictionaries
#     # Convert them to Pandas DataFrames for easier manipulation
#     # tourism_df = pd.DataFrame.from_dict(tourism_data)
#     # wage_df = pd.DataFrame.from_dict(wage_data)

#     # # Get the common years between both datasets
#     # common_years = set(tourism_df['Year']).intersection(set(wage_df['Year']))

#     # # Filter the tourism dataset to keep only the common years
#     # filtered_tourism_df = tourism_df[tourism_df['Year'].isin(common_years)]

#     # Extract the years from the dataframes
#     years = list(wage_data.keys())
    
#     # Define the width of each bar
#     bar_width = 0.35
    
#     # Calculate the positions for bars
#     x = np.arange(len(years))
    
#     # Create a figure
#     plt.figure(figsize=(10, 6))

#     # Get values for bar graph
#     # Filter the tourism data to match the years in wage data
#     common_years = set(tourism_data.keys()).intersection(wage_data.keys())
#     total_people = [np.sum(tourism_data[year] / 1e6) for year in common_years]
#     average_wage_by_year = [np.mean(wage_data[year]) for year in common_years]
    
#     # Create the grouped bar chart
#     plt.bar(x - bar_width/2, total_people, bar_width, label='Tourism', alpha=0.7)
#     plt.bar(x + bar_width/2, average_wage_by_year, bar_width, label='Wages', alpha=0.7)
    
#     # Customize the plot labels and title
#     plt.xlabel('Year')
#     plt.ylabel('Values')
#     plt.title('Comparison of Tourism and Wage Data Over the Years')
    
#     # Set the x-axis labels to be the years
#     plt.xticks(x, years)
    
#     # Add a legend
#     plt.legend()
    
#     # Show the plot
#     plt.show()
