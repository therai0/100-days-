
""" Recursion function in python """

"""
A recursive function is a function that calls itself in order to solve a problem
"""

def recur(n):
    if n == 0:
        return 0
    print(n)
    return recur(n-1)

print(recur(10))
#output: 10 9 8 7 6 5 4 3 2 1


# factorial with recursion
def facto(n):
    if n == 1:
        return 1
    return n * facto(n-1)

print(facto(5))  #output: 120




