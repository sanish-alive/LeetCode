def canConstruct(ransomNote, magazine):
    ran = dict()
    mag = dict()
    for word in ransomNote:
        if word not in magazine:
            return False
        elif word in ran.keys():
            ran[word]+=1
        else:
            ran[word] = 1
        
    for word in magazine:
        if word in mag.keys():
            mag[word]+=1
        else:
            mag[word] = 1
    for word in ran.keys():
        if ran[word] > mag[word]:
            return False
    return True

print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))
print(canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))
