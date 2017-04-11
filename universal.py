import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *
from numpy.linalg import inv, qr
from random import normalvariate
import random


arr = np.arange(10)

np.sqrt(arr)

np.exp(arr)

x = randn(8)

y = randn(8)

np.maximum(x, y)

arr = randn(7)*5

np.modf(arr)

points = np.arange(-5, 5, 0.01)

xs, ys = np.meshgrid(points, points)

z = np.sqrt(xs ** 2 + ys ** 2)

plt.imshow(z, cmap=plt.cm.gray);
plt.colorbar()

plt.title("Image plot")

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])

cond = np.array([True, False, True, True, False])

result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]

result = np.where(cond, xarr, yarr)

arr = randn(4, 4)

np.where(arr > 0, 2, -2)

np.where(arr > 0, 2, arr)

result = []

# for i in range(n):
#     if cond1[i] and cond2[i]:
#         result.append(0)
#     elif cond1[i]:
#         result.append(1)
#     elif cond2[i]:
#         result.append(2)
#     else:
#         result.append(3)

#
# np.where(cond1 & cond2, 0,
#     np.where(cond1, 1,
#             np.where(cond2, 2, 3)))

arr = np.random.randn(5, 4)

arr.mean()

np.mean(arr)

arr.sum()

# print(arr)
# print(arr.mean(axis=1))
# array([-3.1003, -1.6189, 1.4044, 4.5712])

arr.sum(0)

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

arr.cumsum(0)
arr.cumprod(1)

arr = randn(100)

(arr > 0).sum()

bools = np.array([False, False, True, False])
bools.any()
bools.all()

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
np.unique(names)

ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])

np.unique(ints)

values = np.array([6, 0, 0, 3, 2, 5, 6])
np.in1d(values, [2, 3, 6])

arr = np.arange(10)
np.save('some_array', arr)

np.load('some_array.npy')

np.savez('array_archive.npz', a=arr, b=arr)

arhc = np.load('array_archive.npz')

arhc['b']

x = np.array([[1., 2., 3.], [4., 5., 6.]])

y = np.array([[6., 23.], [-1, 7], [8, 9]])

X = randn(5, 5)

mat = X.T.dot(X)

inv(mat)

# print(mat.dot(inv(mat)))

q, r = qr(mat)

# print(r)

samples = np.random.normal(size=(4, 4))

position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

nsteps = 1000
draws  = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk  = steps.cumsum()

# print(walk.min())
# print(walk.max())

# print((np.abs(walk) >= 10).argmax())

nwalks = 5000
nsteps = 1000

draws = np.random.randint(0, 2, size=(nwalks, nsteps))
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)

# print(walks.max())
# print(walks.min())

hits30 = (np.abs(walks) >= 30).any(1)
print(hits30.sum())


























