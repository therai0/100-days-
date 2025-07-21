""".List is the inbuilt data structure """



# creating a list
users = ["Bhaskar","Manish","Aayush","Bishal"]

# accessing the element of the list

print(users[0]) # Bhaskar


""" Basic method of the list """

users.append("Messi") # this method will add the element at the end of list


users.insert(0,"Ronaldo") #it will insert or add the element at the particular place

users.remove("Messi") #it will remove the first occurance of Messi

"""
example
players = ["Messi","Ronaldo","Messi"]
players.remove("Messi") #it remove the first occurance of Messi
print(users) #["Ronaldo","Messi"]

#so in this example there is multiple apperence of Messi and we run the remove() method also
#it just remove the initial Messi not all
# this method just remove the first occurance 
"""


# creating new list
nums = [12,3,54,90,56]

nums.pop() #this method remove the list element of the nums list

nums.clear() #remove all the element of the list
# print(nums)
#output: []



# creating new list
heros = ["Bhaskar","Messi","Messi","Ronaldo","Neymar jr"]

print(heros.index("Messi")) #it will return the index of first occurance of Messi

print(heros.count("Messi")) # number of times particular element appears in list


# creating new list
lst = [12,34,5,56,7]
lst.sort() # sort the element at ascending order
print(lst)

lst.sort(reverse=True) # sort the list at descending order
print(lst)


# method to copy the list
cpy_list = lst.copy() #copying list
print(cpy_list)

# use case of copying list

x = [1,2,3,4]
y = x 

y.pop()
print(x)


