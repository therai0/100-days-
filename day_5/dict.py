"""
A dictionary in Python is an unordered, mutable collection of key-value pairs. Each key in a dictionary is unique, and is used to access its corresponding value
"""


# creating dictionary

emt_dict = {}
print(type(emt_dict)) #<class 'dict'>

# another way to create the dict
emt = dict()
print(emt) #{}
print(type(emt)) #<class 'dict'>



# accesing the element
std = {
    "firstname":"Ayush",
    "last":"Rai",
    "age":22,
    "rollno":21,
    "class":10
}

# now we need to access the element of dict

# basic method
print(std["firstname"]) #Ayush

# with get method
print(std.get("firstname")) #Ayush


# dict is mutable so we can delete, update,add the new element 
# so add the new element in dict
std["address"] = "Mechinagar-3"

print(std) 
#{'firstname': 'Ayush', 'last': 'Rai', 'age': 22, 'rollno': 21, 'class': 10, 'address': 'Mechinagar-3'}

# update the element of the dict
std["class"] = 9
print(std) 
#{'firstname': 'Ayush', 'last': 'Rai', 'age': 22, 'rollno': 21, 'class': 9, 'address': 'Mechinagar-3'}

# deleting the element of dict
# we can use to del keyword

del std["age"]

print(std)
#{'firstname': 'Ayush', 'last': 'Rai', 'rollno': 21, 'class': 9, 'address': 'Mechinagar-3'}


""" Other's method """

keys = std.keys()
print(keys) # dict_keys(['firstname', 'last', 'rollno', 'class', 'address'])

values = std.values()
print(values) # dict_values(['Ayush', 'Rai', 21, 9, 'Mechinagar-3'])

# get the all items in key value pair
itms = std.items()
print(itms) # dict_items([('firstname', 'Ayush'), ('last', 'Rai'), ('rollno', 21), ('class', 9), ('address', 'Mechinagar-3')])


# shallow copy 
# why we need this

user = {
    "username":"bhaskar123",
    "password":"123456",
    "email":"raibhaskar@gmail.com",
    "age":20,
    "gender":"male"
}

# let's do what if we don't copy

demo_user = user
print(user)
print(demo_user)

# {'username': 'bhaskar123', 'password': '123456', 'email': 'raibhaskar@gmail.com', 'age': 20, 'gender': 'male'}

# {'username': 'bhaskar123', 'password': '123456', 'email': 'raibhaskar@gmail.com', 'age': 20, 'gender': 'male'}

# both print same value

# what if we update the value of user elements

user["password"] = "mynameiskhan"

print(user)
print(demo_user)

# {'username': 'bhaskar123', 'password': 'mynameiskhan', 'email': 'raibhaskar@gmail.com', 'age': 20, 'gender': 'male'}
# {'username': 'bhaskar123', 'password': 'mynameiskhan', 'email': 'raibhaskar@gmail.com', 'age': 20, 'gender': 'male'}

# here you can see that in both password value is change 

# so avoid this we need to make the shallow copy


new_users = user.copy()

user["password"] = "apple" #updating the value of password

print(user)
print(new_users)

# {'username': 'bhaskar123', 'password': 'apple', 'email': 'raibhaskar@gmail.com', 'age': 20, 'gender': 'male'}

# {'username': 'bhaskar123', 'password': 'mynameiskhan', 'email': 'raibhaskar@gmail.com', 'age': 20, 'gender': 'male'}

# here in this output there is some changes 
# in users varaible password is updated but not in new_users

for x in user.keys():
    print(user.get(f"{x}"))

# bhaskar123
# apple
# raibhaskar@gmail.com
# 20
# male


# nested dictionary

typ_users = {
 "admin":{
     "username":"Bhaskar",
     "password":"123456"
 },
 "users":{
     "username":"Ayush",
     "password":"000000"
 }
}

print(typ_users)
# {'admin': {'username': 'Bhaskar', 'password': '123456'}, 'users': {'username': 'Ayush', 'password': '000000'}}


# dictonary comphrehension

dict_cmp = {x:x**2 for x in range(10)}
print(dict_cmp)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}



# mergin dictionary
first = {"barnd":"Apple","value":"2B"}
second = {"barnd":"B&B","value":"100M"}
