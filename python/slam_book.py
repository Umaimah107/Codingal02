slam_book_entries = []

def fill_slam_book():
    print("\n Fill the slam book!")
    name = input("Your name: ")
    nickname = input("Your Nickname:  ")
    fav_color = input("Favourite color: ")
    fav_food = input("Your favourite food:  ")
    hobby = input("Your hobby: ")



    entry = {
        "Name": name,
         "Nickname": nickname,
        "Favorite Color": fav_color,
        "Favorite Food": fav_food,
        "Hobby": hobby,
    }

    slam_book_entries.append(entry)
    print("Thankyou! Your response has been saved. \n")

def show_slam_book():
    print("\n Slam Book Entries ")
    for i in range(len(slam_book_entries)):
        print(f"\nEntry #{i + 1}")
        entry = slam_book_entries[i]
        for key, value in entry.items():
            print(f"{key}: {value}")

while True:
    print("Welcome to my slam book!")
    print("1. Fill Slam Book")
    print("2. show all entries")
    print("3. Exit")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        fill_slam_book()
    elif choice == "2":
        show_slam_book()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")