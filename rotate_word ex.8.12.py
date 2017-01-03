def rotate_word(word,step):
    rot_word = ''
    for letter in word:
        l = step + ord(letter)
        if l < 97 and letter.islower():
            l = 97 - l
            l = 123 - l
        elif l > 122 and letter.islower:
            l = l - 122
            l = l + 96
        elif l <65 and letter.isupper():
            l = 65 - l
            l = 91 - l
        elif l > 90 and letter.isupper():
            l = l - 91
            l = 65 + l
        rot_word += chr(l)
    return rot_word
