list = [1,2,3,4,5,6,7,8,9]

print(list)

print(list[0]) #value of index 0

print(list[::-1]) #reverse the list

print(list[2:5]) #value of index 2 to before 5

list[2] = 11 #changing the value of index 2

print(list)

list.reverse() #reverse with built-in function
print(list)

list.append(55) # adding value with append function
print(list)

list2 = [11,22,33,44,55,66,77,88]
list.extend(list2) #combining 2 different lists

print(list)
print(len(list)) #checking length of the list

list.insert(2,99) #inserting 99 at index 2
print(list)

print(list.count(11)) #counting the occurrence of 11 in the list

list.pop(1)  #poping the value of index 1
print(list)

list.sort()  #sorting the list from low to high
print(list)

list.clear() #deleting values of the list
print(list)


list.append(33) # creating a new list
print(list)