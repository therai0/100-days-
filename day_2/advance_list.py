
""" Here we are learning more advance concept of the list"""

"""
 list Comprehension
A compact way to create lists using a for loop in a single line.
"""
lst = [x for x in range(10)]
print(lst) #output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




""" 3x3 matrix in list """

lst_matrix = [[1,2,3],[4,5,6],[7,8,9]] #this is also known as nested list

for x in lst_matrix:
    for y in x:
        print(y,end=" ")
    print() #to break the line

# output
"""
1 2 3
4 5 6
7 8 9
"""



""" Unpacking list """

x , y = [100,200]
print(y) #output: 200


""" Zip and Unzip the list """

books = ["Science","Math","Nepali","Social","Englis"] #list of the books
price = [400,500,200,350,300]

# zip this two list
new_lst = list(zip(books,price))
print(new_lst)
# output: [('Science', 400), ('Math', 500), ('Nepali', 200), ('Social', 350), ('Englis', 300)]


# unzip
x ,y = zip(*new_lst) #it return the tuples so we manually typecast the tuples to list
print(list(x)) #output: ('Science', 'Math', 'Nepali', 'Social', 'Englis')


""" slicing the list """

m = [12,3,5,6,90,78]
print(m[0:4]) #output: [12, 3, 5, 6]

