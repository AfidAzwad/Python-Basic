# key:value

dict ={"Me": 'Azwad',"Age": 23,"Birth":1888}

dict["Birth"] = 2018 #changing value of a key
print(dict)

print(dict.values())

dict2 = dict.copy() #copying the elements of dict to dict2
dict2["Birth"] = 2020 #changing value of a key
print(dict2)

print(dict2.__len__()) #finding the length of dict2

dict.update(dict2) #updating the different value of dict
print(dict)

dict2.clear() #deleting the elements of dict2
print(dict2)