students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

# create a function that takes a list of students and prints: 
# - how many candies are owned by students

# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies

def candy():
    for i in range(len(students)):
        print(students[i]["name"] + ": " + str(students[i]["candies"]))

candy()

def sum_candy():
    sumcandy = 0

    for i in range(len(students)):
        if students[i]["candies"] < 5:
            sumcandy += 1

    print("Number of students with less than 5 candies:" + str(sumcandy))

sum_candy()

