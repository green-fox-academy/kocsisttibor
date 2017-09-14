# Unique - remove the duplicates

# Create a function that takes a list of numbers as a parameter
# Returns a list of numbers where every number in the list occurs only once
# Example

# input: [1, 11, 34, 11, 52, 61, 1, 34]
# output: [1, 11, 34, 52, 61]

from random import randint

random_list = [randint(1, 10) for x in range(20)]

print("input: " + str(random_list))

def unique(given_list):
    newlist = []
    for i in given_list:
        if i not in newlist:
            newlist.append(i)
    return newlist

print("output: " + str(unique(random_list)))
print("\nB-option output: " + str(set(random_list)))