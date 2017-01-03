from swampy.TurtleWorld import *

def cricle(t,r):
    print t
    t.delay=0.01
    c = 2*(22/7)*r
    for i in range(c):
        fd(t,c)
        lt(t,(360/c))
    
world = TurtleWorld()
bob = Turtle()
radius = 4
cricle(bob,radius)
