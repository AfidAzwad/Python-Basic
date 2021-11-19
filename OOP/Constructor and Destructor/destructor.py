class vehicle:
    def __init__(self, name, manufact, color):
        self.name = name
        self.manufacturer = manufact
        self.color = color
        print("Constructor started.... ")
    def __del__(self):
            print("Destructed !! ")
    def drive(self):
        print("Driving ", self.manufacturer, self.name)


if __name__ == '__main__':
    car= vehicle('Porsche', 'F. Porsche AG' , 'Black')
    car.drive()

# after the constructor of vehicle class the destructor is automatically executed