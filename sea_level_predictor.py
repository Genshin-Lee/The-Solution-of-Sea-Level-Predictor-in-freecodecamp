import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df =  pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    plt.scatter(x = df["Year"],y = df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    slope,intercept, r_value, p_value, std_err = linregress(x = df["Year"],y = df["CSIRO Adjusted Sea Level"])
    x_val = pd.Series(range(min(df["Year"]),2051,1))
    y_val = slope*x_val + intercept
    plt.plot(x_val,y_val,color = "green")
    # Create second line of best fit
    slope,intercept, r_value, p_value, std_err = linregress(x = df[df["Year"] >= 2000]["Year"],y = df[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"])
    x_val = pd.Series(range(2000,2051,1))
    y_val = slope*x_val + intercept
    plt.plot(x_val,y_val,color = "red")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()