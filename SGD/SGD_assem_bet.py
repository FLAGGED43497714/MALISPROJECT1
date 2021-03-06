from numpy import NaN, dtype
from sklearn.linear_model import SGDClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sqlalchemy import false, null
from sympy import frac
from matplotlib import pyplot as plt
import numpy as np
from NN_draw import Neural_Network


path_import_sh_odds = 'odds_shuf10.csv'

home_Odds = pd.read_csv(path_import_sh_odds, delimiter=',').loc[:,['HomeWinOdds']]
draw_Odds = pd.read_csv(path_import_sh_odds, delimiter=',').loc[:,['DrawOdds']]
away_Odds = pd.read_csv(path_import_sh_odds, delimiter=',').loc[:,['AwayWinOdds']]



dfclean = pd.read_csv(path_import_sh_odds, delimiter=',')

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

p_home_tr = [0 for _ in range(len(X_train))]
p_home_te = [0 for _ in range(len(X_test))]
p_draw_tr = [0 for _ in range(len(X_train))]
p_draw_te = [0 for _ in range(len(X_test))]
p_away_tr = [0 for _ in range(len(X_train))]
p_away_te = [0 for _ in range(len(X_test))]



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
    p_home_tr[k] = Votes_train[k][0]/100
    p_draw_tr[k] = Votes_train[k][1]/100
    p_away_tr[k] = Votes_train[k][2]/100


for k in range(len(y_te_pred)) :
    if max(Votes_test[k][0],Votes_test[k][1],Votes_test[k][2]) == Votes_test[k][0] :
        y_te_assembly[k] = 1
    if max(Votes_test[k][0],Votes_test[k][1],Votes_test[k][2]) == Votes_test[k][1] :
        y_te_assembly[k] = 2
    if max(Votes_test[k][0],Votes_test[k][1],Votes_test[k][2]) == Votes_test[k][2] :
        y_te_assembly[k] = 3
    p_home_te[k] = Votes_test[k][0]/100
    p_draw_te[k] = Votes_test[k][1]/100
    p_away_te[k] = Votes_test[k][2]/100




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






#########################################################################################

path_import_W1 = 'SGD/NNImport\W1_test8.dat'
path_import_W2 = 'SGD/NNImport\W2_test8.dat'

difElo = X.loc[:,['diffElo']]

maxdelta = 400.90837938

NN = Neural_Network()
NN.set(from_W1=path_import_W1, from_W2=path_import_W2)




capital = [100 for _ in range(len(y_te_assembly)+1)]

def bet(C, K, p) :
    if K == 0 :
        return 0
    if K*p < 1 :
        return 0
    f = p - (1 - p) / ( K - 1 )
    if f < 0 : 
        print('negative bet !')
    return C*f

bets = [0 for k in range(len(y_te_assembly))]
odds_array = [0 for k in range(len(y_te_assembly))]
realResult = [0 for k in range(len(y_te_assembly))]

for k in range(len(y_te_assembly)) :

    # delta_Elo = difElo.iat[34+k,0]
    # draw_percentage = NN.forward([delta_Elo/maxdelta, 1])[0]
    # home_percentage = (1.0 / (1.0 + pow(10, ((-delta_Elo) / 400)))) * (1-draw_percentage)
    # away_percentage = (1.0 / (1.0 + pow(10, ((delta_Elo) / 400)))) * (1-draw_percentage)

    home_percentage = p_home_te[k]
    draw_percentage = p_draw_te[k]
    away_percentage = p_away_te[k]

    prediction = y_te_assembly[k] 

    if prediction == 1 :
        odds = home_Odds.iat[34+k,0]
        p = home_percentage
        # print('step'+str(k)+'odd for '+str(prediction)+' = '+str(odds))
    if prediction == 2 :
        odds = draw_Odds.iat[34+k,0]
        p = draw_percentage
        # print('step'+str(k)+'odd for '+str(prediction)+' = '+str(odds))
    if prediction == 3 :
        odds = away_Odds.iat[34+k,0]
        p = away_percentage
        # print('step'+str(k)+'odd for '+str(prediction)+' = '+str(odds))


    
    odds_array[k]=odds

    actual_Capital = capital[k]

    theBet = bet(C=actual_Capital,K=odds,p=p)
    bets[k] = theBet 

    
    capital[k+1] = capital[k] - theBet

    if y_te_assembly[k] == y[34+k] : 
        capital[k+1] = capital[k+1] + theBet * odds 
    realResult[k] = y[34+k]
    
print(capital[-1])
# df = pd.DataFrame(capital)
# df.to_csv('test1.csv',header=False,index=False)
# df = pd.DataFrame(bets)
# df.to_csv('test2.csv',header=False,index=False)
# df = pd.DataFrame(y_te_assembly)
# df.to_csv('test3.csv',header=False,index=False)
# df = pd.DataFrame(odds_array)
# df.to_csv('test4.csv',header=False,index=False)
# df = pd.DataFrame(realResult)
# df.to_csv('test5.csv',header=False,index=False)

# plt.plot(capital)
# plt.show()