# Without built-in function
# Input = Hello World!
# Output = !dlroW olleH

def stringLength(s):
    index = 0
    for _ in s:
        index+=1
    return index

def stringToList(s):
    lst = [0] * stringLength(s)
    i = 0
    for ch in s:
        lst[i] = ch
        i+=1
    return lst

def listToString(lst):
    s = ''
    for ch in lst:
        s += ch
    return s

def reverseString(s):
    lst = stringToList(s)
    l = 0
    r = stringLength(lst) - 1
    while l < r:
        lst[l], lst[r] = lst[r], lst[l]
        l+=1
        r-=1
    return listToString(lst)

s = "Hello World!"
print(reverseString(s))
print(s[:])
print(s[::-1])
print([s] * 12)
