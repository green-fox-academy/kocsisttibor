# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The seconf represents the number of pigs the farmer has
# It should print how many legs all the animals have

chicken = int(input("Enter the first number (integer): "))
pig = int(input("Enter the second number (integer): "))

print("All the animals have " + str(chicken * 2 + pig * 4)  + " legs.")