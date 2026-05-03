import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

HouseDF = pd.read_csv("USA_Housing.csv")
print(HouseDF)

HouseDF.head()
print(HouseDF)

HouseDF.info()

HouseDF.columns

sns.pairplot(HouseDF)
sns.heatmap(HouseDF.corr(), annot=True)
plt.show()