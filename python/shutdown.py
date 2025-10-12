import os
import time

def shutdown():
    choice = input("Do you want to shut down your computer? (yes/no): ").strip().lower()

    if choice == "yes":
        print("Shutting down in 5 seconds...")
        time.sleep(5)
        os.system("shutdown /s /t 1")

    elif choice == "no":
        print("Shutdown aborted.")

    else:
        print("Sorry, this is an invalid response.")

shutdown()
