class Vehicle:
    __name = 'Audi' #non-public method [ we can use _ or __ which is called Name Mangling ]
    def show(self):
        print(self.__name)
v = Vehicle()
v.show()
#Output : Audi



class Vehicle1:
    __name = ''
    def show1(self):
        self.__name = 'BMW'
        print(self.__name)
v1 = Vehicle1()
v1.show1()
#Output : BMW



class Vehicle2:
    __name = ''
    def _show1(self):
        self.__name = 'Corolla'
        print(self.__name)
    def show2(self):
        self._show1()
v2 = Vehicle2()
v2.show2()
#Output : Corolla CAUSE non-public methods can only be accessed inside class



class Vehicle3:
    __name = ''
    def _show3(self):
        self.__name = 'Bugatti'
        print(self.__name)
v1 = Vehicle3()
v1.show3()
#Output : AttributeError cause it can't access non-public method