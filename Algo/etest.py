from sklearn.model_selection import train_test_split

X = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10]]
y = [1,2,3,4,5,6,7,8,9,10]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, shuffle = False)

print(X)
print(X_train)
print(X_test)

print(y)
print(y_train)
print(y_test)

# print(10*0.33)

# print('y[:2]')
# print(y[:2])

# print('y[2:]')
# print(y[2:])