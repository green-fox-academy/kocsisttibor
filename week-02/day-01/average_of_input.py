# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

number_01 = int(input("Enter first number: "))
number_02 = int(input("Enter second number: "))
number_03 = int(input("Enter third number: "))
number_04 = int(input("Enter forth number: "))
number_05 = int(input("Enter fifth number: "))

summ = number_01 + number_02 + number_03 + number_04 + number_05

print("Sum: " + str(summ) + ", Average: " + str(summ / 5))
