def is_triangle(a,b,c):
    if(a>b and a>c):
        check(a,b,c)
    elif(b>a and b>c):
        check(b,a,c)
    else:
        check(c,b,a)

def check(mx,x,y):
    if(mx > x+y):
        print('No, It cannot form a triangle');
    else:
        print('Yes, It can form a triangle')
    
    
a=int(raw_input('Enter Three intgers'))
b=int(raw_input())
c=int(raw_input())
is_triangle(a,b,c)

