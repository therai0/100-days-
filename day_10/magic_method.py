""" 
Magic method

Magic methods in Python are also known as dunder methods, which means double underscore methods. These are special methods that start and end with double underscores. Magic methods enable you to define the behavior of an object for built-in operations such as arithmetic operations, comparisons, and more.
"""

class Mobile:
    def __init__(self): # this is also magic method 
        print("Object is created")

mbl = Mobile()

print(dir(mbl))

# output:
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__']

# this all are magic method
# we can overide the magic method

class Demo:

    def __init__(self): #magic method
        pass

    def __str__(self): #magic method
        return "This is demo object"

obj = Demo()
print(obj)
# output: This is demo object



""" vector adding using the magic method """

class Vector:

    def __init__(self,x,y):
        self.x = x 
        self.y = y

    def __add__(self,next):
        return Vector(self.x + next.x,self.y+next.y)
    
    def __sub__(self,next):
        return Vector(self.x - next.x,self.y-next.y)
    
    def __mul__(self,next):
        return Vector(self.x * next.x,self.y*next.y)
    
    def __repr__(self):
      return f"Vector({self.x,self.y})"

first = Vector(10,10)
second = Vector(5,5)
print(first+second)
# output: Vector((15, 15))
print(first-second)
# output: Vector((5, 5))
print(first*second)
# output: Vector((50, 50))

"""
Explanation 
__add__() # this magic method use to add the two object


__add__(self,next):
 here next argument we are passing as another object of class

 like:
first = Vector(10,10)
second = Vector(5,5)

 first.__add__(second)
  this is equivalent to first + second

similarly others methods also works in this way
"""