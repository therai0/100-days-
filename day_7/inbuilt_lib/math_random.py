import math
import random 

# math lib provide the different Mathematical functions 

print(math.pi) # output: 3.141592653589793
print(math.sqrt(36)) #output: 6.0
print(math.exp(2)) #output: 7.38905609893065
print(math.floor(7.38905609893065)) #output: 7


# random lib helps to generate the random number

print(random.randint(1,90)) # every time it generate the random number between 1 to 90 (integer)
print(random.uniform(0,1)) # every time it generate the random number between 0 to 1 (floating value)

lst = [ "Bhaskar","Aaysuh","Sandesh","Bishal","Manish","Kiran","Jemish","Samir"]
# from this list we need to choose the two user randomly then we can use the random lib

print(random.choices(lst,k=2)) #every time this function choose the two random name from the list
