with open("C:/Users/knitt/OneDrive/Desktop/New file.txt", "r") as file1, \
     open("C:/Users/knitt/OneDrive/Desktop/new file453.txt", "w") as file2:
    for line in file1:
        if not line.startswith("Coding"):
            print(line, end="")
            file2.write(line)