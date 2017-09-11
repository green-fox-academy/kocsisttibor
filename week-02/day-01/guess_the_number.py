# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8

stored_number = 7
guess = None

while guess != stored_number:
    guess = int(input("Guess: "))
    if guess < stored_number:
        print("The stored number is higher")
    elif guess > stored_number:
        print("The stored number is lower")
    else:
        print("You found the number: " + str(stored_number))