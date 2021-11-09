lists = [5, 8, 3, 2, 4, 12, 23, 55]


print("\nGiven List : ", lists)


print(lists[:3])  # position 0 1 2

print(lists[3:])  # position 3 to end

print(lists[:-3])  # except last 3 items from end

print(lists[-3:])  # last 3 items from end

print(lists[3:-3])  # position 3 to except last 3


lists.sort()
print("\nsorted list : ", lists)


lists.reverse()  # reverse with built-in function
print("\nreversed list : ", lists)


lists.append(40)
print("\nafter append : ", lists)


list2 = [11, 22, 33, 11]
lists.extend(list2)  # combining 2 different lists
print("\nExtended list : ", lists)


lists.insert(2, 99)  # inserting 99 at index 2
print("\nafter inserted : ", lists)


# counting the occurrence of 11 in the list
print("\n11 exists in List :", lists.count(11))


lists.pop(1)  # poping the value of index 1
print("\nafter pop value of index 1 : ", lists)


lists.clear()  # deleting values of the list
print("\nCleared list : ", lists)
