import os
import time

def shutdown():
    choice = input("Do you want to shut down your computer? (yes/no)").strip().lower()

    if choice == "yes":
        print("Shutting down in five seconds....")
        time