import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.plot(xpoints, ypoints, 'o')
plt.show()

xpoints1 = np.array([1, 2, 6, 8])
ypoints1 = np.array([3,8, 1, 10])

plt.plot(xpoints1, ypoints1)
plt.show()

ypoints2 = np.array([3, 8, 1, 10])
plt.plot(ypoints2, marker='o', ms=20, mec='r', linestyle = 'dotted',color='r')
plt.show()