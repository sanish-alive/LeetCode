def removeDuplicate(nums):
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            nums.pop(i)
        else:
            i+=1
    return len(nums)


print(removeDuplicate([0,0]))