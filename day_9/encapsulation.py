""" Encapsulation """

"""
Encapsulation in Object-Oriented Programming (OOP) is the concept of hiding the internal details of an object and restricting direct access to some of its components. Instead, access is provided through public methods (often called getters and setters)
"""



# public variable
# Accessible from anywhere.Inside or outside the class.
class User:

    def __init__(self,name,age):
        self.name = name #public variable
        self.age = age #public variable

ram = User("Ram",123)
print(ram.age) # output: 123
    

# private varaible

class Car:
    def __init__(self,company,price):
        self.__company = company # private variable
        self.__price = price  #private variable

kar  = Car("BMW",120000)

# print(kar.__price)
#AttributeError: 'Car' object has no attribute '__price'
# so wecan't access the private varaible outsite the class



# Protected varaible

class Animal:
    def __init__(self,name):
        self._name = name # Protected varaible

dog = Animal("dog")

print(dog._name) # it is accessable but no recommend
# protected varaible is created to access inside the class and in subclass

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)


votey = Dog("Vokey kukur")
print(votey._name) # output: Vokey kukur









""" Encapsulation with getter and setter method """
class Phone:

    def __init__(self,name):
        self.__name = name #private varaible

    # getter method
    def get_name(self):
        return self.__name 
    
    def set_name(self,name):
        self.__name = name 

# now try to access the name with get method and update the value of name with set method

phn = Phone("samsung")
print(phn.get_name()) # output: samsung

phn.set_name("Iphone")

print(phn.get_name())  #output: Iphone 

