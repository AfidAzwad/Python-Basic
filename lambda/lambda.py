#lambda function is a small anonymous function.
#It can take any number of arguments, but can only have one expression

#syntax = lambda arguments : expression

x = lambda a, b, c, d, e : a + b - c * d / e

print(x(5, 6, 2, 0, 2)) #5+6-2*0/2
print(int(x(5, 6, 2, 0, 2)))


def func(n):
  return lambda a : a * n

x = func(2)
y = func(3)

print(x(11))
print(y(11))