'''
Ex 9.9
'''

def find_num():
    i = 0
    while True:
        if i > 999999:
            break
        n = i
        w = make_6digits(n);
        if is_polindrome(w[2:]):
            n += 1
            w = make_6digits(n);
            if is_polindrome(w[1:]):
                n += 1
                w = make_6digits(n);
                if is_polindrome(w[1:5]):
                    n += 1
                    w = make_6digits(n);
                    if is_polindrome(w):
                        n = int(w)
                        print n-3                        
        i = i+1
def make_6digits(n):
    w = str(n)
    l = len(w)
    if l<6:
        l = 6 - l
        o = ''
        for i in range (0,l):
            o += '0'
            w = o + w
        return w
    else:
        return w
    

def is_polindrome(word):
    flag = 1
    for i in range (0,len(word)/2):
        if(word[i] != word[-i-1]):
            return False
            break
    return True


print find_num()

