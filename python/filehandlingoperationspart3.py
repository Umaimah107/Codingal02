file1 = open("C:/Users/knitt/OneDrive/Desktop/new file453.txt", "r")
file2 = open("C:/Users/knitt/OneDrive/Desktop/New file.txt","w")

for line in file1.readlines():
    if not (line.startswith("Coding")):
         print(line)
         file2.write(line)

file2.close()
file1.close()    