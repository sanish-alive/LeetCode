def isAlpaNum(c):
    if (ord(c) >= 65 and ord(c)<=90) or \
    (ord(c) >= 97 and ord(c) <= 122):
        return True
    return False

def isPalindrome(s):
    s = [char.lower() for char in s if isAlpaNum(char)]
    f = 0
    l = len(s) - 1

    while f <= l:
        if s[f] != s[l]:
            return False
        f += 1
        l -= 1
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))