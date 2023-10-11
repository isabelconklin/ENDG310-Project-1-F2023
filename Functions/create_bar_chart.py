import numpy as np
import matplotlib.pyplot as plt
# Prompt used in ChatGPT:  I would like to make a bar chart. I would like to y axis to be the number of people and the x axis to be the year. The years I have are 2018-2023. How would I do this?
def create_bar_chart(data_by_year):
    """
    Create a bar chart with the number of people on the y-axis and years on the x-axis.

    Parameters:
        data_by_year (dict): A dictionary where keys are years, and values are arrays/DataFrames
                            containing the data for each year.

    Returns:
        None (displays the chart).
    """

    # Calculate the total amount of people entering Canada each year
    years = list(data_by_year.keys())
    total_people = [np.sum(data / 1e6) for data in data_by_year.values()]

    # Create the figure
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.bar(years, total_people)

    # Label and show the graph
    plt.xlabel('Year')
    plt.ylabel('Number of Tourists (millions)')
    plt.title('Number of People Entering Canada by Year (2018-2023)')
    plt.show()
