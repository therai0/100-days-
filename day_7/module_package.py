""" Learn the creating the costume module and package"""
"""
Python is an open-source programming language that includes many packages. These packages contain numerous built-in functions, allowing you to use them without writing code from scratch. Modules and packages help organize and reuse code efficiently.
"""

# importing math module
from math import pi #if we need to import the all the function of particular then we can use the "from math import *"
print(pi) #output: 3.141592653589793




""" A module is simply a .py file containing Python code — functions, classes, variables, etc. """

# now are importing the password module 
import password

userpassword = "mynameiskhan"
# using the custom module check the strenght of the password

print(password.is_password_strong(userpassword)) #output: weak
print(password.is_password_strong("M123!@dgdg")) #output: Strong 


""" A package is a folder/directory that contains one or more modules (and optionally sub-packages). It must have a __init__.py file to be recognized as a package (in older Python versions; newer versions don't strictly require it, but it's still common practice). """




# now importing the  package 
from num_package.numbers import is_prime 
# here all the package,module and function is custom

print(is_prime(99)) #output: Not prime number
print(is_prime(93)) #output: Not prime number
print(is_prime(37)) # output: Prime number