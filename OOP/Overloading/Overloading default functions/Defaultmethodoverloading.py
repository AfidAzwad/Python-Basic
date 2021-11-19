class overloading:
    def __init__(self,argument1, argument2):
       self.argument1 = argument1
       self.argument2 = argument2
    def __len__(self):
      return argument1+argument2

list1 = [ 3,10,0 ]
list2 = [ 4,7,8,9 ]

# Using len() function without method overloading
argument1 = len(list1)
argument2 = len(list2)

Obj = overloading(argument1,argument2)
print('Overall length of both the lists : ', len(Obj))