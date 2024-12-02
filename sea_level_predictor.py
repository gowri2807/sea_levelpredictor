import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read the data from the CSV file
    df = pd.read_csv("epa-sea-level.csv")
    
    # Extract the year and sea level data
    years = df['Year']
    sea_levels = df['CSIRO Adjusted Sea Level']

    # Create the scatter plot
    plt.scatter(years, sea_levels, label='Original Data')

    # Perform linear regression on the entire dataset
    res_all = linregress(years, sea_levels)
    x_all = range(1880, 2051)
    y_all = res_all.slope * x_all + res_all.intercept
    plt.plot(x_all, y_all, color='red', label='Best Fit Line (1880-2050)')

    # Perform linear regression on data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = range(2000, 2051)
    y_recent = res_recent.slope * x_recent + res_recent.intercept
    plt.plot(x_recent, y_recent, color='green', label='Best Fit Line (2000-2050)')

    # Add labels, title, and legend
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    # Save the plot and return
    plt.savefig('sea_level_plot.png')
    return plt.gca()
