def print_num(n):
    if n == 0:
        return
    
    print(n)
    print_num(n-1)

if __name__ == '__main__':
    print_num(5)
    
# Output : 5 4 3 2 1
    print(" \n2nd part :")
    
def print_num1(n):
    if n == 0:
        return
    print_num1(n-1) # it will store the values from 5 to 1 in a stack(in computer memory). The pop as LIFO. 
    print(n)

if __name__ == '__main__':
    print_num1(5)
    
# Output : 1 2 3 4 5