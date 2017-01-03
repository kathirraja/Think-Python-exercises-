def is_anagram(str1,str2):
    word1 = list(str1)
    word2 = list(str2)
    if(len(word1)==len(word2)):
        for letter in word1:
            if letter in word2:
                word2.remove(letter)
            else:
                return False
        if len(word2)==0:
            return True
    else:
        return False

