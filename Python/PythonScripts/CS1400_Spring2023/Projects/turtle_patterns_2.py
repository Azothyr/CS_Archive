"""
Project Name: Turtle Patterns II
Author: Zachary Peterson
Due Date: 2023-03-03
Course: CS1400-x01

This code is for a simple turtle of a flower drawing within a user decided flower pot or
picture frame. The use will need to input their choice of pot or painting, screen scale,
petal count, petal color, scene color.
"""
import turtle
import argparse


def positive_int(_value):
    """Validation functions that checks if a value is a positive int"""
    try:
        value = int(_value)
        if value <= 0:
            raise argparse.ArgumentTypeError(f"{_value} is not a positive int")
    except ValueError:
        error_message = f"{_value} is not an int"
        raise argparse.ArgumentTypeError(error_message) from None
    return value


def positive_float(_value):
    """Validation functions that checks if a value is a positive float"""
    try:
        value = float(_value)
        if value <= 0:
            raise argparse.ArgumentTypeError(f"{_value} is not a positive float")
    except ValueError:
        error_message = f"{_value} is not an float"
        raise argparse.ArgumentTypeError(error_message) from None
    return value


def draw(args):
    """Sets and passes all values for drawing the scene"""
    turtle.speed(15)
    scene = args[0]
    _scale = positive_float(args[1])
    _flower_size = 4
    _petal_count = positive_int(args[2])
    _line_color = "black"
    _petal_fill_color = args[3]
    _stem_fill_color = "green"
    _ground_fill_color = "brown"
    _scene_fill_color = args[4]

    _screen_width = 500 * _scale
    _screen_height = 400 * _scale
    turtle.Screen().setup(_screen_width, _screen_height)

    if scene == 'pot':
        _ground_bool = False
        _flower_position = (0, 0)
        draw_pot(_screen_width, _screen_height, _line_color, _scene_fill_color)
    elif scene == 'painting':
        _ground_bool = True
        _flower_position = (-((_screen_width/3)-(_screen_width/5))/2), \
            -(((_screen_height/2)-(_screen_height/5))/2)
        draw_frame(_screen_width, _screen_height, _line_color, _scene_fill_color)
    else:
        raise Exception("Incorrect scene argument used. Try: pot or painting")

    draw_flower(_screen_width, _screen_height, _flower_size, _petal_count, _flower_position,
                _line_color, _ground_fill_color, _stem_fill_color, _petal_fill_color, _ground_bool)


def draw_frame(screen_width, screen_height, line_color, scene_fill_color):
    """Draws the painting frame boarder"""
    turtle.color(line_color, scene_fill_color)

    def inner_offset(_value, return_length):
        """
        Returns the inner offset of the picture frame from the 0, 0 axis of the turtle window.
        Length bool doubles the value before returning, so it will span across the x or y - and + quadrants.
        """
        half = _value / 2
        offset = _value / 3.85
        outer_offset = half - offset
        if return_length:
            outer_offset *= 2
        return outer_offset

    def outer_offset(_value, return_length):
        """
        Returns the inner offset of the picture frame from the 0, 0 axis of the turtle window.
        Length bool doubles the value before returning, so it will span across the x or y - and + quadrants.
        """
        half = _value / 2
        offset = _value / 5
        inner_offset = half - offset
        if return_length:
            inner_offset *= 2
        return inner_offset

    initial_position = (-(outer_offset(screen_width, False)), -(outer_offset(screen_height, False)))
    width_outer_length = outer_offset(screen_width, True)
    width_inner_length = inner_offset(screen_width, True)
    height_outer_length = outer_offset(screen_height, True)
    height_inner_length = inner_offset(screen_height, True)
    diagonal_length = height_inner_length / 5

    turtle.penup()
    turtle.goto(initial_position)
    turtle.pendown()
    for _ in range(2):
        turtle.begin_fill()
        turtle.forward(width_inner_length)
        turtle.rt(45)
        turtle.forward(diagonal_length)
        turtle.rt(135)
        turtle.forward(width_outer_length)
        turtle.rt(135)
        turtle.forward(diagonal_length)
        turtle.rt(45)
        turtle.forward(width_inner_length)
        turtle.lt(90)
        turtle.end_fill()
        turtle.begin_fill()
        turtle.forward(height_inner_length)
        turtle.rt(45)
        turtle.forward(diagonal_length)
        turtle.rt(135)
        turtle.forward(height_outer_length)
        turtle.rt(135)
        turtle.forward(diagonal_length)
        turtle.rt(45)
        turtle.forward(height_inner_length)
        turtle.lt(90)
        turtle.end_fill()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()


def draw_pot(screen_width, screen_height, line_color, scene_fill_color):
    """Draws the painting frame boarder"""
    turtle.color(line_color, scene_fill_color)
    w_4th = screen_width/4
    w_5th = screen_width/5
    w_30th = screen_width/30
    h_4th = screen_height/4
    h_7th = screen_height/7

    orig_move_list = [w_4th, h_7th, w_30th, h_4th]
    move_reversed = orig_move_list[::-1]
    move_list = orig_move_list + [w_5th] + move_reversed
    orig_turn_list = [100, 80, 280, 80]
    turn_reversed = orig_turn_list[::-1]
    turn_list = orig_turn_list + turn_reversed

    turtle.begin_fill()
    for i in range(len(turn_list)):
        turtle.forward(move_list[i])
        turtle.rt(turn_list[i])
    turtle.forward(move_list[8])
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()


def draw_flower(screen_width, screen_height, flower_size, petal_count, flower_position,
                line_color, ground_fill_color, stem_fill_color, petal_fill_color, ground_bool):
    """Draws the full flower. Broken up into nested functions"""
    turtle.penup()
    turtle.goto(flower_position)
    turtle.pendown()

    def flower_petals():
        """Portion of parent functions that draws petals"""
        turtle.color(line_color, petal_fill_color)
        turtle.begin_fill()

        for _ in range(petal_count):
            turtle.circle(((screen_width + screen_height) / 16) * .3)
            turtle.rt(360 / petal_count)

        turtle.end_fill()

    def flower_stem():
        """Portion of parent functions that draws the stem"""
        stem_length = flower_size * 2

        turtle.color(line_color, stem_fill_color)

        turtle.rt(-90)
        for _ in range(stem_length):
            turtle.rt(-90 / stem_length)
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(((screen_width + screen_height) / 10) * .09)
                turtle.rt(90)
            turtle.end_fill()
            turtle.forward(((screen_width + screen_height) / 10) * .09)

    def ground():
        """Portion of parent functions that draws the dirt"""
        ground_length = flower_size

        turtle.color(line_color, ground_fill_color)

        for lines in range(ground_length):
            turtle.back(((screen_width + screen_height) / 10) * .12)

        for _ in range(ground_length * 2):
            turtle.begin_fill()
            for _ in range(3):
                turtle.forward(((screen_width + screen_height) / 10) * .2)
                turtle.rt(120)
            turtle.end_fill()
            turtle.forward(((screen_width + screen_height) / 10) * .12)

        for _ in range(ground_length):
            turtle.back(((screen_width + screen_height) / 10) * .12)
    if ground_bool:
        ground()
    flower_stem()
    flower_petals()
