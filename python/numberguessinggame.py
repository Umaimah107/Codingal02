import random
num=random.randint(1,10)
name = (input("Enter name"))
print("Welcome",name)
while True: 
    num_guesses=0
    while(num_guesses<5):
        user=int(input("Welcome to the number guessing game. Enter your guess from (1-10)"))
        num_guesses+=1

        if user<num:
            print("Your guess is too low")
        if user>num:
            print("Your guess is too high") 
        if user==num:
            break

    if num==user:
            print("Yay! You guessed the number in",num_guesses,"tries")
            answer=input("Would you like to play again?(y/n)")
            if answer=='n':
             break
    else:
        print("Aww. You couldnt guess the number. It was", num) 