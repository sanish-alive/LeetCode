a = [1, 2, 3, 4, 1, 2, 5, 6]
seen = []
duplicate = []
for i in a:
    if i in seen:
        duplicate.append(i)
        print(i)
    else:
        seen.append(i)