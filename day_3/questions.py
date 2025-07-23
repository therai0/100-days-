# let's solve the different question related to tuples 


# Create a tuple with the first 10 positive integers. Print the tuple.

tup = tuple(x for x in range(0,10)) #creating the tuples 

for x in tup:
    print(x ,end=" ")

print() #breaking the line

# Print the first, middle, and last elements of the tuple created in Assignment 1.
print(tup[0]) #first
print(tup[-1]) #last element
print(tup[len(tup)//2]) #middle element


# Print the first three elements, the last three elements, and the elements from index 2 to 5 of the tuple created in Assignment 1.

print(tup[0:3]) #priting first 3 element
print(tup[-3:]) #printing last 3 element
print(tup[2:5]) # printing element from 2 to 5


# Create a nested tuple representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.

t = ((1,2,3),(4,5,6),(7,8,9))
for x in t:
    for y in x:
        print(y,end=" ")
    print()

# printing the element at second row and thrid column

for x in range(len(t)):
    for y in range(len(t)):
        if x == 1 and y == 2:
            print(t[x][y])
            break


# Concatenate two tuples: (1, 2, 3) and (4, 5, 6). Print the resulting tuple.

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t2 + t1
print(t3)


# Create a tuple with duplicate elements and count the occurrences of an element. Find the index of the first occurrence of an element in the tuple.

tp = (12,34,65,7,78,12,45,76,12)

print(tp.count(12)) #print the number of times 12 occure in tuples
print(tp.index(12)) # print it index where first time it occure










# Create a tuple with 5 elements and unpack it into 5 variables. Print the variables.

# packing
users = ("bhaskar" ,"rai",21,"male","9800000000")

# unpacking
firstname,lastname,age,gender,contact = users
print(firstname,lastname,age,gender,contact)


# Convert a list of the first 5 positive integers to a tuple. Print the tuple.
lst = [x for x in range(5)]

# list to tuple 
new_t = tuple(lst) #converting list in tuples
print(new_t)
print(type(new_t))


# Create a tuple with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a tuple. Print the resulting tuple.


tpl = tuple(x for x in range(5))

print(type(tpl))
tpl_to_lst = list(tpl)
tpl_to_lst.append(100) #appending new element after converting into list

print(tpl_to_lst)



# again covert the list into tuple
new_tpl = tuple(tpl_to_lst)
print(type(new_tpl))


# Create a tuple with the characters of a string. Join the tuple elements into a single string. Print the string.

str_tpl = ('b','h','a','s','k','a','r')

username = ''.join(str_tpl)
print(username)


# Create a dictionary with tuple keys and integer values. Print the dictionary.

dtn = {
    ("username"):"Bhaskar",
    ("password"):"123456",
    ("age"):21
}

print(dtn)



# Create a tuple with duplicate elements. Convert it to a set to remove duplicates and print the resulting set.

tpl = (12,34,54,67,768,12)
print(set(tpl)) # set is the inbuilt data structre which does not store the duplicate elements


# Write functions that take a tuple and return the minimum, maximum, and sum of the elements. Print the results for a sample tuple.

def get_tp(*tp):
    return (min(tp),max(tp),sum(tp))

ans = get_tp(1,2,3,4)
print(ans)
print(type(ans))