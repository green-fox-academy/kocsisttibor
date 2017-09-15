def source():
    print("Enter a number: ")
    num = list(input())
    return num


def power(num):    
    output = 0
    for i in num:
        output += int(i) ** len(num)
    return int(output)


def answer():
    user_input = source()
    if int("".join(user_input)) == power(user_input):
        print("".join(user_input) + " is an Armstrong number")
    else:
        print("".join(user_input) + " is not an Armstrong number")

answer()
