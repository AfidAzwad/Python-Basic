# A static method is a method which is bound to the class and not the object of the class.
# It can’t access or modify class state.
# It helps developers write code in a safe architectural way to prevent conflicts in the code.

class Person:
    def __init__(self, age):
        self.age = age
    # a static method to check if a Person is adult or not.
    @staticmethod # static method decorator
    def isAdult(age):
        return age > 18
# Driver's code
if __name__ == "__main__":
    res = Person.isAdult(12)
    print('Is person adult:', res)
    res = Person.isAdult(22)
    print('Is person adult:', res)