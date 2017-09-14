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

# solution without .sort()

def sorter (in_list):
    for i in range(len(in_list)):
        for j in range(len(in_list)-1-i):
            if in_list[j] > in_list[j + 1]:
                in_list[j], in_list[j + 1] = in_list[j + 1], in_list[j]
    return in_list

print("sorted without .sort(): " + str(sorter(random_list)))
