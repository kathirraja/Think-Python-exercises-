def is_between(x,y,z):
    if(x<=y and y<=z):
        return True
    else:
        return False

x = float(raw_input('Enter x : '))
y = float(raw_input('Enter y : '))
z = float(raw_input('Enter z : '))
print is_between(x,y,z)
