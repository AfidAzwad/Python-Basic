def fact(n):
    result = n
    for i in range(n,1,-1):
        result = result * (i-1)
    return result

if __name__ == '__main__':
    n = input("n = ")
    print("Factorial of " + n + " is " + str(fact(int(n))))