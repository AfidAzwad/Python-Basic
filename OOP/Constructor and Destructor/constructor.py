class vehicle:
    def __init__(self, name, manufact, color):
        self.name = name
        self.manufacturer = manufact
        self.color = color
        print("Constructor started.... ")

    def drive(self):
        print("Driving ", self.manufacturer, self.name)

if __name__ == '__main__':
    car= vehicle('Porsche', 'F. Porsche AG' , 'Black')
    car.drive()

# here __init__ is the constructor of vehicle class when we are creating object it's automatically executed