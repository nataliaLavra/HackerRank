def swap_case(s):
    newWord = ''
    for word in s:
        if word in 'ABCDEFGHIJKLMNOPQRSTUVXZYW':
            newWord+=word.lower()
        elif word in 'abcdefghijklmnopqrstuvxzyw':
            newWord+=word.upper()
        else:
            newWord+=word
    return newWord
