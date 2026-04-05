import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(sns.get_dataset_names())

df = pd.read_csv('Tips.csv')


print(df.head(10))

print(df.shape)

print(df.tail())

print(df.isnull().sum())

print(df.describe())

print(df.dtypes)

print(df.info())

print(df.describe(include='all'))

print(df.corr(numeric_only= True))

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

df.select_dtypes(include=[np.number]).hist(figsize=(12,8))
plt.show()

df.select_dtypes(include=[np.number]).plot(kind='box', subplots=True, layout=(3,2), sharex=False, sharey=False, figsize=(8,12))
plt.show()

print(df.gender.value_counts())
print(df.smoker.value_counts())
print(df.day.value_counts())

sns.countplot(data=df, x='gender')
plt.show()

sns.countplot(data=df, x='smoker')
plt.show()

sns.countplot(data=df, x='day')
plt.show()

sns.countplot(data=df, x='gender', hue='smoker')
plt.show()

sns.countplot(data=df, x='gender', hue='day')
plt.show()

sns.countplot(data=df, x='smoker', hue='day')
plt.show()

sns.pairplot(data=df, hue='smoker')
plt.show()