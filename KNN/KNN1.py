from numpy import NaN, dtype
from sklearn import neighbors
from sklearn.impute import KNNImputer
from sklearn.linear_model import SGDClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.utils import shuffle
from sqlalchemy import false, null
from sympy import frac
from matplotlib import pyplot as plt
import numpy as np

# Can't do both, intentionnal repetition.
imported = True
# created_on_the_fly = False

# # For 'created on the fly' mode 
# path_file = 'fichier_test3.csv'
# path_out_sh = 'shuf.csv'
# path_out_sh_diff = 'shufDif.csv'

# For 'imported' mode 
path_import_sh = 'odds_shuf9.csv'

path_out_sh_pred = 'KNN/resultsKNNneig1.csv'
# path_out_sh_pred_prob = 'KNN/probasKNN.csv'

# path_out_final = 'KNN/resultsANDprobs'





if imported :
    dfclean = pd.read_csv(path_import_sh, delimiter=',')

    dfclean = dfclean.dropna()

    X = dfclean.loc[:,[ 'diffElo','diffSent']]#,'diffSent'
    y = dfclean.loc[:,['Result']]

    y = y.values.ravel()


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, shuffle = False)

    my_KNN = KNeighborsClassifier(n_neighbors=3)
    my_KNN.fit(X_train, y_train)


    y_tr_pred = my_KNN.predict(X_train)
    # y_tr_pred_prob = my_KNN.predict_proba(X_train)

    y_te_pred = my_KNN.predict(X_test)
    # y_te_pred_prob = my_KNN.predict_proba(X_test)


    y_total_pred = np.append(y_tr_pred,[y_te_pred])

    df_total_pred = pd.DataFrame(y_total_pred)
    df_total_pred.to_csv(path_out_sh_pred,index=False,header=False)

    
    nb_goodPredTr = 0

    for k in range(len(y_tr_pred)) :
        if y_tr_pred[k] == y[k] : 
            nb_goodPredTr+=1 


    nb_goodPredTe = 0

    for k in range(len(y_te_pred)) :
        if y_te_pred[k] == y[34+k] : 
            nb_goodPredTe+=1 

    accuarcy_train = nb_goodPredTr/(len(y_tr_pred))
    accuarcy_test = nb_goodPredTe/(len(y_te_pred))




    print('Accuarcy train = '+str(accuarcy_train))
    print('Accuarcy test = '+str(accuarcy_test))
