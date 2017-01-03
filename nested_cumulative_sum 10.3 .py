def nested_cumulative_sum(li):
    nl=[]
    s = 0
    for n in li:
        if type(n) is int:
            s += n
            nl.append(s)
        elif type(n) is list:
            nl.append(nested_cumulative_sum(n))
    return nl
