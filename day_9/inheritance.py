"""
Inheritance is a feature of object-oriented programming that allows a class (called the child class or subclass) to inherit properties and behaviors (attributes and methods) from another class (called the parent class or superclass).

It helps to:
Reuse code.
Organize programs into a hierarchical structure.
Extend or modify functionality of the parent class.
"""


""" Single inheritence """
# this is the base class
class Phone:
    def __init__(self):
        pass 

    def calling(self):
        print("Calling....")
    
    def camera(self):
        print("Camera....")


# creating the child class with the helps of parent class
class Keypad(Phone):
    def __init__(self):
        pass

    def radio(self):
        print("Playiing radio")

# creating another child (SmartPhone) with screen touch feature
class SmartPhone(Phone):
    def __init__(self):
        pass

    def screen_touch(self):
        print("Screen touch feature")


# creating the object of nokia
nokia = Keypad()
nokia.calling() #parents class method
#output: Calling....
nokia.radio() #its own method
# output: Playing radio


# creating the object of samsung
samsung = SmartPhone()
samsung.screen_touch() #its own method
# output: Screen touch feature
samsung.calling() # parents class method
# output: Calling







""" Multiple in heritence """

# base class one 
class Analog_watch:
    def __init__(self):
        pass

    def clock_hand(self):
        print("Display the time using the clock hand.")
    
    def classic_looks(self):
        print("It's design is classic")


# base class tow
class Digital_watch:

    def __init__(self):
        pass

    def digital_num(self):
        print("Show the time in digital number.")
    
    def alarm(self):
        print("Features of alarm")
    
    def calling(self):
        print("Feature of calling")
    
# derive class from both base class
class Hybird_watch(Digital_watch,Analog_watch):

    def __init__(self):
        pass
    
    def information(self):
        print("It is the combination of both analog and digital watch.")

# new create the object of Hybird_watch

hybird = Hybird_watch()

hybird.information() #calling its features

hybird.alarm() # this is the method of digital watch class
hybird.clock_hand() # this is the method of analog watch

# output:
# It is the combination of both analog and digital watch.
# Features of alarm
# Display the time using the clock hand.



    
