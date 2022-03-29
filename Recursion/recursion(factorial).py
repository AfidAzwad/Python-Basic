def f(n):
    if n <= 0:
        return None
    if n == 1:
        return 1
    print(n)
    return n * f(n-1) # n! = n x (n-1)!

if __name__ == '__main__':
    print(f(10))
    