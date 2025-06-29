file_read = open("C:/Users/knitt/OneDrive/Desktop/New file.txt", "r")
print("file in read mode")
print(file_read.read())
file_read.close()

file_write = open("C:/Users/knitt/OneDrive/Desktop/New file.txt", "w")
file_write.write(" File in write mode ....")
file_write.write("My hobbies are coding, crocheting and reading!")
file_write.close

file_append = open("C:/Users/knitt/OneDrive/Desktop/New file.txt", "a")
file_append.write("\n File in append mode ....")
file_append.write("I love the colors pink, white,terquoise!")