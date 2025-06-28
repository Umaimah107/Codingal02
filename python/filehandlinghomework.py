filename = "C:/Users/knitt/OneDrive/Desktop/New file.txt"
while True:
    print("\n1. Read file")
    print("2. Write file")
    print("3. Append to file")
    print("4. Exit")
    choice = input("Choose (1-4): ")

    if choice == "1":
        with open(filename, "r") as f:
            print(f.read())
    elif choice == "2":
        text = input("Enter text to write: ")
        with open(filename, "w") as f:
            f.write(text + "\n")
    elif choice == "3":
        text = input("Enter text to append: ")
        with open(filename, "a") as f:
            f.write(text + "\n")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")