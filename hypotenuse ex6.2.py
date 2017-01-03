def hypotenuse(leg1,leg2):
    return (leg1**2+leg2**2)**.5

l1 = float(raw_input('Enter leg1    : '))
l2 = float(raw_input('Enter leg2    : '))
print 'hypotenuse of right triangle is = ',hypotenuse(l1,l2)
