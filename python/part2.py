with open("C:/Users/knitt/OneDrive/Desktop/new file453.txt", "r") as file:
    data = file.readlines()
    print("Words in this file are.......")
    for line in data:
        word = line.split()
        print(word)
file.close        