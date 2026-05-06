import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv("Titanic Dataset.csv")
data.head(5)
print(data)
data.dtypes
print(data)
data.isnull().sum()
print(data)