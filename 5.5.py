from swampy.TurtleWorld import *
def draw(t, length, n):
    t.delay=0
    if(n==0):
        return
    angle = 15
    fd(t, length/n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t,length*n)

world = TurtleWorld()
bob = Turtle()
draw(bob,30,7)
wait_for_user()
