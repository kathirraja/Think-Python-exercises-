def nested_sum(li):
    t = 0
    for n in li:
        if type(n) == int:
            t += n
            print t
        elif type(n) == list:
            print n
            t += nested_sum(n)
    return t

