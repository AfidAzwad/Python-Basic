import math

List = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def mean(L) :
    return sum(L) * 1.0 / len(L)


""" 
σ = Lower case sigma is the symbol for standard deviation
Σ = Upper case sigma is the summation symbol
X = Each individual value in the data set
x̅ = The arithmetic mean (known as “x-bar”)
n = The number of data points in the set (the number of X values)
"""

def stanDev(L):
    N = len(L)
    m = int(mean(L))
    total_sum = 0
    for i in range(N):
              total_sum += (L[i] - m)**2

    under_root = total_sum*1.0 / N
    return math.sqrt(under_root)


print(stanDev(List))