# Guess my number

# Exercise

# Write a program where the program chooses a number between 1 and 100. The player is then asked to enter a guess. If the player guesses wrong, then the program gives feedback and ask to enter an other guess until the guess is correct.

# Make the range customizable (ask for it before starting the guessing).
# You can add lives. (optional)

import random

def creates_random():
    print("First please set the range, where the random will be chosen from")
    first = int(input("From: "))
    last = int(input("To: "))
    num = random.randint(first, last)
    print(num)
    return num

def play(num):
    tries = 1
    guess = ""
    while guess != num:
        guess = int(input("Guess:"))
        if guess > num:
            print("Too high.")
        elif guess < num:
            print("Too low.")
        else: 
            print("Congrats! " + str(num) + " was the number")

play(creates_random())
    



