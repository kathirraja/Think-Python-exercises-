from swampy.TurtleWorld import *
import math
def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        rt(t, angle)

def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_len = 2 * math.pi *r * angle / 360
    n = int(arc_len / 3) + 1
    s_len = arc_len / n
    s_ang = float(angle) / n
    polyline(t, n, s_len, s_ang)

def circle(t, r):
    arc(t, r, 360)

w = TurtleWorld()
bob = Turtle()
bob.delay = 0
for i in range(8):
    arc(bob, 200, 120)
    rt(bob, (180-120)+(360.0/4))
