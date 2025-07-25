# let's learn about the function in python

"""
To create the function in python we use the def key word
"""

# how to create the function
def demo():
    print("Hello world")

demo() #calling the function
# output: Hello world


# function with return 
def demo_return():
    return ["Apple","Ball"]

get_result = demo_return() #calling the function
print(get_result) #output: ['Apple', 'Ball']



# function with taking argumenta and returning it.

def  get_return(x):
    return x

rslt = get_return(1000)

print(rslt) #output: 1000



""" Some example of function """

""" temperature conversion function """
# this function will convert the celciuse into fahrenheit and vice versa
def temp_convertor(temp,unit):
    if unit.lower() == "f":
        return (temp * 9/5) + 32
    elif unit.lower() == 'c':
        return (temp - 32) * 5/9
    else:
        return ("Please enter the valid unit or number")


ans = temp_convertor(37,'c') #calling the function
print(ans) #output : 98.6

""" Password Strength Checker """
# minimum length,
# presence of digits,
# lowercase and uppercase
# special characters.

def is_password_strong(pswd):
    # if password length is smaller the 6 it is weak password
    if len(pswd) < 6:
        return False
    if not any(x.isdigit() for x in pswd): #check there is digit or not
        return False
    if not any(y.islower() for y in pswd): #check is there any char are in small letter
        return False
    if not any(z.isupper() for z in pswd): #check any char are in captial or not
        return False
    special_char = "!@#$%^&**()~+_"
    if not any(a in special_char for a in pswd): # this will check the special character
        return False
    else:
        return True
    
print(is_password_strong("apple")) #output: False
print(is_password_strong("Mon123#$%45")) #output: True






""" Shopping Cart Total Cost Calculation """

shoping_cart = [
    {"product":"copy","brand":"classmate","quantity":1000,"price":100000},
    {"product":"Pen","brand":"classmate","quantity":100,"price":2000},
    {"product":"Bag","brand":"TheNorthFace","quantity":45,"price":45000},
    {"product":"Shoe","brand":"Nike","quantity":20,"price":40000},
]


# function to calculate the total cost of the shoping_cart
def cal_totalcost(cart):
    total_cost = 0
    for item in cart:
        for key,value in item.items():
            if key == "price":
                total_cost += value
    return total_cost 


print(cal_totalcost(shoping_cart)) #output: 187000






# Palindrome Checker
def check_pallindrom(s):
    
    return s.lower().replace(' ','') == s[::-1].replace(' ','').lower()

print(check_pallindrom("apple balll")) #False
print(check_pallindrom("aa bb aa")) #True
    
# lower() it convert into lowercase
# replace() it will take the two argument first argument is the character which need to replace by second chracter
# s[::-1] this slicing technique use to reverse the string



    







