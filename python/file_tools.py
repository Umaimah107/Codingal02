file_read = open("C:/Users/knitt/OneDrive/Desktop/New file.txt", "r")
print("file in read mode")
print(file_read.read())
file_read.close()

file = open("C:/Users/knitt/OneDrive/Desktop/New file.txt", "r")
print(" \n Read in Parts \n ")
print(file.read(5))
file.close

with open("C:/Users/knitt/OneDrive/Desktop/new file453.txt", "r") as file:
    data = file.readlines()
    print("Words in this file are.......")
    for line in data:
        word = line.split()
        print(word)
file.close        

file = open("C:/Users/knitt/OneDrive/Desktop/New file.txt", "a")
file.write(" My favourite Language to code in is python!")
file.close

