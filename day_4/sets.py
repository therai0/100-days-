""" Sets in python """

"""
Sets are inbuilt datatypes as like tuples and list. Sets only store unique element.
In this sets we can perform mathematical sets operation like  union,intersection,difference and symmentric difference
"""


# let's create the set's
st = {34,45,67,12}
print(type(st)) #output:<class 'set'>

print(st) #output:{34, 67, 12, 45}

# print(st[0])
# this code throw the issue because sets cann't is access through index


""" Method of sets """

st.add(1000)
print(st) #output:{34, 67, 1000, 12, 45}


st.clear()
print(st) #output: set()


# create new sets
nst = {1,2,32,343,5}
nst.discard(1)
print(nst) #output:{32, 2, 5, 343}

nst.pop()
print(nst) #output: {2, 5, 343}

nst.remove(343)
print(nst) #output: {2, 5}


""" Mathematical operation with sets """

set_one = {1,2,3,4,5}
set_two = {4,5,6,7,8}

# difference 
print(set_one.difference(set_two)) #output: {1, 2, 3}, these are the element which are aviable in set_one but not in set_two


# intersection
print(set_two.intersection(set_one)) #output: {4, 5}

# intersection update()
set_two.intersection_update(set_one) 
print(set_two) #output: {4, 5}
# we perform this operation in set_two so it only kept the element which are comman between set_one and set_two




# let's create new sets agains

st_one = {1,2,3,4}
st_two = {3,4,5,6}

# union
print("union",st_one.union(st_two)) #output: {1, 2, 3, 4, 5, 6}

# isdisjoint()
print(st_two.isdisjoint(st_two)) # output:false
# if this two sets are disjoint then it return true else false


# symmetric_difference()
print(st_one.symmetric_difference(st_two)) #output:{1, 2, 5, 6}
# it return the all the except common element of two sets


# symmetric_difference_update()
st_one.symmetric_difference_update(st_two)
print(st_one) #output: {1, 2, 5, 6}
# it will update the st_one sets with symmetric elements

