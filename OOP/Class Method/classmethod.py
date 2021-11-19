# Class is passed in the function as a parameter, and it should be the first parameter.
# We use the ‘cls’ keyword for passing to the function. Cls denotes that class is passed as a variable. This is done so that we can modify the variable of the class and objects.
# The Best use of the class method is when we are making too many methods, and we want to call those methods using class, not objects.

class Car:
    def __init__(self, features):
      self.features = features

    def __repr__(self): # The __repr__ method returns the string representation of an object.
     return f'Car({self.features})' # f-strings ex: print(f"{val}for{val} is a portal for {val}.") where val = Geeks

    @classmethod
    def audi(cls):
      return cls(['ABS', 'Disk Brakes'])
    @classmethod
    def mercedes(cls):
      return cls(['ABS', 'Disk Brakes', 'GPS', 'Alloy Wheels'])

print(Car.audi())
print(Car.mercedes())