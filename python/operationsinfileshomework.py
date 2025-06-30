file_read = open("C:/Users/knitt/OneDrive/Desktop/New file.txt", "r")
print("Reading the whole file using read()")
print(file_read.read())
file_read.close()

file_readlines = open("C:/Users/knitt/OneDrive/Desktop/New file.txt", "r")
print("\nReading the file using readlines()")
lines = file_readlines.readlines()
for line in lines:
    print(line.strip())
file_readlines.close()

file_parts = open("C:/Users/knitt/OneDrive/Desktop/New file.txt", "r")
print("\nReading the file in parts of 20 characters:")
while True:
    part = file_parts.read(20)
    if not part:
        break
    print(part)
file_parts.close()
