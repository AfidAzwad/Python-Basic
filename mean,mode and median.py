List = [1,2,3,4,11,15,12,13,14,15]

def mean(L):
    total = 0
    m = sum(L)/len(L)
    return int(m)


def mode(L):
    List2 = {}
    for i in L:
        if i not in List2:
            List2[i] = 1
        else:
            List2[i] +=1
            
    max_count = 0
    mode = 0
    for n in List2.keys():
     if List2[n] > max_count:
      max_count = List2[n]
      mode = n
    return mode


def median(L):
    if len(L) % 2 != 0:
      mid = int(len(L)-1/2)
      return L[mid]
    else:
        mid1 = int(len(L)/2)-1
        mid2 = int(len(L)/2)
        return L[mid1],L[mid2]

print(mean(List))
print(mode(List))
print(median(List))