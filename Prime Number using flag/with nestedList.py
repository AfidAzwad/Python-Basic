
num = [[20, 70, 29, 97], [50,90,40,29], [50,90,40,20] ]

flag = False

for number in num:
    for n in number:
      for i in range(2, n):
            if (n % i) == 0:
                flag = True
                break
            else:
                  flag = False
      if not flag:
         break
    if not flag:
      print("YES")
    else:
      print("NO")