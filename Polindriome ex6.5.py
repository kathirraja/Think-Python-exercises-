def is_polindrome(word):
    flag = 1
    for i in range (0,len(word)/2):
        if(word[i] != word[-i-1]):
            flag = 0
            break
    if(flag == 1):
        return True
    else:
        return False

print is_polindrome(str(raw_input('Enter a word : ')))

