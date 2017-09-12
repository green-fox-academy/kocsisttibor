# - Create a function called `factorio`
#   that returns it's input's factorial

def factorio(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

print(factorio(5))