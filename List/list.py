lists = [5,8,3,2,4,12,23,55]


print("\nGiven List : ", lists)


print(lists[:3]) # position 0 1 2

print(lists[3:]) # position 3 to end

print(lists[:-3]) # except last 3 items from end 

print(lists[-3:]) # last 3 items from end 

print(lists[3:-3]) # position 3 to except last 3


lists.sort()

print("\nsorted list : ", lists)

lists.append(40)

print("\nafter append : ",lists)
