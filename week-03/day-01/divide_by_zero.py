# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

num = int(input("Enter a number: "))

def divider(num):
    try:
        print(10 / num)
    except ZeroDivisionError:
        print("fail")
        
divider(num)