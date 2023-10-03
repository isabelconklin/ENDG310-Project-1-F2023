import matplotlib.pyplot as plt

def create_seasonal_pie_chart(data_by_season):
    """
    Create a pie chart showing the distribution of people entering Canada by season.

    Parameters:
        data_by_season (dict): A dictionary where keys are seasons, and values are arrays of data for each season.

    Returns:
        None (displays the pie chart).
    """
    # Calculate the total number of people for each season
    season_totals = {season: data.sum() for season, data in data_by_season.items()}

    # Create a figure and set a different background
    fig = plt.figure()
    fig.patch.set_facecolor('white')

    # Create a pie chart
    labels = list(season_totals.keys())
    sizes = list(season_totals.values())
    colors = ['gold', 'lightblue', 'pink', 'orange']
    explode = (0, 0, 0, 0)  # Explode the 2nd slice (i.e., 'Winter')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Number of People Visiting Canada Seasonally')

    plt.show()

