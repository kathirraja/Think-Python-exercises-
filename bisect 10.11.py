def bisect(slist,word):
    l = len(slist)
    hl = l/2
    if slist[hl] is word:
        return l
    elif slist[hl] < word:
        return l - bisect(slist[hl:],word)
    else:
        return l + bisect(slist[:hl],word)
