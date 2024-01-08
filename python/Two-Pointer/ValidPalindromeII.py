def validpalindrome(s):
    l = 0
    r = len(s)-1
    while l<r:
        if s[l] == s[r]:
            l+=1
            r-=1
        else:
            return isPalindrome(s, l+1, r) or isPalindrome(s, l, r-1)
    return True

def isPalindrome(s, tl, tr):
    while tl<tr:
        if s[tl] == s[tr]:
            tl+=1
            tr-=1
        else:
            return False
    return True

print(validpalindrome("aba"))
print(validpalindrome("abca"))
print(validpalindrome("abcav"))
print(validpalindrome("pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip"))
print(validpalindrome("cbbcc"))