def fib(n):
    if n in [1,2]:
        return 1
    result = fib(n-2) + fib(n-1)
    return result # 1 1 2 3 5 8 ..........
if __name__ == '__main__':
    print(fib(5))
