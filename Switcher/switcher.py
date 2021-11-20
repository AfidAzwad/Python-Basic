def week(i):
        switcher={
                0:'Sunday',
                1:'Monday',
                2:'Tuesday',
                3:'Wednesday',
                4:'Thursday',
                5:'Friday',
                6:'Saturday'
             }
        return switcher.get(i,"Invalid day of week\n")
print(week(0))
print(week(5))
print(week(8))


def me(s):
    switcher = {
        'ami': 'bored',
        'you' : 'no',
        'we' : 'No way',
        'family' : 'Yes'
    }
    return switcher.get(s, "Thug life ")

print(me('ami'))
print(me('family'))
print(me('love'))
