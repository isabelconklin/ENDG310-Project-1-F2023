import matplotlib.pyplot as plt
# Prompt used in ChatGPT: I would like to create a pie chart showing the amount of people entering canada seasonally, I have some code from an old project which I would like to use as a base, could you help me do this?
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
    plt.savefig('Images/seasons_piechart.png')
    plt.show()

