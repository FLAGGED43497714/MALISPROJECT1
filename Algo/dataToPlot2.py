from ast import Num
from os import path
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import matplotlib.colors as colors
import matplotlib.cm as cmx
from sqlalchemy import null

path_file = 'CetteFoisCLaBonne.csv'
# data_Matrix = np.genfromtxt(path_file, delimiter=',')
df_full = pd.read_csv(path_file, delimiter=',')


df_reel = df_full.loc[:,['diffElo', 'diffSent', 'yreel']]

df_pred_train = df_full.loc[34:,['diffElo', 'diffSent', 'ypred']]
df_pred_test = df_full.loc[:18,['diffElo', 'diffSent', 'ypred']]

fig, ax = plt.subplots()

colorsreal = {1:'lime', 2:'lightgray', 3:'salmon'}



grouped = df_reel.groupby('yreel')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='diffElo', y='diffSent', s=20, label=key, color=colorsreal[key])

plt.show()

fig, ax = plt.subplots()
colorstrain = {1:'forestgreen', 2:'grey', 3:'coral'}


grouped = df_pred_train.groupby('ypred')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='diffElo', y='diffSent', s=20, label=key, color=colorstrain[key])

plt.show()

colorstest = {1:'darkgreen', 2:'black', 3:'red'}
fig, ax = plt.subplots()

grouped = df_pred_test.groupby('ypred')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='diffElo', y='diffSent', s=20,label=key, color=colorstest[key])

plt.show()



# # plt.scatter(df_diff['diffElo'],df_diff['diffSent'])
# print(df_diff)