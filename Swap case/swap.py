def swap_case(s):
    st = ''
    for i in s:
        if i == i.lower() :
            st += i.upper()
        elif i == i.upper():
            st += i.lower()
    return st

if __name__ == '__main__':
    s = input("string : ")
    result = swap_case(s)
    print(result)