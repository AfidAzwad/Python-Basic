class vehicle:
    def overloading_func(self, argument1 = 0, argument2 =0):
        if argument1 is not None or argument2 is not None:
            print("Overloading count : ", argument1+argument2)

v = vehicle()
# Call the method with no arguments
v.overloading_func()
# Call the method with 1 argument
v.overloading_func(1)
# Call the method with 2 arguments
v.overloading_func(1,1)