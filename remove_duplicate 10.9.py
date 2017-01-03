def remove_duplicate(li):
    l = []
    for n in li:
        if n not in l:
            l.append(n)
    return l
    
