import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Test.csv')
print(df)

sns.barplot(x='weather_type', y='air_pollution_index', data=df)
plt.show()

sns.histplot(df['temperature'], kde=True)
plt.show()

sns.jointplot(x='temperature', y='humidity', data=df, kind='scatter')
plt.show()

sns.pairplot(df[['temperature', 'humidity', 'air_pollution_index']])
plt.show()

sns.stripplot(x='weather_type', y='temperature', data=df)
plt.show()

sns.swarmplot(x='weather_type', y='temperature', data=df)
plt.show()

sns.boxplot(x='weather_type', y='humidity', data=df)
plt.show()

sns.countplot(x='weather_type', data=df)
plt.show()

sns.pointplot(x='weather_type', y='temperature', data=df)
plt.show()

sns.lmplot(x='temperature', y='air_pollution_index', data=df)
plt.show()

