def mutate_string(string, position, character):
    newS = list(string)
    newS[position] = character
    newS = ''.join(newS)
    return newS
