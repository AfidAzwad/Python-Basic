randomList = ['a', 0, 2]

for i in randomList:
    try:
        print("The entry is", i)
        res = 1/int(i)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next.......\n")

print("The reciprocal of", i, "is", res)