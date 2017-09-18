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

def counting(numbers):
    topfive = [0, 0, 0, 0, 0]
    for i in set(numbers):
        if numbers.count(i) > int(topfive[4]):
            if numbers.count(i) > int(topfive[3]):
                if numbers.count(i) > int(topfive[2]):
                    if numbers.count(i) > int(topfive[1]):
                        if numbers.count(i) > int(topfive[0]):
                            topfive[0] = i
                        else:
                            topfive[1] = i
                    else:
                        topfive[2] = i
                else:
                    topfive[3] = i
            else:
                topfive[4] = i
    print(topfive)

counting(gathering())