import matplotlib.pyplot as plt
import numpy as np

def create_grouped_bar_chart(tourism_data, wage_data):
    """
    Create a grouped bar chart to compare tourism and wage datasets over the years.

    Parameters:
        tourism_data (DataFrame): The tourism-related dataset containing 'Year' and the data to be compared.
        wage_data (DataFrame): The wage dataset containing 'Year' and the data to be compared.

    Returns:
        None (displays the grouped bar chart).
    """
    # Extract the years from the dataframes
    years = tourism_data['Year']
    
    # Define the width of each bar
    bar_width = 0.35
    
    # Calculate the positions for bars
    x = np.arange(len(years))
    
    # Create a figure
    plt.figure(figsize=(10, 6))
    
    # Create the grouped bar chart
    plt.bar(x - bar_width/2, tourism_data['Tourism_Data'], bar_width, label='Tourism', alpha=0.7)
    plt.bar(x + bar_width/2, wage_data['Wage_Data'], bar_width, label='Wages', alpha=0.7)
    
    # Customize the plot labels and title
    plt.xlabel('Year')
    plt.ylabel('Values')
    plt.title('Comparison of Tourism and Wage Data Over the Years')
    
    # Set the x-axis labels to be the years
    plt.xticks(x, years)
    
    # Add a legend
    plt.legend()
    
    # Show the plot
    plt.show()
