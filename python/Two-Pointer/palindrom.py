input_string = input("Enter string :: ")
input_string = input_string.lower()
rev_string = input_string[::-1]

if input_string == rev_string:
    print("string is palindrome.")
else:
    print("string is not palindrome")