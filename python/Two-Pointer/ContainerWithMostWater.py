def maxAreaBruteForce(height):
    res = 0
    
    for l in range(len(height)):
        for r in range(l+1, len(height)):
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)
    return res

def maxArea(height):
    res = 0
    left = 0
    right = len(height) - 1

    while left < right:
        if height[left] < height[right]:
            area = (right-left) * height[left]
            left += 1
        else:
            area = (right-left) * height[right]
            right -= 1
        res = max(area, res)
    return res


print(maxAreaBruteForce([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,8,6,2,5,4,8,3,7]))