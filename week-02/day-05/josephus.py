print("Enter a number:")
num = int(input())

def josephus(num):
    seats = [i + 1 for i in range(num)]
    
    i = len(seats)
    if len(seats) % 2 == 0:
        while len(seats) > 1:
            i = len(seats)
            while i > 1:
                seats.remove(seats[i])
                i -= 2
    else:
        while len(seats) > 1:
            i = len(seats) - 1
            while i > 1:
                seats.remove(seats[i])
                i -= 2

    print(seats)


josephus(num)