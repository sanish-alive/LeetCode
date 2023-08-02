def isAnagram(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if (sorted_str1 == sorted_str2):
        return True
    else:
        return False
    
print(isAnagram("sanish shrestha", "apple banana"))
print(isAnagram("care", "race"))
print(isAnagram("part heart", "trap earth"))
