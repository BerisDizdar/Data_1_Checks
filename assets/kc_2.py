# Louisville Weather Data for 2022

# Import Python packages
import pandas as pd
import numpy as np  
import datetime 
from matplotlib import pyplot as plt  

# Create DataFrame (df) 
df_Louisville = pd.read_csv('assets/Louisville_Weather_CSV.csv')

print(df_Louisville.head()) # Display the first five rows from the data.

# DateTime
df_Louisville['DATE'] = pd.to_datetime(df_Louisville['DATE'])   # Datetime module used to manipulate data using the 'DATE' column.

Louisville_monthly_mean = df_Louisville.groupby(df_Louisville.DATE.dt.month)[['TMAX', 'TAVG', 'TMIN']].mean()   # The mean() function calculates the average of the 'TMAX' 'TMIN' and 'TAVG' columns for each month.

print(round(Louisville_monthly_mean, 2))    # The 'round' function rounds the data, in this case it was set to allow two decimal points.

# Graph data
plt.plot(Louisville_monthly_mean, 'o')  
plt.xlabel('Month')
plt.ylabel('Temperature (Fahrenheit)') 
plt.title(' 2022 Mean Monthly Temperature Highs, Lows, and Averages, for Louisville KY')
plt.legend(Louisville_monthly_mean) 

print(plt.show())   # Graph displays the monthly mean high, low, and average temperature for Louisville Ky, for the year 2022.
