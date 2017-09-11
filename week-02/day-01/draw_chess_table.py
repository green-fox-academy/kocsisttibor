# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#

number = int(input("Give me a number: "))

for i in range(number):
    if i == 0 or i % 2 == 0:
        print("% " * number)
    else:
        print(" %" * number)