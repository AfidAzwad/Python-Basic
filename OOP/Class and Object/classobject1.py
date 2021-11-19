class Car:
    name = ""
    color = ""

    def start():
        print("Engine is starting !!")


Car.name = 'Porsche'
Car.color = 'Black'

print(Car.name, "\n", Car.color)
Car.start()
