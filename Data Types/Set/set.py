set = {"apple", 21 , 33 , "lichi", "mango", 44}
set2 = {"banana"}
print(set)

set.update(set2) #set1.update(set2) Here set1 is the set in which set2 will be added
print(set)

set2.add(55) #adding an element
print(set2)

print("banana" in set) #finding string element in set
print(35 in set) #finding integer element in set