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

def candy(given_list):
    for i in range(len(given_list)):
        print(given_list[i]["name"] + ": " + str(given_list[i]["candies"]))

candy(students)

def sum_candy(given_list):
    sumage = 0

    for i in range(len(given_list)):
        if given_list[i]["candies"] < 5:
            sumage += given_list[i]["age"]

    print("Sum of age of students with less than 5 candies:" + str(sumage))

sum_candy(students)

