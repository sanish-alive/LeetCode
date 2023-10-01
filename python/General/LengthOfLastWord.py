def lengthLastWord(s):
    l = s.split()
    return len(l[-1])

print(lengthLastWord("hello world "))