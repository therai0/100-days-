# pyright: ignore[reportMissingImports]
import numpy as np 

print(np.__version__) # version of numpy


# creating array in numpy

""" 
Although the array may look like a list, it is actually a NumPy ndarray
"""

arr = np.array([1,2,3,4,5])
print(arr) # output: [1 2 3 4 5]
print(type(arr)) #output: <class 'numpy.ndarray'>

# arr.shape give the dimension of the array
print(arr.shape) #output:(5,) 

arr2 = np.array([[1,2],[4,5],[7,8]])
print(arr2.shape)
# output:(3, 2) it means 3 row 2 column


# reshaping the arr
"""
arr.reshape(3,3)
print(arr)

this code will trow the error:

The general rule for reshaping the array is 
arr.reshape(x,y)
x * y == len(array)
the new row and column product is equal to total element of array

arr  have 5 element but we try to reshape(3,3) where 3 * 3 is 9
so it doesn't match it will throw the error
"""

arr.reshape(5,1)
print(arr.ndim)
print(arr.shape)


