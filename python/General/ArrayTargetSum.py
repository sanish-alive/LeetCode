specific_sum = 21
arr = {12, 24, 16, 34, 25, 5, 25}

for num in arr:
    complement = specific_sum - num
    if complement in arr:
        print(num, complement)
