from collections import defaultdict
import json
# create the dictionary and add the new key value 

dtc =  {
    "username":"Bhaskar",
    "password":"123456"
}
print(dtc) #{'username': 'Bhaskar', 'password': '123456'}

# adding the new key value 

dtc["email"] = "bhaskar@gmail.com"

print(dtc) #{'username': 'Bhaskar', 'password': '123456', 'email': 'bhaskar@gmail.com'}


# Iterate over the dictionary created in Assignment 1 and print each key-value pair.
for key,value in dtc.items():
    print(f"{key}:{value}")

# username:Bhaskar
# password:123456
# email:bhaskar@gmail.com



# Create a new dictionary containing the cubes of the first 10 positive integers using a dictionary comprehension. Print the new dictionary.

cube_dtc = {x:x**3 for x in range(10)}
print(cube_dtc) #{0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}

# Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, and another with keys as the next 5 positive integers and values as their squares. Merge these dictionaries into a single dictionary and print it.

first = {x:x**2 for x in range(1,6)}
second = {x:x**2 for x in range(6,11)}

print(first) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(second) # {6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
merge_dict = {**first,**second} 
print(merge_dict) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


# Create a nested dictionary representing a student with keys 'name', 'age', 'grades', where 'grades' is another dictionary with keys 'math', 'science', and 'english'. Print the nested dictionary.

student = {
    "name":"Bhaskar",
    "age":21,
    "grades":{
        "math":"A+",
        "science":"A+",
        "english":"A+"
    }
}
print(student) # {'name': 'Bhaskar', 'age': 21, 'grades': {'math': 'A+', 'science': 'A+', 'english': 'A+'}}


# Create a dictionary where the keys are the first 5 positive integers and the values are lists containing the first 5 multiples of the key. Print the dictionary.


x = {a:[a*i for i in range(1,6)] for a in range(1,6)}
print(x)

# {
# 1: [1, 2, 3, 4, 5],
#  2: [2, 4, 6, 8, 10],
#  3: [3, 6, 9, 12, 15],
#  4: [4, 8, 12, 16, 20],
#  5: [5, 10, 15, 20, 25]
# }


# Create a dictionary where the keys are the first 5 positive integers and the values are tuples containing the key and its square. Print the dictionary.

tp = {x:(x,x**2) for x in range(5)}
print(tp)

# {
# 0: (0, 0),
#  1: (1, 1),
#  2: (2, 4),
#  3: (3, 9),
#  4: (4, 16)
# }


# Create a dictionary with the first 5 positive integers as keys and their squares as values. Convert the dictionary to a list of tuples and print it.

num_sq = {x:x**2 for x in range(5)}

new_lst = list(num_sq.items())
print(new_lst)
#  [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]


#  Create a new dictionary containing only the key-value pairs where the key is even. Print the new dictionary.

dtct = {x:x**2 for x in range(10) if x%2 == 0}
print(dtct)
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


# Create a dictionary with the first 5 positive integers as keys and their squares as values. Create a new dictionary with keys and values swapped. Print the new dictionary.

ab = {x:x**2 for x in range(5)}
new_dict = {}
print(ab) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

for key,value in ab.items():
    new_dict[f"{value}"] = key
print(new_dict) # {'0': 0, '1': 1, '4': 2, '9': 3, '16': 4}


# Create a default dictionary where each key has a default value of an empty list. Add some elements to the lists and print the dictionary.


# to create the default dictionary we need to import the defaultdict from collections module
default_dict = defaultdict(list) # we are passing list as a argument 
# when we add the new key it will automatically add the empty list as a value
default_dict["student"].append("Bhaskar")
default_dict["student"].append("Bishal")
default_dict["student"].append("Ayush")
print(default_dict)
# defaultdict(<class 'list'>, {'student': ['Bhaskar', 'Bishal', 'Ayush']})


# Write a function that takes a string and returns a dictionary with the count of each character in the string. Print the dictionary.

def dict_str(s):
    new_dict = {}
    for x in s:
        if x in new_dict: #check that character already exist in dictionary or not
            new_dict[x] += 1 #increase the count value by 1
        else: #if not exist it means it appear frist time
            new_dict[x] = 1
    return new_dict

result_str = dict_str("aaabbb")
print(result_str)
# {
# 'a': 3,
#  'b': 3
# }

# So in the given string a is appear 3 times and b is appear 3 times



# Create a dictionary representing a book with keys 'title', 'author', 'year', and 'genre'. Convert the dictionary to a JSON string and print it.

book = {
    "title":"A to Z",
    "author":"Bhaskar Rai",
    "year":"2083 BS",
    "genre":"fiction"
}

# to convert the json string we need to import the json module
json_str = json.dumps(book) # dumps method we use to convert the dictionary into json string
print(json_str) # {"title": "A to Z", "author": "Bhaskar Rai", "year": "2083 BS", "genre": "fiction"}
