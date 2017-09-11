# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000

a_side = 10
b_side = 20
c_side = 30

surface = 2 * (a_side * b_side) + 2 * (b_side * c_side) + 2 * (a_side * c_side)
volume = a_side * b_side * c_side

print("Surface Area: " + str(surface))
print("Volume: " + str(volume))
