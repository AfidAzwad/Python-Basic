def split_and_join(line):
    line = line.split(" ")
    
    print("Splited Line : ", line)
    
    return "-".join(line) # joined with hypen[-]

if __name__ == '__main__':
    
    line = input("Line : ") # this is a good thing
    
    result = split_and_join(line)
    print("Joined Line :", result)