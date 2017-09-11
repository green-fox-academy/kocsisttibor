# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
#
# If it is bigger it should count from the first number to the second by one
# 
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5

first = int(input("First number:"))
second = int(input("Second number:"))

if first >= second:
    print("The second number should be bigger")
else:
    while first < second:
        print(first) 
        first += 1