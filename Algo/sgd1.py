from sklearn.linear_model import SGDClassifier
import pandas as pd
from sqlalchemy import null
from sympy import frac
from matplotlib import pyplot as plt

# Can't do both, intentionnal repetition.
imported = True
created_on_the_fly = False

# For 'created on the fly' mode 
path_file = 'fichier_test3.csv'
path_out_sh = 'super_clean_shuffled.csv'
path_out_std = 'super_clean.csv'

# For 'imported' mode 
path_import_std = 'super_clean.csv'
path_import_shuffled = 'super_clean_shuffled.csv'



if created_on_the_fly : 

    # data_Matrix = np.genfromtxt(path_file, delimiter=',')
    df_full = pd.read_csv(path_file, delimiter=',')

    df_notPPN = df_full[df_full['Result']!=4]
    df_notPPN = df_notPPN[df_full['Result']!=5]
    df_notPPN = df_notPPN[df_notPPN['Result']!=null]
    df_notPPN = df_notPPN[df_notPPN['Result']!=34]

    df_selected = df_notPPN.loc[:,['HomeAvgPolarity', 'HomeElo', 'AwayAvgPolarity', 'AwayElo', 'Result']]

    df_selected['diffElo'] = df_selected.HomeElo- df_selected.AwayElo
    df_selected['diffSent'] = 1000 * (df_selected.HomeAvgPolarity- df_selected.AwayAvgPolarity)

    df_diff = df_selected.loc[:,['diffElo', 'diffSent', 'Result']]

    shuffled_Data = df_diff.sample(frac=1)

    shuffled_Data.to_csv(path_out_sh, index=False)
    df_diff.to_csv(path_out_std, index = False)



if imported :
    clean_sh = pd.read_csv(path_import_shuffled, delimiter=',')
    clean = pd.read_csv(path_import_std, delimiter=',')

    X_train = clean_sh.loc[:,['diffElo', 'diffSent']]
    Y_train = clean_sh.loc[:,['Result']]
    df_diff = df_selected.loc[:,['diffElo', 'diffSent', 'Result']]
