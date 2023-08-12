def productExceptSelf(nums):
    l = len(nums)
    prefix = 1
    postfix = 1
    result = [1]*l

    for i in range(l):
        result[i] = prefix
        prefix *= nums[i]
    for i in range(l-1, -1, -1):
        result[i] *= postfix 
        postfix *= nums[i]
        
    return result
        

print(productExceptSelf([1,2,3,4]))