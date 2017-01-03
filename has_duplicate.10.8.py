def has_duplicate(li):
    l = []
    l += li
    for n in li:
        l.remove(n)
        if n in l:
            return True
    return False
    
