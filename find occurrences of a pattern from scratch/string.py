text  = "tadadattaetadadadafa"
pattern = 'dada'
t = len(text)
p = len(pattern)
count = 0

for i in range(t): # the loop will run from 0 to len(text)-1 = 19
    j = 0 # for pattern
    while j < p:
        if (text[i+j] != pattern[j]): # if not matched then while loop will be off and the value of i will be increased
            break
        j += 1 # to match the pattern index one by one
    if (j == p): # this means our pattern size is over and we have found a full match
        count += 1 # it will count the occurences
        j = 0 #it will reset to 0 to match with pattern everytime if match with 1st index of pattern

print("Here the pattern " + pattern + " appears in text(" + text + ") " + str(count) + " times")
