import numpy as np
from numpy.random import *
data1 = [1,5,2,4]
arr1 = np.array(data1)
# print(arr1)

data2 = [[1, 4, 5, 6], [3, 8, 10, 12]]
arr2 = np.array(data2)
# print(arr2)
#
# print(arr2.ndim)
# print(arr2.shape)
#
# print(arr1.dtype)
#
# print(np.zeros(10))
# print(np.zeros((3, 7)))
#
# print(np.empty((2, 3, 2)))
#
# print(np.arange(15))

arr1 = np.array([1, 2, 3], dtype=np.float64)

arr2 = np.array([1, 2, 3], dtype=np.int32)

numeric_strings = np.array(['1.25', '-9.6'], dtype=np.string_)

numeric_strings.astype(float)

# print(numeric_strings)

int_array =np.arange(10)

calibers = np.array([.22, .270, .357, .44], dtype=np.float64)

int_array.astype(calibers.dtype)
empty_unit32 = np.empty(8, dtype='u4')

arr = np.array([[1., 2., 3.], [4., 5., 6.]])
# print(arr)
#
# print(arr * arr)
# print(arr - arr)

arr = np.arange(10)
# print(arr[5])
# print(arr[5:8])
# arr[5:8] = 12
# print(arr)

arr_slice = arr[5:8]
arr_slice[1] = 12345
# print(arr)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr2d[:2])

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = randn(7, 4)
# print(names == 'Bob')
# print(data[names == 'Bob', 2:])

mask = (names ==  'Bob') | (names == 'Will')
# print(data[mask])

data[data < 0] = 0
# print(data)

arr = np.empty((8, 4))

for i in range(8):
    arr[i] = i

# print(arr[[4, 3, 0, 6]])

arr = np.arange(32).reshape((8, 4))

print(arr)