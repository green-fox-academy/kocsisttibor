students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints: 
#  - how many candies they have on average

def candies(num, given_list):
    for i in range(len(given_list)):
        if given_list[i]["candies"] > num:
            print(given_list[i]["name"])

candies(4, students)

def average(given_list):
    candies = 0
    for i in range(len(given_list)):
        candies += int(given_list[i]["candies"])
    return candies / (i + 1)

print(average(students))

