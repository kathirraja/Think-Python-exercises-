def backward(string):
    l = len(string)
    for letters in string:
        print string[l-1]
        l -= 1
