from swampy.TurtleWorld import *

def square(t,length):
    print t
    for i in range(4):
        fd(t,length)
        lt(t)
    
world = TurtleWorld()
bob = Turtle()
length = 250
square(bob,length)
