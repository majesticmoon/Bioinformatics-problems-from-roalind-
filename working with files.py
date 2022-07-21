f = open("working with files 2.txt")
contents = f.readlines()
for i in range(len(contents)):
    if i % 2 == 1:
        print(contents[i])
