# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

def number_adder(num):
    if num == 1:
        return 1
    else:
        return num + number_adder(num - 1)

print(number_adder(7))