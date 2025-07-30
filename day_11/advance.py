
""" Function copying """

def hello_world():
    print("Hello world")

# assign this function to another varaible

hlo = hello_world

del hello_world #it will delete the hello_world()

try: 
    hello_world()
except NameError as e:
    print(e)
# output: name 'hello_world' is not defined
# so here we try to call the function after deleting it
 
# lets call the hlo varaible
hlo()
# output:Hello world


"""
**** Closures **** 

A closure is a function defined inside another function, which can access variables from the enclosing function's scope.
"""

def hello_world():
    def print_hello():
        print("I am printing hello world here")
    return print_hello()

hello_world()
# output: I am printing hello world here

# accessing varaibles
def check_password(pwd):
    orignal_pwd = "1234"
    def is_correct():
        if pwd == orignal_pwd:
            return True
        return False
    return is_correct()

print(check_password("1234")) #output: True
print(check_password("abcd")) #output: False



"""
**** Decorator ****

Decorators are a powerful and flexible feature in Python that allow you to modify the behavior of a function or class method. They are commonly used to add functionality to functions or methods without modifying the actual code.
"""


def is_verified_users(func):
    def find_users():
        if func:
            print("User is found and varified")
        else:
            print("User is not found")
    return find_users()

# this is syntax of decorators function
@is_verified_users
def verified_users():
    return True #if it return the false then output will be "User is not found"
# output: User is found and varified



# another example
def repeator(n):
    def decorator(func):
        def hello_world():
            for _ in range(n):
                print("Hello world")
            func()
        return hello_world
    return decorator

@repeator(5)
def completed_func():
    print("Function completed")

completed_func()
# output: 
# Hello world
# Hello world
# Hello world
# Hello world
# Hello world
# Function completed


# Write a decorator named `time_it` that measures the execution time of a function. Apply this decorator to a function that calculates the factorial of a number.

import time 

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(f"Total time taken by function to execute:{end-start}")
    return wrapper

@time_it #this is decorator function
def facto(n):
    ft = 1
    for i in range(1,n):
        ft *= i
    print(f"Factorial:{ft}")

facto(5)
# output:
# Factorial:24
# Total time taken by function to execute:3.814697265625e-06



# Write two decorators: `uppercase` that converts the result of a function to uppercase, and `exclaim` that adds an exclamation mark to the result of a function. Apply both decorators to a function that returns a greeting message.


# decorator function one
def uppar_case(func):
    def wrapper(*args,**kwargs):
        print("i am second")
        return func(*args,**kwargs).upper()
    return wrapper

# decorator finction two
def excl_mark(func):
    def wrapper(*args,**kwargs):
        print("i am first")
        return func(*args,**kwargs) + "!"
    return wrapper

@uppar_case
@excl_mark
def hello(name):
    return f"hello {name}"

print(hello("Bhaskar"))
# output: HELLO BHASKAR!




