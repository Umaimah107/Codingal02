import pandas as pd
import matplotlib.pyplot as plt

countries_df = pd.read_csv('countries.csv')
countries = countries_df
countries.head(3)
#print(countries)

c_52 = countries.loc[countries['year'] == 1952]
c_52.head()
#print(c_52)

c_07 = countries.loc[countries['year']== 2007]
c_07.head()
#print(c_07)

type(c_52)

c_merge = c_52.merge(c_07, left_on='country', right_on='country')
c_merge.head()
#print(c_merge)

c_merge.drop(['year_x', 'year_y'],axis=1)
c_merge.head()
#print(c_merge)

c_merge['population_growth'] = c_merge['population_y'] -c_merge['population_x']
c_merge.head()
#print(c_merge)

31889923 - 8425333

c_merge.shape, type(c_merge)

c_merge = c_merge.sort_values('population_growth', ascending=False).head(10)
c_merge.head(10)
print(c_merge)

names = ['China', 'india', 'United States', 'Indonesia', 'brazil', 'Pakistan', 'Bangladesh', 'nigeria', 'mexico', 'phillippines']
pop_grow = (c_merge['population_growth'] / 10**6)

plt.figure(figsize=(15,9))
plt.bar(names, pop_grow, width=0.6)
plt.xlabel('country')
plt.ylabel('Population Growth( millions)')
plt.title('Top 10 countries with the biggest population growth from 1952 to 2007')
plt.xticks(rotation=45)

for x,y in zip(names, pop_grow):
    label = "({:.2f})".format(y)

    plt.annotate(label,(x,y),textcoords='offset points',xytext=(0,10),ha='center')

plt.show()