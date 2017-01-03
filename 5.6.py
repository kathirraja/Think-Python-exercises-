from swampy.TurtleWorld import *

def draw(t, x):
    t.delay=0
    if(x<3):
        fd(t,x)
        return
    draw(t,x/3.0)
    lt(t,60)
    draw(t,x/3.0)
    rt(t,120)
    draw(t,x/3.0 )
    lt(t,60)
    draw(t,x/3.0)

def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        draw(t, n)
        rt(t, 120)

world = TurtleWorld()
bob = Turtle()
snowflake(bob,100)

world.mainloop()
