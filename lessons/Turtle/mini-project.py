from turtle import Turtle, colormode, done
colormode(255)

leo: Turtle = Turtle()
leo.speed(50)
leo.hideturtle()
leo.penup()
leo.goto(-100, -100)
leo.pendown()
leo.pencolor(99, 204, 250)
leo.fillcolor(200, 200, 200)

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()


bob: Turtle = Turtle()
bob.pencolor(0, 0, 0)
bob.penup()
bob.goto(-100, -100)
bob.pendown()
bob.speed(100)

side_length: float = 300

i: int = 0
while (i < 60):
    bob.forward(side_length)
    bob.left(121)
    i += 1
    side_length = side_length * 0.97

done()