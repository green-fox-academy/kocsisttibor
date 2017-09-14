# Sort that list

# Create a function that takes a list of numbers as parameter
# Returns a list where the elements are sorted in ascending numerical order
# Make a second boolean parameter, if it's true sort that list descending
# Example

# input [34, 12, 24, 9, 5]
# output [5, 9, 12, 24, 34]

from random import randint

random_list = [randint(1, 10) for x in range(20)]

print("input: " + str(random_list))

random_list.sort()

print("sorted: " + str(random_list)) 