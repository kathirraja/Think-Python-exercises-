def read(fname):
    fin = open(fname)
    for line in fin:
        word = str(line.strip())
        if len(word) > 20:
            print word,len(word)
