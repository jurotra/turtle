import turtle
import math
bob = turtle.Turtle()
alice = turtle.Turtle()

def polyline(t, n, length, angle):
    """
    desenha n segmentos de reta com o comprimento length e com angulo entre eles
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """
    desenha um poligono com n quantidades de lados e lado com comprimento length
    """
    angle = 360.0 / n
    polyline(t, n, length, angle)
 

def arc(t, r, angle):
    """
    desenha um segmento de arco de (angle) tamanho e raio r
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle= float(angle) / n
    polyline(t, n, step_length, step_angle) 



def circle(t, r):
    """
    desenha um circulo de raio r
    """
    arc(t, r, 360)     


circle(bob, 100)
turtle.mainloop()
