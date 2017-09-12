# - Write a function called `sum` that sum all the numbers
#   until the given parameter

def sums(final_number):
    sums = 0
    for i in range(final_number + 1):
        sums += i
    return sums

print(sums(10))