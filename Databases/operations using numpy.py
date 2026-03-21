import numpy as np
arr= np.array([1,2,3,4])
print(arr[0])

arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])

arr = np.array([1,2,3,4])
print(arr.dtype)

arr = np.array([[1,2,3,4],
                [5,6,7,8 ]])
print(arr.shape)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)

print(newarr)

arr = np.array([1, 2, 3])
for x in arr:
    print(x)

arr1 = np.array([1 ,2 ,3]) 
arr2 = np.array([4, 5, 6]) 

arr = np.concatenate((arr1, arr2))
print(arr)

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

from numpy import random

x = random.randint(100)
print(x)

a = np.arange(9, dtype=float).reshape(3, 3)
print('First array ')
print(a)
print('\n')

b = np.array([10, 10, 10])
print('Second array ')
print(b)
print('\n')

print('Add the two arrays ')
print(np.add(a, b))
print('\n')

print('Subtract the two arrays ')
print(np.subtract(a, b))
print('\n')

print('Multiply the two arrays ')
print(np.multiply(a, b))
print('\n')

print('Divide the two arrays ')
print(np.divide(a, b))
print('\n')
