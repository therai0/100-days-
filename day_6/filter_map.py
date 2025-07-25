""" Map function """

""" 
The map() function lets you apply a function to every item in an iterable (like a list, tuple, etc.) without writing a loop.
"""

lst = [ 1,2,3,4,5,6]
def suqare(n):
    return n**2

new_squar_list = list(map(suqare,lst)) 

print(new_squar_list)
#output: [1, 4, 9, 16, 25, 36]

# use the inbuit method to convert the string into number
str_num = ['1','2','3','4'] #this are the list of character
print(type(str_num[0])) #<class 'str'>

# so we can apply the map function and convert the datatype into integer

int_num = list(map(int,str_num))
print(int_num) #[1, 2, 3, 4]
print(type(int_num[0])) # <class 'int'>








""" Filter function """

"""
The filter() function lets you select only the elements that satisfy a condition (i.e., where a function returns True).
"""


# filter the all the odd number from the list
num_lst  = [x for x in range(1,10)]
# now we need to filter the all the odd number so
def filter_odd(n):
    if n % 2 != 0:
        return n
odd_list = list(filter(filter_odd,num_lst))
print(odd_list) #output: [1, 3, 5, 7, 9]

# as the argument of the filter function we can pass the lamda function also
even_list = list(filter(lambda x: x % 2 == 0,num_lst))
print(even_list) # output: [2, 4, 6, 8]


# filter method in list of dictionaries

users = [
    {"username":"bhaskar","is_verified":True,},
    {"username":"ayush","is_verified":False,},
    {"username":"Mansih","is_verified":False,},
    {"username":"Deepak","is_verified":True,},
    {"username":"Kiran","is_verified":True,},
]

def filter_user(user):
    return user["is_verified"] == True

# filter the all the varifed users from the list of dictionaries
verified_users = list(filter(filter_user,users))
print(verified_users)
# ouptut: [
# {'username': 'bhaskar', 'is_verified': True},
#  {'username': 'Deepak', 'is_verified': True},
#  {'username': 'Kiran', 'is_verified': True}
# ]