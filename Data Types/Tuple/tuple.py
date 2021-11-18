# Python hash() function is a built-in function and returns the hash value of an object if it has one. The hash value is an integer 
#   which is used to quickly compare dictionary keys while looking at a dictionary.


if __name__ == '__main__':
    
    n = int(input("no of items in tuple = "))
    t = tuple(map(int, input().strip().split(" "))) # input : 4 5 6 7 8
    
    print("\nTuple :", t)  
    
    print("\n2 in Tuple :", t.count(2), "times" )  # counting 2 in tuple
         
    print("\nHash value :", hash(t))
    
    print("\nLength of tuple : ",t.__len__()) #finding the length of tup

    tup2 = (99,44,55,88)
    print("\nafter adding new tuple : ", t.__add__(tup2)) #adding 2 tuples
    
    print("\nTuple : ", t)
    
    print("\nIndex value of 99 : ", t.__add__(tup2).index(99)) #finding the index no of 99 after adding to t

    

