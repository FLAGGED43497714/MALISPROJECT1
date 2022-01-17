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


Votes_train = [[0,0,0] for _ in range(len(X_train))]  
Votes_test = [[0,0,0] for _ in range(len(X_test))]  

y_tr_assembly = [0 for _ in range(len(X_train))]
y_te_assembly = [0 for _ in range(len(X_test))]


for _ in range(maxIter) : 

    my_SGD = SGDClassifier(max_iter=50)
    my_SGD.fit(X_train, y_train)


    y_tr_pred = my_SGD.predict(X_train)
    y_te_pred = my_SGD.predict(X_test)

    for k in range(len(y_tr_pred)) :
        if y_tr_pred[k] == 1 :
            Votes_train[k][0]+=1
        if y_tr_pred[k] == 2 :
            Votes_train[k][1]+=1
        if y_tr_pred[k] == 3 :
            Votes_train[k][2]+=1

    for k in range(len(y_te_pred)) :
        if y_te_pred[k] == 1 :
            Votes_test[k][0]+=1
        if y_te_pred[k] == 2 :
            Votes_test[k][1]+=1
        if y_te_pred[k] == 3 :
            Votes_test[k][2]+=1

for k in range(len(y_tr_pred)) :
    if max(Votes_train[k][0],Votes_train[k][1],Votes_train[k][2]) == Votes_train[k][0] :
        y_tr_assembly[k] = 1
    if max(Votes_train[k][0],Votes_train[k][1],Votes_train[k][2]) == Votes_train[k][1] :
        y_tr_assembly[k] = 2
    if max(Votes_train[k][0],Votes_train[k][1],Votes_train[k][2]) == Votes_train[k][2] :
        y_tr_assembly[k] = 3


for k in range(len(y_te_pred)) :
    if max(Votes_test[k][0],Votes_test[k][1],Votes_test[k][2]) == Votes_test[k][0] :
        y_te_assembly[k] = 1
    if max(Votes_test[k][0],Votes_test[k][1],Votes_test[k][2]) == Votes_test[k][1] :
        y_te_assembly[k] = 2
    if max(Votes_test[k][0],Votes_test[k][1],Votes_test[k][2]) == Votes_test[k][2] :
        y_te_assembly[k] = 3




nb_goodPredTr = 0

for k in range(len(y_tr_assembly)) :
    if y_tr_assembly[k] == y[k] : 
        nb_goodPredTr+=1 


nb_goodPredTe = 0

for k in range(len(y_te_assembly)) :
    if y_te_assembly[k] == y[34+k] : 
        nb_goodPredTe+=1 

accuarcy_train = nb_goodPredTr/len(y_tr_assembly)
accuarcy_test = nb_goodPredTe/len(y_te_assembly)




print('Accuarcy train = '+str(accuarcy_train))
print('Accuarcy test = '+str(accuarcy_test))