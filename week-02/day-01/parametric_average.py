# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4

number = int(input("How many integers would you add?"))
sum_of_items = 0

for i in range(number):
    item = int(input("Give me a number:"))
    sum_of_items += item

print("Sum: " + str(sum_of_items) + ", Average: " + str(sum_of_items / number))