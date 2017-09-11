# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %   %
# %   %
# %   %
# %   %
# %%%%%
#
# The square should have as many lines as the number was

number = int(input("Give me a number: "))

print("%" * number)
for i in range(number-2):
    print("%" + " " * (number - 2) + "%")
print("%" * number)  