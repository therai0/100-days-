""" Python provides a vast collection of libraries and packages that are open source and can be used in your projects or development work. In this lecture, we will discuss an overview of some important standard libraries in Python. """

import array # importing array module


# create array

arr = array.array('f',[1.4,45.5,6.78,9])
print(arr[0]) # 1.399999976158142
#  here f for floating number

arr.append(10)
print(arr) # array('f', [1.399999976158142, 45.5, 6.78000020980835, 9.0, 10.0])

# so in this array lib we can perform multiple operation like append,insert,remove etc
