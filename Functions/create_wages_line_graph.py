import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def create_wages_line_graph(filtered_data):
    """
    Create a line graph of the average wage for tourism-related jobs over the years.

    Parameters:
        filtered_data (Dictionary): The filtered dictionary containing wage data with keys 'Year' and  values 'Average_Wage_Salaire_Moyen'.

    Returns:
        None (displays the line graph).
    """     

    # # Drop rows with NaN values in 'Average_Wage_Salaire_Moyen' column
    # for year in filtered_data:
    #     print('Year: ', year, ' = ', filtered_data[year], ' Is number: ', np.isnan(filtered_data[year]))
    # filtered_data_values = [np.isnan(data) for data in filtered_data.values()]
    # # filtered_data.dropna(subset=['Average_Wage_Salaire_Moyen'])

    # Group the data by 'Year' and calculate the average wage for each year
    years = list(filtered_data.keys())
    average_wage_by_year = [np.mean(data) for data in filtered_data.values()]
    # average_wage_by_year = filtered_data.groupby('Year')['Average_Wage_Salaire_Moyen'].mean().reset_index()

    print('Years', years)
    print('Average wage by year', average_wage_by_year)

    # Create a line plot
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.plot(years, average_wage_by_year, color='tomato', marker='o', linestyle='-')

    # Customize the plot labels and title
    plt.xlabel('Year')
    plt.ylabel('Average Wage')
    plt.title('Average Wage for Tourism-Related Jobs Over the Years')

    # Show the grid
    plt.grid(True)

    # Display the plot
    plt.show()
