# Find the part of int

# Create a function that takes a number and a list of numbers as a parameter
# Returns the indeces of the numbers in the list where the first number is part of
# Returns an empty list if the number is not part any of the numbers in the list
# Example

# input: [1, 11, 34, 52, 61], 1
# output: [0, 1, 4]

def int_finder (in_list, num):
    output = []
    for i in range(len(in_list)):
        if str(num) in str(in_list[i]):
            output.append(i)
    return output

list_a = [2, 3, 24, 55, 33, 53, 1, 2, 3]
number = 3

print(int_finder(list_a, number))

