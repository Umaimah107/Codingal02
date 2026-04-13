#import matplotlib.pyplot as plt

#Year = [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
#Unemployment_Rate = [9.8, 12, 8, 7.2, 6.9, 7,  6.5,6.2, 5.5, 6.3]

#plt.plot(Year, Unemployment_Rate, color='red', marker='o')
#plt.title('Unemployment Rate Vs Year', fontsize=14)
#plt.xlabel('Year', fontsize=14)
#plt.ylabel('Unemployment Rate', fontsize=14)
#plt.grid(True)
#plt.show()

import matplotlib.pyplot as plt
import numpy as np

x= np.array([1,2,3,4])
y=x*2

plt.plot(x, y)

x1 = [2,4,6,8]
y1 = [3,5,7,9]

plt.plot(x, y1, '-.')

plt.xlabel('X axis data')
plt.ylabel("Y axis data")
plt.title('multiple plots')
plt.fill_between(x, y, y1, color='green', alpha=0.5)
plt.show()