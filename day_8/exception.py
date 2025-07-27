
"""
Exception handling in Python allows for graceful management of errors and enables corrective actions without stopping the execution of the program.
"""


# how to use the try catch

try:
    print(10/0)
except:
    print("there is error in the given code")
# we can't divide the number by 0
# it will print the output: there is error in the given code


""" Different types of exception """
""" NameError """
# Raised when a variable is not defined.

try:
    a = b
    # here we didn't define the varaible b 
except NameError as e:
    print(e) #output: name 'b' is not defined






""" TypeError """
# Raised when an operation is applied to an object of inappropriate type.

try:
    a = "10"
    b = 10
    print(a+b) # we can't perform the add operation here so it will throw the exception
except TypeError as e:
    print(e) #output: can only concatenate str (not "int") to str


""" IndexError """
# Raised when trying to access an invalid index in a list/tuple/etc.

try: 
    lst = ["apple"]
    print(lst[1])
except IndexError as e:
    print(e) #output: list index out of range


""" KeyError """
# Raised when trying to access a non-existing key in a dictionary.
try:
    dit = {
        "username":"Bhaskar",
        "password":"123345"
    }
    print(dit["email"]) #we are trying to access the email which is not aviable in dit
except KeyError as e:
    print(e) #output: email 


""" AttributeError """

try:
    a = "x"
    a.append("hello")
    # so we can't append in a 
except AttributeError as e:
    print(e) #output: 'str' object has no attribute 'append'



""" FileNotFoundError """
try:
    with open("apple.txt",'r') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e) #[Errno 2] No such file or directory: 'apple.txt'



""" Else keyword in exception handling """

try:
    num = int(input("Enter the number ? "))
    print(100/num)
    # if num = 0 it should through the error
except ZeroDivisionError as e:
    print(e)
else:
    print("No error")

# output
# 8.333333333333334
# No error



""" Finally keyword """

# The finally block in Python is used to define clean-up actions that must be executed no matter what—whether an exception was raised or not.


try:
    with open("mango.txt",'r') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
finally:
    print("Exception completed")

# output:
# [Errno 2] No such file or directory: 'mango.txt'
# Exception completed