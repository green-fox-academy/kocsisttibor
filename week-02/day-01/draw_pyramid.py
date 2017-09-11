# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was

number = int(input("Give me a number: "))

i = 1
while i <= number:
    print(" " * (number - i) + "*" * (2 * i - 1))
    i += 1