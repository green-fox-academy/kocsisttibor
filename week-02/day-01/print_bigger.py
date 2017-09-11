# Write a program that asks for two numbers and prints the bigger one

number_01 = int(input("First number: "))
number_02 = int(input("Second number: "))

if number_01 > number_02:
    print("First number is bigger.")
elif number_02 > number_01:
    print("Second number is bigger.")
else:
    print("The two numbers are equal.")