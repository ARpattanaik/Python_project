# Python Classes
# A class is considered as a blueprint of objects. 
# We can think of the class as a sketch (prototype) of a house. 
# It contains all the details about the floors, doors, windows, etc. 
# Based on these descriptions we build the house. House is the object.

# Since many houses can be made from the same description, we can create many objects from a class.

# syntax of class
class ClassName:

        # statements
        # methods
        # properties
        # functions

    # class definition 

# Here, we have created a class named ClassName.

# Let's see an example,

    class Bike:
        name = ""
        gear = 0
# Here,

# Bike - the name of the class
# name/gear - variables inside the class with default values "" and 0 respectively.
# Note: The variables inside a class are called attributes.

# Python Objects
# An object is called an instance of a class. For example, suppose Bike is a class then we can create 
# objects like bike1, bike2, etc from the class.

# Here's the syntax to create an object.

objectName = ClassName()
# Let's see an example,


# create class
class Bike:
    name = ""
    gear = 0

# create objects of class
bike1 = Bike()
bike2 = Bike()
bike1.name = "Pulsar"
bike2.name="Ducati"
print("Bike Name: ",bike1.name)
print("Bike 2 Object Name: ",bike2.name)
# # Here, bike1 is the object of the class. Now, we can use this object to access the class attributes.

# # Access Class Attributes Using Objects
# # We use the . notation to access the attributes of a class. For example,

# # modify the name attribute
bike1.name = "Mountain Bike"

# # access the gear attribute
bike1.gear
# # Here, we have used bike1.name and bike1.gear to change and access the value of name and gear attribute respectively.

# # Example 1: Python Class and Objects
# # define a class
class Bike:
    name = ""
    gear = 0

# # create object of class
bike1 = Bike()

# # access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")
# # Run Code
# # Output

# # Name: Mountain Bike, Gears: 11


# Factorial example

class Factorial:
    fact = 1
    gear = 0
    print("Inside the class ")

    def fact(self):
         print("this is factorial function")

    def display(self):
        name="Test"
        print("Inside the class function ")
        # print("Name of the Bike: ", self.fact)


obj = Factorial()
obj.fact()

