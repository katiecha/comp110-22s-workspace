"""EX04 - Draws a space scene! Break up complex functions - lines 221, 229, 237, 245, 253: Used draw_polygon function within draw_earth function to break up complexity. Try something fun: lines 84, 150, 158, 190, 206: Used circle() function to draw circles | line 17: Used Screen() function to create background | lines 22-25, 28-31, 43-46: Used loops to duplicate parts of my drawing | lines 24, 30, 45, 81: Used randint to randomly generate locations or colors."""

from random import randint
from turtle import Turtle, colormode, done, tracer, update
import turtle

__author__ = "730460523"
colormode(255)
MAX_SPEED: int = 0


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)
    katie: Turtle = Turtle()
    # Setting background color to black and defining size.
    turtle.Screen().screensize(500, 500, "black")
    katie.speed(MAX_SPEED)
    katie.hideturtle()

    # Drawing 500 randomly sized stars.
    ind: int = 0
    while ind < 500:
        draw_star(katie, randint(-500, 500), randint(-500, 500), randint(5, 15))
        ind += 1

    # Drawing randomly sized and colored planets.
    ind = 0
    while ind < 6:
        draw_planet(katie, randint(-450, 450), randint(-450, 450), randint(50, 65))
        ind += 1
    
    # Drawing one moon.
    draw_moon(katie, -200, -200, 30)

    # Drawing earth.
    draw_earth(katie, -300, -300, 45, 5)

    # Drawing a rocket ship.
    draw_rocket(katie, 0, 0, 20)

    # Drawing astronauts around th rocket ship.
    ind = 0
    while ind < 3:
        draw_astro(katie, randint(-60, 60), randint(-60, 60), 5)
        ind += 1
    
    update()
    done()


def draw_star(a_turtle: Turtle, x: float, y: float, length: float) -> None:
    """Draws a star with a side of a certain length in yellow."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()

    # Setting the pen color to yellow and the fill color to yellow.
    a_turtle.pencolor(253, 218, 13)
    a_turtle.fillcolor(253, 218, 13)

    a_turtle.begin_fill()
    index1: int = 0
    while index1 < 5:
        a_turtle.right(144)
        a_turtle.forward(length)
        index1 += 1
    a_turtle.end_fill()


def draw_planet(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draws a planet of a certain radius and random color."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()

    # Setting the pen color to white and the fill color to a random color.
    a_turtle.pencolor(255, 255, 255)
    a_turtle.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))

    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()


def draw_rocket(a_turtle: Turtle, x: float, y: float, base: float) -> None:
    """Draws a rocket of a certain size based on the base length in a grey color."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()

    # Setting the pen color to white and the fill color to a dark grey.
    a_turtle.pencolor(255, 255, 255)
    a_turtle.fillcolor(75, 75, 75)

    # Drawing a rectangle.
    a_turtle.begin_fill()
    index2: int = 0
    while index2 < 2:
        a_turtle.forward(base)
        a_turtle.right(90)
        a_turtle.forward(base * 2)
        a_turtle.right(90)
        index2 += 1
    a_turtle.end_fill()
    
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()

    # Drawing a triangle.
    a_turtle.begin_fill()
    index2 = 0
    while index2 < 3:
        a_turtle.forward(base)
        a_turtle.left(120)
        index2 += 1
    a_turtle.end_fill()

    # Drawing red lines beneath the rocket to represent motion.
    index2 = 0
    while index2 < 4:
        a_turtle.penup()
        a_turtle.goto(x + index2 * (base / 3), y - base * 2)
        a_turtle.setheading(0.0)
        a_turtle.pendown()
        a_turtle.pencolor("red")
        a_turtle.left(270)
        a_turtle.forward(base)
        index2 += 1


def draw_astro(a_turtle: Turtle, x: float, y: float, head: float) -> None:
    """Draws an astronaut of a certain size based on the head radius in a grey color."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()

    # Drawing the astronaut head.
    # Setting the pen color to white and the fill color to a light grey.
    a_turtle.pencolor(255, 255, 255)
    a_turtle.fillcolor(200, 200, 200)

    a_turtle.begin_fill()
    a_turtle.circle(head)
    a_turtle.end_fill()

    # Setting the pen color to white and the fill color to a medium grey.
    a_turtle.pencolor(255, 255, 255)
    a_turtle.fillcolor(100, 100, 100)

    a_turtle.begin_fill()
    a_turtle.circle(head - 2)
    a_turtle.end_fill()

    # Drawing the astronaut body.
    a_turtle.penup()
    a_turtle.goto(x - (head / 2), y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()

    a_turtle.begin_fill()
    index3: int = 0
    while index3 < 2:
        a_turtle.forward(head)
        a_turtle.right(90)
        a_turtle.forward(head * 2)
        a_turtle.right(90)
        index3 += 1
    a_turtle.end_fill()


def draw_moon(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draws a moon of a certain radius in a white color."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()

    # Setting the pen color to white and the fill color to a dark white.
    a_turtle.pencolor(255, 255, 255)
    a_turtle.fillcolor(250, 250, 250)

    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()


def draw_earth(a_turtle: Turtle, x: float, y: float, radius: float, sides: int) -> None:
    """Draws an earth of a certain radius in blue and green."""
    # Setting the pen color to white and the fill color to blue.
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.pencolor(255, 255, 255)
    a_turtle.fillcolor("blue")  

    # Drawing base circle for earth in blue to represent water.
    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()

    # Setting fill color to green.
    # Adding details to base circle in green to represent land.
    a_turtle.penup()
    a_turtle.fillcolor("green") 
    a_turtle.pendown()

    poly_len: int = int(radius) // 2
    a_turtle.penup()
    a_turtle.goto(-275, -250)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.begin_fill()
    draw_polygon(a_turtle, poly_len, sides)
    a_turtle.end_fill()

    a_turtle.penup()
    a_turtle.goto(-290, -290)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.begin_fill()
    draw_polygon(a_turtle, poly_len, sides)
    a_turtle.end_fill()

    a_turtle.penup()
    a_turtle.goto(-315, -230)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.begin_fill()
    draw_polygon(a_turtle, poly_len, sides)
    a_turtle.end_fill()

    a_turtle.penup()
    a_turtle.goto(-315, -250)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.begin_fill()
    draw_polygon(a_turtle, poly_len, sides)
    a_turtle.end_fill()

    a_turtle.penup()
    a_turtle.goto(-320, -290)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.begin_fill()
    draw_polygon(a_turtle, poly_len, sides)
    a_turtle.end_fill()


def draw_polygon(a_turtle: Turtle, radius: float, sides: int) -> None:
    """Draws a polygon with n number of sides and a certain radius."""
    index5: int = 0
    while index5 < sides:
        a_turtle.forward(radius * 0.4)
        a_turtle.left(360 / sides)
        index5 += 1


if __name__ == "__main__":
    main()