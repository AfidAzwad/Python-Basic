class SmartPhone:
    __password = 'afid' # Encapsulation
    def __init__(self, version):
         self.version = version
    def open(self,pas):
        if self.__password == pas:
            print("Version : ", self.version)
            print("Open.....")
        else:
            print("Wrong password!!!")
class Samsung(SmartPhone): # Inheritance
    def open(self,pas):
        return super().open(pas) # Overloading open()

    def open(self,pas): # Overridding open() and polymorphism(act as many form)
        print("Version : ", self.version)
        print("Password : ", pas)

sp = SmartPhone(5.0)
sp.open('afid')

s = Samsung(5.1)
s.open('azwad')