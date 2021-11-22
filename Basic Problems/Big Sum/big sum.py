import math
import os
import random
import re
import sys

def bigsum(arr):
    s = 0
    for i in arr:
        s = s + i
    return s


if __name__ == '__main__':
    size = int(input("array size = ").strip())
    arr = []
    for i in range(size):
        value = int(input().strip())
        arr.append(value)
        
    s = bigsum(arr)
    print("Big Sum :", s)