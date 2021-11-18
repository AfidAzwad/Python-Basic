def fibonacci(n):
    if n <= 2:
        return 1
    fib_x, fibnext = 1,1
    i =3
    while i<=n:
        i+=1
        fib_x, fibnext = fibnext, fib_x + fibnext
    return fibnext


for x in range(1,11):
    print(fibonacci(x))