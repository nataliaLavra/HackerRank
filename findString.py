def count_substring(string, sub_string):
    stComb = []
    count = 0
    for st in range(len(string) - len(sub_string) + 1):
        stComb.append(string[st:st+len(sub_string)])
    for st in stComb:
        if st == sub_string:
            count+=1
    
    return count
