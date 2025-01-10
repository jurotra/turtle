
import math
import turtle
regulus = turtle.Turtle()
print(regulus)
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """making a slight left turn before starting reduces
    the error caused by the linear approximation of the arc
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    arc(t, r, 360)


if __name__ == '__main__':
    bob = turtle.Turtle()
    """draw a circle centered on the origin
    """
    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    circle(bob, radius)

arc(regulus, 100, 90)
turtle.mainloop()