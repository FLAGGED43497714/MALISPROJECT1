import os
import re
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def justName(file):
    str = ''
    n = len(file)
    i = 0
    while i < n and not(file[i].isnumeric()):
        str+=file[i]
        i+=1
    return str

MAX=20
nb = 0
pattern = '.*txt'
X = []
Y = []
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for file in files:
    if re.match(pattern, file) and nb < MAX:
        print(file)
        res = 0
        #then we have a text file for sure
        f = open(file, "r")
        lines = f.readlines()
        for line in lines:
            if re.match('created at', line):
                res += 1
        X.append(justName(file))
        Y.append(res)
        nb+=1

X = np.array(X)
Y = np.array(Y)

varY = sum((Y - (sum(Y)/Y.shape[0])*np.ones(Y.shape[0]))**2)
Z = (Y - (sum(Y)/Y.shape[0])*np.ones(Y.shape[0]))/np.sqrt(varY)


plt.bar(X,Y, color = cm.jet(Z))
plt.xticks(rotation=60, fontsize=7)
plt.ylabel('Number of Tweets')
plt.title('Number of Tweets for each match')
plt.show()

