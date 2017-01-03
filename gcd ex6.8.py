def gcd(a,b):
    if(a==0):
        return b
    elif(b==0):
        return a
    elif(a<=b):
        d = a
    else:
        d = b        
    d1=d
    for i in range(1,d+1):
        if (a%d1==0)and(b%d1==0):
            return d1
        d1 = d1 - 1

def gcd1(a,b):
    if(a%b==0):
        return b
    else:
        r = a%b
        if(a1%r==0) and (b1%r==0):
                return r
        else:
            return gcd1(b,r)
            
a1 = int(raw_input('Enter two numbers : '))
b1 = int(raw_input())
print gcd1(a1,b1)
