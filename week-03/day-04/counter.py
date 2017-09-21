# Write a recursive function that takes one parameter: n and counts down from n.

def counter(num):
    if num == 0:
        return 0
    else:
        return counter(num - 1)

print(counter(10))