from unicodedata import decimal
from numpy import NaN, dtype
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.utils import shuffle
from sqlalchemy import false, null
from sympy import frac
from matplotlib import pyplot as plt
import numpy as np


# Can't do both, intentionnal repetition.
imported = True
# created_on_the_fly = True

# # For 'created on the fly' mode 
# path_file = 'fichier_test3.csv'
# path_out_sh = 'shuf.csv'
# path_out_sh_diff = 'shufDif.csv'

# For 'imported' mode 
# path_import_std = 'super_clean.csv'
path_import_sh = 'shuf.csv'


path_out_sh_pred = 'NeuralNet/results.csv'
path_out_sh_pred_prob = 'NeuralNet/probas.csv'



# if created_on_the_fly : 

#     # data_Matrix = np.genfromtxt(path_file, delimiter=',')
#     df_full = pd.read_csv(path_file, delimiter=',')

#     df_notPPN = df_full[df_full['Result']!=4]
#     df_notPPN = df_notPPN[df_full['Result']!=5]
#     df_notPPN = df_notPPN[df_notPPN['Result']!=null]
#     df_notPPN = df_notPPN[df_notPPN['Result']!=34]

#     df_selected = df_notPPN.loc[:,['Hometeam', 'AwayTeam', 'HomeAvgPolarity', 'HomeElo', 'AwayAvgPolarity', 'AwayElo', 'Result']]

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

    my_SGD = MLPClassifier(hidden_layer_sizes=3)
    my_SGD.fit(X_train, y_train)


    y_tr_pred = my_SGD.predict(X_train)
    # y_tr_pred_prob = my_SGD.predict_proba(X_train)

    y_te_pred = my_SGD.predict(X_test)
    # y_te_pred_prob = my_SGD.predict_proba(X_test)



    # print(type(y_te_pred))

    y_total_pred = np.append(y_tr_pred,[y_te_pred])
    # y_total_pred_prob = np.append(y_tr_pred_prob,[y_te_pred_prob])

    df_total_pred = pd.DataFrame(y_total_pred)
    df_total_pred.to_csv(path_out_sh_pred,index=False,header=False)


    # df_total_pred_prob = pd.DataFrame(y_total_pred_prob)
    # df_total_pred_prob.to_csv(path_out_sh_pred_prob,index=False,header=False)


