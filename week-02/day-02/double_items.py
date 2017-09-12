# - Create an array variable named `ag`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Double all the values in the array

ag = [3, 4, 5, 6, 7]
agn = []
agn2 = []

for i in range(len(ag)):
    agn.append(ag[i] * 2)

print(agn)

for i in ag:
    agn2.append(i * 2)

print(agn2)