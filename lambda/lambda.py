# lambda function is a small anonymous function.
# It can take any number of arguments, but can only have one expression

#syntax = lambda arguments : expression

def Xfunc(a, b, c, d, e): return a + b - c * d / e


print(Xfunc(5, 6, 2, 0, 2))  # 5+6-2*0/2


def func(n):
    return lambda a: a * n


x = func(2)  # sending value of n
y = func(3)

print(x(11))  # sending value of a
print(y(11))
