# Create a method that find the 5 most common lottery numbers otos.csv

def importing(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()

def collecting(filename):
    numbers = []
    for line in importing(filename):
        parts = line.split("Ft;")
        for i in parts[-1].split(";"):
            numbers.append(i)
    return numbers

def counting(filename):
    numbers = collecting(filename)
    uniques = list(set(numbers))
    occurrences = []
    top_five = {}

    for i in range(len(uniques)):
        occurrences.append(numbers.count(uniques[i]))

    for i in range(5):
        number = uniques[occurrences.index(max(occurrences))]
        top_five[number] = max(occurrences)
        uniques.remove(number)
        occurrences.remove(max(occurrences))

    return top_five

print(counting("otos.txt"))
