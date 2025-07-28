
""" Polymorphism """

"""
Polymorphism means "many forms."
It allows the same function, method, or operator to work in different ways depending on the object or data type
"""


# base class
class Iphone:
    def __init__(self,iphone_type,camera,storage,price):
        self.iphone_type = iphone_type
        self.camera = camera
        self.storage = storage
        self.price = price

    def print_details(self):
        print(f"Name:{self.iphone_type}\n Camera:{self.camera}\n Storage:{self.storage}\n Price:{self.price}")
    

# base class
class Iphone_15(Iphone):
    def __init__(self,iphone_type,camera,storage,price):
        super().__init__(iphone_type,camera,storage,price)
    
    def print_details(self):
        return super().print_details()

# another base class

class Iphone_16(Iphone):
    def __init__(self,iphone_type,camera,storage,price):
        super().__init__(iphone_type,camera,storage,price)
    
    def print_details(self):
        return super().print_details()


# creating the object of Iphone_15
iphone_15 = Iphone_15("Iphone 15","40MP","128GB","Rs.180000")
iphone_15.print_details() 

# ouutpu:
# Name:Iphone 15
# Camera:40MP
# Storage:128GB
# Price:Rs.18000

# creating the object of Iphone_16
iphone_16 = Iphone_16("Iphone 16","48MP","256GB","Rs.240000")
iphone_16.print_details() 

# output:
# Name:Iphone 16
# Camera:48MP
# Storage:256GB
# Price:Rs.240000

# here we call the same method from parents but it output is different so it is know as polymorphism



# Example of Shapa and area:

# parents class
class Shape_and_area:

    def area(self):
        print(f"Calculating area")


# base class
class Rectangle(Shape_and_area):

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f"Area of reactange is:{self.length*self.breadth}")
    

# base class
class Circle(Shape_and_area):

    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        print(f"Area of circle:{3.14*self.radius**2}")



circle = Circle(7)
circle.area()
# output: Area of circle:153.86


rectangle = Rectangle(10,10)
rectangle.area()
# output: Area of reactange is:100



""" 
**** Abstract class ****

An abstract class is a class that cannot be instantiated directly. It is used as a base class and typically contains abstract methods that are declared but don’t have any implementation in the abstract class itself. 

These must be implemented by its child classes.
"""

from abc import ABC , abstractmethod
# abc is inbuilt module in python
# ABC in inbuilt class in python


class Book(ABC):

    @abstractmethod
    def book_details(self):
        pass
# this is the abstractmethod 


class Muna_madan(Book):

    def __init__(self,book_name,genre):
        self.book_name = book_name
        self.genre = genre
    
    def book_details(self):
        print(f"Book name:{self.book_name}\n Genre:{self.genre}")


class Kabi(Book):
    def __init__(self,book_name,genre):
        self.book_name = book_name
        self.genre = genre
    
    def book_details(self):
        print(f"Book name:{self.book_name}\n Genre:{self.genre}")


# creating the object of Muna_madan

muna_madan = Muna_madan("Muna Madan","Romance")
muna_madan.book_details()
# output:
# Book name:Muna Madan
# Genre:Romance
kabi = Kabi("Kabi","Mystery")
kabi.book_details()
# output:
# Book name:Kabi
#  Genre:Mystery


"""
***** Note *****
if we don't implement the abstract method after initiating the abstract class it will throw the error: TypeError: Can't instantiate abstract class Kabi without an implementation for abstract method 'book_details'
"""