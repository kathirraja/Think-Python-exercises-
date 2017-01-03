def is_abecedarian(word):
    for i in range(0,len(word)-1):
        if not word[i]<=word[i+1]:
            return False
    return True
        
