# Program to check if a number is prime or not

num = [20, 70, 29, 97 ]

flag = False

for number in num:
    for i in range(2, number):
        if (number % i) == 0:
            flag = True
            # break out of loop
            break
        else:
            flag = False
    
    if not flag:
        print(number, "is a prime number")
        