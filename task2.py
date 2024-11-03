# Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

# Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”.
# Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.

import turtle
from reprlib import recursive_repr

screen = turtle.Screen()  # Create the screen.
screen.setup(640, 640)  # Set Window size.

###### TURTLE SHAPE, SPEED, PEN SIZE, COLOR ######
TTL = turtle.Turtle()
TTL.speed(0)  # Set the turtle's speed. 1 is slow, 10 is fast; 0 is fastest.
TTL.color("brown")  # Set the turtle's color.
TTL.pensize(1)  # Set width of turtle drawing pen.

###### SET TURTLE STARTING POSITION ######
TTL.penup()  # Do not let the turtle draw while moving to position (0, 110).
TTL.setposition(0, -100)
TTL.pendown()  # Enable the turtle to draw.
TTL.hideturtle()
TTL.setheading(90)


def treeFractal(TTL, recursionLevel, branchLength, branchReduction, angle):
    if recursionLevel == 0:
        TTL.fd(0)
    else:
        branchLength = branchLength - branchReduction
        TTL.forward(branchLength)
        TTL.left(angle)
        treeFractal(TTL, recursionLevel - 1, branchLength, branchReduction, angle)
        TTL.right(angle * 2)
        treeFractal(TTL, recursionLevel - 1, branchLength, branchReduction, angle)
        TTL.left(angle)
        TTL.backward(branchLength)


recursive_lvl = 7
treeFractal(TTL, recursive_lvl, 50, 5, 25)

screen.exitonclick()  # Exit screen
