class Car:
    def __init__(self,n,c): # when we create object it auto call this __init__ . It's Constructor
        self.name = n
        self.color = c
    def start(self): # when we call method with Object, Object passes as argument that's why self
        print("Car name : ", self.name)
        print("Car color : ", self.color)
        print("Engine is starting !! \n")

myCar = Car("Pourche", 'Black') # object creating and passing argument to the Constructor
myCar.start() # method calling with object or instance

yourCar = Car("Corolla", 'White') # object creating and passing argument to the Constructor
yourCar.start() # method calling with object or instance