def read(fname):
    fin = open(fname)
    for line in fin:
        word = str(line.strip())
        if has_no_e(word):
            print word

def has_no_e(string):
    if not 'e' in string:
        return True
    return False
