""" Assignment """


# Create a list of the first 20 positive integers. Print the list.
x = [z+1 for z in range(20)] # create the list from 1 to 20

for a in x:
    print(a , end=" ") #print in single line
# output: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

print()

# Print the first, middle, and last elements of the list created in Assignment 1.  
first = x[0] # accessing firs element from the list
middle = x[len(x)//2] #middle element
last = x[len(x)-1]#last element
print(first,middle,last)


# Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in Assignment 1.

print(x[0:5]) # print first five elements
print(x[-5:]) #printing last five elements
print(x[5:15]) #print element from 5 to 15

# Create a new list containing the squares of the first 10 positive integers using a list comprehension. Print the new list.

sqr_lst = [x**2 for x in range(1,11)]
print(sqr_lst) #output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Create a new list containing only the even numbers from the list created in Assignment 1 using a list comprehension. Print the new list.

even_lst = [ y  for y in x if y % 2 == 0]
print(even_lst) # output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]



# Create the list of random number and sort them in both ascending and desending order
new_lst = [12,3,54,6,67,8,9]

new_lst.sort()
print(new_lst)

new_lst.sort(reverse=True)
print(new_lst)

# Create a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.

mtrx = [[1,2,3],[4,5,6],[7,8,9]]


for x in mtrx:
    for y in x:
        print(y,end=" ")
    print()

# Access and print the element at the second row and third column.
for x in mtrx:
    for y in x:
       if mtrx.index(x) == 1 and x.index(y) == 2:
           print("element",y) #output will be 6
           break


#Create a list of dictionaries where each dictionary represents a student with keys 'name' and 'score'. Sort the list of dictionaries by the 'score' in descending order and print the sorted list.

student_record = [
    {"student_name":"Bhaskar","score":90},
    {"student_name":"Aayush","score":99},
    {"student_name":"Bishal","score":98},
    {"student_name":"Samir","score":97},
]

student_record.sort(key = lambda x:x["score"]) #this will sort the student record in ascending order





# Write a function that takes a 3x3 matrix (nested list) as input and returns its transpose. Print the original and transposed matrices.

mt_list = [[1,2,3],[4,5,6],[7,8,9]]

# transpose the matrix

transpose_matrix = []

for x in range(len(mt_list)):#column
    row = []
    for y in range(len(mt_list)):#rows
        row.append(mt_list[y][x])
    transpose_matrix.append(row)

# print(transpose_matrix)

# to transpose the matrix 
new_transpose = [list(x) for  x in zip(*mt_list)] # this code also helps to transpose the matrix


# Write a function that takes a nested list and flattens it into a single list. Print the original and flattened lists.


demo_lst = [[12,3],[45,7],90]
# convert this types of list into [12,3,45,7,90]

# create the function

def flatted_list(lst):
    new_list = []
    # so we need to move into each element of the list to check that inside the list there is another 
    # list or not

    for x in demo_lst:
        if isinstance(x,list):
            for y in x:
                new_list.append(y)
        else:
            new_list.append(x) # if the element of the list is not list then directly insert them into new list
    return new_list

new_faltted_list = flatted_list(demo_lst)
print(new_faltted_list)



# Create two lists of the same length. Use the `zip` function to combine these lists into a list of tuples and print the result.

list_one = [12,34,56]
list_two = [0,0,0]

new_zip_list = list(zip(list_one,list_two))
print(new_zip_list)
# list:[(12, 0), (34, 0), (56, 0)]