import turtle
import math
bob = turtle.Turtle()
alice = turtle.Turtle()
print(bob)
print(alice)
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
#desenha n segmentos de reta com o comprimento length e com angulo entre eles

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)
#desenha um poligono com n quantidades de lados e lado com comprimento length

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle= float(angle) / n
    polyline(t, n, step_length, step_angle) 
#desenha um segmento de arco de (angle) tamanho e raio r

def circle(t, r):
    arc(t, r, 360)     
#desenha um circulo de raio r

circle(bob, 100)
turtle.mainloop()
