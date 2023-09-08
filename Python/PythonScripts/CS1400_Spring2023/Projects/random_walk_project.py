"""
Project Name: Project 5: Random Walk
Author: Zachary Peterson
Due Date: 2023-04-14
Course: CS1400-x01

This code takes in command line arguments of
list<walk_lengths> int<trials> str<walker: Pa Mi-Ma Reg or all>
and randomly simulates a walk sequence based on the inputs
Returns:
<walker_name> random walk of <walk_length> steps
Mean = <mean> CV = <coefficient_variance>
Max = <max> Min = <min>
and a plot of movements using turtle.
"""
import random
import subprocess
import sys
import math
import statistics
import tempfile
import textwrap
import traceback
import turtle
tur = turtle.Turtle()


def save_to_image(dest='random_walk.png'):
    """Saves the turtle canvas to dest. Do not modify this cus_funcs."""
    with tempfile.NamedTemporaryFile(prefix='random_walk',
                                     suffix='.eps') as tmp:
        turtle.getcanvas().postscript(file=tmp.name)
        command = ['gs',
                   '-dSAFER',
                   '-o',
                   dest,
                   '-r200',
                   '-dEPSCrop',
                   '-sDEVICE=png16m',
                   tmp.name]
        try:
            subprocess.run(command,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT,
                           check=True)
        except Exception as exp:
            message = f'''\
            There was an error running ghostscript.

            If you are seeing this error in Codio, please report it to your instructor.
            If you are seeing this error elsewhere, consider installing ghostscript or
            replacing the call to `save_to_image()' with `turtle.done()' in your local
            copy. Be sure not to change run_doodles.py in Codio!

            The system was attempting to run the following command:
            {' '.join(command)}

            Error details:
            '''
            print(textwrap.dedent(message), file=sys.stderr)
            [_, minor, _] = sys.version.split()[0].split('.')
            minor = int(minor)
            # python version >= 3.10
            if minor >= 10:
                traceback.print_exception(type(exp), exp, exp.__traceback__)
            # python version < 3.10
            else:
                traceback.print_exception(None, exp, exp.__traceback__)


def plot():
    """
    Function to plot final locations of walkers in a turtle window
    """
    tur.stamp()
    save_to_image()


def simulate(walk_lengths, trials, walker):
    """
    Function to simulate multiple random walks of different lengths for a given walker type
    """
    screen = turtle.Screen()
    screen.setup(300, 400)
    walk_lengths = [int(i) for i in walk_lengths]
    trials = int(trials)
    if walker.lower() == 'all':
        walkers = ['Pa', 'Mi-Ma', 'Reg']
    else:
        walkers = [walker]
    for walker_type in walkers:
        for walk_length in walk_lengths:
            distances = []
            for _ in range(trials):
                x_coord, y_coord = 0, 0
                for _ in range(walk_length):
                    direction = []
                    if walker_type == 'Pa':
                        direction = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
                        shape = 'circle'
                        color = 'black'
                    elif walker_type == 'Mi-Ma':
                        direction = random.choice([(0, 1), (1, 0), (0, -1),  (0, -1), (-1, 0)])
                        shape = 'square'
                        color = 'green'
                    elif walker_type == 'Reg':
                        direction = random.choice([(1, 0), (-1, 0)])
                        shape = 'triangle'
                        color = 'red'
                    x_coord += direction[0]
                    y_coord += direction[1]
                if walk_length <= 100:
                    tur.speed('fastest')
                    tur.penup()
                    tur.shape(shape)
                    tur.color(color)
                    pixel_per_step = 5
                    tur.shapesize(0.5, 0.5)
                    tur.goto(x_coord * pixel_per_step, y_coord * pixel_per_step)
                    plot()
                distance = round(math.hypot(x_coord, y_coord), 1)
                distances.append(distance)
            mean = round(statistics.mean(distances), 1)
            stdev = round(statistics.pstdev(distances), 1)
            coefficient_of_variation = round(stdev / mean, 1)
            max_distance = max(distances)
            min_distance = min(distances)
            print(f'{walker_type} random walk of {walk_length} steps')
            print(f'Mean = {mean} CV = {coefficient_of_variation}')
            print(f'Max = {max_distance} Min = {min_distance}')
            distances.clear()


def main():
    """
    Main cus_funcs to handle command-line arguments and call the simulate() cus_funcs
    """
    args = sys.argv[1:]
    if len(args) != 3:
        raise TypeError('Invalid call... Please call as follows: '
                        'python random_walk.py '
                        '<walk_lengths> <trials> <walker: Pa Mi-Ma Reg or All>')
    walk_lengths = args[0]
    trials = args[1]
    walker_name = args[2]
    simulate(walk_lengths, trials, walker_name)


if __name__ == '__main__':
    main()
