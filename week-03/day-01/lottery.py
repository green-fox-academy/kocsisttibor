# Create a method that find the 5 most common lottery numbers otos.csv

def gathering():
    with open("hatos.txt", "r") as f:
        lines = f.read().splitlines()
    numbers = []
    for line in lines:
        parts = line.split("Ft;")
        for i in parts[-1].split(";"):
            numbers.append(i)
    return numbers

def counting():
    numbers = gathering()
    uniques = list(set(numbers))
    top_five = {}

    occurances = []

    for i in range(len(uniques)):
        occurances.append(numbers.count(uniques[i]))

    for i in range(5):
        top_five[uniques[occurances.index(max(occurances))]] = max(occurances)
        uniques.remove(uniques[occurances.index(max(occurances))])
        occurances.remove(max(occurances))

    print(top_five)


counting()