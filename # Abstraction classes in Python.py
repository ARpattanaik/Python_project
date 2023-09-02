# Abstraction classes in Python

# In Python, abstraction can be achieved by using abstract classes and interfaces.

# A class that consists of one or more abstract method is called the abstract class. Abstract methods do not contain their implementation. 
# Abstract class can be inherited by the subclass and abstract method gets its definition in the subclass. 
# Abstraction classes are meant to be the blueprint of the other class. An abstract class can be useful when we are designing large functions. 
# An abstract class is also helpful to provide the standard interface for different implementations of components.

# base.py
class Base:
    def create_data(data,id):
        #logic of creation data
        
        data.save()

# patient.py
class Patient(Base):
   def create_data(data, patientId):
      data={"name":"abc", "id":"UUID","patientId":"P001","appointedAt":"23-03-2023","createdAt":"23-03-2023"}
    #   E6A23DB4-1F46-4912-95C8-235A1FB538A6
      return super().create_data(data, patientId)
   
# doctor.py
class Doctor(Base):
   def create_data(data, doctorId):
      return super().create_data(data, doctorId)
   

# Syntax:
# from abc import ABC  
# class ClassName(ABC):  

# Python program to define   
# abstract class  
  
# from abc import ABC  
  
# class Polygon(ABC):   
  
#    # abstract method   
#    def sides(self):   
#       pass  
  
# class Triangle(Polygon):   
  
     
#    def sides(self):   
#       print("Triangle has 3 sides")   
  
# class Pentagon(Polygon):   
  
     
#    def sides(self):   
#       print("Pentagon has 5 sides")   
  
# class Hexagon(Polygon):   
  
#    def sides(self):   
#       print("Hexagon has 6 sides")   
  
# class square(Polygon):   
  
#    def sides(self):   
#       print("I have 4 sides")   
  
# # Driver code   
# t = Triangle()   
# t.sides()   
  
# s = square()   
# s.sides()   
  
# p = Pentagon()   
# p.sides()   
  
# k = Hexagon()   
# k.sides()   


# Points to Remember
# Below are the points which we should remember about the abstract base class in Python.

# An Abstract class can contain the both method normal and abstract method.
# An Abstract cannot be instantiated; we cannot create objects for the abstract class.
# Abstraction is essential to hide the core functionality from the users. We have covered the all the basic concepts of Abstraction in Python.


# Polymorphism


# What is Polymorphism?
# The literal meaning of polymorphism is the condition of occurrence in different forms.

# Polymorphism is a very important concept in programming. 
# It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.

# '+' - Addition Operator

# num = 1
# num2 = 2

# print(num + num2) # addition

# s="hello"
# s2="world"

# print(s+s2) # concate

# print(s+ " " +s2)

# Method Overriding - same method name but content are different
# Method Overloading, a way to create multiple methods with the same name but different arguments, 
# is not possible in Python


# class Bank:
   
#    def display(self, name):
#       print("Bank display")

# class Loan(Bank):
   
#    def display(self, name, age):
#       print(" Loan Display")

# l = Loan()
# l.display()


from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
