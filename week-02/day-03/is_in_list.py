# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]

def in_list(guess):
    in_list = False
    for i in guess:
        if i in list_of_numbers:
            in_list = True
        else:
            in_list = False
            break
    return in_list

guess = [int(i) for i in input("Enter a list of numbers separated by space: ").split()]

print(in_list(guess))
