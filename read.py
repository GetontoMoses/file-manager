# opening
with open("file.txt", "r", encoding="utf-16") as file:# using r it overwrites the existing code

    # read
    content = file.readlines()
    
    # display
    print(content)
