import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.lines import Line2D
import numpy as np
import re

files = ['ASSE_RC Lens_ASSE15_01_2022.txt']
hourOfMatch = 13


def justName(file):
    str = ''
    n = len(file)
    i = 0
    while i < n and not(file[i].isnumeric()):
        str+=file[i]
        i+=1
    return str

def hour(i):
    if i<12:
        return str(i) +'am'
    else:
        return str(i) + 'pm'

X = [hour(i) for i in range(24)]
Y = [0 for i in range(24)]

res = 0
#then we have a text file for sure
f = open(file, "r")
lines = f.readlines()
for line in lines:
    if re.match('created at', line):
        hour = 10*int(line[24]) + int(line[25])
        Y[hour] += 1
        res += 1


X = np.array(X)
Y = np.array(Y)

varY = sum((Y - (sum(Y)/Y.shape[0])*np.ones(Y.shape[0]))**2)
Z = (Y - (sum(Y)/Y.shape[0])*np.ones(Y.shape[0]))/np.sqrt(varY)


plt.bar(X,Y, color = cm.jet(Z))
plt.xticks(rotation=40, fontsize=10)
plt.ylabel('Number of Tweets')
plt.title('Number of Tweets per Hour for the match :'+justName(file))
plt.axvline(x=hourOfMatch, color = 'r', linestyle='--', label='Hour of Match')

lines = [Line2D([0], [0], color='red', linewidth=1, linestyle='--')]
labels = ['Hour of Match']
plt.legend(lines, labels)

plt.show()

