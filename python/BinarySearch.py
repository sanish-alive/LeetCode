def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

nums = [-1, 0, 3, 5, 9, 12, 13, 16, 19, 22, 33, 35, 39, 41, 65]
target = 41
result = search(nums, target)
print(result)