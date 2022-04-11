# Abstraction is used to hide the internal functionality of the function from the users. Ex : Camera in phone
# An Abstract class can contain the both method normal and abstract method.
# An Abstract cannot be instantiated; we cannot create objects for the abstract class.

from abc import ABC, abstractmethod

class Polygon(ABC):
   # abstract method
   @abstractmethod
   def sides(self):
      pass
class Triangle(Polygon):
   def sides(self):
      print("Triangle has 3 sides")

class square(Polygon):
   def sides(self):
      print("Square has 4 sides")

# Driver code
t = Triangle()
t.sides()

s = square()
s.sides()