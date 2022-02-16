# Importing turtle functions
from turtle import Turtle, colormode, done
colormode(255)

# Constructs a turtle object
leo: Turtle = Turtle()

# # Moves Turtle object forard to draw line
# leo.forward(50)
# # Turn Turtle left 30 degrees
# leo.left(90)
# leo.forward(50)
# leo.left(90)
# leo.forward(50)
# leo.left(90)
# leo.forward(50)
# leo.left(90)
# done()

# # Square
# i: int = 0
# while (i < 4):
#     leo.forward(300)
#     leo.left(90)
#     i += 1
# done()

# Triangle
leo.speed(50)
leo.hideturtle()

leo.penup()
leo.goto(-100, -100)
leo.pendown()

# leo.color("blue")
# leo.pencolor("pink")
# leo.fillcolor(32, 67, 93)
# leo.color("green", "yellow")
leo.pencolor(99, 204, 250)
leo.fillcolor(75, 75, 75)


leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()
done()