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
path_import_sh = 'shuf.csv'

path_out_sh_pred = 'KNN/resultsKNNneig1.csv'
# path_out_sh_pred_prob = 'KNN/probasKNN.csv'

# path_out_final = 'KNN/resultsANDprobs'



# if created_on_the_fly : 

#     # data_Matrix = np.genfromtxt(path_file, delimiter=',')
#     df_full = pd.read_csv(path_file, delimiter=',')

#     df_full = df_full.dropna()

#     df_notPPN = df_full[df_full['Result']!=4]
#     df_notPPN = df_notPPN[df_full['Result']!=5]
#     df_notPPN = df_notPPN[df_notPPN['Result']!=null]
#     df_notPPN = df_notPPN[df_notPPN['Result']!=34]

#     df_selected = df_notPPN.loc[:,['HomeTeam', 'AwayTeam', 'HomeAvgPolarity', 'HomeElo', 'AwayAvgPolarity', 'AwayElo', 'Result']]

#     df_selected['diffElo'] = df_selected.HomeElo- df_selected.AwayElo
#     df_selected['diffSent'] = 1000 * (df_selected.HomeAvgPolarity- df_selected.AwayAvgPolarity)

#     shuffled_Data = df_selected.sample(frac=1)

#     shuffled_Data.to_csv(path_out_sh, index=False)


#     df_diff_sh = shuffled_Data.loc[:,['diffElo', 'diffSent', 'Result']]

#     df_diff_sh.to_csv(path_out_sh_diff, index = False)



if imported :
    dfclean = pd.read_csv(path_import_sh, delimiter=',')

    dfclean = dfclean.dropna()

    X = dfclean.loc[:,['diffElo', 'diffSent']]
    y = dfclean.loc[:,['Result']]


    # path_tmp_X = 'X.csv'
    # path_tmp_y = 'tempy.csv'

    # X.to_csv(path_tmp_X, header=False, index=False)
    # y.to_csv(path_tmp_y, header=False, index=False)
    
    # X = pd.read_csv(path_tmp_X,header=None)
    # y = pd.read_csv(path_tmp_y,header=None)

    y = y.values.ravel()

    # print(X)
    # print(y)

    
    #random_state : state is random but controllable with an int

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, shuffle = False)

    my_KNN = KNeighborsClassifier(n_neighbors=1)
    my_KNN.fit(X_train, y_train)


    y_tr_pred = my_KNN.predict(X_train)
    # y_tr_pred_prob = my_KNN.predict_proba(X_train)

    y_te_pred = my_KNN.predict(X_test)
    # y_te_pred_prob = my_KNN.predict_proba(X_test)


    y_total_pred = np.append(y_tr_pred,[y_te_pred])

    df_total_pred = pd.DataFrame(y_total_pred)
    df_total_pred.to_csv(path_out_sh_pred,index=False,header=False)


    fig, ax = plt.subplots()
    colorstrain = {1:'green', 2:'grey', 3:'red'}

    for k in range(30) :
        for j in range(30) :
            coord = [[10*k - 150, 150 - 10*j]]
            pred = my_KNN.predict(coord)
            plt.scatter(x = coord[0][0],y=coord[0][1],color=colorstrain[pred[0]], s=50)

    plt.show()
