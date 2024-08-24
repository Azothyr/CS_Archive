"""
A runner for the turtle project.
"""

import argparse
import turtle
from PythonScripts.CS1400_Spring2023.Projects import turtle_patterns_2


def positive_int(_value):
    """Validation functions that checks if a value is a positive int"""
    try:
        value = int(_value)
        if value <= 0:
            raise argparse.ArgumentTypeError(f"{_value} is not a positive int")
    except ValueError:
        raise argparse.ArgumentTypeError(f"{_value} is not an int")
    return value


def positive_float(_value):
    """Validation functions that checks if a value is a positive float"""
    try:
        value = float(_value)
        if value <= 0:
            raise argparse.ArgumentTypeError(f"{_value} is not a positive float")
    except ValueError:
        raise argparse.ArgumentTypeError(f"{_value} is not an float")
    return value


def main():
    parser = argparse.ArgumentParser(
        prog='Turtle Patterns II',
        description='A driver for the Turtle Patterns II project'
    )
    parser.add_argument('-o', '--open',
                        action='store_true',
                        help='Keep the image open when done')
    parser.add_argument('scene', choices=['pot', 'painting'], default='painting',
                        help='the scene to draw (choices= \'pot\' or \'painting\', default=\'painting\')')
    parser.add_argument('--scale', nargs=1, type=positive_float, default=1.00,
                        help='the dimensions of the output (default=1)')
    parser.add_argument('--outer_color', type=str, default='brown',
                        help='the color of the scene (default=\'brown\')')
    parser.add_argument('--petal_color', type=str, default='blue',
                        help='the color of the flower (default=\'blue\')')
    parser.add_argument('--petal_count', type=positive_int, default=5,
                        help='the flower\'s petal count (default=5)')
    """parser.add_argument('arguments',
                        metavar='A',
                        type=str,
                        nargs='+',
                        help='One or more arguments to change your drawing')"""
    args = parser.parse_args()
    # turtle_patterns_2.draw(args.arguments)
    turtle_patterns_2.draw(args)
    if args.open:
        turtle.done()


if __name__ == '__main__':
    main()