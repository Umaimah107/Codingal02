file_obj = open("C:/Users/knitt/OneDrive/Desktop/New file.txt", "w")
file_obj.write("I love to code!")
file_obj.close()

file = open("C:/Users/knitt/OneDrive/Desktop/New file.txt", "r")
print(" \n Read in Parts \n ")
print(file.read(8))
file.close

file = open("C:/Users/knitt/OneDrive/Desktop/New file.txt", "a")
file.write(" My favourite Language to code in is python!")
file.close
