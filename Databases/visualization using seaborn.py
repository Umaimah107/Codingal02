import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

df = pd.read_csv('Tips Dataset.csv')

sb.displot(df['gender'], kde=False)

sb.distplot(df['tip'], hist=False)
               
sb.distplot(df['total_bill'])

sb.jointplot(x = 'total_bill', y='tip', data = df)

sb.set_style("ticks")

sb.pairplot(df, hue= 'day', diag_kind = 'kde', kind="scatter", palette="husl")
plt.show()

import numpy as np;np.random.seed(0)
import seaborn as sns; sns.set_theme()
uniform_data = np.random.rand(10, 12)
ax= sns.heatmap(uniform_data)
plt.show()

#the issue was that we didnt write plt.show at the end for the code of the heatmap:)