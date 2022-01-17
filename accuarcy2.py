import pandas as pd



path_file = 'CetteFoisCLaBonne.csv'
# data_Matrix = np.genfromtxt(path_file, delimiter=',')
df_full = pd.read_csv(path_file, delimiter=',')


df_reel = df_full.loc[:,['diffElo', 'diffSent', 'yreel']]

df_pred_train = df_full.loc[:34,['diffElo', 'diffSent', 'ypred']]

df_pred_test = df_full.loc[34:,['diffElo', 'diffSent', 'ypred']]

print(len(df_pred_train))
print(len(df_pred_test))

good_pred_nb_te = 0

for k in range(len(df_pred_test)) :
    # print(df_pred_test.iat[k,2])
    # print(df_full.iat[33+k,2])

    if df_pred_test.iat[k,2] == df_full.iat[k,2] : 
        good_pred_nb_te+=1 

print('accuarcy test : ')
print(good_pred_nb_te/len(df_pred_test))

    
good_pred_nb_tr = 0

for k in range(len(df_pred_train)) :
    # print(df_pred_test.iat[k,2])
    # print(df_full.iat[33+k,2])

    if df_pred_train.iat[k,2] == df_full.iat[k,2] : 
        good_pred_nb_tr+=1 

print('accuarcy train : ')
print(good_pred_nb_tr/len(df_pred_train))
