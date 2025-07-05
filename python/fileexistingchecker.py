new_file = open("C:/Users/knitt/OneDrive/Desktop/new file800.txt", "x")
new_file.close()

import os
print("Checking if my_file exists or not.......")
if os.path.exists("C:/Users/knitt/OneDrive/Desktop/new file800.txt"):
    os.remove("C:/Users/knitt/OneDrive/Desktop/new file800.txt")
else:
    print("the file does not exist")    

my_file = open("C:/Users/knitt/OneDrive/Desktop/new file453.txt", "w")
my_file.write("I lovecoding and it is my favourite hobby")
my_file.close()

os.remove("C:/Users/knitt/OneDrive/Desktop/new file453.txt")