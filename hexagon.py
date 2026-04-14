import turtle
turtle.Screen().bgcolor("yellow")
a=turtle.Turtle()
num_side=6
side_lenght=80
angle=360.0/num_side
for i in range(num_side):
    a.forward(side_lenght)
    a.right(angle)
turtle.done()