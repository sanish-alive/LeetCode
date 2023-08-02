# def isVowel(str):
#     vowel_count = 0
#     consonant_count = 0
#     vowel = "aeiou"
#     for char in str.lower():
#         if char in vowel:
#             vowel_count += 1
#         elif char.isalpha():
#             consonant_count += 1
#     return vowel_count, consonant_count

# user_string = input("Enter text :: ")
# v, w = isVowel(user_string)
# print(f"Vowel: {v} and consonant : {w}");


def isVowel(str):
    vowel_count = 0
    consoant_count = 0
    vowel = "aeiou"
    for char in str:
        if char in vowel:
            vowel_count += 1
        elif char.isalpha():
            consoant_count += 1
    return vowel_count, consoant_count

user_input = input("Enter text :: ")
v, c = isVowel(user_input.lower())
print(f"Vowel: {v} and Consonant: {c}")