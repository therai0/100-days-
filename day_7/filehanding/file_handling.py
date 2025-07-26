""" 
File handling in Python is the process of working with files—such as reading from or writing to them—using built-in functions and methods.
"""

import os 
print(os.getcwd())

# creating or wrting the file
with open('/Volumes/Demo/100 days/day_7/filehanding/example.txt','w') as file:
    file.write("Hello world\n")

# so this code will create the file and example.txt in path : /Volumes/Demo/100 days/day_7/filehanding/ and write the "Hello world"

# we need to read the this file
with open('/Volumes/Demo/100 days/day_7/filehanding/example.txt','r') as file:
    print(file.read())
    #output: Hello world

# let's append the some text in this files

with open('/Volumes/Demo/100 days/day_7/filehanding/example.txt','a') as file:
    file.write("My name is khan \n") #\n breaking the line
    file.write("Who are you ?\n")
    file.write("Are you Messi? \n")







# reading the file line by line
with open('/Volumes/Demo/100 days/day_7/filehanding/example.txt','r') as file:
   for line in file:
       print(line)

# output:
# Hello world
# My name is khan 
# Who are you ?
# Are you Messi?

# creating another file and write multiple lines 
with open('/Volumes/Demo/100 days/day_7/filehanding/demo.txt','w') as file:
    file.writelines("Assignment-1\n assignment-2\n assignment-3\n")

  
# reading this demo.txt file 
with open('/Volumes/Demo/100 days/day_7/filehanding/demo.txt','r') as file:
    for x in file:
        print(x)
# output:
# Assignment-1
#  assignment-2
#  assignment-3






# Counting Lines, Words, and Characters in a File
with open('/Volumes/Demo/100 days/day_7/filehanding/example.txt','r') as file:
    content = file.readlines()
    num_lines = len(content)
    words = sum((len(line.split()) for line in content))
    letters = sum(len(line) for line in content)

    print(f"Number of lines:{num_lines}\n Number of words:{words}\n Number of letters:{letters}")
    
# Number of lines:4
#  Number of words:13
#  Number of letters:59

