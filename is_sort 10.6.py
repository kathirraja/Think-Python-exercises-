def is_sorted(li):
    for i in range(len(li)-1):
        if li[i] >= li[i+1]:
            return False
    return True
