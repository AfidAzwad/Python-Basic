import collections


print (collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))


arr = [ "d",  "d" , "a", "b",  "d",  "a",  "d"]

print (collections.Counter(arr))


# Output :   Counter({'b': 3, 'a': 2, 'c': 1})
           # Counter({'d': 4, 'a': 2, 'b': 1})