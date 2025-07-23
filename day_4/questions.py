
# Create a set with the first 10 positive integers. Print the set.

new_st = set(x for x in range(10))
print(new_st) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(type(new_st)) # <class 'set'>


# Add the number 11 to the set created in Assignment 1. Then remove the number 1 from the set. Print the modified set

new_st.add(11) #adding new element
print(new_st) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11}

new_st.remove(1) #removing the elements form the sets
print(new_st) #{0, 2, 3, 4, 5, 6, 7, 8, 9, 11}

# Create two sets: one with the first 5 positive integers and another with the first 5 even integers. Perform and print the results of union, intersection, difference, and symmetric difference operations on these sets.

st_one = set(x for x in range(5))  # {0,1,2,3,4}
st_two = set(x for x in range(10) if x%2 == 0) # {0,2,4,6,8}

# union
print(st_one.union(st_two)) #output: {0, 1, 2, 3, 4, 6, 8}

# intersection
print(st_one.intersection(st_two)) #output: {0, 2, 4}

# difference
print(st_one.difference(st_two)) #output: {1, 3}


# symmetric difference
print(st_one.symmetric_difference(st_two)) #output: {1, 3, 6, 8}


# Create a new set containing the squares of the first 10 positive integers using a set comprehension. Print the new set.


# 
sq_set = set(x**2 for x in range(10)) 
print(sq_set) # output:{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}






# Create a new set containing only the even numbers from the set created in Assignment 1 using a set comprehension. Print the new set.

new_even_set = set(x for x in new_st if x % 2 == 0) # new_st is the set which is created at the top 
print(new_even_set) # {0, 2, 4, 6, 8}


# Create two sets: one with the first 5 positive integers and another with the first 3 positive integers. Check if the second set is a subset of the first set and if the first set is a superset of the second set. Print the results.

first_set = set(x for x in range(5)) #{0,1,2,3,4}
second_set = set(x for x in range(3)) # {0,1,2}

# checking if second set is subset of first or not
if  second_set.issubset(first_set):
    print("Yes second set is subset of first set")
else:
    print("No second set is not subset of first set")

# checking if first set is super set of second set or not
if first_set.issuperset(second_set):
    print("Yes first set is super set of second set")
else:
    print("No first is not superset of second set")






#Create a frozenset with the first 5 positive integers. Print the frozense

fr_set = frozenset(x for x in range(5))
print(fr_set) #frozenset({0, 1, 2, 3, 4})
print(type(fr_set)) #<class 'frozenset'>


# Create a set with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a set. Print the resulting set.

first_int = set(a for a in range(5))
print(first_int) #output: {0, 1, 2, 3, 4}

# converting into list to add the new element
lst = list(first_int)

lst.append(6)
print(lst) # output:[0, 1, 2, 3, 4, 6]

update_sets = set(lst)
print(update_sets) #output: {0, 1, 2, 3, 4, 6}



# Create a set and iterate over the elements, printing each element.

pt_sets = {1,2,3,4,5}
for x in pt_sets:
    print(x,end=" ") #end=" " helps to print the all the value in single line
# output :1 2 3 4 5 
print() #just to break the line


# Create a set and remove elements from it until it is empty. Print the set after each removal.

rm_set = {1,2,3,4,5,6}
while rm_set:
    rm_set.pop()
    print(rm_set)
#output: 
# {2, 3, 4, 5, 6}
# {3, 4, 5, 6}
# {4, 5, 6}
# {5, 6}
# {6}
# set()


# Create two sets and update the first set with the symmetric difference of the two sets. Print the modified first set.

one  = {1,2,3,4,5}
two = {4,5,6,7,8}

one.symmetric_difference_update(two)
print(one) #{1, 2, 3, 6, 7, 8}


# Create a set containing tuples, where each tuple contains two elements. Print the set.
tp_sets = {(1,2),(3,4),(5,6)}
for x in tp_sets:
    print(x)

# output: 
# (1, 2) (3, 4)(5, 6)
# 







