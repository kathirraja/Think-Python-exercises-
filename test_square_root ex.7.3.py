import math

def test_square_root():
    for i in range(1,10):
        print i, square_root(i), math.sqrt(i),abs(square_root(i)-math.sqrt(i))

def square_root(a):
    x = 3.0
    while True:
        y = ( x + a/x )/2
        if abs(y-x) < 0.0000001:
            return y
            break
        x=y

test_square_root()

