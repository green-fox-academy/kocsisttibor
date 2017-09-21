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

    for i in set(numbers):
        numbers[numbers.index(i)] = str(numbers.count(i)) + "(" + str(i) + ")"

    print(numbers)
    # numbers.sort()

    # print("Top five numbers: " + numbers[-1] + ", "+ numbers[-2] + ", "+ numbers[-3] + ", "+ numbers[-4] + ", "+ numbers[-5])

counting()