#from matplotlib import pyplot as plt
#import numpy as np

#a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
#fig, ax = plt.subplots(figsize = (10, 7))
#ax.hist(a, bins = [0, 25, 50, 75, 100])
#plt.show()

#example1
#import matplotlib.pyplot as plt
#import numpy as np
#from matplotlib import colors
#\from matplotlib.ticker import PercentFormatter

#np.random.seed(23685752)
#N_points = 10000
#n_bins = 20

#x = np.random.randn(N_points)
#y = .8 ** x + np.random.randn(10000) + 25

#fig, axs = plt.subplots(1,1,figsize=(10,7), tight_layout = True)
#axs.hist(x, bins=n_bins)
#plt.show()

#example 2
#import matplotlib.pyplot as plt

#data = [12, 15, 14, 10, 18, 20, 22, 19, 17, 16, 15, 14, 13, 21, 23]

#plt.hist(data, bins=5)
#plt.xlabel("Values")
#plt.ylabel("Frequency")
#plt.title("Histogram of Data")

#plt.show()

#example 3

#import numpy as np
#import matplotlib.pyplot as plt

#data = np.random.randn(1000)

#plt.hist(data, bins=20)
#plt.title("Histogram of Normally Distributed Data")
#plt.xlabel("Values")
#plt.ylabel("Frequency")
#plt.show()

#example 4
import matplotlib.pyplot as plt
data = [5,7,8,9,10, 12, 15, 18, 20, 22]
plt.hist(data, bins=5, color = "skyblue", edgecolor="black")
plt.title("Styled histogram")
plt.show()