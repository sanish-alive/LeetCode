input_string = input("Enter string :: ")
count = 0
find = "a"
for i in input_string:
    if i == find:
        count += 1
print(f"Occurrence of 'a' in string is {count}")