from swampy.TurtleWorld import *

def polygon(t,length,n):
    print t
    for i in range(n):
        fd(t,length)
        lt(t,(360/n))
    
world = TurtleWorld()
bob = Turtle()
length = 50
n=5
polygon(bob,length,n)
