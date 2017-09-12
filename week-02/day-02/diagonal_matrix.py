# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

def matrix(num):
    outer = []
    for i in range(num):
        inner = []
        for j in range(num):
            if j == i:
                inner.append(1)
            else:
                inner.append(0)
        outer.append(inner)
    return(outer)
    
for l in matrix(4):
    print(l)

for i, l in zip(range(4), matrix(4)):
    print(i , l)