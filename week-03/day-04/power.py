# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def power(num, exponent):
    if exponent == 1:
        return num
    else:
        return num * power(num, exponent - 1)

print(power(2, 10))