# Adds a and b, returns as result
def add(a, b):
    return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b:
        if b > c:
            return a
        if c > a:
            return c
    else:
        if c > b:
            return c
        else:
            return b

# Returns the median value of a list given as param
def median(pool):
    n = len(pool)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(pool)[n//2]
    else:
            return sum(sorted(pool)[n//2-1:n//2+1])/2.0

# Returns true if the param is a vovel
def is_vovel(char):
    return char.lower() in 'aeiouéáőűöüóíú'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    for char in set(teve):
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve

