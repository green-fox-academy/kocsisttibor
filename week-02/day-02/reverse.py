# - Create a variable named `aj`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Reverse the order of the elements in `aj`
# - Print the elements of the reversed `aj`

aj = [3, 4, 5, 6, 7]

aj.reverse()

print(aj)

ak = []

for i in range(1, len(aj)+1):
    ak.append(aj[-i])

print(ak)
