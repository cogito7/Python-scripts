import turtle


num_sides = int(input("Enter number of sides: "))
num_length = int(input("Enter total length of the polygon: "))

angle = 360/num_sides

for i in range (0, num_sides, 1):
    turtle.forward(num_length)
    turtle.right(angle)
