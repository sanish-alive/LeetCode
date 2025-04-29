# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def missingNumber(nums):
    result = 0
    for _ in range(len(nums)):
        if result in nums:
            result += 1
    return result
    
print(missingNumber([0, 1, 2]))