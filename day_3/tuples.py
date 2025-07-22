
"""
Tuples are one of the built-in data structures in Python, and they are used to store multiple items in a single variable. Tuples are similar to lists, but they are immutable, meaning once a tuple is created, its contents cannot be changed (no addition, removal, or updating of elements).

tuples can contain duplicate value
"""

tpls = (12,34,5,65,12)

# accessing element of tuples
print(tpls[0])


""" Basic methods of tupels """

print(tpls.count(12)) #this method use to count the number of times that particular 
# element appear in tuples

print(tpls.index(12)) #return the first index of element


# slicing tuples 
new_t = tpls[0:2] #it doesn't include the list index
print(new_t)

# tuples packing and unpacking

# this is know as packing
student = ("Bhaskar",21,"BIT")


# unpacking this 
name,age,department = student
print(name,age,department)


# in some case we can use the * to address the remain element

# this is the process of packing 
st_nt = ("Bhaskar",21,"BIT","react js","Django","flask","node js")

# now we need to unpack this 
st_name,st_age,st_department,*st_skills = st_nt
print(st_skills) #it will return the list of remain element of tuples cuz we use the * in begning of the variable 


# looping in tuples 
for x in tpls:
    print(x)

# printing length
print(len(tpls))



# concat tuples and repeat multiple times

tp = (12,34,45)
tp2 = (34,56,7)

new_tp = tp + tp2 #concatenation of two tuples 
print(new_tp)

# repeating tuples 
rp_tp = tp*2 #it will create the new tuples by multiplying the orginal tuples doulble time 
print(rp_tp) #(12, 34, 45, 12, 34, 45)


# check the element belong to partular tuples for not

x = (12,34,45,67,78,89)
print(34 in x) # true because 34 belongs to x
print(100 in x) #false because here 100 doesn't belongs to x


# there are different inbuilt function(method) which helps to find the max,min,sum of tuples

y = (1,2,3,4,5,6)

print(max(y))
print(min(y))
print(sum(y))
# we can implement this function in list also


# nested tuples 

ntp = ((12,34),(45,67),(6,90))
print(ntp[0])


# passing multiple elements and accessing as a tuples 

def demo(*arg):
    print(type(arg)) #it will print the tuples 

demo(12,34,45)

"""
ntp[0] = 22 # we can't perform because tuples if immutable
ntp.append(123123 # we can't perform because tuples if immutable
"""

lst = [12,34,45,56]

# coversion of list into tuples 
tp_new = tuple(lst)
print(type(tp_new))



# enumerate() method in tuples loops

t = ("Apple","banana","pineapple","carrot")

for index,value in enumerate(t):
    print(index,value)

# enumerate method convert the tupes into pairs like:
# 0 Apple
# 1 banana
# 2 pineapple
# 3 carrot
# note it is applicable for list also
# this is we need to track the position of element in tuples