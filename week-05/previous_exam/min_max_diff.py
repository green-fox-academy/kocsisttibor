# Create a function called `min_max_diff` that takes a list of numbers as parameter
# and returns the difference between maximum and minimum values in the list
# Create basic unit tests for it with at least 3 different test cases

def min_max_difference(list_of_numbers):
    try:
        return max(list_of_numbers) - min(list_of_numbers)
    except ValueError:
        return "Add list of numbers as argument."

min_max_difference([])
