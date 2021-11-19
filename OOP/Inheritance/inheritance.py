class vehicle:
    def __init__(self, name, manufact, color):
        self.name = name
        self.manufacturer = manufact
        self.color = color
    def drive(self):
        print("Driving ", self.manufacturer, self.name)
    def turn(self, direction):
        print("Turning ", self.name, "to ", direction)
    def brake(self):
        print(self.name," is stopping!!")
class Car(vehicle):
    def change_gear(self, gear_name):
        print(self.name, ' is changing gear to ', gear_name)

if __name__ == '__main__':
    c= Car('Porsche', 'F. Porsche AG' , 'Black')
    c.drive()
    c.turn('right')
    c.brake()
    c.change_gear('P')