#from swampy.TurtleWorld import *
from turtle import *
def circle(r):
    c=(22.0/7)*2*r
    side = c / 360
    for i in range (360):
        fd(side)
        lt(1)

#world = TurtleWorld()
#bob = Turtle()
for i in range(15):
    circle((i+1)*5)
