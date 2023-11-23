import numpy as np
import matplotlib.pyplot as mpl

list = [11, 22, 33, 44, 5, 66, 5, 55]
np_ar = np.array(list)
print(np_ar.shape)
print(np_ar.ndim)
print(type(np_ar))
print(np_ar.dtype)
# np.info()
print(np_ar.size)

np_ar[0] = 100
np_ar[1:3] = 66, 77
print(np_ar)

# Vector addition
u = np.array([0, 1])
v = np.array([1, 0])
z = u + v

print('vector addition', z)
print('vector sub', u - v)
print(type(z))

# Without Numpy

z = []
for i, j in zip(u, v):
    print(i, j)
    z.append(i + j)

print(z)
print(type(z))

print("****  Vector Multiplication ****")

m = np.array([1, 2])
v_m = 3 * m
print(v_m)

n = np.array([3, 3])
o = np.array([4, 6])
v_m = n * o
print(v_m)

v_d = n.dot(o)
print(v_d)

# Univ Functions
print("****** Universal Functions ******")
b = np.array([1, 4, 3 - 2])
print(b.mean())
print(b.sum())
print(b.max())

print(np.pi)

pi_np_ar = np.array([2, 2 / np.pi, np.pi])
print(pi_np_ar)
print(np.sin(pi_np_ar))
line_arr = np.linspace(-2, 2, 11)
print(line_arr)
print(np.linspace(1, 10, 21))

print("********** matplotlib ***********")

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
print(y)
mpl.plot(x, y)
mpl.show()
mpl.savefig('myfig.png')
