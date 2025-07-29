
def print_num(n):
    for i in range(n):
        return i**3

print(print_num(5)) # output: 0

# whene the value is 0 and 0**3=0 return value 0 stop the loop because function already return

"""
A generator function is a special type of function that returns an iterator object. Instead of using return to send back a single value, generator functions use yield to produce a series of results over time. This allows the function to generate values and pause its execution after each yield, maintaining its state between iterations.
"""

def print_square(n):
    for i in range(n):
        yield i**2  #for generator we use yield key word

# print(print_square(1)) # output: <generator object print_square at 0x1008729b0>

for i in print_square(5):
    print(i)

# output:
# 0
# 1
# 4
# 9
# 16





"""
Generators are particularly useful for reading large files because they allow processing one line at a time without loading the entire file into memory. This efficient approach helps manage memory usage when dealing with large datasets.
"""


def read_file(path):
    with open(f"{path}",'r') as file:
        for line in file:
            yield line


for i in read_file("/Volumes/Demo/100 days/day_10/demo.txt"):
    print(i)
# it will print the all file data line by line


