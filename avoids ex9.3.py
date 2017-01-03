def avoid(word,fblet):
    l = len(fblet)
    for letter in fblet:
        if letter in word:
            return False
    return True
