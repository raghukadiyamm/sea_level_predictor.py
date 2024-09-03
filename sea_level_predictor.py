import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series([i for i in range(1880, 2051)])
    plt.plot(years_extended, intercept + slope * years_extended, 'r', label='Best fit line 1')

    # Create second line of best fit (from year 2000)
    recent_df = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    
    # Generate years from 2000 to 2050 for the second line of best fit
    years_recent = pd.Series([i for i in range(2000, 2051)])
    plt.plot(years_recent, intercept2 + slope2 * years_recent, 'green', label='Best fit line 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
