# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

number = int(input("Give me a number: "))

if number % 2 == 0:
    half = number / 2
else:
    half = number // 2 + 1

i = 1

while i <= half:
    print(" " * (number - i) + "*" * (2 * i - 1))
    i += 1

if number % 2 == 0:
    i -= 1
else:
    i -= 2

while i >= 1:
    print(" " * (number - i) + "*" * (2 * i - 1))
    i -= 1

