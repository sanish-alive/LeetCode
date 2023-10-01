def strStr(haystack, needle):
    nlen = len(needle)
    hlen = len(haystack)
    i = 0
    while i+nlen<=hlen:
        if(needle[0] == haystack[i] and needle == haystack[i:i+nlen]):
            return i
        i+=1
    return -1

print(strStr("leetcode", "leeto"))