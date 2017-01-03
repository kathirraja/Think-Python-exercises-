def capitalize_all(li):
    nl = []
    for l in li:
        if type(l) is str:
            nl.append(l.capitalize())
        if type(l) is list:
            nl.append(capitalize_all(l))
    return nl
        
