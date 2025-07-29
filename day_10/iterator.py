"""
Iterators are an advanced Python concept that allows for efficient looping and memory management. Iterators provide a way to access elements of a collection sequentially without exposing the underlying structure.
"""

lst = [1,2,3,4,5,6]

# using iter method to create the iterator
iterator = iter(lst)
# print(type(iterator)) # output: <class 'list_iterator'>

print(next(iterator)) # 1
print(next(iterator)) # 2
print(next(iterator)) # 3
print(next(iterator)) # 4
print(next(iterator)) # 5
print(next(iterator)) # 6


users = ["Bhaskar","bishal","aayush","Manish"]
itr = iter(users)

while True:
    try:
        print(next(itr))
    except StopIteration:
        break
# output:
# Bhaskar
# bishal
# aayush
# Manish