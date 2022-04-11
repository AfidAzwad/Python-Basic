class A:
    def __init__(self):
        print("A")
        
class B(A):
    def __init__(self):
        print("B")
        
class C(B):
    def __init__(self):
        print("C")
        
class D(C):
    def __init__(self):
        print("D")
    def __del__(self):
        print("destructor!!")


d = D()



        