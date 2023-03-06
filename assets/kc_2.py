# Louisville Weather Data for 2022

# Import Python packages
import pandas as pd
import numpy as np  
import datetime 
from matplotlib import pyplot as plt  

# Create DataFrame (df) 
df_Louisville = pd.read_csv('assets/Louisville_Weather_CSV.csv')

print(df_Louisville.head()) 

# DateTime
df_Louisville['DATE'] = pd.to_datetime(df_Louisville['DATE'])

Louisville_monthly_mean = df_Louisville.groupby(df_Louisville.DATE.dt.month)[['TMAX', 'TAVG', 'TMIN']].mean() 

print(round(Louisville_monthly_mean, 2)) 

# Graph data
plt.plot(Louisville_monthly_mean, 'o')  
plt.xlabel('Month')
plt.ylabel('Temperature in Fahrenheit') 
plt.title('Monthly Temperature Highs, Lows, and Averages, for Louisville KY')
plt.legend(Louisville_monthly_mean) 

print(plt.show())  
