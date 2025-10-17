try:
    enter = int(input("ENTER AGE"))
    
    if enter < 0 or enter > 100:
        print(" This is an incorrect input")
    else:
        print(f"The age entered is {enter}.")
    
    if enter%2==0:
        print("Your age is an even number")
    else:
        print("Your age is an odd number")

except ValueError:
    print("Error:Please enter a valid number for your age!")
