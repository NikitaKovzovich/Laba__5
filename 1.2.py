import numpy as np

X = np.zeros((12,3))
X[:, 0] = 1
X[:, 1] = np.random.randint(11,23,(1,12))
X[:, 2] = np.random.randint(60,82,(1,12))

Y = np.zeros((12,1))
Y[:, 0] = np.random.uniform(13.5,18.6,(1,12))

print("Исходные значения Y:")
for i in range(12):
    print(f"y{i + 1} = {Y[i][0]}")


A = np.linalg.inv(X.transpose() @ X) @ (X.transpose() @ Y)

Y = X @ A

print("____________________________")
print("Полученные значения Y:")
for i in range(12):
    print(f"y{i + 1} = {Y[i][0]}")