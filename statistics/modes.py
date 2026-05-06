import statistics as stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("Test.csv")

mean_pollution = stats.mean(df['air_pollution_index'])
print("Mean value of Air Pollution Index - ", mean_pollution)

median_age = stats.median(df['air_pollution_index'])
print("Median value of Air Pollution Index - ", median_age)

median_humidity = stats.median(df['humidity'])
print("Median value of Humidity - ", median_humidity)

mode_pollution = stats.mode(df['air_pollution_index'])
print("Mode value of Air Pollution Index - ", mode_pollution)

mode_weather = stats.mode(df['weather_type'])
print("Mode of Feature Weather Type - ", mode_weather)