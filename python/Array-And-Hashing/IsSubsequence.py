def isSubsequence(s, t):
    if len(s) == 0: return True
    i, index = 0, 0
    while index<len(t):
        if s[i] == t[index]:
            i+=1
            index+=1
            if i==len(s):
                return True
        else:
            index+=1
    return False



print(isSubsequence("b", "c"))