import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

df = pd.read_csv("Tips.csv")

print(df.head())
print(df.info())

plt.figure()
sns.barplot(x='day', y='total_bill', data=df)
plt.title("Average Total Bill by Day")
plt.show()

plt.figure()
sns.histplot(df['total_bill'], kde=True)
plt.title("Total Bill Distribution")
plt.show()

sns.jointplot(x='total_bill', y='tip', data=df, kind='scatter')
plt.show()

sns.pairplot(df[['total_bill', 'tip', 'size']])
plt.show()

plt.figure()
sns.stripplot(x='day', y='tip', data=df)
plt.title("Tips by Day (Stripplot)")
plt.show()

plt.figure()
sns.swarmplot(x='day', y='total_bill', data=df)
plt.title("Total Bill Swarm Plot")
plt.show()

plt.figure()
sns.boxplot(x='day', y='total_bill', data=df)
plt.title("Total Bill Boxplot")
plt.show()

plt.figure()
sns.countplot(x='day', data=df)
plt.title("Count of Days")
plt.show()

plt.figure()
sns.pointplot(x='day', y='tip', data=df)
plt.title("Average Tip by Day")
plt.show()

sns.lmplot(x='total_bill', y='tip', data=df)
plt.title("Total Bill vs Tip Regression")
plt.show()