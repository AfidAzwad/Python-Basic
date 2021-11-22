year = input('Give a Year to check Leap Year :')
year = int(year)
if year % 4 !=0:
    print(year,'is not a Leap Year')
else:
    if year % 100 ==0:
             if year % 400 ==0:
                   print(year,'is a Leap Year')
             else:
                 print(year,"is not a Leap Year")
    else:
          print(year,'is a leap year')






if year % 400 ==0:
    print(year,'is a Leap Year')
elif year % 100 == 0:
    print(year,'is not a Leap Year')
elif year % 4 == 0:
    print(year,'is a Leap Year')
else:
    print(year,'is not a Leap Year')

