def uses_only(word,rqlet):
    for letter in word:
        if not letter in rqlet:
            return False
    return True
