# hint: https://www.youtube.com/watch?v=uCsD3ZGzMgE

print("Enter a number:")
num = int(input())

def power(num):
    i = 0
    while 2 ** i <= num:
        i += 1
    return i - 1


def josephus(num, power):
    odds = num - 2 ** power
    return odds * 2 + 1 


print(josephus(num, power(num)))