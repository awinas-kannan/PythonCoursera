import numpy as np


a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
print(a[0])
anp = np.array(a)
print(anp[0])
print(anp[0][1])
print(anp[0, 1])
print(anp[0:2, 0:2])
print(anp.shape)
print(anp.size)
print(anp.ndim)

print("**********")
x = np.array([[1, 1], [2, 2]])
y = np.array([[3, 3], [4, 4]])
print(x + y)
print(2 * x)
print(2 * y)
print(x * y)
print(x.dot(y))

a = np.array([0, 1])
b = np.array([1, 0])
print(np.dot(a, b))

X = np.array([[1, 0], [0, 1]])
Y = np.array([[0, 1], [1, 0]])
print(X + Y)

X = np.array([[1, 0, 1], [2, 2, 2]])
print(X[0:2, 2])

X = np.array([[1, 0], [0, 1]])
Y = np.array([[2, 2], [2, 2]])
print(np.dot(X, Y))






a= np.array([1,0,1,0,1])
b= np.array([0,1,0,1,0])
print(a*b)
