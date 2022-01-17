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

sum_acc_tr = 0
sum_acc_te = 0

max_acc_tr = 0
max_acc_te = 0

for _ in range(maxIter) : 

    my_SGD = SGDClassifier(max_iter=50)
    my_SGD.fit(X_train, y_train)


    y_tr_pred = my_SGD.predict(X_train)
    y_te_pred = my_SGD.predict(X_test)


    # print('y_tr_pred')
    # print(y_tr_pred)

    nb_goodPredTr = 0

    for k in range(len(y_tr_pred)) :
        if y_tr_pred[k] == y[k] : 
            nb_goodPredTr+=1 


    nb_goodPredTe = 0

    for k in range(len(y_te_pred)) :
        if y_te_pred[k] == y[34+k] : 
            nb_goodPredTe+=1 

    accuarcy_train = nb_goodPredTr/len(y_tr_pred)
    accuarcy_test = nb_goodPredTe/len(y_te_pred)

    sum_acc_tr += accuarcy_train
    sum_acc_te += accuarcy_test

    if accuarcy_train > max_acc_tr : 
        max_acc_tr = accuarcy_train
    if accuarcy_test > max_acc_te : 
        max_acc_te = accuarcy_test


    # print('Accuarcy train = '+str(accuarcy_train))
    # print('Accuarcy test = '+str(accuarcy_test))

avg_acc_tr = sum_acc_tr / 100
avg_acc_te = sum_acc_te / 100

print('Accuarcy train = '+str(avg_acc_tr))
print('Accuarcy test = '+str(avg_acc_te))

print('Acc train = '+str(max_acc_tr))
print('Acc test = '+str(max_acc_te))