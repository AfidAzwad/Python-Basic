# Python hash() function is a built-in function and returns the hash value of an object if it has one. The hash value is an integer 
#   which is used to quickly compare dictionary keys while looking at a dictionary.


if __name__ == '__main__':
    
    n = int(input("no of items in tuple = "))
    t = tuple(map(int, input().strip().split(" "))) # input : 4 5 6 7 8
    
    print("Tuple :", t)  
    
    print(" 2 in Tuple :", t.count(2) )  # counting 2 in tuple
         
    print( "Hash value :", hash(t))
    

