# if else in python

a =  10

# check if the number a is greater then 20 or not
if a > 20:
    print("Yes")
else:
    print("Noo")

# it will print no because a is not greater then 20



# Take the input from the user and check the number is odd or even and grater then 100

num = int(input("Enter the any number "))

if num > 100:
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Number is not valid")

# this is the simple example of nested if else

"""
Nested if else:
if there is the another if else condition inside the if or else condition then 
it is know as nested if else
"""


""" Loop """


""" For Loop """

for x in range(0,5):
    print(x)
# output 1,2,3,4,5

# another example
a = "apple"
for y in a:
    print(y)
# it will print all the character of apple




""" while loop """

n = 10
while n >= 0:
    print("Hello world")
    n -= 1

# this is the simple example of while loop

""" break ,continue keyword"""

# break
# break keyword use to break the loop if the condition meet
username = "Bhaskar"

for x in username:
    if x == 'a':
        print("Stop here")
        break
    print(x)


for x in range(10,200):
    if x == 170:
        continue
    print(x)
# if x == 170 it does not print the value 170


""" nested loop """

for x in range(5):
    for y in range(x):
        print("X",end=" ")
    print("")

#  output
"""
x
xx
xxx
xxxx
"""