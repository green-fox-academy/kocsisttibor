newlist = [x * x for x in range(10) if x % 2 == 0]
newlist2 = [x for x in range(5, 35, 3)]

print(newlist)
print(newlist2)

af = [ 4, 5, 6, 7, 8]

af = [x * 2 for x in af]

print(af)

bs = ["b" for b in range(4)]

print(bs)

bsa = [b + "a" for b in bs]

print(bsa, end = " ")