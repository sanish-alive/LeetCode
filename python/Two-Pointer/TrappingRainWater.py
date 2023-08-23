def trap(height):
    if not height: return 0
    result = 0
    left, right = 0, len(height) - 1
    maxLeft, maxRight = height[left], height[right]

    while left < right:
        if maxLeft < maxRight:
            left += 1
            maxLeft = max(height[left], maxLeft)
            result += maxLeft - height[left]
        else:
            right -= 1
            maxRight = max(maxRight, height[right])
            result += maxRight - height[right]
            
    return result


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))