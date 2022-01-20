from ast import Num
from os import path
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import matplotlib.colors as colors
import matplotlib.cm as cmx
from sqlalchemy import null

path_file = 'fichier_test3.csv'
# data_Matrix = np.genfromtxt(path_file, delimiter=',')
df_full = pd.read_csv(path_file, delimiter=',')

df_notPPN = df_full[df_full['Result']!=4]
df_notPPN = df_notPPN[df_notPPN['Result']!=null]
df_notPPN = df_notPPN[df_notPPN['Result']!=34]

df_selected = df_notPPN.loc[:,['HomeAvgPolarity', 'HomeElo', 'AwayAvgPolarity', 'AwayElo','Result' ]]

df_selected['diffElo'] = df_selected.HomeElo- df_selected.AwayElo
df_selected['diffSent'] = 1000 * (df_selected.HomeAvgPolarity- df_selected.AwayAvgPolarity)

df_diff = df_selected.loc[:,['diffElo', 'diffSent', 'Result']]

print(df_diff)

fig, ax = plt.subplots()

colors = {1:'green', 2:'grey', 3:'red', 5:'yellow'}

# x = [10 *k - 300 for k in range(60)]
# moins_x = [-element for element in x]
# plt.plot(x,moins_x)

grouped = df_diff.groupby('Result')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='diffElo', y='diffSent', label=key, color=colors[key])

plt.show()


# # plt.scatter(df_diff['diffElo'],df_diff['diffSent'])
# print(df_diff)