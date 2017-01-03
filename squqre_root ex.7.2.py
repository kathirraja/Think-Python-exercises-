def squqre_root(a):
    x = 3.0
    while True:
        y = ( x + a/x )/2
        if abs(y-x) < 0.0000001:
            return y
            break
        x=y

print squqre_root(2)
