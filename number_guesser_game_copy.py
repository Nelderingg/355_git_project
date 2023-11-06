import random

top_of_range = input("type a number ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

if top_of_range <= 0:
    print("enter a number greater than zero")

else:
    print("please enter a number ")



random_number = random.randrange(top_of_range)
guesses = 0

while True:
    user_guess = input("make a guess: ")
    guesses += 1

    if user_guess.isdigit:
        user_guess = int(user_guess)
        

    else:
        print("please enter a number")
        continue 

    if user_guess == random_number:
        print("correct ")
        break
    elif user_guess > random_number:
            print("you were above the number ")
    else:
        print("you were below the number ")

print("you got it in ", guesses, " guesses")


