from swampy.TurtleWorld import *

def arc(t,r,a):
    print t
    t.delay=0.01
    c = 2*(22/7)*r*a/360
    n = (c/3)+1
    l = c/n
    a = float(a)/n
    for i in range(n):
        fd(t,l)
        rt(t,a)
    
world = TurtleWorld()
bob = Turtle()
radius = 200
angle = 360
for i in range (10):
    arc(bob,radius,360/7)
    rt(bob,360/7)
