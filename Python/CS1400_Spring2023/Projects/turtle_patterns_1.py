"""
Project Name: Turtle Patterns I
Author: Zachary Peterson
Due Date: 2023-01-18
Course: CS1400-x01

This code is for a simple turtle drawing that is dependent on
the width and height input from the user.
"""
import turtle


def get_dimensions():
    try:
        width = int(input("Enter the width:"))
        height = int(input("Enter the height:"))
        if width <= 0 or height <= 0:
            print("Width and height must be positive integers.")
        draw(width, height)

    except TypeError:
        print("Width and height must be positive integers.")


def draw(width, height):
    """
    Sets the size of the screen to width and height and draws a doodle.
    """
    turtle.speed(15)
    size = 8
    petal_line_color = "purple"
    petal_fill_color = "blue"
    stem_line_color = "white"
    stem_fill_color = "green"
    ground_line_color = "grey"
    ground_fill_color = "brown"

    turtle.Screen().setup(width, height)

    ground(size, ground_line_color, ground_fill_color, width, height)
    flower_stem(size, stem_line_color, stem_fill_color, width, height)
    flower_petals(size, petal_line_color, petal_fill_color, width, height)


def flower_petals(size, line_color, fill_color, width, height):
    petal_count = size

    turtle.color(line_color, fill_color)
    turtle.begin_fill()

    for i in range(petal_count):
        turtle.circle(((width + height) / 10) * .3)
        turtle.rt(360 / petal_count)

    turtle.end_fill()


def flower_stem(size, line_color, fill_color, width, height):
    stem_length = size * 2

    turtle.color(line_color, fill_color)

    turtle.rt(-90)
    for i in range(stem_length):
        turtle.rt(-90 / stem_length)
        turtle.begin_fill()
        for j in range(4):
            turtle.forward(((width + height) / 10) * .09)
            turtle.rt(90)
        turtle.end_fill()
        turtle.forward(((width + height) / 10) * .09)


def ground(size, line_color, fill_color, width, height):
    ground_length = size

    turtle.color(line_color, fill_color)

    for lines in range(ground_length):
        turtle.back(((width + height) / 10) * .12)

    for fill in range(ground_length * 2):
        turtle.begin_fill()
        for triangles in range(3):
            turtle.forward(((width + height) / 10) * .2)
            turtle.rt(120)
        turtle.end_fill()
        turtle.forward(((width + height) / 10) * .12)

    for lines in range(ground_length):
        turtle.back(((width + height) / 10) * .12)


get_dimensions()
