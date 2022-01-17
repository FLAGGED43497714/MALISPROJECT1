import pandas as pd

path_shuf = 'shuf.csv'
# path_pred = 'KNN/resultsKNN.csv'
# path_pred = 'KNN/resultsKNNneig1.csv'
# path_pred = 'SGD/resultsSGD.csv'
path_pred = 'RandomForest/resultsRF.csv'
# path_pred = 'NeuralNet/results.csv'

df_shuf = pd.read_csv(path_shuf,delimiter=',')

df_reel = df_shuf.loc[:,['Result']]

df_pred_train = pd.read_csv(path_pred,header=None).loc[:33,]

# print('df_pred_train')
# print(df_pred_train)

df_pred_test = pd.read_csv(path_pred).loc[33:,]

nb_goodPredTr = 0

for k in range(len(df_pred_train)) :
    if df_pred_train.iat[k,0] == df_reel.iat[k,0] : 
        nb_goodPredTr+=1 


nb_goodPredTe = 0

for k in range(len(df_pred_test)) :
    if df_pred_test.iat[k,0] == df_reel.iat[34+k,0] : 
        nb_goodPredTe+=1 

print('Accuarcy train = '+str(nb_goodPredTr/len(df_pred_train)))
print('Accuarcy test = '+str(nb_goodPredTe/len(df_pred_test)))