import turtle

t = turtle.Turtle()


def triangle(size):
    """Draw a triangle with a given size"""
    for i in range(3):
        t.lt(120)
        t.forward(size)


def rectangle(width, height):
    """Draw a rectangle with a given width and height"""
    for i in range(2):
        t.forward(width)
        t.lt(90)
        t.forward(height)
        t.lt(90)


def reposition(x, y):
    """Pick up the pen, move the turtle, set the
    direction of the turtle, and put the pen down"""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()


rectangle(100, 100)  # draw the house
reposition(100, 100)  # move to starting point for the roof
triangle(100)  # draw the roof
reposition(40, 0)  # move to starting point for the door
rectangle(20, 40)  # draw the door
reposition(10, 50)  # move to starting point for the left window
rectangle(20, 20)  # draw the left window
reposition(70, 50)  # move to starting point for the right window
rectangle(20, 20)  # draw the right window

turtle.mainloop()