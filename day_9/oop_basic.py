import math 
""" OOP basic """

""" 
Object-oriented programming is a paradigm that uses objects to design applications and computer programs. OOP allows us to model real-world scenarios using classes and objects.
"""
# creating class and object 

# while creating the class we use the class keyword
class Car:
    def run(self):
        print("Car is running")
    
    def stop(self):
        print("Stop the car")

# creating the object of class

byd = Car()

# calling the run() and stop() method

byd.run() #output: Car is running
byd.stop() #output: Stop the car

# defining attribute in class

byd.price = 10000000
print(byd.price) #output: 10000000
# we can also define the attribute in this way but more better way is using constructor





# So another class with contstructor and attribute

class Animal:

    # this is the constructor
    def __init__(self,legs,animal_type):
        self.legs = legs
        self.animal_type = animal_type
    
    def print_type(self):
        return self.animal_type
    
    def print_number_legs(self):
        return self.legs

dog = Animal(4,"dog")
print(f"This is {dog.print_type()} with {dog.print_number_legs()} number of legs")
# output: This is dog with 4 number of legs
print(type(dog)) #output:<class '__main__.Animal'>







"""
In Python, a constructor is a special method that is automatically called when a new object of a class is created.
"""

class Cat:
    def __init__(self): #constructor
        print("Cat object is created")

# creating object of Cat
billi = Cat()
# output: Cat object is created
# it show the outout because Cat() object is created so constructor is called


# Create a class named `Student` with attributes `name` and `age`. Use a constructor to initialize these attributes. Create an object of the class and print its attributes.

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def details(self):
        print(f"His name is {self.name} and he is {self.age} years old.")

bhaskar = Student("Bhaskar",20)

# calling the detalis method
bhaskar.details() #His name is Bhaskar and he is 20 years old.

# Create a class named `BankAccount` with private attributes `account_number` and `balance`. Add methods to deposit and withdraw money, and to check the balance. Create an object of the class and perform some operations.
import random
class BankAccount:
    __is_account_created = False
    __account_number = 0
    __balance = 0 
    #this all attribute are private only we can access inside this class
    def __init__(self):
        pass

    # method to create account
    def create_account(self):
        self.__account_number = random.uniform(0,1)
        self.__is_account_created = True
        print("Account created successfully.")

    # method to deposite the balance
    def deposite_balance(self,balance):
        if not self.__is_account_created:
            print("Sorry! you don't have create the account.")
            return
        self.__balance += int(balance)
        print(f"Currenct balace:{self.__balance}\nAccount number:{self.__account_number}")

    # method to withdraw the balance
    def withdraw_balance(self,amount):
        if not self.__is_account_created: # check is account is created or not
            print("Sorry! you don't have create the account.")
            return
        
        if self.__balance < amount: # check if amount is smallar or not comaper to balance
            print("Sorry! sir not engouh balance.")
            return

        self.__balance -= amount #deducting the amount 
        print(f"Currenct balace:{self.__balance}\n Withdraw amount:{amount}\n Account number:{self.__account_number}")
    
    # method to check the details
    def print_details(self):
        print(f"Currenct balace:{self.__balance}\nAccount number:{self.__account_number}")

myacc = BankAccount()
myacc.deposite_balance(100) # output: Sorry! you don't have create the account.
# so we need to create the account
myacc.create_account() # so i have created the account
# output: account created successfully.
# new i try to withdraw the money without deposit
myacc.withdraw_balance(100)
# output: Sorry! sir not engouh balance.
# so i don't have enought balance to withdraw
# let's deposite some amount of money
myacc.deposite_balance(1000)
# output:
# Currenct balace:1000
# Account number:0.1186742561073364
# now withdraw the 500 and check the current balance
myacc.withdraw_balance(500)
# output:
# Currenct balace:500
# Withdraw amount:500
# Account number:0.1186742561073360




""" Static method """

class Math_op:

    @staticmethod
    def add(a,b):
        return a+b
    
print(Math_op.add(10,10))
# output: 20 
# to call the static method we don't need to create the object of class
