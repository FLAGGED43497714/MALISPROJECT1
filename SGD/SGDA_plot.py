from numpy import NaN, dtype
from sklearn.linear_model import SGDClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sqlalchemy import false, null
from sympy import frac
from matplotlib import pyplot as plt
import numpy as np

path_import_sh = 'shuf.csv'


dfclean = pd.read_csv(path_import_sh, delimiter=',')

dfclean = dfclean.dropna()

X = dfclean.loc[:,['diffElo', 'diffSent']]
y = dfclean.loc[:,['Result']]


y = y.values.ravel()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, shuffle = False)

maxIter = 100

print('X_train')
print(X_train.iat([0,0])

Votes_train = [[[0,0,0] for k in range(30)] for j in range(30)] 


fig, ax = plt.subplots()
colorstrain = {1:'green', 2:'grey', 3:'red'}

for _ in range(maxIter) : 

    my_SGD = SGDClassifier(max_iter=50)
    my_SGD.fit(X_train, y_train)

    coord = [[[10*column - 150, 150 - 10*row] for column in range(30)] for row in range(30)]

    for k in range(30) :
        for j in range(30) :
            print([coord[k][j][0]],[coord[k][j][1]])
            pred = my_SGD.predict([coord[k][j][0]],[coord[k][j][1]])

            if pred[0] == 1 :
                Votes_train[k][j][0]+=1
            if pred[0] == 2 :
                Votes_train[k][j][1]+=1
            if pred[0] == 3 :
                Votes_train[k][j][2]+=1

for k in range(30):
    for j in range(30):
            
        if max(Votes_train[k][j][0],Votes_train[k][j][1],Votes_train[k][j][2]) == Votes_train[k][j][0] :
            assRes = 1
        if max(Votes_train[k][j][0],Votes_train[k][j][1],Votes_train[k][j][2]) == Votes_train[k][j][1] :
            assRes = 2
        if max(Votes_train[k][j][0],Votes_train[k][j][1],Votes_train[k][j][2]) == Votes_train[k][j][2] :
            assRes = 3


        plt.scatter(x = coord[k][j][0],y=coord[k][j][0],color=colorstrain[assRes], s=50)

plt.show()

